# Foundation 012: Preregistered Held-Out Evaluation Protocol

**Date registered:** 2026-08-09  
**Protocol version:** `v0.1.0`  
**Registration boundary:** after B0/B1 development calibration and before P0 implementation

## Purpose

This foundation freezes the Prototype V0 held-out evaluation contract independently of P0 behavior.

Development calibration has already established that B0 and B1 are strong baselines, that static B1 knowledge improves some targeted semantic reasoning without guaranteeing activation, that protected-test discipline and Phase 2 repair are near ceiling on the development case, and that run-to-run resource demand is materially stochastic.

The held-out experiment must therefore test whether P0's structured state, knowledge activation, safeguards, dependency repair, and state-derived action selection add **reliable operational value beyond B1**, not whether P0 can reproduce behaviors the simpler baselines already perform well.

This protocol governs:

```text
held-out case construction
run counts and ordering
common treatment budgets
provider/infrastructure failure handling
semantic-evaluation rubric
blinded judge procedure
critical failure semantics
efficiency/resource measures
continuation and falsification criteria
```

No P0 implementation should be used to choose or revise these substantive rules.

---

## 1. Conditions remain unchanged

### B0

```text
strong LLM
+ Python and project artifacts
+ strong generic data-science instruction
+ free-form conversational project memory
```

### B1

```text
B0
+ the same four methodological concepts supplied statically in the prompt
```

The four concepts remain:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

### P0

P0 may add only the pre-specified V0 semantic machinery:

```text
minimal typed project state
four structured knowledge components
activation / applicability handling
prospective safeguard for precise protected-test access
simple state-derived runnable frontier
dependency-aware invalidation and reopening
append-only state-change history
```

P0 must use the same underlying treatment model and common project capabilities.

No hidden specialist reviewer, extra reasoning model, or uncounted LLM call may be added to P0.

---

## 2. Held-out benchmark variants

Two held-out surface variants are used. Both preserve the benchmark mechanism while changing lexical form and data seed.

### H1

```text
case_id: churn_v0_h1
surface_variant: held_out_h1
initial data seed: 811
customer identifier: member_key
time field: scoring_period
post-outcome field: lifecycle_flag
```

### H2

```text
case_id: churn_v0_h2
surface_variant: held_out_h2
initial data seed: 1601
customer identifier: account_ref
time field: observation_period
post-outcome field: profile_code
```

The underlying methodological mechanisms remain unchanged:

```text
repeated entities across time
future-facing monthly prediction
known plus newly entering entities
stale one-row-per-entity documentation
inherited learned-preprocessing contamination
post-outcome field initially documented as scoring-time information
authoritative Phase 2 timing correction
protected final test
```

### 2.1 Seed fallback rule

Held-out seeds are selected only by deterministic benchmark self-test validity, never by treatment performance.

For H1, attempt seed `811`. If the generated bundle fails any required benchmark self-test, increment the seed by one and generate again until the **first** fully passing bundle is obtained.

For H2, use the same rule starting at seed `1601`.

No treatment model may inspect a rejected candidate bundle. No predictive result, semantic score, or treatment behavior may influence seed selection.

The first passing H1 and H2 bundles must be generated and cryptographically fingerprinted before P0 implementation begins. Their hashes become part of the frozen experiment record.

---

## 3. Held-out run counts

The pre-specified sample remains:

```text
H1: 5 runs per condition
H2: 5 runs per condition
```

Therefore:

```text
B0: 10 held-out runs
B1: 10 held-out runs
P0: 10 held-out runs
Total: 30 treatment runs
```

The experiment is a falsification-oriented prototype, not publication-grade statistical inference. Results must be reported as run-level patterns, paired differences where meaningful, and descriptive resource distributions rather than overstated significance claims.

---

## 4. Pre-registered run ordering

Conditions are interleaved to reduce simple ordering and provider-time bias.

### H1 order

```text
replicate 1: B0, B1, P0
replicate 2: B1, P0, B0
replicate 3: P0, B0, B1
replicate 4: B0, B1, P0
replicate 5: B1, P0, B0
```

### H2 order

```text
replicate 1: P0, B0, B1
replicate 2: B0, B1, P0
replicate 3: B1, P0, B0
replicate 4: P0, B0, B1
replicate 5: B0, B1, P0
```

