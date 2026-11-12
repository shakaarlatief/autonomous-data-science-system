# Real historical source-path reference provenance and context audit V01

**Date:** 2026-11-12
**Status:** METHOD_FIXED_BEFORE_FIRST_V01_OUTPUT / EXPLORATORY_SOURCE-LEVEL_EVIDENCE_AUDIT
**Prior state:** Exact immutable Checkpoints 905–910. Latest checkpoint 910, HEAD `76f44304b23c9e94f94aaa4820b40d72ff1f7938`.
**Question:** What evidence has been lost by converting exact historical path occurrences into an unqualified 110-edge graph, and how many edges would syntactic source-context policies expose or withhold?

## Immutable inputs

Exactly 65 old W5 T1 V02 historical source documents read from Git object revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`. Verify the known 65-original source fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`, the exact authored annotation population (65 unique paths) and existing Checkpoint 910 output checksum `b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e`. The old path parser is a fixed reference comparator, not a privileged semantic ground truth.

The preflight already exposed 110 unique directed `docs/*.md|json` source-to-source path edges, with 146 path mention occurrences across original lines, including repeated occurrences. A source-level classification will preserve **all**, without dropping examples, zero-degree nodes or source-local repeated witnesses to make a preferred architecture look better.

## Fixed extraction and evidence model

For every original source body, scan numbered lines and detect the same exact `docs/<path>.md|json` tokens as the old `references()` extractor, admitting only paths in the exact 65-source universe, excluding self-links and missing files. Verify equality of the complete 110 directed pair set with the legacy parser. Do not follow web URLs, add non-corpus targets or infer any relation from file naming.

Classify each actual source-token **occurrence**, in this priority order:
1. **FENCED_CODE** when within a Markdown triple-or-more backtick or tilde code fence; use opening marker character and minimum closing width and do not classify the delimiter line itself.
2. **INLINE_CODE** when the token is between a matched equal-width backtick delimiter pair on the same line, outside fences.
3. **OTHER_TEXT** otherwise, including path-selector strings that resemble machine routing data.

A single directed pair may occur in more than one context. Preserve each occurrence with historical source path, target path, original one-based line, character start/end, entire original source line (trailing CR excluded), SHA-256 of original line bytes (UTF-8), original source Git blob SHA-1, original source SHA-256, context class and the complete ordered set of lexical indicator flags. Evidence flags are **syntactic diagnostics, not truth labels**:
- `PATH_SELECTOR` if source line contains literal `path:docs/` before an eligible path mention;
- `GOVERNANCE_WORDING` when a bounded word or phrase such as `governed by`, `governing`, `authoritative`, `canonical`, `must`, `required`, `source of truth`, `supersed` appears on the line;
- `NAVIGATION_WORDING` when `see`, `read`, `reference`, `mentioned`, `refer to`, `source`, `context` or `citation` appears as word/bounded phrase on the line;
- `MARKDOWN_INLINE_LINK` only if the original exact source text constructs a syntactically explicit Markdown inline link with the current path mention as the destination. This flag does not mean the hyperlink works or conveys authority.

Include every occurrence regardless of whether it has any indicator flags. Preserve source text exactly in the JSON audit so each finding can be traced and manually verified; no claims of independence or restricted material are made about these public historical 65 source files.

## Fixed comparison policies and measures

Build one complete **RAW_PATH_MENTIONS** graph from the old parser and three nested *syntax-only projection sets* from audited occurrences:
- `OUTSIDE_FENCE`: at least one witness to the directed pair outside a fenced code block, including inline-code references;
- `OTHER_TEXT_ONLY`: at least one witness in the OTHER_TEXT class (excluding fenced and inline code). This is explicitly *not* a truth or quality filter; inline code can carry meaningful source-owner instructions;
- `MARKDOWN_LINKS_ONLY`: at least one witness is an explicit inline Markdown link destination.

Report each projection's directed edges, sources with outdegree, targets with indegree, how many source pairs it loses relative to the raw graph, how many raw pairs have mixed contexts, and the differences between the three nested policies. Separately report occurrence totals by context and by lexical indicator flag. Keep a source-level ordered witness inventory for each pair.

**Do not** label raw literal paths as governed B2, J2, real dependencies, operative authority, valid hyperlinks or declared facts. A zero Markdown-link result is NOT evidence of zero meaningful source relationships, because plaintext and inline-code source declarations may be intentional. A fenced path may likewise be documentary evidence; formatting alone cannot decide authority. Do not compute pseudo-precision or recall against a "gold" derived from these classes. This is a reproducible **evidence-distribution and information-loss** audit, not an answer benchmark.

## Reproducibility and negative controls

Persist one deterministically ordered, exclusive-create JSON trace including full original source provenance and all source-to-target occurrence lines. Recompute identical full JSON in a read-only second run. Add unit tests with synthetic:
- fenced code versus inline-code versus unformatted path mentions;
- mixed-context same pair and repeated mentions on one line;
- 4-backtick fences and unmatched inline backticks;
- Markdown-link destination versus ordinary inline source link;
- absence of unknown/self-target pairs;
- no false source authority inference from syntactic flags;
- exact old 110 graph-edge parity, source/revision fingerprints and Checkpoint 910 hash.

A bounded independent exposed Claude review may later interpret these source witnesses, but Claude's review must not become an *independent blind gold* claim when it has earlier R0 architecture/fixture exposure. No change to Checkpoints 905–910 outputs, C01/C02 protected evidence, original Research 513/559/576 method or official architecture selection.

    SOURCE_COUNT=65
    HISTORICAL_PIN=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    PRIOR_EXPERIMENT_910_SHA256=b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e
    ORIGINAL_UNQUALIFIED_EDGE_COUNT=110
    CONTEXT_LABELS=FENCED_CODE_INLINE_CODE_OTHER_TEXT
    MEASURES=SOURCE_OCCURRENCE_AUDIT_NOT_ARCHITECTURE_SCORE
    OUTPUT=EXCLUSIVE_CREATE
    GOVERNING_SEMANTIC_ADMISSION=NONE
    FORMAL_P03_SCORING=NONE
