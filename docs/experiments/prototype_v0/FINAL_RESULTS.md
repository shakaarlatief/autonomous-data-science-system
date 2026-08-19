# Prototype V0 Final Results

**Status:** Final held-out experimental result  
**Date:** 2026-08-19  
**Scope:** Prototype V0 only  
**Authority:** Final descriptive and interpretive record for the completed V0 experiment. The preregistered rules remain governed by `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.

## Executive conclusion

Prototype V0 provides a **strong falsification signal against the current P0 design**.

The structured P0 treatment produced a small and consistent semantic improvement over B1 on the targeted architecture score, but the improvement was far below the preregistered material-reliability threshold and came with severe token and completion costs.

The central pooled comparison is:

```text
B1 targeted architecture mean: 1.73
P0 targeted architecture mean: 1.78
P0 - B1:                    +0.05

B1 strong targeted passes: 0 / 10
P0 strong targeted passes: 0 / 10

B1 critical failure runs:   0 / 10
P0 critical failure runs:   0 / 10

B1 completed within budget: 10 / 10
P0 completed within budget:  3 / 10

B1 budget exhausted:         0 / 10
P0 budget exhausted:         7 / 10

B1 median total tokens: 120,564.5
P0 median total tokens: 260,370.0
P0 / B1 token ratio:          2.160
```

Foundation 012 requires a material reliability improvement of either at least two fewer critical failures, or a targeted-score gain of at least `0.30` together with at least two additional strong-targeted passes. P0 achieved neither.

The strong-falsification rule also states that strong evidence against the current P0 design exists when B1 matches or exceeds P0 reliability while P0 median tokens or calls are at least 25% higher. On the preregistered reliability dimensions, B1 and P0 have identical critical-failure counts and identical strong-targeted-pass counts, while P0's targeted-score gain is only `0.05`, far below the registered material-improvement threshold. P0's median token use is `2.160x` B1. This satisfies the strong-falsification condition.

This result falsifies the **current P0 implementation strategy on this benchmark family**. It does not establish that explicit state, dependency tracking, knowledge activation, or deterministic safeguards can never be useful in a broader Autonomous Data Science System.

---

## 1. Experimental evidence boundary

The V0 result is based on the complete preregistered held-out experiment:

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0: 10 retained runs
B1: 10 retained runs
P0: 10 retained runs
30 retained behavior-evaluable trajectories total
```

Treatment execution completed with:

```text
30 / 30 preregistered slots resolved
34 persisted attempts mechanically verified
34 mechanical integrity PASS
0 mechanical integrity FAIL
4 non-behavior-evaluable provider/interface attempts replaced under protocol
```

All 30 retained trajectories passed the registered deterministic A0-A4 layer.

The blinded semantic stage then completed with:

```text
30 blinded cases
2 independent judge passes per case
60 / 60 logical judge passes persisted
60 provider calls
0 provider failures
0 manual-adjudication cases
```

Two-pass agreement was:

```text
ordinary S1-S10 comparisons: 300
exact agreement:             288 / 300 = 96.0%
adjacent disagreements:       12 / 300 = 4.0%
extreme 0-vs-2 disagreements:  0

SC1/SC2 comparisons:           60
exact agreement:               60 / 60
critical disagreements:         0
```

The complete condition-blind semantic evidence was frozen before decoding with aggregate SHA-256:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

The frozen decoder-free archive was independently checked against its file manifest with zero mismatches before condition identities were revealed.

---

## 2. Pooled semantic results

| Criterion | B0 | B1 | P0 | P0 - B1 |
|---|---:|---:|---:|---:|
| S1 Row-unit correction | 1.00 | 1.00 | 1.00 | 0.00 |
| S2 Validation/generalization | 1.15 | 1.90 | 1.90 | 0.00 |
| S3 Inherited preprocessing contamination | 1.25 | 1.80 | 2.00 | +0.20 |
| S4 Pre-Phase-2 feature eligibility | 1.05 | 1.05 | 1.00 | -0.05 |
| S5 Timing-notice response | 2.00 | 2.00 | 2.00 | 0.00 |
| S6 Repair completeness | 2.00 | 2.00 | 2.00 | 0.00 |
| S7 Repair precision | 1.95 | 1.95 | 2.00 | +0.05 |
| S8 Claim validity | 1.95 | 2.00 | 1.95 | -0.05 |
| S9 Final validation rationale | 1.25 | 2.00 | 1.95 | -0.05 |
| S10 Final conclusions | 2.00 | 2.00 | 1.70 | -0.30 |

