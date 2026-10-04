# Research 515: R0-P02 Attempt 001 hidden-output-vocabulary harness invalid and Attempt 002 prospective refreeze

**Date:** 2026-10-04
**Status:** R0-P02 ATTEMPT 001 HARNESS_INVALID / NO ARCHITECTURE INFERENCE / ATTEMPT 002 OUTPUT CONTRACT PROSPECTIVELY FROZEN / LIVE-HOST LEG HELD
**Parent:** Research 512-514
**Probe:** R0-P02
**Candidate under test:** GOVERNED_LEDGER_KERNEL_V02
**Attempt 001 candidate commit:** `4d045aba282dc1ca609698c1b6d27e3365fa5fd9`
**Attempt 001 result commit:** `53871536bf3f65684c77d6248f75729d3b9e973e`
**Attempt 001 evidence:** `experiments/r0_p02_authority_admission_v01/attempt_001_result.md`
**Scope:** Preserve and classify the first deterministic-core execution, identify the exact blindness/contract defect without changing the frozen semantic test, and prospectively freeze the only permitted Attempt 002 repair before any second score observation.
**Authority:** Harness-defect classification and prospective Attempt 002 repair authorization only. No R0-P02 PASS/AMEND/REOPEN result, physical-target selection, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction, live-host execution, or authority switch is authorized.

## 1. Attempt 001 was frozen before scoring

The bounded implementation produced only:

    experiments/r0_p02_authority_admission_v01/candidate.py

ChatGPT independently reviewed it against the permitted Research 512-514 / fixture / candidate-contract surface while preserving oracle/scorer blindness.

The candidate was then committed alone:

    4d045aba282dc1ca609698c1b6d27e3365fa5fd9
    Freeze R0-P02 candidate attempt 001

and pushed before scoring.

The exact scorer was actually executed once after that freeze. A preceding Runtime Bridge call using an out-of-range timeout was rejected by tool-schema validation before process dispatch and therefore did not execute the scorer.

The observed scorer result was preserved before interpretation at:

    experiments/r0_p02_authority_admission_v01/attempt_001_result.md

and committed/pushed as:

    53871536bf3f65684c77d6248f75729d3b9e973e
    Freeze R0-P02 attempt 001 scorer result

No Attempt 001 candidate repair occurred after result observation.

## 2. Frozen observed result

The scorer reported:

    deterministic_core = FAIL
    case_count         = 20
    error_count        = 57
    metamorphic_checks = 2
    process exit       = 1

The exact error list remains in the frozen attempt evidence.

The live-host leg did not start because Research 514 requires deterministic-core PASS first.

## 3. Post-result inspection boundary

Only after both the candidate and observed result were durably frozen did ChatGPT inspect the previously hidden:

    oracle.json
    score.py

That post-result inspection cannot affect Attempt 001 authorship and does not retroactively expose the blinded implementer.

It is used only to classify the failed attempt and define a prospective repair, as explicitly permitted by Research 514 when a failure is a harness/implementation defect rather than evidence against the architecture mechanism.

## 4. Defect found: exact scored vocabulary was hidden from the blinded implementer

Research 514 froze exact expected outcomes inside the hidden oracle and required the implementer not to inspect that oracle or scorer.

The allowed implementation contract froze:

    output object shape
    case order
    mechanism families to implement
    C19 = CHAIN_VALID / LATESTNESS_UNPROVEN

but it did not publish the complete exact outcome/latestness vocabulary or its normalization rules.

The scorer nevertheless required exact string equality against that hidden vocabulary.

Therefore a blinded implementation could correctly detect a condition while failing because it used a semantically narrower or differently named result label that it had no permitted source from which to learn.

Codex explicitly reported this ambiguity before scoring:

    most outcome/latestness labels, concrete record layouts,
    and case sequencing were unspecified

The omission was real.

## 5. Why the 57 errors are diagnostic of the contract defect

The 57 reported errors consist of the same 19 primary field-classification mismatches repeated across:

    base evaluation                 19
    renamed-case metamorphic        19
    alternate-context metamorphic   19

Total:

    57

The scorer did not report:

    nondeterminism
    output-schema failure
    fixture-order failure
    digest-format failure
    case-ID hard-coding dependence
    alternate project/secret dependence
    semantic-base conflict failure
    forged-signature acceptance
    duplicate-acceptance failure
    duplicate-sequence failure
    fresh-verifier overclaim on C19
    rebuild-equivalence failure

