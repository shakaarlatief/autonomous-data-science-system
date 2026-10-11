# Research 544: R0-P01 signed claim nonce and cross-run synthetic replay resistance

**Date:** 2026-10-11
**Status:** RUN_BOUND_SIGNATURE_NEGATIVES_PASS / DURABLE_NONCE_ISSUANCE_AND_FULL_ADMISSION_PENDING
**Scope:** Resolve the actual historical cross-run signature-replay weakness using a fresh, explicit signed claim identity for both synthetic SSH Ed25519 and WebAuthn-shaped ES256.
**Parent:** Research 543 / Validation 231 / Checkpoint 879; owner-approved simple procedural replacement at Checkpoint 876.
**Authority:** Non-owner synthetic cryptographic verification only, not a new owner run, approved F1/F2 specification, or production identity design.

## 1. Observed predecessor failure and design choice

The historical V02 R0-P01 signature is bound to a nine-field signed statement but does **not** include a new experiment's claim nonce. Research 543 demonstrated that a previously accepted signed P0 record can be admitted into a newly initialized independent SQLite journal when the external journal run label changes. The database path or its unsiged `run_id` cannot cryptographically distinguish that record. Because the owner now may authorize clean replacement research runs after declared accidents, each new run must still have distinct *signed* identity; simplified human retry governance is not authority to replay a governing signature.

Rather than silently changing historical V02 files or placing the run ID in an unrelated legacy field, this experiment introduces a separate, explicit test-only successor signed statement with **two additional mandatory fields**:

- `protocol = ADS-R0-P01-RUN-BOUND-STATEMENT-V01`, explicitly separating new and historical authority domains.
- `claim_nonce`, a 32-byte cryptographically random lower-case hexadecimal value, carried inside the exact signed canonical JSON bytes.

The nine prior statement fields are retained only for direct **synthetic comparison**. The authorized verifier must obtain the *expected entire statement*, including the nonce and semantic/effect digests, from a **trusted run controller**, not infer which run is intended from a proof submitted by an actor. Nonce generation alone is not issuance governance.

## 2. Working executable test implementation

Two new, independent, public-only source files were added:

`experiments/r0_p01_successor_synthetic/run_bound_acceptance.py`: strict required-key set, protocol, digest and nonce validation; fresh `secrets.token_hex(32)` generation; new signed-statement preparation without mutating the historical V02 template; and a verifier that refuses any difference between the presented and trusted-expected statements. A successful result also requires the actual cryptographic proof. The SSH path uses installed **Windows OpenSSH `ssh-keygen -Y verify`** with new namespace `ads-r0-p01-claimed-run-v1`, an exact public credential allowlist and the canonical expected bytes. The ES256 path uses independently verified Node built-in P-256 cryptographic verification of a WebAuthn-shaped assertion challenge bound to the SHA-256 digest of those bytes.

`experiments/r0_p01_successor_synthetic/run_bound_crypto.mjs`: an explicitly synthetic RPC-only Node worker. It generates fresh ephemeral Ed25519 and P-256 signing KeyObjects, retains all private keys in process memory and publishes only synthetic public credentials and proofs. The Ed25519 test proof is a complete framed SSHSIG in the **separate claim-bound namespace**. The P-256 test proof uses an ES256 signature of WebAuthn-shaped authenticator data plus a clientDataJSON challenge that hashes the new signed statement. The verifier independently checks RP hash, UP/UV-shaped flags, origin, client type, exact challenge, canonical base64url and real ES256 signature. This is **not** a Windows Hello credential ceremony or proof of hardware authenticator presence.

`tests/unit/test_r0_p01_run_bound_acceptance.py`: **21 executable cases** exercise both signature mechanisms. They require valid run-1 and run-2 positive controls under the **same signer and acceptance ID**, reject a valid run-1 proof under a distinct trusted run-2 expectation, reject a rewritten claim nonce with unchanged signature bytes even when all other fields match, reject altered signed decision or governing digests, fail closed on wrong/removed/extra protocol/nonce fields, reject wrong credential attribution, and verify the separate protocol cannot be reinterpreted by the unchanged V02 verifier. A 32-nonce sample and invalid nonce inputs check the test generator/format. Negative signer labels must be explicitly `SYNTHETIC-NON-OWNER-`.

**Observed result: 21/21 passed**, with the actual installed OpenSSH verifier and Node cryptographic verifier. The SHA-256 WebAuthn challenge and Ed25519 SSHSIG signed message actually differ when the new run nonce differs. This is an executable security regression rather than a hash-only document guard.

## 3. Security claim and limits

**Verified:** An old run's genuine Ed25519 or synthetic WebAuthn-style ES256 signature is not valid for a different trusted, freshly bound claim identity. Same-run valid signatures remain cryptographically valid; **single-use acceptance** is a distinct journal/admission responsibility, already exercised separately in the Research 543 prototype.

**Not yet qualified:** Claim issuance is not durably persisted with uniqueness/idempotency; the run nonce is not yet integrated with the complete successor's admission journal, recovery role, evidence seal, human sign-what-you-see view and owner-facing test workflow. An attacker controlling the *trusted* run controller/expected statement may misdirect verification; that trust boundary must be implemented, not guessed from the submitted proof. The synthetic ES256 proof is not a real Windows Hello ceremony or RP server test. There is no independent oracle for all successor F1/F2 scored classes. No protection against malicious complete-database rollback is claimed.

The next proportionate implementation step is **durable trusted claim issuance and expectation binding plus a small end-to-end admission test**: a never-before-issued 256-bit claim nonce is recorded by an authoritative local run controller; the exact expected signed statement and run context are independently recovered; an old, correctly signed acceptance from another claim is denied with no state mutation; a proper new-run acceptance succeeds and is consumed once, even after restart. Do not recreate extensive speculative owner-retry policy analyses to qualify this technical feature.

```text
RESEARCH_544=FRESH_RUN_NONCE_IN_SIGNED_BYTES_VERIFIED
RUN_BOUND_SYNTHETIC_CRYPTO_TESTS=21_PASS
HISTORICAL_CROSS_RUN_REPLAY=MITIGATED_AT_SIGNATURE_LAYER_ONLY
DURABLE_ISSUANCE_AND_FULL_ADMISSION=OUTSTANDING
OWNER_CREDENTIAL_USE=NONE
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