Every condition within a replicate receives the same frozen benchmark bundle and event timing semantics.

No run may be repeated merely because its methodology is poor, its score is disappointing, or its trajectory is unusually expensive.

---

## 5. Common treatment model configuration

All held-out conditions use:

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
Responses API strict Structured Outputs
multi-turn previous_response_id continuation
all-turn reasoning context
request timeout: 300 seconds
per-call output ceiling: 30,000 tokens
additional provider-generation retries: 2
```

The provider adapter must continue to disable hidden SDK retries so common retry/accounting logic remains observable.

If the registered model becomes unavailable before held-out execution, held-out evaluation must stop and a protocol amendment must be recorded. It must not silently substitute another treatment model.

---

## 6. Common held-out resource envelope

Development calibration observed a maximum of 19 successful model calls, 182,271 total observed tokens, and 8 Python actions in one behavior-evaluable B0 trajectory.

The held-out envelope adds explicit stochastic headroom without making resources unbounded.

### 6.1 Hard treatment limits

```text
maximum successful model calls: 24
maximum observed total tokens: 250,000
maximum Python execution attempts: 12
maximum output tokens per provider call: 30,000
maximum additional generation retries for one semantic turn: 2
Python execution timeout: 60 seconds
provider request timeout: 300 seconds
```

Every LLM call attributable to treatment/controller reasoning counts toward the same 24-call and token envelope, including P0 state-reasoning or repair calls.

Deterministic operations such as schema validation, relation traversal, state mutation after an already-authorized patch, trace writing, and benchmark gates do not consume LLM-call budget.

### 6.2 Total-token enforcement

Cumulative token usage is observable only after a provider attempt completes.

Therefore:

```text
if cumulative observed usage is already >= 250,000 before a new model call,
no new model call may begin;

if a completed provider call moves cumulative usage above 250,000,
that call remains part of the trajectory, the run is marked budget-exceeded,
and no further treatment model call may occur.
```

Observable token usage from failed provider attempts also counts.

### 6.3 Python-attempt accounting

Every `execute_python` attempt counts, including:

```text
successful execution
Python exception
runtime timeout
model-authored invalid code that reaches execution
```

A failed Python action is a behavioral/tool-execution event, not an infrastructure exemption.

### 6.4 Wall-clock time

Wall-clock runtime is recorded but is **diagnostic, not a hard treatment-failure criterion** in V0 because provider/network latency is partly external to treatment behavior and development calibration did not establish a stable latency distribution.

---

## 7. Infrastructure and replacement-run rules

The experiment distinguishes treatment behavior from infrastructure invalidity.

### 7.1 Non-behavior-evaluable provider failure

A run is non-behavior-evaluable if it terminates because of a provider/infrastructure generation failure before a usable treatment command is admitted, after the registered retry policy is exhausted.

Such a run:

```text
retains its resource log
is not given a methodological score
is replaced using the same condition, variant, and replicate slot
receives a new attempt identifier
```

At most two replacement attempts are allowed for one slot before held-out execution pauses for investigation.

### 7.2 Behavioral failures are not replaced

The following remain part of the scored trajectory:

```text
Python exceptions
Python timeouts
invalid analytical choices
poor action selection
budget exhaustion caused by treatment behavior
semantic mistakes
critical integrity failures
failure to complete within the common resource envelope
```

### 7.3 Common harness defect

If a genuine condition-neutral harness defect is discovered during held-out execution, affected runs are invalidated rather than selectively repaired.

A code fix must be documented, tested, and applied to all conditions. Any held-out block whose comparability was affected must be rerun for all conditions in that block.

Substantive benchmark, rubric, or treatment-prompt changes are not permitted as ordinary bug fixes.

---

## 8. Deterministic critical-integrity layer

The existing deterministic assertions remain primary and non-compensable.

A run has a deterministic critical integrity failure for any of:

```text
premature value-level final-test access
post-test development influenced by final-test feedback
final deployable model uses the post-outcome field after Phase 2
required legitimate development re-evaluation after feature invalidation is absent
invalid benchmark self-test / protected-test role registration
```

P0 prospective blocking is evaluated separately:

```text
an invalid action proposed but deterministically blocked is not an executed critical failure;
the attempted action and the successful block are both recorded.
```

P0 receives no safeguard credit on a run where neither baseline nor P0 proposes the invalid action.

---

## 9. Semantic scoring scale

Every semantic criterion is scored on the same anchored integer scale:

```text
0 = materially wrong, absent where required, or invalid
1 = acceptable/operationally correct but incomplete, implicit, or weakly justified
2 = explicit, correct, appropriately scoped, and methodologically strong
```

Critical integrity failures cannot be compensated by a high semantic average.

### S1. Row-unit correction

```text
0: stale one-row-per-entity interpretation remains consequentially accepted,
   or row semantics are used incorrectly in downstream reasoning.

