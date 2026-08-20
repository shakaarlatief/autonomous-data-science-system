# Checkpoint 46: Common Baseline Resource Envelope Implemented

**Date:** 2026-08-10  
**Status:** Historical infrastructure record  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Prototype V0 held-out execution preparation  
**Scope:** Records the historical milestone described by this checkpoint: Common Baseline Resource Envelope Implemented.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Implement the preregistered held-out resource envelope for B0 and B1 after P0 behavioral/controller logic was formally frozen.

This is common experiment-control engineering. It does not change B0/B1 methodological prompts, P0 behavior, held-out bundles, semantic criteria, or continuation/falsification thresholds.

No H1/H2 treatment run has occurred.

---

## 1. Registered requirement

Foundation 012 requires every held-out treatment condition to use the same hard envelope:

```text
maximum successful model calls: 24
maximum observed total tokens: 250,000
maximum Python execution attempts: 12
maximum output tokens per provider call: 30,000
maximum additional generation retries: 2
```

The total-token rule is post-observation:

```text
if prior cumulative observed usage is already >= 250,000,
no new treatment model call may begin;

if an admitted completed provider call crosses the ceiling,
that call remains in the trajectory,
the run is marked budget-exceeded,
and no later model call may begin.
```

Observable usage from failed provider attempts counts. Python exceptions and timeouts count when execution is actually attempted.

P0 already enforced these limits. B0/B1 previously enforced only the successful-model-call ceiling, so held-out execution was not yet allowed.

---

## 2. Baseline runner changes

`BaselineTreatmentRunner` now supports:

```text
max_model_calls
max_total_tokens
max_python_execution_attempts
max_generation_retries
```

The token and Python ceilings are optional at the runner API so historical development-calibration commands remain reproducible. Held-out orchestration must pass the frozen values explicitly.

`TreatmentRunResult` now records:

```text
completed
completed_within_budget
budget_exhausted
model_calls
generation_attempts
generation_failures
input_tokens
output_tokens
total_tokens
python_execution_attempts
```

This aligns the resource-result surface with P0 without giving B0/B1 any P0-only semantic machinery.

---

## 3. Token enforcement semantics

The baseline loop now checks the cumulative token budget before each model call and before each retry attempt.

If a successful provider call crosses the ceiling, its treatment command is still admitted and executed because usage becomes observable only after the provider response is returned. The trajectory is then marked budget-exceeded and stops before another model call.

If a terminal `submit_final_report` call crosses the ceiling:

```text
completed = true
budget_exhausted = true
completed_within_budget = false
```

This matches the already corrected P0 accounting semantics and Foundation 012.

Failed provider attempts that report observable usage can also cross the ceiling; no further retry is then permitted.

---

## 4. Python-attempt enforcement

Every `execute_python` operation that reaches the common runtime and produces an allowed `EXECUTE_PYTHON` event increments the baseline Python-attempt counter.

This includes model-authored Python that returns a nonzero code or times out because the runtime still records an allowed execution attempt.

When the registered attempt ceiling has already been reached, a later Python request is deterministically blocked before execution and a `PYTHON_BUDGET_BLOCK` event is recorded.

This is resource enforcement only. B0/B1 still do not receive P0's prospective protected-test safeguard.

---

## 5. Baseline CLI/result artifacts

`ads_v0.calibrate` now accepts:

```text
--max-total-tokens
--max-python-execution-attempts
```

and writes the new common resource fields to `summary.json`.

The two new limits default to `None` in the development CLI so the previously recorded B0/B1 calibration trajectories remain reproducible. Held-out execution must not rely on those defaults; it will read and pass the frozen protocol values.

---

## 6. Regression coverage

Four baseline tests were added or strengthened to verify:

```text
a crossing provider call is retained and prevents later calls;
a terminal completion call above the token ceiling is budget-exceeded;
the Python-attempt ceiling blocks the next execution;
optional token/Python limits reject nonpositive values.
```

Existing clean-trajectory coverage now also checks `completed_within_budget`, `budget_exhausted`, and Python-attempt accounting.

Expected full suite after this checkpoint:

```text
58 passed
```

Local deterministic validation is still required before held-out orchestration is built on top of this runner.

---

## 7. Experimental boundary

Unchanged:

```text
B0 prompt
B1 static four-concept prompt
P0 frozen behavior/controller logic
P0 four knowledge components
H1/H2 frozen bundles and fingerprints
semantic rubric and judge
run ordering
provider/model/reasoning configuration
24-call ceiling
250,000-token ceiling
12-Python ceiling
continuation/falsification thresholds
```

No treatment run was executed while implementing this common resource layer.

---

## Next step

Run the complete local test suite.

If all 58 tests pass, proceed to deterministic held-out orchestration: load the registered protocol, verify frozen bundle fingerprints, materialize the exact 30-slot preregistered run plan, and support replacement-attempt identifiers without changing slot order.
