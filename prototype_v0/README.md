# Prototype V0

Prototype V0 is the first completed falsification experiment for the Autonomous Data Science System.

It tested whether a small explicit semantic architecture around a strong LLM materially improves reliability across a changing data-science project.

The central question was:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

## Final result

**Prototype V0 strongly falsified the current P0 design.**

P0 produced a small semantic improvement over the strongest simple control, B1, but the gain was far below the preregistered material-reliability threshold and came with severe token and completion cost.

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
Median model calls      16          16          13
Median Python            6           6           5
```

P0 improved the targeted semantic score over B1 by only `+0.05`. The preregistered material-reliability alternative required a gain of at least `+0.30` together with at least two additional strong-targeted passes, or at least two fewer critical failures.

P0 and B1 both had zero critical failure runs and zero strong-targeted passes.

P0 used `2.160x` B1's median tokens. Foundation 012 preregistered a strong-falsification signal when B1 matches or exceeds P0 reliability while P0 median tokens or calls are at least 25% higher.

Detailed final report:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

The conclusion is about the **current P0 implementation and this benchmark family**. It does not show that structured memory, dependency tracking, knowledge activation, or deterministic controls can never be useful in a broader system.

## Why V0 existed

The project deliberately avoided assuming that a richer architecture must be better than one strong LLM.

Three conditions used the same underlying treatment model, project files, Python capability, and common resource envelope:

```text
B0 = strong LLM + strong generic data-science instructions

B1 = B0 + the same four methodological concepts supplied statically

P0 = same strong LLM + typed project state + structured knowledge activation
     + prospective safeguards + dependency-aware repair
     + state-derived action selection
```

B1 was the critical architectural control. If P0 could not materially outperform B1 at acceptable cost, the structured mechanisms were not justified merely because they were more explicit.

That is what the held-out experiment found.

## Benchmark

Each run used a synthetic monthly customer-churn project. The task was to predict whether an active customer would churn during the next 30 days.

At the start of Phase 1, the treatment received:

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

The project contained several methodological traps and ambiguities.

### Row semantics

The stale README said each row represented one customer. The actual data contained monthly customer snapshots, so customer identifiers legitimately repeated across time.

### Generalization and validation

The target deployment regime was future monthly prediction with both continuing customers and newly entering customers. Repeated identifiers therefore did not mechanically imply a pure unseen-entity split.

### Inherited preprocessing contamination

The inherited baseline fitted learned preprocessing using both train and validation feature information before evaluating validation. Its score was therefore not clean comparative evidence.

### Prediction-time feature eligibility

One feature was initially documented as available at scoring time but was later revealed by an authoritative timing notice to be populated only after the outcome window closed and retrospectively backfilled.

The development-surface name was `account_state_code`; H1 used `lifecycle_flag`; H2 used `profile_code`.

### Protected final evaluation

The test set was reserved for one final evaluation after development choices were locked.

## Dynamic three-phase trajectory

```text
PHASE 1
provisional development
    -> understand semantics
    -> inspect inherited work
    -> choose validation
    -> develop provisional model

PHASE 2
authoritative timing change
    -> invalidate the post-outcome feature
    -> reconsider affected evidence and decisions
    -> preserve unrelated valid work
    -> rebuild legitimate development evidence

FINAL EVALUATION
    -> lock development
    -> access protected test once
    -> produce final conclusions
```

The experiment evaluated the complete reasoning trajectory, not only predictive accuracy.

## P0 architecture under test

P0 implemented a deliberately small semantic spine:

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

### State vocabulary

```text
ARTIFACT
FACT
ASSUMPTION
QUESTION
EVIDENCE
CLAIM
DECISION
OBLIGATION
ACTION
```

### Relation vocabulary

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

### Four methodological knowledge components

```text
K-INFO-001  Protected Final Evaluation
K-INFO-002  Learned Transformation Evaluation Boundary
K-INFO-003  Prediction-Time Feature Eligibility
K-VAL-001   Generalization-Regime Question
```

B1 received these same four concepts statically. P0 represented them as state-triggered structured components.

## Held-out design

Two frozen lexical/data variants were used:

```text
H1
seed: 811
identifier: member_key
time: scoring_period
post-outcome field: lifecycle_flag

