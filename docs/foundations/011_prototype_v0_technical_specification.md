# Foundation 011: Prototype V0 Technical Specification

## Purpose

This foundation translates the Checkpoint 10 falsification experiment into a concrete Version 0 technical specification.

The purpose is not to choose a production architecture. It is to make the first experiment implementable without quietly introducing unnecessary infrastructure.

The governing rule is:

> **Every Version 0 implementation choice should exist because it is needed to test a falsifiable architectural hypothesis.**

Prototype V0 should therefore remain a small Python experiment harness rather than an autonomous-agent platform.

The central experiment remains:

> **Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make the same strong LLM materially more reliable across a changing data-science project than strong simpler workflows?**

The three experimental conditions remain:

```text
B0
Strong LLM + Python + project artifacts + strong generic data-science instruction.

B1
Same as B0 + the same four methodological knowledge components supplied statically.
No typed project state, activation, prospective gate, or dependency-repair mechanism.

P0
Same LLM + same tools + typed project state + four structured knowledge components
+ activation/applicability + prospective safeguards + dependency-aware reopening
+ minimal state-derived action selection.
```

B1 remains the critical control because it tests whether better prompting alone is sufficient.

---

## 1. High-level runtime boundary

Version 0 should be organized around a common experiment harness rather than three separate bespoke environments.

```text
                         EXPERIMENT HARNESS
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
             B0                 B1                 P0
        generic LLM       static knowledge   structured runtime
```

The experiment harness owns:

```text
case generation
visible project artifacts
hidden evaluator truth
phase transitions
instrumented project access
run logging
resource accounting
evaluator assertions
semantic judging inputs
```

The experimental treatments should not own or modify evaluator truth.

---

## 2. Hard separation between visible project material and evaluator truth

Each generated case must contain two conceptually separate information spaces.

```text
SYSTEM-VISIBLE PROJECT WORLD
project brief
stale README
train / validation / test artifacts
inherited baseline code
later authoritative timing notice once released

EVALUATOR-ONLY WORLD
DGP parameters
true row semantics
true prediction timing
artifact roles
true feature timing
source-authority semantics
acceptance envelope
dynamic-event definitions
```

The treatment must not be able to browse evaluator-only material through ordinary file access or Python execution.

A weak implementation in which evaluator truth is placed in the same ordinary workspace and the LLM is merely instructed not to open it would invalidate the benchmark design.

The exact operating-system isolation mechanism remains a prototype convenience, but the information boundary is a methodological requirement.

---

## 3. Instrumented workspace interface

All three conditions should access the project through the same instrumented interface.

Conceptually the minimum capabilities are:

```text
list_artifacts()
read_text(artifact_id)
inspect_table(artifact_id, access_level=...)
execute_python(code, declared_input_artifacts=[...])
signal_phase_1_complete(report)
signal_final_model_locked(report)
submit_final_report(report)
```

The interface must log every artifact access and execution.

### 3.1 Artifact access levels

For Version 0 the important distinction is:

```text
METADATA
file identity
schema
column names
dtypes
shape

VALUE_LEVEL
rows
summary statistics
feature distributions
target prevalence
predictions
model evaluation
any computation using actual values
```

During development, metadata-level access to the protected final test artifact may be permitted, while value-level access is methodologically prohibited until final model lock.

### 3.2 Python execution

Python execution must operate only on explicitly declared project inputs.

A proposed execution therefore has a semantic boundary such as:

```text
ACTION
Run Python analysis.

Declared inputs:
train
validation

Runtime-visible inputs:
train
validation
```

Evaluator-only files must never enter the execution environment.

P0 may block an action before execution. B0 and B1 use the same interface but do not receive P0's prospective enforcement layer. If they request an invalid development-time access, the harness logs and permits it so that the evaluator can observe the failure.

This difference is deliberate because prospective enforcement is one of the architectural features under test.

---

## 4. Project phases

Version 0 needs only three practical project phases.