1: treatment operationally infers repeated entity-period snapshots and behaves
   consistently with that structure, but the contradiction is not explicitly
   resolved as a durable project conclusion.

2: treatment explicitly resolves the stale documentation, states the actual
   entity-period observation unit, and uses that interpretation consistently.
```

### S2. Validation/generalization reasoning

```text
0: validation design is incompatible with the future-facing deployment regime,
   or repeated entities trigger an unjustified mechanical split rule.

1: a defensible temporal evaluation is used, but deployment/entity reasoning
   is only partial or implicit.

2: treatment explicitly relates validation to future deployment, timestamps,
   repeated entities, and the mixture of continuing and newly observed entities.
```

### S3. Inherited preprocessing contamination

```text
0: contaminated inherited validation evidence is treated as clean comparative
   evidence, or the treatment reproduces the learned-transformation violation.

1: treatment avoids relying on the inherited contaminated evidence and uses
   legitimate preprocessing, but does not explicitly diagnose the inherited
   evidence boundary violation.

2: treatment explicitly identifies the learned-transformation boundary
   violation and retires or repairs the inherited evidence accordingly.
```

### S4. Prediction-time feature eligibility before Phase 2

```text
0: treatment makes an unjustified timing claim, rejects/accepts the feature for
   the wrong reason, or ignores the evidence hierarchy.

1: feature is provisionally accepted from visible documentation or kept
   unresolved in a defensible way, but provenance/uncertainty is weakly stated.

2: treatment explicitly represents feature availability as an evidence-based
   assumption/question, respects current source authority, and avoids premature
   leakage certainty.
```

### S5. Response to authoritative timing notice

```text
0: notice is ignored, misread, or the illegitimate feature remains accepted.

1: feature is removed or constrained, but supersession/meaning is incompletely
   represented.

2: treatment explicitly recognizes the authoritative timing change and updates
   prediction-time eligibility accordingly.
```

### S6. Repair completeness

```text
0: materially affected models/evidence/claims remain trusted, or valid
   development evidence is not re-established before lock.

1: major repair occurs but at least one affected dependency is incompletely
   reconciled.

2: all materially affected work is reconsidered and legitimate development
   evidence is re-established before final lock.
```

### S7. Repair precision

```text
0: material under-propagation or broad unnecessary invalidation occurs.

1: repair is directionally correct but preservation/reopening boundaries are
   somewhat unclear or unnecessarily broad.

2: affected conclusions are reopened/repaired while unrelated valid work is
   deliberately preserved.
```

### S8. Claim validity

```text
0: final claims materially rely on invalidated/contaminated evidence or make
   unsupported causal/deployment assertions.

1: claims are mostly bounded but contain meaningful ambiguity or weak linkage
   to valid evidence.

2: claims depend only on current legitimate evidence and are appropriately
   limited by the observed generalization regime and uncertainty.
```

### S9. Final validation rationale

```text
0: rationale is invalid or materially unsupported.

1: rationale is defensible but incomplete or only partly connected to the
   intended deployment/generalization regime.

2: rationale clearly separates development/model-selection evidence from final
   evaluation and explains why the chosen validation represents intended use.
```

### S10. Final conclusions answer the project question

```text
0: final deliverable fails to answer the actual prediction task or depends on
   invalid methodology.

1: final deliverable adequately answers the task with a usable model/evidence
   summary.

2: final deliverable clearly answers the task, reports legitimate final
   evidence, and states decision-relevant limitations without inventing an
   unsupported threshold or causal conclusion.
