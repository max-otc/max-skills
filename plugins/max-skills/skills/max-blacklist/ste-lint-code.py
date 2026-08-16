#!/usr/bin/env python3
"""ste-lint-code.py - score the PROSE INSIDE SOURCE CODE against ASD-STE100.

This script pulls comments, docstrings, and user-facing string literals out of source
files. It then scores them with the SAME engine as the prose linter. It loads that engine
by path from ~/.claude/skills/ste-writing/ste-lint.py. One engine means the two skills
cannot drift apart.

LIMITS, stated plainly. Extraction uses line scanning and regular expressions, not a
parser. Python docstrings are the one exception. They use the `ast` module.

  - String extraction gives false positives. A SQL fragment, a regular expression, a
    template, or a config key with a space in it can look like a sentence. Read the
    reported line before you act on it.
  - String extraction gives false negatives. It often misses or truncates strings that
    the code joins, interpolates, or writes across several lines.
  - Comment scanning tracks quotes one line at a time. A `//` or a `#` inside a
    multi-line string can look like the start of a comment.
  - A filter drops commented-out code by its shape, not by parsing it. The filter drops
    some prose that looks like code. It keeps some code that reads like a sentence.

The score is a signal for a delta. It is not a certification. Lint, rewrite, lint again.

SCORING MODEL. The script scores each chunk on its own, then adds the results. A chunk is
one comment line, one docstring block, or one string literal. Per-chunk scoring is what
makes the file:line attribution exact. Single-line comments never trip the paragraph rule.
Long docstring blocks still can, and that result is correct.
"""

import argparse
import ast
import importlib.util
import json
import os
import re
import sys

_LOCAL_ENGINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ste-lint.py")
ENGINE_PATH = (_LOCAL_ENGINE if os.path.isfile(_LOCAL_ENGINE)
               else os.path.expanduser("~/.claude/skills/ste-writing/ste-lint.py"))


def load_engine(path=ENGINE_PATH):
    """Load the prose linter as a module so there is one scoring engine."""
    if not os.path.isfile(path):
        sys.stderr.write(
            "error: scoring engine not found at %s\n"
            "The ste-code linter reuses the ste-writing linter. Install the ste-writing\n"
            "skill first, or set STE_LINT_PATH to the ste-lint.py file.\n" % path
        )
        sys.exit(2)
    spec = importlib.util.spec_from_file_location("ste_lint_engine", path)
    if spec is None or spec.loader is None:
        sys.stderr.write("error: cannot load the scoring engine from %s\n" % path)
        sys.exit(2)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:  # noqa: BLE001 - report and stop, do not guess
        sys.stderr.write("error: the scoring engine failed to load: %s\n" % exc)
        sys.exit(2)
    if not hasattr(mod, "lint"):
        sys.stderr.write("error: %s has no lint() function\n" % path)
        sys.exit(2)
    return mod


SKIP_DIRS = {
    "node_modules", ".git", "vendor", "target", "dist", "build",
    ".next", "__pycache__", "out",
}
SKIP_PATH_FRAGMENTS = ("lib/forge-std",)

URL_RE = re.compile(r"(?:https?://|ftp://|www\.)\S+")
PRAGMA_RE = re.compile(
    r"eslint-disable|eslint-enable|prettier-ignore|@ts-ignore|@ts-nocheck|@ts-expect-error"
    r"|noqa|nolint|#\[allow\(|#\[deny\(|#\[warn\(|pylint:|mypy:|type:\s*ignore"
    r"|golangci|clippy::|solhint|forge-lint|slither-disable|fmt:\s*(?:on|off)"
    r"|istanbul ignore|c8 ignore|coverage:\s*ignore|pragma\s+solidity|#!/",
    re.I,
)
LICENCE_RE = re.compile(
    r"SPDX-License|SPDX-FileCopyright|Copyright\s|\(c\)\s*\d{4}|All rights reserved"
    r"|Licensed under|MIT License|Apache License|GNU General Public",
    re.I,
)
CODEISH_RE = re.compile(
    r"[=<>!]==?|=>|->|::|\+\+|--\s*$|\w+\([^)]*\)|\{\s*$|^\s*[@#$]\w+"
    r"|^\s*(?:if|else|for|while|switch|case|return|import|from|export|const|let|var"
    r"|def|class|fn|func|pub|struct|impl|require|assert|console\.|print\(|System\.)\b"
)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]+")
SCHEMA_LINE_RE = re.compile(
    r"^[\[\]{}(),;:\s]*$"                       # bare brackets and punctuation
    r"|^[\w\"'.\[\]]+\s*:\s*[\w\[\]\s|.\"'<>]*,?$"  # field: type,
    r"|^[\w.]+\s*\([^)]*\)\s*:?\s*$"            # name(type):
)
STRING_RE = re.compile(
    r"\"\"\"(?P<td>(?:[^\\]|\\.)*?)\"\"\""
    r"|'''(?P<ts>(?:[^\\]|\\.)*?)'''"
    r"|\"(?P<d>(?:[^\"\\\n]|\\.)*)\""
    r"|'(?P<s>(?:[^'\\\n]|\\.)*)'"
    r"|`(?P<b>(?:[^`\\]|\\.)*)`",
    re.S,
)