```text
PHASE 1: PROVISIONAL DEVELOPMENT
initial artifacts available
system investigates project and produces a provisional development position

PHASE 2: REVISED DEVELOPMENT
new authoritative CRM timing notice becomes visible
system must repair or reaffirm prior reasoning

FINAL EVALUATION
system explicitly locks development choices
protected final-test value access becomes legitimate
```

### 4.1 Phase 1 completion

The system decides when it has a provisional development position and emits `PHASE_1_COMPLETE` together with a condition-neutral milestone report.

The harness then reveals the Phase 2 timing notice.

A resource ceiling prevents a treatment from avoiding the dynamic event indefinitely.

The reveal is therefore milestone-based rather than tied to a fixed number of LLM calls.

### 4.2 Final model lock

After Phase 2 repair, the system emits `FINAL_MODEL_LOCKED` with a condition-neutral development report.

Only then is value-level final-test access methodologically legitimate.

After the first final-test value exposure, further model fitting, feature selection, validation redesign, threshold tuning, or other development changes count as test-feedback contamination unless the run explicitly abandons the final-test interpretation.

---

## 5. Synthetic case family

The first benchmark is a synthetic customer-month churn project.

### 5.1 Fixed conceptual dimensions

```text
months: 24
underlying customers: approximately 4,000
train period: months 1-16
validation period: months 17-20
test period: months 21-24
prediction target: churn during the next 30 days
prediction moment: beginning of the snapshot month
```

Customers enter at different months and remain observable until churn or the simulation horizon ends.

This creates repeated customer observations plus new customers entering during validation and test periods.

### 5.2 Customer entry distribution

The initial DGP uses a deliberately simple weighted entry distribution.

For months 1 through 8, each month receives relatively high entry mass. Months 9 through 16 receive moderate mass. Months 17 through 20 receive lower but nonzero mass. Months 21 through 24 retain a smaller new-entry mass.

A concrete Version 0 weight vector is:

```text
months 1-8:   0.075 each before normalization
months 9-16:  0.035 each before normalization
months 17-20: 0.020 each before normalization
months 21-24: 0.010 each before normalization
```

The vector is normalized before sampling.

The purpose is not realism. It is to ensure that later periods contain both previously observed customers and new entrants.

### 5.3 Persistent customer heterogeneity

Each customer receives a latent persistent effect:

\[
u_i \sim N(0, 0.65^2).
\]

This creates meaningful within-customer dependence without making customer identity itself a target feature.

### 5.4 Plan tier

Each customer receives one plan tier:

```text
basic:    0.45
standard: 0.40
premium:  0.15
```

Indicative monthly-charge centers are:

```text
basic:    28
standard: 48
premium:  76
```

with customer-level and month-level noise.

### 5.5 Legitimate monthly features

The visible modeling table should contain at least:

```text
customer_id
snapshot_month
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
account_state_code
churn_next_30d
```

The legitimate predictors are generated before the target outcome.

One concrete DGP is:

\[
\lambda^{support}_{it}
=
\exp(-0.25 + 0.25u_i + 0.08\sin(2\pi t/12)),
\]

with

\[
support\_tickets\_90d_{it}
\sim Poisson(\lambda^{support}_{it})
\]

and a practical cap of 8.

For late payments:

\[
p^{late}_{it}
=
\sigma(-2.0 + 0.55u_i + 0.25I(plan_i=basic)),
\]

\[
late\_payments\_90d_{it}
\sim Binomial(3,p^{late}_{it}).
\]

Usage change is generated as:

\[
usage\_change\_30d_{it}
\sim N(-0.06u_i - 0.015(t-12), 0.28^2).
\]

Monthly charge is approximately:

\[
monthly\_charge_{it}
=
base(plan_i)
+ customer\_charge\_noise_i
+ N(0,1.5^2)
+0.08t,
\]

with

\[
customer\_charge\_noise_i \sim N(0,3^2).
\]

Tenure is deterministic:

\[
tenure\_months_{it}=t-entry_i+1.
\]

### 5.6 Churn outcome

The next-30-day churn probability is generated with a logistic model:

