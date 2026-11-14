# Validation 380: Live GitHub check/job/workflow contradiction and source assurance boundary

**Date:** 2026-11-14
**Status:** LIVE_PROVIDER_SOURCE_CONTRADICTION_REPRODUCED / COHERENT_GIT_SOURCE_IDS / SOURCE_STATUS_HOLD / 53_NEW_TESTS_PASS
**Research:** 683. **Checkpoint:** 944. **Collaboration:** MC-0030 Message 097.
**Scope:** Evaluate a genuine native GitHub CI status contradiction across current connected provider tools. Bind all source records to exact commit/check/job/workflow IDs and source issuer. Prove source conflict is neither false CI failure nor unqualified CI success, and avoid promoting a derived source copy to governing actor/transport proof.
**Authority:** Engineering and exposed source qualification only. No accepted new effect, independently signed provider receipt, natural-owner J2, original D1 connector proof, governing J3, formal P03 score, physical target or migration.

## Live provider reads

Real GitHub App-backed Runtime Bridge calls for exact commit 2a7f8fe3f170840262122296d9b7f3e54664bc39 returned:

    check 132565047313: in_progress, success, completedAt=2026-11-14T19:41:49Z
    job 132565047313: in_progress, success, completedAt=2026-11-14T19:41:49Z
    run 43633469851: completed, success, attempt=1
    job steps: five completed success
    commit check list: seven completed success plus the inconsistent eighth

Source identity bindings all matched. GitHub Actions issuer app ID 15368 and app slug github-actions matched. The source current check's annotation was a non-failing Ubuntu runner migration notice. Independent read through the separately connected GitHub job reader confirmed the same job status and completed step states; root cause remains not proven.

The exact source relay is an expressly DERIVED coordinator transcription, not provider signed:

    experiments/r0_p03_navigation_probe/v03_live_ci_provider_conflict_source_v01.json
    bytes=5091
    sha256=1d968a4eb516780c70cfd70ae51a82eadbcad8e92e043b861a2a1f5b0c776bf2

The program rechecks exact Git original source ancestry, rejects wrong issuer/source/run/check IDs and duplicate/missing facts, then classifies the conflicting source status:

    experiments/r0_p03_navigation_probe/v03_live_ci_provider_reconciliation_v01.py
    experiments/r0_p03_navigation_probe/v03_live_ci_provider_reconciliation_result_v01.json
    source_status=SOURCE_REPORTED_CONTRADICTION
    completed_success=7
    failed_complete=0
    conflicting_check=132565047313
    provider_authenticated_from_relay=false
    new_qualified_j2=0

Source and result JSON are pinned to raw LF Git bytes by two exact -text .gitattributes entries, with a regression for both. No new credential, provider signature or privileged read capability was created inside the Python module.

## Local test execution

The first focused test execution had 52 passing tests and one failed test caused by an incorrect assumption that the first workflow job in a returned array was the selected Ubuntu job. The verifier correctly retained the source conflict. The test was revised to select the target by its source-owned job ID 132565047313 rather than list order; no validator semantics were weakened.

The complete corrected targeted execution was:

    .venv/Scripts/python.exe -m pytest -q -p no:cacheprovider --basetemp=tests/.tmp_p03_944 tests/unit/test_r0_p03_v03_live_ci_provider_reconciliation_v01.py

Result: **53 PASS**. Negative tests cover cross-SHA replay, wrong source issuer and app ID, duplicate or missing checks/jobs, inconsistent list/check/job fields, completed-parent and nonterminal-child conflict, source-reported failure, true pending state, all-five-step conformance, independence of unrelated workflow failures, false signed-owner claims and source copy not becoming provider authentication.

## Final postflight

Actually observed after Research 683, Checkpoint 944, Message 097, current routing and Knowledge Map updates:

- scripts/check_current_routing.py: PASS, checkpoint 944, formal R0-P03 INCOMPLETE, current boundary p-three-provider-composite-or-capability-hold-next.
- scripts/check_knowledge_map.py: PASS, topics 19, foundations 24, specifications 28, research 683, numbered checkpoints 945.
- scripts/check_checkpoint_metadata.py: 945/945 numbered checkpoints compliant, zero errors.
- scripts/check_model_collaboration_state.py: PASS, 28 thread-state records.
- scripts/check_repository_integrity.py: initial 30-second Runtime Bridge call timed out without a reported failing assertion; subsequent read-only retry PASS, including Project Knowledge, checkpoint, Knowledge Map, collaboration and routing guards and PUBLIC_REPOSITORY_INTEGRITY=PASS.
- git diff --check: exit 0, only advisory Windows LF/CRLF warnings.
- New live provider source status reconciliation: **53 PASS in 0.40 seconds**.
- Research 682 provider receipt admission controls: **52 PASS in 5.94 seconds**.
- Research 680 typed J2 source assurance controls: **44 PASS in 11.16 seconds**.
- Genuine forward at-action event source controls: **39 PASS in 13.59 seconds**.
- Collaboration, historical message identity, routing and repository integrity controls: **73 PASS in 1.46 seconds**.
- Total **261 passing regression cases across five successful pytest invocations**. These are unscored engineering tests, not primary Research 513/673 navigation comparisons.
- Temporary project-local pytest source was removed. The new exact source relay and its derived result are raw LF blobs with -text in .gitattributes, preserving their SHA-256 across Windows checkout.

The evidence belongs to original 943 source commit 2a7f8fe3. The forthcoming Checkpoint 944 documentation commit must be checked against its own native provider check-run status, without inheriting the original seven successes, conflict or any earlier PASS.

    SOURCE_COMMIT=2a7f8fe3f170840262122296d9b7f3e54664bc39
    NATIVE_CI_STATUS=SOURCE_CONFLICT_HOLD
    COMPLETED_SUCCESS_CHECKS=7
    FAILED_CHECKS=0
    EIGHT_FULLY_COMPLETED=NOT_ESTABLISHED
    AUTHENTICATED_ACTOR_IDENTITY=NOT_ESTABLISHED
    EXISTING_EXPERIMENT_J1=4
    NEW_RELATIONAL_J2=0
    HISTORICAL_E01_J3=HOLD
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