LANGS = {
    ".py": "python", ".pyi": "python",
    ".js": "cfamily", ".jsx": "cfamily", ".ts": "cfamily", ".tsx": "cfamily",
    ".mjs": "cfamily", ".cjs": "cfamily",
    ".rs": "cfamily", ".go": "cfamily", ".sol": "cfamily",
    ".c": "cfamily", ".h": "cfamily", ".cpp": "cfamily", ".hpp": "cfamily",
    ".cc": "cfamily", ".hh": "cfamily", ".java": "cfamily",
    ".sh": "hash", ".bash": "hash", ".zsh": "hash", ".rb": "hash",
    ".toml": "hash_only", ".yaml": "hash_only", ".yml": "hash_only",
}
DOC_LINE_PREFIXES = ("///", "//!", "//?")


# ---------------------------------------------------------------- prose filters

def has_sentence_shape(text):
    return len(WORD_RE.findall(text)) >= 4


def is_non_prose_comment(body):
    """True when this comment body is not English prose worth scoring."""
    b = body.strip().strip("*").strip()
    b = b.lstrip("-=#/! \t")
    if len(b) < 4:
        return True
    if LICENCE_RE.search(b) or PRAGMA_RE.search(b):
        return True
    if b.startswith("TODO") or b.startswith("FIXME") or b.startswith("HACK"):
        b = re.sub(r"^(?:TODO|FIXME|HACK)\b[:(\s]*", "", b)
        if len(WORD_RE.findall(b)) < 3:
            return True
    stripped = URL_RE.sub(" ", b).strip(" \t-—:.,")
    if not stripped or len(WORD_RE.findall(stripped)) < 2:
        return True
    if not has_sentence_shape(b):
        return True
    ends_code = b.rstrip().endswith((";", "{", "}", ")", ",", "|", "&&", "||"))
    if (ends_code or CODEISH_RE.search(b)) and not has_sentence_shape(
        CODEISH_RE.sub(" ", b)
    ):
        return True
    if CODEISH_RE.search(b) and len(WORD_RE.findall(b)) < 6:
        return True
    return False


def is_prose_string(text):
    """True when a string literal looks like user-facing prose."""
    s = text.strip()
    if len(s) < 8 or " " not in s:
        return False
    words = WORD_RE.findall(s)
    if len(words) < 2:
        return False
    letters = sum(1 for c in s if c.isalpha())
    if letters < len(s) * 0.45:
        return False
    if URL_RE.search(s) and len(WORD_RE.findall(URL_RE.sub(" ", s))) < 3:
        return False
    if re.fullmatch(r"[\s{}%\d.\-:sdfrxeg,<>=\[\]#*+_/|]+", s):
        return False
    if re.search(r"[=<>]=|=>|\w+\(\)|;\s*$|\{\{|\}\}|</\w|/>", s):
        return False
    if "\n" in s and len(words) < 5:
        return False
    return True


def clean_for_score(text):
    """Remove URLs and comment furniture before scoring."""
    t = URL_RE.sub(" ", text)
    t = re.sub(r"^[\s*/#!\-]+", "", t, flags=re.M)
    t = re.sub(r"\{[^{}\s]{0,40}\}|%[sdfrxg]|%\([^)]*\)[sdfr]", " ", t)
    # Collapse horizontal whitespace only. Newlines must survive: the scoring engine
    # treats a line as a sentence boundary. Collapsing them joins the separate lines of
    # a docstring or a help text into one false run-on sentence.
    t = re.sub(r"[ \t]+", " ", t)
    kept = []
    for ln in t.split("\n"):
        ln = ln.strip()
        if not ln:
            continue
        # Drop schema furniture inside docstrings: bare brackets and `field: type,`
        # lines from an embedded JSON or Args block. They are not sentences, and
        # counting them inflates the sentence count and trips the paragraph rule.
        if len(WORD_RE.findall(ln)) < 4 and (
            SCHEMA_LINE_RE.match(ln) or ln.endswith(("{", "}", "[", "]", "{,", "},", "],"))
        ):
            continue
        kept.append(ln)
    return "\n".join(kept).strip()


# ---------------------------------------------------------------- extraction

