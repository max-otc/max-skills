#!/usr/bin/env python3
"""Scenario tests for the max-merge skill.

Each test builds throwaway git repos in a new temp dir and checks one rule of
../SKILL.md under parallel sessions and sub-agents: two sessions in one tree,
a sub-agent in its own worktree, a push race during the merge, merged, dirty
and parked branches. Where SKILL.md gives a command or a check, the test runs
that command. test_skill_quotes_each_command fails when SKILL.md drops one.

Stdlib and git only. No network. Each test removes its temp dir.
Run: python3 tests/test_scenarios.py   (exit 0 = every rule holds)
"""
import os
import re
import shutil
import subprocess
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, '..', 'SKILL.md')) as fh:
    SKILL_TEXT = fh.read()

MTIME_MIN = 30    # E-active: file mtime or reflog entry < 30 min old
GITMETA_MIN = 15  # E-active: index or HEAD moved < 15 min ago
IDLE_AGE = 2 * 3600
PROC = re.compile(r'\b(forge|solc|cargo|rustc|docker|git|claude)\b')
PROGRESS = re.compile(r'^(READY|LANDING|LANDED)\b.*\b([0-9a-f]{40})\s*$')

ENV = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
ENV.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1',
           GIT_AUTHOR_NAME='Test', GIT_AUTHOR_EMAIL='test@example.invalid',
           GIT_COMMITTER_NAME='Test', GIT_COMMITTER_EMAIL='test@example.invalid',
           GIT_TERMINAL_PROMPT='0', LC_ALL='C')


def sh(cwd, *args, ok=True, env=None, stdin=None):
    p = subprocess.run(args, cwd=cwd, env=env or ENV, input=stdin,
                       capture_output=True, text=True)
    if ok and p.returncode != 0:
        raise AssertionError('%s -> %d: %s' % (' '.join(args), p.returncode, p.stderr.strip()))
    return p


def git(cwd, *args, **kw):
    return sh(cwd, 'git', *args, **kw).stdout.rstrip('\n')


def rc(cwd, *args):
    return sh(cwd, 'git', *args, ok=False).returncode


def write(path, body):
    with open(path, 'w') as fh:
        fh.write(body)


def read(path):
    with open(path) as fh:
        return fh.read()


def numbered(n=10):
    return ''.join('line %d\n' % i for i in range(1, n + 1))


def set_line(path, i, text):
    rows = read(path).splitlines(True)
    rows[i - 1] = text + '\n'
    write(path, ''.join(rows))


def gitpath(tree, name):
    return git(tree, 'rev-parse', '--path-format=absolute', '--git-path', name)


def dirty(tree):
    """Dirty count. --no-optional-locks: the survey must not write the index."""
    out = git(tree, '--no-optional-locks', 'status', '--porcelain')
    return len(out.splitlines()) if out else 0


def sample(tree):
    """Survey sample of a tree: HEAD and dirty count."""
    return git(tree, 'rev-parse', 'HEAD'), dirty(tree)


def classify(repo, ref, base='origin/main'):
    """Branch class from SKILL.md Classes: A on main, B clean, C conflicts.

    A: ancestor, or landed by cherry-pick or rebase (`git cherry` prints only
    `-` lines), or by a multi-commit squash (the merge tree is base's tree).
    """
    if rc(repo, 'merge-base', '--is-ancestor', ref, base) == 0:
        return 'A'
    cherry = git(repo, 'cherry', base, ref).splitlines()
    if cherry and all(c.startswith('-') for c in cherry):
        return 'A'
    p = sh(repo, 'git', 'merge-tree', '--write-tree', base, ref, ok=False)
    if p.returncode == 0 and p.stdout.split()[0] == git(repo, 'rev-parse', base + '^{tree}'):
        return 'A'
    return {0: 'B', 1: 'C'}[p.returncode]


