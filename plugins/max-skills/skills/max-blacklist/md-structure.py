"""Document-level AI-tell checker for raw Markdown.

ste-lint.py reads one line at a time and cleans the layout away before it scores.
md_clean strips a list marker and splits a table row into one line per cell, so a
bullet, a table cell and a bold phrase mid-paragraph all reach the scorer as the
same string. Four tells live in the LAYOUT and are invisible to it:

  bold-lead      three or more list items shaped  - **Term** - explanation
  uniform        four or more list items of near-identical length
  templated      three or more sections opening on the same grammatical shape
  restating      a section closing on a paragraph that repeats its own heading

Four more live in the RHYTHM, in how long the sentences and paragraphs run
rather than in any word they use:

  sent-rhythm    sentence word-counts inside one paragraph, spread too narrow
  para-rhythm    paragraph word-counts inside one section, spread too narrow
  opener-run     consecutive sentences opening on one word or one determiner
  comma-rhythm   every sentence of a paragraph carrying the same comma count

This script reads the file RAW, before any cleaning, and reports the eight.

MEASURED on 160 Markdown files in the audit repository, split into three
populations that were compared against each other: 30 in-scope documents, 36
agent-written planning notes under notes/, and 94 vendored library documents
under lib/. One detector earns its place. Seven are off by default, each because
a hand check put it over 30% false, and a noisy detector trains the reader to
ignore the tool.

  bold-lead     ON    0 hits on the 22 audited documents, 31 across all 160.
                      10 hand-checked on the wider set, 1 false (10%).
  uniform       OFF   0 hits here. 14 hits on a 500-list reference corpus,
                      10 hand-checked, 5 false (50%). Enable with --uniform.
  templated     OFF   3 hits, all 3 hand-checked, 2 false (67%). --templated.
  restating     OFF   1 hit, hand-checked, false (100%, n=1). --restating.
  sent-rhythm   OFF   7 hits on the 30 tuning documents, 20 across all 160.
                      10 hand-checked, 8 false (80%). --sent-rhythm.
  para-rhythm   OFF   2 hits on the 30, 11 across all 160, its whole population.
                      All 11 hand-checked, 10 false (91%). --para-rhythm.
  opener-run    OFF   17 hits on the 30, 26 across all 160. 10 hand-checked,
                      6 false (60%). --opener-run.
  comma-rhythm  OFF   2 hits on the 30 and 2 across all 160, its whole
                      population. Both hand-checked, both false. --comma-rhythm.

Why each one failed:

uniform      Parallel construction is a legitimate device. A changelog, a file
             reference list and four rules each opening "Never" all cluster
             tightly and none is a tell. Worse, every TRUE hit in the sample was
             also a bold-lead hit, so on this evidence the detector adds no
             signal that bold-lead does not already carry.
templated    The shape signature cannot separate a house convention from a
             generated one. A deploy document that opens each section with the
             artifact it is about is doing its job.
restating    No corpus document closes a section by restating it. The one hit is
             an action item that reuses the heading's nouns.
sent-rhythm  The premise holds in general and fails on this corpus. Sentence-length
             CV per paragraph runs median 0.492 in-scope, 0.505 in the
             agent-written notes and 0.330 in the vendored library documents:
             the three populations sit on top of each other, and the machine-written
             one is the MOST varied of the three. Every hit is therefore a tail
             cut, not a separation, and the tail is dense technical prose whose
             sentences happen to weigh the same. Eight of ten hand-checked hits
             carry sentence lengths a reader sees as varied, [19, 25, 30, 25, 24]
             among them. The document scope fires on nothing in scope: the
             in-scope floor is CV 0.436, well clear of the 0.35 cut, and its only
             2 hits in 160 files are one vendored README counted twice at 0.309.
para-rhythm  Nearly as weak as sent-rhythm, on the same evidence. Section-level
             paragraph CV bottoms out at 0.179 in-scope against 0.066 in the
             notes, so the populations overlap. The measure also lies at the top
             end: the lowest-CV section in the corpus runs paragraphs of 45 to
             142 words, a three-fold spread that reads as varied and scores as
             uniform only because the mean is large. Ten of the 11 hits in the
             whole corpus are false by hand, the 3 document-scope ones among
             them: each sits at the n=10 floor, where CV cannot yet see a
             distribution. The one true hit is the shape worth
             knowing about: four paragraphs under one heading, each opening on a
             bold slot label, Where / The change / Blast radius / Verify, each
             filled to about 30 words. A filled template is what this detector
             finds, and a bold-lead run finds most of those first.
opener-run   Its hits are real and its premise is backwards here. The rule fires
             17 times over 30 hand-edited documents and 6 times over 36
             agent-written ones, so on this corpus a repeated opener is a mark of
             the human writer, not the model. The two halves of the rule also
             behave nothing alike, and the JSON scope field separates them.
             Scope "word", one literal opener repeated, took 4 of the 30-document
             hits and none of the four hand-checked is false: six sentences
             opening "No" and three opening "Whether" are repetitions a reader
             sees. Scope "shape", a bare determiner and a noun, took the other
             13 and all 6 hand-checked are false, because the run allows the
             determiner to change and "The core. One opens. The second. The
             deployer." is ordinary English. Filter on scope == "word" to use
             this detector at all.
comma-rhythm The cut is already at its ceiling: a hit needs EVERY sentence of the
             paragraph to carry the identical non-zero comma count, and even
             there the corpus yields 2 hits, both coincidence. The mode share
             distribution is identical across all three populations, p90 = 0.75
             in each, so any looser cut flags a tenth of all prose everywhere.

Controls. A detector that reports nothing has proved nothing until it has been
shown to fire, so every claim above rests on two fixtures and one real document.

  reference/md-structure-control.md         the four LAYOUT tells, 8 hits:
                                            bold-lead 1, uniform 2, templated 1,
                                            restating 4. The rhythm four report
                                            zero on it, which is correct.
  reference/md-structure-rhythm-control.md  the four RHYTHM tells, 15 hits, every
                                            scope of every rhythm detector fired:
                                            sent-rhythm 5 (4 paragraph, 1 whole
                                            document), para-rhythm 2 (1 section,
                                            1 whole document), opener-run 5 (4
                                            word, 1 determiner shape),
                                            comma-rhythm 1.
  audit/readiness/SECURE-CONTRACTS-GAP.md   the negative control, 63 KB of
                                            hand-edited prose, 92 prose sentences
                                            at CV 0.643 and 21 paragraphs at CV
                                            0.470. Silent on all eight detectors.

Usage: python3 md-structure.py [--json] [--quiet] [--uniform] [--templated]
                               [--restating] [--sent-rhythm] [--para-rhythm]
                               [--opener-run] [--comma-rhythm] [--all] FILE...
Exit code 1 when any detector fires, 0 when the corpus is clean, 2 on a usage
error. A gate can read the exit code.
"""

