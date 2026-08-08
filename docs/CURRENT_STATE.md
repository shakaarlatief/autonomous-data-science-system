# Current State

## Checkpoint

**Checkpoint:** 10  
**Date:** 2026-08-08  
**Development stage:** Transition from conceptual research to controlled prototype specification  
**Implementation status:** Not started

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, analytical depth, speed, or low cost are project-dependent objectives rather than universal goals.

## Current project constitution

The conceptual hierarchy remains:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

The five candidate epistemic invariants remain:

1. semantic validity;
2. information legitimacy;
3. evidence validity;
4. claim validity;
5. traceability and dependency integrity.

These remain strong design hypotheses rather than finalized system requirements.

## Development foundations so far

### Checkpoint 4: project state and orchestration

Project state is treated as a living dependency-aware representation of what the system is currently entitled to believe and do. Important ideas include typed state, validity versus currency, dependency impact, reopening, computational plus information lineage, a runnable frontier, and state-driven rather than fixed-plan orchestration.

Detailed reasoning:

`docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md`

### Checkpoint 5: project initialization

New projects should enter through progressive source-aware state construction and a small universal bootstrap rather than one-shot problem definition.

Detailed reasoning:

`docs/foundations/005_project_initialization_and_universal_bootstrap.md`

### Checkpoint 6: knowledge activation

Reusable knowledge should activate from meaningful project-state patterns and contribute questions, obligations, safeguards, evidence requirements, reviews, or candidate actions back into shared state. Activation may be reactive or prospective and should remain open-world.

Detailed reasoning:

`docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`

### Checkpoint 7: reusable knowledge representation

The strongest representation hypothesis is a thin semantic knowledge package containing versioned, provenance-aware, typed composable reasoning components such as question templates, invariants, evidence requirements, failure modes, claim constraints, dependencies, resolution criteria, and reopen conditions.

Detailed reasoning:

`docs/foundations/007_reusable_knowledge_representation_and_composable_components.md`

### Checkpoint 8: knowledge quality and evolution

Reusable knowledge should itself obey epistemic discipline. Important hypotheses include minimum justified generalization, separation of project-specific lessons from reusable knowledge, different thresholds for reasoning/reuse/enforcement, counterexample-driven scope discovery, staged promotion, challenge history, knowledge versioning, and cross-project invalidation after material knowledge revisions.

Detailed reasoning:

`docs/foundations/008_knowledge_quality_generalization_and_evolution.md`

### Checkpoint 9: behavioral system evaluation

The system should be evaluated as a trajectory through a partially observable project world rather than by one final model metric. Behavioral cases should specify an acceptance envelope: mandatory obligations, prohibited behavior, acceptable alternative resolutions, dynamic state changes, repair expectations, claim constraints, and optional quality opportunities.

Detailed reasoning:

`docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md`

## Major development at Checkpoint 10: minimum falsification prototype

The project now has a concrete first implementation experiment.

The central experimental question is:

> **Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?**

The first prototype should test the semantic spine rather than build a production system:

```text
PROJECT STATE
      ↓
KNOWLEDGE ACTIVATION
      ↓
QUESTIONS / OBLIGATIONS / CONSTRAINTS
      ↓
RUNNABLE ACTIONS
      ↓
EXECUTION
      ↓
EVIDENCE
      ↓
STATE UPDATE
      ↓
DEPENDENCY IMPACT / REOPENING
```

Detailed reasoning and the experimental contract:

`docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`

Historical snapshot:

`docs/checkpoints/010_minimum_falsification_prototype.md`

## Experimental conditions

The first experiment should compare three conditions using the same strong underlying LLM and comparable execution resources:

```text
B0
Strong generic LLM workflow.

B1
Same model plus the prototype's small methodological
knowledge set supplied as static prompt guidance.
No typed state, activation, prospective gate, or dependency repair.

P0
Same model plus minimal typed state, a tiny knowledge set,
activation/applicability, prospective safeguards,
a simple runnable frontier, and dependency-aware reopening.
```

B1 is the critical control. If B1 matches P0 at lower complexity, then much of the explicit state machinery may not be justified for this project scale.

## Prototype project

The first benchmark family is a synthetic customer-month churn project.

Visible files include:

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

The project contains repeated customers, timestamps, a stale README claiming one row per customer, an inherited baseline with learned-preprocessing contamination, a protected final test, and an `account_state_code` whose timing is initially described incorrectly by stale documentation.

