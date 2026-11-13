# Source event sample: independently returned GitHub Actions execution witness V01

**Date:** 2026-11-13
**Status:** PUBLIC_GITHUB_API_WITNESS_SUPPLEMENT / SAMPLE_FROZEN_BEFORE_EXTERNAL_QUERY / NOT_BLIND / NOT_SCORED
**Authority:** Exact pre-existing source-only V01 sample at historical Git pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`, 16 SHA-selected commits, all sampling rules committed as an earlier local method file before querying Actions. This is a provenance and execution-basis engineering supplement, not a reference corpus release or a test of private C02 case answerability.

## Full fixed query universe and transport

Query **all 16** source-selected commits, no replacement or post-output selection, using GET:
`https://api.github.com/repos/shakaarlatief/autonomous-data-science-system/actions/runs?head_sha=<commit_sha>&per_page=100`

A non-privileged, read-only GitHub API bridge returned HTTP status and workflow run metadata. Preserve status, total_count, returned_count, exact head SHA, run ID, event trigger, run_attempt, status, conclusion, created_at, updated_at, workflow_id and official run URL. Require every returned `head_sha` to equal the sampled commit. For counts greater than 100, label the single page incomplete. For HTTP errors, record lookup error instead of turning it into `NO_RUN`.

**Crucial distinction:** A direct PR-only endpoint was initially tried and showed zero on some commits, *before* the all-event exact-head API query was chosen. The correct API showed real `push` runs. This method change happened after a limited initial inspection; it is an **exploratory correction**, not a pre-observation blind design. The Git 16-case source sampling did not change. No approach is tuned to obtain a positive result; all run statuses, including failures, are retained.

For a concrete **prespecified source-evidence interpretation check** after discovering run-level success and failure, include job summaries for exactly three observed runs:
- failed workflow `32356647189` (test-matrix successes with evidence persistence failure);
- failed workflow `32359491623` (database diagnosis failure);
- successful workflow `32356647199` (cross-platform test matrix plus evidence-persistence success).

The job selection is explicitly **purposive after observing run-level conclusions**, so job statistics must not be represented as a random sample or independent failure-rate estimate. Retrieve job IDs, names, statuses, conclusions, run attempts, start/end and official URLs, and verify the job's run ID matches the exact selected workflow. These are GitHub's reported outcomes. Do not equate `success` with the substantive correctness of every generated artifact or with live production deploy/owner authorization.

## Truth/authority boundary and custody

- `GIT_COMMIT_CHANGE_CONFIRMED`: independently replayable original Git commit/tree/path membership.
- `EXTERNAL_WORKFLOW_RUN_REPORTED`: public GitHub API returned run with matching commit head_sha. This witnesses a provider-recorded workflow event, not the claims/effect of every step.
- `EXTERNAL_JOB_CONCLUSION_REPORTED`: specific matched run/job reported conclusion; distinguish partial job successes inside failed overall run.
- `EVIDENCE_PUBLICATION_PASSED`: only a run or job named for evidence-persistence has a successful provider-reported completion. This does NOT prove artifact bytes present without separate artifact retrieval.
- `OPERATIVE_AUTHORITY`: requires separate identity-authenticated owner effect, currentness/deployment and independent evidentiary adjudication. **Never infer from CI conclusion**.
- `NO_RUNS_RETURNED` means `NO_MATCHES_IN_THIS_API_QUERY_AT_TIME_OF_QUERY`, not that no tests, local runs, other repository branch runs, archived/deleted jobs or execution ever occurred.

No protected C01/C02 wording, source mappings, gold, review reports, owner credentials, or original source contents are inspected here. This is not formal R0-P03 scoring, not a scored source admission and not a prospective C02 amendment.

Persist one exact exclusive-create JSON receipt in `experiments/r0_p03_navigation_probe` with 16 case-level lookups, 3 job receipts and conservative aggregate counts. Source-run matching, job-run matching, known success/failure inclusion, zero-result semantics and exact rerun or structural tests must be verified before publication. Since GitHub API data is mutable, **immutable saved receipts** are source of what was observed at this time; later live re-query may legitimately differ and should be treated as a separately versioned observation.

    REPO=shakaarlatief/autonomous-data-science-system
    SOURCE_SAMPLE=16_ORIGINAL_GIT_COMMITS
    ALL_EVENTS_API=actions/runs?head_sha=<sha>&per_page=100
    MAX_PAGE=100
    JOB_DETAIL_RUN_IDS=32356647189,32359491623,32356647199
    INITIAL_PR_ONLY_LOOKUP=NEGATIVE_BUT_NOT_EXHAUSTIVE
    PUBLIC_EXTERNAL_RUNS_OBSERVED_BEFORE_SUPPLEMENT_CONTRACT=true
    WORKFLOW_PROVENANCE_ONLY=true
    PRODUCTION_OPERATIVE_AUTHORITY_INFERRED=false
    PRIVATE_REFERENCE_ACCESS=false
    FORMAL_R0_P03_SCORE=NONE
    OUTPUT=EXCLUSIVE_CREATE