Targeted architecture score uses S1, S2, S3, S6, and S7:

```text
B0: 1.47
B1: 1.73
P0: 1.78
```

The B1 improvement over B0 is `+0.26`, while the additional P0 improvement over B1 is only `+0.05`.

This is a central architectural result. Most of the semantic improvement associated with the four methodological concepts came from making them explicitly available to the strong LLM in the simple B1 prompt. The more elaborate P0 state, activation, dependency, and action-selection machinery added only a small additional gain.

No condition produced a strong-targeted pass because S1 remained at `1.0` throughout the held-out pool.

No retained run in any condition received an SC1 or SC2 semantic critical flag.

---

## 3. Variant-specific robustness

The small P0 semantic advantage was consistent across both surface variants rather than being created by one benchmark wording.

```text
H1 targeted mean:
B1 = 1.70
P0 = 1.76
P0 - B1 = +0.06

H2 targeted mean:
B1 = 1.76
P0 = 1.80
P0 - B1 = +0.04
```

P0 therefore passes the preregistered cross-variant noninferiority requirement. The problem is not instability across H1 and H2. The problem is that the incremental gain is too small relative to complexity and cost.

---

## 4. Paired replicate comparison

Within each H1/H2 replicate, P0 and B1 saw the same frozen benchmark bundle and event semantics.

P0 minus B1 targeted-score differences were:

```text
H1 R1: +0.10
H1 R2:  0.00
H1 R3:  0.00
H1 R4:  0.00
H1 R5: +0.20

H2 R1:  0.00
H2 R2: +0.20
H2 R3:  0.00
H2 R4:  0.00
H2 R5:  0.00
```

Therefore:

```text
7 / 10 paired blocks: exact targeted-score tie
3 / 10 paired blocks: small P0 advantage
0 / 10 paired blocks: B1 targeted-score advantage
```

This supports a narrow interpretation: P0 contains mechanisms that can improve some semantic behavior, especially explicit diagnosis of inherited preprocessing contamination, but the observed improvement is not large enough to justify the architecture as implemented.

---

## 5. Resource and completion result

| Condition | Completed | Completed within budget | Budget exhausted | Median tokens | Median calls | Median Python |
|---|---:|---:|---:|---:|---:|---:|
| B0 | 10 / 10 | 10 / 10 | 0 / 10 | 122,544.5 | 16 | 6 |
| B1 | 10 / 10 | 10 / 10 | 0 / 10 | 120,564.5 | 16 | 6 |
| P0 | 6 / 10 | 3 / 10 | 7 / 10 | 260,370.0 | 13 | 5 |

P0/B1 median ratios:

```text
total tokens:              2.160
successful model calls:    0.813
Python execution attempts: 0.833
```

P0 therefore did **not** fail by taking more actions. It actually used fewer successful LLM calls and fewer Python executions than B1.

The failure was context cost per reasoning cycle.

P0 input context grew rapidly over successive calls. Across the ten retained P0 trajectories, median input tokens per successful call increased approximately as follows:

```text
call 1:   2,793
call 4:   7,710
call 8:  21,344
call 12: 36,029
call 14: 40,975
```

The model-facing `P0_STATE_VIEW` also grew from roughly 2,000 characters initially to roughly 9,000-10,000 characters late in a run, while provider continuation retained prior conversation context.

The current P0 representation therefore imposed a large repeated-context tax even though it reduced action count.

---

## 6. P0 architecture-specific diagnostic review

A separate post-unblinding diagnostic export was inspected for all ten retained P0 trajectories. It contained the complete P0 state, state history, knowledge activations, trace, conversation, milestones, summaries, and execution provenance for each retained run.

The export contained 100 covered trajectory files plus its manifest. All manifest SHA-256 values matched the uploaded bytes.

Aggregate structural observations across the ten P0 runs:

