# Research 542: R0-P01 signed-but-unauthorized admission security regression

**Date:** 2026-10-11
**Status:** ACTUAL_SYNTHETIC_ADMISSION_SECURITY_TESTS_PASS / SUCCESSOR_UNFROZEN
**Scope:** Verify that cryptographically valid but unauthorized, replayed, stale or mislabeled SSH/WebAuthn decisions cannot mutate the historical R0-P01 trust ledger.
**Parent:** Research 540 and 541; Validation 229; Checkpoint 877; owner-approved simplified accidental/technical interruption replacement procedure.
**Authority:** Non-owner synthetic testing and public technical analysis only. No owner SSH material, Windows Hello ceremony, production acceptance, or real R0-P01 attempt.

## Why this is necessary

A valid signature proves that a credential signed a particular message. It does **not** by itself establish that the credential is currently authorized for a particular governing role, that the statement describes the current semantic base, or that its acceptance ID has not already been consumed. These are essential owner-authenticity properties, independent of the former B02 exceptional-retry cap.

The historical V02 `Ledger.admit` implementation separates cryptographic proof verification from expected signed statement reconstruction, replay detection, and current signer-role membership. Research 541 introduced eight real synthetic cryptographic positive/negative tests against the original SSH Ed25519 and WebAuthn ES256 verifier. Research 542 extends executable assurance from signature validity to **authorized state mutation**.

## New executable integration tests

`tests/unit/test_r0_p01_signed_unauthorized_admission.py` adds **19 tests** using new in-memory synthetic keys created inside the existing Node child process, verified by actual Windows OpenSSH `ssh-keygen -Y verify` or the Node ES256 verifier. The test runner holds only public credentials and proof bytes. All negative cases that concern valid but unauthorized signatures first independently confirm the signature is **VALID**.

For both Arm A (SSH Ed25519 primary) and Arm B (WebAuthn ES256 primary), tests verify:
- A valid P0 owner-record signature admits once, consumes exactly one acceptance ID, and a second identical signed acceptance is rejected as `CONSUMED_ACCEPTANCE_ID` with no further mutation.
- The recovery key can produce a valid signature but cannot authorize an ordinary S01 event as `PRIMARY`.
- A different, genuinely valid, unregistered cryptographic signer cannot enter the trust ledger.
- A correctly signed statement becomes inadmissible when its **actual governed dependency lineage** changes after signing. The preserved original proof still verifies, but the latest semantic-base digest no longer matches.
- A changed recorded owner view or changed event identity cannot enter the ledger even while the original signed statement/proof remains cryptographically valid.
- An explicitly signed AMEND or REJECT consumes once but must **not** apply ACCEPT effects, rotate signers or change trust authority.

Additional transition tests:
- After a genuine primary-signed `P5` rotation in Arm A, the prior correctly signed `S01` statement fails because its signer-set semantic base is stale. Even a **fresh** signature from the former primary is denied the new PRIMARY role. A newly authorized signer must successfully admit the intended `S01` positive control.
- In each arm, the recovery credential's valid S01 signature is denied, whereas its separately signed explicit `P6` recovery transition is accepted and the historical prior approval remains verifiable.

### Rejected-state invariant

Tests snapshot the entire authority-relevant mutable ledger surface immediately before each rejected operation: recorded entries, consumed acceptance IDs, applied effects, signer members, signer-set version, governed dependencies, and target signer credentials. A rejection must preserve each field exactly. Only confirming a rejection reason is insufficient if that denial silently consumed an ID or modified authorized state.

## Evidence and scope boundaries

All **19 new tests passed**. Together with the eight previous cryptographic-sensitivity tests and 84 previous focused provenance/contract regressions, the combined run is **111/111 PASS**. The 27 executable synthetic tests now provide direct cryptographic and admission-behavior evidence, while the older 84 cover specification provenance and guards. These totals are deliberately distinguished.

This runs against the **historical V02** `harness.py`, `webauthn_server.mjs`, frozen fixture and real local cryptographic verification. The historical files have not changed; no official R0-P01 result was created. This is not a certification of the future successor, not an F1/F2 freeze, and not complete coverage of all 13 security controls. The tests currently exercise accepted/denied admission in memory; separate durable/restart replay protection, end-to-end successor execution semantics, Windows interruption/evidence retention, real WebAuthn platform usability and independently written scored outcome vectors remain to be qualified.

## Next proportionate engineering target

Do not resume the earlier automatic D01–D15 speculative reviewer loop. Next, determine a justified and reversible successor implementation boundary, using the demonstrated cryptographic/admission behavior as known-good tests. The immediate technical risk to investigate is **durable consumed-ID and signer/trust history preservation across process restart**: in-memory single-use rules are insufficient if replay state can be lost when a process is restarted. This should be tested synthetically, with public data and no owner keys, before any real owner run. Implement only the durability/provenance controls truly needed for R0-P01's objective. The owner-approved simple replacement procedure remains separate and is not a bypass for signed acceptance reuse inside a particular trial.

```text
RESEARCH_542=EXECUTABLE_SYNTHETIC_ADMISSION_REGRESSION_PASS
NEW_ADMISSION_TESTS=19
FOCUSED_TOTAL_TESTS=111
HISTORICAL_V02_ONLY=TRUE
OWNER_CRYPTO_MATERIAL=NOT_USED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