def _split_line_comment(line, marker):
    """Return (code_part, comment_body) splitting on `marker` outside quotes."""
    quote = None
    i = 0
    n = len(line)
    mlen = len(marker)
    while i < n:
        ch = line[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "\"'`":
            quote = ch
        elif line.startswith(marker, i):
            return line[:i], line[i + mlen:]
        i += 1
    return line, None


def extract_hash(text, hash_only=False):
    """Comments (and optionally strings) from `#`-comment languages."""
    chunks = []
    for no, line in enumerate(text.split("\n"), 1):
        if no == 1 and line.startswith("#!"):
            continue
        code, body = _split_line_comment(line, "#")
        if body is not None:
            chunks.append(("comment", no, body))
        if not hash_only:
            for m in STRING_RE.finditer(code):
                val = next((g for g in m.groups() if g), None)
                if val:
                    chunks.append(("string", no, val))
    return chunks


def extract_cfamily(text):
    """Comments, block docs, and strings from C-family languages."""
    chunks = []
    lines = text.split("\n")
    in_block = False
    block_is_doc = False
    block_start = 0
    block_buf = []
    for no, line in enumerate(lines, 1):
        rest = line
        if in_block:
            end = rest.find("*/")
            if end == -1:
                block_buf.append(rest)
                continue
            block_buf.append(rest[:end])
            chunks.append((
                "docstring" if block_is_doc else "comment",
                block_start,
                "\n".join(block_buf),
            ))
            in_block = False
            block_buf = []
            rest = rest[end + 2:]
        while True:
            start = rest.find("/*")
            slash = None
            code, body = _split_line_comment(rest, "//")
            if body is not None:
                slash = len(code)
            if start != -1 and (slash is None or start < slash):
                pre = rest[:start]
                for m in STRING_RE.finditer(pre):
                    val = next((g for g in m.groups() if g), None)
                    if val:
                        chunks.append(("string", no, val))
                block_is_doc = rest.startswith("/**", start) or rest.startswith("/*!", start)
                end = rest.find("*/", start + 2)
                if end == -1:
                    in_block = True
                    block_start = no
                    block_buf = [rest[start + 2:]]
                    break
                chunks.append((
                    "docstring" if block_is_doc else "comment",
                    no,
                    rest[start + 2:end],
                ))
                rest = rest[end + 2:]
                continue
            if body is not None:
                for m in STRING_RE.finditer(code):
                    val = next((g for g in m.groups() if g), None)
                    if val:
                        chunks.append(("string", no, val))
                kind = "docstring" if line.lstrip().startswith(DOC_LINE_PREFIXES) else "comment"
                chunks.append((kind, no, body))
                break
            for m in STRING_RE.finditer(rest):
                val = next((g for g in m.groups() if g), None)
                if val:
                    chunks.append(("string", no, val))
            break
    return chunks


def extract_python(text):
    """Extract hash comments by scan. Extract docstrings and strings with ast."""
    chunks = []
    for no, line in enumerate(text.split("\n"), 1):
        if no == 1 and line.startswith("#!"):
            continue
        _, body = _split_line_comment(line, "#")
        if body is not None:
            chunks.append(("comment", no, body))
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        for no, line in enumerate(text.split("\n"), 1):
            code, _ = _split_line_comment(line, "#")
            for m in STRING_RE.finditer(code):
                val = next((g for g in m.groups() if g), None)
                if val:
                    chunks.append(("string", no, val))
        return chunks
    doc_nodes = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            body = getattr(node, "body", None)
            if not body:
                continue
            first = body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) \
                    and isinstance(first.value.value, str):
                doc_nodes.add(id(first.value))
                chunks.append(("docstring", getattr(first, "lineno", 1), first.value.value))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and id(node) not in doc_nodes:
            chunks.append(("string", getattr(node, "lineno", 1), node.value))
    return chunks


def extract(path, text):
    kind = LANGS.get(os.path.splitext(path)[1].lower())
    if kind == "python":
        return extract_python(text)
    if kind == "cfamily":
        return extract_cfamily(text)
    if kind == "hash":
        return extract_hash(text)
    if kind == "hash_only":
        return extract_hash(text, hash_only=True)
    return []


# ---------------------------------------------------------------- scoring

