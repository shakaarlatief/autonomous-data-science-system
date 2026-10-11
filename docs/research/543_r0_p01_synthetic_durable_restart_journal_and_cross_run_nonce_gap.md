# Research 543: R0-P01 durable synthetic admission across restart, with a demonstrated cross-run limitation

**Date:** 2026-10-11
**Status:** SYNTHETIC_CRASH_RESTART_PROTOTYPE_VALIDATED / CROSS_RUN_SIGNED_NONCE_GAP_OPEN
**Scope:** Test replay consumption and current signer history after process crashes/restarts using actual synthetic Ed25519/ES256 verification, without committing to an ADS storage architecture.
**Parent:** Research 542 / Validation 230 / Checkpoint 878 / owner-approved simplified accidental-replacement procedure.
**Authority:** Public non-owner synthetic testing only. No B01/B02 amendment, real owner-key material, physical architecture selection, F1/F2 freeze or Attempt 002 execution.

## Engineering question and observed result

The historical V02 `Ledger` correctly rejects repeated acceptance IDs **within one process** and preserves signer-role transitions in memory, as confirmed by 19 existing signed-admission tests. This is insufficient evidence that the same rule survives process loss. A terminated process can discard its consumption set and current trust members, so **we implemented a bounded, explicitly synthetic, one-run durability experiment** rather than conducting another normative-source review.

The new module `experiments/r0_p01_successor_synthetic/durable_admission.py` implements a small SQLite FULL-synchronous transaction journal. Its immutable public genesis binds the **caller-provided** synthetic run identity, fixture, arm, scenario and all initial signer roles/credentials. Its admitted-event rows contain exact canonical signed records, consumed acceptance IDs, record hashes and a public ordered hash chain. On every use, the store replays and cryptographically verifies all persisted acceptance records through the historical V02 `Ledger.admit`. An admission uses `BEGIN IMMEDIATE`, so competing processes must serialize before testing and consuming an ID. The accepted record, unique acceptance ID and end-of-journal sequence/head update commit atomically. Rejected submissions publish no trusted state.

Fresh journal creation must be explicitly indicated with `create=True`. Normal restart opens an existing file without creating or silently resetting it. If the database or committed metadata is missing, the operation fails closed. This prevents accidental loss of consumed-ID history from being mistaken for a fresh empty run, while acknowledging that the prototype does **not** independently prevent malicious full-file deletion/rollback by an actor authorized to create a fresh store.

## Actual tests, not simulated documentation

The new `tests/unit/test_r0_p01_durable_synthetic_admission.py` contains **15 executable tests**:
- Both arm A (OpenSSH Ed25519) and arm B (ES256) persist consumption across an actual **new child Python process**, which re-verifies the signed acceptance and rejects reuse without any change to durable state.
- A separate child process exits abruptly **before SQLite commit** and leaves no consumed state; the original valid acceptance remains available. A child process exiting abruptly **after commit but before response** leaves the ID consumed, and retrying it is rejected.
- Two actual concurrent Python processes racing to accept one signature produce exactly one admission and one consumed-ID rejection, never double application.
- Restart after a genuine signed P5 primary trust-root rotation reconstructs the newer signer-set version. The previously signed statement is stale and rejected, while an authorized current-primary signature is admitted.
- A changed synthetic run identity or initial public trust identity cannot reopen the same journal; row corruption, deleted accepted rows and missing/empty journal state fail closed.
- A rejected same-ID replay does not change the durable public-state snapshot.

**Most importantly, the tests explicitly demonstrate a remaining security gap:** the historical V02 signed statement has **no unique per-research-run nonce**. The same historically valid signed P0 acceptance may be admitted in *two separate freshly initialized databases*, even if their externally supplied synthetic run IDs differ. A file-name or metadata label is **not** sufficient claim binding. This is an intentional observed negative result, not evidence of success. **A future R0-P01 successor MUST bind a fresh independently verified run nonce or unique claim identity into the actual signed statement and its verification context.** The new, human-authorized replacement-run procedure also requires a new cryptographic claim identity; it cannot simply reuse a signed historical decision.

## Limits and proportionate next implementation

The public hash chain only checks internal consistency and ordinary corruption. It is **not** adversarially anchored anti-rollback proof: a malicious actor with disk-control could replace or truncate a database and its metadata. SQLite tests establish observed process-crash/restart behavior under this Windows workspace, not comprehensive sudden-power-loss or multi-host correctness. Real owner authentication, RP/WebAuthn platform ceremony, signed fresh-run nonce, end-to-end successor proof/scorer integration, crash-safe reporting of *rejected* records, external audit sealing and the human-approved run-specific execution consent remain separate concerns.

The SQLite backend and use of the historical Ledger are **replaceable test decisions**, not frozen storage or interface architecture. Do not preserve them merely to conform to this prototype if a better ADS realization emerges. The next essential development task is a **successor-level signed fresh-run identity and cross-run replay negative test**, followed by minimal durable audit-anchoring as required by the actual threat model. Do not reintroduce the superseded exceptional-retry cap or an automatic Claude review campaign.

```text
RESEARCH_543=PER_RUN_DURABLE_REPLAY_SYNTHETIC_PROTOTYPE_VALIDATED
NEW_EXECUTABLE_TESTS=15
CROSS_RUN_OLD_SIGNATURE_REPLAY=KNOWN_GAP_REPRODUCED
OWNER_CREDENTIAL_USE=NONE
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
