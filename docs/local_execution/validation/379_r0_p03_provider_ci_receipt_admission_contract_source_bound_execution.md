# Validation 379: Real GitHub-source receipt replay and trust-root non-escalation

**Date:** 2026-11-14
**Status:** TWO_REAL_SOURCE_CASES_REPLAYED / 52_NEW_ADVERSARIAL_TESTS_PASS / PROVIDER_AUTHENTICATION_NOT_CLAIMED / FORMAL_P03_INCOMPLETE
**Research:** 682. **Checkpoint:** 943. **Collaboration:** MC-0030 Message 096.
**Authority:** Exposed non-governing source-admission and evidence-scoping verification. No new J1 acceptance, independently authenticated owner/agent/provider source, governing J2/J3 or physical selection.

## 1. Original live provider observations

The connected GitHub App API was used in this exposed interaction to inspect both exact original check-run lists, original workflow runs and commit verification statuses. Observed reference SHAs:

    941: 511224a037bf63031ead0eda61754702361eebd7, 8 checks, 6 success / 2 failure
    942: e29329b3097b593a917a386d33f900a3cf97b193, 8 checks, 8 success / 0 failure

Each set comprises five workflow-run IDs and eight concrete check IDs with run attempt=1. Native GitHub commit verification for the two inspected commits reports unsigned. The GitHub account actor is not model-exclusive identity. This is live source API observation but not detached, independently signed proof of the same contents after copying to a file.

## 2. Original source and derived program

The model-transcribed native-source copy is:

    experiments/r0_p03_navigation_probe/v03_provider_ci_receipt_source_snapshot_v01.json

SHA-256 cd37b2222f9efd1e10ba0c884f2fe27af63209abf7605015b7267f265de610bd, 10,143 UTF-8 LF bytes. Two exact -text entries in .gitattributes preserve the source and the immutable derived result across Windows checkout. The added 52nd test verifies both attributes and LF worktree bytes, guarding against the earlier historical Message 063 cross-platform SHA failure pattern.

Its source class explicitly declares a DERIVED model transcription and offline_provider_authentication=false. The code reopens the exact original two Git commit objects and checks their expected parents, then validates the source copy's expected check/run tuples, run attempts, provider app, status binding, exact SHA and completeness. No native GitHub read can occur inside this offline Python program, so all structural decisions are labelled UNAUTHENTICATED_REPLAY.

The program also reopens the existing Research 680 four-effect accepted experimental J1 source context; it does not import any new J1, natural-owner authenticator or provider receipt verification backend.

Actual code and immutable output:

    experiments/r0_p03_navigation_probe/v03_provider_ci_admission_contract_v01.py
    experiments/r0_p03_navigation_probe/v03_provider_ci_receipt_admission_result_v01.json

Actual output from first execution:

    status=R0_P03_V2_EXPOSED_UNSCORED_RECEIPT_TRUST_ROOT_PROTOCOL
    historical_ci_failure_count=2
    later_ci_success_count=8
    provider_receipt_authenticated_by_program=false
    new_qualified_j2=0

The code does not claim that a copied JSON file proves the actual source provider or gives a currently fresh CI verdict for a different Git SHA.

## 3. Actual adversarial suite

Command used:

    .venv/Scripts/python.exe -m pytest -q -p no:cacheprovider --basetemp=tests/.tmp_p03_ci_contract tests/unit/test_r0_p03_v03_provider_ci_admission_contract_v01.py

Final result: **52 PASSED in 6.45 seconds**. This includes wrong-SHA replay, forged app issuer, wrong run/check linkage, duplicate IDs, missing or extra checks, incorrect attempts, false signature and model authentication, changing old failed checks into a coherent false success copy, and preventing that copy from becoming governing proof.

The falsification test explicitly shows the offline parser can recognize a self-consistent rewritten green copy but will **not** admit J2, J3 or provider authentication from it. This is essential: the absence of an authenticated provider client in the Python process is not disguised as a passed native assurance test.

## 4. Existing governing boundaries

Original experiment-only accepted J1 effects remain four. Newly accepted J1=0, natural-owner RELATIONAL J2=0, native original D1 connector transport independently verified=false, historical E01 J3 HOLD, original D1_AMEND unchanged, formal R0-P03 INCOMPLETE, physical target unselected. Checkpoint 942's 8/8 GitHub CI success remains a source-relative result of that exact historical commit, not a declaration about any later documentation head.

## 5. Final structural and regression postflight

Actual postflight after completing the source, Research 682, Checkpoint 943, Message 096, routing and Knowledge Map:

- scripts/check_current_routing.py: PASS with current checkpoint 943, formal outcome INCOMPLETE and boundary p-three-trusted-provider-and-owner-source-feasibility-next.
- scripts/check_knowledge_map.py: PASS with 19 subjects, 24 foundations, 28 specifications, 682 numbered research records and 944 numbered checkpoint files.
- scripts/check_checkpoint_metadata.py: 944/944 numbered checkpoints compliant, zero errors.
- scripts/check_model_collaboration_state.py: PASS, 28 thread-state files.
- scripts/check_repository_integrity.py: PUBLIC_REPOSITORY_INTEGRITY=PASS, including the focused validators and Project Knowledge authority.
- git diff --check: PASS, exit 0, advisory Windows line-ending warnings only.
- New provider CI receipt admission suite: **52 PASS in 6.45 seconds**, including the exact -text source/receipt byte-preservation regression.
- Existing source-bound two-event typed J2 suite: **44 PASS in 11.88 seconds**.
- Earlier real forward at-action source suite: **39 PASS in 14.52 seconds**.
- Collaboration-state, historical message identity and repository-integrity regression set: **73 PASS in 1.34 seconds**.
- Total **208 passing test cases across four completed test invocations**. These are unscored engineering controls and are not formal R0-P03 B0-B4 comparator results.
- The repository-local pytest temporary directory was removed. Both exact JSON artifacts are -text, raw LF source SHA unchanged, and no historical D1/Message 091/accepted J1 source was rewritten.

Checkpoint 942's 8/8 provider-reported CI outcome remains bound to its exact original SHA. The eventual Checkpoint 943 documentation commit requires independent GitHub check-run verification; an older successful provider receipt is not transferable.

    SOURCE_CASES=2_REAL_GITHUB_API_HISTORIES
    SOURCE_COPY_GITHUB_SIGNED=false
    OFFLINE_SOURCE_VERIFIER_TRUST_ROOT=ABSENT
    NEW_TARGET_EFFECT_ACCEPTED=0
    ORIGINAL_EXPERIMENT_ONLY_J1=4
    NEW_J2_RELATIONAL=0
    HISTORICAL_E01_J3=HOLD
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
