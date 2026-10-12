# Validation 239: native OpenSSH verification observation and regression

**Date:** 2026-10-12
**Research:** Research 551
**Scope:** Real non-owner Ed25519 SSHSIG verification against trusted expected synthetic run-bound statements, verifier-error segregation, and adjacent historical F1/security regressions.
**Parent:** Checkpoint 887 / Validation 238
**Status:** 15_NEW_NATIVE_SSH_TESTS_PASS / 409_FOCUSED_PASS / PUBLIC_INTEGRITY_PASS
**Authority:** Bounded test-only implementation, not owner credential qualification or F1/F2 freeze.

The new module is `experiments/r0_p01_successor_synthetic/trusted_ssh_observation.py`, with 15 explicit real-source/negative/error cases in `tests/unit/test_r0_p01_trusted_ssh_observation.py`.

Initial run: **14 passed, 1 failed**. A real valid foreign signer caused OpenSSH to print `Could not verify signature.` on stdout with empty stderr. This produced ERROR under the first deliberately narrow classifier. We examined the native output and refined the verifier-refusal classification without relying solely on nonzero exit status.

After the correction:

```text
New native + two earlier F1 expected-case modules  146 passed
Historical synthetic executable group A             63 passed
Historical synthetic executable group B             70 passed
Historical synthetic executable group C             46 passed
Structural/source-provenance group                   84 passed
=============================================================
Focused executable cases                             325 passed
Focused total (including structural)                 409 passed
Public repository integrity                          PASS (worktree)
```

The 84 structural/provenance guards passed in 15.35 seconds after routing reconciliation. The aggregate `python -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume` returned `PUBLIC_REPOSITORY_INTEGRITY=PASS` on the changed working tree, including family contracts, Project Knowledge validation, checkpoint metadata, Knowledge Map, model collaboration and current routing. A second aggregate check on the exact published commit will be required for a postpublication claim. This focused set is NOT a complete integrated V3 pass.

The observed positive uses real OpenSSH, but synthetic ephemeral keys only. The output observation is in-process evidence with digests, not a cryptographically signed/attested producer receipt. No owner proof, WebAuthn hardware, actual R0-P01 event, real Attempt 002 or production authority is involved.

```text
VALIDATION_239=BOUNDED_NATIVE_SSH_OBSERVATION_PASS
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
