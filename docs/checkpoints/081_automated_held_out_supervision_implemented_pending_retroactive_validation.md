# Checkpoint 81: Automated Held-Out Supervision Implemented, Pending Retroactive Validation

**Date:** 2026-08-18

## Purpose

Record the architectural change that removes repetitive human transport and repeated manual mechanical inspection from Prototype V0 held-out execution while preserving the frozen treatment experiment unchanged.

The user explicitly raised a scalability concern after ten resolved treatment slots. The scientific experiment itself was not the problem. The operational loop around it had become too manual:

```text
run attempt
-> paste terminal output
-> package raw artifacts
-> upload raw ZIP
-> manually re-check repeated mechanics
-> update repository
-> pull
-> launch next attempt
```

The project agreed that continuing this way for the remaining twenty slots would waste time and would not scale to future experiments with hundreds of trajectories.

## Architectural decision

The project now separates:

```text
FROZEN TREATMENT EXECUTION
    existing heldout_runner and B0/B1/P0 behavior

EXTERNAL EXPERIMENT SUPERVISION
    automated read-only verification and sequential orchestration
```

The treatment side remains unchanged.

## New implementation

Created:

```text
prototype_v0/src/ads_v0/heldout_verifier.py
prototype_v0/src/ads_v0/heldout_supervisor.py
prototype_v0/tests/test_heldout_verifier.py
prototype_v0/tests/test_heldout_supervisor.py
```

### Mechanical verifier

The verifier is read-only with respect to attempt artifacts and performs no model inference or semantic judging.

Version `v0.1.0` currently checks:

```text
M01 required attempt artifacts
M02 frozen slot / attempt identity
M03 frozen plan and bundle hashes
M04 frozen registered runtime configuration
M05 summary / executor classification consistency
M06 resource accounting and budget semantics
M07 trace sequencing and resource reconciliation
M08 exact deterministic-evaluator recomputation
M09 milestone / trace consistency
M10 protected final-test value access sequencing
M11 conversation / successful-model-call consistency
```

It writes reports outside treatment attempt directories:

```text
results/held_out/mechanical_verification/
```

Reports include hashes of the source attempt artifacts so the verification result remains tied to exact persisted bytes.

Behavioral events such as a Python error, timeout, budget exhaustion, incomplete work, generation retry, or deterministic failure are recorded as review flags. They do not become replacement reasons or integrity failures merely because the treatment performed poorly.

### Sequential supervisor

The supervisor delegates every paid attempt to the already-frozen:

```text
heldout_runner.execute_next_attempt()
```

It does not implement a second execution path.

It supports:

```text
status
verify-existing
run-batch --max-model-attempts N
export
```

A batch remains strictly sequential. The next attempt cannot begin until the prior attempt has returned, persisted its executor record, and passed mechanical integrity verification.

Registered provider-failure replacements remain inside the same slot and can continue automatically through the existing runner. Behavior-evaluable outcomes remain permanently retained even when they contain poor methodology, Python errors, budget exhaustion, or deterministic failures.

Compact exports contain verification and supervisor reports, not raw treatment conversation text.

## Experimental integrity boundary

This change does not modify:

```text
B0 prompt
B1 prompt
P0 behavior or controller
P0 knowledge
H1/H2 bundles or hashes
run order
condition order
model/provider
reasoning effort
resource limits
provider retry semantics
structured-output normalization
replacement policy
protected-test rules
A0-A4 evaluator
semantic S1-S10 / SC1-SC2 rubric
blinded judge procedure
continuation or falsification criteria
```

No paid held-out attempt has yet been launched through the new supervisor.

## Validation gate before prospective use

The supervisor is not authorized for paid held-out execution merely because the code has been written.

Before the next frozen slot may run through the supervisor:

```text
1. pull Checkpoint 81;
2. run the full deterministic pytest suite;
3. run heldout_supervisor verify-existing;
4. retroactively verify every completed attempt, including the two non-behavior-evaluable provider attempts;
5. require zero verifier integrity failures;
6. create one compact supervisor export;
7. inspect that export against the already-preserved manual records;
8. repair verifier/supervisor defects only if needed;
9. freeze the validated supervision layer;
10. only then authorize prospective batch execution.
```

This ensures that the same verifier is applied to earlier and later attempts rather than being trusted only on future outputs.

## Current experiment state

The treatment experiment itself remains:

```text
resolved treatment slots: 10 / 30
remaining treatment slots: 20 / 30
next frozen slot: h1-r04-b1-a01
```

That slot is temporarily held behind the supervisor-validation gate. It has not been skipped, reordered, or changed.

## Documentation promotion audit

This is a major evaluation-infrastructure architecture change rather than a local checkpoint-only implementation detail.

Promoted to:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/MAJOR_CHANGES.md
```

No change to `VISION.md` or the frozen Prototype V0 experimental foundations is warranted because the system vision and treatment contract did not change.

## Next step

Run deterministic tests and retroactive verification only. Do not launch `h1-r04-b1-a01` until those checks have been reviewed.
