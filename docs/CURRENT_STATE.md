# Current State

## Checkpoint

**Checkpoint:** 42  
**Date:** 2026-08-09  
**Development stage:** `dev-p0-03` fully diagnosed; persistent alias handling, supplemental-motivator tolerance, and obligation-support reassessment semantics corrected; deterministic re-validation pending  
**Implementation status:** All pre-P0 experimental controls remain frozen. The third real P0 development run materially improved context efficiency but again exhausted the 250,000-token envelope. Raw inspection showed that its critical failure was caused by failure to reach final lock, after three avoidable state-reference rejections and a redundant repair blocker created when an obsolete model decision stopped supporting the broad deliverable obligation. Generic controller/interface corrections are implemented and four regression tests were added. No held-out H1/H2 treatment run has occurred. The next step is local deterministic validation, expected at 54 tests.

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

## Baseline calibration

All six B0/B1 development trajectories completed and passed critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

The clearest repeatable B1 semantic advantage was explicit inherited learned-preprocessing diagnosis:

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

## P0 architecture under development calibration

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

The controller supports scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived motivators/frontier, blocking and repair priority, phase gates, dependency-aware reopening, append-only audit history, and a compact model-facing current-state projection.

## Real P0 development history

### `dev-p0-01`

```text
Completed: False
Budget exhausted: True
Calls: 10
Tokens: 250,279
Python: 2
Generation failures: 0
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
Generation failures: 0
Critical deterministic pass: True
```

Reached legitimate protected final evaluation after strong targeted repair. Only final reconciliation/reporting remained. Raw diagnosis found one temporary/canonical-ID handoff failure, more removable audit metadata, and a terminal budget-accounting edge case. Corrections were validated with 50/50 tests.

### `dev-p0-03`

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Calls: 14
Generation attempts: 14
Generation failures: 0
Input tokens: 250,015
Output tokens: 10,219
Total tokens: 260,234
Python attempts: 4
Critical deterministic pass: False
```

Exact position at termination:

```text
phase: PHASE_2_REVISED_DEVELOPMENT
phase_1_report: present
final_lock_report: absent
final_report: absent
```

Deterministic assertions:

```text
A0 PASS
A1 PASS
A2 PASS
A3 FAIL because no final lock existed
A4 FAIL because final lock was absent, although legitimate Phase 2 development re-evaluation occurred
```

The run again performed strong substantive Phase 1 and Phase 2 analysis, including explicit inherited-preprocessing diagnosis, future temporal validation, authoritative feature-timing repair, invalidation of old development evidence, and fresh eligible-feature model comparison.

## `dev-p0-03` context efficiency

Per-call totals:

```text
3,009
4,250
5,885
7,301
9,879
13,176
15,475
19,411
22,427
25,276
27,753
31,483
35,618
39,291
```

For the first twelve common positions, calls were approximately 13% to 40% cheaper than `dev-p0-02`, confirming that the second model-state compaction worked materially.

Model-facing state views ranged from about 2.0k to 9.7k characters.

## `dev-p0-03` reference-interface failures

Three rejected calls were caused by state-reference handling rather than missing analytical work:

```text
call 3: same-patch Q2 was listed as an extra motivator although valid pre-patch motivators were also present
call 6: earlier client ref F3 was reused instead of canonical F-0003
call 13: earlier client ref D4 was reused instead of canonical D-0004
```

Those rejected calls consumed:

```text
5,885 + 13,176 + 35,618 = 54,679 tokens
```

Corrections now implemented:

```text
accepted client refs persist as controller-level aliases to canonical state IDs;
later patch relations/status updates can use either canonical IDs or remembered aliases;
the private state view exposes the small persistent alias map;
a same-patch client ref may be a supplemental motivator when at least one valid pre-patch motivator already satisfies the frontier;
a same-patch-only motivator still cannot retroactively manufacture action justification.
```

These are state-interface corrections, not new methodological knowledge.

## `dev-p0-03` final-lock support-reassessment blocker

On call 14 the corrected final-lock patch superseded old model decision D-0003 and created replacement current evidence/decision. Generic SUPPORTS-loss handling then created:

```text
O-0006: Reassess O-0001 because supporting object D-0003 is no longer current.
priority:repair
```

Here O-0001 is the broad project deliverable obligation. Because O-0006 was created during the same patch, the model could not know its ID in advance and the final-lock gate blocked.

This is a type-semantics mismatch. SUPPORTS represents non-exclusive evidential support. Facts/assumptions/evidence/claims/decisions can require support sufficiency reassessment. An OBLIGATION's force is instead represented directly by OPEN/SATISFIED/BLOCKED status. Losing a decision that supported the deliverable should not create a second repair obligation about whether the original deliverable still exists.

The controller now closes support-loss reassessment objects whose target is an OBLIGATION before phase-gate evaluation. The audit trail retains their creation/closure. Real Phase 2 support-reassessment obligations targeting the obsolete model decision remain unchanged and must still be explicitly satisfied.

## Deliberately unresolved state-graph issue

The model authored a hard `DEPENDS_ON` edge from its Phase 2 timing question Q-0006 to old decision D-0003. Superseding D-0003 later reopened Q-0006 even though the question had already been answered. This did not cause the registered critical failure or a repair-priority block.

No automatic dependency rewrite is introduced from this single observation. Relation quality remains behavior to monitor rather than something silently corrected in a development-case-specific way.

## New regression coverage

Four tests were added:

```text
persistent client-ref alias resolution across later patches;
same-patch supplemental motivators with an existing valid pre-patch motivator;
rejection of same-patch-only retroactive motivators;
no open repair blocker when SUPPORTS loss targets an OBLIGATION.
```

Expected full suite:

```text
54 passed
```

## What remains unchanged

```text
B0/B1 prompts
four privileged knowledge components
P0 state object/relation vocabulary
P0 hard-dependency semantics
P0 prospective final-test gate
model and reasoning effort
provider continuation/all-turn context
H1/H2 frozen bundles
semantic rubric and judge
held-out ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
continuation/falsification thresholds
```

All three failed P0 development trajectories remain part of the record.

## Relevant latest records

```text
docs/checkpoints/039_dev_p0_02_raw_diagnosis_id_handoff_and_further_context_compaction.md
docs/checkpoints/040_p0_second_corrections_deterministically_validated.md
docs/checkpoints/041_third_real_p0_run_budget_exhaustion_terminal_record.md
docs/checkpoints/042_dev_p0_03_raw_diagnosis_and_reference_semantics_hardening.md
```

## Current priority

**Deterministically validate the generic `dev-p0-03` controller/interface corrections before any further paid P0 run.**

Immediate next action:

```text
git pull origin main
pytest
```

Expected result:

```text
54 passed
```

Do not run `dev-p0-04` or begin held-out H1/H2 before this validation is green and the implementation boundary is reviewed.
