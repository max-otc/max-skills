import re, sys, json, glob, os, time

MARKETING = ["seamless","seamlessly","robust","powerful","cutting-edge","effortless","effortlessly",
    "world-class","next-generation","revolutionary","blazing","lightning-fast","elegant","delightful",
    "turnkey","best-in-class","state-of-the-art","game-changing","first-class","battle-tested",
    "enterprise-grade","supercharge","unlock","unleash","empower","empowers"]
BANNED = ["begin","begins","commence","commences","initiate","initiates","originate",
    "utilize","utilizes","utilizing","leverage","leverages","leveraging","facilitate","facilitates",
    "ensure","ensures","ensuring","prior to","subsequent to","obtain","obtains","acquire","acquires",
    "demonstrate","demonstrates","additionally","furthermore","moreover","comprehensive","comprehensively",
    "utilization","aforementioned","henceforth","therein","whilst","amongst","numerous","myriad","plethora",
    "in order to","a variety of","in the event that","due to the fact that","it is important to note"]
PHRASAL = ["spin up","spin down","reach out","dive into","dives into","diving into","kick off","kicks off",
    "roll out","rolls out","tear down","ramp up","circle back","drill down","spun up","reaching out"]
MODAL_HEDGE = ["it is important to note","it should be noted","it is worth noting","please note that",
    "as mentioned","as noted above"]
WORDS_PATH = os.environ.get(
    "STE_WORDS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt"))
SECTIONS = ("banned", "marketing", "phrasal", "hedge", "address", "pattern", "allow",
            "compound-allow", "term-of-art")
CUSTOM_CATS = ("banned", "marketing", "phrasal", "hedge")  # roll up into custom_word
ADDRESS_CAT = "address"                                     # scored as second_person
PATTERN_CAT = "pattern"                                     # scored as pattern_hit
CALLOW_CAT = "compound-allow"                               # names a [pattern] may not flag
TOA_CAT = "term-of-art"                                     # hyphenations that are JARGON
NAME_CATS = (CALLOW_CAT, TOA_CAT)                           # both take one token per line
OPTIONS_CAT = "options"                                     # key = value settings
# Sections the reader accepts. [options] is NOT in SECTIONS, so --ban cannot write
# a word into it.
PARSE_SECTIONS = SECTIONS + (OPTIONS_CAT,)
SECTION_RE = re.compile(r"^\[([A-Za-z][A-Za-z-]*)\]$")
OPTION_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)\s*=\s*(.+?)$")
# Defaults ARE the upstream behaviour. A missing words.txt, or a missing key, scores
# exactly what the published numbers say.
DEFAULT_OPTIONS = {
    "possessive": "flag",             # 's is a possessive, not a contraction
    "identifier_apostrophe": "flag",  # delegatecall'd is a code identifier, not a verb
    "code_token": "flag",             # mask identifiers, version pins, numeric ranges
    "markdown_structure": "flag",     # a table cell and a list item are not a paragraph
    "partial_token": "flag",          # report the whole compound, never a fragment
    "module_tag": "flag",             # "fold-gate: stale" opens with a log namespace
    "prefix_propernoun": "flag",      # pre-Cancun is a prefix on a NAME, not prose
    "term_of_art": "flag",            # [term-of-art] names a hyphenation to exempt
}
OPTION_VALUES = {k: ("flag", "allow") for k in DEFAULT_OPTIONS}
ARROW_RE = re.compile(r"\s+->\s+")   # spaced arrow, so a regex may contain a bare ->
PATTERN_BUDGET_MS = 100.0
_BACKTRACK_SAMPLE = ("the quick brown fox-jumps over re-lazy dogs and on-chain "
                     "anchors 2020-2024 --json https://a-b.com/x-y " * 120)[:10240]
SECTION_TEMPLATE = """# Custom word rules. Add a line, save. No restart, no code edit.
# Format:  phrase -> replacement          (replacement is optional)
# Case-insensitive. Multi-word phrases work. Lines starting with # are ignored.
#
# [banned]     words to replace with a plainer one   e.g.  torn up -> damaged
# [marketing]  sales adjectives with no meaning      e.g.  frictionless -> simple
# [phrasal]    two-word verbs to replace with one    e.g.  stand up -> start
# [hedge]      filler that delays the sentence       e.g.  it goes without saying -> delete
# [allow]      turn OFF a built-in rule you disagree with (phrase only, no arrow)
# [compound-allow]  names a [pattern] rule may never flag: EIP-712, forge-std.
#              One token per line, or a prefix family: EIP-*. Whole token only.
# [term-of-art]  hyphenations that are JARGON, not names. Read only when
#              term_of_art = allow, which is NOT the default. Same one-token form.
# [options]    tune a built-in rule. One  key = value  per line. Every key takes
#              flag or allow. flag is upstream behaviour and is the default.
#
#   possessive             token's mark is a possessive, not a contraction
#   identifier_apostrophe  delegatecall'd is a code identifier, not a verb
#   code_token             mask identifiers, version pins, and numeric ranges
#   markdown_structure     a table cell and a list item are not a paragraph
#   partial_token          report the whole compound, never a fragment of it
#   module_tag             "fold-gate: stale" opens with a log namespace
#   prefix_propernoun      pre-Cancun is a closed prefix on a NAME, not prose
#   term_of_art            read the [term-of-art] list and exempt what it names

[options]
possessive = flag
identifier_apostrophe = flag
code_token = flag
markdown_structure = flag
partial_token = flag
module_tag = flag
prefix_propernoun = flag
term_of_art = flag

[banned]

[marketing]

[phrasal]

[hedge]

[allow]

[compound-allow]

[term-of-art]
"""


