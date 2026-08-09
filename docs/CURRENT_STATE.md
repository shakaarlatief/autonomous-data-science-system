# Current State

## Checkpoint

**Checkpoint:** 45  
**Date:** 2026-08-09  
**Development stage:** Final P0 development trajectory fully inspected; P0 behavioral/controller logic frozen for held-out evaluation  
**Implementation status:** `dev-p0-04`, predeclared as the final planned P0 behavioral development run, completed end-to-end inside the unchanged 24-call / 250,000-token / 12-Python envelope. Full raw inspection found no experiment-invalidating mechanical defect. Ordinary P0 behavioral/controller tuning is now closed. No held-out H1/H2 treatment run has occurred. The next work is common held-out experiment infrastructure, beginning with resource-envelope enforcement for B0/B1.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The LLM is one reasoning component inside a system that should operationalize methodological knowledge, project state, questions, evidence, claims, dependencies, repair, resource constraints, and selective human involvement.

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
No typed state, activation, deterministic gates, or dependency-aware repair.

P0
Same underlying model/tools + typed project state
+ the same four structured knowledge components
+ state-triggered activation/applicability
+ prospective protected-test safeguard
+ dependency-aware repair
+ state-derived runnable frontier
+ append-only audit history.
```

B1 remains the primary architectural control. P0 must demonstrate value from operationalization, not from receiving better methodological knowledge.

## Baseline development calibration

All six B0/B1 development runs completed and passed critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

Clearest repeated B1 semantic advantage:

```text
explicit inherited learned-preprocessing diagnosis
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

Common resource envelope:

```text
24 successful model calls
250,000 observed treatment tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries per semantic turn
60 s Python timeout
300 s provider timeout
```

A provider call may begin only while prior observed cumulative usage is below 250,000. If a completed call crosses the ceiling, that call remains part of the trajectory, the run is budget-exceeded, and no later call may begin. Terminal completion above the ceiling is still budget-exceeded. Failed provider attempts with observable usage count toward the same token envelope. Model-authored Python errors/timeouts remain behavioral and count as Python attempts.

Frozen bundles:

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

Strong targeted pass requires all five targeted criteria to equal 2.0.

Pre-P0 judge calibration:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

The judge reproduced the key manual S3 result exactly: B0 0/3 strong versus B1 2/3 strong. No rubric, threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component changed afterward.

## Frozen P0 architecture

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

Frozen controller capabilities include scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived motivators/frontier, blocking and repair priority, phase gates, dependency-aware reopening, append-only audit history, compact current-state projection, persistent client-ref aliases to canonical state IDs, same-patch supplemental-motivator handling that still requires a legitimate pre-patch motivator, and type-aware closure of redundant support-loss reassessment targeting obligations.

The complete local suite passed before the final development run:

```text
54 passed in 17.43s
```

## P0 development history

```text
dev-p0-01
Completed: False
Calls: 10
Tokens: 250,279
Python: 2
Critical deterministic pass: False
Reached early Phase 2; exposed motivator-order and repeated-audit-context defects.

dev-p0-02
Completed: False
Calls: 12
Tokens: 291,350
Python: 4
Critical deterministic pass: True
Reached legitimate protected final evaluation; exposed canonical-ID handoff, audit-metadata overhead, and terminal-accounting defects.

dev-p0-03
Completed: False
Calls: 14
Tokens: 260,234
Python: 4
Critical deterministic pass: False
Reached repaired Phase 2 evidence; final lock was prevented by reference-interface/controller friction. Context cost was materially lower than dev-p0-02.

dev-p0-04
Completed: True
Completed within budget: True
Budget exhausted: False
Calls: 12
Generation attempts: 12
Generation failures: 0
Input tokens: 218,948
Output tokens: 9,116
Total tokens: 228,064
Python: 4
Critical deterministic pass: True
All deterministic assertions: True
```

The first three runs remain development evidence and are not discarded or relabeled. They are not interchangeable stochastic replicates because implementation defects were repaired between them.

## `dev-p0-04` full inspection

Exact action sequence:

```text
1 read project brief
2 read README
3 inspect train metadata
4 inspect train/validation temporal and repeated-entity structure
5 inspect inherited baseline
6 leakage-safe Phase 1 model comparison
7 Phase 1 complete
8 read authoritative Phase 2 timing notice
9 eligible-feature Phase 2 re-evaluation
10 final model lock
11 single protected final evaluation
12 final report
```

