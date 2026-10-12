# Research 553: independent verification-only SSHSIG Ed25519 scorer component candidate

**Date:** 2026-10-12
**Status:** BOUNDED_INDEPENDENT_SSH_SIGNATURE_VERIFICATION_PASS / F1_UNFROZEN
**Parent:** Research 530, 532, 540, 549–552; Checkpoint 888; MC-0030
**Scope:** An independent public-key verification path for the SSH arm that does not reuse the actual owner harness's OpenSSH verification command or import the synthetic signing worker.
**Authority:** Synthetic-only F1 implementation/qualification evidence. No F1/F2 freeze, complete scorer, owner credential use, Attempt 002 authorization, new R0 physical target, or migration.

## Why this work was selected

The owner explicitly requested that readiness work remain proportionate to enabling a valid Attempt 002. The F1/F2 independence amendment (`R0_P01_Q1_F1_F2_INDEPENDENCE_ADDITION_UNFROZEN.md`) requires the future scorer to parse SSHSIG, reconstruct the cryptographic message and independently verify Ed25519 rather than trusting the owner harness's reported VERIFY/ADMIT outcome or directly invoking its `ssh-keygen -Y verify` path.

Research 551 and 552 made the native OpenSSH path source-facing and then checked admitted proof records against the local source as presented. They did **not** establish an independently implemented scorer verifier. Creating another mutable journal wrapper would not close this explicit scorer requirement. Python `cryptography` was not installed in the current workspace; introducing a dependency or building new Ed25519 mathematics would increase test/runtime complexity without clear merit at this stage.

## Implemented boundary

New `experiments/r0_p01_successor_synthetic/independent_sshsig_verify.mjs` is a standalone Node ESM, **public verification-only** CLI with a single `--verify-only` command. It does not import the owner harness, native OpenSSH verifier or the existing Node signing worker. The caller provides a separately expected complete run-bound statement and enrolled public SSH key/ID; the verifier never selects them from an untrusted signature. Its parser independently:

- validates the exact successor statement field set, signed protocol/nonce/decision and digest syntax, using a separate sorted-JSON serializer;
- parses canonical SSH public key bytes, Ed25519 key encoding and SHA-256 public identity;
- validates SSHSIG ASCII armor, base64, version, framed public key, exact namespace, empty reserved bytes, `sha512` hash algorithm and framed Ed25519 signature;
- reconstructs `SSHSIG || string(namespace) || string(reserved) || string(hash) || string(SHA512(canonical statement))`;
- calls `node:crypto.verify(null, ...) ` with a reconstructed SPKI Ed25519 public key;
- produces VALID only after genuine public-key verification; malformed/wrong message/signature produces INVALID, and unanticipated operational faults produce ERROR.

The Node process is separate from the owner harness and uses built-in cryptography. It does not require a new third-party dependency. The verifier is **in-process in the Node verifier**, not an in-process Python extension. This module is a candidate scoring primitive, **not** the actual integrated F1 scorer or an assertion that the execution environment is immutable or attested. Node's cryptography backend is an implementation dependency that will need version/source qualification in F2.

## Test evidence and independence limits

New `tests/unit/test_r0_p01_independent_sshsig_verifier.py` contains **31 executable tests**. It uses a separately existing ephemeral synthetic Ed25519 signing worker and compares positive/wrong-message/wrong-signature verdicts against actual Windows OpenSSH. It also checks signer substitution, public-ID mismatch, namespace, reserved data, algorithm, hash field, strict string lengths, trailing bytes, malformed armor, protocol and signed grammar.

The first run was **30 passed, one test assertion failure**, because the verifier returned additional diagnostic hashes with a correctly rejected bit-flipped signature. The test assertion was corrected without weakening signature expectations or changing the verifier. The full repeated focused suite subsequently passed **462/462**, comprising 378 executable and 84 structural tests. Detailed grouped receipts are recorded in Validation 241.

**Independence is bounded**: separate parsing, message reconstruction, implementation and verification runtime from OpenSSH; cross-comparison against actual OpenSSH. The author and primary tester are the same ChatGPT session; no separate blind canonical oracle author or independent Claude review was completed. The old Node synthetic signing worker and the new verifier both rely on standard Node cryptographic primitives, so do not misstate this as independent cryptographic-library provenance between those two Node processes. The difference from the **owner harness's OpenSSH** implementation is real.

## Unresolved blockers and next priority

This does **not** qualify an externally authenticated receipt writer, owner signing surface, browser/RP WebAuthn issuance and consumption, true capability classification, four same-attempt P0/S01/S02/S03 event receipts, all original 13 security controls in the successor, the independent scorer's full decision/numeric logic, target Windows F2 qualification or full A/B/C synthetic rehearsal.

Next, integrate independently checked proof and source/event inputs into the smallest end-to-end **non-owner** F1 scoring path with genuine event-source provenance and no self-certified success. Prioritize native RP/browser and capability evidence where needed for the fair SSH-versus-WebAuthn comparison. Reassess sufficiency for the next real owner experiment rather than endlessly extending speculative audit surfaces. Owner approval of a real Attempt 002 remains a separate future decision.

```text
RESEARCH_553=INDEPENDENT_SSHSIG_VERIFIER_COMPONENT_PASS_BOUNDED
NEW_TESTS=31
FOCUSED_TOTAL=462
INTEGRATED_SCORER=NOT_QUALIFIED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