\[
P(Y_{it}=1)=\sigma(\eta_{it}),
\]

where a concrete Version 0 specification is:

\[
\begin{aligned}
\eta_{it} ={}& -2.60
+0.34\,support_{it}
+0.55\,latepay_{it}
-1.15\,usagechange_{it} \\
&+0.012(monthlycharge_{it}-48)
-0.11\log(1+tenure_{it})
+0.55u_i \\
&+plan\_effect_i
+0.018(t-12)
+0.08\sin(2\pi t/12).
\end{aligned}
\]

The plan effect is initially:

```text
basic:     +0.18
standard:   0.00
premium:   -0.12
```

The current parameterization is intended to produce roughly 10 percent monthly churn prevalence and a nontrivial but not trivial legitimate prediction problem.

These numerical choices are benchmark parameters, not system architecture.

Before held-out evaluation, a benchmark self-test must confirm that prevalence and signal strength remain inside pre-specified acceptable ranges across the chosen case seeds.

### 5.7 Absorbing churn

After a customer churns in month `t`, that customer should not produce later monthly snapshots.

This yields a more coherent longitudinal project world and prevents unrealistic post-churn observations.

---

## 6. Post-outcome feature used for the Phase 2 correction test

`account_state_code` is deliberately generated after observing the churn outcome for the same row.

It has opaque categories:

```text
S1
S2
S3
```

A suitable initial conditional distribution is:

```text
If churn_next_30d = 1:
S1 0.30
S2 0.38
S3 0.32

If churn_next_30d = 0:
S1 0.50
S2 0.32
S3 0.18
```

This makes the field useful enough to influence model development but not a deterministic copy of the target.

Its illegitimacy is therefore a provenance/timing issue rather than a perfect-correlation trick.

The field name and category labels are intentionally semantically opaque.

Held-out surface variants should rename this field while preserving the underlying mechanism.

---

## 7. Visible project artifacts

The generated visible case contains:

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

The Phase 2 notice is withheld initially and later added to the visible project.

### 7.1 `project_brief.md`

The brief should establish only the project information that must be authoritative from the beginning.

It should state substantially:

```text
Build a model that scores active customers at the beginning of each month
for the probability of churn during the following 30 days.

Use the provided development data to choose and validate the approach.
The final test set is reserved for final evaluation and should not influence
development choices.

The intended output is a defensible model, validation rationale,
and final performance report.
```

It should not reveal the hidden row-unit contradiction or the post-outcome timing issue.

### 7.2 Stale `README.md`

The README deliberately contains two stale statements.

It says substantially:

```text
Each row represents one customer.
```

and describes `account_state_code` as:

```text
Current CRM lifecycle classification available during monthly scoring.
```

The README should otherwise describe the table reasonably well so that it is not an obviously malicious artifact.

The benchmark tests whether the system treats documentation as evidence rather than unquestionable truth.

### 7.3 `baseline_model.py`

The inherited baseline should contain an explicit learned-preprocessing information-boundary violation.

Conceptually:

```python
X_preprocessor_fit = concat(X_train, X_validation)
preprocessor.fit(X_preprocessor_fit)

X_train_transformed = preprocessor.transform(X_train)
X_validation_transformed = preprocessor.transform(X_validation)

model.fit(X_train_transformed, y_train)
validation_predictions = model.predict_proba(X_validation_transformed)
```

A scikit-learn `ColumnTransformer` with `StandardScaler` and `OneHotEncoder` is sufficient.

The baseline may include `account_state_code` because the initial visible README says it is a scoring-time field.

The benchmark should not artificially inflate the numerical impact of the preprocessing contamination. The methodological violation matters even if the metric difference is small.

---

## 8. Phase 2 authoritative notice

After `PHASE_1_COMPLETE`, the harness reveals an artifact such as:

```text
crm_field_timing_notice.md
```

It should state substantially:

```text
Current CRM field-timing notice

account_state_code is generated only after the monthly outcome window closes.
The value is retrospectively backfilled into the analytical warehouse.
It is not available at the beginning-of-month scoring time.

This notice supersedes older README descriptions of this field's availability.
```

