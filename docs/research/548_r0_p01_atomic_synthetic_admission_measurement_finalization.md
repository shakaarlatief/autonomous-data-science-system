# Research 548: atomic synthetic admission and measurement finalization

**Date:** 2026-10-12
**Status:** SYNTHETIC_MEASURED_ADMISSION_ATOMICITY_VALIDATED / HUMAN_MEASUREMENT_AND_F1_OUTCOME_UNQUALIFIED
**Scope:** Close the tested successful-admission versus timing-observation commit gap from Research 547 without adding a new journal, replacing the physical ADS architecture, or complicating owner-authorized interrupted-run replacement.
**Parent:** Research 547 / Validation 235 / Checkpoint 883; owner-approved simple operator-accident replacement procedure at Checkpoint 876.
**Authority:** Synthetic non-owner implementation and test evidence only. No owner credential, Windows Hello ceremony, human execution approval, F1/F2 freeze or real Attempt 002.

## Specific failure and proportionate implementation

Checkpoint 883 showed that cryptographic acceptance was committed by `SyntheticClaimStore.admit`, after which `run_measured_synthetic_case` independently called `record_observation`. A crash after the first transaction but before the second left an accepted signature with no captured elapsed operation evidence. The historical assessor correctly disclosed `observation_coverage=MISSING`, but could not make the measured path complete by itself.

The fix **extends the existing journal and API**. No new SQLite tables, schemas, separate queues or generalized recovery machinery are introduced. A single optional `measurement_started_ns` argument to `SyntheticClaimStore.admit` activates atomic synthetic measurement in governed mode. The orchestrator captures `time.perf_counter_ns()` **immediately before synthetic signing** and passes this start value to the admission call. Only after independent verification of the exact signed run statement, public signer and current claim does the store calculate elapsed nanoseconds using a monotonic clock, validate the interval and append a fixed, predetermined `COMPLETED` nonsecret observation.

The accepted signature, consumed claim status and elapsed-time observation then **commit in the same SQLite transaction** under the existing `BEGIN IMMEDIATE` lock. An invalid signature cannot append success evidence. Invalid, impossible or future monotonic timestamps refuse/roll back a measured acceptance. A replayed claim cannot append another completed observation. The synthetic orchestration skips its former separate observation write on successful measured admission; interruption and failure observations still use their previous independent, non-success path. The pre-existing unmeasured `admit` remains for earlier tests and transparently yields `observation_coverage=MISSING` unless some other observation exists.

## Direct executable proof

The new `tests/unit/test_r0_p01_atomic_measurement_finalization.py` contains **22 executable cases** across actual locally installed Windows OpenSSH Ed25519 SSHSIG verification and Node synthetic WebAuthn-shaped ES256 verification using ephemeral in-process non-owner keys.

- A signed acceptance from the correct enrolled public signer commits exactly **one** `COMPLETED` observation with its synthetic precommit elapsed milliseconds. An injected delay before admission is reflected in the measured interval.
- An actual separate Python process forcibly exits from the commit seam **before** SQLite commit. After restarting, the claim remains issued and no completion observation exists. A legitimate fresh admission then succeeds once and commits its observation.
- A process forcibly exits **after** SQLite commit but **before** returning the result. After restarting, both accepted proof and duration observation remain persisted and cryptographically reverify; retry returns `CLAIM_NOT_ACTIVE` with no further mutation.
- A valid-looking but wrong signed decision context cannot commit an observation or acceptance. Invalid monotonic start types, zero, negative values and an impossibly future start reject with state unchanged.
- The earlier unmeasured API still leads to an accepted proof with `observation_coverage=MISSING`, preserving honest reporting rather than claiming universal evidence atomicity.

**Observed:** new cases **22/22 PASS**. The combined run exceeded the purpose-specific bridge time limit without returning a result, so it was **not** counted as a test pass. The unchanged scopes were re-executed in bounded groups: **116/116 executable core/integration**, **63/63 executable signature/admission/security**, **84/84 structural source/guard**. The resulting total is **179 actual executable synthetic tests** plus **84 structural regression checks**, or **263 passing focused checks**.

## Explicit scope and limits

The elapsed interval ends **after real synthetic signature verification but immediately before the SQLite commit**. It excludes the final database commit/fsync duration, prior run issuance, human signing preparation, passphrase entry, platform-authenticator user-presence latency, and any real owner interaction. The signer call count of one is a *scripted invocation*, not a human gesture measurement. The method's start timestamp is caller-provided synthetic instrumentation rather than separately attested evidence. This code does not prove malicious-disk rollback protection or power-loss durability in a hostile platform. A direct legacy unmeasured admission still exists and must be considered non-complete in any future evidence qualification. Failed/interrupted observations use a separate transaction and are outside the atomic-success guarantee.

It does **not** implement a full scored R0-P01 experiment, independently frozen F1 oracle, real WebAuthn Windows Hello credential, real owner trust bootstrap, or owner-execution consent. The local prototype's journal and format are not final architecture choices.

## Next bounded research task

Move toward **independently authored actual outcome vectors for the successor implementation**, using the now tested cryptographic, authorization, durable-state and measurement pathways. Carefully distinguish signature validity, procedural research permission, interruption, missing evidence and the formal scored outcome. Evaluate whether any genuinely necessary host-specific Windows/authenticator qualification remains before requesting a *separate* owner authorization for Attempt 002. Do not resume the superseded B02 Ctrl+C exceptional-retry approval bureaucracy.

```text
RESEARCH_548=ATOMIC_SYNTHETIC_ACCEPTANCE_MEASUREMENT_PASS
NEW_EXECUTABLE_TESTS=22
EXECUTABLE_TOTAL=179
STRUCTURAL_TOTAL=84
FOCUSED_TOTAL=263
TESTED_PRECOMMIT_AND_POSTCOMMIT_CRASH=PASS
REAL_OWNER_TIME=NOT_MEASURED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
