# Checkpoint 49: Held-Out Plan Layer Deterministically Validated

**Date:** 2026-08-10  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution preparation  
**Scope:** Records the historical milestone described by this checkpoint: Held-Out Plan Layer Deterministically Validated.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record deterministic validation of the common held-out bundle-validation and run-plan materialization layer before any H1/H2 treatment execution.

No held-out treatment model call has occurred.

## Validation result

The user pulled the implementation introduced in Checkpoints 47-48 and ran the complete local suite from `prototype_v0`:

```text
.............................................................. [100%]
62 passed in 9.77s
```

This validates the current deterministic suite after adding:

```text
common B0/B1 24-call / 250,000-token / 12-Python held-out envelope support;
execution-time H1/H2 fingerprint verification;
exact 30-slot preregistered H1/H2 schedule materialization;
stable initial/replacement attempt identifiers;
plan overwrite protection;
registered treatment-resource snapshot checks.
```

The result does not constitute held-out evidence because no H1/H2 treatment inference has run.

## Frozen identities to verify locally

The committed pre-P0 bundle record remains authoritative:

```text
H1
seed: 811
file count: 9
aggregate SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
seed: 1601
file count: 9
aggregate SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

The next local command should validate the actual git-ignored `generated/held_out/H1` and `H2` directories against those frozen identities and write the real execution plan to:

```text
results/held_out/run_plan.json
```

This command performs no model inference:

```bash
python -m ads_v0.heldout_execution
```

Do not use `--force`. If the plan path already exists, stop and inspect it rather than overwriting it.

## Boundary after plan materialization

After the real local plan is materialized and its output is inspected, implement a resumable one-attempt-at-a-time held-out executor. It must:

```text
revalidate protocol/bundle identity before every launch;
read the immutable 30-slot plan rather than recomputing order ad hoc;
select only the earliest unresolved preregistered slot;
launch exactly one attempt per invocation;
use B0/B1 or frozen P0 according to the slot condition;
pass the registered model and 24 / 250k / 12 resource envelope explicitly;
persist attempt metadata before and after execution;
classify provider/infrastructure termination separately from behavioral outcomes;
allow at most two replacements only for non-behavior-evaluable provider/infrastructure termination;
never replace poor methodology, Python failures/timeouts, semantic mistakes, deterministic failures, or treatment budget exhaustion;
never skip ahead while a slot is unresolved;
never begin semantic judging while treatment execution is still being assembled or debugged.
```

P0 behavioral/controller logic remains frozen.

## Current decision

The deterministic planning layer is green. The immediate next action is to materialize and inspect the real frozen local run plan, still with zero paid inference, before wiring the paid `run-next` executor.