```text
P0 state objects:                     506
P0 relations:                         483
invalidated status transitions:        14
reopened status transitions:           24
repair-priority objects:               32
support-reassessment objects:          30
knowledge-component reopen events:      2
P0 state-control error events:           0
blocked ACTION objects:                  0
P0 Python-budget block events:           0
```

### 6.1 False blocking

No retained P0 trajectory contains a `P0_STATE_CONTROL_ERROR`, a blocked P0 ACTION object, or a P0 Python-budget block.

The only disallowed trace events are the seven registered resource-budget exhaustion markers.

Therefore:

```text
critical architecture-induced false blocks: 0 / 10
noncritical architecture-induced false blocks: 0 / 10
```

The prospective controller did not create observed false blocking on this benchmark.

### 6.2 Invalidation precision

The 14 INVALIDATED transitions were inspected individually.

They applied to evidence, claims, or assumptions that materially depended on `lifecycle_flag` or `profile_code`, or to model-comparison evidence produced from pipelines containing those fields.

No unrelated evidence or claim was invalidated merely because Phase 2 changed feature timing.

This agrees with the blinded external S7 result, where P0 received a pooled repair-precision score of `2.00`.

Therefore no critical over-invalidation failure is observed.

### 6.3 Reopening behavior

Most of the 24 REOPENED transitions were direct and appropriate consequences of feature invalidation:

```text
model-selection decisions containing the now-ineligible field;
feature-eligibility questions tied to those decisions;
questions about whether the authoritative timing notice changes the pipeline;
model-selection questions whose supporting decision was superseded.
```

One H2 R4 transition is a useful diagnostic warning. A claim tagged with both validation evidence and validation-regime semantics was invalidated because its model used `profile_code`. The tag-based knowledge-reopen logic consequently reopened the general validation-regime question even though the chronology/entity generalization regime itself had not changed. The next state patch immediately resolved the question with the explicit conclusion that feature revision did not change the established validation regime.

This is a real example of latent over-propagation in the current representation, but it did not block an action, invalidate unrelated external evidence, or cause an additional analysis beyond the legitimate feature-repair work.

A few other transitions changed an already OPEN question to REOPENED after a hard dependency broke. Those transitions are semantically redundant status churn rather than broad project reopening.

The registered architecture-friction threshold is therefore not exceeded. Conservatively, V0 contains at most one run with a noncritical over-broad reopening artifact and zero runs with behaviorally consequential false blocking.

### 6.4 Duplicate support-reassessment churn

The diagnostic state contains 30 support-reassessment obligations. Several target the top-level deliverable obligation and are deterministically closed as redundant because an obligation's lifecycle is represented directly by its own status.

This does not count as a false block or an externally consequential broad reopening, but it is implementation overhead and evidence that generic support-loss propagation creates avoidable internal state churn.

A future structured-memory design should not preserve this mechanism unchanged.

### 6.5 Knowledge activation coverage

Activation counts across ten P0 runs were:

```text
K-INFO-001 Protected Final Evaluation:              10 / 10
K-INFO-002 Learned Transformation Boundary:         10 / 10
K-VAL-001 Generalization-Regime Question:           10 / 10
K-INFO-003 Prediction-Time Feature Eligibility:      8 / 10
```

K-INFO-003 failed to activate in two runs because those trajectories learned schema/value information through Python rather than the specific table-metadata path used by the activation predicate.

The LLM still reasoned successfully about feature timing in those trajectories, but this exposes a brittleness in the current state-pattern activation design: semantically equivalent evidence paths can fail to trigger the same reusable knowledge component.

### 6.6 Held-out-specific hard coding

No held-out-case-specific hard coding was found in the P0 implementation.

The treatment code uses generic state types, generic methodological knowledge, and generic activation tags. Static inspection of `p0.py` and `p0_controller.py` found no occurrences of the held-out trap field names `lifecycle_flag` or `profile_code`; `p0.py` also contains no development trap name `account_state_code` or held-out identifier `member_key`.

The H1/H2 surface renaming therefore did not receive treatment-specific implementation branches.

---

## 7. Preregistered continuation criterion

Foundation 012 requires every continuation component to hold.

### Integrity

```text
P0 critical failures <= B1: PASS
P0: 0
B1: 0
```