import glob
import json
import os
import re
import statistics
import sys

# ------------------------------------------------------------------ thresholds
# Every number here was tuned against the audit corpus. The comment on each says
# what moved it.

# A run of bold-lead bullets. Three is the shortest run that reads as a pattern
# rather than as one emphasised item next to another.
BOLD_RUN_MIN = 3
# The bold span is a TERM, not a paragraph in bold. 100 characters covers the
# longest real lead in the corpus (TRUST-MODEL.md:320, 70 characters) and rejects
# a whole bolded sentence.
BOLD_LEAD_MAX_CHARS = 100
# An item needs prose after the bold, or it is a definition label, not this tell.
BOLD_TAIL_MIN_WORDS = 3

# Uniform length. Four items is the shortest list where a length cluster is not
# chance. CV 0.12 is the tuned cut, and the tuning needed a second corpus: the 88
# qualifying lists in this repository bottom out at CV 0.181, so no cut inside
# this repository separates anything. A 500-list reference corpus of machine-written
# Markdown does separate: 14 lists sit at or under 0.12, the lowest at 0.040, and
# the hand-written lists in both corpora sit above 0.18. Raising the cut to 0.19
# to force a hit here would fit one document, so it stayed at 0.12. The 45-character
# floor drops link lists and one-word lists, where a tight CV says only that the
# items are short.
UNIFORM_MIN_ITEMS = 4
UNIFORM_CV_MAX = 0.12
UNIFORM_MIN_MEAN_CHARS = 45

# Templated openings. Three sections at one heading level sharing the first
# token key and the class of the next two tokens.
TEMPLATE_MIN_SECTIONS = 3

# Restating summary. Overlap is the share of the closing paragraph's content
# words that already appear in the heading or in the section's first sentence.
# Stopwords and words under four letters are out, and a trailing s is stripped.
# 0.50 is the tuned cut. The full distribution over 129 qualifying closers here
# tops out at 0.50 and over 89 in the reference corpus tops out at 0.50, so the
# cut sits on the ceiling of both: this is the point where the rule fires at all,
# not a point that separates two populations. The section must hold three prose
# paragraphs, so the rule reads a closer and not a second paragraph. The 70-word
# cap keeps it off a long final argument, and the 4-word floor stops a short line
# from scoring 1.00 on nothing.
RESTATE_OVERLAP_MIN = 0.50
RESTATE_MAX_WORDS = 70
RESTATE_MIN_CONTENT = 4

# ------------------------------------------------------------ rhythm thresholds
# These four were set BEFORE the hit counts were read, from the measured spread
# of the corpus rather than from the number of hits any cut produced. The measured
# coefficient of variation of sentence length per paragraph has median 0.492 over
# the 247 qualifying in-scope paragraphs, 0.505 over 192 in the agent-written
# notes/ tree and 0.330 over 36 in the vendored lib/ tree. A cut at 0.20 is a
# paragraph whose sentences vary less than half as much as the corpus norm. The
# 4-sentence floor is the shortest run where a spread is not chance; the 8-word
# mean floor drops a run of terse status lines, where a tight spread says only
# that the lines are short.
SENT_MIN_SENTENCES = 4
SENT_CV_MAX = 0.20
SENT_MIN_MEAN_WORDS = 8
# Document scope, same reasoning at one level up. The floor of 20 sentences keeps
# a stub out. NOTE: no document in any of the three populations reaches this cut.
# The lowest measured is 0.309, in a vendored library document, and the in-scope
# floor is 0.436. Document-level sentence uniformity does not exist in this corpus.
SENT_DOC_MIN_SENTENCES = 20
SENT_DOC_CV_MAX = 0.35

