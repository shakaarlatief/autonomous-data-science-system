# Current State

## Checkpoint

**Checkpoint:** 13  
**Date:** 2026-08-08  
**Development stage:** Experimental construction  
**Implementation status:** Benchmark and common treatment-neutral runtime implemented; baseline runners are next

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## Current conceptual core

The project constitution remains:

```text
Admissibility
-> Epistemic integrity
-> Risk-sensitive assurance
-> Project optimization
```

The candidate epistemic invariants remain semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

## Prototype V0 experiment

The current experiment compares:

```text
B0: strong generic LLM workflow
B1: same model/tools plus the same small methodological knowledge supplied statically
P0: same model/tools plus typed state, structured knowledge activation,
    prospective safeguards, and dependency-aware repair
```

B1 is the critical control. If B1 matches P0's critical-integrity and repair behavior at materially lower complexity or cost, the structured semantic runtime should be simplified or rejected for this project scale.

Detailed experiment design:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
```

## Implemented benchmark

`prototype_v0/src/ads_v0/casegen.py` generates the synthetic 24-month customer-month churn benchmark.

Core mechanisms include:

```text
true row unit = customer-month
stale README says row = customer
later periods contain known and new customers
baseline preprocessing uses validation information
account_state_code is generated after the target outcome
stale README says that field is available at scoring time
Phase 2 authoritative notice corrects the timing claim
final test is protected final evaluation
```

The generator writes visible Phase 1 artifacts, a withheld Phase 2 timing notice, and evaluator-only truth/self-test artifacts.

`prototype_v0/src/ads_v0/selftest.py` rejects benchmark instances that do not satisfy the intended structural, semantic, temporal, or predictive-signal conditions.

The default development case has approximately:

```text
31,220 rows
4,000 customers
10.19% target prevalence
19.81% new-customer share in validation
12.09% new-customer share in test
0.6884 legitimate validation AUROC
0.7212 AUROC with the post-outcome field
0.0328 incremental AUROC from that field
```

## Implemented common experiment runtime

`prototype_v0/src/ads_v0/runtime.py` now provides the same experiment boundary for future B0, B1, and P0 treatments.

It implements:

```text
Phase 1 / Phase 2 / final-evaluation transitions
phase-aware artifact visibility
metadata-versus-value access
explicit declared-input Python execution
condition-neutral event tracing
condition-neutral milestone reports
optional protected-final-test enforcement
```

Evaluator-only files are never treatment-facing artifacts.

Python execution uses a fresh temporary working directory containing only copies of explicitly declared project inputs. This is an experimental exposure boundary, not a production security sandbox.

For B0/B1, premature protected-test value requests will be allowed and logged. For future P0, the same request can be prospectively blocked. This creates a direct comparison between static methodological guidance and enforceable operational knowledge.

## Implemented deterministic evaluator

`prototype_v0/src/ads_v0/evaluator.py` currently checks:

```text
A0 benchmark self-validation passed
A1 no premature final-test value access
A2 no new development after final-test feedback
A3 final locked model excludes the established post-outcome feature
A4 relied-upon feature invalidation is followed by Phase 2 development re-evaluation
```

The deterministic evaluator intentionally does not judge semantic questions such as whether the validation design is scientifically appropriate. Those remain for a later blinded semantic evaluator.

## Validation status

The current automated test suite covers benchmark generation, surface variants, inherited baseline execution, phase visibility, protected-test gating, declared-input execution, and deterministic evaluator behavior.

The first CI run containing the complete Checkpoint 13 runtime/evaluator milestone succeeded with:

```text
10 passed in 5.72s
```

The workflow then regenerated and self-validated the full development benchmark successfully.

Historical implementation checkpoints:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
```

## P0 remains intentionally unimplemented

Planned P0 state types:

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

Planned relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Planned knowledge:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

P0 must remain unimplemented until B0 and B1 can complete the same common runtime end to end.

## Explicit non-decisions

No production agent architecture, permanent state database, graph technology, vector retrieval system, workflow framework, provider strategy, automatic knowledge-learning mechanism, deployment architecture, UI, or monitoring stack has been selected.

Prototype Python modules, JSON-like records, local files, pytest, and CI are experiment conveniences only.

## Current priority

Q-041 remains the highest-priority implementation question.

The immediate milestone is:

> **Define the provider-neutral model interaction contract and implement genuine B0 and B1 end-to-end treatment runners against the common workspace before implementing P0.**

## Required context for a new chat

A new implementation session should read the canonical project documents plus:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
```

## Next step

Implement the provider-neutral model protocol and B0/B1 treatment loop, using deterministic scripted-model tests before connecting any real model provider.