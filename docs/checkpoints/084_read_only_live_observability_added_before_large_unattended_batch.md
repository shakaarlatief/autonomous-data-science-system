# Checkpoint 84: Read-Only Live Observability Added Before Large Unattended Batch

**Date:** 2026-08-18  
**Status:** Operational observability improvement; no treatment or supervisor execution semantics changed

## Why this checkpoint exists

After the first prospective supervisor batch passed, the remaining Prototype V0 held-out execution became eligible for one large bounded unattended sequential batch.

Before starting that longer run, one usability and operational concern remained: the validated supervisor prints its compact batch summary only when the batch finishes. For a long sequence of paid model runs, that can leave the terminal apparently idle for an extended period even while the experiment is progressing normally.

This is not a scientific or execution-correctness problem, but it is an observability problem. Long unattended jobs should expose enough read-only progress information to distinguish normal work from a stalled or failed process without changing the execution path.

## Change introduced

A new module was added:

```text
prototype_v0/src/ads_v0/heldout_monitor.py
```

with tests in:

```text
prototype_v0/tests/test_heldout_monitor.py
```

The monitor is intentionally separate from:

```text
heldout_runner.py
heldout_verifier.py
heldout_supervisor.py
```

The validated supervisor and verifier implementations are not modified.

## Authority boundary

The monitor is observation-only. It:

```text
launches no model calls;
changes no run order;
changes no replacement decision;
writes no attempt, supervisor, or verifier state;
performs no semantic judging;
does not modify B0, B1, P0, the benchmark bundles, or the frozen run plan.
```

It only reads the append-only local attempt and verification directories.

A started attempt that has not yet produced an executor record is reported neutrally as active/pending. The monitor does not attempt to decide whether such an attempt is still running or has actually been interrupted. The frozen runner remains authoritative for that distinction.

## Information displayed

During an active attempt the monitor can display:

```text
attempt identity
current phase
successful model generations observed in trace
Python execution attempts
generation-error count
trace-event count
latest event type
completed attempt-record count
mechanical-verification report count
verification-integrity failures, if any
```

The JSONL reader is tolerant of a partially written trailing line so that concurrent trace appends are not mistaken for integrity defects.

The monitor prints on observable state changes and also emits periodic heartbeats so a long provider call does not look indistinguishable from a dead terminal.

## Intended use

Use two terminals from `prototype_v0/`.

Monitoring terminal:

```bash
python -m ads_v0.heldout_monitor watch
```

Execution terminal:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

Stopping the monitor with Ctrl+C does not stop or modify the supervisor.

## Experimental consequence

None.

This addition does not alter the validated prospective execution mechanism. The large bounded batch remains governed by Decision D-027 and the frozen supervisor/verifier boundary established in Foundation 015.

## Promotion audit

No new system-level foundation or decision is required. This is a practical observability refinement that belongs in the operational checkpoint and current-state guidance. The broader durable principle that repeated mechanical work should be automated while human attention is reserved for semantic or exceptional decisions is already preserved in Foundation 015.

## Next step

Pull the monitor addition, run the software tests once, then start the read-only monitor and the already-authorized large supervisor batch in separate terminals.
