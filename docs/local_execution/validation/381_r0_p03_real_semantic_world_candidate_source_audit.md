# Validation 381: P03-V2 real-content semantic-world candidate and exact prospective owner J1 packet

**Date:** 2026-11-14
**Status:** ORIGINAL_SOURCE_WORLD_GIT_AUDIT_EXECUTED / PROJECT_KNOWLEDGE_IDENTITY_REFRESH_CANDIDATE_VERIFIED / EXPERIMENT_ONLY_J1_PACKET_PREPARED_UNACCEPTED
**Research:** 684. **Checkpoint:** 945. **Collaboration:** MC-0030 Message 098.
**Scope:** Verify original real ADS source histories and experimental-source boundaries needed for Research 672–673 M1–M6, assess the least unblocked semantic-world candidate, and preflight a precisely bounded new J1 owner proposal without converting an unverified historical statement into qualified J2/J3.
**Authority:** Exposed, unscored preadmission development. No historical source rewrite, accepted new experimental J1, natural-owner J2, real S1 transition, integrated J3, formal B0-B4 score, physical target or migration.

## 1. Exact source and Git checks

Original immutable source pin:

    5463b2ad2e6799339746637f38340fa2a9dc00f6

The executable auditor rebuilds Research 674's 15 distinct original Git paths and 16 witnesses with original source-role classes. It independently verifies 12 additional original source witnesses across 10 candidate paths, four new beyond the first source frame, for a combined 19 real source paths. Every witness includes original Git blob ID, SHA-256, path, line, source role and exact source commit.

Historical implementation event verification:

    G006 commit: 99cca3484f4dcb37128c38c2436a6dbcd6d00a0f
    G006 parent: 256c5bfa253a9ad178e1fa578c028071cb26f6d2
    G013 commit: 192dc161203577c11e7a7fce869634a5fccc29d8
    G013 parent: abd752d3c604a382121e45773442de69ed4c01e1

These commits are ancestors of the original pin and contain their expected code/test changed paths. Source role distinctions preserve natural code vs test definition vs historical gate report vs frozen contract/navigation source. Research 181/189 report historical G006/G013 implementation gates accepted, but not P03 experiment-specific J1 effects. Those commits' chronological order is not by itself a source-authorized J1 REPLACE or J2 COVERS.

The original D1 Research 676 effect set remains four accepted development-only J1, zero qualified RELATIONAL J2, historical D1_AMEND and no new J3 satisfaction.

## 2. Actual live functional checks

The original G006 identity test file was invoked with four targeted semantic-selector fragments:

    current identity/canonical move, explicit supersession, move-merge-split/retirement and duplicate current ownership

Observed:

    5 PASS, 58 deselected, exit 0, 0.52s

The current G013 refresh tests were executed separately:

    test_g006_same_identity_move_and_authored_transition_are_not_rename_heuristics
    1 PASS, 39 deselected, exit 0, 9.26s

    test_manifest_output_relocation_selects_only_that_view_and_matches_full_build
    1 PASS, 39 deselected, exit 0, 7.70s

An earlier combined broader refresh selection exceeded the Codexless Runtime Bridge's 30-second timeout and was neither recorded as a pass nor a failed assertion. The two narrowed tests passed. All current live executions used the current development repository environment and do not pretend to have executed the exact historical build as of the older source pin.

## 3. New audit and proposed packet

Created, executed and source-verified:

    experiments/r0_p03_navigation_probe/v03_real_pk_semantic_candidate_audit_v01.py
    experiments/r0_p03_navigation_probe/v03_real_pk_semantic_candidate_audit_result_v01.json
    tests/unit/test_r0_p03_v03_real_pk_semantic_candidate_audit_v01.py

Source audit result is 12,613 UTF-8 LF bytes, SHA-256:

    59de22c2709d380189d60cab305902bff7033f9453cd5687223abe58805f56ac

Created separately:

    experiments/r0_p03_navigation_probe/v03_real_pk_semantic_j1_owner_proposal_v01.py
    experiments/r0_p03_navigation_probe/v03_real_pk_semantic_j1_owner_proposal_v01.json
    tests/unit/test_r0_p03_v03_real_pk_semantic_j1_owner_proposal_v01.py

Exact frozen proposal:

    P03V2_PKA_REAL_SOURCE_TWO_STATE_EXPERIMENT_J1_001
    canonical_payload_sha256 = 0fa8ecc09f4745b514697d206356ce2f529fa66e15380a9bd0d43f1c6a00a6df
    status = PROPOSED_NOT_OWNER_ACCEPTED
    proposed effects = 4
    admitted new effects = 0