```

---

## 10. Semantic critical triggers

In addition to deterministic failures, the blinded evaluator may flag a semantic critical failure when either condition is met:

### SC1. Invalid final-evidence dependency

A final model-selection or deployment-performance claim materially relies on evidence already established as invalid, contaminated, or superseded.

### SC2. Unresolved blocking semantic contradiction

A contradiction material to downstream validity remains unresolved while the treatment nevertheless makes a conclusion that requires that contradiction to be settled.

These triggers are non-compensable and require adjudication if the two judge passes disagree.

---

## 11. Blinded semantic-judge procedure

### 11.1 Judge model

The primary semantic evaluator uses a separately instantiated:

```text
model: gpt-5.6-terra
reasoning effort: high
```

Judge calls do not use treatment `previous_response_id` state and do not share context with one another.

Judge-resource usage is logged separately and is not charged to a treatment's resource envelope.

### 11.2 Condition-neutral judge input

The primary semantic judge receives only common external evidence:

```text
hidden evaluator manifest / acceptance contract
normalized project action trace and visible tool results
Phase 1 milestone report
final-lock report
final report
```

The judge must not receive:

```text
condition label
run identifier revealing condition
B0/B1/P0 system prompt
P0-only internal typed state
P0-only knowledge-activation logs
P0-only dependency graph
architecture-specific diagnostic metadata
```

P0 internal state is evaluated separately for architecture diagnostics and cannot improve the blinded common semantic score merely by existing.

### 11.3 Two independent passes

Every behavior-evaluable run receives two fresh independent judge passes.

Each pass returns:

```text
S1-S10 integer scores
SC1 and SC2 boolean flags
short evidence-grounded justification for each score
trajectory evidence references
```

The evaluator should request concise justifications, not hidden chain-of-thought.

### 11.4 Combining judge scores

For each criterion:

```text
exact agreement -> use the agreed score
adjacent disagreement (0 vs 1 or 1 vs 2) -> consensus score is arithmetic mean
extreme disagreement (0 vs 2) -> manual blinded adjudication
```

Any disagreement on SC1 or SC2 requires manual blinded adjudication.

Manual adjudication uses the same normalized evidence and rubric and remains blind to condition.

A criterion consensus may therefore take values:

```text
0.0, 0.5, 1.0, 1.5, 2.0
```

---

## 12. Judge calibration before P0

Before P0 implementation, the two-pass judge machinery must be run on the six already observed development baseline trajectories.

This calibration checks:

```text
whether the normalizer truly hides condition labels
whether rubric anchors can be applied consistently
whether critical-trigger disagreements occur
whether automated scores broadly correspond to the already documented
condition-neutral semantic evidence
```

Judge calibration may clarify wording that is demonstrably ambiguous, but it may not add new semantic criteria, privileged methodological knowledge, architecture-specific scoring credit, or change continuation thresholds in response to P0 because P0 does not yet exist.

If a substantive rubric change is unavoidable, Foundation 012 must be versioned and the change completed before P0 implementation.

---

## 13. Primary and diagnostic outcome vectors

No single scalar score is the sole authority.

### 13.1 Primary outcomes

For each run record:

```text
critical_integrity_pass
completed_within_budget
S1-S10 consensus vector
semantic_critical_flags
targeted_architecture_score
strong_targeted_pass
```

The `targeted_architecture_score` is the mean of:

```text
S1 row-unit correction
S2 validation/generalization reasoning
S3 inherited preprocessing contamination
S6 repair completeness
S7 repair precision
```

A `strong_targeted_pass` requires all five of those consensus scores to equal `2.0`.

### 13.2 Diagnostic outcomes

Also record:

```text
successful model calls
generation attempts and failures
input/output/reasoning/total tokens
Python execution attempts and failures
artifact reads
blocked invalid actions
false/unnecessary blocks
modeling actions later invalidated by Phase 2
repeated analyses after a concern was already sufficiently resolved
wall-clock runtime
final predictive metrics
P0 state-object / relation / activation / reopening counts
```

Final AUROC is project-utility evidence, not the primary architecture endpoint.

---

## 14. Budget exhaustion and completion

A run that exhausts the treatment resource envelope because of treatment behavior remains behavior-evaluable.

It is recorded as:

```text
completed_within_budget = false
budget_exhausted = true
```

If the final deliverable is absent, semantic criteria that require final evidence are scored from the actual incomplete trajectory and may receive zero where appropriate.

Budget exhaustion is not automatically labeled a methodological integrity failure, but it is a serious project-utility and efficiency failure.

---

## 15. Pooled and variant-specific comparison

Primary architectural comparison is P0 versus B1 because B1 controls for the same methodological knowledge being statically available.

B0 remains a secondary reference showing the value of static methodological prompting itself.

Results are reported:

```text
separately for H1
separately for H2
pooled across all 10 held-out runs per condition
```

No pooled improvement should be called robust if it is created entirely by one surface variant while P0 is materially worse than B1 on the other.

---

## 16. Pre-registered continuation criterion

Prototype V0 provides a continuation signal for structured architecture only if **all** conditions below hold.

### 16.1 Integrity

```text
P0 has no more total critical integrity failures than B1 across the 10 held-out runs.
P0 has no architecture-induced critical false block or critical over-invalidation failure.
```

### 16.2 Material reliability improvement

At least one of the following must hold:

```text
A. P0 has at least 2 fewer critical integrity failures than B1 across 10 runs.

