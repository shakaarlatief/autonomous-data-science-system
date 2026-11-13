# T2 V01: Actual new-source owner-status retrieval and false-acceptance safeguards

**Date:** 2026-11-13
**Status:** EXECUTION_FIRST_EXPLORATORY_METHOD_FIXED_BEFORE_OUTPUT / NO_FORMAL_R0_P03_SCORE
**Scientific lineage:** Research 649 / Checkpoint 912, Claude Message 064 T2 proposal. This is a bounded *pilot subset*, not the complete independently scored T2 or frozen R0-P03 Research 513 protocol.
**New source horizon:** Exact public repository Git snapshot `e8ae867392f818f43dc8b76984f164e277d5cc87`; take `git archive --format=tar <pin> docs/research docs/checkpoints docs/specifications`. Historical 65 original W5 comparison source paths are excluded from **all 120** documents used here. No private C01/C02.

## User question and ascertainable truth

Test source-local **owner-decision status evidence**, not general current governing authority. Source Status headers do not prove present-day operative governance. Neither title wording, historical acceptance nor a source quoting owner language establishes live accepted target. A header category is a limited *self-description*, not independent truth.

Three mutually exclusive source-header classes:
- `OWNER_ACCEPTANCE_RECORDED` iff the first-100-line header `Status` contains bounded `OWNER ACCEPTED` or `OWNER-ACCEPTED` and does not say `OWNER DECISION REQUIRED`.
- `OWNER_DECISION_REQUIRED_RECORDED` iff the same header contains exactly bounded `OWNER DECISION REQUIRED`; this wins against any simultaneous `CANDIDATE`.
- `CANDIDATE_RECORDED` iff header Status contains a bounded `CANDIDATE` and neither of the previous rules applies nor `ACCEPTED` appears anywhere in header. This is a broad candidate label; `CANDIDATE QUALIFIED` means only candidate qualified, not owner acceptance.

Use existing `scripts.repository_integrity.read_header_fields` on exact archived Git source bytes in isolated temp files; do not classify by filename or an alternative homegrown header parser. Reject missing Status. H1 and exact source body will be frozen per original bytes.

## Fixed population before output observation

From the three-family archive, excluding the entire historical 65-source path universe, collect all eligible Markdown paths with governed header Status. For each class sort candidates by SHA-256(`T2-V01-NOV13-STATUS-FIXED|<class>|<path>`) then lexicographic path and select the **first eight**; no cherry-picking or per-case substitution after results. Include **96** additional eligible documents from the same archive excluding the selected 24 and original 65, SHA-sorted by `T2-V01-DISTRACTOR-FIXED|<path>`. Report the underlying class counts and full 120 roster with exact body SHA-256; exclude duplicate paths. This is a single physically new source population relative to the 65 historical comparator, but the task author knows the selection rule and documents, so independence is **not** claimed.

For every selected target derive one fixed naturalish user request by taking its actual first Markdown H1, lowercasing and omitting exact `OWNER`, `ACCEPTED`, `APPROVED`, `DECISION`, `REQUIRED`, `CANDIDATE`, `PENDING` tokens. `What is the owner-decision status for [topic]? Was it actually accepted, still awaiting an owner decision, or only a candidate? Return source evidence and useful candidate documents separately.` The bracket is the sanitized title; it is still **title-derived**, not independent author wording. It must never be represented as a blinded natural-language benchmark. Freeze all 24 query strings before building any retrieval index. Query ranker sees only the sanitized topic phrase, not reference labels or ground-truth path. No hidden ID.

## Fixed source access, comparators and two-channel contract

Build one SQLite FTS5 Unicode61/BM25 index over the **same 120 exact archived full texts**. Query by OR of non-stopword alphanumeric topic tokens, return best K=10 (full FTS matches are sorted by BM25 then path). Nonmatches remain empty, never force-insert the target. Report hit@1, hit@5, hit@10, MRR@10 and raw ranked paths per item.

On the **same top-ranked candidate** compare independent interpretation policies:
1. `LEXICAL_ONLY`: ranked candidate documents, no owner-status/authority assertion. Report candidate recall; abstention is correct as an evidence safety policy, but not scored as successful status interpretation.
2. `BODY_KEYWORD_HEURISTIC`: first match over the entire document body using the same three case-insensitive phrases, ignoring line/structural scope; first priority owner decision required, then owner accepted, then candidate. A candidate result must never be promoted merely by a bare `ACCEPTED` elsewhere. This **deliberately fragile diagnostic comparator** measures false *source-header-status* claims relative to the independent `Status` field, not general false governance. It is not a formal R0 arm.
3. `GOVERNED_HEADER_ASSERTION`: only an explicit parsed header Status can be asserted, with original source path and Status line witness. If top-ranked candidate lacks a supported status class, answer `NOT_FOUND_IN_COVERED_SCOPE` rather than inventing authority.
4. `TWO_CHANNEL_GUARDED`: same evidence-bound Status assertion as (3), but always return the separate top-ten lexical candidate list labeled **non-authoritative suggestions**, even when an assertion is unsupported. Do not fuse candidate rank into an evidence assertion.

Because retrieval may return the wrong document, **a status assertion about the top-ranked document is not automatically an answer about the intended target**. Score exact-target owner-status correctness **only when retrieved document equals target**; otherwise report `WRONG_SOURCE_ASSERTION` and do not count as correct regardless of matching class. Additionally report unsupported `OWNER_ACCEPTANCE_RECORDED` for nonaccepted target, and any document's falsely stated owner acceptance relative to its own parsed Status. No code is allowed to use expected labels to choose the retrieved source.

## Result and negative controls

Persist each query, expected original source path/status text and its exact source bytes SHA; all four answer representations, top-ten rankings, top-source Status witness/provenance, output states, per-policy exact-source correctness and false positive counts. Store exact Git SHA, tool versions and complete population identities. Include total source world 120, 24 questions and exactly 8 from each class. Prespecify zero silent promotion of a candidate suggestion into a governing fact; never state `CLOSED_WORLD_ABSENT`, and do not claim proof of actual live currentness. No post-run threshold tuning, dropped rows or task replacement.

If FTS5 returns a known target absent at K=10, that is a genuine retrieval miss in this bounded source world; no hidden path fallback. Testing might find failures. Original Research 513/559/576 thresholds and arms are untouched; all conclusions are **exploratory evidence-handling and ranking demonstrations**, not scored B0-B4 physical architecture choices. A genuinely independent fresh-author T2 requires separate user/source evidence and fair semantic comparator later.

    EXACT_SOURCE_PIN=e8ae867392f818f43dc8b76984f164e277d5cc87
    SOURCE_SAMPLE=120
    TARGETS=24
    TARGETS_PER_CLASS=8
    CANDIDATES_K=10
    SOURCE_STATUS_IS_OPERATIVE_AUTHORITY=false
    EXPOSED_TITLE_DERIVED_QUERIES=true
    INDEPENDENT_GOLD=false
    COMPLETE_T2=false
    FORMAL_P03_SCORING=NONE
    OUTPUT=EXCLUSIVE_CREATE
