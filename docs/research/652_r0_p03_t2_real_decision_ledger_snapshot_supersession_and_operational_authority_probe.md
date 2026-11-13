# Research 652: Actual two-snapshot decision ledger authority and supersession qualification

**Date:** 2026-11-13
**Status:** ACTUAL_94_REQUEST_GIT_DECISION_LEDGER_T2_V03_EXECUTED / SCOPED_DECISION_PRESENCE_AND_SUPERSESSION / NO_REAL_OPERATIVE_AUTHORITY_GOLD
**Scope:** Extend Checkpoints 913–914 beyond source-title/header echoing to explicit project decision identities and real original Git-history differences. Test a fixed snapshot, source-specific status, partial supersession scope, contradictory identity and selected-successor/not-operational controls.
**Authority:** Actual original Git blobs for `docs/DECISIONS.md` at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` (S0) and `6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3` (S1), before-output method contract, exclusive-create complete real source/result trace and actual regression. Research 513/559/576 remain unscored. **Checkpoint 915, Validation 351**.
**Scientific status:** EXPOSED_REAL_DOCUMENT_REGRESSION / NO_INDEPENDENT_NEUTRAL_USER_GOLD / NO_FORMAL_R0-P03_ARM_SELECTION.

## 1. Why this was a material next step

The new-source T2 V01 Checkpoint 913 retrieved source-local `Status` with a 22/24 top-one exact-document rate. Checkpoint 914 tested a complete normalized first-H1 gate over those same title-derived questions and recovered the two wrong-top-one cases, but the gate was advantaged by the query construction and could not answer a substantive question about governing decisions. Claude's exposed Message 064 called for source-authored lifecycle and authority evidence rather than path-only relations or inferred authority from arbitrary `Status` wording.

The repository already has a **source-authored decision ledger** where decisions are numbered D-NNN, individual sections have exact `**Status:**` lines, some supersession is explicitly partial, and a selected successor can be accepted but not yet operational. The appropriate near-term move was to execute real snapshot-dependent decision queries, rather than add more H1-derived status examples.

This 94-request experiment asks precisely what the two historical Git *records* contain. It does **not** claim to verify that a repository status is factually true of deployment, or that an accepted selection currently governs the code. It is not a genuine independent human evaluation: the ledger and failure modes are already exposed, the request templates are coordinator-authored, and the exact numbered ID is supplied to the parser. The ledger at the earlier S0 Git blob also overlaps the old 65-source universe, so no new blind source status is asserted.

## 2. Frozen source horizon and actual change

Two exact public repository Git object snapshots were pinned before the run, both containing `docs/DECISIONS.md`. Actual source parsing found:

| Evidence | S0 earlier Git revision | S1 later Git revision |
| --- | --- | --- |
| Numbered decision sections | **35** | **36** |
| Decision range | D-001 through D-035 | D-001 through D-036 |
| D-035 recorded source Status | `Accepted / selected successor target / not yet operational authority` | Same |
| D-036 recorded source Status | Not present in this version of the ledger | `Accepted / selected successor target / not yet operational authority` |
| Explicit superseded decisions | D-003, D-011, D-015 | D-003, D-011, D-015 |

The public original Git blobs and each individual section body, exact section boundaries, heading line, Status line, optional Date line and Superseded-in-scope line were preserved with SHA-256 hashes and Git blob SHA-1. The parser rejects ambiguous duplicate decision IDs, missing Status and duplicate Status fields. All 36 newer decision IDs are distinct and all 35 earlier IDs are preserved. A pre-execution source inspection observed that D-036 was added and status labels of the shared 35 did not change. These are recorded observations, not blinded discoveries.

D-003 explicitly records private-to-public supersession in the current repository state, but does not preserve an exact original visibility-change decision/date. D-011 is superseded only in certain technology-architecture scopes; its residual constraint against premature selections remains applicable in other unspecified subsystems. D-015 is superseded in its architectural-uncertainty scope while the exclusion of unrelated binary learning sources from public Git persists. The method preserves each **complete Status and scope text**, rather than collapsing those decisions into one global `SUPERSEDED` bit.

## 3. Frozen test requests, methods and answer contract

Before indexing, deterministic code constructed **94 typed request envelopes**:

| Request type | Count | Grounded answer channel |
| --- | ---: | --- |
| Status of each of 36 newer IDs at both snapshots | 72 | 71 source-recorded Status, 1 bounded source absence (D-036 at S0) |
| D-900 through D-903 at both snapshots | 8 | Absence **only from that examined Git snapshot** |
| Five fixed mismatched ID/title pairs at each snapshot | 10 | Conflicting identity; no source-Status assertion |
| Governing/operative Status of D-035/D-036 at both snapshots | 4 | Three explicit `not yet operational` source statements; one source absence |
| **Total** | **94** | **No positive operative-governance assertion** |

All queries include the explicit `snapshot`, `decision_id`, typed `intent`, and, for mismatch tests, a separate full `requested_title`. A natural-language paraphrase is persisted for review, but parsing arbitrary user language into those fields has **not** been tested.

Methods run over exactly the same per-snapshot section bodies:
- **Section lexical baseline:** SQLite FTS5/BM25 Unicode61 over full original numbered decision-section bodies for S0 or S1, top five by deterministic rank, using the user-supplied ID and optional title. This is useful as a candidate retrieval comparator, not as a subject/governance oracle.
- **Lexical top-one Status:** Naively identifies the best-ranked section and interprets its Status, without verifying that it belongs to the user's requested ID. Deliberately weak hazard diagnostic.
- **Naive latest-only:** Uses S1's exact ID even when the user explicitly asks about S0. A deliberately invalid time-scope comparator.
- **Naive accepted-is-operative:** Interprets a top section's `Accepted` prefix as positive operational authority. An intentionally unsound semantic control, not a fair contemporary retrieval arm.
- **Identity-and-snapshot evidence guard:** Uses the requested ID in the exact requested source snapshot and refuses contradictory full titles, unknown IDs and unsupported positive operational status. It returns original section lines, Git source and status/scope evidence, never inferred global governing truth.
- **Combined two-channel answer:** Adds the same lexical top-five candidates as a separate **not-authority** list, without converting relevance into accepted governing fact. Its assertion rule is intentionally identical to the evidence guard.

The experimental `Status` category is syntax-bound: `RECORDED_SUPERSESSION_WITH_SCOPE`, `RECORDED_SELECTED_NOT_OPERATIVE` or `OTHER_RECORDED_DECISION`. The third is *not* equated to currently operational; it includes accepted records with possibly narrower original intent. The original first lines and optional supersession scope remain present in the output.

## 4. Actual comparison and genuine failures

| Observed measure | Value |
| --- | ---: |
| Actual Git decision sections at S0 and S1 | 35 + 36 |
| All executed requests | **94** |
| Original status tasks / source Status correct | **71/71 existing sections**, plus correct scoped absence for the 72nd |
| Lexical top-ranked section matches requested ID, ordinary status requests | **53/72** (includes one expected source absent at S0) |
| Lexical top-one wrong ID across all 94 requests | **39** |
| Explicit contradictory ID/title requests rejected | **10/10** |
| Unknown decision IDs returned as bounded source absence | **8/8** |
| Explicit supersession scope witnesses retained | **6/6** |
| Selected-not-operational ledger statements returned as negative statements | **3** |
| Old-snapshot D-036 correctly not recorded | **1** |
| Naive latest-only leaked D-036's later Status into S0 | **1** |
| Naive accepted-is-operative asserted positive despite explicit source negative | **1** |
| Wrong recorded decision Status from guarded answer | **0** |
| Positive operative-governance assertions from guarded answer | **0**, by construction |
| Two-channel non-authoritative lexical candidates kept | **94/94** |

The **19 mismatched top-one results in 72 normal Status tasks** show that even exact ID terms, when queried with lexical OR across entire sections, can be diluted by other IDs mentioned in historical decision texts. This is not evidence that a carefully tuned lexical ID filter or semantic system would necessarily fail. The index/ID resolver have different information and task roles.

A specifically observed temporal counterexample is D-036. It is not a ledger decision in S0, yet the naive `latest-only` method produces its S1 source Status. This is an actual version-grounded false historical attribution, not a speculative failure or a false nonexistence claim.

Another actual counterexample is the accepted/nonoperative distinction. For the S1 D-036 operative request the lexical top section is D-036 and the naive `Accepted` prefix produces `OPERATIVE_TRUE`, contradicting the very same source's `not yet operational authority` clause. The evidence guard only reports the exact document's **recorded explicit negative** and declines to establish any independent operational state.

The supersession scope counterexamples matter as well. A global `SUPERSEDED` label for D-011 would lose that only some old architecture-uncertainty scopes have been replaced. A source may be historically superseded for one effect while containing other still-applicable reasoning. D-003 also explicitly warns that exact transition timing is missing. The parser preserves these qualifications and does not invent dates or missing causes.

## 5. Interpretation, model choice and next falsifier

**Supported:** An information system that can recognize explicit decision IDs and source versions can avoid some temporally wrong and wrong-document assertions that unconstrained retrieval permits. A source-defined accepted record is not necessarily an operative authority record; typed scope and currentness have to remain separate. Search candidates still help even when no answer is qualified.

**Not supported:** General natural-language decision resolution, independent owner verification, present-day deployment state, live effective source authority, fair B0–B4 physical architecture choice, benefits of embedding-based retrieval, quantitative cost advantages or the true world status of any incomplete source. The observed counts mainly measure internal extraction fidelity with the same ledger that supplies the answer key. The two negative comparators were deliberately flawed, and the current ID lookup is directly advantaged by requests containing exact IDs. These are engineering controls, not neutral system-performance comparisons.

The next decisive investigation requires a **different independent source/task frame**, or a truly distinct human-originated question set and source-owner/lifecycle answer packet: questions referencing decisions by meaning and scope without pre-supplied IDs, contradictory owner approvals, superseded decisions and operative effect transitions. Compare lexical, identity and alias mapping, source-authority metadata, source-backed two-channel hybrid and fair embedding retrieval with equal context/cost. Allow `UNKNOWN/NOT_CONFIRMED` and separately score false authority, correct temporal scope, correct referent, citations, candidate recall, and metadata authoring burden. Do not continue merely to optimize the exposed 65/120/36 fixture or silently promote it to formal Research 513 primary gold.

All code/branch/workflow/database design decisions remain open to principled revision. No project technology or physical architecture is promoted merely because this mechanism passes its source-own regression.

    CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_T2_DECISION_LEDGER_SNAPSHOT_AND_SCOPE_CONTRACT_V03.md
    EXECUTABLE=experiments/r0_p03_navigation_probe/exploratory_t2_decision_ledger_snapshot_and_scope_v03.py
    RESULT=experiments/r0_p03_navigation_probe/exploratory_t2_decision_ledger_snapshot_and_scope_result_v03.json
    ORIGINAL_RESULT_BYTES=710228
    ORIGINAL_RESULT_SHA256=c22d6b1e62616066f55e22b8811feb21e383e6a568de36a06faf38de7d6d8a27
    S0_ORIGINAL_GIT=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    S1_ORIGINAL_GIT=6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3
    EXPOSED_REQUESTS=94
    STATUS_RECORDS_IN_PAIR=71
    EXTRA_SOURCE_ABSENCE=1
    SOURCE_SCOPE_PRESERVED=6
    NAIVE_LATEST_SNAPSHOT_LEAKAGE=1
    NAIVE_ACCEPTED_OPERATIVE_ERROR=1
    NEW_INDEPENDENT_GOLD=NONE
    ORIGINAL_FORMAL_R0_P03_SCORE=NONE
