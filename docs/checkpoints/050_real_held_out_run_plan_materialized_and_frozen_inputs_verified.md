# Checkpoint 50: Real Held-Out Run Plan Materialized and Frozen Inputs Verified

**Date:** 2026-08-10  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution preparation  
**Scope:** Records the historical milestone described by this checkpoint: Real Held-Out Run Plan Materialized and Frozen Inputs Verified.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the first execution-time verification of the real local H1/H2 held-out bundles and the successful materialization of the preregistered 30-slot run plan before any held-out treatment inference.

No H1/H2 treatment model call has occurred.

## Deterministic validation immediately before materialization

The user pulled the held-out planning implementation and ran the complete local suite:

```text
62 passed in 9.77s
```

This validated the common B0/B1 resource envelope, frozen-bundle verification, exact run-order materialization, replacement-attempt identifiers, and plan overwrite protection.

## Real local bundle verification

The user then ran:

```bash
python -m ads_v0.heldout_execution
```

The command performs no model inference. It verified the real git-ignored local H1/H2 directories against the bundle identities frozen before P0 implementation.

Observed output:

```text
Protocol: v0.1.0
Validated bundles: H1, H2
H1: seed=811 files=9 sha256=7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
H2: seed=1601 files=9 sha256=44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
Run slots: 30
Output: C:\Projects_Data\autonomous-data-science-system\prototype_v0\results\held_out\run_plan.json
```

The observed identities exactly match the preregistered and committed freeze record.

## Meaning of the materialized plan

`results/held_out/run_plan.json` is now the local execution plan for the confirmatory experiment. It links:

```text
protocol version v0.1.0
verified H1/H2 bundle identities
registered treatment model/resource configuration
exact 30-slot interleaved H1/H2 order
stable initial attempt IDs
replacement-attempt policy
```

The plan is intentionally git-ignored as execution state. It must not be overwritten or regenerated once held-out treatment execution begins.

## Execution boundary

The next implementation step is a resumable one-attempt-at-a-time executor. Before every launch it must revalidate the current local bundles and verify that the materialized plan is exactly consistent with the frozen protocol and bundle identities.

The executor must:

```text
select only the earliest unresolved preregistered slot;
launch exactly one attempt per explicit invocation;
use the registered gpt-5.6-terra / high configuration;
apply the common 24-call / 250,000-token / 12-Python envelope;
persist a pre-launch attempt marker before paid inference;
refuse to duplicate an interrupted/ambiguous attempt;
classify provider-generation terminal failures as non-behavior-evaluable;
allow at most two replacements inside the same slot;
never replace behavioral failures, budget exhaustion, Python failures, semantic mistakes, or poor methodology;
pause after three non-behavior-evaluable attempts in one slot;
never advance past an unresolved earlier slot.
```

## Current decision

The frozen inputs are now verified in the actual local execution environment and the 30-slot plan exists. Do not launch H1/H2 until the sequential executor and its failure/recovery semantics are implemented and deterministically tested.
