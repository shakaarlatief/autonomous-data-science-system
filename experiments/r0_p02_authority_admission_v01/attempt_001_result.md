# R0-P02 Attempt 001 deterministic-core result

**Status:** RESULT OBSERVED / CANDIDATE FROZEN / NO REPAIR AUTHORIZED BY THIS ARTIFACT
**Candidate commit:** `4d045aba282dc1ca609698c1b6d27e3365fa5fd9`
**Scorer:** frozen `experiments/r0_p02_authority_admission_v01/score.py`
**Oracle:** frozen `experiments/r0_p02_authority_admission_v01/oracle.json`

## Execution integrity

The candidate was committed and pushed before scoring.

One attempted Runtime Bridge command was rejected by tool-schema validation because `timeoutMs=60000` exceeded the surface maximum of 30000. That rejection occurred before command execution and did not run the scorer.

The scorer was then actually executed exactly once with:

```text
python experiments/r0_p02_authority_admission_v01/score.py
```

Observed process exit code:

```text
1
```

## Observed scorer output

```json
{
  "case_count": 20,
  "deterministic_core": "FAIL",
  "error_count": 57,
  "errors": [
    "C01_GENESIS_VALID latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C02_BASE_ACCEPTANCE_VALID latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C03_UNRELATED_NON_GOVERNING latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C04_UNRELATED_GOVERNING latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C05_CONFLICT_A_ADMITS latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C06_CONFLICT_B_AFTER_A latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C08_CHANGED_ENVELOPE outcome 'ENVELOPE_DIGEST_MISMATCH' != 'INVALID_SIGNATURE'",
    "C09_DECISION_SUBSTITUTION outcome 'DECISION_MISMATCH' != 'INVALID_SIGNATURE'",
    "C10_CROSS_PROJECT_REPLAY outcome 'PROJECT_MISMATCH' != 'WRONG_PROJECT'",
    "C11_ACCEPTANCE_ID_REPLAY latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C13_BROKEN_PREV_DIGEST outcome 'BROKEN_PREV_DIGEST' != 'CHAIN_BREAK'",
    "C14_MIDDLE_CHAIN_REWRITE outcome 'ENVELOPE_DIGEST_MISMATCH' != 'CHAIN_BREAK'",
    "C15_HOST_TRANSFORM outcome 'ADMITTED' != 'PROOF_UNCHANGED'",
    "C15_HOST_TRANSFORM latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C16_INTERRUPTED_BEFORE_ADMISSION latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C17_INTERRUPTED_AFTER_ADMISSION outcome 'DONE' != 'DONE_NO_DUPLICATE'",
    "C17_INTERRUPTED_AFTER_ADMISSION latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "C18_PRIOR_WITNESS_TRUNCATION latestness 'ROLLBACK_DETECTED' != 'STALE'",
    "C20_OUT_OF_BAND_HEAD_WITNESS latestness 'ROLLBACK_DETECTED' != 'STALE'",
    "renamed-case metamorphic: META-01 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-02 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-03 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-04 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-05 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-06 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-08 outcome 'ENVELOPE_DIGEST_MISMATCH' != 'INVALID_SIGNATURE'",
    "renamed-case metamorphic: META-09 outcome 'DECISION_MISMATCH' != 'INVALID_SIGNATURE'",
    "renamed-case metamorphic: META-10 outcome 'PROJECT_MISMATCH' != 'WRONG_PROJECT'",
    "renamed-case metamorphic: META-11 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-13 outcome 'BROKEN_PREV_DIGEST' != 'CHAIN_BREAK'",
    "renamed-case metamorphic: META-14 outcome 'ENVELOPE_DIGEST_MISMATCH' != 'CHAIN_BREAK'",
    "renamed-case metamorphic: META-15 outcome 'ADMITTED' != 'PROOF_UNCHANGED'",
    "renamed-case metamorphic: META-15 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-16 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-17 outcome 'DONE' != 'DONE_NO_DUPLICATE'",
    "renamed-case metamorphic: META-17 latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "renamed-case metamorphic: META-18 latestness 'ROLLBACK_DETECTED' != 'STALE'",
    "renamed-case metamorphic: META-20 latestness 'ROLLBACK_DETECTED' != 'STALE'",
    "alternate-context metamorphic: C01_GENESIS_VALID latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C02_BASE_ACCEPTANCE_VALID latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C03_UNRELATED_NON_GOVERNING latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C04_UNRELATED_GOVERNING latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C05_CONFLICT_A_ADMITS latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C06_CONFLICT_B_AFTER_A latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C08_CHANGED_ENVELOPE outcome 'ENVELOPE_DIGEST_MISMATCH' != 'INVALID_SIGNATURE'",
    "alternate-context metamorphic: C09_DECISION_SUBSTITUTION outcome 'DECISION_MISMATCH' != 'INVALID_SIGNATURE'",
    "alternate-context metamorphic: C10_CROSS_PROJECT_REPLAY outcome 'PROJECT_MISMATCH' != 'WRONG_PROJECT'",
    "alternate-context metamorphic: C11_ACCEPTANCE_ID_REPLAY latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C13_BROKEN_PREV_DIGEST outcome 'BROKEN_PREV_DIGEST' != 'CHAIN_BREAK'",
    "alternate-context metamorphic: C14_MIDDLE_CHAIN_REWRITE outcome 'ENVELOPE_DIGEST_MISMATCH' != 'CHAIN_BREAK'",
    "alternate-context metamorphic: C15_HOST_TRANSFORM outcome 'ADMITTED' != 'PROOF_UNCHANGED'",
    "alternate-context metamorphic: C15_HOST_TRANSFORM latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C16_INTERRUPTED_BEFORE_ADMISSION latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C17_INTERRUPTED_AFTER_ADMISSION outcome 'DONE' != 'DONE_NO_DUPLICATE'",
    "alternate-context metamorphic: C17_INTERRUPTED_AFTER_ADMISSION latestness 'NOT_APPLICABLE' != 'VALID_AS_PRESENTED'",
    "alternate-context metamorphic: C18_PRIOR_WITNESS_TRUNCATION latestness 'ROLLBACK_DETECTED' != 'STALE'",
    "alternate-context metamorphic: C20_OUT_OF_BAND_HEAD_WITNESS latestness 'ROLLBACK_DETECTED' != 'STALE'"
  ],
  "metamorphic_checks": 2,
  "protocol": "R0-P02-V01",
  "schema_version": 1
}
```

This artifact preserves the observed result only. It does not classify the cause, authorize a repair, start Attempt 002, or start the live-host leg.
