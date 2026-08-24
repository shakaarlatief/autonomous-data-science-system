# Checkpoint 177: Specification 021 Live Source Frozen

**Date:** 2026-08-24  
**Status:** EXACT LIVE-CAPABLE SOURCE FROZEN; PROVIDER CALL NOT YET AUTHORIZED  
**Checkpoint class:** LIVE SOURCE / PRE-AUTHORIZATION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the exact Specification 021 source that adds only a separately governed provider-capable wrapper, target workflow, provider-free tests, and the lifecycle correction required for the pre-authorization invariant after Checkpoint 176 permitted those live surfaces.  
**Authority:** Makes the exact source eligible for one later Specification 018 repository authorization. It does not itself authorize a provider call and does not modify Specification 021's frozen scientific contract.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-dependency-backed-recommendation-value`  
**PR:** #55 draft  
**Specification:** 021

## 1. Prior frozen boundaries

Scientific contract:

```text
Specification 021 v0.1
Checkpoint 174
```

Provider-free implementation gate:

```text
Checkpoint 175
validated implementation head 8e199c29e3f082b353f92f27868aedca0ebbbf74
```

Exact reconciled pre-live boundary:

```text
Checkpoint 176
validated pre-live source aa830eda4fe80bc349afcb4f3bd0ab53f37bfcc7
```

No Specification 021 provider call occurred before this checkpoint.

## 2. Exact live-capable source

The exact source validated immediately before this checkpoint is:

```text
b589bad975880b2d3cccc3596fc82539b1b96577
```

It has been pinned to the dedicated historical live-source ref:

```text
v1-spec021-dependency-backed-recommendation-value-live-source
```

That ref points directly to the exact validated source and must not move during this authorization cycle.

## 3. Live-capable additions after Checkpoint 176

Only bounded execution plumbing was added:

```text
experiments/dependency_backed_recommendation_action_value/live_runner.py
tests/unit/test_dependency_backed_recommendation_action_live_runner.py
.github/workflows/v1-dependency-backed-recommendation-action-live.yml
```

The ordinary Specification 021 workflow was extended only to validate the live-boundary files provider-free and to require that the one-shot Specification 021 repository authorization still be absent.

No fixture, frozen evaluator truth, condition treatment, semantic-judge rubric, randomization, model configuration, metric, gate threshold, value-signal definition, or scientific outcome rule changed.

## 4. Separation of frozen science and provider execution

The existing provider-neutral runner remains:

```text
experiments/dependency_backed_recommendation_action_value/runner.py
```

The new `live_runner.py` only:

```text
instantiates the accepted ADS OpenAI Agents reasoning runtime
calls the existing frozen experiment runner
uses the existing frozen Specification 021 semantic judge path
adds one execution annotation after completion
rewrites result.json with that execution annotation
exposes the explicit governed CLI entry point
```

It does not alter the frozen scientific result content, plan, treatment, gates, or outcome.

Importing the live module does not call a provider.

## 5. Frozen target-workflow boundary

Target workflow:

```text
.github/workflows/v1-dependency-backed-recommendation-action-live.yml
```

It accepts exactly the three inputs emitted by the accepted Specification 018 launcher:

```text
launch_id
expected_source_sha
confirmation
```

Frozen launch identity:

```text
launch_id      spec021-dependency-backed-recommendation-value-001
confirmation   RUN_SPEC_021_FROZEN
```

The target independently requires:

```text
exact frozen launch_id
exact frozen confirmation
expected_source_sha == github.sha
lowercase 40-hex source identity
OPENAI_API_KEY present only for the explicit live job
```

Before the first provider call, the workflow clears `OPENAI_API_KEY` and runs the frozen provider-free Specification 021 harness, live-wrapper, and complete fake-runtime integration tests. The live job checks out only the repository-authorized source SHA and uploads the complete result directory even if later execution fails.

Issue text cannot define a model, prompt, command, benchmark, fixture, workflow, ref, or source SHA.

## 6. Live-boundary lifecycle defect caught and repaired before freeze

The first provider-free validation after adding the permitted live workflow failed in run:

```text
32724023671
```

The frozen provider-neutral runner still carried the implementation-stage invariant:

```text
DBRA-INV-24_no_live_surface
```