# Paragraph length, per section and per document. Same 0.20 and 0.35 cuts against
# a measured section-level median of 0.432 in-scope and 0.422 in notes/. Paragraphs
# under 15 words are furniture, a lead-in or a one-line aside, and are not counted.
PARA_MIN_PARAS = 4
PARA_CV_MAX = 0.20
PARA_MIN_WORDS = 15
# The document floor is 10 and not 5. A CV over five samples is not a distribution:
# at n=5 the measure fired on seven short planning notes whose paragraphs a reader
# sees as plainly unequal, and every one of those hits died when the floor rose.
PARA_DOC_MIN_PARAS = 10
PARA_DOC_CV_MAX = 0.35

# Repeated opener. Four is the run length that reads as a pattern; three earns a
# hit only when the repeated opener is a real word rather than a bare article,
# because three sentences opening "The" is ordinary English and fires once per
# file across the whole corpus.
OPENER_RUN_MIN = 4
OPENER_WORD_RUN_MIN = 3
ARTICLES = {"the", "a", "an"}
DETERMINERS = {"the", "a", "an", "this", "that", "these", "those", "each",
               "every", "no", "any", "all", "its", "their", "one", "both"}

# Comma count. The share cut sits at 1.00, its ceiling: every sentence of the
# paragraph carries the identical comma count. The measured mode share is p90 =
# 0.75 in all three populations, so a looser cut cannot separate anything. A mode
# of zero is not a tell, it is short prose, so the count must be at least one.
COMMA_MIN_SENTENCES = 4
COMMA_SHARE_MIN = 1.00
COMMA_MIN_COUNT = 1

DETECTORS = ("bold-lead", "uniform", "templated", "restating",
             "sent-rhythm", "para-rhythm", "opener-run", "comma-rhythm")
DEFAULT_OFF = ("uniform", "templated", "restating",
               "sent-rhythm", "para-rhythm", "opener-run", "comma-rhythm")

# ------------------------------------------------------------------ line kinds
FENCE_RE = re.compile(r"^(\s{0,3})(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])(\s+)(.*)$")
INDENT_CODE_RE = re.compile(r"^(?: {4}|\t)")
REFDEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*\S")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
HR_RE = re.compile(r"^\s{0,3}(?:[-*_]\s*){3,}$")
BOLD_LEAD_RE = re.compile(r"^\*\*(.+?)\*\*")
IMAGE_LINK_RE = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")


def is_table_row(line):
    s = line.strip()
    return s.startswith("|") and s.count("|") >= 2


def is_badge_row(line):
    """True for a row that is only images and links, the badge strip under a title."""
    s = line.strip()
    if "![" not in s and "[!" not in s:
        return False
    rest = IMAGE_LINK_RE.sub(" ", s)
    rest = re.sub(r"[\[\]()|]", " ", rest)
    return len(WORD_RE.findall(rest)) < 3


def scan(raw):
    """Classify every line of a raw Markdown file.

    Returns a list of kinds, one per line. Everything a detector must never read
    gets its own kind here, once, so no detector has to re-derive it: front
    matter, fenced blocks including mermaid, HTML comments, indented code,
    reference-link definitions, badge rows, tables and horizontal rules.
    """
    lines = raw.split("\n")
    kinds = ["text"] * len(lines)
    i = 0
    n = len(lines)
    # YAML front matter: --- on line 1, up to the next --- .
    if n and lines[0].strip() == "---":
        for j in range(1, n):
            if lines[j].strip() in ("---", "..."):
                for k in range(0, j + 1):
                    kinds[k] = "frontmatter"
                i = j + 1
                break
    fence = None          # (indent, marker char, run length)
    html_comment = False
    prev_blank = True
    prev_listish = False
    in_indent_code = False
    while i < n:
        line = lines[i]
        if fence is not None:
            kinds[i] = "fence"
            m = FENCE_RE.match(line)
            if m and m.group(2)[0] == fence[1] and len(m.group(2)) >= fence[2] \
                    and not m.group(3).strip():
                fence = None
            i += 1
            continue
        if html_comment:
            kinds[i] = "html"
            if "-->" in line:
                html_comment = False
            i += 1
            continue
        m = FENCE_RE.match(line)
        if m:
            kinds[i] = "fence"
            fence = (m.group(1), m.group(2)[0], len(m.group(2)))
            i += 1
            prev_blank = False
            continue
        if line.lstrip().startswith("<!--"):
            kinds[i] = "html"
            html_comment = "-->" not in line
            i += 1
            continue
        if not line.strip():
            kinds[i] = "blank"
            prev_blank = True
            in_indent_code = False
            i += 1
            continue
        # An indented block that opens after a blank line, outside a list, is code.
        # A list marker does not rescue it: four spaces after a paragraph is a code
        # block by the CommonMark rule, and a bullet drawn inside one is a sample,
        # not a bullet. Inside a list the same indent is a continuation line, so
        # prev_listish carries across the blank line that separates two items.
        if INDENT_CODE_RE.match(line):
            if in_indent_code or (prev_blank and not prev_listish):
                in_indent_code = True
                kinds[i] = "indentcode"
                i += 1
                continue
        else:
            in_indent_code = False
        if HEADING_RE.match(line):
            kinds[i] = "heading"
        elif REFDEF_RE.match(line):
            kinds[i] = "refdef"
        elif is_table_row(line):
            kinds[i] = "tablesep" if TABLE_SEP_RE.match(line) else "table"
        elif HR_RE.match(line):
            kinds[i] = "rule"
        elif is_badge_row(line):
            kinds[i] = "badge"
        elif LIST_RE.match(line):
            kinds[i] = "list"
        else:
            kinds[i] = "text"
        prev_blank = False
        prev_listish = kinds[i] == "list"
        i += 1
    return lines, kinds