H2
seed: 1601
identifier: account_ref
time: observation_period
post-outcome field: profile_code
```

The preregistered held-out sample was:

```text
H1: 5 B0 + 5 B1 + 5 P0
H2: 5 B0 + 5 B1 + 5 P0
Total: 30 retained treatment trajectories
```

All run ordering, model/provider configuration, budgets, failure handling, semantic rubric, judge procedure, and continuation/falsification rules were frozen before P0 implementation.

Authoritative protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

## Evaluation integrity

Treatment execution ended with:

```text
30 / 30 slots resolved
34 persisted attempts mechanically verified
34 integrity PASS
0 integrity FAIL
```

The semantic evaluation then used two independent condition-blind judge passes per retained trajectory:

```text
60 / 60 judge passes completed
0 provider failures
0 manual-adjudication cases
```

Judge agreement across S1-S10 was:

```text
288 / 300 exact = 96.0%
12 / 300 adjacent disagreements = 4.0%
0 extreme 0-vs-2 disagreements
```

All 60 SC1/SC2 comparisons agreed exactly and produced zero semantic-critical flags.

The complete blinded evidence was cryptographically frozen before condition decoding with aggregate SHA-256:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

## Semantic results

| Criterion | B0 | B1 | P0 |
|---|---:|---:|---:|
| S1 Row-unit correction | 1.00 | 1.00 | 1.00 |
| S2 Validation/generalization | 1.15 | 1.90 | 1.90 |
| S3 Inherited preprocessing contamination | 1.25 | 1.80 | 2.00 |
| S4 Pre-Phase-2 feature eligibility | 1.05 | 1.05 | 1.00 |
| S5 Timing-notice response | 2.00 | 2.00 | 2.00 |
| S6 Repair completeness | 2.00 | 2.00 | 2.00 |
| S7 Repair precision | 1.95 | 1.95 | 2.00 |
| S8 Claim validity | 1.95 | 2.00 | 1.95 |
| S9 Final validation rationale | 1.25 | 2.00 | 1.95 |
| S10 Final conclusions | 2.00 | 2.00 | 1.70 |

The main semantic lesson is that **B1 captured most of the benefit**.

```text
B0 -> B1 targeted gain: +0.26
B1 -> P0 targeted gain: +0.05
```

P0's clearest incremental improvement was S3, explicit treatment of the inherited learned-preprocessing boundary.

## P0 internal diagnostic result

The ten retained P0 trajectories were reviewed after unblinding.

Across them:

```text
state objects: 506
relations: 483
invalidated transitions: 14
reopened transitions: 24
repair-priority objects: 32
support-reassessment objects: 30
P0 state-control errors: 0
blocked P0 ACTION objects: 0
```

The dependency repair itself was precise. All 14 invalidations were materially tied to the post-outcome feature or model evidence that used it.

No false P0 action block occurred.

One internal validation-regime question was reopened more broadly than necessary and immediately re-resolved. The support-reassessment machinery also created avoidable internal obligation churn.

Knowledge activation was path-sensitive: K-INFO-003 activated in only 8/10 P0 runs because two runs inspected relevant information through Python instead of the table-metadata path expected by the trigger.

No held-out-specific P0 hard coding was found.

## What V0 taught the architecture

The correct response is simplification.

Strong current defaults are:

```text
one strong LLM reasoner
compact explicit methodological knowledge
instrumented execution and traceability
precise deterministic boundaries where justified
append-only experiment provenance
external mechanical verification
read-only observability separated from execution
```

Do not carry forward the following P0 mechanisms unchanged:

```text
full typed state resent every reasoning cycle
large always-on object/relation context
generic support-reassessment propagation
path-sensitive tag-trigger activation
universal dependency reopening machinery
full frontier representation that requires the entire P0 state context
```

Possible ideas for a smaller successor include compact question/claim/decision memory, incremental state deltas, selective state retrieval, event-driven repair, precise deterministic gates outside model context, and a lightweight unresolved-blocker frontier.

Those are next-stage hypotheses, not an already chosen architecture.

## What V0 does not show

V0 does not prove that one strong LLM plus a static prompt is sufficient for every data-science project.

The benchmark contains one major dynamic state change and relatively short trajectories. B1 was already very strong on repair.

A future benchmark should target cases where ordinary conversational memory and static knowledge are more likely to fail, such as multiple sequential state changes, longer dependency chains, selectively relevant knowledge, partially shared evidence, and meaningful under-propagation versus over-propagation consequences.

## Repository map

Read in this order:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
    Final V0 evidence, interpretation, hypothesis outcomes, and architectural consequences.

docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
    Why V0 exists and what mechanisms it was designed to test.

docs/foundations/011_prototype_v0_technical_specification.md
    Detailed V0 technical contract.

docs/foundations/012_preregistered_held_out_evaluation_protocol.md
    Frozen held-out design, semantic rubric, and continuation/falsification criteria.

docs/CURRENT_STATE.md
    Current project stage after V0.

docs/checkpoints/
    Append-only implementation and experiment provenance.
```

Implementation lives under:

```text
prototype_v0/src/ads_v0/
```

The main P0 implementation files are:

```text
p0.py
p0_controller.py
p0_schema.py
```

The evaluation infrastructure includes held-out execution, mechanical verification, semantic judging, blinded freeze/decoding, and read-only observability components.

## Local setup

From `prototype_v0/`:

```bash
python -m pip install -e ".[dev,openai]"
pytest
```

No further V0 treatment or judge inference should be run. Prototype V0 is a completed experiment and should be treated as immutable evidence for subsequent architectural design.
