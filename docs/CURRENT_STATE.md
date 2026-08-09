# Current State

## Checkpoint

**Checkpoint:** 18  
**Date:** 2026-08-09  
**Development stage:** Real-model baseline calibration and semantic trajectory review  
**Implementation status:** The first behavior-evaluable B0 trajectory has completed successfully after two condition-neutral provider-interface repairs. Full semantic inspection of that trajectory is now the required next step before B1.

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

Semantic project-quality judgments remain separate from these deterministic checks.

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

## Current development-calibration configuration

The provisional common configuration remains:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max output tokens per call: 30,000
max additional generation retries: 2
request timeout: 300 seconds
strict Structured Outputs
multi-turn previous_response_id continuation
all-turn reasoning context
```

These remain development-calibration values, not frozen held-out budgets. They must be applied condition-neutrally across B0, B1, and future P0 comparisons.

## Real-model calibration record

### `dev-b0-01`: output-budget diagnostic

The first provider-backed B0 attempt used a 10,000-token per-call ceiling and returned:

```text
status = incomplete
incomplete_details.reason = max_output_tokens
successful model commands = 0
behavior_evaluable = false
```

Checkpoint 16 raised the development-calibration ceiling condition-neutrally to 30,000 tokens, preserved failed-response usage/provider metadata, and separated infrastructure-aborted runs from behavioral scores.

### `dev-b0-02`: duplicate structured-output diagnostic

The second attempt completed at the provider but returned two identical strict-JSON message outputs. The SDK aggregate concatenated them, causing the old adapter's single `json.loads(...)` call to fail.

Observed provider usage was:

```text
input tokens = 1,107
output tokens = 130
reasoning tokens = 41
total tokens = 1,237
behavior_evaluable = false
```

Checkpoint 17 added conservative normalization: duplicate-equal output blocks may collapse to one provider-neutral command, while distinct multiple commands remain an error.

### `dev-b0-03`: first behavior-evaluable B0 trajectory

After both shared infrastructure repairs, the next B0 run completed:

```text
Completed: True
Successful model calls: 15
Generation attempts: 15
Generation failures: 0
Total observed tokens: 103,240
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

This is the first genuine provider-backed B0 trajectory eligible for methodological interpretation.

Immediate operational implications are narrow but important:

```text
the command/runtime interface can support a complete B0 trajectory
the 20-call ceiling was sufficient in this run, with 5 calls unused
the 30,000-token per-call ceiling did not prevent completion
no provider-generation retry was needed
the current critical deterministic integrity assertions all passed
```

The 103,240-token total is now a material budget observation. It must be decomposed and interpreted from the raw trace before a common protocol is frozen.

## What has not yet been established about B0

The successful deterministic result does not establish the full quality of the trajectory.

The raw artifacts still need semantic review for:

```text
row-unit contradiction resolution
validation and generalization-regime reasoning
inherited preprocessing contamination recognition and handling
Phase 1 feature-eligibility assumptions
response to the Phase 2 authoritative timing notice
repair completeness and precision
final model lock discipline
final-test use
claim scope and limitations
unnecessary or weak analyses
command/tool efficiency
token growth across turns
```

The required raw artifacts are:

```text
results/raw/dev-b0-03/trace.jsonl
results/raw/dev-b0-03/summary.json
results/raw/dev-b0-03/deterministic_evaluation.json
results/raw/dev-b0-03/milestones.json
results/raw/dev-b0-03/conversation.json
```

## Provider/runtime robustness now implemented

The OpenAI adapter and common runner currently preserve:

```text
successful model calls
generation attempts and failures
observable input/output/total token usage
reasoning-token metadata where available
provider response IDs and status
specific incomplete reasons
duplicate structured-output normalization metadata
terminal generation errors
```

Infrastructure-aborted runs are marked `behavior_evaluable = false` rather than being misread as methodological failures.

## Automated validation

After the Checkpoint 17 repair, GitHub Actions passes:

```text
25 passed in 8.30s
```

The suite covers the benchmark/runtime/evaluator/baseline harness plus the real-provider adapter's current error accounting and duplicate-output normalization behavior. CI does not make paid API requests.

Historical implementation/calibration checkpoints:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
docs/checkpoints/015_real_model_calibration_infrastructure.md
docs/checkpoints/016_first_real_model_calibration_output_budget.md
docs/checkpoints/017_duplicate_structured_output_normalization.md
docs/checkpoints/018_first_behavior_evaluable_b0_run.md
```

## P0 remains intentionally unimplemented

The experimental protocol still requires baseline calibration before P0 is built.

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

Implementing P0 before B0/B1 calibration is sufficiently understood would weaken the falsification design by allowing the treatment to influence the interface or resource budget.

## Explicit non-decisions

No production agent architecture, permanent state database, graph technology, vector retrieval system, workflow framework, permanent provider strategy, automatic knowledge-learning mechanism, deployment architecture, UI, or monitoring stack has been selected.

## Current priority

**Q-042 remains the highest-priority question:** what do real B0/B1 development-calibration trajectories show, and what common protocol/budget should be frozen before P0?

The project has now crossed the first genuine behavioral boundary: one B0 trajectory completed and is evaluable.

The immediate priority is not another model run. It is to inspect `dev-b0-03` in full and decide whether the completed trajectory reveals any shared interface defect or budget issue that should be resolved before B1.

## External execution requirement

Paid calibration requires a securely configured local API credential. Credentials must remain outside the repository and must not be pasted into project conversations or committed files.

## Required context for a future chat

A future implementation/calibration session should read the canonical project documents plus:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
docs/checkpoints/015_real_model_calibration_infrastructure.md
docs/checkpoints/016_first_real_model_calibration_output_budget.md
docs/checkpoints/017_duplicate_structured_output_normalization.md
docs/checkpoints/018_first_behavior_evaluable_b0_run.md
```

## Next step

Inspect the complete raw `dev-b0-03` trajectory, including trace, milestones, deterministic evaluation, and conversation. Do not run B1 until that review determines whether the common interface is viable as-is or needs one more condition-neutral calibration repair.