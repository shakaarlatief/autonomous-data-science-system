# R0-P03 Route B: frozen extractive answer, citation and evidence-completeness execution V01

**Date:** 2026-11-13
**Status:** FIXED_BEFORE_FIRST_EXTRACTIVE_ANSWER_RESULT / NON-BLIND EXPLORATORY / REFERENCE TRUTH NOT INDEPENDENT
**Motivation:** The first B0, B1/B2/B3 and classical B4-LSA source-ranking comparisons have actually run. The next bounded, executable advance is **source-to-answer evidence reconstruction**, not another task origination programme. This test measures whether equal-bounded retrieved sources can produce supported, cited *extractive* answers and how much of the previously frozen reference evidence is preserved. It does **not** pretend a deterministic quote renderer is a full LLM-level natural-language reasoner.

## Immutable prior inputs

- Original source horizon `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
- The same **12** original exposed coordinator-authored questions, fixed source-answer/reference manifest exactly `9784` bytes SHA-256 `c628555ef02f87499007ead3420a513cf43080262c7288cd347dc2479b4b0330`.
- Exactly the original **60 build** and **20 excluded heldout** source carriers, and original identical content from Git, with no later worktree state.
- Checkpoint918 B0 original source/results **122682 bytes**, SHA-256 `59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab`.
- Checkpoint919 B1/B2/B3 comparison **92547 bytes**, SHA-256 `6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2`.
- Checkpoint920 real classical LSA vector experiment **154662 bytes**, SHA-256 `59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f`.
- Checkpoint918 source H1/title and 12,000-character indexing limit unchanged, with identical target-independent source access across arms.

## Frozen arm source rankings and context budget

Evaluate the following seven **already saved**, unchanged candidate-order methods:
1. `B0_ORIGINAL` = Checkpoint918 whole-body BM25.
2. `B1_EXPOSED_SUBJECT_B0` = Checkpoint919 B1+B0.
3. `B2_SOURCE_WRITTEN_LINK_B0` = Checkpoint919 B2+B0.
4. `B3_EXPOSED_CONCERN_B0` = Checkpoint919 B3+B0.
5. `B4_CLASSICAL_LSA_DENSE_ONLY` = Checkpoint920 LSA.
6. `B4_CLASSICAL_LSA_B0_FUSION` = Checkpoint920 LSA+B0.
7. `B4_CLASSICAL_LSA_B2_FUSION` = Checkpoint920 LSA+B2.

For each arm and question, take only its **top three actual retrieved source paths**. Do not receive/retrieve the intended target path or reference-answer text during passage selection or answer rendering. Each source may expose only the **first 12,000 original Unicode characters**, matching the previous retriever's model context; no reference gold, post-archive source, cross-source inferred status, owner credential, or live worktree data. The **same generic** quote-selection algorithm is used for every arm, without per-task or per-arm tailoring.

For each source: include the first original heading `# ...` if available. Among the first **35** complete nonempty lines outside Markdown fenced code, select at most **four additional lines**, each at most **550** original characters. Do not cut or fabricate a line; discard any longer line. Candidate relevance is the number of **distinct, fixed V04 query tokens** also present in the line, plus field bonuses: `**Status:**` (+2), `**Scope:**` (+1), `**Authority:**` (+1), and `**Checkpoint:**` or `**Active development branch:**` (+1), independent of task identity. Ties go to earlier source-line position. Select the highest-scored candidates, then restore ascending original line order, keeping original content/line SHA and byte-identified source carrier. No markdown fence, JSON evidence block, original foreign document, or source beyond 12,000 characters can become a quote. The header/title counts as the fifth potential line, for a strict maximum **five cited lines per source**.

The renderer emits a deterministic short answer **draft**:
`At the archived Git revision, the highest-ranked retrieved record is "<H1>" [source path@SHA]. Its source text states: "<first selected quote>"; "<second selected quote>"...`. It must **say "source text reports" rather than "we have implemented/accepted"**, and append an explicit operative-governance disclaimer. It may include up to **three** cited sources; it does not silently resolve conflicting sources. This is an *extractive evidence draft*, not a constructed full natural-language reference answer or a human-reviewed synthesis. An empty candidate list yields an abstention.