No critical architecture-induced false block or over-invalidation was observed.

### Material reliability improvement

Registered alternatives:

```text
A. at least 2 fewer P0 critical failures than B1
OR
B. targeted mean gain >= 0.30 AND at least 2 additional strong-targeted passes
```

Observed:

```text
critical-failure difference: 0
P0 - B1 targeted mean: +0.05
strong-targeted-pass difference: 0
```

Result: **FAIL**.

### Cross-variant robustness

```text
H1 P0 - B1: +0.06
H2 P0 - B1: +0.04
```

Result: **PASS**.

### Completion

Required:

```text
P0 >= 9 / 10 completed within budget
and no more than one below B1
```

Observed:

```text
P0: 3 / 10
B1: 10 / 10
```

Result: **FAIL**.

### Resource cost

Required:

```text
P0/B1 median tokens <= 1.50
P0/B1 median calls <= 1.50
P0/B1 median Python <= 1.50
P0 budget-exhausted runs <= 1
```

Observed:

```text
tokens: 2.160  FAIL
calls:  0.813  PASS
Python: 0.833  PASS
budget exhausted: 7 / 10  FAIL
```

Result: **FAIL**.

### Architecture-induced friction

No false blocks were observed. One noncritical over-broad internal reopen artifact was identified conservatively, which is within the allowed maximum of one run.

Result: **PASS**, while retaining the implementation warning.

### Overall continuation result

**NO CONTINUATION SIGNAL.**

The current P0 architecture must not be expanded as though V0 supported it.

---

## 8. Strong-falsification classification

Foundation 012 states that any one of several conditions is sufficient for a strong falsification signal.

The first four architecture-specific conditions are not triggered:

```text
P0 more critical failures than B1: no
critical architecture-induced false block/over-invalidation: no
architecture-induced false blocking/broad reopening in >=2/10 runs: no
held-out-specific hard coding: no
```

The fifth condition is triggered:

> B1 matches or exceeds P0 reliability while P0 median tokens or calls are at least 25% higher than B1.

The preregistered reliability measures show:

```text
critical failure runs: B1 0 / 10, P0 0 / 10
strong targeted passes: B1 0 / 10, P0 0 / 10
targeted score: B1 1.73, P0 1.78, difference +0.05
registered material targeted improvement threshold: +0.30 plus strong-pass gain
```

The observed `+0.05` targeted-score difference is a small semantic advantage, not the registered material reliability improvement needed to distinguish P0 from a matched B1 reliability level.

Resource cost is:

```text
P0/B1 median tokens = 2.160
```

which is far above the 1.25 strong-falsification trigger.

The completion evidence makes the practical comparison even stronger:

```text
B1 completed within budget: 10 / 10
P0 completed within budget:  3 / 10
```

**Final V0 classification: STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

---

## 9. Hypothesis-level interpretation

### H1: typed structured state

Not supported as a material reliability improvement in V0.

P0 maintained rich typed state internally, but S1 row-unit correction remained `1.0`, identical to B0 and B1. The architecture did not convert the row-semantics issue into a stronger external conclusion.

The state trace is useful for provenance and inspection, but the always-on model-facing representation did not earn its cost.

### H2: state-triggered reusable knowledge activation

Not supported over static knowledge in its current form.

B1 already gained substantially over B0 by receiving the same four concepts statically. P0 added only a small further targeted-score gain, and K-INFO-003 activation itself was path-sensitive and absent in 2/10 P0 runs.

This suggests that compact static or selectively retrieved methodological knowledge is a stronger default than the current explicit activation mechanism.

### H3: prospective safeguards

Not positively identified by this benchmark.

No retained condition produced a protected-final-test critical failure, and P0 did not need to block a premature final-test action. The P0 gate also produced zero false blocks.

Therefore the mechanism appears operationally safe in V0 but its incremental benefit remains untested rather than demonstrated.

### H4: dependency-aware correction

Mechanically successful but not materially better than B1.

P0 repaired affected evidence precisely and achieved S6 = `2.00`, S7 = `2.00`. B1 was already at S6 = `2.00`, S7 = `1.95`.