The notice is intentionally unambiguous and authoritative for field timing.

Version 0 is testing dependency-aware correction, not difficult authority arbitration.

---

## 9. Hidden evaluator manifest

The case generator should emit a machine-readable evaluator manifest from the same underlying case specification that generated the visible artifacts.

A minimal conceptual structure is:

```text
case_id
case_version
surface_variant
data_seed

world_truth:
    row_unit
    prediction_moment
    target_definition
    deployment_generalization
    feature_timing
    artifact_roles

source_authority:
    project_brief
    README
    timing_notice

dynamic_events:
    phase_2_notice

acceptance_contract:
    critical_failures
    mandatory_behaviors
    acceptable_alternatives
    optional_opportunities
```

The generator, visible artifacts, timing notice, and hidden evaluator truth should be derived from one case specification so they cannot silently drift apart.

### 9.1 Generated world facts versus semantic authority facts

The manifest should distinguish:

```text
GENERATED WORLD FACTS
for example account_state_code is generated after Y

SEMANTIC / SOURCE-AUTHORITY FACTS
for example the timing notice supersedes the stale README for field timing
```

This distinction mirrors the project's broader source-aware epistemic model.

---

## 10. Benchmark self-tests

Before any LLM run, a generated case instance must pass deterministic self-tests.

At minimum the self-tests should verify:

```text
customer_id repeats
(customer_id, snapshot_month) is unique
train contains only months 1-16
validation contains only months 17-20
test contains only months 21-24
new customers enter during validation and test
both known and newly entering customers appear in later periods
account_state_code is generated from post-outcome information
README row-unit statement conflicts with generated structure
README field-timing statement conflicts with evaluator truth
Phase 2 notice agrees with evaluator truth
baseline_model.py fits learned preprocessing using validation information
test is registered as protected final evaluation
outcome prevalence falls inside the accepted benchmark range
legitimate features contain nontrivial predictive signal
account_state_code improves development prediction enough to be behaviorally relevant but is not a perfect target proxy
```

If any self-test fails, the case instance should not be used for model evaluation.

---

## 11. Common condition-neutral milestone reports

All three conditions must produce the same external milestone report structure so the evaluator can compare them without relying on P0's richer internal state.

### 11.1 Phase 1 report

The report should contain:

```text
problem understanding
observation-unit interpretation
validation approach and rationale
current preferred model or candidate
current evidence summary
material unresolved issues
readiness for Phase 2
```

### 11.2 Final development report

Before test access, the system should report:

```text
what changed after the timing notice
final validation design and rationale
final deployable feature/model position
current valid development evidence
remaining limitations
readiness to lock development choices
```

### 11.3 Final report

After legitimate final evaluation:

```text
final model summary
final test evidence
claim scope
material limitations
important project-state revisions
```

These reports are evaluation artifacts, not a substitute for P0's internal project state.

---

## 12. Common action and trace model

Every treatment should interact with the harness through actions that are logged in a common trajectory.

A minimal action request contains conceptually:

```text
action_id
run_id
step
kind
purpose
input_artifacts
operation
```

P0 additionally supplies:

```text
motivated_by
```

where `motivated_by` references current P0 questions, obligations, reopened decisions, or deliverable needs.

The common harness trace should record at least:

```text
event_id
case_id
condition
run_id
step
event_type
action_id
artifacts_requested
artifacts_accessed
access_level
allowed_or_blocked
execution_result_reference
model_call_usage
runtime
```

P0 may produce an additional internal diagnostic trace containing state patches and dependency events, but primary treatment scoring should rely on condition-neutral observable behavior wherever possible.

---

## 13. Minimal P0 state model

Prototype V0 keeps the nine state object types from Checkpoint 10:

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

### 13.1 Common object envelope

Each state object should contain at least:

```text
id
type
scope
content
source_refs
created_step
updated_step
```

The exact Python class implementation remains a convenience.

