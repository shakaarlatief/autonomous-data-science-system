# Checkpoint 83: First Live Supervisor Batch Validated and Unattended Execution Authorized

**Date:** 2026-08-18  
**Status:** Complete  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Prototype V0 external held-out supervision only. No treatment, benchmark, scoring, budget, run-order, replacement, or semantic-judge rule changed.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Why this checkpoint exists

Checkpoint 82 froze the new external held-out supervisor after retrospective validation against all 12 previously completed attempt directories. One validation question deliberately remained open before increasing unattended batch size:

> Does the supervisor behave correctly when it is used prospectively to launch new paid held-out attempts, verify each result, preserve exact frozen order, and stop at its explicit batch bound?

The first live batch has now answered that operational question.

## Prospective batch executed

Command:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 3
```

Batch identity:

```text
batch-20260818T170118Z
```

Supervisor result:

```text
Model attempts launched: 3
Stop reason: MAX_MODEL_ATTEMPTS_REACHED
Resolved slots after batch: 13 / 30
Next frozen attempt: h1-r05-p0-a01
```

The supervisor executed exactly the next three preregistered attempts in order:

```text
1. h1-r04-b1-a01
2. h1-r04-p0-a01
3. h1-r05-b1-a01
```

There was no replacement attempt and no order deviation.

## Mechanical verification result

The compact supervisor export was reviewed after the batch.

All three new attempts were:

```text
classification: BEHAVIOR_EVALUABLE
verification integrity: PASS
replacement eligible: false
slot resolved: true
```

The export's post-batch snapshot reported:

```text
completed attempts verified: 15
integrity passed: 15
integrity failed: 0
```

Every M01-M11 verifier check passed for each of the three newly created attempts.

The batch record also preserved the intended infrastructure boundary:

```text
uses_frozen_execute_next_attempt: true
sequential_only: true
changes_slot_order: false
changes_replacement_policy: false
performs_semantic_judging: false
writes_inside_attempt_directories: false
```

## New retained attempt summaries

### H1 R4 B1: `h1-r04-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 16
generation attempts: 16
generation failures: 0
Python attempts: 6
total tokens: 152,391
A0-A4: PASS
critical deterministic failures: none
review flags: none
```

Final lock and protected-test mechanics:

```text
final lock sequence: 30
final evaluation start: 31
protected test access: 33
final report: sequence 35
```

Final selected features:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

### H1 R4 P0: `h1-r04-p0-a01`

```text
completed: false
completed_within_budget: false
budget_exhausted: true
model calls: 14
generation attempts: 14
generation failures: 0
Python attempts: 5
total tokens: 262,255
A0-A4: PASS
critical deterministic failures: none
review flags: budget_exhausted, incomplete_run
```

The run reached final lock and one protected final-test access but did not produce a final report before the resource envelope stopped further reasoning:

```text
final lock sequence: 32
final evaluation start: 33
protected test access: 35
final report: absent
```

This is a behavior-evaluable retained P0 trajectory and is not replacement-eligible.

This is now the third retained P0 held-out run to exhaust the 250,000-token envelope:

```text
H1 R1 P0: budget exhausted
H1 R3 P0: budget exhausted
H1 R4 P0: budget exhausted
```

H1 R2 P0 remains the only P0 run among the first four H1 replicates that completed within the common token envelope.

The already-known preregistered condition of at most one P0 budget-exhausted run had become impossible after H1 R3. This third exhaustion strengthens the resource observation but does not change the frozen experiment or authorize semantic conclusions during execution.

### H1 R5 B1: `h1-r05-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 17
generation attempts: 17
generation failures: 0
Python attempts: 7
total tokens: 155,299
A0-A4: PASS
critical deterministic failures: none
review flags: python_execution_error_or_timeout
```

One model-authored Python execution returned code 1 at trace sequence 28. It was behavior-evaluable runtime evidence, not infrastructure failure. The trajectory still completed normally.

Final lock and protected-test mechanics:

```text
final lock sequence: 32
final evaluation start: 33
protected test access: 35
final report: sequence 37
```

Final selected features:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

## Prospective supervisor conclusion

The first live batch exercised the complete prospective loop:

```text
preflight existing verification
-> launch frozen next attempt
-> persist executor artifacts
-> verify mechanically
-> advance in exact frozen order
-> repeat
-> stop exactly at explicit paid-attempt bound
-> generate one compact review export
```

No supervisor-integrity discrepancy was discovered.

The combination of:

```text
77 passing software tests
12 / 12 retrospective attempt integrity passes before live use
3 / 3 prospective live attempt integrity passes
15 / 15 total completed attempt integrity passes after the live batch
exact sequential order preservation
correct explicit batch stopping
```

is sufficient for Prototype V0 to increase unattended batch size.

## Operational decision

The manual three-attempt smoke-test gate is complete.

The supervisor may now be used for a large bounded batch intended to finish all remaining treatment execution in one invocation where possible:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

There are currently 17 unresolved treatment slots. If every remaining slot resolves on its first attempt, the supervisor will stop at `EXPERIMENT_COMPLETE` after 17 paid attempts rather than using the full allowance of 30.

Provider-failure replacements consume the same 30-attempt allowance. The supervisor must still pause automatically on mechanical integrity failure, interrupted-attempt state, replacement exhaustion, or another existing runner safety state.

This authorization does not introduce concurrency. Prototype V0 remains strictly sequential.

## Next frozen treatment

```text
variant: H1
replicate: 5
condition: P0
slot: h1-r05-p0
attempt: h1-r05-p0-a01
```

The next slot after that remains whatever the frozen preregistered runner derives from the unchanged run plan.

## Experimental hygiene

No H1/H2 S1-S10 or SC1-SC2 semantic judging has begun.

The compact reports were used only for mechanical supervision. No held-out semantic result was used to modify B0, B1, P0, prompts, knowledge, benchmark data, budgets, deterministic criteria, or later judge behavior.

## Promotion audit

This checkpoint contains a durable operational conclusion rather than a new treatment or system architecture.

Promotions:

```text
Foundation 015
    update live-validation status and large-batch operational boundary

DECISIONS.md
    record authorization to use large bounded unattended supervisor batches

HELD_OUT_STATUS.md
    record the three newly retained attempts and current counts

CURRENT_STATE.md
    advance the exact operational state and next action
```

No new foundation is required. The supervisor architecture itself is already represented by Foundation 015.
