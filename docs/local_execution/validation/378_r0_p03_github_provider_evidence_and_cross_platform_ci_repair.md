# Validation 378: GitHub-native evidence, original Checkpoint 941 Windows CI failure and cross-platform repair

**Date:** 2026-11-14
**Status:** ORIGINAL_CI_FAILURE_PROVIDER_VERIFIED / CROSS_PLATFORM_REPRODUCTION_CONFIRMED / TWO_SCOPE_BOUNDED_REPAIR_COMMITS_PUSHED / FOUR_NATIVE_CI_CHECKS_SUCCESS
**Research:** 681. **Checkpoint:** 942. **Collaboration:** MC-0030 Message 095.
**Authority:** Source/CI evidence only. The GitHub-origin check-run result is a provider observation of CI status, not new original D1 connector transport, model identity, accepted J1, qualified RELATIONAL J2 or J3.

## 1. Actual GitHub API and job-log evidence

Using read-only GitHub App-backed Runtime Bridge GitHub commit/check-run and run APIs, the following original GitHub commit-signature verifications were retrieved:

    cd0cf087a4d0ddb30920a8c753e478da8f92295c -> verified=false, reason=unsigned
    90dc870cd059fa555299505b7c7f8110dadb47f4 -> verified=false, reason=unsigned
    131c54a4aec9f8733af35b1c90e8b16a7c9919a5 -> verified=false, reason=unsigned
    511224a037bf63031ead0eda61754702361eebd7 -> verified=false, reason=unsigned
    36ab6cd33a31d579c68b6b814ca70b1fae59fc40 -> verified=false, reason=unsigned

No API result returned a verified commit signature for these particular sampled commits. This does not prove any source was malicious or identify which GitHub client wrote it.

GitHub reported eight completed Checkpoint 941 checks. The failed checks were exactly:

    132549849947: validate-collaboration-state (windows-latest), failure
    132549849558: repository-integrity (windows-latest), failure

The six other checks succeeded. The detailed GitHub job logs tied the two Windows failures to the original MC-0030 Message 063 duplicate historical identity exception. The original historical file bytes and Git blobs were intact. The check hashed a CRLF-converted Windows worktree instead of the pinned LF byte representation.

## 2. Reproduction and repair

The original exact historical collision file SHA-256 pins were independently checked. Recreating the exact source contents as temporary CRLF worktree files made the validator fail, while the original LF versions passed. This isolates a platform representation issue rather than a third message number or modified historical content.

Commit 66076d3d889645ca43f25d892dbf75a2f8355474:

    .gitattributes
    tests/unit/test_model_collaboration_message_identity.py

The .gitattributes file now marks exactly the two preserved Message 063 historical paths -text, preventing CRLF conversion on Windows while preserving the validator's exact byte hash. A focused test asserts that the worktree equals the original Git blob, preserves expected SHA-256, and that both paths have text attribute unset. The preexisting historic exception and original files were not changed.

The original focused test command using pytest's default host TEMP path failed with five PermissionError fixture setup errors under the constrained Runtime Bridge. Its repository-local basetemp rerun succeeded: **7 passed**. The temporary directory was removed.

Commit 36ab6cd33a31d579c68b6b814ca70b1fae59fc40:

    .github/workflows/model-collaboration-state.yml
    .github/workflows/repository-integrity.yml

Both workflows now include .gitattributes and the message identity test in push and pull_request path filters, and both run the exact test file in their existing cross-platform validation steps. No earlier workflow checks or OS runners were removed.

The new combined local model collaboration and repository integrity regression command (with project-local basetemp) succeeded: **73 passed in 1.81 seconds**. Its repository-local temporary test files were removed. At the repair's publication boundary the GitHub connector's bounded push reported PUBLIC_REPOSITORY_INTEGRITY=PASS. A later direct local scripts/check_repository_integrity.py rerun also returned PASS; two earlier attempts timed out under the 30-second bridge limit and were not counted as completed.

## 3. Provider-native postrepair qualification

