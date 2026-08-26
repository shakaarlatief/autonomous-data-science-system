# Checkpoint 170: RECOMMENDED versus BLOCKING_REQUIRED Calibration Live Source Frozen

**Date:** 2026-08-24  
**Status:** EXACT LIVE-CAPABLE SOURCE FROZEN  
**Checkpoint class:** LIVE SOURCE / PRE-AUTHORIZATION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the exact Specification 020 source that adds only a separately governed provider-capable entry path and target workflow around the already frozen provider-neutral diagnostic.  
**Authority:** Makes this exact source eligible for one later Specification 018 authorization. It does not itself authorize a provider call.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-blocking-calibration-diagnostic`  
**PR:** #44 draft  
**Specification:** 020

## 1. Prior frozen boundaries

Scientific contract:

```text
Specification 020 v0.1
Checkpoint 167
```

Provider-free implementation gate:

```text
Checkpoint 168
```

Exact reconciled pre-live boundary:

```text
Checkpoint 169
validated branch source b1eb5b3fb6a3364bb7b660b81120ffc82c949fc0
```

No Specification 020 provider call occurred before this checkpoint.

---

## 2. Exact live-capable source

The exact source validated immediately before this checkpoint is:

```text
82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
```

It has been pinned to the dedicated live-source ref:

```text
v1-spec020-blocking-calibration-live-source
```

That ref was created directly at the exact validated source and must not move for this authorization cycle.

---

## 3. Live-capable additions

Only bounded execution plumbing was added after Checkpoint 169:

```text
experiments/blocking_calibration/live_runner.py
.github/workflows/v1-blocking-calibration-live.yml
tests/unit/test_blocking_calibration_live_runner.py
```

The ordinary provider-free workflow was extended only to include the new live-boundary files/tests and this checkpoint path.

No fixture or frozen evaluator truth changed.

---

## 4. Separation of provider-neutral science and provider execution

The existing `experiments/blocking_calibration/runner.py` remains the scientific execution mechanism and still requires an injected `ReasoningRuntime`.

The new `live_runner.py` only:

```text
instantiates OpenAIAgentsReasoningRuntime
calls the existing frozen injected-runtime experiment
marks preserved execution metadata as live
exposes the explicit governed CLI entry point
```

It does not alter:

```text
call plan
fixture truth
model-visible evidence
structured result schema
pointer validation
retry policy
attempt budget
gate evaluation
scientific outcome
```

Importing the live module does not call a provider.

---

## 5. Frozen target-workflow boundary

Target workflow:

```text
.github/workflows/v1-blocking-calibration-live.yml
```

It accepts only the three inputs produced by the accepted Specification 018 launcher:

```text
launch_id
expected_source_sha
confirmation
```

The target independently requires:

```text
launch_id              spec020-blocking-calibration-001
confirmation           RUN_SPEC_020_FROZEN
expected_source_sha    exactly github.sha
source format           lowercase 40-hex
OPENAI_API_KEY          present only in live job
```

The workflow checks out the exact authorized SHA, clears `OPENAI_API_KEY` during the provider-free preflight test step, executes the frozen live runner only after all checks pass, and uploads the complete result bundle even when later steps fail.

Issue text cannot define a model, prompt, command, benchmark path, fixture path, workflow, ref, or source SHA. Those remain repository-controlled through Specification 018.

---

## 6. Provider-free live-boundary tests

The new provider-free tests verify that:

```text
live wrapper instantiates the provider adapter only when invoked
frozen runner result/gate content is preserved
execution metadata is changed from provider-free to live only after execution
result.json is rewritten with the correct live execution annotation
live workflow contains the frozen launch ID and confirmation
live workflow verifies authorized source identity
live workflow performs provider-free preflight before live execution
live workflow cannot accept arbitrary model/prompt/command/fixture inputs
```

No provider is contacted by these tests.

---

## 7. Exact green live-source validation

All required workflows associated with exact source `82cfbdd...` completed successfully:

```text
V1 blocking calibration diagnostic          run 32701656679  success
V1 reasoning context value                   run 32701656608  success
V1 disposition semantics diagnostic          run 32701656627  success
V1 autonomous live experiment launcher CI   run 32701656597  success
Checkpoint metadata                          run 32701656653  success
```

Specification 020 jobs:

```text
Ubuntu   job 97354264763   success
Windows  job 97354264391   success
```

Both jobs passed the dedicated provider-free gate and the full V1 Python regression suite. The ordinary CI credential check passed with `OPENAI_API_KEY` absent.

---

## 8. Scientific contract checksum by construction

The live-capable implementation did not modify the frozen authority:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
tests/fixtures/reasoning/blocking_calibration_v1.json
```

The experiment remains:

```text
6 pairs
12 variants
36 planned successful reasoner outputs
45 maximum provider attempts
seed 2026082401
BC-G01 through BC-G06
no methodology treatment
no semantic judge
no tools
no project mutation
```

Allowed outcomes remain exactly:

```text
BLOCKING_BOUNDARY_SUPPORTED
BLOCKING_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

---

## 9. Authorization boundary

At this checkpoint:

```text
exact live-capable source     frozen
immutable live-source ref     created
target workflow               present on frozen source
provider-free CI              green
main workflow exposure        not yet installed
Spec020 registry entry        absent
Spec020 launch issue          absent
provider calls                0
```

Therefore:

```text
provider calls authorized by Checkpoint 170 = 0
```

The next step may install one exact repository authorization and default-branch workflow exposure only as required by the accepted Specification 018 control plane.

---

## 10. Exact next authorization

Any authorization created after this checkpoint must use exactly:

```text
launch_id            spec020-blocking-calibration-001
workflow_file        v1-blocking-calibration-live.yml
ref                  v1-spec020-blocking-calibration-live-source
expected_source_sha  82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
confirmation         RUN_SPEC_020_FROZEN
```

The required CI evidence must include the exact successful run IDs frozen above and must pass the Specification 018 launcher's exact-head validation.

Only one provider-backed launch is intended. Duplicate protection must reject a second workflow-dispatch run for the same workflow and source SHA.

---

## 11. Exact continuation

```text
1. expose the identical frozen target workflow on main for GitHub workflow-dispatch discoverability
2. add one exact enabled Specification 018 registry authorization on main
3. create one owner-authored [ADS LIVE] issue with only the frozen launch ID and confirmation
4. verify launcher acceptance and exact target run identity
5. make no scientific interpretation from partial outputs
6. preserve the complete raw artifact before tuning or interpretation
7. evaluate only the frozen BC-G01 through BC-G06 gates
8. classify only BLOCKING_BOUNDARY_SUPPORTED, BLOCKING_BOUNDARY_NOT_SUPPORTED, or INCOMPLETE
9. retire the one-shot authorization/default-branch target exposure after preservation
```
