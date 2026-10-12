# Research 547: measured synthetic R0-P01 operation and evidence-aware descriptive outcome

**Date:** 2026-10-12
**Status:** EXECUTED_SYNTHETIC_MONOTONIC_MEASUREMENT_AND_OUTCOME_TESTS_PASS / ACTUAL_OWNER_EFFORT_AND_F1_SCORER_NOT_QUALIFIED
**Parent:** Checkpoint 882, Research 546, Validation 234, owner-approved simplified accident-replacement procedure at Checkpoint 876.
**Scope:** Replace exclusively caller-supplied duration observations in the synthetic rehearsal with a directly measured test-operation interval, preserve interrupted/replaced attempts, and produce descriptive outcomes from verified durable admission state rather than completion notes.
**Authority:** Non-owner synthetic test execution only. No genuine human-owner execution authorization, credential ceremony, F1/F2 scorer freeze, or ADS physical architecture selection.

## Problem and actual improvement

Checkpoint 882 preserved procedural permission, interruption and effort records in a durable synthetic journal, but all time measurements were caller supplied. Those observations were not proof of elapsed operation time. Also, an event labelled `COMPLETED` must not be mistaken for verified governing acceptance.

The new `experiments/r0_p01_successor_synthetic/synthetic_measurement.py` supplies two strictly bounded operations:

1. `run_measured_synthetic_case` uses the already governed and tested `SyntheticClaimStore` to issue a synthetic claim, then captures a real elapsed interval using Python `time.perf_counter_ns` around the synthetic signing request and signature-admission operation. It saves the measured millisecond duration, the scripted signer-call count and a small predetermined nonsecret observation into the existing durable journal. It covers `VALID`, `INTERRUPTED` (no signing call) and `INVALID_PROOF` (correct signer signed different bytes) test paths. Any caught synthetic signer error saves only a generic error note, never a raw exception message.
2. `assess_verified_journal` first calls `store.snapshot(node)`, which reconstructs the issuer state and re-verifies committed signatures through the original real OpenSSH Ed25519 or synthetic ES256 crypto path. For each issued claim it returns a **descriptive** outcome: `VERIFIED_CRYPTOGRAPHIC_ADMISSION`, `SUPERSEDED_WITHOUT_ADMISSION`, `INTERRUPTED_WITHOUT_ADMISSION`, `ERROR_WITHOUT_ADMISSION`, or `UNRESOLVED_WITHOUT_ADMISSION`. A caller-supplied `COMPLETED` observation with no valid admitted proof **never** creates a successful cryptographic outcome. Per-claim and aggregate recorded elapsed times and scripted interactions retain all superseded/unfinished trials.

This is **not** a replacement for the R0-P01 independent F1 classification oracle. An `ADMITTED` signature is not evidence that a whole multi-event research trial should score PASS.

## Evidence completeness and a real remaining gap

The issued-run admission and its observation are committed in **separate** transactions. A crash after valid proof admission but before observation commit can leave a valid governing signature with no recorded timing evidence. Rather than conceal that issue, the assessment now reports `observation_coverage=PRESENT|MISSING` independently of the cryptographic admission outcome. Executable tests reproduce this postadmission missing-evidence case and require the missing coverage to be explicit.

**The gap remains open** for the eventual experiment: its evidence protocol must distinguish the recorded true observation interval from missing measurements and decide whether a crash-safe unified receipt/finalization mechanism is necessary. Do not claim that merely storing a valid signature makes burden evidence complete. The current small rehearsal does not purport to repair that atomicity yet.

## Executable regression results

The new `tests/unit/test_r0_p01_synthetic_measurement.py` provides **24 tests** across SSH Ed25519 and WebAuthn-shaped ES256:
- Legitimate signing and admission, real signed-but-invalid context and interruption generate independently authored expected descriptive classes.
- A simulated accident plus a separately approved valid replacement retains **both runs' observations and recorded effort**.
- A `COMPLETED` note without a governing signature does not award acceptance.
- An intentionally slowed synthetic signer demonstrates the monotonic measurement actually includes technical operation latency instead of merely trusting a supplied duration.
- An interruption invokes no signer; failures leave generic, nonsecret diagnostic text; invalid method/label/mode refuses issuance.
- Corrupted committed proof evidence is rejected when computing the report, and a new Python process recovers the same verified assessment.
- A cryptographically committed event missing a postcommit observation is explicitly reported as `observation_coverage=MISSING`.

Observed: **24/24 new tests PASS**; executable-focused **157/157 PASS**; structural source/guard suite **84/84 PASS**, for **241 focused passing checks**. The structural guards do not qualify the successor's operational or cryptographic behavior. No real owner key material is used.

## Correct boundaries and next step

The timer measures **synthetic local signing/admission operation latency**, which can include local verification and prior persisted-entry revalidation. It does **not** measure human time, password prompts, user-presence checks, actual WebAuthn/Windows Hello ceremony, owner decision effort or real interaction count. `interactions` represents a known *scripted* signer-call count, not real gestures. Persisted observations are not independently attested against a hostile controller, and a keyword-based note check is not secret redaction.

The next proportionate engineering task is to qualify the **minimal end-to-end evidence-finalization boundary**, especially a crash between signed admission and duration logging, then connect real owner-facing timing only when the consent and hardware test are separately approved. A separate bounded F1 expected-outcome oracle remains necessary before drawing an architectural winner; do not revive the older B02 exceptional-retry document-review loop just to decide whether the owner may restart a spoiled test.

```text
RESEARCH_547=SYNTHETIC_MEASURED_OPERATION_AND_DESCRIPTIVE_EVIDENCE_PASS
NEW_EXECUTABLE_TESTS=24
EXECUTABLE_TOTAL=157
STRUCTURAL_TOTAL=84
FOCUSED_TOTAL=241
POSTADMISSION_OBSERVATION_ATOMICITY=OPEN
REAL_OWNER_TIME=NOT_MEASURED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
