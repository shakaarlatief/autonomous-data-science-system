# Checkpoint 879: R0-P01 durable synthetic admission verified; cross-run nonce gap next

**Date:** 2026-10-11
**Checkpoint class:** R0-P01 owner-authenticity research probe / executable synthetic durability qualification
**Project stage:** R0 physical-architecture decision probes
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-37
**Conversation title:** 37 - Project System Realization Architecture and Qualification
**Primary collaborator:** ChatGPT
**Status:** SYNTHETIC_DURABLE_SAME_RUN_REPLAY_PASS / CROSS_RUN_CLAIM_NONCE_NOT_IMPLEMENTED
**Research:** Research 543
**Validation:** Validation 231
**Scope:** Exercise original V02 valid signed admissions against a new isolated, replaceable SQLite public-data journal across hard process exits, restart and concurrent writes.
**Authority:** Synthetic engineering qualification only; no B01/B02 owner-policy change, live owner credential use, frozen F1/F2, real Attempt 002 or physical architecture selection.

Research 543 records the bounded implementation: the historical trust ledger can be reconstructed and cryptographically replayed from an atomic SQLite journal, and a successful acceptance remains consumed after a crash/restart. Tests cover immediate crash before commit, crash after commit but before acknowledgement, concurrent acceptance races, signer-set reconstruction, rejection invariance and missing/corrupted-journal behavior. Fresh DB creation requires explicit initialization rather than silent resetting on reopen.

**15/15 new executable durability tests pass; combined 126/126 focused regressions pass.** The precise breakdown is 42 executable synthetic security tests (15 durable, 19 admission, eight cryptographic) plus 84 source/provenance guards. The tested journal is **NOT an approved successor design** and does not imply hostile rollback resistance.

A real limitation was reproduced deliberately: historical signed statements have no per-run identity nonce, so a signature can be replayed successfully into an otherwise independent new-run database despite a different external run label. A new owner-approved research attempt must bind fresh run identity **inside the signed message**. Implement the corresponding successor-level signed context and a genuinely negative cross-run replay test as the next practical engineering step. Never treat new owner-governance permission to retry as a bypass for cryptographic proof/replay rules.

Checkpoint 876's owner-authorized accidental/technical interruption replacement procedure remains operative, while Attempt 001 AMEND, historical B01/B02 exact-byte approvals and all older evidence remain intact. 55 inherited source-audit findings remain preserved and risk-prioritized, not automatically re-reviewed. F1/F2 stay unfrozen. R0-P02 PASS, R0-P03 pending, ADS physical architecture still unselected, Specification 028 unchanged.

```text
CHECKPOINT_879=ONE_RUN_SYNTHETIC_DURABLE_REPLAY_PASS
NEXT_ACTOR=chatgpt
NEXT_BOUNDARY=p-one-signed-fresh-run-identity
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