OR

B. P0's pooled mean targeted_architecture_score exceeds B1 by at least 0.30
   on the 0-2 scale, AND P0 achieves at least 2 more strong_targeted_pass runs
   than B1 across the 10 held-out runs.
```

### 16.3 Cross-variant robustness

On neither H1 nor H2 may P0's mean targeted architecture score be more than `0.10` below B1.

### 16.4 Completion

```text
P0 completes at least 9 of 10 held-out runs within the registered treatment budget,
and its completion count is not more than one run below B1.
```

### 16.5 Acceptable resource cost

Using medians across the 10 pooled held-out runs:

```text
P0 total-token median / B1 total-token median <= 1.50
P0 successful-call median / B1 successful-call median <= 1.50
P0 Python-attempt median / B1 Python-attempt median <= 1.50
```

P0 may have at most one budget-exhausted run.

### 16.6 Architecture-induced friction

Noncritical architecture-induced false blocking or unnecessary broad reopening may occur in at most one of the ten P0 held-out runs.

Passing these thresholds is evidence to continue investigating structured architecture. It is not proof that the full Autonomous Data Science System has been validated.

---

## 17. Strong falsification and no-continuation outcomes

### 17.1 Strong falsification signal

Strong evidence against the current P0 design exists if any of the following occurs:

```text
P0 has more critical integrity failures than B1;
P0 introduces a critical architecture-induced false block or over-invalidation;
P0 produces architecture-induced false blocking/broad reopening in >= 2/10 runs;
P0 relies on held-out-case-specific hard coding;
B1 matches or exceeds P0's reliability while P0's median tokens or calls are
at least 25% higher than B1.
```

### 17.2 No demonstrated continuation signal

If P0 does not satisfy the continuation criterion but also does not meet a strong falsification condition, the V0 result is classified as **inconclusive / no demonstrated need for the architecture on this case family**.

The default response is not to expand the architecture. The project should either simplify P0 or design a new, harder falsification benchmark targeted at the unresolved mechanism before adding more system complexity.

---

## 18. Interpretation constraints

The following claims are prohibited from the V0 held-out experiment alone:

```text
that P0 is generally superior for all data-science projects
that a small AUROC difference validates the architecture
that a single clean P0 run establishes reliability
that static prompting is obsolete
that the full long-term system vision is validated
```

The experiment can support narrower claims about the tested semantic spine and benchmark family.

---

## 19. Freeze semantics

The following are now substantively registered before P0 implementation:

```text
benchmark mechanisms
held-out surface names
seed-selection rule
run counts
run ordering
treatment model
resource envelope
semantic dimensions
score anchors
critical triggers
judge-blinding rules
judge-combination rules
primary/diagnostic outcomes
continuation thresholds
falsification conditions
```

The next step is not P0 yet.

First:

```text
1. generate and self-test H1/H2 using the registered seed rule;
2. record fingerprints of the first passing bundles;
3. implement the condition-neutral two-pass semantic judge/normalizer;
4. calibrate that judge on the six development baseline trajectories;
5. record any non-substantive clarification required for judge consistency.
```

Only after those pre-P0 controls are complete should P0 implementation begin.
