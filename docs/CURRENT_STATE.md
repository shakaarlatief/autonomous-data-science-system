# Current State

## Checkpoint

**Checkpoint:** 14  
**Date:** 2026-08-08  
**Development stage:** Experimental construction  
**Implementation status:** Benchmark, common runtime/evaluator, and provider-neutral B0/B1 runners implemented; real-model baseline calibration is next

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## Prototype V0 experiment

Prototype V0 tests whether operationalized semantic machinery adds reliability beyond a strong model and excellent prompting.

```text
B0
Strong generic LLM workflow.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, action gate, or dependency repair.

P0
Same model/tools + typed state + structured reusable knowledge
+ activation/applicability + prospective safeguards
+ dependency-aware repair + minimal state-driven action selection.
```

B1 is the critical control. If B1 matches P0's critical-integrity and repair behavior at materially lower complexity or cost, the explicit semantic runtime should be simplified or rejected for this project scale.

## Implemented benchmark

`prototype_v0/src/ads_v0/casegen.py` generates the 24-month synthetic customer-month churn benchmark.

Core hidden mechanisms are:

```text
true row unit = customer-month
stale README says row = customer
later periods contain both known and new customers
baseline preprocessing uses validation information
account_state_code is generated after the target outcome
stale README says that field is available at scoring time
Phase 2 notice authoritatively corrects the timing claim
final test is protected final evaluation
```

The generated case separates initial visible material, a withheld Phase 2 notice, and evaluator-only truth/self-tests.

The default development case remains stable at approximately:

```text
31,220 rows
4,000 customers
10.19% target prevalence
0.6884 legitimate validation AUROC
0.7212 AUROC with the post-outcome field
0.0328 incremental AUROC from that field
```

## Implemented common runtime and evaluator

`runtime.py` provides:

```text
phase-aware artifact visibility
metadata-versus-value access
explicit declared-input Python execution
condition-neutral event tracing
Phase 1 / Phase 2 / final-evaluation transitions
optional protected-final-test enforcement
condition-neutral milestone reports
```

`evaluator.py` currently checks:

```text
A0 benchmark self-validation passed
A1 no premature final-test value access
A2 no development after final-test feedback
A3 final locked model excludes the established post-outcome feature
A4 relied-upon invalid feature triggers Phase 2 development re-evaluation
```

Semantic questions such as validation-design quality, row-unit reasoning, repair adequacy, and claim scope remain for a later blinded semantic evaluator.

## Checkpoint 14: provider-neutral baselines

`model.py` now defines:

```text
ModelMessage
ModelUsage
ModelGeneration
ModelClient protocol
ScriptedModel
```

`treatments.py` now implements `BaselineTreatmentRunner` for B0 and B1.

Both conditions use the same command protocol and `ExperimentWorkspace`.

B0 receives strong generic data-science guidance.

B1 receives the same guidance plus the substantive content of:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001  Generalization-Regime Reasoning
```

B1 does not receive P0's state, activation, prospective enforcement, or repair machinery.

The runner tracks model calls and provider-neutral token usage and stops unfinished runs at a configurable model-call budget.

Historical implementation checkpoints:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
```

## Automated validation

The corrected B0/B1 orchestration suite passes in CI:

```text
14 passed in 4.54s
```

The one preceding failure was a whitespace-sensitive test assertion over B1 prompt text, not an implementation or treatment failure. It was corrected by normalizing whitespace before semantic prompt-content checking.

The same CI run regenerated and self-validated the development benchmark successfully.

## P0 remains intentionally unimplemented

The planned P0 state types remain:

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

with:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

and only four initial reusable knowledge components.

P0 should not be implemented until the real B0/B1 baseline interface has been calibrated against a strong model.

## Explicit non-decisions

No production agent architecture, permanent state database, graph technology, vector retrieval system, workflow framework, permanent provider strategy, automatic knowledge-learning mechanism, deployment architecture, UI, or monitoring stack has been selected.

Any model/provider chosen for the first experiment is an experiment configuration, not a production architecture decision.

## Current priority

The immediate next milestone is **real-model baseline calibration**.

It should establish:

```text
real structured-command reliability
fair retry/parsing semantics
reasonable common call/token budget
B0 development-case behavior
B1 development-case behavior
resource-accounting correctness
which run artifacts are needed for later blinded semantic evaluation
```

Only after the baseline interface and budget are viable should P0 be implemented.

## Required context for a new chat

A new implementation session should read the canonical project documents plus:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
```

## Next step

Select a provisional strong-model experiment configuration, implement its adapter without coupling the treatment logic to that provider, and run B0/B1 development calibration before P0 exists.