# Current State

## Checkpoint

**Checkpoint:** 15  
**Date:** 2026-08-08  
**Development stage:** Experimental construction and baseline calibration  
**Implementation status:** Benchmark, common runtime/evaluator, B0/B1 runners, and real-model calibration infrastructure implemented; real B0/B1 execution is next

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## Prototype V0 experimental question

Prototype V0 asks whether operationalized semantic machinery materially improves reliability beyond a strong reasoner and excellent prompting.

```text
B0
Strong generic LLM workflow.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, action gate, or dependency repair.

P0
Same model/tools + typed project state + structured reusable knowledge
+ activation/applicability + prospective safeguards
+ dependency-aware repair + minimal state-driven action selection.
```

B1 is the critical control. If B1 matches P0's critical-integrity and repair behavior at materially lower complexity or cost, P0 should be simplified or rejected for this project scale.

## Implemented benchmark

`prototype_v0/src/ads_v0/casegen.py` generates the synthetic 24-month customer-month churn case.

Core hidden mechanisms are:

```text
true row unit = customer-month
stale README says row = customer
later periods contain known and new customers
baseline preprocessing uses validation information
account_state_code is generated after the target outcome
stale README says that field is available at scoring time
Phase 2 notice authoritatively corrects the timing claim
final test is protected final evaluation
```

The generated case separates Phase 1 visible material, a withheld Phase 2 notice, and evaluator-only truth/self-tests.

The development case remains approximately:

```text
31,220 rows
4,000 customers
10.19% target prevalence
0.6884 legitimate validation AUROC
0.7212 AUROC with the post-outcome field
0.0328 incremental AUROC from that field
```

## Common runtime and deterministic evaluator

`runtime.py` provides:

```text
phase-aware artifact visibility
metadata-versus-value access
explicit declared-input Python execution
condition-neutral trajectory logging
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

Semantic project-quality judgments remain for a later blinded evaluator.

## Implemented B0/B1 baselines

`model.py` defines the provider-neutral model protocol and provider-neutral generation errors.

`treatments.py` implements B0/B1 through the same command protocol and workspace.

B0 receives strong generic data-science guidance.

B1 receives the same guidance plus the substantive content of:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Reasoning
```

B1 still has no typed project state, dynamic activation, prospective action gate, or dependency-aware repair.

## Checkpoint 15: real-model calibration infrastructure

A provisional OpenAI Responses API adapter exists in:

`prototype_v0/src/ads_v0/openai_model.py`

The first calibration model configuration is:

```text
model: gpt-5.6-terra
reasoning effort: high
strict Structured Outputs
multi-turn previous_response_id continuation
all-turn reasoning context
request timeout: 300 seconds
```

The adapter class permits a 12,000-token output ceiling by default, but the **current development-calibration CLI deliberately uses the more conservative defaults**:

```text
max successful model calls: 20
max output tokens per call: 10,000
max additional generation retries: 2
```

These are calibration limits, not frozen held-out budgets. They may be revised condition-neutrally if the first genuine baseline runs show that the interface is unnecessarily restrictive.

This provider/model choice is experimental only. OpenAI support remains an optional dependency rather than a core architecture dependency.

## Centralized generation reliability

The OpenAI SDK's internal automatic retries are disabled for clients created by the adapter so provider retries do not silently nest under the experiment runner.

The common treatment runner owns retry behavior for B0/B1 and future P0.

`ModelGenerationError` distinguishes retryable transient failures from non-retryable provider/configuration failures.

The trajectory records:

```text
successful model calls
generation attempts
generation failures
model/provider metadata
provider response IDs where available
observable input/output/total token usage
terminal generation failure if any
```

Non-retryable errors terminate immediately; retryable errors may use the common bounded retry allowance.

## Real calibration CLI

`prototype_v0/src/ads_v0/calibrate.py` can execute B0 or B1 against an already generated benchmark.

Example:

```text
python -m ads_v0.calibrate \
  --bundle generated/development \
  --condition B0 \
  --run-id dev-b0-01 \
  --output results/raw/dev-b0-01
```

B1 uses the same model/runtime configuration with `--condition B1`.

Generated run artifacts are:

```text
trace.jsonl
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
```

`summary.json` preserves the exact run configuration and observed usage.

Local credentials must remain outside the repository. `.env` and `.env.*` are ignored.

## Automated validation

The current CI suite passes:

```text
21 passed in 7.47s
```

CI installs the optional OpenAI dependency, validates the adapter without network calls, tests common retry/error semantics, and regenerates/self-validates the benchmark.

No paid API request is made in CI.

Historical implementation checkpoints:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
docs/checkpoints/015_real_model_calibration_infrastructure.md
```

## P0 remains intentionally unimplemented

The experimental protocol requires genuine B0/B1 viability evidence before P0 is built.

Planned P0 state remains:

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

and only four initial structured knowledge components.

Implementing P0 before real baseline calibration would weaken the falsification design by allowing the interface or resource budget to be tuned around the treatment.

## Explicit non-decisions

No production agent architecture, permanent state database, graph technology, vector retrieval system, workflow framework, permanent provider strategy, automatic knowledge-learning mechanism, deployment architecture, UI, or monitoring stack has been selected.

## Current priority

**Q-042 is now the highest-priority question:** what do real B0/B1 development-calibration runs show, and what common protocol/budget should be frozen before P0?

The next evidence should establish:

```text
structured-command reliability
provider retry/error behavior
reasonable call/token budget
B0 development-case behavior
B1 development-case behavior
runtime/tool usability
resource accounting
outputs needed for later semantic judging
```

No additional P0 implementation should occur before this evidence is obtained unless a concrete baseline-interface defect requires condition-neutral repair.

## External execution requirement

The current assistant cannot execute paid OpenAI API calibration without a securely configured API credential and should not request that secret in chat.

The next practical step is to run the prepared B0 and B1 commands in an environment where `OPENAI_API_KEY` is configured securely, then inspect the generated result artifacts.

## Required context for a future chat

A future implementation session should read the canonical project documents plus:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
docs/checkpoints/015_real_model_calibration_infrastructure.md
```

## Next step

Run one real B0 and one real B1 development-calibration trajectory with identical model configuration, then review command reliability, deterministic assertions, cost, and semantic behavior before implementing P0.