# Prototype V0

Prototype V0 is the first deliberately limited implementation experiment for the Autonomous Data Science System.

It is not the production architecture. Its purpose is to test whether a small amount of explicit system architecture around a strong LLM materially improves the reliability of a changing data-science project.

The central question is:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

The experiment is intentionally falsification-oriented. P0 is not assumed to be the right architecture. If a simpler workflow performs just as well with less cost or friction, that is evidence to simplify the next version.

## Quick mental model

One run gives the same strong LLM a realistic churn-modelling project and lets it work autonomously through the project with Python and project files.

The classifier itself is not the main object of study. The experiment tests whether the system handles the surrounding data-science reasoning correctly:

```text
understand the project
    -> inspect inherited work
    -> reason about data semantics
    -> choose a defensible validation regime
    -> develop a provisional model
    -> receive new authoritative information
    -> repair affected evidence and decisions
    -> preserve unrelated valid work
    -> lock the final model
    -> use the protected test once
    -> produce defensible final conclusions
```

Three conditions use the same underlying model, data, Python capability, project files, and common resource limits:

```text
B0 = strong LLM + strong generic data-science instructions

B1 = B0 + the same four methodological principles supplied statically
     in the prompt

P0 = same strong LLM + explicit typed state + structured knowledge
     activation + safeguards + dependency-aware repair + state-derived
     action selection
```

B1 is the primary architectural control. If B1 matches P0 reliably with less complexity or cost, the richer P0 machinery is not justified for this benchmark.

## What one run is about

The benchmark is a synthetic monthly customer-churn project. The task is to predict whether an active customer will churn during the following 30 days.

At the start of Phase 1, the treatment receives:

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

The project deliberately contains several methodological traps and ambiguities.

### 1. Row semantics

The inherited README says that each row represents one customer.

That statement is stale. The data actually contain monthly customer snapshots, so the same customer can legitimately appear in multiple periods.

A strong solution should discover and resolve this contradiction rather than silently treating both descriptions as true.

### 2. Generalization and validation

The deployment objective is future-facing monthly prediction.

The data contain:

```text
repeated customers across time
future observations of already-seen customers
new customers entering later
```

Therefore repeated IDs do not mechanically imply a grouped split such as GroupKFold. The system should reason about the actual deployment regime and use a defensible temporal validation design.

### 3. Inherited preprocessing contamination

The inherited `baseline_model.py` uses information from both training and validation data when fitting a learned preprocessing transformation before validation is evaluated.

The printed validation score may be computationally correct for that script, but it is not clean evidence for model comparison.

A strong solution should inspect the inherited workflow and recognize this distinction.

### 4. Prediction-time feature eligibility

One feature is intentionally problematic.

In the development surface it is called `account_state_code`. In held-out H1 it is called `lifecycle_flag`. In held-out H2 it is called `profile_code`.

Initially, stale project documentation says that the field is available at scoring time. Treating it provisionally as eligible is therefore not automatically a failure.

After the provisional Phase 1 milestone, the system receives an authoritative timing notice stating that the field is populated only after the churn outcome is complete and then backfilled retrospectively into the analytical warehouse.

The feature is therefore not legitimately available at the beginning-of-period prediction moment.

The system must repair affected work.

### 5. Protected final evaluation

The test set is reserved for one final evaluation after development decisions are complete.

The system should not inspect test outcomes while tuning models, features, preprocessing, thresholds, or other development choices.

After the final model is explicitly locked, one final test evaluation is permitted. Development after seeing final-test outcomes would violate the protected-evaluation role unless the system explicitly abandons that role and weakens its claims accordingly.

## The three project phases

### Phase 1: provisional development

The system investigates the project and develops a provisional analytical position.

A good trajectory usually needs to address:

```text
row semantics
validation/generalization regime
status of inherited baseline evidence
feature-eligibility assumptions
candidate model evidence
important unresolved questions
```

The evaluator does not prescribe one exact model family or one exact action order.

### Phase 2: authoritative state change

A new timing notice reveals that the suspicious feature is post-outcome and unavailable at scoring time.

Any model, evidence, decision, or claim that materially depended on that feature should be reconsidered.

Unrelated valid work should remain current.

This is the central dynamic-state-change test in Prototype V0.

### Phase 3: final evaluation

After the repaired development state is complete, the system locks the final model.

Only then may it access the protected test values for one final evaluation and produce final conclusions.

## Experimental conditions

### B0: strong generic baseline

B0 receives:

```text
strong LLM
Python execution
project artifacts
strong general data-science instructions
free-form conversational project memory
```