def score_file(engine, path, buckets, no_em_dash=False):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        return {"path": path, "error": str(exc), "words": 0, "total": 0,
                "per100w": 0.0, "chunks": []}
    kept = []
    for bucket, lineno, body in extract(path, text):
        if bucket not in buckets:
            continue
        if bucket == "string":
            if not is_prose_string(body):
                continue
        else:
            if is_non_prose_comment(body):
                continue
        scored_text = clean_for_score(body)
        if len(WORD_RE.findall(scored_text)) < 3:
            continue
        # Pass the bucket. The engine cannot see WHAT a chunk is, and one rule
        # needs to know: a hyphen compound that opens a string literal and is
        # followed by a colon is a log namespace, not prose. An older engine
        # without the argument keeps its own scoring.
        try:
            res = engine.lint(scored_text, no_em_dash=no_em_dash, kind=bucket)
        except TypeError:
            res = engine.lint(scored_text, no_em_dash=no_em_dash)
        if res["words"] < 3:
            continue
        cats = sorted(k for k, n in res["violations"].items() if n)
        kept.append({
            "file": path, "line": lineno, "bucket": bucket,
            "words": res["words"], "violations": res["total"],
            "categories": cats, "per100w": res["total_per100w"],
            "text": scored_text[:200],
        })
    words = sum(c["words"] for c in kept)
    total = sum(c["violations"] for c in kept)
    return {
        "path": path, "words": words, "total": total,
        "per100w": round(total * 100.0 / words, 2) if words else 0.0,
        "chunks": kept,
    }


# ---------------------------------------------------------------- walking

def is_skipped(path):
    parts = os.path.normpath(path).split(os.sep)
    if any(p in SKIP_DIRS for p in parts):
        return True
    posix = "/".join(parts)
    return any(frag in posix for frag in SKIP_PATH_FRAGMENTS)


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                if is_skipped(root):
                    continue
                for n in sorted(names):
                    f = os.path.join(root, n)
                    if os.path.splitext(n)[1].lower() in LANGS and not is_skipped(f):
                        files.append(f)
        elif os.path.isfile(p):
            if os.path.splitext(p)[1].lower() in LANGS:
                files.append(p)
            else:
                sys.stderr.write("skip (unsupported extension): %s\n" % p)
        else:
            sys.stderr.write("skip (not found): %s\n" % p)
    return files


# ---------------------------------------------------------------- cli

def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="ste-lint-code.py",
        description="Score comments, docstrings, and user-facing strings in source code "
                    "against the machine-checkable subset of ASD-STE100.",
    )
    ap.add_argument("paths", nargs="+", help="files or directories to scan")
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="print machine-readable output")
    ap.add_argument("--bucket", action="append",
                    choices=["comment", "docstring", "string"],
                    help="score only this bucket (repeatable)")
    ap.add_argument("--top", type=int, metavar="N", default=0,
                    help="list the N worst lines across everything scanned")
    ap.add_argument("--all", action="store_true",
                    help="list every attributed violation, not just the worst")
    ap.add_argument("--max-score", type=float, metavar="N", default=None,
                    help="exit 1 when the aggregate per100w is above N")
    ap.add_argument("--no-em-dash", action="store_true",
                    help="count em dashes as violations")
    ap.add_argument("--engine", default=os.environ.get("STE_LINT_PATH", ENGINE_PATH),
                    help="path to the ste-writing scoring engine")
    args = ap.parse_args(argv)

    engine = load_engine(args.engine)
    buckets = set(args.bucket) if args.bucket else {"comment", "docstring", "string"}
    files = collect(args.paths)
    if not files:
        sys.stderr.write("error: no supported source files found\n")
        return 2

    results = [score_file(engine, f, buckets, args.no_em_dash) for f in files]
    words = sum(r["words"] for r in results)
    total = sum(r["total"] for r in results)
    agg = round(total * 100.0 / words, 2) if words else 0.0
    every = [c for r in results for c in r["chunks"] if c["violations"]]
    every.sort(key=lambda c: (-c["violations"], -c["per100w"], c["file"], c["line"]))

    if args.as_json:
        print(json.dumps({
            "files": results,
            "aggregate": {"files": len(results), "words": words,
                          "violations": total, "per100w": agg},
            "worst": every[:args.top] if args.top else every,
        }, indent=2))
    else:
        for r in results:
            worst = max(r["chunks"], key=lambda c: (c["violations"], c["per100w"]),
                        default=None) if r["chunks"] else None
            tail = ""
            if worst and worst["violations"]:
                tail = "  worst=%s:%d (%d: %s)" % (
                    worst["file"], worst["line"], worst["violations"],
                    ",".join(worst["categories"]))
            print("%-58s words=%5d viol=%4d per100w=%6.2f%s"
                  % (r["path"], r["words"], r["total"], r["per100w"], tail))
        print("-" * 78)
        print("AGGREGATE  files=%d words=%d violations=%d per100w=%.2f"
              % (len(results), words, total, agg))
        listing = every if args.all else (every[:args.top] if args.top else [])
        if listing:
            print("\nAttributed violations (worst first):")
            for c in listing:
                print("  %s:%d [%s] %d viol (%s)\n      %s"
                      % (c["file"], c["line"], c["bucket"], c["violations"],
                         ",".join(c["categories"]), c["text"][:110]))

    if args.max_score is not None and agg > args.max_score:
        sys.stderr.write("FAIL: aggregate per100w %.2f is above --max-score %.2f\n"
                         % (agg, args.max_score))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