# ------------------------------------------------------------------ list model
class Item(object):
    __slots__ = ("start", "end", "indent", "marker", "text")

    def __init__(self, start, indent, marker, text):
        self.start = start          # 0-based first line
        self.end = start            # 0-based last line, continuations included
        self.indent = indent
        self.marker = marker
        self.text = text


def list_groups(lines, kinds):
    """Group consecutive list items into lists, one group per indent level.

    A group breaks on a heading, a table, a fence, a rule, or two blank lines in
    a row. A continuation line folds into the item above it, so an item that runs
    over three lines is measured as one string, not three.
    """
    groups = []
    cur = None
    blanks = 0
    i = 0
    n = len(lines)
    while i < n:
        k = kinds[i]
        if k == "list":
            m = LIST_RE.match(lines[i])
            indent = len(m.group(1).expandtabs(4))
            marker = "ol" if m.group(2)[-1] in ".)" else "ul"
            it = Item(i, indent, marker, m.group(4).strip())
            if cur and (cur["indent"] != indent or cur["marker"] != marker
                        or blanks > 1):
                groups.append(cur)
                cur = None
            if cur is None:
                cur = {"indent": indent, "marker": marker, "items": []}
            cur["items"].append(it)
            blanks = 0
        elif k == "blank":
            blanks += 1
            if blanks > 1 and cur:
                groups.append(cur)
                cur = None
        elif k in ("text", "badge") and cur and blanks == 0:
            # A continuation line: indented under the marker, no blank between.
            lead = len(lines[i]) - len(lines[i].lstrip())
            if lead > cur["indent"]:
                it = cur["items"][-1]
                it.text += " " + lines[i].strip()
                it.end = i
            else:
                groups.append(cur)
                cur = None
        else:
            if cur:
                groups.append(cur)
                cur = None
            blanks = 0
        i += 1
    if cur:
        groups.append(cur)
    return [g for g in groups if g["items"]]


def visible_len(s):
    """Length of an item as a reader sees it, with markup and code spans out.

    A bullet ending in a 60-character path must not read as a long bullet, and
    the same bullet written with the path in backticks must measure the same.
    """
    s = INLINE_CODE_RE.sub("X", s)
    s = IMAGE_LINK_RE.sub(lambda m: m.group(0).split("](")[0][1:], s)
    s = s.replace("**", "").replace("*", "").replace("_", "")
    return len(" ".join(s.split()))


# ------------------------------------------------------------------ detector 1
def d_bold_lead(path, lines, kinds):
    hits = []
    for g in list_groups(lines, kinds):
        run = []
        for it in g["items"] + [None]:
            ok = False
            if it is not None:
                m = BOLD_LEAD_RE.match(it.text)
                if m and len(m.group(1)) <= BOLD_LEAD_MAX_CHARS:
                    tail = it.text[m.end():]
                    ok = len(WORD_RE.findall(tail)) >= BOLD_TAIL_MIN_WORDS
            if ok:
                run.append(it)
                continue
            if len(run) >= BOLD_RUN_MIN:
                hits.append({
                    "detector": "bold-lead",
                    "file": path,
                    "line": run[0].start + 1,
                    "end": run[-1].end + 1,
                    "n": len(run),
                    "note": "%d consecutive bold-lead bullets" % len(run),
                    "quote": lines[run[0].start].strip()[:110],
                })
            run = []
    return hits


# ------------------------------------------------------------------ detector 2
def d_uniform(path, lines, kinds):
    hits = []
    for g in list_groups(lines, kinds):
        items = g["items"]
        if len(items) < UNIFORM_MIN_ITEMS:
            continue
        lens = [visible_len(it.text) for it in items]
        mean = statistics.fmean(lens)
        if mean < UNIFORM_MIN_MEAN_CHARS:
            continue
        sd = statistics.pstdev(lens)
        cv = sd / mean
        if cv > UNIFORM_CV_MAX:
            continue
        hits.append({
            "detector": "uniform",
            "file": path,
            "line": items[0].start + 1,
            "end": items[-1].end + 1,
            "n": len(items),
            "cv": round(cv, 3),
            "mean": round(mean, 1),
            "note": "%d items, mean %.0f chars, CV %.3f" % (len(items), mean, cv),
            "quote": lines[items[0].start].strip()[:110],
        })
    return hits


# ------------------------------------------------------------------ sections
def sections(lines, kinds):
    """Split a file into sections, one per ATX heading.

    Setext headings are not read. The corpus uses ATX only, and a bare === or ---
    underline is also a horizontal rule, so guessing costs more than it returns.
    """
    heads = [i for i, k in enumerate(kinds) if k == "heading"]
    out = []
    for pos, i in enumerate(heads):
        m = HEADING_RE.match(lines[i])
        end = heads[pos + 1] if pos + 1 < len(heads) else len(lines)
        out.append({"line": i, "level": len(m.group(1)), "title": m.group(2),
                    "body": (i + 1, end)})
    return out


PROSE_KINDS = ("text", "list")