S0 and S1 are explicitly **prospective experimental** effect states. The proposed LIFECYCLE would REPLACE S0 with S1 under OPEN_RESET only when a separately qualified real prospective source-revision event activates it. The proposal explicitly requires real natural-owner COVERS and executed source-revision evidence, and prohibits derived output/path promotion into authority. A later valid owner acceptance still requires its own binding, not a user-reply dictionary supplied to the proposed program.

The proposed effect-state timeline is not presented as the historical G006-to-G013 Git commit relationship. No source-owner J2 has been qualified or future source transition executed.

## 4. Source/owner packet adversarial tests

The first auditor suite had two failed test assumptions: the expected number of *candidate unique paths* was eight rather than ten, and a swapped historical commit's valid SHA triggered the parent-mismatch diagnostic instead of an invalid-commit diagnostic. The test assertions were corrected to match verified source facts. The source/audit code was not changed for either failure.

The final candidate-audit suite passed:

    39 PASS in 12.16 seconds

The first proposed owner-packet suite exceeded the 30-second command limit because negative tests repeatedly regenerated the entire original Git source graph. The rejection route was narrowed to exact staged-packet comparison and still always refuses arbitrary owner claims; its positive full Git source audit is separately executed and tested. Final proposal suite:

    29 PASS; verified in a combined 68-case audit/proposal run (17.83 seconds)

Both JSON artifacts are explicitly -text in .gitattributes to prevent Windows CRLF checkout from changing the original pinned raw-byte source and proposed packet digest. Their original source texts were generated as LF UTF-8.

The exact packet tests verify source-audit SHA, exact new effect IDs and two-state lineage, ALL_REQUIRED realization components, missing genuine source-owner J2, false authority/derived nonpromotion, no automatic new acceptance or migration, and forged model-written owner decisions rejected.

## 5. Final structural and regression postflight

Actual final checks after Research 684, Checkpoint 945, Message 098, source audit/owner packet, Knowledge Map, collaboration state and routing updates:

- scripts/check_current_routing.py: **PASS**, checkpoint 945, branch v1-source-vault-bootstrap-resume, formal outcome INCOMPLETE, next p-three-real-source-effect-owner-review-next.
- scripts/check_knowledge_map.py: **PASS**, 19 topics, 24 foundations, 28 specifications, 684 numbered research records and 946 numbered checkpoint files.
- scripts/check_checkpoint_metadata.py: **946/946 PASS**, no numbered errors.
- scripts/check_model_collaboration_state.py: **PASS**, 28 collaboration states.
- scripts/check_repository_integrity.py: first read-only attempt exceeded the 30-second Runtime Bridge limit, but the next read-only invocation returned PUBLIC_REPOSITORY_INTEGRITY=PASS with Project Knowledge, Knowledge Map, checkpoint, collaboration and routing gates passing. The timeout was not counted as either a failing assertion or a successful check.
- git diff --check: **PASS**, exit 0 with only advisory Windows CRLF conversion messages.
- Exact real source audit and proposed experiment-only owner packet suites: **68 PASS in 17.83 seconds**, comprising 39 source audit and 29 proposed packet cases.
- Preexisting actual original Research 674 source-frame and Research 676 accepted-J1 projection regression suites: **44 PASS in 18.97 seconds**.
- Collaboration, historical duplicate identity and repository integrity regression suites: **73 PASS in 1.67 seconds**.
- Real current-code semantic behavior checks: **5 G006 identity PASS**, **1 G013 cross-semantic identity move PASS**, **1 G013 manifest relocation/full rebuild equivalence PASS**.
- Total **192 distinct passing test cases across six successful selected invocations**. These are exposed engineering source and regression tests, NOT independently authored/scored R0-P03 B0–B4 navigation tasks.
- The local pytest temporary directory was removed. Both new JSON artifacts are exact LF files and explicitly text-unset in .gitattributes. Audited source-result file SHA-256 59de22c2709d380189d60cab305902bff7033f9453cd5687223abe58805f56ac; staged owner-review packet file SHA-256 340ec577f6bbe2fca7f8739cc33788e878bff659cf6ef554745d60af7d3088b0. The latter is distinct from its canonical content SHA-256 0fa8ecc09f4745b514697d206356ce2f529fa66e15380a9bd0d43f1c6a00a6df.

The owner decision remains **PENDING** regardless of local regression results or eventual GitHub CI. No new experiment-only J1, source-owner J2, integrated J3 or physical target is admitted; original Source Method M1–M6 and historical D1 effect packet remain untouched.

    SOURCE_CANDIDATE_REAL_GIT=VERIFIED
    COMBINED_REAL_SOURCE_PATHS=19
    NEW_EFFECTS_PROPOSED=4
    NEW_EFFECTS_ACCEPTED=0
    J2_NATURAL_OWNER_QUALIFIED=0
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