The second repair commit triggered two real GitHub Actions workflow runs with event push and exact head SHA 36ab6cd33a31d579c68b6b814ca70b1fae59fc40:

    run 43629997613: Model collaboration state, completed success, attempt 1
    run 43629997620: Repository integrity, completed success, attempt 1

The four native GitHub check-run results were independently queried:

    132554259150: validate-collaboration-state (ubuntu-latest) = completed success
    132554258967: validate-collaboration-state (windows-latest) = completed success
    132554258768: repository-integrity (ubuntu-latest) = completed success
    132554258516: repository-integrity (windows-latest) = completed success

GitHub's own check-run details for both Windows jobs reported head SHA 36ab6cd3, conclusion success, annotationsCount zero, provider app github-actions, app ID 15368.

Original provider-run URLs:

    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43629997613
    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43629997620

The first repair commit had no matching CI checks because prior workflow path filters excluded its two changed files; the second commit fixed that coverage gap. This case demonstrates why no matching check is different from a successful check and why source provenance must preserve workflow trigger policy.

## 4. Assurance boundaries

GitHub's Git object/commit data verifies original source ancestry and content, but sampled commits were unsigned and did not independently authenticate the originating model. GitHub Actions check-runs verify provider-reported CI execution outcomes for named jobs and exact refs, but not which model/connector initiated the Git push. The source-only historical D1 connector attestation remains unverified; no new accepted-effect COVERS or governing J3 result was obtained.

The development branch was independently reported unprotected by the observed GitHub branch-protection endpoint at the prior repair head. A successful CI result is therefore not equivalent to pre-push mandatory enforcement. No branch protections/rulesets, identity trust roots or workflow authority have been changed in this experiment.

## 5. Final postflight of Checkpoint 942 integration

Observed after completing Research 681, Checkpoint 942, Message 095 and project state updates:

- scripts/check_current_routing.py: PASS, current checkpoint 942, formal outcome INCOMPLETE, next boundary p-three-j-two-trust-root-and-provider-receipt-design-next.
- scripts/check_knowledge_map.py: PASS, 19 subjects, 24 foundations, 28 specifications, 681 numbered research records and 943 numbered checkpoint files.
- scripts/check_checkpoint_metadata.py: 943/943 compliant numbered checkpoints, zero errors.
- scripts/check_model_collaboration_state.py: PASS, 28 thread state files.
- scripts/check_repository_integrity.py: PUBLIC_REPOSITORY_INTEGRITY=PASS, including Project Knowledge, collaboration state, routing and Knowledge Map.
- git diff --check: exit 0, with advisory Windows LF/CRLF worktree warnings only.
- Targeted message identity, collaboration state and repository-integrity regression set: **73 PASS in 1.13 seconds** using repository-local pytest basetemp.
- Existing real two-event typed J2 source-assurance port regression set: **44 PASS in 10.78 seconds** with the same bounded local basetemp.
- Total **117 passing local regression cases across two successful commands**, neither a formal P03 benchmark. Repository-local pytest temporary material was removed.

The four GitHub-native Windows/Ubuntu checks recorded in section 3 had already completed SUCCESS for repair commit 36ab6cd3. The eventual Checkpoint 942 documentation commit is a separate new Git SHA and must receive its own source-relative CI status; no prior run can be carried forward automatically. Original D1 E01 transport remains UNKNOWN and no new J2/J3 qualification is claimed.

    ORIGINAL_941_GITHUB_CI=2_WINDOWS_FAIL_6_OTHER_SUCCESS
    SOURCE_BYTES_ORIGINAL=UNCHANGED
    CROSS_PLATFORM_REPAIR_COMMITS=2
    REPAIR_CI=4_GITHUB_PROVIDER_CHECKS_COMPLETED_SUCCESS
    ORIGINAL_D1_PROVIDER_TRANSPORT=UNKNOWN
    AUTHENTICATED_MODEL_ACTOR=NOT_VERIFIED
    NEW_RELATIONAL_J2_QUALIFIED=0
    ORIGINAL_E01_J3=HOLD
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
