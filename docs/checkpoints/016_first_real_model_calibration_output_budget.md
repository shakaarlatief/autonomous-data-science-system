# Checkpoint 016: First Real-Model Calibration Output-Budget Correction

**Date:** 2026-08-08  
**Status:** Historical mixed checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Experimental construction and baseline calibration  
**Scope:** Records the historical milestone described by this checkpoint: First Real-Model Calibration Output-Budget Correction.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** First paid B0 request reached the provider but terminated before producing a usable command; the discovered output-budget and accounting defects have been corrected and test-validated

## Why this checkpoint exists

Checkpoint 15 made real B0/B1 calibration executable. The first genuine B0 attempt then supplied the first evidence from the actual provider boundary.

The attempt used:

```text
condition: B0
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 10,000
```

The provider accepted the request but returned:

```text
status = incomplete
incomplete_details.reason = max_output_tokens
```

No visible structured command was produced and therefore no B0 data-science behavior occurred.

The attempt is an infrastructure diagnostic, not a failed B0 reasoning trajectory.

## Root cause

For current OpenAI reasoning models, `max_output_tokens` limits total generated tokens, including hidden reasoning tokens, visible output tokens, and non-visible formatting tokens.

The first B0 request exhausted the 10,000-token ceiling during reasoning before a usable structured command was returned.

Current OpenAI reasoning guidance recommends reserving at least 25,000 tokens for reasoning and output when initially experimenting with these models.

The previous 10,000-token calibration ceiling was therefore too restrictive for the selected model/effort configuration.

## Condition-neutral correction

The development-calibration ceiling is now:

```text
max output tokens per call: 30,000
```

The reasoning effort remains `high` for now because the benchmark is intended to test a strong reasoning baseline and current provider guidance describes high effort as appropriate for complex workflows and agentic tasks.

The 30,000-token value is still a ceiling rather than a required expenditure. It is a calibration setting, not a frozen held-out budget.

B0, B1, and later P0 must receive the same value within paired comparisons.

## Discovered accounting defect

The first attempt also exposed a second infrastructure problem.

The run summary reported:

```text
input_tokens: 0
output_tokens: 0
total_tokens: 0
```

That did not imply that the failed request was free. An incomplete Responses API object can contain observable usage even when no visible output is produced.

The adapter previously raised `ModelGenerationError` before extracting that usage.

This would make condition-level resource accounting incomplete and could bias later B0/B1/P0 comparisons.

## Failed-generation usage is now first-class

`ModelGenerationError` can now carry:

```text
usage
provider_metadata
```

The OpenAI adapter extracts provider-reported usage before deciding whether a response is complete.

For incomplete responses it preserves:

```text
input tokens
output tokens
total tokens
response ID
status
reasoning-token count when reported
max-output-token configuration
```

The common treatment runner accumulates observable usage from both successful generations and failed generations that report usage.

Failures that occur before a provider response exists may still have unknown provider-side work. The experiment therefore continues to describe its totals as **observable provider-reported usage**, not perfect billing truth.

## More precise incomplete-response diagnostics

The previous adapter used the generic response status `incomplete` as the error code.

It now records the specific incomplete reason where available, for example:

```text
max_output_tokens
```

Repeating the exact same request with the same fixed output ceiling is not treated as a useful transient retry, so this failure remains non-retryable under the common retry policy.

The appropriate recovery is a condition-neutral calibration change, not three identical paid attempts.

## Behavioral scoring correction

The first infrastructure-aborted run was originally summarized with deterministic critical failure `A3` because no final model-lock report existed.

That raw assertion is mechanically understandable but methodologically misleading: the model had produced zero successful commands and never entered the behavioral experiment.

Calibration summaries now distinguish:

```text
behavior_evaluable = true / false
```

A run terminated by a provider-generation error is not reported as a completed behavioral score. The raw deterministic evaluator output is still preserved for diagnosis, but summary-level pass/fail fields are left unscored for infrastructure-aborted trajectories.

Runs that simply fail to complete within the ordinary model-call budget remain behaviorally evaluable because that is treatment behavior rather than an infrastructure abort.

## Test coverage

New tests verify that:

```text
an incomplete OpenAI response preserves observable usage
max_output_tokens is surfaced as the specific failure reason
reasoning-token metadata is retained when reported
the 30,000-token default reaches the provider request
failed-generation usage contributes to aggregate run totals
failed-generation usage appears in the common trace
```

The complete CI suite after the correction passed:

```text
23 passed in 8.17s
```

The benchmark was regenerated and self-validated successfully with unchanged development-case sanity metrics.

## Status of the first paid attempt

The original `dev-b0-01` attempt must not be used as B0 behavioral evidence.

It established only that:

```text
provider authentication worked
model access worked
request construction reached the model
10,000 generated tokens was insufficient for the first high-effort turn
infrastructure failure tracing worked
resource accounting needed correction
```

Because no successful model generation occurred, no B0 methodological conclusions should be drawn from that attempt.

## Next step

Pull the corrected repository, rerun the local tests, and start a new B0 development-calibration trajectory with a new run ID and the 30,000-token ceiling.

Do not run B1 until the corrected B0 trajectory is shown to be operationally viable.
