# Validation 376: Actual forward J2 at-action source receipt, independent Git facts and qualification boundary

**Date:** 2026-11-14
**Status:** NEW_GIT_ACTION_COMPLETED_AND_PUBLISHED / ONE_SOURCE_CLAIM_CO_COMMITTED / 39_NEW_TESTS_PASS / OWNER_AND_PROVIDER_ASSURANCE_NOT_QUALIFIED
**Research:** 679. **Checkpoint:** 940. **Collaboration:** MC-0030 Message 093.
**Authority:** Exposed, non-governing source/evidence feasibility test. No new accepted J1, natural-owner qualified J2, J3, formal P03 score, physical architecture or migration.

## 1. Actual action and publication

The registered Codexless workspace was clean on the shared v1-source-vault-bootstrap-resume branch, local and origin tracking head fefa21bd57df9d40d71a53c5b8af8da0d81b667c.

One JSON actor-authored source record was exclusively created BEFORE the commit, with its planned parent, exact path, single-file commit intent, requested Codexless Git commit mechanism and explicit non-governing assurance limitations. The source itself stated the commit had not yet happened and its SHA was not yet known.

The bounded codex_git_commit_paths operation was invoked with precisely that one file and the expected previous head, returning exit 0, index clean, exact action commit 131c54a4aec9f8733af35b1c90e8b16a7c9919a5. A subsequent codex_git_push_ff_only returned exit 0 with ordinary non-force same-branch publication and repository integrity PASS.

Independent Git postflight:

    commit = 131c54a4aec9f8733af35b1c90e8b16a7c9919a5
    parent = fefa21bd57df9d40d71a53c5b8af8da0d81b667c
    changed = [A experiments/r0_p03_navigation_probe/v03_forward_j2_at_action_event_001.json]
    blob_oid = 425b365c3a845e776babbccd8a6ecf7188c3a73b
    git_bytes = 2990
    source_sha256 = ce7a6addb7c1b612c4e1ed5a65fa3baacf06c57f11fae06a512e213b41f923a2

The Git original and materialized worktree match byte-for-byte. Git independently verifies the commit's tree membership and parent/path, NOT the identity of the actor who typed the claim or the actual provider API that performed the invocation. The observed tool response exists in this live conversation but is not a detached provider signature or independently persisted platform call record.

## 2. Durable derived preflight

Files:

    experiments/r0_p03_navigation_probe/v03_forward_j2_at_action_event_001.json
    experiments/r0_p03_navigation_probe/v03_forward_j2_at_action_evidence_probe_v01.py
    experiments/r0_p03_navigation_probe/v03_forward_j2_at_action_evidence_result_v01.json
    tests/unit/test_r0_p03_v03_forward_j2_at_action_evidence_probe_v01.py

The prospective experiment contains a COVERS field targeting only UNACCEPTED_PROBE_ONLY_ACTION_RECORDING_CRITERION. That is deliberately NOT an accepted J1 effect. The claim is a source-local actor statement, identity NOT independently authenticated and J2 NOT admitted.

The separate Python program reads the exact real commit and its original bytes, verifies the closed source schema, original parent/path, the source role and all assurance exclusions, then contrasts the result with the historical Message 091 CANNOT_ATTEST result. The projection is deterministic and refuses overwrite if a future execution yields different facts.

Actual direct invocation succeeded, reporting:

    status = REAL_GIT_AT_ACTION_CLAIM_COCOMMITTED_WITH_INDEPENDENT_OBSERVABLES
    git_verified = true
    actor_claim_cocommitted = true
    provider_proof = false
    qualified_j2 = 0

Artifact bytes and SHA-256 at stable post-test read:

- Original event source: 2,990 bytes, ce7a6addb7c1b612c4e1ed5a65fa3baacf06c57f11fae06a512e213b41f923a2.
- Executable: 12,608 bytes, e26d6548a9d13d6366b5f0d0a77e21db4e63f10d5dec71ae9aca24b3f3333dc2.
- Derived immutable JSON: 3,810 bytes, 60b4b8a36b1aed1af4e201847a131858996587be240d8bf4e395cfd52568e2e7.
- Tests: 10,695 bytes, 0c64e4c6a9db38b0fbf6d9c57d607521646de0eeab0544e67279af751791ffa1.

