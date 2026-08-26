# Checkpoint 165: Specification 019 Governed Live Authorization Frozen

**Date:** 2026-08-23  
**Status:** EXACT GOVERNED LIVE AUTHORIZATION FROZEN  
**Checkpoint class:** LIVE AUTHORIZATION / CONTROL-PLANE BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes one exact Specification 018 launch authorization for the already preregistered and cross-platform validated Specification 019 experiment.  
**Authority:** Historical authorization boundary. Research 026, Specification 019 v0.1, its frozen overlay fixture, and immutable Specification 017 benchmark truth remain scientific authority. Specification 018 governs launch transport. This checkpoint authorizes one exact live source only and does not alter the experiment contract.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Development branch:** `v1-recommendation-action-value-system-provenance`  
**PR:** #33 -> `v1-frontend-spike`

## 1. Frozen live source

A dedicated live-source ref has been pinned to the exact checkpoint-containing provider-free green commit:

```text
ref
    v1-spec019-system-provenance-live-source

source SHA
    6b5e6237b738250458550f95c9f3a6b0d51e86ec
```

The ref was verified to resolve exactly to that commit before this authorization was frozen.

The moving development branch is not the live dispatch ref. This keeps later evidence-preservation and documentation commits from changing the provider-backed source.

## 2. Exact required CI evidence

The frozen live source passed:

```text
V1 system-owned provenance recommendation action
    run 32664369953
    source 6b5e6237b738250458550f95c9f3a6b0d51e86ec
    Ubuntu success
    Windows success
    targeted Specification 019 tests 13 passed on each OS
    full V1 suite 116 passed, 2 skipped on each OS
    ordinary CI provider credential absent

Checkpoint metadata
    run 32664369955
    source 6b5e6237b738250458550f95c9f3a6b0d51e86ec
    success
```

## 3. Exact launch authorization

Exactly one registry entry is authorized:

```json
{
  "launch_id": "spec019-system-provenance-001",
  "enabled": true,
  "owner_login": "shakaarlatief",
  "workflow_file": "v1-system-owned-provenance-recommendation-action-live.yml",
  "ref": "v1-spec019-system-provenance-live-source",
  "expected_source_sha": "6b5e6237b738250458550f95c9f3a6b0d51e86ec",
  "confirmation": "RUN_SPEC_019_FROZEN",
  "required_ci_runs": [
    {
      "run_id": 32664369953,
      "workflow_name": "V1 system-owned provenance recommendation action"
    },
    {
      "run_id": 32664369955,
      "workflow_name": "Checkpoint metadata"
    }
  ]
}
```

No other workflow, ref, SHA, confirmation, model, prompt, secret, or dispatch argument is authorized by this checkpoint.

## 4. Independent target-workflow boundary

The frozen target workflow independently requires:

```text
launch_id == spec019-system-provenance-001
confirmation == RUN_SPEC_019_FROZEN
github.sha == expected_source_sha
OPENAI_API_KEY present inside the explicit live workflow
```

The launcher itself receives no provider credential.

The target reruns the provider-free Specification 019 preflight before provider execution and uploads the complete result directory even when the experiment exits nonzero after provider execution.

## 5. Issue transport

The only accepted connected-interface launch request is:

```text
title
    [ADS LIVE] spec019-system-provenance-001

body
    authorization: RUN_SPEC_019_FROZEN
```

The issue is transport only. The default-branch registry remains executable authorization.

## 6. Frozen provider plan unchanged

This authorization does not change any Specification 019 treatment:

```text
4 cases
3 conditions
3 repetitions
36 planned successful reasoner calls
36 planned successful judge calls
72 planned successful provider calls
90 maximum provider attempts
randomization seed 2026082304
reasoner gpt-5.6-sol / medium
judge gpt-5.6-sol / high
OpenAI Agents SDK 0.19.4
```

The model/runtime values remain experiment constants only.

## 7. No scientific conclusion yet

This checkpoint does not classify Specification 019 as:

```text
PROMOTE_SYSTEM_PROVENANCE_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Those outcomes are permitted only after a complete scored provider-backed design with execution integrity, according to the frozen evaluator.

If the live run is incomplete or execution integrity fails, no advancement outcome may be assigned.

## 8. Exact next action

```text
1. place exactly the authorization above into main:.github/ads_live_experiments.json
2. create the exact owner [ADS LIVE] issue through the connected GitHub interface
3. allow Specification 018 to validate source, CI, duplicate state, and dispatch
4. observe the target live run
5. preserve every raw result/attempt artifact before interpretation
6. apply only the frozen Specification 019 advancement rule
7. retire the one-shot registry authorization after evidence is secured
```

At this checkpoint, the provider-backed run is explicitly authorized only through the exact governed path above.
