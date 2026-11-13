# T2 V03: Real decision-ledger snapshot, identity, supersession scope and selected-not-operative semantics

**Date:** 2026-11-13
**Status:** METHOD_FIXED_BEFORE_FIRST_SAVED_V03_OUTPUT / EXPOSED_SOURCE_DERIVED_REGRESSION / NOT_INDEPENDENT_CURRENT_AUTHORITY_GOLD
**Primary rationale:** The last 120-source T2 V02 experiment can precisely bind a requested source status but cannot establish accepted decision authority or time-scoped supersession. This experiment directly exercises source-owned numbered decision records and Git-snapshot lifecycle evidence.

## Frozen real source world

Read original Git blob `docs/DECISIONS.md` at exactly two public commits:
- **S0 (earlier):** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`.
- **S1 (later):** `6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3`.

Do not inspect the mutable worktree as the evidence basis. Every claim must name the Git snapshot and exact original evidence line. These documents were partly exposed in prior 65-source tests; **this is an additional nonblind mechanistic regression**, not a newly independent corpus.

A pre-execution read established that S0 includes D-001...D-035, S1 includes D-001...D-036, D-036 is absent from S0, and D-003/D-011/D-015 carry explicit supersession language while D-035 and D-036 carry `not yet operational authority`. This preflight is disclosed. No independent gold claim is made.

## Fixed section parser and evidence

Parse only exact level-two headings `## D-NNN. <title>` in `docs/DECISIONS.md`. Maintain unique decision IDs and original line boundaries. Require exactly one `**Status:**` in each section; capture the first original status line and its text, strip two trailing Markdown hard-break spaces only for normalized comparisons while retaining source line unchanged. Capture original `**Date:**` and optional `**Superseded in scope:**`, retaining exact lines. Preserve section byte range/fragment heading and each witness's SHA-256 and source Git blob SHA-1. Reject duplicate IDs or missing Status. All sections share one original document, but a `D-035` record is **not** the same semantic identity as the whole file.

The only predeclared *syntactic* status categories:
- `RECORDED_SUPERSESSION_WITH_SCOPE` when original Status begins `Superseded`; preserve the full status, and `Superseded in scope` field as a qualified description. This is NOT universal supersession.
- `RECORDED_SELECTED_NOT_OPERATIVE` when original Status contains literal `not yet operational authority` (case insensitive); this is a **negative source statement**, not independently verified present-time deployment state.
- `OTHER_RECORDED_DECISION` otherwise. `Accepted` wording here is source-authored decision status, **not** evidence of current operative deployment.

Do not treat a documentary date as a timestamp that overrides Git snapshot provenance. A missing D-036 at S0 means `NOT_RECORDED_IN_THIS_SNAPSHOT`, not that the decision never existed or no other authority exists.

## Deterministic fixed request matrix (94)

Generate before indexing:
1. **RECORDED_STATUS:** for all 36 IDs of S1, one request at each S0 and S1. Total **72**. User-form query text references the literal `D-NNN`, no title echo; exact source status requested, including scoped supersession and nonoperative qualifications.
2. **UNKNOWN_ID:** nonexistent IDs D-900, D-901, D-902, D-903 at each snapshot. Total **8**. All should yield not recorded in covered ledger, not global nonexistent.
3. **CONFLICTING_ID_TITLE:** five fixed pairs `(D-003,D-011)`, `(D-015,D-024)`, `(D-028,D-035)`, `(D-033,D-036)`, `(D-035,D-036)`; request the **first ID** with the **other decision's actual title** as an explicit topic-confirmation field. Repeat at each snapshot. Total **10**. Reject if both fields cannot point to the same unique source section, including when the other ID was not present at S0. The title is generated from S1 records and only appears in an explicit structured `requested_title` field; we are not evaluating natural-language extraction.
4. **OPERATIVE_GOVERNANCE:** explicit operation question for D-035 and D-036 at each snapshot. Total **4**. Answer `RECORDED_NOT_YET_OPERATIONAL` *only where that literal section statement exists*; answer `NOT_RECORDED_IN_THIS_SNAPSHOT` if absent. Never assert positive real-world operative governance. Answers are about recorded decision-ledger evidence only.