def paragraphs(lines, kinds, a, b):
    """Prose paragraphs inside a line range. Layout and code never reach here."""
    out = []
    cur = []
    for i in range(a, min(b, len(lines))):
        if kinds[i] in PROSE_KINDS:
            cur.append(i)
        else:
            if cur:
                out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def para_text(lines, idx):
    body = " ".join(lines[i].strip() for i in idx)
    m = LIST_RE.match(body)
    if m:
        body = m.group(4)
    return " ".join(body.split())


SENT_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'`(])")


def first_sentence(text):
    parts = SENT_END_RE.split(text, 1)
    return parts[0] if parts else text


# ------------------------------------------------------------------ detector 3
FUNCTION_WORDS = {
    "the", "a", "an", "this", "that", "these", "those", "it", "there",
    "we", "you", "i", "they", "he", "she", "each", "every", "all", "no",
    "not", "none", "both", "either", "neither", "any", "some", "one", "two",
    "in", "on", "at", "by", "for", "with", "from", "to", "of", "after",
    "before", "under", "over", "into", "across", "per", "via", "without",
    "within", "between", "when", "where", "if", "because", "since", "while",
    "is", "are", "was", "were", "be", "been", "being", "has", "have", "had",
    "do", "does", "did", "can", "may", "must", "should", "will", "would",
    "shall", "could", "and", "or", "but", "so", "as", "than", "then",
}
AUXES = {"is", "are", "was", "were", "be", "been", "being", "has", "have", "had",
         "do", "does", "did"}
MODALS = {"can", "may", "must", "should", "will", "would", "shall", "could"}


def tok_class(tok):
    if not tok:
        return "NONE"
    if tok.startswith("`"):
        return "CODE"
    bare = tok.strip("`*_\"'(),.;:").lower()
    if not bare:
        return "PUNCT"
    if bare.replace(".", "").replace(",", "").isdigit():
        return "NUM"
    if bare in AUXES:
        return "AUX"
    if bare in MODALS:
        return "MOD"
    if bare in FUNCTION_WORDS:
        return "FUNC"
    if bare.endswith("ing") and len(bare) > 5:
        return "ING"
    if tok.strip("`*_\"'(),.;:").isupper() and len(bare) > 1:
        return "ABBR"
    return "WORD"


def opening_shape(text):
    toks = text.split()[:3]
    if len(toks) < 2:
        return None
    head = toks[0].strip("`*_\"'(),.;:").lower()
    key = head if head in FUNCTION_WORDS else tok_class(toks[0])
    return (key, tok_class(toks[1]), tok_class(toks[2]) if len(toks) > 2 else "NONE")


def informative(shape):
    """Reject a signature that says nothing.

    WORD is the catch-all class, so (WORD, WORD, WORD) matches most English
    sentences and groups sections that share no shape at all. A signature counts
    only when the head is a function word, or when two of the three positions
    carry a real class.
    """
    key, c2, c3 = shape
    if key in FUNCTION_WORDS:
        return True
    return sum(1 for c in (key, c2, c3) if c not in ("WORD", "NONE")) >= 2


def d_templated(path, lines, kinds):
    hits = []
    secs = sections(lines, kinds)
    # Siblings only. Sections that share a parent heading are a set the writer
    # laid out together. Two sections 1000 lines apart are not.
    stack = []
    for idx, s in enumerate(secs):
        while stack and secs[stack[-1]]["level"] >= s["level"]:
            stack.pop()
        s["parent"] = stack[-1] if stack else -1
        stack.append(idx)
    families = {}
    for s in secs:
        paras = paragraphs(lines, kinds, s["body"][0], s["body"][1])
        if not paras:
            continue
        text = first_sentence(para_text(lines, paras[0]))
        shape = opening_shape(text)
        if shape is None or not informative(shape):
            continue
        families.setdefault((s["parent"], s["level"]), []).append((s, shape, text))
    for (_parent, level), members in sorted(families.items()):
        by_shape = {}
        for s, shape, text in members:
            by_shape.setdefault(shape, []).append((s, text))
        for shape, group in by_shape.items():
            # A shape must cover most of the family. Three matches out of twenty
            # siblings is coincidence, three out of four is a template.
            if len(group) < TEMPLATE_MIN_SECTIONS:
                continue
            if len(group) * 2 < len(members):
                continue
            hits.append({
                "detector": "templated",
                "file": path,
                "line": group[0][0]["line"] + 1,
                "end": group[-1][0]["line"] + 1,
                "n": len(group),
                "shape": " ".join(shape),
                "note": "%d of %d h%d siblings open on '%s'"
                        % (len(group), len(members), level, " ".join(shape)),
                "quote": group[0][1][:110],
            })
    return hits


# ------------------------------------------------------------------ detector 4
def content_words(text):
    text = INLINE_CODE_RE.sub(" ", text)
    out = set()
    for w in WORD_RE.findall(text.lower()):
        if len(w) < 4 or w in FUNCTION_WORDS:
            continue
        out.add(w.rstrip("s") if len(w) > 4 and w.endswith("s") else w)
    return out


