# Current State

## Checkpoint

**Checkpoint:** 12  
**Date:** 2026-08-08  
**Development stage:** Experimental construction  
**Implementation status:** Benchmark generator and self-validation implemented; experiment harness is next

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, analytical depth, speed, or low cost remain project-dependent objectives rather than universal goals.

## Project constitution

The current conceptual hierarchy remains:

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

These are strong design hypotheses now entering limited empirical testing.

## Foundations established before implementation

The relevant design progression is:

```text
Checkpoint 4   dependency-aware project state and state-driven orchestration
Checkpoint 5   progressive initialization and universal bootstrap
Checkpoint 6   knowledge activation and open-world reasoning
Checkpoint 7   reusable knowledge packages and typed components
Checkpoint 8   knowledge quality, generalization, and evolution
Checkpoint 9   behavioral reasoning regression and system evaluation
Checkpoint 10  minimum falsification prototype and experimental contract
Checkpoint 11  concrete Prototype V0 technical specification
Checkpoint 12  first implemented benchmark milestone
```

Detailed rationale is preserved in Foundations 004 through 011 and the historical checkpoint files.

## Central Prototype V0 experiment

Prototype V0 asks:

> **Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than equally capable simpler workflows?**

The three planned conditions remain:

```text
B0
Strong generic LLM workflow.

B1
Same model and tools plus the same small methodological knowledge set
supplied statically in the prompt.

P0
Same model and tools plus minimal typed project state, structured knowledge,
activation/applicability, prospective safeguards, dependency-aware reopening,
and minimal state-derived action selection.
```

B1 is the critical control. If B1 matches P0's critical integrity and repair behavior at materially lower complexity/cost, the structured semantic runtime is not justified at this project scale.

## Prototype technical specification

The full Version 0 technical contract is preserved in:

`docs/foundations/011_prototype_v0_technical_specification.md`

Checkpoint 11 snapshot:

`docs/checkpoints/011_prototype_v0_technical_specification.md`

## Checkpoint 12: benchmark implementation milestone

The benchmark-first implementation has begun under:

```text
prototype_v0/
├── .gitignore
├── README.md
├── pyproject.toml
├── src/
│   └── ads_v0/
│       ├── __init__.py
│       ├── casegen.py
│       └── selftest.py
└── tests/
    └── test_casegen.py
```

Continuous integration is defined in:

`.github/workflows/prototype-v0-tests.yml`

Historical implementation snapshot:

`docs/checkpoints/012_benchmark_generator_and_self_validation.md`

## Implemented benchmark world

The generator creates a 24-month synthetic customer-month churn project with approximately 4,000 underlying customers.

```text
train:      months 1-16
validation: months 17-20
test:       months 21-24
prediction moment: beginning of month
target: churn during the following 30 days
```

Customers enter over time and disappear after churn. Later partitions contain both previously observed and newly entering customers.

The true row unit is customer-month, while the visible stale README incorrectly says one row is one customer.

Legitimate visible predictors include tenure, plan tier, monthly charge, support tickets, late payments, and usage change.

## Dynamic feature-legitimacy mechanism

`account_state_code` is generated after the churn outcome with opaque categories `S1`, `S2`, and `S3`.

The initial README incorrectly describes it as available during monthly scoring.

After Phase 1, an authoritative timing notice establishes that the field is generated after the outcome window and retrospectively backfilled.

This creates the controlled belief-revision event that will later test dependency-aware repair.

## Inherited preprocessing contamination

The generated `baseline_model.py` deliberately fits learned preprocessing on combined train and validation inputs before reporting validation performance.

The generated script is valid executable code. A dedicated test now runs it in a subprocess so the benchmark tests methodological reasoning rather than incidental debugging.

## Visible versus evaluator-only artifacts

Each generated case contains:

```text
visible/
    project_brief.md
    README.md
    train.csv
    validation.csv
    test.csv
    baseline_model.py

phase_2/
    crm_field_timing_notice.md

evaluator_only/
    manifest.json
    self_test_report.json
```

The serialized separation is implemented. The next runtime milestone must make the information boundary operational so treatments cannot browse evaluator-only material.

## Benchmark self-tests

The generator automatically verifies:

```text
repeated entity IDs
unique entity-month pairs
correct temporal partitions
known + new entities in later periods
absorbing churn
prevalence range
README row-unit contradiction
README feature-timing contradiction
Phase 2 notice consistency
test role = protected final evaluation
inherited preprocessing contamination
post-outcome feature relevance without perfect target copying
legitimate predictive signal
moderate incremental post-outcome signal
expected visible columns only
```

A benchmark instance that fails a required check is rejected before any LLM run.

## Validated development-case properties

The current deterministic development case produces:

```text
rows:                              31,220
customers:                          4,000
target prevalence:                  0.1018578
validation new-customer share:      0.1981020
test new-customer share:            0.1209486
legitimate validation AUROC:         0.6883573
AUROC with post-outcome field:       0.7211739
post-outcome AUROC gain:             0.0328166
post-outcome total variation:        0.2050478
```

This is a useful benchmark shape: legitimate signal is meaningful but nontrivial, the post-outcome field can influence model choice without being a perfect target proxy, and later periods genuinely mix known and new entities.

## Automated validation status

GitHub Actions now installs Prototype V0, runs tests, generates the full development case, executes benchmark self-validation, and prints benchmark sanity metrics.

Latest validated implementation run completed successfully with:

```text
4 passed in 4.76s
```

The earlier `python -m ads_v0.casegen` `runpy` warning was fixed by removing eager executable-submodule imports from `ads_v0/__init__.py`. The generated CLI now runs cleanly. Remaining GitHub runner Node deprecation notices are external to Prototype V0.

## Minimal P0 semantics remain specified but unimplemented

P0 is still intentionally absent.

Its planned state vocabulary remains:

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

with relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Its four planned knowledge components remain:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001  Generalization-Regime Question
```

P0 should not be implemented until the common experiment boundary and simpler baselines exist.

## Explicit non-decisions

The project has still not selected a production agent architecture, permanent state database, graph technology, vector retrieval system, workflow framework, provider strategy, automatic knowledge-learning mechanism, full admissibility engine, full risk/assurance implementation, deployment architecture, UI, or monitoring stack.

Prototype conveniences such as Python records, local files, JSON, pytest, and GitHub Actions are experimental tools rather than production commitments.

## Current focus

The first benchmark-construction milestone is complete.

The next implementation milestone is:

> **Build the common instrumented workspace, project-phase runtime, condition-neutral action trace, and deterministic behavioral evaluator that B0, B1, and P0 will all use.**

The order remains benchmark-first and treatment-neutral:

```text
instrumented workspace / trace
-> deterministic behavioral evaluator
-> B0 runner
-> B1 runner
-> only then P0 state / knowledge / action gate / repair
```

## Required context for a new chat

A new implementation chat should read, at minimum:

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
11. `docs/foundations/011_prototype_v0_technical_specification.md`
12. `docs/checkpoints/012_benchmark_generator_and_self_validation.md`

Deeper foundations should be read when an implementation issue needs their rationale.

## Next step

Implement the treatment-neutral experiment boundary: artifact registry/access control, project phases, common action/event trace, and deterministic behavioral assertions.