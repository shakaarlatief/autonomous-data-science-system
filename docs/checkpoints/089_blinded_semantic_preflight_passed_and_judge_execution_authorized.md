# Checkpoint 89: Blinded Semantic Preflight Passed and Judge Execution Authorized

**Date:** 2026-08-19

## Purpose

Record the successful corrected no-inference preflight for the Prototype V0 blinded semantic-evaluation supervisor and authorize the preregistered held-out semantic judge stage.

## Verified boundary before judge inference

The user pulled the blind-ID test correction and ran:

```bash
pytest
python -m ads_v0.heldout_monitor status
python -m ads_v0.semantic_judge_supervisor prepare
python -m ads_v0.semantic_judge_supervisor status
```

Observed:

```text
pytest: 84 passed in 12.14s
held-out monitor:
    active=none
    completed_attempts=34
    verified=34
    integrity_failures=none

semantic preparation:
    prepared blinded cases: 30 / 30
    model inference launched: 0
    private decoder created locally and excluded from blinded review exports

semantic status:
    prepared_cases=30
    logical_passes=0/60
    completed_cases=0/30
    manual_cases=0
    provider_calls=0
    next=case-0586d0f63f905bd0 pass 1
```

The corrected deterministic suite therefore passes completely and the 30-case preparation is stable and idempotent.

## Experimental integrity

At this boundary:

```text
held-out treatment slots resolved: 30 / 30
held-out treatment reruns authorized: none
prepared blinded semantic cases: 30 / 30
held-out semantic logical passes persisted: 0 / 60
held-out semantic provider calls launched: 0
condition decoder inspected: no
condition-level semantic comparison performed: no
```

The semantic supervisor uses the already calibrated judge implementation and registered Foundation 012 rules. It does not change treatment trajectories, S1-S10 anchors, SC1/SC2 definitions, the two-pass requirement, consensus rules, or manual-adjudication triggers.

## Judge execution rule

Each of the 30 opaque cases requires two independently instantiated completed judge passes, for 60 logical passes total.

A usable completed logical pass is never rerun because of its score. A failed provider call that produces no usable judgment may be retried condition-neutrally, with at most three provider attempts for one logical pass. All provider attempts are persisted separately.

The supervisor remains condition-blind during execution. Terminal progress may reveal only opaque case IDs, logical pass numbers, provider-call counts, completion counts, and whether blinded manual adjudication is required. It must not expose the private decoder or aggregate B0/B1/P0 semantic results.

## Authorized unattended command

A single bounded batch may now be launched:

```bash
python -m ads_v0.semantic_judge_supervisor run-batch --max-judge-calls 180
```

Why `180`:

```text
30 cases × 2 logical passes = 60 required completed judgments
maximum 3 provider attempts per logical pass
60 × 3 = 180 absolute provider-call allowance
```

This is an upper bound, not a target. With no provider failures, the supervisor should launch 60 calls and stop at `JUDGE_COMPLETE`. It stops earlier if a logical pass exhausts its three provider attempts or another explicit safety state is reached.

The command writes every successful logical pass immediately, is resumable, and produces one blinded review ZIP at the end of the invocation. The export explicitly excludes `private_decoder.json`.

## Required next review

After the batch stops, inspect only the blinded review export before any condition decoding.

If no manual adjudication is required, freeze the blinded consensus directly. If one or more cases require adjudication because of an S1-S10 `0` versus `2` disagreement or an SC1/SC2 flag disagreement, adjudicate those cases using the blinded packets and judge outputs only.

Only after every required adjudication is frozen may the private decoder be used to map opaque cases back to H1/H2 and B0/B1/P0 identities and calculate the preregistered variant-specific and pooled comparisons.

## Decision

The semantic supervisor preflight has passed. Prototype V0 is authorized to begin its preregistered held-out blinded semantic evaluation.