It has no typed state, reusable structured knowledge components, deterministic protected-test gate, or dependency-repair mechanism.

B0 asks how well a strong model can handle the project with a good ordinary workflow.

### B1: static-knowledge baseline

B1 is identical to B0 except that four methodological concepts are supplied directly and permanently in the prompt:

```text
K-INFO-001  Protected Final Evaluation
K-INFO-002  Learned Transformation Evaluation Boundary
K-INFO-003  Prediction-Time Feature Eligibility
K-VAL-001   Generalization-Regime Question
```

B1 still has no typed project state, dynamic activation, state-derived runnable frontier, deterministic action gate, or dependency-aware state repair.

This condition tests whether P0's potential advantage comes from architecture or merely from giving the LLM better methodological instructions.

### P0: structured prototype

P0 uses the same treatment model and project capabilities as the baselines, but adds a small explicit semantic architecture around the LLM.

The P0 semantic loop is:

```text
PROJECT STATE
    -> KNOWLEDGE ACTIVATION
    -> QUESTIONS / OBLIGATIONS / CONSTRAINTS
    -> RUNNABLE ACTIONS
    -> EXECUTION
    -> EVIDENCE
    -> STATE UPDATE
    -> DEPENDENCY IMPACT / REOPENING
    -> next cycle
```

P0 deliberately uses one strong LLM reasoner. It does not add a hidden reviewer model or a multi-agent roster merely to increase reasoning capacity.

## P0 architecture

### Typed project state

P0 stores important project information using a small vocabulary:

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

The distinctions are intentional. For example, a numerical model result is `EVIDENCE`, a statement about expected deployment performance is a `CLAIM`, and choosing a model is a `DECISION`.

### Explicit relations

State items can be connected through:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

The most important distinction is between a hard dependency and ordinary support.

If a decision hard-depends on an assumption that becomes invalid, reopening is normally required. If one supporting evidence path disappears but independent support remains, the conclusion should be reassessed rather than blindly destroyed.

### Reusable knowledge activation

P0 contains only the same four methodological concepts supplied statically to B1:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Question
```

The difference is that P0 represents them as structured components that can activate when project state makes them relevant.

For example:

```text
protected test artifact appears
    -> protected-final-evaluation knowledge activates
    -> premature value access can be blocked
```

or:

```text
feature timing becomes uncertain
    -> prediction-time eligibility knowledge activates
    -> timing becomes an explicit question or constraint
```

### Prospective safeguard

Prototype V0 includes a deterministic protected-final-test safeguard where the rule is precise enough to enforce mechanically.

Before final-model lock, a proposed action that would inspect protected test values can be rejected before the information enters the reasoning process.

### State-derived runnable frontier

P0 uses unresolved project state to help determine what work is currently runnable.

The rough priority is:

```text
hard blockers
    -> blocking questions
    -> repair obligations
    -> high-value optional analysis
```

The purpose is not to remove LLM judgment. It is to give the LLM a structured representation of what remains unresolved instead of relying entirely on conversational recall.

### Dependency-aware repair

When authoritative information changes, P0 propagates the impact through explicit dependencies.

For the post-outcome feature, the intended behavior is approximately:

```text
feature-availability assumption becomes invalid
    -> dependent provisional evidence becomes invalid or stale
    -> dependent model decision reopens
    -> dependent claims are reconsidered
    -> replacement evidence is generated without the feature
    -> unrelated valid validation reasoning is preserved
```

The experiment evaluates both repair completeness and repair precision.

### Traceable history

P0 records state transitions instead of silently overwriting the past.

A decision can therefore move through states such as:

```text
PROVISIONAL
    -> REOPENED
    -> SUPERSEDED
```

This provides a traceable history of how project conclusions changed and why.

## Held-out evaluation

Prototype V0 uses two frozen held-out surface variants.

### H1

```text
seed: 811
customer identifier: member_key
time field: scoring_period
post-outcome field: lifecycle_flag
```

### H2

```text
seed: 1601
customer identifier: account_ref
time field: observation_period
post-outcome field: profile_code
```

The underlying methodological mechanisms are the same, but the data seed and lexical surface differ. This reduces the chance that a condition succeeds only because it responds to one particular field name or one particular generated dataset.

The preregistered sample is:

```text
H1: 5 B0 + 5 B1 + 5 P0
H2: 5 B0 + 5 B1 + 5 P0

