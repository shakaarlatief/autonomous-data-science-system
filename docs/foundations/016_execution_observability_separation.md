# Foundation 016: Execution and Observability Separation

**Date:** 2026-08-19  
**Status:** Accepted system-level architectural principle  
**Scope:** Long-running system workflows, experiment orchestration, evaluation, and future autonomous project execution

## Purpose

Prototype V0 exposed the same design question twice in different forms.

Held-out treatment execution used:

```text
heldout_supervisor.py
    execution and experiment-control responsibility

heldout_monitor.py
    separate read-only human observability
```

The blinded semantic judge initially placed live progress printing directly inside:

```text
semantic_judge_supervisor.py
```

Both designs were operationally workable. The important architectural question is therefore not which implementation already exists, but which separation is strongest for the long-term Autonomous Data Science System.

The preferred answer is:

> Execution and observability should be separate responsibilities connected through persisted structured state or events.

This is broader than terminal output. It defines which parts of the system are allowed to influence work and which parts merely help a human understand that work.

---

## 1. Core architecture

The target pattern is:

```text
EXECUTION / REASONING PROCESS
        |
        | performs work
        | owns state transitions
        | persists structured events/artifacts
        v
PERSISTED OBSERVABLE STATE
        |
        +-------------------+
        |                   |
        v                   v
VERIFICATION / AUDIT    OBSERVABILITY
                            |
                            | read-only
                            v
                     HUMAN INTERFACE
```

The observer is downstream of execution.

There must be no ordinary control path:

```text
observer -> execution semantics
```

A display failure must not become an execution failure merely because both capabilities happen to be running on the same machine.

---

## 2. Why separation is preferable

### 2.1 Reliability isolation

A monitor may contain formatting, timestamping, heartbeat logic, elapsed-time calculation, progress aggregation, terminal refresh behavior, or later a graphical interface.

Those capabilities are useful but are not part of analytical correctness.

With a sidecar observer:

```text
observer crashes
    -> execution continues

observer is stopped
    -> execution continues

observer is upgraded
    -> execution semantics remain unchanged
```

This reduces the trusted execution surface.

### 2.2 Replaceable interfaces

The same persisted event/state contract can support:

```text
terminal watcher
CLI dashboard
web dashboard
VS Code panel
experiment console
notification service
historical replay
```

without requiring the execution engine to know which interface is active.

### 2.3 Better provenance

Structured persisted events are useful independently of a live UI. They support:

```text
reproducibility
audit
post-mortem analysis
mechanical verification
progress reconstruction
historical replay
```

Terminal strings should therefore not be the authoritative execution record.

### 2.4 Cleaner evolution

Presentation needs evolve much faster than analytical semantics. Human users may later want:

```text
local timestamps
heartbeats
elapsed time
estimated remaining work
progress percentages
warnings
resource counters
multiple concurrent project views
```

Keeping those concerns outside the core process prevents user-interface evolution from repeatedly modifying execution machinery.

---

## 3. Execution may still print minimal lifecycle information

Separation does not require absolute silence from an execution command.

A core process may emit coarse lifecycle messages such as:

```text
batch started
batch stopped
safety condition reached
experiment complete
export written
```

These messages are convenience output, not the primary observability architecture.

Detailed live presentation such as:

```text
current unit
current phase
case X / N
pass Y / M
local time
heartbeat
elapsed duration
provider-attempt progress
resource counters
```

belongs preferentially in the observer.

---

## 4. Observer contract

A read-only observer should satisfy the following properties.

### 4.1 No execution authority

The observer must not:

```text
launch model calls
run analytical code
advance workflow state
change retry eligibility
change stopping decisions
write treatment or judge evidence
modify project reasoning state
```

### 4.2 Read persisted truth

The observer should derive its display from state that the execution process already persists for its own provenance or recovery.

It should not require a second hidden state machine whose interpretation can silently diverge from the executor.