There were:

```text
0 P0 state-control errors
0 treatment-command recovery loops
0 model-generation failures
0 resource-budget events
```

All four V0 knowledge components activated.

The inherited baseline's train+validation learned-preprocessing contamination was explicitly diagnosed and not relied upon. Chronological future validation was chosen after inspecting repeated customer observations and entity overlap. The run noted that validation mainly represents continuing customers and separately considered validation-only/new-customer evidence.

Two semantic imperfections remain ordinary behavior to score rather than tuning targets:

```text
the stale README claim "Each row represents one customer" was not converted into a separate explicit durable contradiction-correction object, although repeated monthly customer snapshots were operationally recognized;
pre-Phase-2 account_state_code timing was accepted from visible documentation rather than represented with especially strong epistemic qualification.
```

## `dev-p0-04` Phase 2 repair

Authoritative timing evidence established that `account_state_code` is generated after the churn outcome window and retrospectively backfilled.

P0 then:

```text
disputed the older README timing fact;
reopened and later superseded the seven-feature model decision;
invalidated Phase 1 evidence that depended on account_state_code;
invalidated the dependent Phase 1 performance claim;
created and satisfied targeted reassessment obligations;
preserved the unrelated accepted chronological validation-regime decision;
re-evaluated development models using only eligible features;
locked a replacement six-feature logistic model.
```

Replacement development evidence:

```text
logistic eligible operational: AUROC 0.68836, AP 0.22658, Brier 0.09173
logistic + snapshot_month: AUROC 0.68772
histogram gradient operational: AUROC 0.67833
histogram gradient + snapshot_month: AUROC 0.67934
```

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

## `dev-p0-04` final evaluation

The protected test was accessed only after final lock. The already locked pipeline was trained on all development data and evaluated once.

```text
n_test: 4,084
positives: 445
AUROC: 0.66004
average precision: 0.21232
Brier: 0.09304
```

Monthly AUROC ranged from 0.63736 to 0.69014.

Cohorts:

```text
seen in development: n=3,775, AUROC=0.65468
new to development: n=309, AUROC=0.72621
```

No development followed test feedback. The final report stated that final AUROC was below eligible-feature development validation, bounded claims to similar future monthly snapshots, and did not invent an operating threshold without a utility/intervention specification.

## Resource interpretation

Per-call totals:

```text
3,036
4,290
6,038
8,199
13,218
17,145
20,555
23,079
27,005
31,408
35,014
39,077
```

Cumulative usage ended at 228,064 tokens. Model-facing state views remained roughly 2.0k-10.0k characters.

This demonstrates P0 feasibility inside the frozen envelope, not efficiency parity. Relative to the B1 development mean:

```text
228,064 / 124,434 ~= 1.83x
```

The preregistered held-out median resource ratios and reliability thresholds remain decisive.

## P0 behavioral freeze

Full raw inspection found no experiment-invalidating mechanical defect.

Therefore ordinary P0 behavioral/controller logic is now **frozen for held-out H1/H2 execution**.

Do not change P0 merely to improve semantic scores, row-unit explicitness, pre-notice caution, resource use, model-authored relation quality, model-selection behavior, or final-report wording. Only a purely mechanical common protocol/runtime defect that would invalidate fair execution may justify a condition-neutral correction under the preregistered defect policy.

Do not run another P0 development trajectory.

## Remaining common pre-held-out engineering

Before any H1/H2 treatment run:

```text
1. enforce the same 24-call / 250k-token / 12-Python envelope for B0/B1;
2. implement the preregistered H1/H2 run scheduler and ordering;
3. implement batch blinded semantic judging;
4. implement blinded manual-adjudication routing;
5. aggregate semantic/resource/completion outcomes and apply continuation/falsification rules.
```

These tasks are common experimental controls, not P0 behavioral tuning.

## Relevant latest records

```text
docs/checkpoints/042_dev_p0_03_raw_diagnosis_and_reference_semantics_hardening.md
docs/checkpoints/043_p0_reference_semantics_validated_and_final_development_run_boundary.md
docs/checkpoints/044_final_p0_development_run_terminal_success.md
docs/checkpoints/045_dev_p0_04_full_inspection_and_p0_behavioral_freeze.md
```

## Current priority

**Implement and deterministically validate the common B0/B1 held-out resource envelope before building the held-out scheduler.**

H1/H2 remain untouched.