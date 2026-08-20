# Checkpoint 015: Real-Model Calibration Infrastructure

**Date:** 2026-08-08  
**Status:** Historical infrastructure record  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Experimental construction  
**Scope:** Records the historical milestone described by this checkpoint: Real-Model Calibration Infrastructure.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Real-model B0/B1 calibration path implemented and test-validated; paid baseline execution has not yet been run

## Why this checkpoint exists

Checkpoint 14 made B0 and B1 executable against the common experiment runtime through a provider-neutral model protocol, but only deterministic scripted model doubles had been exercised.

Checkpoint 15 completes the infrastructure required to run the first genuine strong-model baseline calibration without coupling the experiment architecture to one provider.

The next evidence should now come from actual B0/B1 model trajectories rather than additional P0 implementation.

## Provider remains experiment configuration

The project has still not selected a permanent model provider.

The first provisional calibration adapter uses the OpenAI Responses API because the current GPT-5.6 family supports reasoning and strict structured outputs suitable for the one-command-per-turn experiment contract.

The initial calibration default is:

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
reasoning context: all turns
structured output: strict JSON Schema
multi-turn continuation: previous_response_id
per-turn output ceiling: 12,000 tokens
request timeout: 300 seconds
```

This is a benchmark configuration, not an architectural commitment.

B0, B1, and later P0 must use the same underlying model configuration within paired experiments.

## Optional dependency boundary

The core Prototype V0 package remains provider-neutral.

OpenAI support is installed through an optional dependency group:

```text
python -m pip install -e ".[dev,openai]"
```

The provider adapter lives in:

```text
prototype_v0/src/ads_v0/openai_model.py
```

No OpenAI SDK object appears in the common runtime, evaluator, B0/B1 command dispatcher, or future P0 semantic interface.

## Strict structured command output

The adapter maps the provider response to the existing provider-neutral `ModelGeneration` object.

The OpenAI request uses a strict JSON Schema with an object root and a nested `anyOf` command union for:

```text
list_artifacts
read_text
table_metadata
table_sample
execute_python
phase_1_complete
final_model_locked
submit_final_report
```

All fields in each command variant are required and objects disallow additional properties.

This reduces parser variance while preserving the same semantic command contract used by scripted tests.

## Multi-turn context

The adapter can chain Responses API generations through `previous_response_id`.

The provider-neutral treatment runner still mirrors each assistant command and harness result in its own conversation transcript.

When continuing a provider-side response chain, the adapter sends only the newly appended non-assistant harness result because the prior assistant output is already part of the provider response chain.

This keeps provider threading out of treatment logic.

## Provider-neutral generation failures

`model.py` now defines `ModelGenerationError` with:

```text
retryable
provider
error_code
```

This separates transient provider failures from permanent configuration/authentication/request failures without making the common treatment runner depend on provider exception classes.

The OpenAI adapter translates connection/time-out/rate-limit/server-style failures into retryable generation errors and treats ordinary client/configuration/status failures as non-retryable where appropriate.

Error messages written to experiment traces are deliberately credential-safe.

## Centralized retry policy

An important calibration correction was made before real execution.

The current OpenAI Python SDK automatically retries several transient failures by default. If those retries remained enabled while the common treatment runner also retried generations, the experiment could silently perform multiple nested provider attempts and make reliability/cost accounting difficult.

Therefore, SDK-level retries are disabled for clients constructed by the adapter:

```text
max_retries = 0
```

The common `BaselineTreatmentRunner` owns the observable retry policy for B0/B1 and future P0.

Current default:

```text
max_generation_retries = 2
```

meaning at most three attempts for one reasoning turn when the error is retryable.

Non-retryable `ModelGenerationError` failures terminate immediately without spending the remaining retry budget.

Generic model doubles/errors are treated as retryable by default so provider-neutral testing remains simple.

## Generation-attempt instrumentation

`TreatmentRunResult` now distinguishes:

```text
successful model calls
generation attempts
generation failures
terminal generation error
input tokens
output tokens
total observed tokens
```

Every successful model generation creates a common trace event containing:

```text
model name
command type
provider-neutral token usage
provider metadata
response ID where available
generation attempts so far
generation failures so far
```

Failed attempts create `MODEL_GENERATION_ERROR` events.

Exhausted or permanent generation failures create `RUN_TERMINATED_GENERATION_ERROR`.

Provider APIs may not report token billing for network requests that fail before a normal response, so token totals are explicitly treated as observable successful-response usage rather than a claim about unknowable provider-side cost.

## Real calibration CLI

`prototype_v0/src/ads_v0/calibrate.py` now runs a real B0 or B1 trajectory against an already generated benchmark bundle.

Example B0:

```text
python -m ads_v0.calibrate \
  --bundle generated/development \
  --condition B0 \
  --run-id dev-b0-01 \
  --output results/raw/dev-b0-01