def d_restating(path, lines, kinds):
    hits = []
    for s in sections(lines, kinds):
        paras = paragraphs(lines, kinds, s["body"][0], s["body"][1])
        if len(paras) < 2:
            continue
        last_idx = paras[-1]
        # A closer is a paragraph, not the tail item of a list.
        if kinds[last_idx[0]] == "list":
            continue
        last = para_text(lines, last_idx)
        words = len(WORD_RE.findall(last))
        if words > RESTATE_MAX_WORDS:
            continue
        cw = content_words(last)
        if len(cw) < RESTATE_MIN_CONTENT:
            continue
        head = content_words(s["title"])
        opener = content_words(first_sentence(para_text(lines, paras[0])))
        r_head = len(cw & head) / len(cw) if head else 0.0
        r_open = len(cw & opener) / len(cw) if opener else 0.0
        best = max(r_head, r_open)
        if best < RESTATE_OVERLAP_MIN:
            continue
        hits.append({
            "detector": "restating",
            "file": path,
            "line": last_idx[0] + 1,
            "end": last_idx[-1] + 1,
            "overlap": round(best, 2),
            "against": "heading" if r_head >= r_open else "first sentence",
            "note": "closing paragraph repeats its %s, overlap %.0f%%"
                    % ("heading" if r_head >= r_open else "first sentence",
                       best * 100),
            "quote": last[:110],
        })
    return hits


# ------------------------------------------------------------------ prose model
# The four rhythm detectors measure prose and nothing else. A list item, a table
# cell, a heading and a fenced block all have a length the writer did not choose
# freely, so counting them would measure the layout a second time. What reaches
# these four is a run of "text" lines that no list item swallowed.

MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
AUTOLINK_RE = re.compile(r"<https?://[^>]*>|https?://\S+")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?])[\"')\]]*\s+")
# A period after one of these does not end a sentence. A single letter covers an
# initial, "J. Smith", and the abbreviations cover the ones this corpus uses.
ABBREVIATIONS = {"e.g", "i.e", "etc", "vs", "cf", "fig", "no", "approx", "incl",
                 "al", "ca", "eq", "ref", "vol", "ch", "sec", "mr", "mrs", "dr",
                 "st", "jr", "sr", "inc", "ltd", "co", "op", "resp"}


def flatten_prose(s):
    """One prose string with the markup out and every code span made one token.

    A path in backticks must not count as six words, and the same sentence
    written with and without the backticks must measure the same length.
    """
    s = INLINE_CODE_RE.sub(" CODE ", s)
    s = MD_LINK_RE.sub(lambda m: m.group(1) or " ", s)
    s = AUTOLINK_RE.sub(" URL ", s)
    s = s.replace("**", "").replace("__", "")
    return " ".join(s.split())


def split_sentences(text):
    """Split flattened prose into sentences.

    The split needs whitespace after the stop, so 0.12 and v1.2.3 survive whole.
    A stop that follows an abbreviation or a single letter rejoins the piece that
    follows it.
    """
    out = []
    buf = ""
    for piece in SENT_SPLIT_RE.split(text):
        buf = (buf + " " + piece).strip() if buf else piece
        tail = buf.rstrip("\"')]").rstrip()
        if not tail:
            continue
        last = tail.split()[-1]
        core = last.rstrip(".!?").strip("\"')]")
        low = core.lower()
        if low in ABBREVIATIONS or (len(core) == 1 and core.isalpha()):
            continue
        out.append(buf)
        buf = ""
    if buf.strip():
        out.append(buf)
    return out


def list_line_set(lines, kinds):
    """Every line a list item owns, its folded continuation lines included."""
    used = set()
    for g in list_groups(lines, kinds):
        for it in g["items"]:
            for i in range(it.start, it.end + 1):
                used.add(i)
    return used


def prose_paragraphs(lines, kinds):
    """Maximal runs of text lines that no list item swallowed, as line indices."""
    used = list_line_set(lines, kinds)
    out = []
    cur = []
    for i, k in enumerate(kinds):
        if k == "text" and i not in used:
            cur.append(i)
        else:
            if cur:
                out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def prose_text(lines, idx):
    return flatten_prose(" ".join(lines[i].strip() for i in idx))


def prose_sentences(lines, idx, min_words=3):
    """Sentences of one paragraph, each carrying at least min_words words.

    A fragment shorter than that is a caption or a stub and would distort every
    spread it entered.
    """
    out = []
    for s in split_sentences(prose_text(lines, idx)):
        if len(WORD_RE.findall(s)) >= min_words:
            out.append(s)
    return out


def coeff_var(values):
    """Spread as a share of the mean. None when the mean is zero."""
    mean = statistics.fmean(values)
    if mean <= 0:
        return None
    return statistics.pstdev(values) / mean


# ------------------------------------------------------------------ detector 5
def d_sent_rhythm(path, lines, kinds):
    """Sentence-length spread, per paragraph and once for the whole document."""
    hits = []
    doc_lens = []
    for idx in prose_paragraphs(lines, kinds):
        sents = prose_sentences(lines, idx)
        lens = [len(WORD_RE.findall(s)) for s in sents]
        doc_lens += lens
        if len(lens) < SENT_MIN_SENTENCES:
            continue
        mean = statistics.fmean(lens)
        if mean < SENT_MIN_MEAN_WORDS:
            continue
        cv = coeff_var(lens)
        if cv is None or cv > SENT_CV_MAX:
            continue
        hits.append({
            "detector": "sent-rhythm",
            "file": path,
            "line": idx[0] + 1,
            "end": idx[-1] + 1,
            "scope": "paragraph",
            "n": len(lens),
            "cv": round(cv, 3),
            "lens": lens,
            "note": "%d sentences, %s words, CV %.3f"
                    % (len(lens), lens, cv),
            "quote": sents[0][:110],
        })
    if len(doc_lens) >= SENT_DOC_MIN_SENTENCES:
        cv = coeff_var(doc_lens)
        if cv is not None and cv <= SENT_DOC_CV_MAX:
            hits.append({
                "detector": "sent-rhythm",
                "file": path,
                "line": 1,
                "end": 1,
                "scope": "document",
                "n": len(doc_lens),
                "cv": round(cv, 3),
                "note": "whole document: %d sentences, mean %.1f words, CV %.3f"
                        % (len(doc_lens), statistics.fmean(doc_lens), cv),
                "quote": os.path.basename(path),
            })
    return hits


