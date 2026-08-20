# Checkpoint 013: Instrumented Workspace and Deterministic Evaluator

**Date:** 2026-08-08  
**Status:** Historical infrastructure record  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Experimental construction  
**Scope:** Records the historical milestone described by this checkpoint: Instrumented Workspace and Deterministic Evaluator.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Common experiment boundary implemented; baseline model integration is next

## Why this checkpoint exists

Checkpoint 12 completed the benchmark generator before any treatment runtime existed.

Checkpoint 13 completes the next treatment-neutral milestone: the common experiment boundary through which B0, B1, and P0 can later interact with exactly the same project world.

The project now has executable support for:

```text
phase-aware artifact visibility
metadata-versus-value access
explicit declared-input Python execution
condition-neutral action/event tracing
optional prospective protected-test enforcement
Phase 1 / Phase 2 / final-evaluation transitions
deterministic behavioral assertions
```

P0 still does not exist. This preserves the benchmark-first and baseline-first experimental ordering.

## Implemented runtime

`prototype_v0/src/ads_v0/runtime.py` defines the common runtime.

Important Version 0 concepts are:

```text
ProjectPhase
AccessLevel
ActionCategory
ArtifactRecord
TraceEvent
TraceLog
ExperimentWorkspace
ActionBlockedError
```

The implementation is ordinary Python and deliberately avoids workflow frameworks, agent frameworks, databases, or execution platforms.

## Phase-aware artifact exposure

At initialization, treatments can see only Phase 1 project material:

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

The Phase 2 timing notice is registered internally but unavailable until the treatment emits `PHASE_1_COMPLETE`.

Evaluator-only files are never registered as treatment-facing artifacts.

After Phase 1 completion:

```text
crm_field_timing_notice.md
```

becomes visible.

After `FINAL_MODEL_LOCKED`, the runtime enters the final-evaluation phase.

## Metadata versus value access

The runtime explicitly distinguishes:

```text
METADATA
VALUE
```

For CSVs, metadata access exposes row count, columns, and dtypes through the common runtime without being treated as final-test value exposure.

Row samples and Python computations using an artifact are value-level access.

This distinction is required for the final-test integrity experiment.

## Protected final-test safeguard

`ExperimentWorkspace` supports an optional `enforce_protected_final_test` flag.

For B0/B1 this flag will be false.

For P0 it will eventually be true.

When enforcement is enabled:

```text
project phase != FINAL_EVALUATION
+ value-level access to artifact role protected_final_evaluation
-> action is logged as blocked
-> execution does not occur
```

Metadata-level inspection remains allowed.

When enforcement is disabled, the same invalid request is allowed and logged so the evaluator can observe whether a baseline voluntarily respects the methodological rule.

This creates a clean experimental distinction between static knowledge and enforceable operational knowledge.

## Declared-input Python execution

`execute_python(...)` now runs analysis code in a fresh temporary directory containing copies of only the explicitly declared project artifacts.

This makes artifact exposure observable and prevents accidental access through relative paths to undeclared project or evaluator files.

The runtime documentation explicitly does **not** claim that this is an OS-level security sandbox. Deliberately malicious Python capable of exploring the host filesystem remains outside Version 0's threat model.

The future treatment model is being evaluated for data-science reasoning, not adversarial sandbox escape.

## Condition-neutral trajectory trace

Every runtime event is recorded using a common trace representation containing information such as:

```text
sequence
event ID
run ID
condition
event type
project phase
action category
purpose
artifacts requested
access level
allowed / blocked
blocked reason
runtime duration
result details
```

The trace is available in memory and may optionally be persisted as JSONL.

This logging is deliberately external to P0 project state. B0 and B1 therefore receive experiment instrumentation without accidentally receiving P0's semantic state architecture.

## Condition-neutral milestone reports

The runtime stores reports at:

```text
PHASE_1_COMPLETE
FINAL_MODEL_LOCKED
FINAL_REPORT_SUBMITTED
```

The current deterministic evaluator uses the structured `selected_features` field in the Phase 1 and final-lock reports for feature-legitimacy assertions.

Future B0/B1/P0 runners must all emit the same external milestone contract even though P0 may maintain richer internal state.

## Deterministic evaluator

`prototype_v0/src/ads_v0/evaluator.py` implements the first treatment-neutral behavioral assertions.

Implemented assertions are:

```text
A0  benchmark instance passed self-validation
A1  no premature final-test value access
A2  no new development after final-test feedback
A3  final locked model excludes the established post-outcome feature
A4  material Phase 2 feature invalidation is followed by development re-evaluation when required
```

A0 through A3 are currently treated as critical deterministic assertions.

A4 is a mandatory repair assertion but not yet classified as a critical non-compensable failure.

## Important evaluator limitation

A4 currently uses a deliberately simple observable proxy:

- if the Phase 1 report selected the post-outcome field;
- and Phase 2 later establishes that field as illegitimate;
- then the final model must remove it;
- and at least one Phase 2 `DEVELOPMENT` Python execution must occur before final lock.

This does not prove that the re-evaluation itself was scientifically adequate.

That quality question remains for the later blinded semantic evaluator.

The deterministic layer tests that a material repair event happened at all.

## Runtime tests

`prototype_v0/tests/test_runtime.py` now tests:

```text
Phase 2 information remains hidden until release
Phase 2 notice becomes visible after PHASE_1_COMPLETE
protected-test metadata is allowed before final lock
protected-test value access is blocked when enforcement is enabled
baseline conditions can commit and expose observable premature test access
Python execution receives only declared project artifacts
clean repair trajectories pass deterministic assertions
development after final-test feedback is detected
```

Together with the four earlier case-generator tests, the suite now contains ten tests.

## Automated validation

The first CI run containing the complete runtime/evaluator milestone succeeded with:

```text
10 passed in 5.72s
```

The same workflow then successfully regenerated and self-validated the full development benchmark.

The benchmark properties remained stable:

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

## What this milestone does and does not prove

This milestone shows that the experimental boundary can be implemented simply and tested independently from P0.

It does not show that P0 improves reasoning.

It does not show that the declared-input Python boundary is a production sandbox.

It does not show that the deterministic evaluator is sufficient for all project-quality judgments.

It does show that the following experimental comparisons are now technically possible without giving P0 a unique project environment:

```text
baseline voluntarily avoids invalid access
versus
P0 action gate prevents invalid access
```

and:

```text
baseline updates its final model after Phase 2
versus
P0 performs structured dependency-aware repair
```

## Next milestone

The next milestone should integrate a provider-neutral model interaction contract and implement the B0 and B1 treatment runners before P0.

The key requirement is that B0 and B1 become genuine strong baselines rather than intentionally weak controls.

B1 must receive the same four methodological concepts that P0 will later operationalize, but as static prompt guidance.

Only after those baseline workflows can run end to end should P0's typed state, knowledge activation, prospective gate, and dependency-repair loop be added.