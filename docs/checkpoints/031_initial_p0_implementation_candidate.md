# Checkpoint 31: Initial P0 Implementation Candidate

**Date:** 2026-08-09

## Purpose

Record the first implementation of the pre-specified P0 semantic machinery after all pre-P0 experimental controls were frozen and the semantic judge calibration was accepted.

This checkpoint is an implementation candidate pending local deterministic test execution. No real-model P0 trajectory has been run yet.

## Experimental boundary preserved

P0 implementation began only after:

```text
B0/B1 development calibration was complete;
all six baseline trajectories were semantically analyzed;
held-out protocol v0.1.0 was preregistered;
H1/H2 exact bundles were frozen and fingerprinted;
semantic rubric and continuation/falsification thresholds were frozen;
two-pass condition-blinded judge calibration completed with 59/60 exact
criterion agreement, no extreme disagreement, and no manual adjudication.
```

No held-out benchmark or evaluator rule was changed while implementing P0.

## New implementation files

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_schema.py
prototype_v0/src/ads_v0/p0_openai_model.py
prototype_v0/src/ads_v0/calibrate_p0.py
prototype_v0/tests/test_p0.py
```

## Typed state

P0 implements the nine pre-specified state types:

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

with the type-specific Version 0 status vocabularies registered in Foundation 011.

Each state object records:

```text
canonical ID
type
status
scope
content
source references
semantic tags
created step
updated step
```

State content is immutable after object creation in this first implementation. Semantic revision is expressed through status changes, newly created objects, and explicit relations. This makes the append-only audit history easier to interpret.

## Relations and repair

The implemented relation vocabulary remains exactly:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

A broken hard `DEPENDS_ON` path triggers deterministic targeted propagation. Example transitions include:

```text
EVIDENCE -> INVALIDATED
CLAIM -> INVALIDATED
DECISION -> REOPENED
QUESTION -> REOPENED
OBLIGATION -> OPEN
```

Unrelated objects are preserved.

Loss of a `SUPPORTS` path does not blindly invalidate the target. It creates an explicit repair obligation to reassess whether remaining support is sufficient.

## Four-component knowledge library

P0 contains only the four methodological components already supplied statically to B1:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

The full library is not inserted wholesale into the P0 prompt.

Instead, scoped activations are created from project state patterns.

Current Version 0 activation signals include:

```text
inspected Python artifact
    -> K-INFO-002

prediction-moment state + inspected table schema
    -> K-INFO-003

future-prediction objective + repeated entities + temporal structure
    -> K-VAL-001

protected-final-evaluation state
    -> K-INFO-001
```

Activation is idempotent for a component/scope pair.

Activated components instantiate concrete project questions or obligations. Resolved instances can later reopen rather than creating duplicate concerns.

## Runnable frontier

Every P0 action must cite a current state motivator:

```text
open/reopened QUESTION
open OBLIGATION
reopened DECISION
project deliverable obligation
```

Blocking and repair-tagged concerns take priority over ordinary deliverable work.

The controller validates motivators before allowing the external command to execute.

ACTION objects are controller-maintained and record proposed, allowed, blocked, executed, or failed actions plus `GENERATED_BY` links to their motivators.

## Prospective protected-test gate

P0 enables the already implemented common workspace protection:

```text
enforce_protected_final_test=True
```

A proposed value-level final-test action before final model lock is recorded and blocked rather than executed.

The attempt remains visible as architecture diagnostic evidence, but is not an executed deterministic A1 failure.

## Common external command interface

P0 retains the same external commands as B0/B1:

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

The P0 model response adds only:

```text
state_patch
motivator_ids
```

around the same common command.

The semantic trajectory normalizer already ignores P0 internal state messages and extra patch fields, so the primary semantic judge continues to compare only common external behavior.

## Provider adapter

`OpenAIP0ResponsesModel` subclasses the calibrated B0/B1 OpenAI adapter.

Therefore P0 retains the same:

```text
provider
model family
reasoning effort semantics
previous_response_id threading
all-turn reasoning context
SDK retry disabling
request timeout
usage accounting
incomplete-response handling
duplicate-equal structured-output normalization
```

Only the strict Structured Outputs response schema changes to accommodate the state patch.

## Resource envelope

The P0 runner directly enforces the already registered development/held-out limits:

```text
24 successful treatment model calls
250,000 observed total treatment tokens
12 Python execution attempts
2 additional generation retries per semantic turn
```

A provider call that crosses the cumulative token limit remains part of the trajectory, but no later model call is allowed.

Architecture-internal deterministic state operations do not consume hidden LLM budget.

## P0 diagnostic outputs

The development CLI writes the same common artifacts as baseline calibration plus:

```text
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

These are architecture diagnostics and remain excluded from the blinded primary semantic score.

## Deterministic test coverage added

The new tests exercise:

```text
hard dependency propagation with unrelated-state preservation;
SUPPORTS loss causing reassessment rather than blind invalidation;
idempotent learned-transformation knowledge activation;
generalization and feature-eligibility activation from state patterns;
prospective protected-test blocking;
minimal P0 runner completion;
semantic normalizer exclusion of P0_STATE_VIEW and state_patch;
P0 OpenAI adapter use of the P0 strict schema;
strict P0 schema structure and reuse of the common command contract.
```

The repository test suite has not yet been rerun locally after these new files in this checkpoint. That is the immediate next step.

## Next step

Pull the implementation and run the full deterministic test suite.

If all tests pass, record the validated implementation boundary and run the first real-model P0 development-calibration trajectory on the development case only.

Held-out H1/H2 remain untouched until P0 development debugging is complete.