### 13.2 Typed status vocabularies

Version 0 should not force one universal status enum.

A practical minimal vocabulary is:

| Object type | Candidate Version 0 statuses |
|---|---|
| ARTIFACT | AVAILABLE, PROTECTED, SUPERSEDED |
| FACT | ACTIVE, DISPUTED, SUPERSEDED |
| ASSUMPTION | PROVISIONAL, SUPPORTED, INVALIDATED |
| QUESTION | OPEN, RESOLVED, BLOCKED, REOPENED |
| EVIDENCE | CURRENT, INVALIDATED, STALE |
| CLAIM | PROVISIONAL, SUPPORTED, WEAKENED, INVALIDATED |
| DECISION | PROVISIONAL, ACCEPTED, REOPENED, SUPERSEDED |
| OBLIGATION | OPEN, SATISFIED, BLOCKED |
| ACTION | PROPOSED, ALLOWED, BLOCKED, EXECUTED, FAILED |

This vocabulary is a Version 0 test instrument, not the final system ontology.

### 13.3 Relations

Version 0 keeps only:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Relations should be explicit records rather than implicit text.

Example:

```text
E-012 SUPPORTS C-003
D-005 DEPENDS_ON A-017
```

The distinction between `DEPENDS_ON` and `SUPPORTS` is especially important for repair semantics.

---

## 14. State history

Version 0 should preserve an append-only change log alongside current state.

A minimal change record contains:

```text
step
object_id
old_status_or_value
new_status_or_value
reason
trigger_or_source
```

For example:

```text
step 14
A-017
PROVISIONAL -> SUPPORTED
reason: README describes field as scoring-time information

step 32
A-017
SUPPORTED -> INVALIDATED
reason: authoritative timing notice supersedes stale README
```

This is an audit history, not a commitment to event-sourcing architecture.

---

## 15. Dependency-aware repair algorithm

Version 0 must not blindly invalidate every descendant of a changed state object.

The minimum repair logic is:

```text
UPSTREAM CHANGE
      |
      v
find directly and transitively affected objects
      |
      v
classify dependency semantics
      |
      +--> hard DEPENDS_ON relationship
      |       -> reopen / invalidate dependent object as appropriate
      |
      +--> SUPPORTS relationship
              -> remove invalid support
              -> reassess whether remaining support is sufficient
```

Dependency discovery can be deterministic.

Materiality and sufficiency reassessment may use the LLM.

This hybrid is intentional.

### 15.1 Repair precision

The evaluator should distinguish:

```text
UNDER-PROPAGATION
material dependents remain trusted

CORRECT PROPAGATION
affected objects reopen while unrelated valid state remains current

OVER-PROPAGATION
unrelated valid state is unnecessarily discarded
```

---

## 16. P0 reasoning calls and state patches

The model should not be asked to reconstruct project state from conversation memory.

Each P0 reasoning cycle receives a compact current-state view containing the relevant active facts, assumptions, questions, obligations, evidence, claims, decisions, artifacts, and newly observed information.

A single semantic reasoning call should normally return:

```text
state objects to create
state objects to update
relations to add/remove
next action proposal
short human-readable rationale
```

The system should preserve concise rationale and provenance, not hidden chain-of-thought reasoning.

Deterministic code should handle:

```text
schema validation
ID integrity
relation integrity
hard action gates
dependency traversal
logging
```

This keeps P0's model-call overhead from becoming unnecessarily large.

---

## 17. Minimal reusable knowledge representation

Version 0 contains only four manually authored components.

### K-INFO-001 Protected Final Evaluation

```text
Role:
hard methodological invariant / prospective safeguard

Applicability:
a proposed action requests value-level access to an artifact
whose role is protected final evaluation while development choices
remain unlocked

Required behavior:
block the action

Repair:
use validation or other legitimate development evidence instead
```

This is the first deterministic prospective gate.

### K-INFO-002 Learned Transformation Evaluation Boundary

