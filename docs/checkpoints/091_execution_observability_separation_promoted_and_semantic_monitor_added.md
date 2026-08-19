# Checkpoint 091: Execution-Observability Separation Promoted and Semantic Monitor Added

**Date:** 2026-08-19

## Purpose

Record the architectural conclusion reached after comparing the held-out treatment monitoring design with the blinded semantic-judge live-print design.

The question was deliberately framed as:

> What architecture is best for the long-term system, independent of what happened to be implemented first?

The answer is now promoted beyond Prototype V0 implementation detail.

## Architectural conclusion

The preferred system pattern is:

```text
EXECUTION / REASONING
    owns work, state transitions, safety, and persisted evidence

PERSISTED STRUCTURED STATE / EVENTS
    authoritative observable substrate

READ-ONLY OBSERVABILITY
    owns timestamps, heartbeats, elapsed time, progress rendering, and UI
```

Detailed human observability should normally be downstream from execution rather than embedded in the trusted execution path.

Minimal lifecycle printing from an executor remains acceptable.

## Why this was not treated as a cosmetic preference

The held-out treatment phase provided a useful empirical example.

The separately running `heldout_monitor.py` could be introduced and later corrected without changing:

```text
heldout_runner.py
heldout_supervisor.py
heldout_verifier.py
any treatment trajectory
any supervisor continuation decision
```

The monitor could be stopped independently and displayed local timestamps and heartbeats while reading only append-only execution artifacts.

The semantic supervisor, by contrast, initially included detailed progress printing directly in the execution process because it was built fresh before semantic inference. That was operationally safe, but implementation history is not itself an architectural justification.

The project therefore standardizes the cleaner sidecar-observer pattern for future workflows.

## New semantic sidecar observer

Added:

```text
prototype_v0/src/ads_v0/semantic_judge_monitor.py
prototype_v0/tests/test_semantic_judge_monitor.py
```

The monitor:

```text
launches no model calls;
writes no semantic state;
never reads private_decoder.json;
shows opaque case identity only;
shows case X/N and pass Y/2;
shows persisted logical-pass and completed-case counts;
shows provider-call counts;
shows active provider-attempt number;
shows local wall-clock timestamps;
shows elapsed time for an active provider call;
prints periodic heartbeats;
can be stopped without affecting semantic execution.
```

Example intended display:

```text
[14:34:22] active=case-... case=8/30 pass=1/2 provider_attempt=1 elapsed=00:00:31 | logical_passes=15/60 completed_cases=7/30 manual_cases=0 provider_calls=16
```

## Why the evidence-producing supervisors were not rewritten

The semantic judge batch had already completed before this architectural promotion.

The existing semantic supervisor therefore remains untouched in this change even though it contains detailed progress prints.

This is intentional.

The exact implementation that generated the experiment evidence should remain easy to identify in Git history rather than being rewritten after the fact merely to conform aesthetically to a newly clarified architecture.

The same reasoning applies even more strongly to the frozen held-out supervisor/verifier versions whose identities are already recorded in Foundation 015.

The architecture is improved prospectively by adding the observer and promoting the principle, not by obscuring the historical evidence-producing implementation.

## Durable promotion

The result is promoted to:

```text
docs/foundations/016_execution_observability_separation.md
```

and to canonical principle:

```text
docs/PRINCIPLES.md, P-022
```

The durable principle is broader than experiment monitoring. It applies to future autonomous analytical work, long-running tool execution, report generation, model search, validation studies, approval waits, and system dashboards.

## Future direction

Prototype V0 now has two concrete sidecar observers:

```text
heldout_monitor.py
semantic_judge_monitor.py
```

They should not immediately be generalized into a large observability framework merely because two monitors exist.

A future reusable event contract becomes justified when additional workflows demonstrate enough common structure that shared infrastructure reduces complexity.

The likely direction is a machine-readable event/state interface containing fields such as:

```text
timestamp_utc
workflow_id
project_id
unit_id
phase
event_type
sequence
status
progress_current
progress_total
safe_metadata
```

The observer can then project that state into terminal, web, editor, or notification interfaces.

## Validation status

The new semantic observer and its tests were added after the completed semantic-judge batch.

No experimental evidence depends on the new observer.

Local test-suite validation is required after the user next pulls the repository.

## Promotion audit

Promotion is complete:

```text
FOUNDATION
    Foundation 016 created

CANONICAL PRINCIPLE
    P-022 added

IMPLEMENTATION
    semantic_judge_monitor.py added
    test_semantic_judge_monitor.py added

KNOWLEDGE ROUTING
    KNOWLEDGE_MAP should route to Foundation 016

CURRENT STATE
    should record semantic completion and the new observer architecture
```

No change to the frozen Prototype V0 treatment or semantic scoring contract is warranted.
