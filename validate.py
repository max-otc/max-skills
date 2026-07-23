#!/usr/bin/env python3
"""Repo check for the max-skills marketplace.

Verifies the three things that silently rot:
  1. every marketplace entry resolves to a real plugin dir + matching plugin.json
  2. every skill's frontmatter names itself, and the bundle copy is byte-identical
  3. no manifest or README names a skill that does not exist, and none omits one

Run it after adding, renaming, or deleting a skill. Exit 0 means clean.
"""
import json
import os
import re
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
fails = []

mp = json.load(open('.claude-plugin/marketplace.json'))
entries = {p['name']: p for p in mp['plugins']}
print("marketplace.json parses OK - %d plugin entries" % len(entries))

dirs = sorted(d for d in os.listdir('plugins') if os.path.isdir(os.path.join('plugins', d)))

for name, p in entries.items():
    src = p['source'].lstrip('./')
    pj = os.path.join(src, '.claude-plugin', 'plugin.json')
    if not os.path.isdir(src):
        fails.append("entry %s: missing dir %s" % (name, src))
    elif not os.path.isfile(pj):
        fails.append("entry %s: missing %s" % (name, pj))
    elif json.load(open(pj))['name'] != name:
        fails.append("entry %s: plugin.json name mismatch" % name)

for d in dirs:
    if d not in entries:
        fails.append("dir plugins/%s not declared in marketplace.json" % d)

skills = []
for d in dirs:
    if d == 'max-skills':
        continue
    sp = os.path.join('plugins', d, 'skills', d, 'SKILL.md')
    if not os.path.isfile(sp):
        fails.append("missing %s" % sp)
        continue
    m = re.match(r'^---\n(.*?)\n---\n', open(sp).read(), re.S)
    if not m:
        fails.append("%s: no frontmatter" % sp)
        continue
    nm = re.search(r'^name:\s*(\S+)', m.group(1), re.M)
    if not nm:
        fails.append("%s: no name" % sp)
    elif nm.group(1) != d:
        fails.append("%s: name %s != dir %s" % (sp, nm.group(1), d))
    if not re.search(r'^description:\s*(\S.*)', m.group(1), re.M):
        fails.append("%s: no description" % sp)
    skills.append(d)
print("skills validated: %d" % len(skills))

for d in skills:
    a = os.path.join('plugins', d, 'skills', d)
    b = os.path.join('plugins', 'max-skills', 'skills', d)
    if not os.path.isdir(b):
        fails.append("bundle missing %s - run plugins/max-skills/sync.sh" % d)
        continue
    fa, fb = sorted(os.listdir(a)), sorted(os.listdir(b))
    if fa != fb:
        fails.append("bundle file-set drift %s: %s vs %s" % (d, fa, fb))
        continue
    for f in fa:
        if open(os.path.join(a, f), 'rb').read() != open(os.path.join(b, f), 'rb').read():
            fails.append("bundle content drift %s/%s - run plugins/max-skills/sync.sh" % (d, f))
orphans = sorted(set(os.listdir(os.path.join('plugins', 'max-skills', 'skills'))) - set(skills))
if orphans:
    fails.append("bundle has orphan skills: %s" % orphans)
print("bundle parity checked across %d skills" % len(skills))

bundle_desc = json.load(open('plugins/max-skills/.claude-plugin/plugin.json'))['description']
for text, label in ((bundle_desc, 'bundle plugin.json'),
                    (entries['max-skills']['description'], 'marketplace bundle entry')):
    for d in skills:
        if d not in text:
            fails.append("%s does not name %s" % (label, d))
    for tok in re.findall(r'\bmax-[a-z0-9-]+\b', text):
        if tok not in skills and tok != 'max-skills':
            fails.append("%s names absent skill %s" % (label, tok))

rd = open('README.md').read()
for d in skills:
    if ('### %s' % d) not in rd:
        fails.append("README missing section for %s" % d)
for tok in set(re.findall(r'^### (\S+)', rd, re.M)):
    if tok not in skills:
        fails.append("README documents absent skill %s" % tok)
WORDS = {'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
         'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
for n in re.findall(r'all (\w+) skills', rd):
    if WORDS.get(n.lower()) != len(skills):
        fails.append("README says 'all %s skills' but there are %d" % (n, len(skills)))

if fails:
    print("\nFAIL (%d):" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("\nALL CHECKS PASS")
