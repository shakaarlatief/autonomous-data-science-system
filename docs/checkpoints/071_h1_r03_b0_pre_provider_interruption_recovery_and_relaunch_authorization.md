# Checkpoint 71: H1 R3 B0 pre-provider interruption recovery and relaunch authorization

**Date:** 2026-08-18  
**Status:** Historical mixed checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Frozen held-out execution  
**Scope:** Records the historical milestone described by this checkpoint: H1 R3 B0 pre-provider interruption recovery and relaunch authorization.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Event

The first local invocation intended to launch `h1-r03-b0-a01` did not reach the provider. The OpenAI client raised a missing-credentials error during construction because the new terminal session did not contain `OPENAI_API_KEY`.

The held-out executor had already created:

```text
results/held_out/attempts/h1-r03-b0-a01/attempt_started.json
```

before entering the treatment runner, so later `run-next` and `status` calls correctly reported `INTERRUPTED_ATTEMPT` and refused to duplicate a potentially paid attempt.

## Mechanical verification

The user verified that the API key is now available in the environment:

```text
OPENAI_API_KEY set: True
```

The interrupted directory contained exactly one persisted file:

```text
attempt_started.json
```

There was no `summary.json`, `attempt_record.json`, `trace.jsonl`, conversation artifact, model output, or Python-execution artifact. Together with the original traceback, which terminated while constructing the OpenAI client, this establishes that no provider generation request or treatment execution occurred.

This event therefore does not consume a preregistered treatment attempt and must not advance the slot to `a02`.

## Audit-preserving recovery

Rather than deleting the start marker, the directory was moved outside the executor's treatment-attempt ledger to:

```text
results/held_out/pre_provider_interruptions/h1-r03-b0-a01_missing_api_key_20260818T1133/
```

This preserves the administrative evidence while restoring the treatment ledger to its genuine pre-inference state.

A subsequent no-inference status check returned:

```text
Status: READY_INITIAL
Resolved slots: 7/30
Next attempt: h1-r03-b0-a01
Initial attempt is ready for earliest unresolved slot h1-r03-b0.
Model attempt launched: False
```

## Experimental classification

This is an administrative pre-provider interruption, not a behavior-evaluable treatment attempt and not a non-behavior-evaluable provider/interface attempt under the preregistered replacement policy. No model inference, paid provider generation, Python execution, treatment behavior, or semantic evidence occurred.

The frozen treatment configuration, prompts, budgets, provider-normalization behavior, run order, bundles, and controller remain unchanged.

## Current counts

```text
resolved treatment slots: 7 / 30
behavior-evaluable retained attempts: 7
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

## Next authorized action

The genuine initial treatment attempt remains:

```text
variant: H1
replicate: 3
condition: B0
slot: h1-r03-b0
attempt: h1-r03-b0-a01
```

Exactly one `python -m ads_v0.heldout_runner run-next` invocation is authorized after pulling this checkpoint. Stop immediately after the executor result and inspect `h1-r03-b0-a01` before any H1 R3 B1 execution.