# ------------------------------------------------------------------ detector 6
def d_para_rhythm(path, lines, kinds):
    """Paragraph-length spread, per section and once for the whole document."""
    hits = []
    paras = prose_paragraphs(lines, kinds)
    sized = [(p, len(WORD_RE.findall(prose_text(lines, p)))) for p in paras]
    for s in sections(lines, kinds):
        a, b = s["body"]
        lens = [w for p, w in sized if p[0] >= a and p[-1] < b
                and w >= PARA_MIN_WORDS]
        if len(lens) < PARA_MIN_PARAS:
            continue
        cv = coeff_var(lens)
        if cv is None or cv > PARA_CV_MAX:
            continue
        hits.append({
            "detector": "para-rhythm",
            "file": path,
            "line": s["line"] + 1,
            "end": min(b, len(lines)),
            "scope": "section",
            "n": len(lens),
            "cv": round(cv, 3),
            "lens": lens,
            "note": "%d paragraphs under '%s', %s words, CV %.3f"
                    % (len(lens), s["title"][:40], lens, cv),
            "quote": s["title"][:110],
        })
    doc = [w for _p, w in sized if w >= PARA_MIN_WORDS]
    if len(doc) >= PARA_DOC_MIN_PARAS:
        cv = coeff_var(doc)
        if cv is not None and cv <= PARA_DOC_CV_MAX:
            hits.append({
                "detector": "para-rhythm",
                "file": path,
                "line": 1,
                "end": 1,
                "scope": "document",
                "n": len(doc),
                "cv": round(cv, 3),
                "note": "whole document: %d paragraphs, mean %.1f words, CV %.3f"
                        % (len(doc), statistics.fmean(doc), cv),
                "quote": os.path.basename(path),
            })
    return hits


# ------------------------------------------------------------------ detector 7
def opener_keys(sent):
    """(literal first word, determiner shape) for one sentence.

    An identifier opener is not an opener the writer chose: a sentence starting
    on a backticked symbol or an all-caps token repeats because the subject
    repeats. Both keys come back None for those.
    """
    toks = sent.split()[:2]
    if len(toks) < 2:
        return None, None
    if toks[0].startswith("`"):
        return None, None
    head = toks[0].strip("`*_\"'(),.;:-")
    if not head or not head.replace("-", "").replace("'", "").isalpha():
        return None, None
    if head.isupper() and len(head) > 1:
        return None, None
    low = head.lower()
    shape = None
    if low in DETERMINERS and tok_class(toks[1]) == "WORD":
        shape = "DET+NOUN"
    return low, shape


def _runs(keyed):
    """Maximal runs of equal, non-None keys. Yields (key, start, count)."""
    out = []
    cur_key = None
    start = 0
    count = 0
    for i, k in enumerate(keyed + [None]):
        if k is not None and k == cur_key:
            count += 1
            continue
        if count >= 2:
            out.append((cur_key, start, count))
        cur_key, start, count = (k, i, 1) if k is not None else (None, i, 0)
    return out


def d_opener_run(path, lines, kinds):
    hits = []
    for idx in prose_paragraphs(lines, kinds):
        sents = prose_sentences(lines, idx)
        if len(sents) < OPENER_WORD_RUN_MIN:
            continue
        keys = [opener_keys(s) for s in sents]
        words = [k[0] for k in keys]
        shapes = [k[1] for k in keys]
        claimed = set()
        found = []
        for key, start, count in _runs(words):
            floor = OPENER_WORD_RUN_MIN if key not in ARTICLES else OPENER_RUN_MIN
            if count < floor:
                continue
            found.append(("word", "'%s'" % key, start, count))
            claimed.update(range(start, start + count))
        for key, start, count in _runs(shapes):
            if count < OPENER_RUN_MIN:
                continue
            # A determiner run already reported as one repeated word adds nothing.
            if all(i in claimed for i in range(start, start + count)):
                continue
            found.append(("shape", "determiner + noun", start, count))
        for kind, label, start, count in sorted(found, key=lambda x: x[2]):
            hits.append({
                "detector": "opener-run",
                "file": path,
                "line": idx[0] + 1,
                "end": idx[-1] + 1,
                "scope": kind,
                "n": count,
                "key": label,
                "note": "%d consecutive sentences open on %s" % (count, label),
                "quote": " / ".join(s.split()[0] + " " + s.split()[1]
                                    for s in sents[start:start + count])[:110],
            })
    return hits


