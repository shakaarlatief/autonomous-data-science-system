# Checkpoint 880: R0-P01 signed fresh claim nonce verified synthetically

**Date:** 2026-10-11
**Checkpoint class:** R0-P01 owner-authenticity architecture probe / executable fresh-run cryptographic binding
**Project stage:** R0 physical-architecture decision probes
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-37
**Conversation title:** 37 - Project System Realization Architecture and Qualification
**Primary collaborator:** ChatGPT
**Status:** FRESH_RUN_SIGNED_CRYPTO_BINDING_SYNTHETIC_PASS / DURABLE_TRUSTED_NONCE_ISSUANCE_NEXT
**Research:** Research 544
**Validation:** Validation 232
**Scope:** Implement distinct synthetic successor statement with cryptographically signed claim nonce and test cross-run SSHSIG/ES256 proof non-reuse using exact independently expected statements.
**Authority:** Public non-owner synthetic cryptography only. No historical B01/B02 policy edits, owner credential use, F1/F2 approval, physical architecture selection or real Attempt 002.

Checkpoint 879 experimentally demonstrated that the original V02 signature can be replayed into a separate new-run SQLite database because the external run label is **not signed**. This checkpoint introduces a separate experimental signed-statement protocol with explicit domain separation and a new 256-bit `claim_nonce`. The run's independent expected signed statement is the verification authority; it is not reconstructed from the presented untrusted proof. Historical V02 code and source evidence remain unchanged.

Node generates ephemeral non-owner Ed25519 SSHSIG and WebAuthn-shaped ES256 signature proofs. Actual Windows OpenSSH signature verification and Node P-256 cryptographic verification both accept correct run signatures, reject old-run signatures despite an identical acceptance ID and signer, and reject a modified claim nonce without a new signature. **21/21 new executable tests pass**. Together with 42 earlier executable security tests and 84 prior structural provenance tests, **147 focused tests pass**, verified in two groups after an all-in-one bridge timeout.

This **closes the demonstrated cross-run gap at the signature-verification layer**, not at complete admission level. No durable authoritative nonce issuance, recovery of trusted run context, exactly-once cross-run journal operation, full successor scorer, host-specific true WebAuthn hardware qualification, or adversarial ledger rollback protection has been established. Next task is a bounded end-to-end synthetic claim issuer and integrated durable admission path with trusted expected nonce, repeated old-run replay denial, correct same-run single consumption, and process-restart recovery.

The new protocol is an experimental candidate, not a frozen physical ADS architecture. Owner-approved simple replacement of declared accidental/technical interrupted runs remains in force and still requires separate fresh owner execution consent. Permanent Attempt 001 AMEND, historic B01/B02 hashes, 55 unresolved inherited audit notes and F1/F2 boundary remain untouched. R0-P02 PASS, R0-P03 pending, Specification 028 unchanged.

```text
CHECKPOINT_880=SYNTHETIC_SIGNED_RUN_NONCE_BINDING_PASS
NEXT_ACTOR=chatgpt
NEXT_BOUNDARY=p-one-trusted-durable-claim-issuance
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