The explicit dependency machinery therefore worked, but the simpler LLM workflow repaired the benchmark almost as reliably without the state cost.

### H5: state-driven action selection

Mixed mechanism result, negative system-level result.

P0 used fewer model calls and fewer Python actions than B1, which suggests the runnable-frontier idea may reduce action count.

However, the cost per call grew so much that the overall token budget failed in 7/10 runs. The current representation therefore converts a possible action-efficiency benefit into a much larger context-efficiency loss.

---

## 10. Architectural consequences

The correct response to V0 is **simplification, not expansion**.

The next system iteration should use B1-like reasoning as the reference baseline and preserve only mechanisms that have an independent reason to exist or can be tested more cheaply.

### Preserve as strong current defaults

```text
one strong LLM reasoner
compact explicit methodological guidance
instrumented execution and traceability
protected information boundaries where rules are precise
append-only experiment provenance
external mechanical verification
read-only observability separated from execution
```

The supervision, verification, freeze, and observability infrastructure are not part of the failed P0 semantic treatment. They proved useful for running and auditing the experiment and should not be discarded because P0 lost.

### Do not carry forward unchanged

```text
full typed project state resent every reasoning cycle
large always-on object/relation view
current generic support-reassessment propagation
current tag-driven knowledge activation predicates
current dependency reopening semantics as a universal mandatory layer
state-derived frontier machinery that requires the full P0 context representation
```

### Candidate ideas worth retesting in cheaper form

```text
compact question/claim/decision memory rather than a full ontology
incremental state deltas rather than resending the current graph
selective retrieval of only state relevant to the next decision
selective methodological knowledge retrieval rather than static full context or brittle trigger predicates
event-driven dependency repair only after material state changes
precise deterministic gates outside the LLM context for truly non-negotiable boundaries
a lightweight runnable frontier containing only unresolved blockers and next obligations
```

These are hypotheses for the next design stage, not accepted V1 architecture yet.

---

## 11. What V0 does not establish

V0 does **not** show that:

```text
explicit project memory is never useful;
dependency tracking can never outperform ordinary LLM reasoning;
knowledge activation is universally unnecessary;
deterministic safeguards are unnecessary;
one strong LLM plus a static prompt is sufficient for every data-science project;
the broader Autonomous Data Science System vision is falsified.
```

The benchmark has one dynamic feature-timing change, a relatively short trajectory, only four methodological knowledge components, and strong baselines that performed near ceiling on repair.

A harder future benchmark may expose failure modes in B1 that this case family did not.

The V0 evidence does establish that a richer architecture must earn its cost against a strong B1 baseline rather than being assumed beneficial because its internal state looks more systematic.

---

## 12. Recommended next experimental question

The next experiment should not ask whether the same P0 machinery can be tuned until it passes this benchmark.

A better next question is:

> What is the smallest low-overhead mechanism that improves reliability beyond B1 on project trajectories where ordinary conversational memory and static methodological prompting are expected to fail?

A useful next benchmark should stress one or more mechanisms that V0 did not discriminate strongly:

```text
multiple sequential authoritative state changes;
longer dependency chains;
several partially independent claims sharing evidence;
project facts that become stale at different times;
knowledge concerns that are relevant only conditionally and would be expensive to keep permanently in context;
longer trajectories where conversational recall becomes a real limitation;
repair where both under-propagation and over-propagation have meaningful consequences.
```

Any next structured candidate should have a prospectively measured context-cost budget so that a reliability gain cannot hide behind unbounded state repetition.

---

## 13. Provenance

Core preregistration:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Treatment completion:

```text
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
```

Blinded semantic execution and freeze:

```text
docs/checkpoints/090_blinded_semantic_judge_execution_complete.md
docs/checkpoints/092_blinded_semantic_consensus_freeze_implemented_pending_validation.md
docs/checkpoints/093_blinded_semantic_freeze_independently_verified_and_unblinding_authorized.md
```

Condition decoding:

```text
docs/checkpoints/094_post_freeze_condition_decoder_implemented_pending_validation.md
docs/checkpoints/095_decoded_semantic_results_reviewed_and_p0_diagnostics_prepared.md
```

The architecture-specific diagnostic export was reviewed after condition decoding and before this final classification was recorded.