### 4.3 Tolerate concurrent writes

When observation occurs during execution, the observer should handle transient partial state conservatively.

Examples include:

```text
an append-only JSONL trace whose final line is currently incomplete;
a provider-attempt start marker without a completion marker;
a file that has not yet appeared because persistence occurs after a successful step.
```

Ambiguous observational state should be displayed neutrally rather than reclassified as an execution failure.

### 4.4 Respect information boundaries

An observer may only expose information appropriate to its audience.

For blinded semantic evaluation this means, in particular:

```text
read opaque blinded case state
never read private_decoder.json
never display B0/B1/P0 identity
never reveal treatment run identity before unblinding
```

Observability must not become a side channel that defeats experimental or security boundaries.

---

## 5. Time semantics

Human-facing progress should normally include local wall-clock time because it materially improves usability during long-running workflows.

A useful display pattern is:

```text
[14:34:22] case=08/30 pass=1/2 status=running elapsed=00:00:31
```

The authoritative persisted record should continue to use explicit timezone-aware timestamps, preferably UTC, while observers may render those timestamps or current progress in the user's local time.

This separates:

```text
machine/provenance time
    -> timezone-aware persisted UTC

human display time
    -> local readable timestamp
```

---

## 6. Prototype V0 evidence

### Held-out treatment execution

The read-only held-out monitor demonstrated the value of sidecar observability.

It could be introduced after the supervisor/verifier were already validated without changing the frozen execution path. It displayed live trace progress and heartbeats, and a later monitor-only counting defect could be corrected after treatment execution without changing any treatment evidence or supervisor decision.

That is direct evidence for fault isolation between execution and presentation.

### Blinded semantic evaluation

The semantic supervisor was built fresh and therefore included live progress printing internally. This was safe for V0, but the resulting discussion exposed that the implementation history should not determine the long-term architecture.

After the complete semantic run, a separate:

```text
prototype_v0/src/ads_v0/semantic_judge_monitor.py
```

was added to establish the same read-only sidecar pattern for semantic judging.

The evidence-producing semantic supervisor itself is intentionally not rewritten merely to remove its existing prints. Git preserves the exact implementation that generated the evaluation evidence. Future workflows should use the cleaner separation prospectively rather than retroactively rewriting experimental instrumentation for presentation reasons.

---

## 7. Recommended future observable-state contract

The full system should eventually converge on a common machine-readable event/state interface rather than building unrelated monitor parsers for every workflow.

A future event representation may include fields such as:

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

This is a direction, not a requirement to introduce an event bus or observability platform now.

Prototype V0 should keep the implementation small. Reusable infrastructure becomes justified when multiple workflows demonstrate enough common structure to reduce rather than increase complexity.

---

## 8. Relationship to the long-term autonomous system

This principle applies beyond experiments.

A future Autonomous Data Science System may execute:

```text
data inspection
feature investigations
model searches
validation studies
report generation
external tool calls
human approval waits
long-running background project work
```

Humans should be able to inspect that activity without the UI becoming part of the reasoning mechanism itself.

The architectural boundary therefore becomes:

```text
SYSTEM CORE
    reasoning + execution + persisted state

OBSERVABILITY LAYER
    read-only projection of safe system state for humans and operational tooling
```

This is consistent with the broader system view that the LLM, executor, verifier, state store, and human interface are components of one system with different responsibilities rather than one monolithic conversational process.

---

## 9. Current implementation consequence

For Prototype V0 and immediate follow-up work:

```text
held-out treatment execution
    heldout_supervisor.py + heldout_monitor.py

blinded semantic judging
    semantic_judge_supervisor.py + semantic_judge_monitor.py
```

Detailed monitoring belongs in the sidecar monitors.

The V0 evidence-producing supervisors should not be rewritten solely to conform aesthetically after the fact. Their existing Git versions remain provenance. New workflows and later architecture should adopt execution/observability separation prospectively.