```text
Role:
hard methodological invariant

Meaning:
a learned transformation participating in an evaluation must be fitted
only from information legitimate for that evaluation's training portion

Version 0 enforcement:
interpretive inspection of inherited baseline code

Output when violated:
mark inherited evaluation as invalid for model comparison
create repair obligation for legitimate re-evaluation
```

Version 0 does not attempt arbitrary static program analysis.

### K-INFO-003 Prediction-Time Feature Eligibility

```text
Role:
hard methodological principle with semantic applicability

Question:
Would the information represented by a proposed feature actually exist
at the represented prediction moment?

Output:
feature-eligibility assumption/question and, when illegitimacy is established,
constraint plus downstream revalidation obligations
```

### K-VAL-001 Generalization-Regime Question

```text
Role:
question template / decision principle

Activation hints:
repeated entities
+ timestamps
+ future-facing prediction objective

Question:
What generalization regime should validation estimate?

Important constraint:
repeated IDs do not mechanically imply pure unseen-entity validation
```

### 17.1 Static B1 knowledge

B1 receives the complete semantic content of all four components upfront in ordinary prompt prose.

P0 receives the same substantive knowledge as structured components with dynamic activation/applicability.

This intentionally gives B1 strong knowledge access so P0 must demonstrate value from operationalization rather than from possessing better methodology.

---

## 18. Minimal activation semantics

With only four components, Version 0 does not need embeddings or semantic retrieval infrastructure.

Hard prospective safeguards can be checked directly.

Interpretive activation can use simple state patterns.

For example:

```text
repeated customer fact
+ timestamp fact
+ future prediction objective
        -> K-VAL-001 becomes relevant
```

Knowledge instances must be idempotent for a given scope.

If `K-VAL-001` has already instantiated the project-level validation-regime question, observing repeated IDs again must not create duplicate questions.

If the question was resolved and a material dependency changes, the existing scoped instance should reopen rather than creating a duplicate concern.

---

## 19. Minimal runnable-frontier behavior

Version 0 does not need a planner or numeric prioritization engine.

Every P0 action should reference at least one current motivator:

```text
open blocking question
open obligation
reopened decision
deliverable need
```

Priority is qualitatively:

```text
hard blocker
    -> blocking semantic/methodological question
    -> repair obligation
    -> high-value optional analysis
```

The LLM may choose among legitimate ties.

This is enough to test whether explicit project state reduces premature or orphaned work.

---

## 20. Deterministic evaluator assertions

Wherever possible, the evaluator should use direct trace evidence rather than LLM judging.

Version 0 should deterministically check at least:

### A1. Premature final-test access

A critical integrity failure occurs if value-level test access happens before `FINAL_MODEL_LOCKED`.

### A2. Post-test development

After the first legitimate final-test value exposure, subsequent model fitting, feature selection, threshold tuning, validation redesign, or comparable development changes count as test-feedback contamination.

### A3. Final feature legitimacy

After the authoritative timing notice, the final deployable model/evaluation must not use `account_state_code` or a direct renamed equivalent in held-out variants.

### A4. Repair re-evaluation

If a Phase 1 model or evidence used the now-illegitimate field, a legitimate development evaluation without that field must occur before final model lock.

### A5. Test-role registration

The generated case must register test as protected final evaluation in evaluator truth and P0 artifact state.

### A6. Case self-test validity

The generated benchmark instance must have passed all benchmark self-tests before the run starts.

Other important criteria remain semantic rather than deterministic.

---

## 21. Semantic evaluator criteria

A blinded semantic evaluator should assess condition-neutral trajectories and milestone reports for at least:

```text
row-unit correction
validation/generalization reasoning
handling of inherited preprocessing contamination
appropriate uncertainty about account_state_code before Phase 2
material response to the timing notice
repair completeness
repair precision
claim validity
quality of final validation rationale
whether final conclusions answer the actual project question
```

The evaluator receives hidden benchmark truth and the behavioral contract but should not receive the condition label.

Critical semantic criteria should initially receive at least two independent judge passes.

Disagreement during calibration triggers manual adjudication and possible evaluator-rule clarification.

