# Checkpoint 014: Provider-Neutral B0/B1 Treatment Runners

**Date:** 2026-08-08  
**Development stage:** Experimental construction  
**Implementation status:** Benchmark, common runtime/evaluator, and baseline treatment orchestration implemented; real-model baseline calibration is next

## Why this checkpoint exists

Checkpoint 13 established a treatment-neutral experiment boundary before any autonomous semantic treatment was implemented.

Checkpoint 14 completes the next deliberate control milestone: B0 and B1 can now run end to end against that same boundary through a provider-neutral model protocol.

P0 remains intentionally unimplemented. The experiment therefore still follows the ordering:

```text
benchmark
-> common runtime/evaluator
-> B0/B1 orchestration
-> real B0/B1 calibration
-> only then P0
```

This ordering is important because the structured treatment must be compared against genuine strong baselines rather than against controls designed after P0 exists.

## Provider-neutral model protocol

`prototype_v0/src/ads_v0/model.py` now defines:

```text
ModelMessage
ModelUsage
ModelGeneration
ModelClient protocol
ScriptedModel
```

The central interface is conceptually:

```text
ModelClient.generate(messages) -> ModelGeneration
```

`ModelGeneration` contains:

```text
structured treatment payload
model name
provider-neutral token usage
optional provider metadata
```

No provider SDK or permanent provider choice is embedded in the treatment runtime.

`ScriptedModel` is a deterministic model double used only to test orchestration and evaluation mechanics before a real provider is connected.

## Common treatment command contract

`prototype_v0/src/ads_v0/treatments.py` implements a structured command loop.

Each model generation returns one short-rationale JSON command rather than persisted private chain-of-thought.

Available commands are:

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

The runner dispatches these commands to the same `ExperimentWorkspace` used by all conditions.

This keeps provider behavior separate from artifact access, Python execution, phase transitions, and evaluator logging.

## B0 baseline

B0 receives a strong generic autonomous data-science instruction rather than an intentionally weak prompt.

It is explicitly told to:

```text
investigate before committing to modeling choices
treat documentation as evidence rather than infallible truth
resolve material semantic contradictions
use validation representing intended use
guard against information leakage
distinguish facts from assumptions
protect final evaluation from development feedback
keep claims within valid evidence
prefer simple defensible work over unnecessary complexity
```

This makes B0 a meaningful strong-LLM workflow baseline.

## B1 baseline

B1 receives the same B0 instruction plus the substantive content of all four methodological knowledge components that future P0 will operationalize:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Reasoning
```

The static knowledge explicitly states that repeated IDs do not mechanically imply a pure unseen-entity split.

B1 therefore has the relevant methodology available from the beginning.

It does **not** receive:

```text
typed project state
dynamic knowledge activation
prospective action gating
dependency-aware reopening
state-derived action motivation
```

This remains the experiment's key control for asking whether structured operationalization adds value beyond excellent prompting.

## Condition-neutral milestone contract

All baseline treatments emit external reports at:

```text
PHASE_1_COMPLETE
FINAL_MODEL_LOCKED
FINAL_REPORT_SUBMITTED
```

The reports include structured `selected_features` plus ordinary project rationale/evidence fields.

These reports are not P0-style internal state. They are common experimental outputs required so the deterministic and later semantic evaluators can judge all conditions on comparable external evidence.

## Model-call and token accounting

`TreatmentRunResult` now records:

```text
model call count
input tokens
output tokens
total tokens
conversation messages
common runtime trajectory
deterministic evaluator result
```

Real provider adapters must reduce provider-specific usage metadata to the same `ModelUsage` representation.

This prepares B0/B1/P0 for explicit architecture-cost comparison.

## Budget behavior

`BaselineTreatmentRunner` accepts a maximum model-call budget.

If the model never reaches the required milestones, the run terminates incomplete rather than being allowed to reason indefinitely.

The final held-out budget is still to be selected during development calibration and frozen before held-out evaluation.

## Treatment errors

Invalid or malformed model commands are returned to the model as structured harness errors so a strong model can recover rather than causing the entire experiment process to crash immediately.

The common runtime also records treatment-command errors in the external trace.

Real-provider parsing/retry semantics must later be kept identical across B0 and B1 and, where applicable, P0.

## Deterministic scripted-run tests

`prototype_v0/tests/test_treatments.py` now verifies:

```text
B0 can complete a clean end-to-end project trajectory
B1 receives static knowledge that B0 does not
premature test access by B1 remains observable as deterministic A1 failure
an unfinished baseline stops at the model-call budget
```

The clean scripted trajectory exercises:

```text
Phase 1 development
Phase 1 report
Phase 2 notice
Phase 2 repair evaluation
final model lock
legitimate final-test evaluation
final report
```

The scripted model does not establish that a real strong LLM will behave correctly. It establishes that the baseline runner and experiment contract can support a real run.

## Test failure and correction

The first B0/B1 runner CI attempt produced:

```text
13 passed, 1 failed
```

The failure was not an implementation or methodological failure. A prompt-content test searched for an exact text substring that crossed a source-code line break.

The assertion was changed to normalize whitespace before checking semantic prompt content.

The corrected CI run completed successfully with:

```text
14 passed in 4.54s
```

The development benchmark then regenerated and self-validated with the same stable benchmark properties as earlier checkpoints.

This correction is intentionally documented because experimental test brittleness should not be silently confused with a treatment failure.

## Current implementation boundary

The codebase now contains:

```text
casegen.py      synthetic benchmark world
selftest.py     benchmark self-validation
runtime.py      common instrumented treatment boundary
evaluator.py    deterministic behavioral assertions
model.py        provider-neutral model protocol
treatments.py   B0/B1 treatment loop
```

Tests cover all of these layers using deterministic model doubles.

## What remains intentionally absent

No real model provider is connected yet.

P0 also remains absent.

The following therefore remain upcoming:

```text
real-model adapter and experiment configuration
actual B0/B1 development calibration
prompt/JSON reliability calibration
frozen baseline resource budget
P0 state runtime
P0 structured knowledge activation
P0 prospective gate
P0 dependency repair
semantic evaluator
paired B0/B1/P0 experiment execution
held-out H1/H2 evaluation
```

## Main conclusion

The strong baseline paths are now executable independently from P0.

The next meaningful evidence should come from a real strong model completing B0 and B1 on the development benchmark.

This should happen before P0 is implemented.

If B0 or B1 cannot complete the project because the model-command protocol is unnecessarily restrictive, that protocol should be repaired before P0 exists. Otherwise P0 could accidentally gain an advantage from a treatment interface tuned only for structured-state behavior.

## Next milestone

The next milestone is **real-model baseline calibration**.

It should establish, for one provisional experiment model configuration:

```text
structured-command reliability
reasonable maximum model-call/token budget
whether B0 completes the benchmark without extra methodological knowledge
whether B1 uses the static knowledge effectively
common-tool usability
whether command/recovery behavior is fair
what outputs must be preserved for later blinded semantic evaluation
```

The provider/model configuration is an experimental choice, not a production architecture decision.