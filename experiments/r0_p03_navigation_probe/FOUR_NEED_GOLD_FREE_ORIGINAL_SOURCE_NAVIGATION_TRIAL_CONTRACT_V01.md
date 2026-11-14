# R0-P03: four fixed fresh-needs, original-source gold-free navigation/answer pilot V0.1

**Date:** 2026-11-14
**Status:** PROSPECTIVE_UNSCORED_TRIAL_PROTOCOL_BEFORE_FIRST_RETRIEVAL / NOT_FORMAL_R0_P03
**Input questions:** original MC-0030 Message 073, SHA-256 `95dec6abdc5ad7ceec435f9cb3b3eb114a4dad8ac75f4865df05ea9509eff5d6`, four categories N01-N04, no replacement.
**Original source world:** Git `47ed6344a9153dcf366769e95722840fbf1a8f8b`; no current branch-head text.
**External reference:** local-only original-source reviewer report, citation audits and twelve-item classification from Message 077. **This execution MUST NOT read them.**
**Actual goal:** Observe actual original Git source contexts discoverable for four independently originated complex needs and whether source-limited models can produce appropriately qualified answers/abstentions, before any final architecture decision.

## 1. Fair source candidate world and two named diagnostics

Enumerate exactly the original Git *blob* paths at the pin matching:
- `docs/CURRENT_STATE.md`, `docs/DECISIONS.md`;
- `docs/research/**/*.md`, `docs/checkpoints/**/*.md`, `docs/specifications/**/*.md`, `docs/foundations/**/*.md`, `docs/local_execution/validation/**/*.md`;
- `tools/**/*.py`, `tests/**/*.py`, `scripts/**/*.py`.

No question-specific source closure, expected-source whitelist, labels, old answer-bearing question packet, reference relevance mapping, private report, source-annotation updates, top-K oracle hints or conditional addition of missing gold. All original eligible files, including difficult long files, enter a **single common corpus**. Pin every Git blob SHA-1 and verify its original bytes. Exclude noneligible files by this path/type-only rule. Do not infer operative authority from path type, doc title or tests.

Use the same original source text truncated at **12,000 characters per document** for both retrieval methods. This cap may hide late-document evidence and is a declared limitation, never tuned after observing results. Build a fresh in-memory SQLite FTS5 Unicode61 index with:
- `BODY_FTS5_BM25`: default BM25 rank on the normalized original document text;
- `BODY_PLUS_HEADINGS_RRF_DIAGNOSTIC`: stable reciprocal-rank fusion (damping **60**) of BODY_FTS5_BM25 and a second FTS5 query against Markdown headings extracted exclusively from the same original text, top 10 of each.

No source-owner subject tagging, editorial links, accepted semantic ontology, directed owner labels or embeddings are introduced by this heading diagnostic. **Do not call it the official B1/B2/B3/B4 arm.** It is a transparent, cheap original-source navigation ablation. Same original text/corpus/input queries, top four final source carriers and excerpt budget per case. Deterministic ties by original path. Queries are exact frozen need text with the common 40-character historical Git pin removed only as a temporal locator string (never rewritten to easier question text); use existing fixed lexical token/stopword algorithm. No query-gold exposure.

## 2. Gold-free, citation-preserving answer packets

From each method's **top four** original Git source carriers per fixed need, select source-only, deterministic query-term-overlap excerpts (up to **two** disjoint original line windows per source, with **2,400 maximum excerpt characters per source**, clipping indicated). Include original relative path, original Git blob SHA-1, exact original line numbers, selected source line text and whether a line was clipped. These are retrieval outputs, **not qualified expected witnesses**. Keep the entire original question; do not tell answerers the private reference or provide the reviewer classification, citation audit, expected source path or other method's packet.

Produce two **separate** exact original answer-input JSON files:
- `four_need_gold_free_source_packet_A_v01.json`: body lexical source evidence.
- `four_need_gold_free_source_packet_B_v01.json`: body+heading navigation diagnostic evidence.

Their treatment identities are frozen here but **not** shown inside the model-facing files. The packets are author-visible source texts, **not secret historical gold**, and this is not an official blind arm protocol. No original reviewer answer or source relevance mapping is copied into either packet. Save each file exclusively once, and preserve SHA-256/bytes. Publish source-free aggregate metadata/cost counts without copying original source excerpts into summary logs.

## 3. Source-limited answer generation and scientific limitations

The next phase must use fresh model sessions, one **per packet**, with no cross-packet exposure. Each model may read only its assigned source packet and the narrow answer-authoring instruction. It must produce one response per frozen question with original path@blob/line citations *actually present in that packet*, distinguish historical recorded status from operative authority, and explicitly abstain on unsupported subquestions. No web, original whole Git, old exposed B0/B1 P01-P12 answers, private reference report, earlier Claude reviewer evaluations, alternate retrieval outputs or hidden gold.

Source-limited answers may be recorded as source-only outputs and audited for exact excerpt citations, but **cannot** be compared to private gold in the exposed coordinator context. Do not pre-score or tune sources against the four source-specific reference answers, which remain Git-ignored and same-user-local-only. If independence or custody requirements for a fair official trial are not established, keep a clearly labelled **unscored exploratory result**, no architecture rank or Research 513 score.

No source-specific evidence should be silently upgraded to physical implementation, authority, owner acceptance or actual CI. A top-four source ranking measures neither complete original answer truth nor qualified corpus recall. The four original questions are especially broad, and their prior private review found **N01 full / N02-N04 partial** within its different source search budget: this aggregate is background qualification, not a retrieval expected-source oracle.

    ORIGINAL_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    FROZEN_NEEDS=4
    SOURCE_WORLD=OBJECTIVE_FULL_HISTORICAL_SELECTED_PATH_FAMILIES
    INDEXED_CHARS_PER_FILE=12000
    TOP_K_SOURCES=4
    MAX_EXCERPTS_PER_SOURCE=2
    MAX_EXCERPT_CHARS_PER_SOURCE=2400
    TREATMENTS=BODY_FTS5_BM25;BODY_PLUS_HEADINGS_RRF_DIAGNOSTIC
    METADATA_OWNER_SUBJECT_TAGS=false
    EXPECTED_SOURCE_GOLD_IN_RETRIEVAL=false
    PRIVATE_REFERENCE_READ=false
    FORMAL_R0_P03_SCORING=false
