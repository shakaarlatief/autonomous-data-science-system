# Research 541: R0-P01 execution-facing synthetic security testing and proportionate next build

**Date:** 2026-10-11
**Status:** FIRST ACTUAL SYNTHETIC CRYPTO REGRESSION PASS / SUCCESSOR F1 F2 UNFROZEN
**Scope:** Move from procedural audit/review repetition into real non-owner cryptographic tests and an implementation-facing safety checklist for R0-P01 successor preparation.
**Parent:** Research 540 / Checkpoint 876 / the 2026-10-11 owner-approved replacement decision / inherited original V02 harness.
**Authority:** Public engineering/test evidence using synthetic in-memory keys only; historical Attempt 001 and owner approval unchanged.

## Why this is the next task

The owner approved an explicit prospective replacement procedure for declared accidental or technical interruptions, superseding the historical B02 cap/exception requirements for that limited purpose. Therefore we do **not** need increasingly detailed Ctrl+C/Node timing or scored-subtype rules **merely to establish whether a separate owner-authorized run is permitted**. We do need truthful records of interruptions and genuine cryptographic acceptance and security checks. Those are part of the original architectural research objective, not procedural bureaucracy.

The former 18-batch source review is complete but 55 reviewer source findings remain task-owner unresolved. They constitute a **triage input**, not 55 automatic review rounds. Claude Message 059 remains independent technical background, not an instruction to produce Message 061. This project remains open to changing any implementation, test, workflow, storage, CI/CD, architecture or technology boundary when justified; the historical three-file V02 owner probe is **not** a target constraint.

## First implementation-facing exercise completed

`tests/unit/test_r0_p01_cryptographic_sensitivity.py` implements **eight actual non-owner executable checks** against the original V02 verifier, including:

1. A valid synthetic Ed25519 SSHSIG signed in an isolated Node child process must verify through the installed Windows OpenSSH `ssh-keygen -Y verify`.
2. A signature-bit mutation preserving all SSHSIG framing, signer key, namespace, digest algorithm and message must fail. This reaches the real signature-check path rather than merely corrupting the SSHSIG magic.
3. A second synthetic Ed25519 signer must produce a valid proof under its *own* public key, but a framed signature packet spoofing the first trusted public key while retaining the second signer’s signature must fail.
4. Changing the exact signed decision statement without a new signature must fail.
5. An unrelated `semantic_base.source_revision` mutation passed through the actual Python `semantic_base` derivation must leave the digest unchanged; altering the actual governing `effects[0].lineage_head` through that same path must change it. The previous C09 test only inserted unused unrelated metadata, so it was weaker.
6. The historical `mutate_proof` C02-style negative is confirmed to corrupt the SSHSIG magic, and therefore cannot by itself demonstrate cryptographic forgery rejection.
7. A valid Node synthetic WebAuthn ES256/P-256 assertion must verify; a canonical ASN.1 DER-preserving ECDSA signature-scalar mutation must fail.
8. A P-256 assertion cryptographically signed by a different synthetic key but presented with the intended credential ID must fail against the intended SPKI.

These are executable **cryptographic regression checks**, not merely audit-source/metadata validators. Each test requires a working positive control and an actual negative, uses synthetic ephemeral non-owner keys only and never reads owner SSH key material, opens Windows Hello, or creates an official trial marker.

### Environment failure avoided

The initial SSH baseline appeared `False` in a bridge `readOnly` profile because the original verifier needs a temporary directory for *public* allowlist/signature files; the read-only profile does not permit temp file creation. Repeating the identical synthetic positive control with the permitted workspace execution profile yielded `True`. A read-only sandbox false negative is **not** cryptographic evidence. All eight tests were run with the appropriate `inherit` workspace execution profile and passed. This is important when interpreting automated test outcomes and deploying CI.

### Limitations

The tests exercise the **original V02** implementation's cryptographic behavior, not a rewritten or frozen prospective successor. A few negative cases directly harden historically weak C02 and C09 expectations, but **do not mark all 13 controls qualified**. WebAuthn here uses synthetic Node cryptography and is **not** real Windows Hello user-presence or hardware capability evidence. The separate scorer and blind oracle have not been implemented. New F1/F2 freeze is not justified.

## Proportionate critical path toward owner-authorized Attempt 002

| Priority | Concrete work | Why it matters | Minimal qualification | Status |
|---|---|---|---|---|
| Essential 1 | Trustworthy exact statement signature verification for both arms; forgery and altered message/key negatives | Wrong owner acceptance is an architectural security failure | Independent positive/negative cryptographic regression with well-formed proofs | Historical V02 **eight synthetic tests pass**; successor integration pending |
| Essential 2 | Admission-source replay, stale semantic base, stale signer-set, role/recovery and recovery-denial negatives (including C05/C07) | Signed but unauthorized and replayed decisions could enter trusted state | Real signed synthetic counterexamples and state-unchanged postcondition | NOT YET qualified on successor |
| Essential 3 | WebAuthn error/evidence and viability under supported browser/OS, with no invented completed event | Could falsely declare mechanism unavailable or owner proof complete | Synthetic P0 registration/assertion evidence cases and bounded physical capability qualification when appropriate | NOT YET qualified |
| Essential 4 | Safe process interruption, durable honest evidence and distinct user-requested replacement | Corruption, fabricated positive outcome and misleading usability would invalidate the study | Targeted synthetic interrupted-run cleanup/record preservation and later host-specific qualification for actual execution | Procedural owner approval recorded; technical successor incomplete |
| Essential 5 | Comparable owner-time, friction, recovery burden, volume and classification without silent threshold relaxation | Required to make an architectural mechanism choice | Deterministic synthetic timing/evidence checks, independent qualified scorer and clearly described owner instructions | NOT YET qualified |
| Essential 6 | Credible independent expected answers and version/hash provenance for the actual successor | Avoid scorer and test sharing the same bugs | Targeted independent known-answer vectors for each *material* scored branch, rather than 1,022 new documents | NOT YET qualified |

**Non-critical by itself:** completing another audit of all 55 reviewer notes, hash-pinning every draft sentence, performing further 15-row review cycles, or proving Ctrl+C intent **solely to decide whether owner-authorized replacement is permitted**. Retain those artifacts as reference and reopen a particular item if it corresponds to a real security/science failure or implementation issue.

The next engineering step is to **extend actual synthetic tests of signed-but-unauthorized admission**, reusing baseline positive controls and verifying unchanged ledger state on rejection. After that, implement the successor behind a reasonable and revisable boundary, with synthetic safety/measurement qualification. Do not freeze a technology, folder structure or test framework by habit. Do not ask the owner to execute keys or start the official next attempt until the actual safety checks pass and separate fresh execution consent is obtained.

```text
RESEARCH_541=IMPLEMENTATION_FIRST_SECURITY_SMOKE
CRYPTOGRAPHIC_SYNTHETIC_NEGATIVES=EXECUTED
PROCEDURAL_RETRY_POLICY=OWNER_APPROVED_SIMPLIFICATION
HISTORICAL_B01_B02=UNCHANGED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