The temporal partitions are approximately:

```text
train: months 1-16
validation: months 17-20
test: months 21-24
```

Deployment includes future observations of both known and newly entering customers. Repeated IDs should therefore activate generalization reasoning but should not mechanically imply a pure unseen-entity split.

## Dynamic state change

After a provisional model/validation milestone, the evaluator reveals an authoritative notice showing that `account_state_code` is populated only after the churn outcome and retrospectively backfilled.

The system must then revise feature eligibility, discover affected dependencies, reopen materially affected models/evidence/decisions/claims, preserve unrelated valid work, rerun legitimate evaluation, and ensure final claims use current evidence.

This is the central Version 0 test of dependency-aware self-correction.

## Minimal P0 state vocabulary

The first structured prototype currently requires only:

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

Candidate minimal relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

The exact serialization and storage technology remain open.

## Minimal reusable knowledge

Version 0 should contain only four manually authored components:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001  Generalization-Regime Question
```

This is enough to test both deterministic safeguard behavior and interpretive applicability without building a large knowledge library or retrieval system.

## Evaluation logic

The evaluator should measure behavioral dimensions such as:

```text
semantic correction
validation reasoning
preprocessing integrity
test integrity
feature legitimacy
repair completeness
repair precision
claim validity
detection latency
analytical efficiency
project utility
```

Critical integrity failures should not be compensated by marginally better predictive performance.

A development case can be used for implementation debugging, followed by at least two held-out surface variants with changed field names, documentation wording, random seeds, and nonessential DGP details.

A reasonable first protocol is three calibration runs per condition on the development case, followed by five paired held-out runs per condition on each of two surface variants.

Quantitative continuation thresholds should be frozen after calibration and before held-out evaluation.

## Falsification criteria

The structured architecture is not assumed to be necessary.

Strong evidence against P0 would occur if B1 matches it across critical integrity behavior, repair completeness, repair precision, and held-out variants while using materially less reasoning/state-management cost.

Repeated false blockers, duplicate obligations, excessive reopening, or case-specific hard-coded rules also count against P0.

The strongest reason to continue would be repeated held-out evidence that P0 prevents or repairs critical methodological failures more reliably and precisely than B1 without unacceptable cost or systematic false blocking.

Higher AUROC alone is not a reason to continue the architecture.

## Explicit prototype exclusions

Version 0 does not require:

```text
multi-agent architecture
provider routing
vector database
graph database
large reusable knowledge library
automatic knowledge learning
full admissibility implementation
full risk/assurance implementation
external web research
production deployment
monitoring
workflow engine
UI
```

These should remain deferred until the semantic spine earns additional complexity.

## Continuity and chat rotation

Checkpoint timing and chat rotation are proactive AI responsibilities.

A new chat should not be opened merely because the conceptual topic changes or a checkpoint is reached. One chat may contain many checkpoints while continuity remains healthy.

The AI collaborator should recommend a new chat before context pressure materially threatens continuity, preserve the repository first, and provide the next numbered content-specific chat title and minimal continuation instruction.

See `DECISIONS.md` D-018 through D-020 and `docs/CONTINUITY.md`.

## Explicit non-decisions

The project has still not selected a production agent architecture, provider strategy, workflow framework, database, graph technology, vector retrieval system, full state schema, full knowledge schema, final status vocabulary, final evaluation framework, deployment architecture, automatic knowledge-learning mechanism, or full autonomy model.

Prototype conveniences must not be mistaken for production architecture decisions.

## Current focus

The conceptual architecture is now sufficiently specified to support a first limited implementation.

The immediate next question is:

> **How should Prototype V0 be represented and implemented concretely while preserving the experimental contract and avoiding premature production architecture?**

The next work should specify the benchmark/evaluator implementation first, then the minimal state model, action gate, knowledge components, baseline harness, P0 control loop, run logging, and resource instrumentation.

## Required context for a new chat

A new design/implementation chat should read, at minimum:

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/VISION.md`
4. `docs/PRINCIPLES.md`
5. `docs/DECISIONS.md`
6. `docs/OPEN_QUESTIONS.md`
7. `docs/DEVELOPMENT_METHOD.md`
8. `docs/CONTINUITY.md`
9. `docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md`
10. `docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md`

If deeper architectural context is needed, read Foundations 002 through 008 as relevant.

## Next step

Define the concrete implementation contract for Prototype V0, beginning with the synthetic benchmark generator and evaluator rather than the autonomous treatment.