All requests carry `snapshot_id`, `requested_decision_id`, typed `intent` and an optional `requested_title`; a real NL question sentence is persisted for inspection but **the engine receives parsed fields rather than performing NL understanding**. No request receives a label, an expected source section, or a target state. Exact IDs are realistic explicit identifiers and intentionally easy for an ID lookup. This is a scoped identity/provenance correctness test, not a semantic-paraphrase benchmark.

## Methods, same source scope and budget distinctions

Both snapshots have separate *section-level* SQLite FTS5 Unicode61/BM25 indexes over all their exact real decision-section bodies, K=5. Lexical input is only the explicit requested decision ID, plus requested title when present (do not access answer labels). Stable rank by BM25 and ID; persist top-five for every request. A lexical-only policy returns candidates with `NO_STATUS_ASSERTION`.

The **LEXICAL_TOP1_STATUS** source-only comparator reads the Status of the first retrieved section without confirming requested ID/title or Git snapshot target. It must not be passed the expected label. This is an intentionally weak hazard comparator, not a fair full B0-B4 design. The **NAIVE_LATEST_ONLY** comparator chooses the S1 decision record by requested ID even if user asked about S0; this tests snapshot leakage, not fair retrieval. The **NAIVE_ACCEPTED_IS_OPERATIVE** comparator claims `OPERATIVE_TRUE` for any source Status beginning `Accepted`; it is deliberately invalid and scored only against direct explicit `not yet operational authority` source statements.

The **EVIDENCE_GUARDED_IDENTITY** policy uses the exact decision-ID index of the requested snapshot (not a hidden expected target): if requested ID is not present, return `NOT_RECORDED_IN_THIS_SNAPSHOT` with scoped coverage and nonassertive candidate suggestions. If an explicit title field is provided, require its full normalized spelling to match the same section's full title, else `CONFLICTING_IDENTITY`. For recorded-status intent return the complete source Status plus exact location and scope witness, with category but **no operative-governance assertion**. For operative intent, only an explicit negative status yields `RECORDED_NOT_YET_OPERATIONAL`; all other present IDs return `UNSUPPORTED_OPERATIVE_GOVERNANCE`. None of these methods infer real owner authority/currentness beyond the source text.

**TWO_CHANNEL_EVIDENCE_GUARDED** returns identical evidence-bound assertion plus independently retained lexical K5 candidate paths/decision IDs in a separate `not_authority` list. Status candidate retrieval and operative authority assertion must never be fused. This is an answer-shape comparison, not a distinct scoring victory.

## Measurements and stopping

Save all 94 predeclared requests and exact original two Git blob hashes, all 36+35 section witness digests, status/supersession scope strings, candidate rankings, comparator outputs, evidence-guarded outputs and neutral evaluation fields. Compare:
- correct *ledger-section status retrieval by requested snapshot* for 72 normal requests;
- false claimed S0 record status for D-036, relative to original S0 absence;
- scope preservation for D-003/D-011/D-015 in both snapshots;
- explicit selected-not-operative handling for D-035 (both) and D-036 (S1 only);
- unsupported or conflicting controls (8 missing IDs, 10 conflicts, 4 operative questions);
- safe separate candidate retention and false provenance statements; exact Git byte replay.

No item drops, model retuning, post-result correction of task subsets, or source mutation. Document any first-run failures and fix only with explicit pre-output method boundary amendment. This records what the **decision ledger actually says**, not independent reconstruction of time/implementation events. It cannot answer a user asking “what really governs now?” absent validated source-owner/activation evidence.

Original R0-P03 Research 513/559/576 remains unscored; no physical architecture selected, no true B2/B3/B4 arm claim, and prior Checkpoint 914 original result remains immutable.

    S0=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    S1=6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3
    REAL_DECISION_SECTIONS_S0=35
    REAL_DECISION_SECTIONS_S1=36
    EXPECTED_REQUESTS=94
    SOURCE_GOLD=DOCUMENTED_DECISION_STATUS_ONLY
    INDEPENDENT_EVALUATOR_GOLD=false
    FORMAL_R0_P03_SCORING=NONE
    OUTPUT=EXCLUSIVE_CREATE