Total: 30 held-out treatment runs
```

All conditions use the same frozen treatment model and common resource envelope.

The exact run order, failure handling, budgets, judge procedure, and continuation/falsification rules were preregistered before P0 implementation. See `docs/foundations/012_preregistered_held_out_evaluation_protocol.md`.

## What is evaluated

Evaluation has two layers.

### Deterministic mechanical checks

The common evaluator checks mechanically observable requirements such as:

```text
benchmark validity
protected final-test sequencing
no development after protected final-test feedback
final locked feature legality
required Phase 2 redevelopment after feature invalidation
```

Resource and runtime information is also recorded, including model calls, token use, Python attempts, provider failures, and completion status.

### Blinded semantic evaluation

After held-out execution, normalized external trajectories are judged without exposing condition identity or P0 private state.

The semantic rubric covers:

```text
S1   row-unit understanding
S2   validation/generalization reasoning
S3   inherited preprocessing contamination
S4   pre-Phase-2 feature-eligibility reasoning
S5   response to the authoritative timing notice
S6   repair completeness
S7   repair precision
S8   claim validity
S9   final validation rationale
S10  final conclusions
```

Critical semantic failures are evaluated separately.

The final comparison focuses especially on P0 versus B1 because B1 already receives the same methodological knowledge without the additional architecture.

## How to interpret the experiment

Prototype V0 is not trying to prove that one architecture is universally best for data science.

It asks whether these explicit mechanisms earn their complexity on a controlled changing project.

Possible outcomes include:

```text
P0 materially improves reliability at acceptable cost
    -> preserve the useful mechanisms and test them on broader problems

B1 matches P0 with less cost and friction
    -> simplify the next architecture

some P0 mechanisms help while others add cost or brittleness
    -> keep the useful mechanisms and redesign or remove the rest
```

The goal is therefore not to preserve P0. The goal is to learn what the smallest reliable architecture for a more general autonomous data-science system should contain.

## Repository map

Use this file as the quick entry point.

For deeper detail:

```text
prototype_v0/README.md
    Current short conceptual and operational overview of Prototype V0.

prototype_v0/src/ads_v0/
    Executable implementation.

prototype_v0/tests/
    Prototype tests.

prototype_v0/configs/
    Frozen experiment configuration.

docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
    Why V0 exists, benchmark design, hypotheses, B0/B1/P0, semantic spine,
    state vocabulary, relation vocabulary, and required behavior.

docs/foundations/011_prototype_v0_technical_specification.md
    Detailed technical design.

docs/foundations/012_preregistered_held_out_evaluation_protocol.md
    Frozen held-out variants, 30-run design, run order, budgets, failure
    handling, semantic judge, and continuation/falsification criteria.

docs/CURRENT_STATE.md
    Current execution status and next authorized step.

docs/checkpoints/
    Append-only development and experiment history.
```

Important implementation files include:

```text
src/ads_v0/p0.py
    P0 state, knowledge, dependency, and control machinery.

src/ads_v0/p0_schema.py
    Structured P0 model-response schema.

src/ads_v0/p0_controller.py
    P0 controller/runtime orchestration.

src/ads_v0/calibrate_p0.py
    P0 treatment entry point used during calibration and execution support.

src/ads_v0/calibrate.py
    B0/B1 treatment runner entry point.

src/ads_v0/casegen.py
    Synthetic benchmark generator.

src/ads_v0/evaluator.py
    Common deterministic evaluator.

src/ads_v0/heldout_execution.py
    Frozen held-out execution plan and validation logic.

src/ads_v0/heldout_runner.py
    One-attempt-at-a-time held-out execution interface.

src/ads_v0/openai_model.py
    OpenAI Responses API model adapter used by the experiment.
```

Paths in the implementation list are relative to `prototype_v0/`.

## Local setup

From `prototype_v0/`:

```bash
python -m pip install -e ".[dev,openai]"
```

Run the deterministic test suite with:

```bash
pytest
```

The experiment reads the OpenAI credential from the local environment:

```text
OPENAI_API_KEY
```

Do not place API keys in repository files or persisted run artifacts.

## Held-out execution interface

Held-out execution is deliberately one attempt at a time.

Check status without inference:

```bash
python -m ads_v0.heldout_runner status
```

Advance exactly one eligible attempt:

```bash
python -m ads_v0.heldout_runner run-next
```

The runner validates the frozen inputs, preserves attempt-level artifacts, and refuses to silently duplicate interrupted attempts.

For the exact currently authorized slot and current experiment progress, always consult:

```text
docs/CURRENT_STATE.md
```

## Governing documents

The authoritative conceptual and experimental specifications are:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

This README is intentionally simpler. If it ever conflicts with a frozen foundation document, the foundation document governs the experiment.