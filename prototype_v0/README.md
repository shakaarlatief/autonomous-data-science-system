# Prototype V0

This directory contains the first deliberately limited implementation experiment for the Autonomous Data Science System.

It is not the production architecture.

The experiment asks whether explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make the same strong LLM materially more reliable than strong simpler workflows.

The benchmark, common experiment boundary, and strong baseline runners are implemented before the P0 treatment so P0 cannot define its own evaluation retrospectively.

## Current implementation scope

Implemented:

```text
synthetic customer-month churn DGP
visible Phase 1 project artifacts
hidden evaluator manifest
Phase 2 authoritative timing notice
benchmark self-tests
instrumented project workspace
Phase 1 / Phase 2 / final-evaluation transitions
metadata-versus-value access logging
declared-input Python execution
optional protected-final-test action gate
condition-neutral trajectory trace
deterministic behavioral evaluator
provider-neutral model protocol
deterministic scripted-model test double
B0 strong generic baseline runner
B1 static-knowledge baseline runner
model-call and token-usage accounting contract
provisional OpenAI Responses API adapter
real-model calibration CLI
```

Not implemented yet:

```text
executed real B0/B1 development calibration
P0 typed project-state runtime
P0 knowledge activation and dependency repair
semantic evaluator
paired calibration / held-out experiment runner
```

## Install

For benchmark development and tests:

```bash
python -m pip install -e ".[dev]"
```

For the current provisional OpenAI calibration adapter as well:

```bash
python -m pip install -e ".[dev,openai]"
```

The provider extra is experiment-specific. It does not make OpenAI a permanent architecture dependency.

## Run tests

```bash
pytest
```

The repository also runs the tests in GitHub Actions whenever Prototype V0 code or its workflow changes. CI additionally generates and self-validates the complete development benchmark.

## Generate the development case

```bash
python -m ads_v0.casegen --output generated/development
```

The generated bundle separates:

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

Treatment runtimes expose only the currently legitimate project region through `ExperimentWorkspace`. `evaluator_only/` is never registered as a treatment-facing project artifact.

Python analysis is executed in a fresh temporary directory containing copies of only the explicitly declared project artifacts. This is an experimental declared-input boundary, not an OS-level security sandbox.

## Baseline conditions

`BaselineTreatmentRunner` can execute B0 and B1 against the same workspace.

B0 receives strong generic data-science instructions.

B1 receives the same instructions plus the substantive content of the four methodological concepts that P0 will later operationalize:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Reasoning
```

B1 still has no typed state, dynamic activation, action gate, or dependency-repair mechanism.

A provider-neutral `ModelClient` contract keeps model/provider choice outside the treatment architecture. `ScriptedModel` is used for deterministic runner tests.

## Provisional real-model calibration

The first real adapter is isolated in `ads_v0.openai_model.OpenAIResponsesModel`.

The current calibration default is:

```text
model: gpt-5.6-terra
reasoning effort: high
Responses API structured JSON commands
multi-turn continuation through previous_response_id
```

This is a provisional experiment configuration, not a production-provider decision.

Set `OPENAI_API_KEY` in the local environment. Do not place keys in repository files or generated run artifacts.

Run B0:

```bash
python -m ads_v0.calibrate \
  --bundle generated/development \
  --condition B0 \
  --run-id dev-b0-01 \
  --output results/raw/dev-b0-01
```

Run B1 with the same model configuration:

```bash
python -m ads_v0.calibrate \
  --bundle generated/development \
  --condition B1 \
  --run-id dev-b1-01 \
  --output results/raw/dev-b1-01
```

The calibration CLI writes:

```text
trace.jsonl
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
```

Calibration results should be reviewed before selecting or freezing the common held-out resource budget. P0 should still not be implemented until the real baseline interface is shown to be viable.

## Deterministic behavioral evaluation

The first common evaluator can detect:

```text
premature value-level final-test access
new development after final-test feedback
final model lock that still includes the established post-outcome feature
missing Phase 2 development re-evaluation after relied-upon feature invalidation
benchmark self-validation failure
```

Semantic questions such as validation-design quality and claim scope remain outside the deterministic evaluator and will be handled by a later blinded semantic evaluation layer.

## Governing specification

See:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
```

Recent implementation checkpoints:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
```
