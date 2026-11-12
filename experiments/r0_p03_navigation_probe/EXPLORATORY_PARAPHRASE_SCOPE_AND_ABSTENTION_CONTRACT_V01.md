# Paraphrase, unsupported relation claims, and explicit evidence-scope abstention V01

**Date:** 2026-11-12
**Status:** FIXED BEFORE NEW EXPERIMENTAL SCORING
**Parent:** Checkpoint 909's real 130-question forward/reverse literal-path index.
**Purpose:** Actually test whether a constrained query-intent adapter handles several differently worded relationship requests, and whether it avoids converting literal path mentions into ungrounded dependencies, governing relationships or hyperlinks. This is an exploratory implementation exercise, not the original Research 513 R0-P03 scored experiment.

## Source world and immutable historical controls

Only the same 65 original Git document bodies at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`, are admissible. The old 110 directed exact `docs/...` source-path mentions form the bounded **literal mention** relation oracle. Verify exact prior Checkpoint 909 source result full SHA-256 `99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399`; never mutate it.

All 65 first-H1 titles must be unique and contain no double quotes. No selective document/task omission, manual answer rewriting, post-result token tuning, new sources, private C01/C02 materials, or changes to the previous 74 + 130 queries.

## Fixed new full-population tasks

For each of the 65 titles and **both directions**, generate exactly four **new** differently worded positive requests (520 questions):

| Family | Forward | Reverse |
| --- | --- | --- |
| S1 (parser design) | `In "<TITLE>", which other documents are referenced by repository path?` | `Which documents reference "<TITLE>" by repository path?` |
| S2 (parser design) | `List the docs/ paths mentioned inside "<TITLE>".` | `Find files that mention "<TITLE>" via a docs/ path.` |
| H1 (held-out morphology) | `Which file paths are explicitly cited within "<TITLE>"?` | `Where is "<TITLE>" explicitly cited by file path?` |
| H2 (held-out morphology) | `Give outbound docs/ path citations for "<TITLE>".` | `Give inbound docs/ path citations for "<TITLE>".` |

The existing Checkpoint 909 original exact template is a **separate 130-query backward-compatibility test only**, not counted as new paraphrase results. The S1/S2 strings inform the first new parser specification, while H1/H2 are fixed holdout wording families. **No parameter or rule changes after observing H1/H2.** The grammar may reject semantically valid held-out queries and that failure must be reported, not papered over with gold-dependent fallback.

Reference targets for each *in-scope* path-mention query are the original exact outgoing/incoming edges of that historical source. The 110 directed edges produce 220 relation opportunities per family, so all four families contain **880** required occurrences. The K=10 maximum is **832** over all four families because the old original index ceiling was 208/220 per family. Retain over-limit/empty cases for every family.

For every one of 65 titles, add three **distinct unsupported-scope** requests (195 questions):
- U1: `Which documents actually depend on "<TITLE>" in practice?`
- U2: `Which documents does "<TITLE>" govern authoritatively?`
- U3: `Which documents contain working hyperlinks to "<TITLE>"?`

They are **NOT** equivalent to literal repository-path mentions. The expected safe behavior is `unsupported_scope` with zero asserted relationship-source results, **not** a claim that there are zero real dependencies, zero governing relations, or zero working hyperlinks. Even when a path mention exists, its presence does not close these claims.

Add four malformed/unresolved controls: unknown title for both directions using the S1 format, plus two different known titles in one quoted multi-title forward/reverse request. These must return `unknown_title` or `ambiguous_title`, never `no_matching_literal_mentions`. The full new population is **719** requests: 520 in-scope paraphrases, 195 unsupported semantic scopes and 4 unknown/ambiguous title controls.

## Fixed mechanisms and semantics

1. **Generic lexical B0 control:** same source-body FTS5 unicode61 BM25 and existing literal OR query tokenization, top ten; ranking does not inspect answer targets. Results are generic candidate documents, not asserted relation answers. Count how often it fills results on semantically unsupported requests. Never equate lexical retrieval with a false generated answer.
2. **Old rigid exact-template relation parser:** call immutable Checkpoint 909 `parse_relation_question` on each new query. It either resolves the old grammar or rejects; report coverage. No retroactive addition of paraphrase patterns to the old parser.
3. **New source-scoped guarded parser:** extract exactly **one** double-quoted title from the request and resolve it using the 65 first-H1 title index, never the expected neighbor list. Reject two or more quoted titles as `ambiguous_title`; unknown title as `unknown_title`. Before classifying the direction, reject tokens `depend`, `govern`, `authorit`, `hyperlink`, `working link`, `actually related` as `unsupported_scope`. Accept literal-mention scope only if the non-title request has a path anchor (`repository path`, `file path`, `file paths`, or `docs/`) **and** contains a mention/reference/citation cue (`referenc`, `mention`, or `cit`). Direction is FORWARD if the part preceding the quote ends in `in`, `inside` or `within`, REVERSE if it uses the bounded pre-title linguistic forms `which documents reference`, `find files that mention`, or `where is`. Otherwise classify `unparsed_in_scope`, not a fabricated structural answer. This intentionally does not add special patterns for held-out `outbound`/`inbound` wording.
4. **Typed reference operator:** for accepted forward/reverse requests, return outgoing/incoming exact path-mention neighbors ranked by shared lexical BM25 then path, with K=10; if no literal mentions exist report `no_matching_literal_mentions`. For unsupported, unknown, ambiguous or unparsed requests, return no asserted relation targets with an explicit state distinct from graph absence. It does not silently fall back to lexical document candidates as relation *answers*.

Report per-family parsing acceptance, structural hits/required, ceiling-normalized hit count, structurally empty abstentions, parsed-direction errors, unsupported-scope safe abstentions, original template coverage, generic B0 candidate count for unsupported/unknown, and per-task source paths for the positive graph-index cases. **Separate lexical candidate retrieval from asserted structural answers** in saved JSON. Do not pool unsupported requests into structural recall or treat a rejected equivalent query as correct source absence. The held-out H1/H2 result is a diagnostic measure of finite-rule robustness, not independent LLM understanding.

No claim of actual historical dependency, governed link semantics, source truth, B3 concern selectors, embeddings B4, answer synthesis, independent blind gold, validated new query distribution or physical architecture selection. A literal mention in prose/code cannot be elevated to an authoritative relationship.

## Reproducibility

Exclusive-create deterministic result JSON, audit the old fixed source and result hashes, assert exact task counts and corpus reference totals, and run a full deterministic rerun. Old original 130 query handling must stay unchanged; old 74 non-relation router behavior remains the responsibility of the untouched published Checkpoint 909 and its tests. No after-result score-driven rule changes.

    CURRENT_FROZEN_SOURCE_DOCUMENTS=65
    PATH_REFERENCE_EDGES=110
    PARAPHRASE_FAMILIES=4
    PARAPHRASE_POSITIVE_REQUESTS=520
    UNSUPPORTED_SEMANTIC_SCOPE_REQUESTS=195
    UNKNOWN_OR_AMBIGUOUS_REQUESTS=4
    TOTAL_NEW_REQUESTS=719
    STRUCTURAL_REFERENCE_INSTANCES=880
    STRUCTURAL_HITS_K10_CEILING=832
    FORMAL_R0_P03_SCORING=NONE