Checkpoint 176 had already authorized creation of the separated live wrapper and target workflow while still prohibiting repository authorization and provider calls. The invariant therefore rejected the exact lifecycle transition Checkpoint 176 had permitted.

The repair was narrow and governance-only:

```text
DBRA-INV-24_no_live_surface
    -> DBRA-INV-24_pre_authorization_boundary
```

The replacement invariant requires the one-shot Specification 021 entry to remain absent from `.github/ads_live_experiments.json` until this exact live source is frozen. It does not prohibit the now-authorized wrapper/workflow files themselves.

No scientific input, truth label, relation, condition, metric, gate, value signal, retry rule, provider treatment, or allowed outcome changed.

## 7. Exact green validation of the live-capable source

All required workflows associated with exact source `b589bad975880b2d3cccc3596fc82539b1b96577` completed successfully:

```text
V1 dependency-backed recommendation action value  run 32724242554  success
Current routing consistency                       run 32724242550  success
Checkpoint metadata                               run 32724242502  success
V1 reasoning context value                        run 32724242572  success
V1 disposition semantics diagnostic               run 32724242509  success
V1 blocking calibration diagnostic                run 32724242515  success
V1 autonomous live experiment launcher CI         run 32724242570  success
```

Specification 021 jobs:

```text
Windows  job 97421896915  success
Ubuntu   job 97421897042  success
```

Both jobs passed:

```text
OPENAI_API_KEY absent in ordinary CI
Specification 021 repository authorization absent
application/domain provider-neutrality check
frozen provider-free Specification 021 gates
live-wrapper provider-free tests
complete fake-runtime experiment
full V1 Python regression suite
```

No provider call occurred in these workflows.

## 8. Scientific contract remains unchanged

The exact live-capable source still executes:

```text
4 prospective cases
3 conditions: GENERIC / SELECTIVE / FULL_HORIZON
3 repetitions per condition per case
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
90 maximum provider attempts
randomization seed 2026082402
fixed gpt-5.6-sol / OpenAI Agents treatment
no tools
no project mutation
```

Allowed complete outcomes remain exactly:

```text
PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Incomplete or integrity-failed execution receives no advancement classification.

Specifications 015-020 remain immutable historical evidence and are not rescored.

## 9. Authorization boundary

At this checkpoint:

```text
exact live-capable source        frozen
immutable live-source ref        created
target workflow                  present on frozen source
provider-free CI                 green
main target-workflow exposure    not yet installed
Spec021 registry authorization   absent
Spec021 launch issue             absent
provider calls                   0
```

Therefore:

```text
provider calls authorized by Checkpoint 177 = 0
```

The next step may expose the identical frozen target workflow on `main`, add one exact Specification 018 authorization, and create one exact owner launch request.

## 10. Exact authorization values

Any authorization created after this checkpoint must use exactly:

```text
launch_id            spec021-dependency-backed-recommendation-value-001
workflow_file        v1-dependency-backed-recommendation-action-live.yml
ref                  v1-spec021-dependency-backed-recommendation-value-live-source
expected_source_sha  b589bad975880b2d3cccc3596fc82539b1b96577
confirmation         RUN_SPEC_021_FROZEN
owner_login          shakaarlatief
```

Required CI evidence must refer only to successful runs on exact source `b589bad975880b2d3cccc3596fc82539b1b96577` and must satisfy the accepted Specification 018 launcher's exact-head checks.

Only one provider-backed launch is intended. The bounded duplicate rule must reject another workflow-dispatch run for this same target workflow/source SHA.

## 11. Exact continuation

```text
1. reconcile routing/current-state pointers to Checkpoint 177
2. validate the checkpointed routing head
3. expose the identical frozen target workflow on main for workflow-dispatch discoverability
4. add one exact enabled Specification 018 authorization on main
5. create one owner-authored [ADS LIVE] issue with only the frozen launch ID and confirmation
6. verify launcher acceptance and exact target run identity
7. make no scientific interpretation from partial outputs
8. preserve the complete raw result artifact before tuning or interpretation
9. classify only with the frozen Specification 021 gates
10. retire the one-shot authorization/default-branch target exposure after preservation
11. do not modify or rescore Specifications 015-020
```
