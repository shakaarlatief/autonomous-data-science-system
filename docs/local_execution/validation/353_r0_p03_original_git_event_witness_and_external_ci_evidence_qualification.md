# Validation 353: Original Git evidence-class sampling and externally reported workflow execution

**Date:** 2026-11-13
**Status:** ACTUAL_SOURCE_AND_EXTERNAL_RUN_WITNESS_SAVED / DEDICATED_TESTS_PASS / REPOSITORY_CHECKS_PENDING
**Scope:** Validate exact historical Git source event partition/sample, original Git diff-tree witnesses, all 16 publicly returned GitHub Actions queried commit SHA associations, mixed workflow/job statuses and the bound step-level exception.
**Research:** Research 654. **Checkpoint:** 917.
**Authority:** Original Git pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`, two method contracts, frozen sampling rule, real original Git and GitHub API returns, three immutable JSON receipts and dedicated replay tests.

## Original evidence

    GIT_ORIGINAL_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    NONMERGE_HISTORICAL_COMMITS=3230
    WORKFLOW_CHANGE=117_SAMPLE_4
    TEST_CHANGE=203_SAMPLE_4
    IMPLEMENTATION_CHANGE=615_SAMPLE_4
    DOCUMENTATION_ONLY=2047_SAMPLE_4
    OTHER_OR_UNCLASSIFIED=248_SAMPLE_0
    SAMPLE_TOTAL=16
    ORIGINAL_GIT_DIFF_TREE_VERIFIED=16
    SOURCE_BYTES_INSPECTED=NONE
    PRIVATE_C01_C02_QUESTION_OR_GOLD_ACCESS=NONE

The source-only contract was written before the first sampled roster was generated. A complete Git log classification was performed on *all* 3230 reachable non-merge commits and cross-verified against `git rev-list`. The 16 source-selected commits were independently checked using `git cat-file`, `git merge-base` and `git diff-tree` changed path results. Their complete selected identities, original diff-tree stdout SHA-256 and Git metadata are in the saved source result.

    SOURCE_RESULT_BYTES=27509
    SOURCE_RESULT_SHA256=2c50e692a63f8542307fd325f987fc792a7a7cd9698f5c68885b01e120d11900

After seeing the 16 SHA IDs, a first PR-only run lookup was found to be incomplete for the relevant question. The all-event direct GitHub Actions API was then applied to **every** originally selected SHA without changing the sample. The exact 16 query URLs, HTTP 200 statuses, result counts and individual matched-head workflow IDs/statuses/URLs were preserved. All results fit in one 100-result page per SHA.

    EXTERNAL_MATCHED_COMMITS=9
    EXTERNAL_ZERO_QUERY_MATCHES=7
    REPORTED_WORKFLOW_RUNS=27
    RUN_SUCCESS=25
    RUN_FAILURE=2
    EXTERNAL_RESULT_BYTES=30236
    EXTERNAL_RESULT_SHA256=a320ddea0a0905805dc2550661c54b17e9c1c08dc30288a1f584be54921aa65a

A post-result purposive, non-random job inspection of exact runs `32356647189`, `32359491623`, `32356647199` found 15 jobs (13 success, two failure). The provider step receipts for selected jobs `96387316689`, `96395817325`, `96387336750` preserve actual success/failure step names. The failure of `Persist successful interchange evidence` after six green test matrix jobs is a real case demonstrating separation of test status and workflow/evidence-persistence outcome. An observed success step does not verify released artifact bytes.

    STEP_RESULT_BYTES=6624
    STEP_RESULT_SHA256=654771d41ab68adecb4ec28f787579c9b7cd4a88aa0162d8573e9fc1dc14775d

## Executed dedicated test evidence

`tests/unit/test_r0_p03_source_event_witness_capacity_and_external_ci.py`: **7/7 PASS** (3.50 seconds). Tests reconstruct all 3230 original Git commits and deterministic selected 16; rerun the source-only V01 executable from original Git and compare complete JSON; validate original diff-tree and source semantics; check external run counts against exact sampled SHAs, mixed success/failure conclusions and precise returned URLs; verify all job/step associations and their purposive selection; enforce that no source status is promoted to owner-signed operative governing authority.

## Observed grouped regression and full prepublication repository controls

All selected test files and assertions actually executed with isolated `--basetemp` and pytest cache disabled:

| Actual verified unit suite | Result |
| --- | --- |
| New source event, original-Git path census, deterministic 16 commit replay and external run/job/step receipts | **7/7 PASS** (4.04s latest) |
| Previous T2 V04 64-case no-ID four-method comparator and exact source/result replay | **9/9 PASS** (0.53s) |
| Previous T2 V03 94 real two-snapshot decision-ID/authority qualifier | **9/9 PASS** (0.28s) |
| Previous native Specification 025/028 reference-grammar V03 and model collaboration state/identity | **41/41 PASS** (6.51s) |
| Existing C02 source-free aggregate/identity and protected evidence boundary regressions | **15/15 PASS** (0.17s) |
| Previous T2 V02 118-case source-referent/authority abstention and replay | **10/10 PASS** (1.00s) |
| Previous T2 V01 synthetic status-grammar/keyword/heading controls | **3/3 PASS** (0.14s) |
| Previous T2 V01 original 120-document Git roster, sampling and source identity | **2/2 PASS** (17.44s) |
| Previous T2 V01 full deterministic original Git-source result replay | **1/1 PASS** (14.09s) |
| Previous T2 V01 saved 24-case result and two original failures | **2/2 PASS** (0.12s) |
| **Total selected nonoverlapping observed tests** | **99/99 PASS** |

Additional actual repository gates:
- `scripts/check_current_routing.py`: **PASS** for Checkpoint **917**, branch `v1-source-vault-bootstrap-resume`, boundary `p-three-original-git-and-ci-evidence-witness-tested`, original R0-P03 outcome `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **654**, **918** numbered checkpoints and 19 topic groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **918/918** canonical checkpoints compliant.
- `git check-attr text` for all three exact original Git/provider JSON receipts: **unset** to preserve their bytes on Windows.
- `git diff --check`: **PASS**, only routine Windows LF/CRLF warnings in tracked text files.
- `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including family-aware contracts, Project Knowledge validation, checkpoint, Knowledge Map, model collaboration and routing.
- Original exclusive-create receipt sizes/hashes: source Git 27,509 / `2c50e692a63f8542307fd325f987fc792a7a7cd9698f5c68885b01e120d11900`; externally reported workflows 30,236 / `a320ddea0a0905805dc2550661c54b17e9c1c08dc30288a1f584be54921aa65a`; purposive step reports 6,624 / `654771d41ab68adecb4ec28f787579c9b7cd4a88aa0162d8573e9fc1dc14775d`. Byte-identity checks and complete Git-source rerun are covered by dedicated tests, and exact committed bytes must still be checked after commit.

The GitHub/API evidence has no current provider-server immutability guarantee; immutable saved results represent this witnessed observation, and later API changes do not retroactively invalidate a truthful historical receipt. The API witnesses are not independently reproduced test executions, build artifact confirmations or owner-signed deployments.

**Publication and remote branch verification remain pending** until the actual commit/push/postflight result. No C02 private task text, original restricted case-to-source mapping or answer gold was inspected. No new source was admitted or any existing scientific hold repaired.

## Boundary

Git provenance and CI provider metadata are two different evidence layers. The initial PR-only endpoint's lack of results does not imply no workflows; the corrected all-event endpoint is still not universal execution or deployment proof. A saved `success` conclusion can coexist with another failing workflow on the same commit. No protected C02 question/gold/source mapping was inspected, no case fully closed, no new independent question author activated, no task/source admitted and no Research 513/559/576 formal score authorized.
