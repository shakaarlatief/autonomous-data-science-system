# Research 551: native OpenSSH source-derived verification observation

**Date:** 2026-10-12
**Status:** BOUNDED_NATIVE_SSH_VERIFICATION_OBSERVATION_PASS / F1_UNFROZEN
**Scope:** One execution-facing synthetic R0-P01 SSH cryptographic-verification observation boundary, distinguishing real positive proof, rejected proof, untrusted signer, malformed input and verifier malfunction without owner credential use.
**Parent:** Research 540 / 544-550, Checkpoint 886, accepted B01/B02 and owner-approved accident replacement.
**Authority:** Non-owner test-only F1 qualification evidence. This is not real owner event authentication, terminal-event attestation, a frozen whole scorer, an implementation-architecture selection or execution authorization.

## Why this increment matters

Research 550 established typed synthetic receipt completeness, but its caller supplies each `verification_result`. A data-shaped field such as `"VALID"` cannot certify that the SSH verifier actually ran. The subsequent implementation therefore must begin at a real evidence-producing mechanism rather than adding another speculative scoring rule over asserted values.

The newly added `experiments/r0_p01_successor_synthetic/trusted_ssh_observation.py` derives an in-process observation by running **actual local OpenSSH `ssh-keygen -Y verify`** over the separately provided expected run-bound statement, separately trusted public signer and submitted signature. It does not accept a claimant's verdict string. The recorded exact expected-message and proof SHA-256 digests, trusted signer public ID and CLI exit status allow later source-material reconciliation.

The code deliberately keeps the trusted-run/credential inputs distinct from submitted proof fields. A mismatched presented statement or signer is rejected before native verification. An actual `ssh-keygen` success must have both exit code zero and the narrowly expected positive stdout shape. Nonzero results are not automatically classified INVALID: recognized English Windows OpenSSH messages are separated into signature rejection, untrusted-public-signer refusal, and malformed proof, while unknown process failures or unexpected success output become ERROR. A missing executable, launch error, timeout or unusable permitted scratch directory also remains ERROR.

One initial test failure was informative: foreign-key proof against the separately enrolled signer produced nonzero exit, empty stderr and `Could not verify signature.` on stdout, unlike wrong-message signatures which produced `Signature verification failed: incorrect signature` on stderr. The implementation was corrected before final qualification to preserve the distinction between refusal by the allowed-signers boundary and a demonstrated cryptographic signature mismatch. This negative remained visible rather than being reported as an initial all-green result.

## Test evidence

`tests/unit/test_r0_p01_trusted_ssh_observation.py` has **15 executable non-owner cases**. It exercises real valid Ed25519 SSHSIG from the ephemeral Node test signer, changed claims, an unauthorized valid foreign signer, wrong-message cryptographic rejection, malformed proof, verifier binary failure, timeout, unrecognized nonzero exit, spoofed zero exit without actual positive output, missing scratch capacity and separation from the four-event receipt state. No real owner keys, signer prompt, hardware WebAuthn ceremony or actual R0-P01 owner attempt were used.

The first test pass was **14/15**, with the previously described foreign-signer source-message mismatch. After a bounded classifier correction, the new plus previous F1 expectation modules passed **146/146**. Prior execution-facing security and measurement modules passed unchanged in three groups: **63 + 70 + 46 = 179**. The previous **84/84 structural checks PASS** and the aggregate public repository integrity returned **PASS** on the changed working tree. The total is **409 focused PASS** (325 executable and 84 structural). The exact published-HEAD postflight remains a separate claim; see Validation 239.

## Qualified and unqualified boundaries

Supported, bounded:

- Real Windows OpenSSH was invoked with public trust input and exact candidate signed bytes.
- Distinct verified positive, rejected input/signer, malformed proof and operational error outcomes were observed.
- Unknown process behavior was not converted into a claimant's INVALID signature outcome.
- The existing raw-event F1 reference remains separate from the new verification observation.

**Not yet supported**:

- Authenticity of a serialized receipt's producer or externally verified host/process attestation. A Python dataclass and output label can still be copied or fabricated by a later caller.
- Owner presence or exclusive real owner credential use. The tests use ephemeral synthetic signer keys.
- End-to-end trusted P0/S01/S02/S03 terminal event production, lifecycle timing or completion.
- Browser/RP WebAuthn issuance/invocation/consumption authentication.
- Independently demonstrated platform incapability and NOT_REALIZABLE classification.
- Every source-site flag, all security controls under the real successor, independent frozen F1 scorer/oracle or F2 Windows/owner ceremony qualification.
- A provider-independent OpenSSH error taxonomy. Output parsing is bounded to observed English Windows OpenSSH and deliberately fails closed for unrecognized tool behavior.
- Any fixed final storage, execution-provider, operating system, Python module or repository architecture.

## Next meaningful work

Bind produced observations to durable independently re-verifiable source artifacts and trusted issuance, plus authenticated P0/S01/S02/S03 event lifecycles. Prioritize RP/browser and true capability attribution only where required for safe F1 completion. Integrate source-qualified states with independent full B01 scoring and the remaining F1/F2 obligations; use proportionate independent review when it materially tests a risk. Do not treat this bounded SSH result as an excuse to award COMPLETED, REALIZABLE/NOT_REALIZABLE, F1/F2 freeze or authorization for actual Attempt 002.

```text
RESEARCH_551=NATIVE_OPENSSH_VERIFICATION_OBSERVATION_PASS_BOUNDED
NEW_TESTS=15
NATIVE_OPENSSH=EXECUTED_NON_OWNER
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