Held-out adjudication rules must be frozen before held-out runs begin.

A single opaque judge call should not be the only authority on whether P0 succeeds.

---

## 22. Acceptance-envelope semantics

The evaluator should encode methodological outcomes rather than one exact workflow.

For example, after the timing notice the requirement is not:

```text
Expected action: drop account_state_code.
```

It is:

> **The final deployable model and the evidence supporting it must not depend on information established to be unavailable at prediction time.**

Dropping the feature is one valid repair. Reconstructing a legitimate pre-prediction version would also be valid if the project made that possible.

Similarly, repeated customers should require deployment-aware generalization reasoning rather than one mandatory `GroupKFold` procedure.

---

## 23. Critical failures versus mandatory behaviors

Version 0 should separate non-compensable integrity failures from ordinary quality criteria.

Candidate critical failures include:

```text
premature value-level test access
final deployable model still uses the post-outcome field after Phase 2
post-test development influenced by final-test feedback
final report presents invalid/contaminated evidence as independent final evidence
```

Mandatory but non-binary reasoning obligations include:

```text
resolve or correctly represent row-unit contradiction
choose a defensible validation/generalization interpretation
avoid relying on contaminated inherited baseline evidence
respond materially to the Phase 2 notice
re-establish valid development evidence after material invalidation
keep final claims within valid evidence
```

Optional quality opportunities should not become hidden mandatory checklist items.

---

## 24. Resource parity and instrumentation

Every run should record common cost measures:

```text
LLM calls
input tokens
output tokens
Python executions
tool operations
wall-clock runtime
artifact reads
blocked actions
```

P0 additionally records diagnostic architecture overhead:

```text
state objects created
state updates
relations created
objects reopened
knowledge activations
knowledge deduplication events
```

B0/B1 do not receive equivalent project-state machinery merely for logging fairness.

The experiment harness may keep neutral external trace logs for all conditions.

Calibration should establish a comparable maximum budget envelope for:

```text
model calls
total tokens
Python actions
wall time
```

The held-out budget is frozen before held-out evaluation.

P0 may choose a different distribution of calls within the same overall envelope.

---

## 25. Efficiency measures

Version 0 should distinguish total effort from unjustified effort.

Useful diagnostic quantities include:

```text
actions executed before a critical methodological issue is detected
modeling work later invalidated by a discovered issue
repeated analysis after a concern was already sufficiently resolved
blocked invalid actions
false or unnecessary blocks
```

The goal is not minimum action count.

The goal is appropriate effort conditional on project state.

---

## 26. Experimental seeds and surface variants

The benchmark should distinguish:

```text
data_seed
surface_variant
LLM run index / controllable model seed where available
```

The initial protocol remains:

```text
Development calibration case:
3 runs per condition

Held-out H1:
5 runs per condition

Held-out H2:
5 runs per condition
```

Held-out variants preserve the underlying failure mechanisms while changing names, documentation wording, seeds, and nonessential numerical details.

Examples include:

```text
customer_id -> member_key -> account_ref
snapshot_month -> scoring_period -> observation_period
account_state_code -> lifecycle_flag -> profile_code
```

The development case is not evidence of generalization after P0 has been tuned on it.

---

## 27. Quantitative continuation criteria

The evaluator and experiment harness should support a pre-registered continuation decision after calibration.

The exact numeric thresholds should be frozen after calibration and before H1/H2.

Calibration is allowed to:

```text
remove ambiguous evaluator rules
verify case difficulty
choose a viable common resource envelope
verify semantic-judge consistency
fix implementation defects
```

Calibration must not be used to tune P0 against held-out cases.

Strong evidence against P0 remains:

```text
B1 matches P0 on critical integrity and repair behavior
while using materially less cost/complexity
```

or P0 introduces systematic:

```text
false blocking
duplicate obligations
over-invalidation
case-specific hard coding
```

The strongest continuation evidence remains a reproducible held-out reduction in critical methodological failure and stale-conclusion persistence without unacceptable cost.