Preserve for each arm and question full candidate rankings, all consumed top-three paths, each exact original line witness/line SHA, draft text and source citation string. Output supports exact full replay and source-verifiable auditing.

## Evaluation-only retrospective checks

**Only after all drafts are generated**, read the separately frozen 12-question reference manifest and compare:
- `required_source_in_top_3`: source identity from frozen task manifest appears in consumed candidate paths;
- `all_required_excerpts_in_accessible_context`: every frozen reference excerpt appears verbatim in one complete original line in a correctly retrieved source within the same 12,000-character budget; no author answer synthesis is assumed;
- `all_required_excerpts_in_emitted_quotes`: every required frozen excerpt is literally present within actual emitted cited original lines of that same source, after the quote algorithm. **This is stronger than source@3 but weaker than answer correctness.**
- Per-case `reconstruction_evidence_class`: `ALL_REFERENCES_QUOTED`, `REFERENCES_ACCESSIBLE_NOT_ALL_QUOTED`, `REQUIRED_SOURCE_NOT_RETRIEVED` or `REFERENCE_CONTEXT_NOT_AVAILABLE`. No unsupported semantic PASS is inferred.
- Track source retrieval top-three, evidence exposure, quote precision (each emitted quote copied exactly from original) and fixed rendering output, including output size/counts. Report all 12 cases for all 7 methods, all failures, and per-category counts, without excluding hard cases post-observation.

A *reference answer* may include semantic propositions that **do not follow exclusively from its listed witness snippets**; a complete independent evaluator must assess whether the cited source actually supports the full answer. This run can identify concrete missing/exposed evidence, not self-certify full answer truth or complete original R0-P03 `>=10/12` PASS.

## Independence/authority and collaboration limits

- Reference author, arm author, runner and evaluator remain exposed; this is **non-scored Level C engineering** authorized by the owner's pragmatic Path B direction, **not** Research575 Level B independent-scored admission.
- Claude CLI was found installed at `claude 2.1.283`; one no-tool, no-session-persistence headless readiness attempt with the authorized local Runtime Bridge **timed out** under the bridge's bounded 30-second command limit. Do not claim a Claude independent answer review took place.
- The model-free renderer receives only source evidence, never target reference paths/answers until the retrospective evaluation pass. No source Status or agent prose can be promoted to **current operative authority**, accepted migration or production deployment.
- Original C01/C02 independently originated but unresolved protected cases remain private, unmodified and unscored. No original legacy nine-case neutral gold, heldout maintenance F1, source-owner B1/B3 authority, complete V03 substrate or full formal B0-B4 task reconstruction is established.
- No method, task, label, question, retrieved arm ranking, query or quote limit may change after the first saved result. Any later improvement must be a new prospectively frozen version and preserve negative cases.
- Freeze before execution, save complete immutable exclusive-create JSON, exact Git original sha, source hashes and source-line witnesses, test exact deterministic replay, then commit/push via ordinary guarded controls only after repository validation.

    SOURCE_HORIZON=47ed6344a9153dcf366769e95722840fbf1a8f8b
    SOURCE_BUILD=60
    HELDOUT=20_EXCLUDED
    PRIMARY_TASKS=12_EXPOSED
    ARMS=7_ALREADY_EXECUTED
    CANDIDATE_SOURCES_PER_ANSWER=3
    SOURCE_CHAR_LIMIT=12000
    CANDIDATE_SCAN_FIRST_COMPLETE_LINES=35
    QUOTES_MAX_PER_CARRIER=5_INCLUDING_H1
    QUOTE_LENGTH_MAX=550
    MODEL=STANDARD_LIBRARY_FIXED_EXTRACTIVE_CITATION_RENDERER
    REFERENCE_READ_STAGE=ONLY_AFTER_ALL_ANSWER_DRAFTS
    SEMANTIC_CORRECTNESS_GOLD=NOT_QUALIFIED
    CLAUDE_SOURCE_ONLY_REVIEW=NOT_EXECUTED
    FORMAL_R0_P03_SCORE=NONE
    OWNER_PHYSICAL_ARCHITECTURE_SELECTION=false