## 3. Actual tests

Command:

    .venv/Scripts/python.exe -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_v03_forward_j2_at_action_evidence_probe_v01.py

Initial execution: 38 passed, one test regex failure because the program classified false precommit post-action status with a distinct error code. No source or model semantics were changed. The test matcher was corrected.

Final execution: **39 passed in 14.29 seconds, exit 0.** The tests cover exact published Git commit, parent/path/blob, source claim in same tree, no provider or actor identity escalation, no accepted J1 target, no J2 qualification, unchanged historical D1/J3, and negative controls for false identity, altered source path/branch/parent, multiple changed files, false precommit knowledge, fabricated provider proof, switched fact owners and attempted E01 coverage.

These are source-integrity and design feasibility checks, not 39 formally scored navigation tasks.

## 4. Remaining engineering boundary

The source-attached claim is a promising local-carrier pattern, but the evidence is not sufficient to select it as the physical architecture or declare a governing effect satisfied. A strong next discriminating experiment would compare genuine independent source-owner relationship binding and native provider execution receipts, ideally against a separately owner-accepted experimental target. No such new effect has been accepted.

Research 512 distinguishes direct OBSERVABLE facts, genuine source-owner RELATIONAL coverage and durable EPHEMERAL receipts. This probe preserves those classes rather than silently promoting any self-authored claim.

## 5. Final repository postflight

Actually observed postflight after Checkpoint 940, Research 679, collaboration Message 093, source program and routing updates:

- scripts/check_current_routing.py: PASS, current checkpoint 940, formal experiment INCOMPLETE and current boundary p-three-j-two-source-assurance-port-next.
- scripts/check_knowledge_map.py: PASS, 19 subjects, 24 foundations, 28 specifications, 679 numbered Research records and 941 numbered checkpoint files.
- scripts/check_checkpoint_metadata.py: 941/941 numbered checkpoints compliant, zero errors.
- scripts/check_model_collaboration_state.py: PASS, 28 collaboration-state records.
- scripts/check_repository_integrity.py: PUBLIC_REPOSITORY_INTEGRITY=PASS, including Project Knowledge, checkpoint, Knowledge Map, collaboration and routing guards.
- git diff --check: exit 0, only advisory Windows worktree LF/CRLF messages.
- New real forward at-action J2 source probe: **39 PASS in 14.17 seconds**.
- Historical Claude Message 091 CANNOT_ATTEST reconciliation: **25 PASS in 28.52 seconds**.
- Original natural-owner J2 evidence preflight: **33 PASS in 20.33 seconds**.
- Earlier real-source, X1 and Project Knowledge authority regressions: **180 PASS in 13.69 seconds**.
- Existing experiment-only accepted D1 J1 projection: **16 PASS in 8.87 seconds**.
- Original D1 owner event/admission suite, split to respect the fixed 30-second command limit: **7 PASS in 4.49 seconds** and complementary **15 PASS in 24.58 seconds**. No cases were omitted across the two selections.
- Total **315 passing regression cases across seven successful invocations**. These are engineering source/authority tests, NOT 315 independent blinded Research 513 navigation tasks or any formal P03 B0-B4 outcome.

A genuine one-file action has been published already as commit 131c54a4. The subsequent validation receipt remains strictly DERIVED and does not become a second natural fact carrier. No original D1, owner J1 packet, existing formal protected gold, production authority, or physical target was modified.

    REAL_FORWARD_SOURCE_EVENT=COMMITTED_AND_PUSHED
    ACTOR_CLAIM=CO_COMMITTED_UNQUALIFIED
    AUTHENTICATED_CLAIMANT=NO
    PROVIDER_NATIVE_EXECUTION_RECEIPT=NOT_VERIFIED
    NEW_QUALIFIED_J2=0
    EXISTING_P03_ACCEPTED_J1=4
    ORIGINAL_E01_J3=HOLD
    FORMAL_R0_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