def prune(repo, pins=()):
    """SKILL.md step 5: delete class A branches, local and remote; keep -parked and pins."""
    def keep(b):
        return b == 'main' or b in pins or b.endswith('-parked')
    git(repo, 'fetch', '-q', '--prune')
    current = git(repo, 'branch', '--show-current')
    for b in git(repo, 'branch', '--format=%(refname:short)').split():
        if not keep(b) and b != current and classify(repo, b) == 'A':
            git(repo, 'branch', '-D', b)
    for line in git(repo, 'ls-remote', '--heads', 'origin').splitlines():
        sha, ref = line.split()
        b = ref[len('refs/heads/'):]
        if not keep(b) and classify(repo, sha) == 'A':
            git(repo, 'push', '-q', 'origin', '--delete', b)


def done_heads(repo, pins=()):
    """SKILL.md Done: remote heads other than main, intended pins and -parked branches."""
    heads = [l.split()[1][len('refs/heads/'):]
             for l in git(repo, 'ls-remote', '--heads', 'origin').splitlines()]
    return [b for b in heads if b != 'main' and b not in pins and not b.endswith('-parked')]


def e_signals(tree, start=None, now=None):
    """Git evidence of the SKILL.md E-active test that holds for one tree."""
    now = time.time() if now is None else now
    out = []
    for base, dirs, files in os.walk(tree):
        dirs[:] = [d for d in dirs if d != '.git']
        if any(os.lstat(os.path.join(base, f)).st_mtime > now - MTIME_MIN * 60
               for f in files if f != '.git'):
            out.append('mtime')
            break
    m = re.search(r'\{(\d+)\}', git(tree, 'reflog', '-1', '--date=unix', '--format=%gd', 'HEAD'))
    if m and int(m.group(1)) > now - MTIME_MIN * 60:
        out.append('reflog')
    for name in ('index', 'HEAD'):
        f = gitpath(tree, name)
        if os.path.exists(f) and os.stat(f).st_mtime > now - GITMETA_MIN * 60:
            out.append(name)
    for name in ('rebase-merge', 'rebase-apply', 'MERGE_HEAD'):
        if os.path.exists(gitpath(tree, name)):
            out.append(name)
    if dirty(tree):
        out.append('dirty')
    if start is not None and sample(tree) != start:
        out.append('moved')
    return out


def live_pids(tree):
    """PIDs of a build or agent process with the tree in argv or as cwd."""
    rows = sh(None, 'ps', '-axo', 'pid,etime,command').stdout.splitlines()[1:]
    hits, check = set(), []
    for row in rows:
        pid, _, cmd = row.strip().split(None, 2)
        if not PROC.search(cmd):
            continue
        if tree in cmd:
            hits.add(pid)
        else:
            check.append(pid)
    if check:
        out = sh(None, 'lsof', '-a', '-d', 'cwd', '-p', ','.join(check), ok=False).stdout
        for row in out.splitlines()[1:]:
            cols = row.split()
            if cols and cols[-1] == tree:
                hits.add(cols[1])
    return hits


def progress_sha(path):
    """Last progress line READY/LANDING/LANDED <sha> -> (state, sha)."""
    m = PROGRESS.match(read(path).splitlines()[-1])
    return (m.group(1), m.group(2)) if m else (None, None)


