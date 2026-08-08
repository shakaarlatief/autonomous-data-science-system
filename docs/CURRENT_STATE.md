# Current State

## Checkpoint

**Checkpoint:** 17  
**Date:** 2026-08-08  
**Development stage:** Experimental construction and real-model baseline calibration  
**Implementation status:** Two provider-interface diagnostics have run before any behavior-evaluable B0 trajectory. Output-budget/accounting and duplicate-structured-output normalization defects have been repaired condition-neutrally and CI-validated. A fresh B0 run is next.

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

These are development-calibration values, not frozen held-out budgets. They must be applied condition-neutrally across B0, B1, and future P0 comparisons.

## Real-model calibration record

### `dev-b0-01`

The first provider-backed B0 attempt used a 10,000-token per-call ceiling and returned:

```text
status = incomplete
incomplete_details.reason = max_output_tokens
successful model commands = 0
behavior_evaluable = false
```

This exposed two infrastructure issues:

1. the 10,000-token ceiling was too restrictive for the first high-effort reasoning turn;
2. the old adapter raised before preserving usage from an incomplete Responses API object.

Checkpoint 16 corrected both. Incomplete responses now preserve observable usage/provider metadata, specific incomplete reasons are retained, infrastructure-aborted runs are separated from treatment-behavior scores, and the development-calibration ceiling was raised condition-neutrally to 30,000 tokens.

### `dev-b0-02`

The second B0 attempt used the corrected 30,000-token ceiling. The provider response itself completed successfully:

```text
status = completed
input tokens = 1107
output tokens = 130
reasoning tokens = 41
total tokens = 1237
successful model commands accepted by old adapter = 0
behavior_evaluable = false
```

The terminal adapter error was `invalid_json`.

Retrieving the stored response by response ID showed why. The response contained two assistant message items, each holding the same independently valid strict-JSON command:

```json
{
  "rationale": "I need to identify the available documentation and data artifacts before assessing the task or modeling plan.",
  "command": {
    "type": "list_artifacts"
  }
}
```

The OpenAI Python SDK `Response.output_text` convenience property concatenates all message-level `output_text` blocks. The old adapter therefore saw conceptually:

```text
{valid JSON object}{the same valid JSON object}
```

and `json.loads(...)` correctly rejected that aggregate as one JSON document.

This was a provider-normalization defect, not a B0 methodological failure. The model's actual proposed first action was valid, but the common adapter never admitted it to the treatment runtime.

## Duplicate structured-output normalization

The OpenAI adapter now uses a conservative condition-neutral normalization rule:

```text
extract non-empty message-level output_text blocks
try the aggregate normally when it is valid JSON
if aggregate parsing fails, parse blocks independently
accept multiple blocks only when every block is valid JSON and all parsed payloads are equal
collapse duplicate-equal blocks into one provider-neutral generation
reject multiple distinct valid commands as ambiguous
reject malformed or absent structured output
```

The adapter never arbitrarily chooses a first or last command when multiple distinct commands are present.

Provider metadata now records:

```text
output_text_block_count
distinct_output_text_block_count
duplicate_identical_output_blocks_collapsed
structured_output_source
```

An unsafe-to-normalize multi-command response is classified as `ambiguous_structured_output`.

This normalization applies identically to B0, B1, and future P0.

## Failed-generation resource accounting

`ModelGenerationError` carries optional:

```text
usage
provider_metadata
```

The OpenAI adapter extracts usage before response-status validation and preserves, where reported:

```text
input tokens
output tokens
total tokens
reasoning tokens
response ID
response status
max-output-token setting
```

The common runner accumulates observable usage from failed generations as well as successful generations.

The totals are explicitly **observable provider-reported usage**, not a claim about provider work that cannot be observed when a request fails before a normal response exists.

## Failure classification and behavioral scoring

Incomplete responses expose their specific reason, for example `max_output_tokens`, instead of only a generic `incomplete` status.

Exhausting a fixed output ceiling is non-retryable for the same request configuration because immediately repeating the identical request would predictably spend more inference without changing the constraint.

Infrastructure-aborted runs are separated from behavioral treatment failures:

```text
behavior_evaluable = false
```

when a terminal provider-generation error prevents the treatment from proceeding.

The raw deterministic evaluator output remains persisted for diagnosis, but summary-level behavioral pass/fail is not reported for such runs.

## Automated validation

After the Checkpoint 17 duplicate-output repair, GitHub Actions passes:

```text
25 passed in 8.30s
```

The suite now additionally verifies:

```text
incomplete OpenAI response usage preservation
specific max_output_tokens failure classification
reasoning-token metadata preservation
30,000-token provider request ceiling
failed-generation usage aggregation
failed-generation trace accounting
duplicate identical structured output blocks are safely collapsed
multiple distinct structured commands are rejected as ambiguous
```

The same CI run regenerated and self-validated the benchmark with unchanged sanity metrics.

Historical implementation/calibration checkpoints:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
docs/checkpoints/015_real_model_calibration_infrastructure.md
docs/checkpoints/016_first_real_model_calibration_output_budget.md
docs/checkpoints/017_duplicate_structured_output_normalization.md
```

## P0 remains intentionally unimplemented

The experimental protocol still requires genuine B0/B1 viability evidence before P0 is built.

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

**Q-042 remains the highest-priority question:** what do real B0/B1 development-calibration trajectories show, and what common protocol/budget should be frozen before P0?

Calibration has now exposed and repaired two shared infrastructure assumptions before P0 exists:

```text
1. reasoning-aware output budget and failed-response accounting
2. multi-message structured-output normalization
```

Neither `dev-b0-01` nor `dev-b0-02` is behavior-evaluable. No genuine B0 methodological trajectory has yet been observed.

The next evidence must establish actual B0 behavior under the corrected common interface before B1 is run.

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
```

## Next step

Pull the corrected repository, rerun the local test suite, and execute a fresh B0 development-calibration trajectory using a new run ID such as `dev-b0-03` with the same 30,000-token, high-reasoning configuration.

Do not run B1 until the corrected B0 trajectory is operationally viable and inspected.