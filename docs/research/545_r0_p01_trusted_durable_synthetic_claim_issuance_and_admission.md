# Research 545: trusted durable synthetic claim issuance and end-to-end run-bound admission

**Date:** 2026-10-11
**Status:** EXECUTABLE_SYNTHETIC_ISSUANCE_ADMISSION_PASS / FULL_SUCCESSOR_AND_OWNER_CEREMONY_UNQUALIFIED
**Scope:** Test durable generation, trusted reconstruction, supersession and single-use admission of cryptographically signed R0-P01 claims for synthetic Ed25519 and ES256 credentials.
**Parent:** Research 544 / Validation 232 / Checkpoint 880; Research 543 durable single-run journal; owner-approved simplified accident-replacement procedure at Checkpoint 876.
**Authority:** Public non-owner engineering and synthetic integration only. No real owner credential use, owner execution authorization, B01/B02 replacement, F1/F2 freeze or physical architecture selection.

## Security question and implementation

Research 543 reproduced an old V02 cross-run proof replay because the run label was external to the signed message. Research 544 introduced explicit signed `protocol` and random 256-bit `claim_nonce` fields and showed both Ed25519 and synthetic WebAuthn-shaped ES256 reject an old-run proof against a different *independently trusted expected signed statement*. That isolated the cryptographic boundary but had **no durable trusted issuer** supplying the expected statement.

This checkpoint introduces `experiments/r0_p01_successor_synthetic/trusted_claim_store.py`. Its **replaceable prototype** uses SQLite transactions to keep trusted genesis, issuance sequence, unique random run nonce, exact canonical expected signed statement, claim lifecycle and accepted proof in one durable database. The genesis binds an explicit synthetic issuer ID, a historical nine-field comparison template, the trusted enrolled *public* credential, and the new protocol identity. All accepted records are checked again using actual OpenSSH Ed25519 or Node ES256 signature verification after restart.

- The caller must explicitly create a new issuer store (`create=True`); ordinary reopening refuses a missing or empty database rather than resetting consumed state.
- Issuance uses `BEGIN IMMEDIATE`, a fresh cryptographically generated 256-bit nonce, a unique database constraint and one atomic commit. It constructs the expected statement from trusted genesis and the nonce. A new issuance supersedes an unfinished older claim; a previously admitted claim remains admitted.
- An admission is tied to the **controller-selected claim nonce**, not a nonce from a submitted proof. It compares the complete submitted statement against the independent expected statement and the exact enrolled public credential, then performs real cryptographic verification. It commits accepted proof bytes, their integrity digest and the status transition atomically. Replay and other denials make no state change.
- After restart, the store checks exact genesis, contiguous issuance history, no duplicate nonces, at most one active outstanding claim, trusted expected statement reconstructed from genesis plus nonce, and every stored accepted proof's cryptographic validity. An attacker changing a persisted statement and recomputing its ordinary SHA-256 cannot change the expected run identity.

This is **one acceptance per issued claim**, not the full event lifecycle, multi-role trust rotation, owner instructions or scorer.

## Executable behavior established

`tests/unit/test_r0_p01_trusted_claim_store.py` adds **26 parametrized synthetic integration tests** across the SSH Ed25519 and WebAuthn-shaped ES256 paths. They prove:

1. Fresh issuance followed by genuine signature and one successful admission; acceptance remains durable after reopening and a separate Python child process verifies the same outcome.
2. An unfinished earlier claim is superseded by new issuance, so the earlier valid signature is denied even when an attacker explicitly selects the old nonce. Altering its presented nonce also fails cryptographically against the new claim.
3. A valid signature from another enrolled *test* key is denied unless the exact trusted public signer matches; changing the governing digest, decision or run nonce without a new signature cannot change durable state.
4. An actual child process exiting just before issuance commit rolls back issuance; an exit just after issuance commit leaves the exact issued claim recoverable. Likewise, admission crashes before commit retain an unconsumed claim, while after-commit/before-acknowledgment crashes leave it consumed.
5. Two concurrently issuing processes yield two distinct saved identities, but only the newer claim stays active. Two concurrently admitting processes yield exactly **one** admission for a shared claim.
6. Modifying the saved trusted expected statement and recomputing its unkeyed hash fails against independent genesis reconstruction. Altering a committed proof's signed claim identity and recomputing its hash fails on restart. Wrong genesis, deleted database and nonce collision fail closed.
7. A caller cannot authorize a self-declared nonce that was never durably issued.

Observed tests: **26/26 passed**. The previously tested executable security suites also pass: **89/89 runnable cryptography, admission, restart and issuance tests**, and **84/84 structural source/audit/guard tests**, for **173 focused passing tests**, run as two bounded groups.

## Security claims deliberately NOT made

This only demonstrates the test-store durability and authoritativeness of **synthetic** public trust genesis in the tested Windows process environment. The real controller's human-governed authority to issue a claim and cryptographically trustworthy source of initial enrolled public signer identity have **not** been implemented. The full successor must protect against unauthorized claim creation and distinguish owner-sanctioned new research execution from an arbitrary synthetic `issue()` call. Local SQLite and its ordinary SHA-256 checks are not an external anti-rollback anchor: an attacker able to restore an entire earlier database can evade this prototype's detection. Sudden power loss, malicious filesystem substitution and distributed host trust remain unqualified.

The synthetic ES256 path is **not** hardware-backed Windows Hello. Reusing the V02 nine-field template is an interoperability test only; it does not freeze the successor statement/evidence format. This prototype does not implement a full repeatable experiment protocol, multi-event admission, recovery roles, full end-to-end P0/S/T trials, real owner friction metrics, independent scorer/oracle, F1/F2 approval or human test consent.

## Proportionate next work

The following real objective is **trusted owner-facing initiation and measurement/evidence integration**, not more speculative B02 exception scoring. First test bounded synthetic claim issuance authorization and the separation between the owner's procedural permission to repeat research and cryptographic proof of a governing decision. Then connect the claim-bound acceptance prototype to actual successor nonsecret event/evidence and independent scoring checks at the appropriate level. Any true hardware or owner-key test remains separately authorized and only follows relevant qualification.

The 55 historical pending source-unit findings remain available to triage by genuine security/scientific relevance. Retain this prototype only if it continues to be useful; no existing repository folder, tooling, storage design or review procedure is an immutable architecture constraint.

```text
RESEARCH_545=TRUSTED_SYNTHETIC_CLAIM_ISSUANCE_ADMISSION_PASS
NEW_EXECUTABLE_TESTS=26
EXECUTABLE_TOTAL=89
STRUCTURAL_TOTAL=84
FOCUSED_TOTAL=173
SYNTHETIC_TRUST_ONLY=TRUE
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
