# Current State

## Checkpoint

**Checkpoint:** 43  
**Date:** 2026-08-09  
**Development stage:** `dev-p0-03` controller/reference corrections deterministically validated; one final P0 development trajectory authorized before behavioral freeze  
**Implementation status:** All pre-P0 experimental controls remain frozen. The generic P0 corrections discovered in `dev-p0-03` now pass the complete local suite at 54/54 tests. `dev-p0-04` is designated the final planned P0 behavioral development-calibration trajectory before held-out freeze. No held-out H1/H2 treatment run has occurred.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The long-term target is a system-mediated data-science process that operationalizes methodological knowledge, questions, checks, dependencies, repair, persistent state, and selective human involvement. The LLM is one reasoning component inside that system, not the system itself.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

Semantic spine:

```text
PROJECT STATE
  -> KNOWLEDGE ACTIVATION
  -> QUESTIONS / OBLIGATIONS / CONSTRAINTS
  -> RUNNABLE ACTIONS
  -> EXECUTION
  -> EVIDENCE
  -> STATE UPDATE
  -> DEPENDENCY IMPACT / REOPENING
```

## Experimental conditions

```text
B0
Strong LLM + Python + project artifacts + strong generic data-science guidance.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, prospective gate, or dependency repair.

P0
Same underlying model/tools + typed project state
+ the same four structured knowledge components
+ state-triggered activation/applicability
+ prospective protected-test safeguard
+ dependency-aware repair
+ minimal state-derived runnable frontier
+ append-only state-change history.
```

B1 remains the primary architectural control. P0 must demonstrate value from operationalization rather than from receiving better methodological knowledge.

## Baseline development calibration

All six B0/B1 development trajectories completed and passed critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

The clearest repeated B1 semantic advantage was explicit inherited learned-preprocessing diagnosis:

```text
B0: 0/3 strong
B1: 2/3 strong
```

Both simpler conditions were already strong on protected-test discipline and Phase 2 repair.

## Frozen held-out protocol

Authoritative files:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

Held-out design:

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out runs each
30 treatment runs total
```

Common treatment envelope:

```text
24 successful model calls
250,000 observed treatment tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries per semantic turn
60 s Python timeout
300 s provider timeout
```

A call may begin only while cumulative observed usage is below 250,000. The completed crossing call remains part of the trajectory, marks the run budget-exceeded, and prevents any further call. The resource envelope has not been increased in response to P0 development failures.

Frozen held-out bundles:

```text
H1 seed 811
SHA-256 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed 1601
SHA-256 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

No held-out treatment trajectory has run.

## Frozen semantic judge

Targeted score:

```text
mean(S1, S2, S3, S6, S7)
```

Pre-P0 calibration:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

No rubric, threshold, bundle, B0/B1 prompt, or privileged knowledge component changed afterward.

## P0 architecture

Typed objects:

```text
ARTIFACT FACT ASSUMPTION QUESTION EVIDENCE CLAIM DECISION OBLIGATION ACTION
```

Relations:

```text
DEPENDS_ON SUPPORTS CONTRADICTS ANSWERS GENERATED_BY
```

Exactly four privileged components:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

Current controller capabilities include scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived motivators/frontier, blocking and repair priority, phase gates, dependency-aware reopening, append-only audit history, compact current-state projection, and persistent model-created client-ref aliases to canonical state IDs.

## Real P0 development history

### `dev-p0-01`

```text
Completed: False
Budget exhausted: True
Calls: 10
Tokens: 250,279
Python: 2
Critical deterministic pass: False
```

Reached early Phase 2. Raw diagnosis found same-turn motivator-closure rejection and repeated audit-state serialization. Both were corrected.

### `dev-p0-02`

```text
Completed: False
Budget exhausted: True
Calls: 12
Tokens: 291,350
Python: 4
Critical deterministic pass: True
```

Reached legitimate protected final evaluation after targeted repair. Only final reconciliation/reporting remained. Raw diagnosis found temporary/canonical-ID handoff failure, removable audit metadata, and a terminal budget-accounting edge case. Corrections were validated with 50/50 tests.

### `dev-p0-03`

```text
Completed: False
Budget exhausted: True
Calls: 14
Input tokens: 250,015
Output tokens: 10,219
Total tokens: 260,234
Python: 4
Critical deterministic pass: False
```

The run reached revised Phase 2 development and had already produced legitimate replacement six-feature model evidence. It failed to reach final lock because of three avoidable state-reference/controller rejections and a redundant support-loss repair blocker targeting the broad deliverable obligation.

Per-call context cost improved materially versus `dev-p0-02`; the first twelve common calls were approximately 13% to 40% cheaper, and model-facing state views were about 2.0k to 9.7k characters.

Corrections from `dev-p0-03`:

```text
accepted client refs persist as aliases to canonical state IDs;
later relations/status updates may use canonical IDs or remembered aliases;
same-patch client refs may be supplemental motivators only when a valid pre-patch motivator already satisfies the frontier;
same-patch-only motivators remain invalid;
redundant support-loss reassessment of an OBLIGATION is closed before phase gates.
```

A questionable model-authored hard dependency observed in `dev-p0-03` was deliberately not auto-rewritten because it did not cause the registered critical failure and relation quality is behavior to evaluate rather than silently repair benchmark-specifically.

## Deterministic validation after `dev-p0-03` corrections

The complete local suite passes:

```text
54 passed in 17.43s
```

This validates deterministic coherence of the corrections only. It does not establish P0 completion, resource viability, or superiority over B1.

## Final P0 development-run boundary

`dev-p0-04` is the **final planned P0 behavioral development-calibration trajectory before held-out freeze**.

It must use the unchanged common resource envelope and model configuration.

After `dev-p0-04`, P0 behavioral/controller logic should be frozen for held-out execution regardless of whether the run completes successfully, unless a purely mechanical protocol/runtime correctness defect makes the experiment itself invalid.

Do not continue tuning P0 merely because a further heuristic could improve this benchmark, a model-authored state relation is questionable, or another run might fit within budget. Those outcomes must remain observable evidence about the architecture.

## Remaining common pre-held-out engineering

After P0 behavioral freeze, held-out execution still requires common experiment infrastructure:

```text
B0/B1 enforcement of the registered 24-call / 250k-token / 12-Python envelope;
held-out run scheduler and preregistered ordering;
batch blinded semantic judging;
manual-adjudication handling;
resource/outcome aggregation and continuation/falsification comparison.
```

These are common experiment-control tasks, not P0 behavioral tuning.

## Relevant latest records

```text
docs/checkpoints/040_p0_second_corrections_deterministically_validated.md
docs/checkpoints/041_third_real_p0_run_budget_exhaustion_terminal_record.md
docs/checkpoints/042_dev_p0_03_raw_diagnosis_and_reference_semantics_hardening.md
docs/checkpoints/043_p0_reference_semantics_validated_and_final_development_run_boundary.md
```

## Current priority

**Run `dev-p0-04` under the unchanged frozen resource envelope, inspect it completely, then freeze P0 behavioral/controller logic and move to common held-out experiment infrastructure.**

H1/H2 remain untouched.