# Checkpoint 878: R0-P01 synthetic unauthorized admission tests pass, durable replay qualification next

**Date:** 2026-10-11
**Checkpoint class:** R0-P01 owner-authenticity research probe / signed-but-unauthorized cryptographic admission qualification
**Project stage:** R0 physical-architecture decision probes
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-37
**Conversation title:** 37 - Project System Realization Architecture and Qualification
**Primary collaborator:** ChatGPT
**Status:** SYNTHETIC_ADMISSION_SECURITY_PASS / DURABLE_CONSUMPTION_ACROSS_RESTART_NEXT
**Research:** Research 542
**Validation:** Validation 230
**Scope:** Test valid SSH/WebAuthn signatures that must be denied by trust-role, replay, identity and semantic-base policies; verify rejected admissions cannot mutate ledger state.
**Authority:** Non-owner synthetic runtime testing only. No owner credential use, scored F1/F2 freeze, B01/B02 modification, real Attempt 002 authorization or physical ADS target selection.

New `tests/unit/test_r0_p01_signed_unauthorized_admission.py` provides 19 executable synthetic admission tests. Both Ed25519 and ES256 cryptographic positive controls are actually verified; disallowed recovery roles, unregistered signers, stale governed lineage, view/event identity changes and consumed IDs must be rejected. Separate P5 rotation and P6 recovery cases verify both old-signer denial and new authorized signer acceptance. Rejected operations are checked against a deep snapshot of the entire mutable ledger trust state. All 19 passed, and the combined historical-source and actual-crypto R0-P01 regression is 111 PASS.

Research 542 records the meaningful next risk: an in-memory consumed-ID check alone does not demonstrate durable replay resistance across separate processes or restart. Qualify this with synthetic, public test material and a revised successor implementation boundary; do not accidentally treat a fresh owner-authorized **new research run** as permission to replay an old acceptance ID within the original trial. No automatic Claude review or repetitive procedural rulebook expansion is requested.

The broader R0-P01 safety objective remains accurate forgery/replay/role/semantic binding, safe operation, faithful owner-facing measurement, and independent score qualification. The owner has explicitly approved a simpler separately authorized replacement procedure after declared accidents or technical interruption, preserving original evidence. Attempt 001 remains permanent AMEND; 55 inherited source-review findings remain pending and should be triaged by actual risk rather than driving automatic review cycles.

R0-P02 PASS; R0-P03 pending; physical realization architecture open; Specification 028 unchanged; F1/F2 unfrozen and real Attempt 002 unauthorized.

```text
CHECKPOINT_878=SIGNED_BUT_UNAUTHORIZED_ADMISSION_REGRESSION_PASS
NEW_EXECUTABLE_TESTS=19
FOCUSED_TESTS=111
NEXT_ACTOR=chatgpt
NEXT_BOUNDARY=p-one-durable-replay-across-process
F1=UNFROZEN
F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