Representative mismatches show the defect directly:

    changed signed envelope
        candidate detected ENVELOPE_DIGEST_MISMATCH
        hidden oracle required INVALID_SIGNATURE

    decision substitution
        candidate detected DECISION_MISMATCH
        hidden oracle required INVALID_SIGNATURE

    cross-project replay
        candidate detected PROJECT_MISMATCH
        hidden oracle required WRONG_PROJECT

    broken previous digest
        candidate detected BROKEN_PREV_DIGEST
        hidden oracle required CHAIN_BREAK

    host transform
        candidate preserved and admitted the detached proof
        hidden oracle required the reporting label PROOF_UNCHANGED

    recovery after admission
        candidate returned DONE and mechanically checked no duplicate mutation
        hidden oracle required DONE_NO_DUPLICATE

    witnessed truncation
        candidate outcome detected ROLLBACK_DETECTED
        candidate latestness also said ROLLBACK_DETECTED
        hidden oracle required latestness STALE

These are scored-interface vocabulary mismatches. They do not provide valid evidence that the underlying Git-ledger mechanism failed its architecture question.

This finding also explains why the same mismatches survived both metamorphic transformations: the candidate was not keying on literal case IDs or one synthetic project/secret context.

## 6. Attempt 001 classification

Accordingly:

    R0_P02_ATTEMPT_001=HARNESS_INVALID
    DETERMINISTIC_CORE_RECORDED_RESULT=FAIL
    ARCHITECTURE_INFERENCE=NONE

This is not PASS because the frozen scorer did not pass.

This is not AMEND or REOPEN because the observed failures do not establish a load-bearing mechanism failure.

This is not permission to reinterpret the frozen FAIL as a PASS.

The raw Attempt 001 result remains exactly as observed.

## 7. Prospective Attempt 002 repair principle

Attempt 002 repairs only the missing public output-classification contract.

The following remain unchanged:

    Research 513 probe question and decision thresholds
    Research 514 20-case fixture
    fixture.json
    oracle.json
    score.py
    canonicalization profile
    synthetic HMAC profile
    semantic-base rules
    signed-statement bindings
    ledger order / prev-digest chain
    duplicate-admission control
    recovery requirement
    witness/fresh-verifier distinction
    metamorphic checks
    deterministic-core PASS rule
    live-host gate

The architecture candidate is unchanged.

The only new allowed information is the exact canonical result vocabulary and general semantic normalization rules required by the already-frozen scorer.

Those rules are frozen in:

    experiments/r0_p02_authority_admission_v01/
        attempt_002_output_contract.md

This is prospective: it is committed before any Attempt 002 candidate modification or score observation.

## 8. Attempt 002 implementation blindness

The bounded Attempt 002 implementer may read only:

    docs/research/512_mc0030_claude_critique_reconciliation_governed_ledger_kernel_v02.md
    docs/research/513_r0_physical_architecture_decision_probe_preregistration_v01.md
    docs/research/514_r0_p02_authority_admission_fixture_harness_freeze_v01.md
    docs/research/515_r0_p02_attempt001_hidden_output_vocabulary_harness_invalid_and_attempt002_refreeze.md
    experiments/r0_p02_authority_admission_v01/fixture.json
    experiments/r0_p02_authority_admission_v01/candidate_contract.md
    experiments/r0_p02_authority_admission_v01/attempt_002_output_contract.md
    experiments/r0_p02_authority_admission_v01/candidate.py

The implementer must not inspect:

    oracle.json
    score.py
    attempt_001_result.md
    any future Attempt 002 result
    any later repair/result artifact

The implementer may edit only:

    candidate.py

The repair must remain limited to canonical result classification/reporting. It may not weaken checks, remove negative controls, change semantic mechanics, or add case_id-specific answer mappings.

Syntax checks and non-oracle smoke checks are allowed.

Scoring is not.

## 9. Attempt 002 score rule

After the revised candidate is independently reviewed and frozen in a new commit:

    score.py may be executed exactly once for Attempt 002

Once that score is observed:

    the Attempt 002 candidate is frozen
    no result-guided repair to Attempt 002 is permitted

A further attempt would require another explicit prospective defect classification and refreeze.

There is no retry-to-green.

## 10. Live-host boundary

The Research 514 live-host squash/transport leg remains held.

It may begin only if a valid deterministic attempt satisfies the unchanged PASS condition:

    score.py exits 0
    deterministic_core = PASS
    error_count = 0
    20/20 frozen cases match
    both metamorphic checks pass

## 11. Current state

    R0_P02_ATTEMPT_001=HARNESS_INVALID
    ATTEMPT_001_ARCHITECTURE_INFERENCE=NONE

    FIXTURE_CHANGED=false
    ORACLE_CHANGED=false
    SCORER_CHANGED=false
    THRESHOLDS_CHANGED=false
    ARCHITECTURE_CANDIDATE_CHANGED=false

    ATTEMPT_002_OUTPUT_CONTRACT=FROZEN
    ATTEMPT_002_CANDIDATE=NOT_IMPLEMENTED
    ATTEMPT_002_RESULT=NOT_OBSERVED

    LIVE_HOST_LEG=NOT_STARTED
    PHYSICAL_ARCHITECTURE_SELECTED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    NEXT=BOUNDED_MANUAL_CODEX_ATTEMPT_002_CANDIDATE_REPAIR
