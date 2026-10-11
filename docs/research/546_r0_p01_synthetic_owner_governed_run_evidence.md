# Research 546: R0-P01 synthetic owner-governed initiation and preserved interruption evidence

**Date:** 2026-10-11
**Status:** SYNTHETIC_GOVERNED_ISSUANCE_AND_OBSERVATION_TESTS_PASS / REAL_OWNER_EXECUTION_UNAUTHORIZED
**Scope:** Demonstrate a minimal, durable connection between run-specific procedural permission, cryptographically bound claims, and nonsecret experimental observations, without inventing further cryptographic owner-consent bureaucracy.
**Parent:** Research 545, Validation 233, Checkpoint 881, and the owner-approved simplified accident-replacement procedure from Checkpoint 876.
**Authority:** Synthetic engineering evidence only. No inference of live owner approval, hardware authentication, full R0-P01 outcome, or production design freeze.

## Goal and separation of authorities

The human owner approved a simple research-governance principle: when an accident or technical interruption occurs, the owner can describe it in ordinary language and **separately authorize** a fresh research execution. The interrupted run remains in the record; an owner explanation does not retroactively produce a valid governing signature. Research 545 already tested durable nonce issuance and cryptographic single-use acceptance but had no link to procedural permission or incident observations.

This stage **extends the existing** `experiments/r0_p01_successor_synthetic/trusted_claim_store.py`, rather than building another competing persistence system. A new **synthetic governed mode** is explicitly bound into the issuer genesis and cannot be disabled on reopen. In this mode:

1. The ungoverned `issue()` entry point refuses to issue. The `issue_governed()` operation requires a syntactically valid, affirmative synthetic-controller decision with a unique reference, purpose, and optional earlier claim nonce for a replacement. A replacement must reference an existing recorded claim.
2. The exact approval record and the cryptographically issued run identity are committed in **one SQLite transaction**. An authorization reference cannot be consumed for two claims.
3. A small append-only-at-the-API-level observations table stores the run nonce, `INTERRUPTED` / `ERROR` / `COMPLETED` observation type, supplied elapsed milliseconds, interaction count, and a short nonsecret synthetic note. Observations persist across restarts and remain attached to interrupted or superseded claims.
4. Observations **never** alter `ISSUED`, `SUPERSEDED`, or `ADMITTED` cryptographic claim status. A note describing accidental Ctrl+C does not make an unsigned/failed governing acceptance valid.
5. Reopening the journal validates contiguous observation sequence, synthetic authorization structure, acceptance associations and ordinary record hashes. Missing authorizations in governed mode or inconsistent observed evidence fail closed.
6. Existing ungoverned synthetic prototype behavior remains available under its different genesis setting for regression compatibility. The store's test schema was bumped to version 2 to distinguish this expanded format.

The stored approval is **not authenticated evidence of a real human**. The literal `source=SYNTHETIC_TRUSTED_CONTROLLER` is a test assertion supplied by a caller. A real run needs the actual explicit owner authorization captured through the trusted owner interaction and associated with its execution identity. The real approval must not be fabricated by writing JSON or inferred from a previous generic `Proceed` authorizing engineering work. Nor does the consent record replace SSHSIG or WebAuthn cryptographic owner acceptance.

## Executed checks

New module: `tests/unit/test_r0_p01_governed_run_evidence.py`. **44 test cases** across synthetic Ed25519 OpenSSH and ES256 Node verification establish:

- Invalid, missing, non-boolean and malformed approvals refuse issuance without mutation; the older ungoverned API is inaccessible in governed mode and cannot be restored by reopening under changed genesis.
- Unique approval evidence is linked to the issued claim and durable over reopen. Duplicate approval references and unknown replacement targets fail.
- A synthetic accident recorded as `INTERRUPTED` with elapsed time and interactions remains visible after issuing an **independently authorized** replacement. Old valid signed proof cannot be admitted to either the superseded run or the replacement. A fresh valid signature admits the replacement once.
- Recorded `ERROR` and `COMPLETED` observations do not automatically admit a signature or change trial outcome. A changed signed decision is still rejected.
- Invalid/negative measurements, malformed fields and obvious sensitive-keyword notes fail without mutation. Observation history is preserved across a genuine new Python process. Corruption of approval/observation bytes without valid recorded hashes fails closed.

**Combined passing regressions:** 133 genuine executable synthetic security/measurement/issuance tests and 84 earlier structural provenance/guard tests, **217 focused PASS** in two bounded groups. The 84 prior guards are not misrepresented as cryptographic verification.

## Important limitations and proportionate next work

This does **not** prove that text supplied by an arbitrary process originated from the human owner. It is not a live owner-identity API or a production consent mechanism. The simple human owner instruction should be captured as ordinary human governance evidence with a run-specific reference, not used to excuse a missing signature. The notes/measurement input is caller-supplied synthetic data; the simple keyword screen is **not reliable secret detection or redaction** and actual owner-secret material must never be submitted to it. Actual owner timing and interaction measurement require instrumentation. SQLite hashes are not cryptographic proof against whole-file replacement or a compromised controller.

The relevant next engineering step is a **bounded synthetic rehearsal of the real run's evidence/measurement path and independent outcome logic**, including interrupted trials, without starting a real owner ceremony or relaunching the old B02 exceptional-retry review cycle. Separately confirm real owner authorization immediately before any real Attempt 002, after appropriate evidence/safety qualification. The future storage, file layout, testing and operational architecture remain open to redesign.

```text
RESEARCH_546=SYNTHETIC_GOVERNED_PERMISSION_AND_OBSERVATIONS_PASS
NEW_EXECUTABLE_TESTS=44
EXECUTABLE_TESTS=133
STRUCTURAL_TESTS=84
FOCUSED_TOTAL=217
REAL_OWNER_AUTHENTICITY=NOT_ESTABLISHED_BY_SYNTHETIC_APPROVAL_RECORD
OWNER_CREDENTIALS=UNUSED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
