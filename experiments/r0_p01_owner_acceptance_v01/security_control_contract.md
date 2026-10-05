# R0-P01 V01 Security Control Contract

**Status:** PROSPECTIVELY FROZEN
**Protocol:** R0-P01-V01
**Applies to:** every REALIZABLE owner-exclusive cryptographic arm

The result vocabulary is public. There is no hidden oracle.

Each control returns PASS or FAIL. NOT_APPLICABLE is permitted only for Arm C, which is not a cryptographic selection candidate.

## 1. VALID_ACCEPTANCE

Create the exact SignedAcceptanceStatement and a proof from the current valid owner credential.

PASS only if independent verification succeeds and the acceptance ID has not previously been consumed.

## 2. FORGED_OR_AGENT_PREPARED_PROOF_REJECTS

Modify proof bytes without owner credential use.

PASS only if verification rejects.

The harness must never manufacture a replacement valid proof.

## 3. CHANGED_ENVELOPE_REJECTS

Change one semantic envelope field after proof creation while reusing the original proof.

Recompute the presented envelope_digest as the attacker would, so the presented statement differs from what the original credential signed.

PASS only if the original proof rejects against the changed statement.

## 4. CHANGED_SHOWN_VIEW_REJECTS

Change one byte of the exact displayed owner-view representation after proof creation and recompute shown_digest.

PASS only if the original proof rejects against the changed statement.

## 5. DECISION_SUBSTITUTION_REJECTS

Replace ACCEPT with REJECT for the security vector while reusing the original proof.

PASS only if verification rejects.

AMEND substitution is equivalent and need not be a second owner proof.

## 6. CROSS_PROJECT_REPLAY_REJECTS

Replace project_id with OTHER-PROJECT-SYNTHETIC while reusing the original proof.

PASS only if verification rejects.

## 7. ACCEPTANCE_ID_REPLAY_REJECTS

Two distinct replay classes are checked:

A. same proof attached to a different acceptance_id:
   cryptographic verification must reject because the statement changed.

B. exact same already-consumed statement/proof presented a second time:
   cryptographic proof may remain mathematically valid, but the harness admission guard must reject the repeated acceptance_id.

PASS requires both.

## 8. SEMANTIC_BASE_MISMATCH_REJECTS

Change semantic_base_digest while reusing the original proof.

PASS only if verification rejects.

## 9. UNRELATED_REPOSITORY_LANDING_DOES_NOT_INVALIDATE

Introduce a synthetic unrelated carrier/repository metadata change that is not part of any SignedAcceptanceStatement field.

PASS only if the unchanged statement/proof still verifies exactly.

This control prevents accidental whole-repository binding.

## 10. SIGNER_SET_MISMATCH_REJECTS

Change signer_set_version while reusing the original proof.

PASS only if verification rejects.

## 11. TRUST_ROOT_ROTATION_DRY_RUN

Construct a synthetic signer-set rotation envelope.

The CURRENT primary credential must sign the exact rotation SignedAcceptanceStatement.

PASS only if:

    current credential proof verifies
    proposed new signer/public fingerprint is visible in the rendered effect
    rotation cannot be authorized by the candidate/new signer alone
    signer-set version changes only after the current proof is accepted

For Arm A the target signer may be the recovery public key.

For Arm B the target signer may be the Arm-A primary public key; heterogeneous signer sets are permitted by the probe.

No production trust root changes.

## 12. RECOVERY_CREDENTIAL_DRY_RUN

The preregistered recovery public key is part of the synthetic trust-root fixture before the dry-run.

The owner uses the recovery Ed25519 credential to sign a synthetic recovery-rotation SignedAcceptanceStatement.

PASS only if:

    recovery proof verifies
    an unregistered key cannot act as recovery
    recovery rotates the synthetic signer set prospectively
    prior accepted proofs remain historically valid
    no recovery secret enters the result

For both A and B, the exact recovery credential is the dedicated Arm-A recovery Ed25519 key.

No production recovery path changes.

## 13. COMPROMISE_BOUNDARY_DRY_RUN

Declare a synthetic compromise boundary for the current primary credential.

Use an otherwise valid already-created proof whose synthetic ledger position is after that boundary.

PASS only if the harness classifies the acceptance:

    REVIEW_REQUIRED
    resolving_owner = GOVERNING_OWNER

rather than silently accepting it as current or retroactively invalidating pre-boundary accepted records.

This is a deterministic policy dry-run and requires no additional credential secret.

## 14. Zero-miss gate

For A/B:

    eligible_security = all 13 controls PASS

One FAIL makes the arm ineligible for P01 PASS_WITH_SELECTION.

Controls may not be removed, weakened, renamed into success, or post-hoc marked NOT_APPLICABLE after owner results are observed.