---

## 28. Provider-neutral model interface

The first implementation should expose a minimal model abstraction such as:

```text
generate(system_instruction, conversation_state, response_contract)
```

Provider choice belongs in experiment configuration.

B0, B1, and P0 must use the same underlying model within each paired experiment.

The semantic evaluator should preferably be separately instantiated and blinded. Whether it uses the same provider or a different strong model can remain a calibration choice, but judge provenance must be logged.

---

## 29. Repository boundary for Version 0

Prototype implementation should be isolated from the conceptual repository documents so disposable experiment code is not mistaken for the final architecture.

A suitable provisional boundary is:

```text
prototype_v0/
    README.md
    case_spec/
    src/
    tests/
    configs/
    results/
```

Within `src`, responsibilities can remain small and explicit:

```text
case generation
workspace / trace harness
evaluator
model interface
B0/B1 treatments
P0 state/knowledge/controller
experiment runner
```

The exact file layout can evolve during implementation.

Raw run artifacts may be large or contain redundant model traces, so the repository should eventually distinguish committed experiment summaries from disposable/generated run outputs.

No production package architecture is implied by this prototype layout.

---

## 30. Implementation sequence

The implementation order should protect the experiment from retrospective benchmark design.

```text
1. deterministic synthetic DGP
2. visible artifact generation
3. hidden evaluator manifest
4. Phase 2 authoritative notice
5. benchmark self-tests
6. instrumented workspace and common trace
7. deterministic evaluator assertions
8. B0 runner
9. B1 static-knowledge runner
10. P0 state representation
11. P0 knowledge components and action gate
12. P0 dependency repair and control loop
13. paired experiment runner
14. semantic evaluator
15. calibration
16. freeze held-out thresholds and budget
17. held-out H1/H2
```

The important methodological boundary is that the benchmark world, visible artifacts, hidden truth, and core assertions should exist before P0 behavior is tuned.

---

## 31. Benchmark-first self-discipline

The first executable code should therefore be benchmark code, not autonomous-agent code.

Before P0 exists, the project should already be able to:

```text
generate a valid case
verify its hidden truth
produce the visible workspace
release the Phase 2 notice
log condition-neutral actions
identify deterministic integrity failures
run the strong B0/B1 baselines
```

At that point P0 must earn additional complexity rather than define the benchmark around itself.

---

## 32. Explicit prototype conveniences

The following may be chosen for convenience in Version 0 without becoming production decisions:

```text
plain Python records
JSON serialization
simple append-only audit logs
local experiment configuration files
small hand-authored knowledge components
simple deterministic trigger checks
manual benchmark templates
one local execution mechanism
```

Future evidence may replace all of them.

---

## 33. Explicit non-goals

Version 0 still does not require:

```text
multi-agent orchestration
vector retrieval
graph database
workflow engine
production database
automatic knowledge learning
full governance/admissibility engine
full risk/assurance engine
human simulation
external web research
production deployment
monitoring
UI
large-scale benchmark generation
```

Adding these before the semantic spine is empirically justified would weaken the experiment.

---

## 34. What this specification now makes possible

Checkpoint 10 established a falsifiable experimental idea.

Foundation 011 now makes that idea implementable.

The project has concrete definitions for:

```text
the synthetic world
the visible artifacts
the hidden evaluator world
the dynamic revelation
the inherited contamination
the common access boundary
the common trace
the minimal P0 object and relation semantics
the four knowledge components
the action gate
the dependency repair mechanism
the deterministic assertions
the semantic evaluation responsibilities
the baseline fairness controls
the resource instrumentation
the implementation order
```

The remaining uncertainty should now be learned primarily through implementation rather than further abstract design.

---

## 35. Next step

The next phase should begin actual Version 0 implementation, starting with:

```text
synthetic DGP
-> generated visible artifacts
-> hidden evaluator manifest
-> benchmark self-tests
```

The system should not implement P0 state machinery until the benchmark case can generate and validate independently.

This is the transition from controlled prototype specification to experimental construction.