# ------------------------------------------------------------------ detector 8
def d_comma_rhythm(path, lines, kinds):
    hits = []
    for idx in prose_paragraphs(lines, kinds):
        sents = prose_sentences(lines, idx)
        if len(sents) < COMMA_MIN_SENTENCES:
            continue
        counts = [s.count(",") for s in sents]
        mode = statistics.mode(counts)
        if mode < COMMA_MIN_COUNT:
            continue
        share = counts.count(mode) / len(counts)
        if share < COMMA_SHARE_MIN:
            continue
        hits.append({
            "detector": "comma-rhythm",
            "file": path,
            "line": idx[0] + 1,
            "end": idx[-1] + 1,
            "n": len(counts),
            "commas": mode,
            "share": round(share, 2),
            "note": "%d of %d sentences carry exactly %d comma(s)"
                    % (counts.count(mode), len(counts), mode),
            "quote": sents[0][:110],
        })
    return hits


DETECTOR_FN = {
    "bold-lead": d_bold_lead,
    "uniform": d_uniform,
    "templated": d_templated,
    "restating": d_restating,
    "sent-rhythm": d_sent_rhythm,
    "para-rhythm": d_para_rhythm,
    "opener-run": d_opener_run,
    "comma-rhythm": d_comma_rhythm,
}


def check(path, raw, enabled):
    lines, kinds = scan(raw)
    hits = []
    for name in DETECTORS:
        if name in enabled:
            hits += DETECTOR_FN[name](path, lines, kinds)
    hits.sort(key=lambda h: (h["line"], h["detector"]))
    return hits


USAGE = """usage: md-structure.py [--json] [--quiet] [--uniform] [--templated]
                       [--restating] [--sent-rhythm] [--para-rhythm]
                       [--opener-run] [--comma-rhythm] [--all] FILE...

Report document-level AI tells that a line-level linter cannot see.
Exit 1 when anything fires, 0 when clean, 2 on a usage error.

LAYOUT tells, in how the page is built:
  bold-lead     3+ consecutive bullets shaped  - **Term** - explanation
                ON. 10 hand-checked on the audit corpus, 1 false.
  uniform       4+ bullets of near-identical length, CV <= 0.12
                OFF, 50% false. Parallel construction is not a tell.
  templated     3+ sibling sections opening on one grammatical shape
                OFF, 67% false. It cannot see a house convention.
  restating     a closing paragraph that repeats its own heading
                OFF, 100% false on one hit. No corpus document does this.

RHYTHM tells, in how long the sentences and paragraphs run:
  sent-rhythm   sentence word-counts in one paragraph, CV <= 0.20
                OFF, 90% false. The measured spread does not separate
                hand-written from agent-written prose in this corpus.
  para-rhythm   paragraph word-counts in one section, CV <= 0.20
                OFF, 100% false. Same overlap, and CV understates the
                spread once the paragraphs are long.
  opener-run    4+ sentences opening on one word or on determiner + noun,
                3+ when the repeated word is not a bare article
                OFF, 60% false. Real repetitions, but this corpus shows
                them 4x more often in the hand-edited documents.
  comma-rhythm  every sentence of a paragraph at one non-zero comma count
                OFF, 100% false on 2 hits. Already at its strictest cut.

  --uniform --templated --restating --sent-rhythm --para-rhythm
  --opener-run --comma-rhythm         turn one off-by-default detector on
  --all        turn every detector on
  --json       print one JSON object instead of the text report
  --quiet      print the per-file and corpus totals only
"""


def main(argv):
    args = list(argv)
    if "-h" in args or "--help" in args:
        print(USAGE)
        return 0
    as_json = "--json" in args
    quiet = "--quiet" in args
    enabled = set(d for d in DETECTORS if d not in DEFAULT_OFF)
    if "--all" in args:
        enabled = set(DETECTORS)
    for d in DEFAULT_OFF:
        if "--" + d in args:
            enabled.add(d)
    known = {"--json", "--quiet", "--all", "-h", "--help"} | \
            set("--" + d for d in DETECTORS)
    files = []
    for a in args:
        if a.startswith("--"):
            if a not in known:
                sys.stderr.write("md-structure: unknown flag %s\n" % a)
                return 2
            continue
        files += sorted(glob.glob(a)) if any(c in a for c in "*?[") else [a]
    if not files:
        sys.stderr.write(USAGE)
        return 2
    all_hits = []
    per_file = []
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                raw = fh.read()
        except OSError as e:
            sys.stderr.write("md-structure: cannot read %s: %s\n" % (f, e))
            continue
        hits = check(f, raw, enabled)
        all_hits += hits
        per_file.append((f, hits))
    counts = {d: sum(1 for h in all_hits if h["detector"] == d) for d in DETECTORS}
    if as_json:
        print(json.dumps({
            "enabled": sorted(enabled),
            "files": len(per_file),
            "total": len(all_hits),
            "by_detector": counts,
            "hits": all_hits,
        }, indent=2))
        return 1 if all_hits else 0
    for f, hits in per_file:
        if not hits and quiet:
            continue
        if not hits:
            continue
        print("%-46s %d" % (os.path.basename(f), len(hits)))
        if quiet:
            continue
        for h in hits:
            span = ("%d" % h["line"]) if h["end"] == h["line"] \
                else "%d-%d" % (h["line"], h["end"])
            print("  %-13s %-9s %s" % (h["detector"], span, h["note"]))
            print("             %s" % h["quote"])
    print("\n%d file(s), %d hit(s): %s"
          % (len(per_file), len(all_hits),
             ", ".join("%s=%d" % (d, counts[d]) for d in DETECTORS
                       if d in enabled)))
    off = [d for d in DETECTORS if d not in enabled]
    if off:
        print("off by default (too noisy): %s" % ", ".join(off))
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