```

Example B1 uses the same command with `--condition B1` and a different run ID/output directory.

The CLI supports explicit model, reasoning-effort, model-call, generation-retry, and output-token configuration.

It writes:

```text
trace.jsonl
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
```

These outputs are sufficient to diagnose command reliability and deterministic behavioral outcomes before the blinded semantic evaluator exists.

## Credential handling

Local `.env` and `.env.*` files are ignored by Git.

The adapter expects the ordinary `OPENAI_API_KEY` environment configuration when used locally.

Keys must not be placed in source files, committed configuration, prompts, or generated result artifacts.

No real API key is available to the current design assistant, and no paid API calibration request has been executed as part of this checkpoint.

This is an expected experiment-execution boundary rather than a software defect.

## Test coverage

Network-free adapter tests verify:

```text
provisional model/reasoning configuration
strict Structured Outputs request construction
all-turn reasoning context
first-turn versus threaded previous_response_id behavior
provider-neutral usage mapping
threading requires stored provider responses in this adapter
schema object/anyOf invariants
```

Common generation-reliability tests verify:

```text
transient generation failure is retried and logged
successful retry records provider metadata and usage
retry exhaustion terminates the run without crashing the process
negative retry budgets are rejected
non-retryable provider-neutral failures terminate immediately
```

The full CI suite at this checkpoint passed with:

```text
21 passed in 7.47s
```

The same run then regenerated and self-validated the development benchmark with unchanged sanity metrics.

The OpenAI optional dependency installed successfully in CI. No API request is made in CI.

## Why P0 is still not implemented

The experiment deliberately required the strong simple baselines to exist and be viable before the structured treatment is built.

That requirement has not yet been satisfied empirically because B0/B1 have not run against a real model.

Implementing P0 now would weaken the falsification design by allowing the interface, budgets, or benchmark protocol to be adapted around P0 before observing how a strong simpler workflow behaves.

P0 therefore remains intentionally paused.

## Next evidence required

The next milestone is not another architecture component.

It is the first **real-model development calibration**:

```text
generate/pull the current development benchmark
set a local API credential outside the repository
run B0 once
run B1 once with the identical model configuration
inspect command reliability and deterministic results
review token/call/runtime costs
repair only provider/interface defects that affect both conditions fairly
repeat enough development runs to establish a viable common budget
```

Only after B0/B1 are demonstrably viable should P0 implementation begin.

## Calibration is not held-out evidence

The development case and its first real-model runs are explicitly for calibration.

They may be used to repair:

```text
provider adapter defects
ambiguous command-contract wording
unreasonable model-call/output budgets
condition-neutral runtime usability
logging omissions
```

They must not be interpreted as evidence that P0 generalizes, and P0 should not later be scored on this development case as held-out evidence.

The held-out H1/H2 protocol remains downstream of P0 implementation and calibration freeze.

## Current methodological boundary

The project has reached a useful stop condition in autonomous code construction:

> **Do not implement P0 merely because more code can be written. First obtain the empirical baseline evidence that the experimental design says must precede P0.**

This is an application of the project's own principle that the next action should be justified by project state rather than by implementation momentum.