class Scenario(unittest.TestCase):
    """Bare origin with app.txt (10 lines), a.txt, b.txt; home = primary clone."""

    def setUp(self):
        self.root = os.path.realpath(tempfile.mkdtemp(prefix='max-merge-test-'))
        self.addCleanup(shutil.rmtree, self.root, True)
        seed = self.p('seed')
        git(self.root, 'init', '-q', '-b', 'main', seed)
        for name, body in (('app.txt', numbered()), ('a.txt', 'a0\n'), ('b.txt', 'b0\n')):
            write(os.path.join(seed, name), body)
        git(seed, 'add', '.')
        git(seed, 'commit', '-q', '-m', 'base')
        git(self.root, 'clone', '-q', '--bare', seed, self.p('origin.git'))
        self.home = self.clone('home')

    def p(self, *parts):
        return os.path.join(self.root, *parts)

    def clone(self, name):
        git(self.root, 'clone', '-q', self.p('origin.git'), self.p(name))
        return self.p(name)

    def worktree(self, name, branch, start='origin/main', env=None):
        git(self.home, 'worktree', 'add', '-q', '-b', branch, self.p(name), start, env=env)
        return self.p(name)

    def commit(self, tree, msg, env=None, **files):
        """Commit only the named tracked paths (SKILL.md: commit only your own paths)."""
        for name, body in files.items():
            write(os.path.join(tree, name.replace('_', '.')), body)
        paths = [n.replace('_', '.') for n in files]
        git(tree, 'commit', '-q', '-m', msg, '--', *paths, env=env)
        return git(tree, 'rev-parse', 'HEAD')

    def push_main_change(self, name, line, text):
        """A peer session lands one line on origin main."""
        peer = self.clone(name)
        body = read(os.path.join(peer, 'app.txt')).splitlines(True)
        body[line - 1] = text + '\n'
        sha = self.commit(peer, 'peer ' + name, app_txt=''.join(body))
        git(peer, 'push', '-q', 'origin', 'HEAD:main')
        return sha

    def origin_main(self):
        return git(self.root, 'ls-remote', self.p('origin.git'), 'refs/heads/main').split()[0]

    # -- SKILL.md text ---------------------------------------------------

    def test_skill_quotes_each_command(self):
        for quote in ('`git branch -vv`', '`git worktree list`', '`git ls-remote --heads origin`',
                      '`git fetch --prune`', '`ps -axo pid,etime,command`',
                      '`lsof -a -d cwd -p <pid>`', '`find /private/tmp/claude-501 -maxdepth 4 -name .git`',
                      '`git worktree add`', '`git format-patch`', '`rebase-merge`, `rebase-apply` or `MERGE_HEAD`',
                      '< 30 min old', '< 15 min ago', '`git rev-parse --git-path index` / `HEAD`',
                      'resolve each with `--git-path`', '`git --no-optional-locks status`',
                      '`git cherry origin/main <branch>`', '`git merge-tree --write-tree origin/main <branch>`',
                      'Keep `-parked` branches (local + remote)', 'intended pins and `-parked` branches',
                      '`~/bin/forge-slot status`',
                      'no `git add -A`, `reset` or `stash`', 'Commit only your own paths',
                      '`--ours` is upstream, `--theirs` your commit', '`READY`/`LANDING`/`LANDED <sha>`',
                      '`-parked` branches', 'Never `--force` to main', 'Clean tree + idle owner = F',
                      'Fetch the SHA into the primary clone at once', 'Re-resolve every SHA at land time',
                      'returns `git format-patch`; the builder applies serially',
                      'ABORT the branch', 'Rebase in parallel, cherry-pick last'):
            self.assertIn(quote, SKILL_TEXT, 'SKILL.md no longer says: ' + quote)

    def test_skill_drops_the_four_faults(self):
        steps = SKILL_TEXT.split('## Steps', 1)[1]
        for fault in ('`.git/index`', '`.git/HEAD`', 'ancestor/merged', 'zero parked branches',
                      'only `main` (+ intended pins)', '`~/.forge-build.lock`'):
            self.assertFalse(fault in steps, 'SKILL.md steps still say: ' + fault)

    # -- two sessions, one tree ------------------------------------------

    def test_two_sessions_one_tree_commit_own_paths(self):
        write(self.p('home', 'a.txt'), 'a1\n')
        write(self.p('home', 'b.txt'), 'b1\n')
        add_all = git(self.home, 'add', '-A', '--dry-run')
        self.assertIn("add 'b.txt'", add_all, 'git add -A would snapshot the peer file')

        lock = gitpath(self.home, 'index.lock')
        write(lock, '')
        head = git(self.home, 'rev-parse', 'HEAD')
        p = sh(self.home, 'git', 'commit', '-q', '-m', 'A', '--', 'a.txt', ok=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn('index.lock', p.stderr)
        self.assertEqual(git(self.home, 'rev-parse', 'HEAD'), head)
        os.remove(lock)

        procs = {f: subprocess.Popen(['git', 'commit', '-q', '-m', 'session ' + f, '--', f],
                                     cwd=self.home, env=ENV, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, text=True)
                 for f in ('a.txt', 'b.txt')}
        for f, proc in procs.items():
            _, err = proc.communicate()
            if proc.returncode:
                self.assertIn('lock', err)
                git(self.home, 'commit', '-q', '-m', 'session ' + f, '--', f)
        new = git(self.home, 'rev-list', '--reverse', head + '..HEAD').split()
        self.assertEqual(len(new), 2)
        touched = sorted(git(self.home, 'show', '--name-only', '--format=', c) for c in new)
        self.assertEqual(touched, ['a.txt', 'b.txt'])
        self.assertEqual((read(self.p('home', 'a.txt')), read(self.p('home', 'b.txt'))), ('a1\n', 'b1\n'))
        self.assertEqual(dirty(self.home), 0)

    # -- sub-agent in its own worktree and branch -------------------------

    def test_subagent_own_worktree_and_branch(self):
        live_before = sample(self.home)
        index = gitpath(self.home, 'index')
        os.utime(index, (time.time() - IDLE_AGE,) * 2)
        index_mtime = os.stat(index).st_mtime
        wt = self.worktree('wt-sub', 'sub/feature')
        self.commit(wt, 'sub-agent work', a_txt='sub\n')

        self.assertEqual(sample(self.home), live_before, 'sub-agent wrote in the live tree')
        self.assertEqual(os.stat(index).st_mtime, index_mtime)
        self.assertTrue(os.path.isfile(os.path.join(wt, '.git')))
        self.assertFalse(os.path.exists(os.path.join(wt, '.git', 'index')),
                         'literal .git/index misses a linked worktree')
        for name in ('index', 'HEAD'):
            self.assertTrue(os.path.isfile(gitpath(wt, name)), '--git-path resolves ' + name)
        self.assertIn('index', e_signals(wt))
        self.assertIn('HEAD', e_signals(wt))
        self.assertIn('reflog', e_signals(wt))

        self.assertIn(wt, git(self.home, 'worktree', 'list'))
        self.assertRegex(git(self.home, 'branch', '-vv'), r'(?m)^\+ sub/feature ')
        self.assertEqual(classify(self.home, 'sub/feature'), 'B')
        self.assertNotEqual(rc(self.home, 'worktree', 'add', '-q', self.p('wt-second'), 'sub/feature'), 0,
                            'one writer per tree: a branch checks out in one worktree only')

    def test_scratchpad_gc_keeps_worktree_commits_and_fetched_handoff(self):
        scratch = self.p('scratch', 'claude-501')
        os.makedirs(os.path.join(scratch, 's1'))
        wt = self.p('scratch', 'claude-501', 's1', 'wt')
        git(self.home, 'worktree', 'add', '-q', '-b', 'sub/gc', wt, 'origin/main')
        sub_sha = self.commit(wt, 'sub-agent', a_txt='gc\n')
        handoffs = []
        for s in ('s2', 's3'):
            c = os.path.join(scratch, s, 'clone')
            git(self.root, 'clone', '-q', self.p('origin.git'), c)
            handoffs.append(self.commit(c, 'handoff ' + s, b_txt=s + '\n'))

        found = sh(None, 'find', scratch, '-maxdepth', '4', '-name', '.git').stdout.split()
        heads = {os.path.dirname(g): git(os.path.dirname(g), 'rev-parse', 'HEAD') for g in found}
        self.assertEqual(sorted(heads.values()), sorted([sub_sha] + handoffs))

        git(self.home, 'fetch', '-q', os.path.join(scratch, 's2', 'clone'), handoffs[0])
        shutil.rmtree(self.p('scratch'))

        self.assertEqual(rc(self.home, 'cat-file', '-e', sub_sha + '^{commit}'), 0)
        self.assertEqual(rc(self.home, 'cat-file', '-e', handoffs[0] + '^{commit}'), 0)
        self.assertNotEqual(rc(self.home, 'cat-file', '-e', handoffs[1] + '^{commit}'), 0,
                            'an unfetched handoff dies with its scratchpad')
        git(self.home, 'worktree', 'prune')
        self.assertNotIn(wt, git(self.home, 'worktree', 'list'))
        git(self.home, 'worktree', 'add', '-q', '--detach', self.p('wt-gc'), sub_sha)
        self.assertEqual(read(self.p('wt-gc', 'a.txt')), 'gc\n')

    def test_land_time_resolve_picks_amended_subagent_commit(self):
        wt = self.worktree('wt-amend', 'sub/amend')
        self.commit(wt, 'first', a_txt='v1\n')
        survey_sha = git(self.home, 'rev-parse', 'sub/amend')

        write(os.path.join(wt, 'a.txt'), 'v2\n')
        git(wt, 'commit', '-q', '--amend', '-m', 'first, amended', '--', 'a.txt')
        self.commit(wt, 'second', b_txt='v2\n')

        land_sha = git(wt, 'rev-parse', 'HEAD')
        self.assertEqual(git(self.home, 'rev-parse', 'sub/amend'), land_sha)
        self.assertNotEqual(rc(self.home, 'merge-base', '--is-ancestor', survey_sha, land_sha), 0,
                            'the survey SHA is stale after an amend')
        git(self.home, 'fetch', '-q', '--prune')
        git(self.home, 'push', '-q', 'origin', land_sha + ':main')
        self.assertEqual(self.origin_main(), land_sha)
        git(self.home, 'fetch', '-q', '--prune')
        self.assertEqual(git(self.home, 'show', 'origin/main:a.txt'), 'v2')

    # -- concurrent session during the merge -----------------------------

    def test_concurrent_push_during_merge_refetch_rebase_keeps_peer(self):
        lander = self.clone('lander')
        git(lander, 'checkout', '-q', '-b', 'feat')
        body = read(os.path.join(lander, 'app.txt')).splitlines(True)
        body[1] = 'line 2 lander\n'
        mine = self.commit(lander, 'lander', app_txt=''.join(body))
        git(lander, 'fetch', '-q', '--prune')

        live = self.clone('live')
        start = sample(live)
        body = read(os.path.join(live, 'app.txt')).splitlines(True)
        body[8] = 'line 9 live\n'
        peer = self.commit(live, 'live session', app_txt=''.join(body))
        git(live, 'push', '-q', 'origin', 'HEAD:main')
        self.assertIn('moved', e_signals(live, start=start), 'a moving HEAD is a finding')

        self.assertNotEqual(rc(lander, 'push', '-q', 'origin', 'HEAD:main'), 0)
        self.assertEqual(self.origin_main(), peer, 'a plain push never overwrites the peer')

        git(lander, 'fetch', '-q', '--prune')
        git(lander, 'rebase', '-q', 'origin/main')
        git(lander, 'push', '-q', 'origin', 'HEAD:main')
        tip = git(lander, 'rev-parse', 'HEAD')
        self.assertEqual(self.origin_main(), tip, 'fast-forward of the exact commit')
        self.assertEqual(rc(lander, 'merge-base', '--is-ancestor', peer, tip), 0)
        final = git(lander, 'show', 'origin/main:app.txt')
        self.assertIn('line 2 lander', final)
        self.assertIn('line 9 live', final)
        self.assertNotEqual(mine, tip)

    # -- classes A/B/C, already merged -----------------------------------

    def test_classes_and_already_merged_branch(self):
        h = self.home
        git(h, 'checkout', '-q', '-b', 'done', 'origin/main')
        self.commit(h, 'done', a_txt='done\n')
        git(h, 'push', '-q', 'origin', 'done:main')
        git(h, 'checkout', '-q', '-b', 'squashed', 'origin/main')
        picked = self.commit(h, 'squashed', b_txt='sq\n')
        git(h, 'checkout', '-q', '-b', 'multi', 'origin/main')
        m1 = numbered().replace('line 8\n', 'line 8 m1\n')
        self.commit(h, 'multi 1', app_txt=m1)
        multi = self.commit(h, 'multi 2', app_txt=m1.replace('line 9\n', 'line 9 m2\n'))
        git(h, 'checkout', '-q', '-b', 'rebased', 'origin/main')
        rebased = self.commit(h, 'rebased', a_txt='rb\n')
        git(h, 'checkout', '-q', '-b', 'clean', 'origin/main')
        self.commit(h, 'clean', app_txt=numbered().replace('line 5\n', 'line 5 clean\n'))
        git(h, 'checkout', '-q', '-b', 'clash', 'origin/main')
        self.commit(h, 'clash', app_txt=numbered().replace('line 2\n', 'line 2 branch\n'))
        git(h, 'checkout', '-q', 'main')

        peer = self.clone('peer')
        self.commit(peer, 'main line 2', app_txt=numbered().replace('line 2\n', 'line 2 main\n'))
        git(peer, 'fetch', '-q', self.home, picked, multi, rebased)
        git(peer, 'cherry-pick', picked)
        self.assertNotEqual(git(peer, 'rev-parse', 'HEAD'), picked)
        git(peer, 'merge', '-q', '--squash', multi)
        git(peer, 'commit', '-q', '-m', 'multi squashed')
        git(peer, 'branch', 'rb', rebased)
        git(peer, 'rebase', '-q', 'main', 'rb')
        git(peer, 'checkout', '-q', 'main')
        git(peer, 'merge', '-q', '--ff-only', 'rb')
        self.assertNotEqual(git(peer, 'rev-parse', 'HEAD'), rebased)
        git(peer, 'push', '-q', 'origin', 'HEAD:main')
        git(h, 'fetch', '-q', '--prune')

        names = ('done', 'squashed', 'multi', 'rebased', 'clean', 'clash')
        got = {b: classify(h, b) for b in names}
        self.assertEqual(got, {'done': 'A', 'squashed': 'A', 'multi': 'A', 'rebased': 'A',
                               'clean': 'B', 'clash': 'C'})
        cherry = git(h, 'cherry', 'origin/main', 'multi').splitlines()
        self.assertTrue(any(c.startswith('+') for c in cherry),
                        'git cherry misses a multi-commit squash; the merge-tree check finds it')
        merged = git(h, 'branch', '--merged', 'origin/main')
        self.assertIn('done', merged)
        for b in ('squashed', 'multi', 'rebased'):
            self.assertNotIn(b, merged, '--merged sees ancestors only; class A needs the patch checks')
        git(h, 'checkout', '-q', 'squashed')
        git(h, 'rebase', '-q', 'origin/main')
        self.assertEqual(git(h, 'rev-parse', 'HEAD'), git(h, 'rev-parse', 'origin/main'),
                         'an already-merged branch adds nothing on rebase')

    # -- dirty worktree and parked branch --------------------------------

    def test_dirty_worktree_is_e_active_and_survives_the_merge(self):
        wt = self.worktree('wt-dirty', 'wip')
        head = self.commit(wt, 'wip', a_txt='wip\n')
        write(os.path.join(wt, 'b.txt'), 'half done\n')
        self.assertIn('dirty', e_signals(wt))

        land = self.worktree('wt-land', 'ready')
        self.commit(land, 'ready', app_txt=numbered().replace('line 3\n', 'line 3 ready\n'))
        git(land, 'fetch', '-q', '--prune')
        git(land, 'rebase', '-q', 'origin/main')
        git(land, 'push', '-q', 'origin', 'HEAD:main')
        git(self.home, 'worktree', 'remove', self.p('wt-land'))

        self.assertNotEqual(rc(self.home, 'worktree', 'remove', wt), 0, 'a dirty worktree refuses removal')
        self.assertTrue(os.path.isdir(wt))
        self.assertEqual(git(wt, 'rev-parse', 'HEAD'), head)
        self.assertEqual(read(os.path.join(wt, 'b.txt')), 'half done\n')
        self.assertEqual(git(wt, '--no-optional-locks', 'status', '--porcelain'), ' M b.txt')

    def test_parked_branch_survives_prune(self):
        h = self.home
        for b, f, body in (('old-done', 'a_txt', 'od\n'), ('land-me', 'b_txt', 'lm\n'),
                           ('idea-parked', 'app_txt', numbered().replace('line 7\n', 'line 7 idea\n'))):
            git(h, 'checkout', '-q', '-b', b, 'origin/main')
            self.commit(h, b, **{f: body})
        git(h, 'branch', 'done-parked', 'old-done')
        parked = {b: git(h, 'rev-parse', b) for b in ('idea-parked', 'done-parked')}
        git(h, 'push', '-q', 'origin', 'old-done:main', 'idea-parked', 'done-parked', 'land-me')
        git(h, 'fetch', '-q', '--prune')

        git(h, 'checkout', '-q', 'land-me')
        git(h, 'rebase', '-q', 'origin/main')
        git(h, 'push', '-q', 'origin', 'HEAD:main')
        git(h, 'checkout', '-q', 'main')
        git(h, 'merge', '-q', '--ff-only', 'land-me')
        git(h, 'fetch', '-q', '--prune')
        self.assertEqual(classify(h, 'done-parked'), 'A')
        self.assertEqual(classify(h, 'origin/land-me'), 'A', 'remote side branch of a rebase landing')
        self.assertNotIn('origin/land-me', git(h, 'branch', '-r', '--merged', 'origin/main'))

        prune(h)

        for b, sha in parked.items():
            self.assertEqual(git(h, 'rev-parse', b), sha, b + ' kept local')
        heads = sorted(l.split()[1] for l in git(h, 'ls-remote', '--heads', 'origin').splitlines())
        self.assertEqual(heads, ['refs/heads/done-parked', 'refs/heads/idea-parked', 'refs/heads/main'])
        self.assertEqual(sorted(git(h, 'branch', '--format=%(refname:short)').split()),
                         ['done-parked', 'idea-parked', 'main'])
        self.assertEqual(done_heads(h), [], 'Done: only main, pins and -parked branches remain')

    # -- E-active signals ------------------------------------------------

    def test_rebase_in_progress_is_e_active_ours_theirs_and_abort(self):
        self.push_main_change('peer', 2, 'line 2 main')
        wt = self.worktree('wt-c', 'clash')
        before = self.commit(wt, 'clash', app_txt=numbered().replace('line 2\n', 'line 2 branch\n'))
        git(wt, 'fetch', '-q', '--prune')
        self.assertNotEqual(rc(wt, 'rebase', 'origin/main'), 0)
        self.assertIn('rebase-merge', e_signals(wt))
        self.assertFalse(os.path.exists(os.path.join(wt, '.git', 'rebase-merge')),
                         'literal .git/ path misses a linked worktree')

        git(wt, 'checkout', '--ours', 'app.txt')
        self.assertIn('line 2 main', read(os.path.join(wt, 'app.txt')), '--ours is upstream in a rebase')
        git(wt, 'checkout', '--theirs', 'app.txt')
        self.assertIn('line 2 branch', read(os.path.join(wt, 'app.txt')), '--theirs is the branch commit')

        git(wt, 'rebase', '--abort')
        self.assertEqual(git(wt, 'rev-parse', 'HEAD'), before)
        self.assertEqual(dirty(wt), 0)
        self.assertNotIn('rebase-merge', e_signals(wt))

        self.assertNotEqual(rc(wt, 'merge', 'origin/main'), 0)
        self.assertIn('MERGE_HEAD', e_signals(wt))
        git(wt, 'merge', '--abort')

    def test_live_process_in_tree_is_e_active(self):
        if not shutil.which('lsof'):
            self.skipTest('lsof absent')
        wt = self.worktree('wt-live', 'live')
        in_cwd = subprocess.Popen(['git', 'cat-file', '--batch'], cwd=wt, env=ENV,
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        in_argv = subprocess.Popen(['git', '-C', wt, 'cat-file', '--batch'], cwd=self.root, env=ENV,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        try:
            pids = live_pids(wt)
            self.assertIn(str(in_cwd.pid), pids, 'cwd arm (lsof)')
            self.assertIn(str(in_argv.pid), pids, 'command-line arm (ps)')
        finally:
            for proc in (in_cwd, in_argv):
                proc.communicate(b'')
        self.assertFalse(live_pids(wt) & {str(in_cwd.pid), str(in_argv.pid)})

    def test_idle_clean_tree_is_f_and_survey_must_not_write_index(self):
        old = time.time() - IDLE_AGE
        stamp = '@%d +0000' % old
        aged = dict(ENV, GIT_AUTHOR_DATE=stamp, GIT_COMMITTER_DATE=stamp)
        wt = self.worktree('wt-idle', 'handoff', env=aged)
        self.commit(wt, 'finished', env=aged, a_txt='finished\n')
        for base, dirs, files in os.walk(wt):
            for f in files:
                os.utime(os.path.join(base, f), (old, old))
        for name in ('index', 'HEAD'):
            os.utime(gitpath(wt, name), (old, old))

        index = gitpath(wt, 'index')
        before = os.stat(index).st_mtime_ns
        start = sample(wt)
        git(wt, '--no-optional-locks', 'status', '--porcelain')
        self.assertEqual(os.stat(index).st_mtime_ns, before, 'the survey status leaves the index alone')
        self.assertEqual(e_signals(wt, start=start), [], 'clean + idle tree carries no E signal')
        self.assertEqual(classify(self.home, 'handoff'), 'B', 'F lands as B')

        git(wt, 'status', '--porcelain')
        self.assertIn('index', e_signals(wt), 'a plain git status rewrites the index of the tree it reads')

    # -- own sub-agents in parallel --------------------------------------

    def test_sublanes_return_patches_builder_applies_serially(self):
        builder = self.worktree('wt-builder', 'build/x')
        self.commit(builder, 'builder', app_txt=numbered().replace('line 1\n', 'line 1 builder\n'))
        start = sample(builder)
        patches = []
        for name, line in (('s1', 4), ('s2', 8)):
            wt = self.worktree('wt-' + name, name, start='build/x')
            set_line(os.path.join(wt, 'app.txt'), line, 'line %d %s' % (line, name))
            self.commit(wt, name, app_txt=read(os.path.join(wt, 'app.txt')))
            patches.append(git(wt, 'format-patch', '-1', '--stdout') + '\n')
        self.assertEqual(sample(builder), start, 'sub-lanes never write in the builder tree')
        for patch in patches:
            sh(builder, 'git', 'am', '-q', stdin=patch)
        body = read(os.path.join(builder, 'app.txt'))
        for text in ('line 1 builder', 'line 4 s1', 'line 8 s2'):
            self.assertIn(text, body)
        self.assertEqual(git(builder, 'rev-list', '--count', 'origin/main..HEAD'), '3')

    def test_lander_rebases_early_and_cherry_picks_ready_commits(self):
        fixer = self.worktree('wt-fix', 'fix/y')
        f1 = self.commit(fixer, 'fix 1', a_txt='fix1\n')
        lander = self.worktree('wt-lander', 'land/y', start='fix/y')
        peer = self.push_main_change('peer', 10, 'line 10 peer')
        git(lander, 'fetch', '-q', '--prune')
        git(lander, 'rebase', '-q', 'origin/main')

        set_line(os.path.join(fixer, 'app.txt'), 5, 'line 5 fix2')
        f2 = self.commit(fixer, 'fix 2', app_txt=read(os.path.join(fixer, 'app.txt')))
        progress = self.p('progress-fix.md')
        write(progress, 'gates green\nREADY fix/y %s\n' % f2)

        state, sha = progress_sha(progress)
        self.assertEqual((state, sha), ('READY', f2))
        git(lander, 'cherry-pick', f1 + '..' + sha)
        git(lander, 'reset', '--soft', 'origin/main')
        git(lander, 'commit', '-q', '-m', 'fix/y squashed')
        git(lander, 'fetch', '-q', '--prune')
        git(lander, 'push', '-q', 'origin', 'HEAD:main')
        tip = git(lander, 'rev-parse', 'HEAD')
        with open(progress, 'a') as fh:
            fh.write('LANDED %s\n' % tip)

        self.assertEqual(progress_sha(progress), ('LANDED', tip))
        self.assertEqual(self.origin_main(), tip)
        self.assertEqual(git(lander, 'rev-list', '--count', peer + '..' + tip), '1')
        self.assertEqual(git(lander, 'show', tip + ':a.txt'), 'fix1')
        app = git(lander, 'show', tip + ':app.txt')
        self.assertIn('line 5 fix2', app)
        self.assertIn('line 10 peer', app)


if __name__ == '__main__':
    unittest.main(verbosity=2)