def compile_pattern(src, path="<none>", n=0):
    """Compile one [pattern] regex. A bad or slow pattern warns and is skipped."""
    try:
        comp = re.compile(src, re.I)
    except re.error as e:
        sys.stderr.write("ste-lint: %s line %d: bad regex %r (%s), skipped\n"
                         % (path, n, src, e))
        return False, None
    try:
        t0 = time.time()
        comp.findall(_BACKTRACK_SAMPLE)
        ms = (time.time() - t0) * 1000.0
    except Exception as e:
        sys.stderr.write("ste-lint: %s line %d: regex %r failed to run (%s), skipped\n"
                         % (path, n, src, e))
        return False, None
    if ms > PATTERN_BUDGET_MS:
        sys.stderr.write("ste-lint: %s line %d: regex %r took %.0fms on a 10KB sample, "
                         "above the %.0fms budget, skipped\n"
                         % (path, n, src, ms, PATTERN_BUDGET_MS))
        return False, None
    return True, comp


def load_words(path=None):
    """Read the user wordlist. A missing file is not an error, it means no custom rules."""
    path = path or WORDS_PATH
    custom = {"banned": [], "marketing": [], "phrasal": [], "hedge": [], "address": []}
    fixes, allow, patterns = {}, set(), []
    names = {CALLOW_CAT: [], TOA_CAT: []}
    options = dict(DEFAULT_OPTIONS)
    if not path or not os.path.isfile(path):
        return custom, fixes, allow, patterns, options, names
    sec = None
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            raw_lines = fh.readlines()
    except OSError as e:
        sys.stderr.write("ste-lint: cannot read %s: %s\n" % (path, e))
        return custom, fixes, allow, patterns, options, names
    for n, raw in enumerate(raw_lines, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = SECTION_RE.match(line)
        if m:
            key = m.group(1).lower()
            if key not in PARSE_SECTIONS:
                sys.stderr.write("ste-lint: %s line %d: unknown section [%s], skipped\n"
                                 % (path, n, m.group(1)))
                sec = None
            else:
                sec = key
            continue
        if line.startswith("[") or line.endswith("]"):
            sys.stderr.write("ste-lint: %s line %d: malformed section header, skipped\n"
                             % (path, n))
            continue
        if sec is None:
            sys.stderr.write("ste-lint: %s line %d: entry before any section, skipped\n"
                             % (path, n))
            continue
        if sec == OPTIONS_CAT:
            # key = value. An unknown key or value warns and keeps the default, so a
            # typo never changes a score and never stops the run.
            om = OPTION_RE.match(line)
            if not om:
                sys.stderr.write("ste-lint: %s line %d: malformed option %r, "
                                 "expected  key = value, skipped\n" % (path, n, line))
                continue
            okey = om.group(1).strip().lower()
            oval = om.group(2).strip().lower()
            if okey not in DEFAULT_OPTIONS:
                sys.stderr.write("ste-lint: %s line %d: unknown option %r, skipped. "
                                 "Known: %s\n"
                                 % (path, n, okey, ", ".join(sorted(DEFAULT_OPTIONS))))
                continue
            if oval not in OPTION_VALUES[okey]:
                sys.stderr.write("ste-lint: %s line %d: option %s takes one of %s, "
                                 "got %r, skipped. %s stays %r\n"
                                 % (path, n, okey, "|".join(OPTION_VALUES[okey]),
                                    oval, okey, options[okey]))
                continue
            options[okey] = oval
            continue
        # Split on a SPACED arrow so a regex may contain a bare -> of its own.
        bits = ARROW_RE.split(line, 1)
        raw_phrase = bits[0].strip()
        repl = bits[1].strip() if len(bits) > 1 else ""
        if not raw_phrase:
            sys.stderr.write("ste-lint: %s line %d: empty phrase, skipped\n" % (path, n))
            continue
        if sec == PATTERN_CAT:
            ok, comp = compile_pattern(raw_phrase, path, n)
            if ok:
                patterns.append((raw_phrase, comp))
                if repl:
                    fixes[raw_phrase] = repl
            continue
        if sec in NAME_CATS:
            # A name, not a phrase. One token per line, or one prefix family ending
            # in *. Whitespace inside means the writer meant prose, so it is refused
            # rather than silently matching nothing.
            if len(bits) > 1:
                sys.stderr.write("ste-lint: %s line %d: [%s] takes a name "
                                 "only, the replacement was ignored\n" % (path, n, sec))
            if len(raw_phrase.split()) > 1:
                sys.stderr.write("ste-lint: %s line %d: [%s] takes one "
                                 "token, got %r, skipped\n" % (path, n, sec, raw_phrase))
                continue
            low = raw_phrase.lower()
            if low not in names[sec]:
                names[sec].append(low)
            continue
        phrase = " ".join(raw_phrase.split()).lower()
        if sec == "allow":
            if len(bits) > 1:
                sys.stderr.write("ste-lint: %s line %d: [allow] takes a phrase only, "
                                 "the replacement was ignored\n" % (path, n))
            allow.add(phrase)
            continue
        if phrase not in custom[sec]:
            custom[sec].append(phrase)
        if repl:
            fixes[phrase] = repl
    return custom, fixes, allow, patterns, options, names


CUSTOM, FIXES, ALLOW, PATTERNS, OPTIONS, NAMES = load_words()
CALLOW = NAMES[CALLOW_CAT]
TOA = NAMES[TOA_CAT]


def effective(builtin):
    """Built-in list minus anything the user turned off in [allow]."""
    return [w for w in builtin if w.lower() not in ALLOW]


def custom_phrases():
    """Custom entries that roll up into custom_word. Second person is scored apart."""
    return [p for cat in CUSTOM_CATS for p in CUSTOM.get(cat, []) if p not in ALLOW]


def address_phrases():
    return [p for p in CUSTOM.get(ADDRESS_CAT, []) if p not in ALLOW]


def show_fix(phrase):
    """Print the user's replacement when they wrote one. A bare entry prints bare."""
    repl = FIXES.get(phrase)
    return "%s -> %s" % (phrase, repl) if repl else phrase


# The 's is the one ambiguous ending in English. It is a contraction in "it's ready"
# and a possessive in "the token's mark". Every other ending (-'t -'re -'ve -'ll -'d
# -'m) is always a contraction, so only 's needs a list.
CONTRACTION_RE = re.compile(r"\b\w+['’](?:t|re|ve|ll|d|s|m)\b")
S_CONTRACTIONS = frozenset([
    "it's", "that's", "there's", "here's", "what's", "who's", "let's",
    "he's", "she's", "how's", "where's", "when's", "why's",
])


def opt(key):
    """One option value. An absent key reads as the upstream default."""
    return OPTIONS.get(key, DEFAULT_OPTIONS.get(key, "flag"))


# Words that carry an apostrophe because a writer put a code identifier into a
# sentence: delegatecall'd, keccak'd, abi.encode'd. The stem is not an English verb.
CODE_BUILTINS = frozenset("""
delegatecall staticcall call callcode selfdestruct keccak sha256 ripemd ecrecover
abi msg tx block calldata memory storage mapping payable immutable constant
uint uint8 uint16 uint32 uint64 uint128 uint256 int256 bytes bytes32 bytes4 address
require revert assert emit modifier struct enum interface library contract
sload sstore mload mstore create2 extcodesize returndata gasleft
unwrap wrap serde clone deref unsafe async await impl trait enum crate
json yaml toml regex api url uri http https sql cli env repo diff
""".split())
CAMEL_RE = re.compile(r"[a-z][A-Z]")


def is_identifier_apostrophe(token, context=""):
    """True when the word before the apostrophe is a code identifier, not a verb.

    Structural, not a word list: camelCase, snake_case, a digit inside, a known
    language builtin, or a stem the surrounding text uses as an identifier
    (preceded by a dot, or called with brackets somewhere in the same chunk).
    """
    tok = token.replace("’", "'")
    stem = tok.split("'")[0]
    if not stem:
        return False
    if "_" in stem or any(c.isdigit() for c in stem) or CAMEL_RE.search(stem):
        return True
    if stem.lower() in CODE_BUILTINS:
        return True
    if context:
        # abi.encode'd -> the stem is a member, so it is an identifier.
        for m in re.finditer(re.escape(tok), context):
            if m.start() and context[m.start() - 1] in "._":
                return True
        if re.search(r"(?<![A-Za-z])" + re.escape(stem) + r"\s*\(", context):
            return True
    return False


def count_contractions(text, possessive="flag", identifier_apostrophe="flag"):
    """Count contractions. Two options narrow what counts as one.

    possessive='allow' drops the possessive 's. identifier_apostrophe='allow' drops
    an apostrophe hung on a code identifier. Both default to 'flag', which is
    upstream: every match counts, and the published numbers depend on it.
    """
    n = 0
    for m in CONTRACTION_RE.finditer(text):
        tok = m.group(0).replace("’", "'").lower()
        if possessive == "allow" and tok.endswith("'s") and tok not in S_CONTRACTIONS:
            continue
        if identifier_apostrophe == "allow" and is_identifier_apostrophe(m.group(0), text):
            continue
        n += 1
    return n


# ------------------------------------------------------------------ code tokens
# Spans that are code, not prose. Masking them stops a [pattern] rule from firing
# on a name no writer may rewrite: a version pin, a target triple, an identifier,
# a numeric range. Every one of these was measured on a real Solidity repo.
# A signal only. The span then grows to the whole compound it sits in, so one
# code-shaped part carries the rest with it: the `x86_64` in `x86_64-apple-darwin`
# and the `v5` in `sp1-v5.2.1` both take their whole name out of scoring.
# Order matters. The ranges come FIRST: at the `4` of `4–9` the range alternative
# must win, or the bare-number alternative claims the `4` alone and leaves the dash
# behind for the punctuation rule to charge for.
CODE_SIGNAL_RE = re.compile(
    r"[§#]\s*\d+\s*[–—-]\s*[§#]?\s*\d+"               # §1–§13, #1–#16
    r"|\d+\s*[–—-]\s*\d+"                             # numeric range: 4-9, 12–14
    r"|\b0[xX][0-9a-fA-F]+\b"                         # hex literal, address, selector
    r"|\b\w*_\w*\b"                                   # snake_case, SCREAMING_SNAKE
    r"|\b[A-Za-z][A-Za-z0-9]*[a-z][A-Z][A-Za-z0-9]*\b"  # camelCase, PascalCase
    r"|\b\w*\d\w*\b"                                  # EIP-712, terms3f2, v5
)


def mask_code_tokens(s):
    """Blank out code-shaped spans, keeping length so the shared mask stays aligned."""
    out = None
    for m in CODE_SIGNAL_RE.finditer(s):
        a, b = widen_token(s, m.start(), m.end())
        if out is None:
            out = list(s)
        for i in range(a, b):
            out[i] = " "
    return s if out is None else "".join(out)


# ------------------------------------------------------------ markdown structure
# A Markdown table and a list are layout, not paragraphs. Scoring them as prose
# charges a writer for furniture: an empty cell drawn as a dash, a whole table row
# read as one 40-word sentence, eight bullets read as one runaway paragraph.
MD_LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
MD_INDENT_RE = re.compile(r"^(?: {4}|\t)")
MD_TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
MD_FURNITURE_RE = re.compile(r"^[\s—–\-*·•✅❌✓✗×~]*$|^n/?a\.?$", re.I)
MD_FENCE_RE = re.compile(r"^\s*(?:```|~~~)")


def is_table_row(line):
    s = line.strip()
    return s.startswith("|") and s.count("|") >= 2


def md_clean(text):
    """Rewrite Markdown furniture out of the text before it is scored.

    Three moves, and nothing else. A table row becomes one line per cell, so a row
    is no longer one long sentence. A cell holding only a dash or a tick is an empty
    cell, so it is dropped. An indented code block is code, so it is dropped.
    Fenced blocks are left alone: strip_code removes them later.
    """
    out = []
    lines = text.split("\n")
    fenced = False
    prev_blank = True
    prev_listish = False
    in_indent_code = False
    for line in lines:
        if MD_FENCE_RE.match(line):
            fenced = not fenced
            out.append("")
            prev_blank = True
            continue
        if fenced:
            # Blank the body, do not delete it. strip_code drops a whole fence in one
            # move, but the paragraph rule splits on blank lines FIRST, so a fence
            # holding a blank line reaches it as two halves with no closing marker.
            out.append("")
            continue
        blank = not line.strip()
        if blank:
            out.append(line)
            prev_blank = True
            in_indent_code = False
            continue
        # An indented code block opens after a blank line, outside any list. Inside
        # a list the same indent is a nested item or a continuation, which is prose.
        if MD_INDENT_RE.match(line) and not MD_LIST_RE.match(line):
            if in_indent_code or (prev_blank and not prev_listish):
                in_indent_code = True
                out.append("")
                continue
        else:
            in_indent_code = False
        if is_table_row(line):
            if not MD_TABLE_SEP_RE.match(line):
                for cell in line.strip().strip("|").split("|"):
                    c = cell.strip()
                    if c and not MD_FURNITURE_RE.match(c):
                        out.append(c)
            prev_blank = False
            prev_listish = True
            continue
        # A list marker is layout. Left in place, the `-` of a bullet reads as a
        # hyphen used for sentence punctuation and scores as one.
        mk = MD_LIST_RE.match(line)
        out.append(line[mk.end():] if mk else line)
        prev_blank = False
        prev_listish = bool(mk)
    return "\n".join(out)


def is_structural_block(block):
    """True when a block is a list or a table, so the paragraph rule must skip it."""
    lines = [l for l in block.split("\n") if l.strip()]
    if not lines:
        return True
    n = sum(1 for l in lines if MD_LIST_RE.match(l) or is_table_row(l)
            or MD_INDENT_RE.match(l))
    return n * 5 >= len(lines) * 3   # 60% or more of the lines are furniture


BE = r"(?:am|is|are|was|were|be|been|being)"
PP_IRREG = r"(?:done|made|sent|read|built|kept|held|set|put|run|written|shown|given|taken|found|got|gotten|seen|known|thrown|drawn)"

def strip_code(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    # Backticks around a bare path:line citation are typography, not a code sample.
    # The span is kept so the citation rule reads it. Anything else inside the
    # backticks goes, exactly as upstream.
    t = re.sub(r"`[^`]*`",
               lambda m: m.group(0)[1:-1]
               if CITE_RE.fullmatch(m.group(0)[1:-1]) else " ", t)
    return t

def sentences(text):
    out = []
    for line in text.split("\n"):
        s = line.strip()
        if not s: continue
        s = re.sub(r"^\s*#{1,6}\s*", "", s)
        s = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", s)
        if not s: continue
        parts = re.split(r"(?<=[.!?:])\s+(?=[A-Z0-9\"'\-])", s)
        for p in parts:
            p = p.strip()
            if p: out.append(p)
    return out

def wc(s):
    return len([w for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-/]*", s)])

def count_ci(text, phrases):
    n = 0; hits = []
    low = text.lower()
    for ph in phrases:
        for m in re.finditer(r"(?<![a-z])" + re.escape(ph) + r"(?![a-z])", low):
            n += 1; hits.append(ph)
    return n, hits

NOISE_RE = re.compile(
    r"https?://\S+|www\.\S+"                 # URLs
    r"|\S*/\S*"                              # anything with a slash: paths, and/or
    r"|(?<![\w-])--?[A-Za-z][\w-]*"          # CLI flags: --json, -v
    r"|\b[\w-]+\.[A-Za-z]{2,5}\b"            # file names and domains
)


# A path:line citation is prose the writer chose, not a code token. Every mask
# above blanks part of one: the slash alternative takes the path, the file-name
# alternative takes `Foo.sol`, and code_token eats the digits. What reaches the
# pattern stage is blanks, indistinguishable from a clock time, so a rule written
# against the citation can never fire. The span is put back after the masks run.
CITE_RE = re.compile(
    r"\b[\w./-]+\.(?:sol|rs|sh|toml|md|py|js|ts|json|yaml|yml):\d+(?:-\d+)?\b")


def mask_noise(s):
    """Blank out non-prose spans, keeping length so the shared mask stays aligned."""
    out = NOISE_RE.sub(lambda m: " " * (m.end() - m.start()), s)
    if opt("code_token") == "allow":
        out = mask_code_tokens(out)
    keep = [m.span() for m in CITE_RE.finditer(s)]
    if keep:
        buf = list(out)
        for a, b in keep:
            buf[a:b] = s[a:b]
        out = "".join(buf)
    return out


def widen_token(text, s, e):
    """Grow a span to the whole hyphen or underscore compound it sits inside.

    `\\b[a-z]+-[a-z]+\\b` matches `byte-for` inside `byte-for-byte` and stops. The
    count is right, the reported text is not, and a rewrite driven by the fragment
    corrupts the word. Widening reports the compound whole.
    """
    while s >= 2 and text[s - 1] in "-_" and (text[s - 2].isalnum() or text[s - 2] == "_"):
        s -= 1
        while s and (text[s - 1].isalnum() or text[s - 1] == "_"):
            s -= 1
    n = len(text)
    while e + 1 < n and text[e] in "-_" and (text[e + 1].isalnum() or text[e + 1] == "_"):
        e += 1
        while e < n and (text[e].isalnum() or text[e] == "_"):
            e += 1
    return s, e


# ------------------------------------------------------ structural exemptions
# A hyphen hit is a false positive only when the token is NOT PROSE AT ALL: a
# name, or an artifact a machine wrote. Jargon is prose. `pre-Cancun`,
# `high-water` and `mark-to-market` are dense domain language, and whether to
# keep or cut them is a judgement the writer makes one instance at a time. So
# they must keep firing. A name list reaches a name. It cannot reach a SHAPE.
# These three read the shape. Each is one [options] key, and each defaults to
# flag, which is upstream: an absent words.txt scores exactly as published.

# A closed prefix. `re-` is NOT here and never will be. re-anything is banned by
# name, so `re-Cancun` must keep firing. The corpus added no prefix to this set.
PREFIXES = frozenset("""
pre post non anti mid multi semi sub inter intra pseudo quasi ultra
co counter over under extra supra trans
""".split())


def is_prefix_propernoun(tok):
    """True for pre-Cancun, post-Merge, non-EVM: a closed prefix on a NAME.

    The hyphen is mandatory orthography, not a compound the writer chose. The
    test is the CASE of the segment after the hyphen, so `pre-flight` and
    `non-zero` are ordinary prose and still flag.
    """
    head, sep, tail = tok.partition("-")
    if not sep or not tail:
        return False
    low = head.lower()
    if low == "re" or low not in PREFIXES:
        return False
    return tail[0].isupper()


def is_module_tag(text, ws, we, kind):
    """True for the `oracle-registry:` that OPENS a log or error string.

    Two locks, and both must open. The chunk must BE a string literal, which
    only the code linter can say, so it passes kind="string". And the compound
    must be position-anchored at the head of that literal with a colon behind
    it. A hyphen later in the same string is prose and still flags, and so does
    `Fail-closed: a wrong length` at the head of a DOCSTRING, because a writer
    wrote that label and a writer may rewrite it.
    """
    if kind != "string":
        return False
    return not text[:ws].strip() and text[we:we + 1] == ":"


def compound_exempt(text, ws, we, alts, kind=None):
    """True when a [pattern] hit names a thing, rather than saying one.

    Four tests. The two name lists are exact and run first. The two shape tests
    then reach what no list can hold. Every test is off unless the user turned
    it on, and an explicit [banned] entry never reaches here at all: the literal
    rules claim their spans before any pattern runs, so dry-run, on-chain and
    re-arm keep scoring whatever this function would say about them.
    """
    tok = text[ws:we]
    callow = alts["compound_allow"]
    if callow is not None and callow.fullmatch(tok):
        return True
    toa = alts["term_of_art"]
    if toa is not None and opt("term_of_art") == "allow" and toa.fullmatch(tok):
        return True
    if opt("module_tag") == "allow" and is_module_tag(text, ws, we, kind):
        return True
    if opt("prefix_propernoun") == "allow" and is_prefix_propernoun(tok):
        return True
    return False


def count_patterns(text, patterns, mask=None, kind=None):
    """Count [pattern] regex hits, skipping spans a literal rule already counted."""
    if mask is None:
        mask = bytearray(len(text))
    whole = opt("partial_token") == "allow"
    alts = get_alts()
    # Widening costs a scan, so it runs only when some exemption can use it.
    # With no words.txt and no option set, nothing can, and the loop is upstream.
    exempting = (alts["compound_allow"] is not None
                 or (alts["term_of_art"] is not None and opt("term_of_art") == "allow")
                 or (kind == "string" and opt("module_tag") == "allow")
                 or opt("prefix_propernoun") == "allow")
    n, hits = 0, []
    for src, comp in patterns:
        for m in comp.finditer(text):
            s, e = m.span()
            if e == s or any(mask[s:e]):
                continue
            if whole:
                s, e = widen_token(text, s, e)
                if any(mask[s:e]):
                    continue
            if exempting:
                # The WHOLE token is tested, never a fragment of it, so allowing
                # EIP-* never quiets a prose compound that merely starts the same
                # way. The span is claimed so no later pattern charges for it.
                ws, we = widen_token(text, s, e)
                if compound_exempt(text, ws, we, alts, kind):
                    mask[ws:we] = b"\x01" * (we - ws)
                    continue
            mask[s:e] = b"\x01" * (e - s)
            n += 1
            hits.append(src)
    return n, hits


_ALT_CACHE = {}


def build_alternation(phrases):
    """Compile a whole word list into ONE regex.

    Longest first, so at any position the longer phrase wins: `reach out` beats
    `reach`, `dry-run` beats a later hyphen pattern. One pass over the text then
    finds every hit, so matching cost stops scaling with the size of the list.
    """
    ordered = sorted(set(p for p in phrases if p), key=len, reverse=True)
    if not ordered:
        return None
    body = "|".join(re.escape(p) for p in ordered)
    return re.compile(r"(?<![a-z])(" + body + r")(?![a-z])", re.I)


def build_compound_allow(names):
    """Compile one whole name list into ONE anchored regex.

    Serves [compound-allow] and [term-of-art]. Both hold names, one per line.

    Anchored, so the test is the WHOLE token and never a fragment: `end-to-end`
    does not quiet `end-of-day`. A trailing * is a prefix family, so `EIP-*` covers
    every EIP number without listing one. One fullmatch per pattern hit, so the cost
    does not scale with the length of the list.
    """
    parts = []
    for name in sorted(set(n for n in names if n)):
        if name.endswith("*"):
            stem = name[:-1]
            if not stem:
                sys.stderr.write("ste-lint: [compound-allow] entry '*' matches every "
                                 "compound, skipped\n")
                continue
            parts.append(re.escape(stem) + r"[\w.*+-]*")
        else:
            parts.append(re.escape(name))
    if not parts:
        return None
    return re.compile(r"(?:" + "|".join(parts) + r")", re.I)


def _alt_key():
    try:
        st = os.stat(WORDS_PATH)
        return (WORDS_PATH, st.st_mtime, st.st_size)
    except OSError:
        return (WORDS_PATH, 0, 0)


def get_alts():
    """Compiled alternations, rebuilt only when words.txt changes."""
    key = _alt_key()
    hit = _ALT_CACHE.get(key)
    if hit is None:
        _ALT_CACHE.clear()
        hit = _ALT_CACHE[key] = {
            "custom": build_alternation(custom_phrases()),
            "address": build_alternation(address_phrases()),
            "builtin": build_alternation(
                [w for bl in (BANNED, MARKETING, PHRASAL, MODAL_HEDGE)
                 for w in effective(bl)]),
            "compound_allow": build_compound_allow(CALLOW),
            "term_of_art": build_compound_allow(TOA),
        }
    return hit


def count_alt(text, compiled, mask=None):
    """Count hits from one compiled alternation, skipping already-claimed spans."""
    if compiled is None:
        return 0, []
    if mask is None:
        mask = bytearray(len(text))
    n, hits = 0, []
    for m in compiled.finditer(text):
        s, e = m.span()
        if any(mask[s:e]):
            continue
        mask[s:e] = b"\x01" * (e - s)
        n += 1
        hits.append(m.group(1).lower())
    return n, hits


def mark_alt(text, compiled, mask):
    """Claim built-in spans without counting them. See mark_spans for why."""
    if compiled is None:
        return
    for m in compiled.finditer(text):
        s, e = m.span()
        mask[s:e] = b"\x01" * (e - s)


def mark_spans(text, phrases, mask):
    """Claim built-in spans WITHOUT counting them.

    The built-in lists keep scoring through count_ci exactly as upstream, so their
    numbers never move. Marking their spans first only stops a CUSTOM rule from
    charging for the same characters: `reach out` scores once as phrasal_verb, and
    the custom `reach` does not add a second hit on top of it.
    """
    low = text.lower()
    for ph in sorted(set(phrases), key=len, reverse=True):
        for m in re.finditer(r"(?<![a-z])" + re.escape(ph) + r"(?![a-z])", low):
            s, e = m.span()
            mask[s:e] = b"\x01" * (e - s)


def count_masked(text, phrases, mask=None):
    """count_ci with the same word-boundary regex, but a span is counted once.

    Custom lists overlap in a way the built-ins do not: `you` sits inside `you're`.
    Matching the longest phrase first and masking its span stops one occurrence from
    scoring twice. Built-in lists still use count_ci, so their numbers do not move.
    """
    low = text.lower()
    taken = bytearray(len(low)) if mask is None else mask
    n, hits = 0, []
    for ph in sorted(set(phrases), key=len, reverse=True):
        for m in re.finditer(r"(?<![a-z])" + re.escape(ph) + r"(?![a-z])", low):
            s, e = m.span()
            if any(taken[s:e]):
                continue
            taken[s:e] = b"\x01" * (e - s)
            n += 1
            hits.append(ph)
    return n, hits


def lint(text, no_em_dash=False, kind=None):
    # kind names WHAT this chunk is, and only the code linter can say. It passes
    # "string" for a string literal, "comment" or "docstring" otherwise. The
    # default None means prose, so a Markdown file never reads as a log line.
    # no_em_dash=False (default) keeps the published scoring exactly: the em dash is
    # reported as a marker only, never as a violation. ASD-STE100 bans the semicolon,
    # not the em dash. Pass no_em_dash=True to opt in to counting it.
    raw = text                       # untouched, so the layout stays readable below
    md = opt("markdown_structure") == "allow"
    # Furniture out first. Everything downstream then scores prose only.
    scored_raw = md_clean(raw) if md else raw
    text = strip_code(scored_raw)
    sents = sentences(text)
    words = sum(wc(s) for s in sents) or 1
    v = {}
    longs = [(wc(s), s) for s in sents if wc(s) > 20]
    v["long_sentence(>20w)"] = len(longs)
    v["semicolon"] = text.count(";")
    v["contraction"] = count_contractions(text, opt("possessive"),
                                          opt("identifier_apostrophe"))
    v["passive_voice"] = len(re.findall(rf"\b{BE}\s+(?:\w+ed|{PP_IRREG})\b", text, re.I))
    v["ing_main_verb"] = len(re.findall(rf"\b{BE}\s+\w+ing\b", text, re.I))
    v["nominalization"] = len(re.findall(r"\b(?:perform(?:s|ed)?|conduct(?:s|ed)?|provide(?:s|d)?|carry out|carries out|make use of|makes use of)\b", text, re.I)) + len(re.findall(r"\b\w{4,}(?:tion|ment|ance|ence)\s+of\b", text, re.I))
    v["phrasal_verb"], _ = count_ci(text, effective(PHRASAL))
    v["banned_word"], bh = count_ci(text, effective(BANNED))
    v["marketing_adjective"], mh = count_ci(text, effective(MARKETING))
    v["modal_hedge"], _ = count_ci(text, effective(MODAL_HEDGE))
    # Custom rules from words.txt. Straight apostrophes only, so normalize first.
    # One shared span mask. Literal rules run first, so a span they claim is never
    # counted a second time by a pattern (dry-run scores 1, not 2).
    norm = text.replace("’", "'")
    shared = bytearray(len(norm))
    _alts = get_alts()
    mark_alt(norm, _alts["builtin"], shared)
    v["custom_word"], ch = count_alt(norm, _alts["custom"], shared)
    v["second_person"], ah = count_alt(norm, _alts["address"], shared)
    v["pattern_hit"], ph_hits = count_patterns(mask_noise(norm), PATTERNS, shared, kind)
    # Paragraphs split on the ORIGINAL text: the layout is what says where a block
    # begins and what kind of block it is. A list and a table are layout, so eight
    # bullets are not one runaway paragraph.
    paras = [p for p in re.split(r"\n\s*\n", raw) if p.strip()]
    if md:
        paras = [md_clean(p) for p in paras if not is_structural_block(p)]
    v["long_paragraph(>6s)"] = sum(1 for p in paras if len(sentences(strip_code(p))) > 6)
    em = scored_raw.count("—") + scored_raw.count("–")
    if no_em_dash:
        # Opt-in only. Skip dashes a [pattern] rule already counted, or the two
        # rules would score the same character twice.
        v["em_dash"] = sum(1 for i, c in enumerate(norm)
                           if c in "—–" and not shared[i])
    total = sum(v.values())
    per100 = {k: round(x*100.0/words, 2) for k, x in v.items()}
    return {
        "words": words, "sentences": len(sents),
        "violations": v, "total": total,
        "total_per100w": round(total*100.0/words, 2),
        "em_dash(slop-marker)": em,
        "longest_sentence_words": (max(longs)[0] if longs else max((wc(s) for s in sents), default=0)),
        "sample_marketing": list(dict.fromkeys(mh))[:6],
        "sample_banned": list(dict.fromkeys(bh))[:6],
        "sample_custom": [show_fix(p) for p in list(dict.fromkeys(ch))[:6]],
        "sample_second_person": [show_fix(p) for p in list(dict.fromkeys(ah))[:6]],
        "sample_pattern": [{"pattern": p, "note": FIXES.get(p, ""),
                            "hits": ph_hits.count(p)}
                           for p in list(dict.fromkeys(ph_hits))[:6]],
    }

USAGE = """usage: ste-lint.py [--no-em-dash] [--json] [FILE ...]
       ste-lint.py --ban "<phrase>" [--as banned|marketing|phrasal|hedge|address|pattern] [--fix "<text>"]
       ste-lint.py --allow "<phrase>"
       ste-lint.py --words

Score prose against the machine-checkable subset of ASD-STE100.
Reads stdin when no FILE is given. Score is violations per 100 words, lower is cleaner.

  --no-em-dash   count em dashes and en dashes as violations (opt in; STE bans
                 the semicolon, not the em dash)
  --json         print the full JSON result for each FILE instead of one summary line
  --ban          add a phrase to words.txt, creating the file when absent
  --as           which section --ban writes to, default banned (pattern = regex)
  --fix          optional replacement text to record with the phrase
  --allow        add a phrase to [allow], which turns off a built-in rule
  --words        print the effective lists, built-in plus custom minus allowed
"""


def _flag_value(args, name):
    if name in args:
        i = args.index(name)
        if i + 1 < len(args) and not args[i + 1].startswith("--"):
            return args[i + 1]
    return None


def add_entry(phrase, section="banned", fix=None, path=None):
    """Append a phrase to words.txt. Returns (ok, message)."""
    path = path or WORDS_PATH
    section = (section or "banned").lower()
    if section not in SECTIONS:
        return False, "unknown section [%s], pick one of: %s" % (
            section, ", ".join(SECTIONS))
    phrase = " ".join(phrase.split())
    if not phrase:
        return False, "empty phrase"
    custom, _, allow, pats, _opts, names = load_words(path)
    if section in NAME_CATS:
        if len(phrase.split()) > 1:
            return False, "[%s] takes one token, got %r" % (section, phrase)
        existing = set(names[section])
    elif section == PATTERN_CAT:
        existing = set(src for src, _c in pats)
        ok, _c = compile_pattern(phrase)
        if not ok:
            return False, "%r is not a valid regex, nothing added" % phrase
    elif section == "allow":
        existing = set(allow)
    else:
        existing = set(custom.get(section, []))
    if phrase in existing or phrase.lower() in existing:
        return False, "%r is already in [%s], nothing added" % (phrase, section)
    if not os.path.isfile(path):
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(SECTION_TEMPLATE)
        except OSError as e:
            return False, "cannot create %s: %s" % (path, e)
    line = (phrase if (section == "allow" or section in NAME_CATS or not fix)
            else "%s -> %s" % (phrase, fix))
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().split("\n")
    except OSError as e:
        return False, "cannot read %s: %s" % (path, e)
    header = "[%s]" % section
    if header not in [l.strip() for l in lines]:
        while lines and not lines[-1].strip():
            lines.pop()
        lines += ["", header, line, ""]
    else:
        idx = [l.strip() for l in lines].index(header)
        end = idx + 1
        while end < len(lines) and not SECTION_RE.match(lines[end].strip()):
            end += 1
        while end > idx + 1 and not lines[end - 1].strip():
            end -= 1
        lines.insert(end, line)
    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    except OSError as e:
        return False, "cannot write %s: %s" % (path, e)
    return True, "added to [%s]: %s" % (section, line)


def print_words():
    print("words.txt: %s%s" % (WORDS_PATH,
                               "" if os.path.isfile(WORDS_PATH) else "  (absent)"))
    rows = [("banned", BANNED), ("marketing", MARKETING),
            ("phrasal", PHRASAL), ("hedge", MODAL_HEDGE)]
    for name, builtin in rows:
        eff = effective(builtin)
        cust = [p for p in CUSTOM.get(name, []) if p not in ALLOW]
        off = len(builtin) - len(eff)
        print("\n[%s] built-in %d, custom %d, allowed off %d -> effective %d"
              % (name, len(builtin), len(cust), off, len(eff) + len(cust)))
        for p in cust:
            print("    custom: %s" % show_fix(p))
    addr = address_phrases()
    print("\n[address] custom %d -> scored as second_person" % len(addr))
    for p in addr:
        print("    custom: %s" % show_fix(p))
    print("\n[pattern] %d live -> scored as pattern_hit" % len(PATTERNS))
    for src, _c in PATTERNS:
        note = FIXES.get(src, "")
        print("    regex: %s%s" % (src, ("   -> " + note) if note else ""))
    print("\n[compound-allow] %d names a pattern may not flag" % len(CALLOW))
    fam = [c for c in CALLOW if c.endswith("*")]
    if fam:
        print("    families: %s" % ", ".join(sorted(fam)))
    print("\n[term-of-art] %d jargon hyphenations, read only when term_of_art = allow"
          % len(TOA))
    if TOA and opt("term_of_art") != "allow":
        print("    LOADED BUT OFF. Set  term_of_art = allow  in [options] to use them.")
    if ALLOW:
        print("\n[allow] %d off: %s" % (len(ALLOW), ", ".join(sorted(ALLOW))))
    print("\n[options]")
    for k in sorted(DEFAULT_OPTIONS):
        val = OPTIONS.get(k, DEFAULT_OPTIONS[k])
        print("    %s = %s%s" % (k, val,
                                 "   (default)" if val == DEFAULT_OPTIONS[k] else ""))
    total = (sum(len([p for p in CUSTOM.get(c, []) if p not in ALLOW]) for c in CUSTOM_CATS)
             + len(addr) + len(PATTERNS))
    print("\nTOTAL custom rules live: %d" % total)

if __name__ == "__main__":
    args = sys.argv[1:]
    no_em = "--no-em-dash" in args
    as_json = "--json" in args
    if "-h" in args or "--help" in args:
        print(USAGE); sys.exit(0)
    if "--words" in args:
        print_words(); sys.exit(0)
    if "--ban" in args or "--allow" in args:
        if "--allow" in args:
            phrase, section = _flag_value(args, "--allow"), "allow"
        else:
            phrase, section = _flag_value(args, "--ban"), _flag_value(args, "--as")
        if not phrase:
            sys.stderr.write("error: --ban/--allow needs a phrase\n"); sys.exit(2)
        ok, msg = add_entry(phrase, section, _flag_value(args, "--fix"))
        print(msg if ok else "refused: " + msg)
        sys.exit(0 if ok else 1)
    consumed = set()
    for f in ("--as", "--fix", "--ban", "--allow"):
        val = _flag_value(args, f)
        if val: consumed.add(val)
    files = [a for a in args if not a.startswith("--") and a not in consumed]
    if not files:
        print(json.dumps(lint(sys.stdin.read(), no_em_dash=no_em), indent=2)); sys.exit(0)
    exp = []
    for f in files: exp += sorted(glob.glob(f)) if any(c in f for c in "*?[") else [f]
    out = {}
    for f in exp:
        with open(f) as fh: r = lint(fh.read(), no_em_dash=no_em)
        if as_json:
            out[f] = r
        else:
            print(f"{os.path.basename(f):32} words={r['words']:4d} total={r['total']:3d} per100w={r['total_per100w']:6.2f} em_dash={r['em_dash(slop-marker)']:2d}")
    if as_json:
        print(json.dumps(out, indent=2))
