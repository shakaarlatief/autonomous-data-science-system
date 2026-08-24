# Checkpoint 178: Specification 021 Live Execution Incomplete Due to Attempt-Metadata Serialization

**Date:** 2026-08-24  
**Status:** LIVE EXECUTION INCOMPLETE; RAW EVIDENCE PRESERVED; NO SCIENTIFIC ADVANCEMENT CLASSIFICATION  
**Checkpoint class:** LIVE RESULT / FAILURE ATTRIBUTION / CONTINUITY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Records the first governed provider-backed Specification 021 execution, preserves its raw artifact before interpretation, classifies the run as incomplete under the frozen contract, and isolates the observed failure to experiment/runtime attempt-metadata serialization rather than recommendation quality.  
**Authority:** Specification 021 remains scientifically unchanged. This checkpoint does not rescore the incomplete run and does not authorize a replacement provider run.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-dependency-backed-recommendation-value`  
**PR:** #55  
**Specification:** 021

## 1. Frozen source and governed launch

Exact frozen provider-capable source:

```text
b589bad975880b2d3cccc3596fc82539b1b96577
```

Frozen source ref:

```text
v1-spec021-dependency-backed-recommendation-value-live-source
```

Governed launch transport and execution:

```text
launch issue            56
launch id               spec021-dependency-backed-recommendation-value-001
confirmation            RUN_SPEC_021_FROZEN
launcher run            32727227189
live run                32727241852
live job                97431195730
source SHA              b589bad975880b2d3cccc3596fc82539b1b96577
workflow event          workflow_dispatch
```

The Specification 018 launcher accepted the exact owner request and dispatched only the repository-authorized workflow/ref/source. The target independently passed its frozen source, confirmation, provider-credential, and provider-free preflight checks before live execution.

## 2. Raw artifact preserved before interpretation

The live workflow completed and uploaded:

```text
artifact id             9520249437
artifact name           v1-dependency-backed-recommendation-action-b589bad975880b2d3cccc3596fc82539b1b96577-1
artifact SHA-256        b936fab44a17dc22fb9fe31dacdb6f09104a765fcb2223df8ef517338403fe77
```

The complete artifact was force-added unchanged to the experiment branch before `result.json` or attempt content was scientifically interpreted:

```text
preservation commit     247314916fa028e2d27ea282ee030a26a30a84cc
preserved path          experiments/dependency_backed_recommendation_action_value/results/spec021-live-20260824-run-32727241852/
```

Preserved files:

```text
RESULT.md
dependency_backed_recommendation_action.sqlite3
judge_attempts.jsonl
judge_plan.json
reasoner_attempts.jsonl
reasoning_plan.json
result.json
system_provenance_plan.json
```

This ordering is part of the evidence boundary: raw provider evidence existed durably in Git before scientific classification began.

## 3. Frozen result classification

The preserved result reports:

```text
planned reasoner outputs       36
successful reasoner outputs    0
planned judge outputs          36
successful judge outputs       0
scored observations            0
reasoner failed attempts       72
judge failed attempts          0
provider attempts used         72 / 90
complete scored design         false
execution integrity            false
gate evaluation                null
advancement outcome            null
authoritative state unchanged  true
```

All frozen technical invariants are true except:

```text
DBRA-INV-20_complete_design = false
```

Therefore the only legitimate Specification 021 interpretation is:

```text
INCOMPLETE / INTEGRITY FAILED
NO SCIENTIFIC ADVANCEMENT CLASSIFICATION
```

This run is not `FAIL`, `SAFE_BUT_NOT_DIFFERENTIATED`, or `PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM`. There are zero scored recommendation observations from which any of those complete-design outcomes could be inferred.

The substantive scientific question remains unresolved.

## 4. Uniform failure signature

All 72 reasoner attempts recorded exactly the same error:

```text
cannot pickle 'mappingproxy' object
```

The signature is uniform across:

```text
GENERIC        24 attempts
SELECTIVE      24 attempts
FULL_HORIZON   24 attempts

DBRA-01        18 attempts
DBRA-02        18 attempts
DBRA-03        18 attempts
DBRA-04        18 attempts

first attempts 36
retries        36
```

No semantic judge call was reached because no reasoner output survived attempt recording as a successful observation.

This uniformity provides no condition-specific recommendation signal.

## 5. Failure attribution

The failure is strongly isolated to live attempt-metadata serialization.

`ReasoningUsage` makes non-null `raw_provider_usage` immutable by storing it as a `MappingProxyType`. The accepted OpenAI Agents runtime populates non-null raw provider usage for live calls. Specification 021's attempt recorder then applies `dataclasses.asdict(outcome.usage)`. Python's dataclass deep-copy path cannot pickle a `mappingproxy`, reproducing the exact observed exception:

```text
TypeError: cannot pickle 'mappingproxy' object
```

The reasoner retry block catches that exception while constructing the attempt record, classifies it as `PROVIDER_FAILURE`, retries once, and ultimately discards the otherwise returned outcome.

The blinded judge recorder contains the same latent `asdict(outcome.usage)` pattern and should be repaired at the same instrumentation boundary before another live run.

This attribution is based on the exact preserved error signature plus deterministic code-path reproduction. The current raw artifact does not contain a Python stack trace, so the checkpoint does not claim direct stack-trace proof.

## 6. Why provider-free CI did not catch it

The provider-free doubles exercised the complete 36-reasoner plus 36-judge design but did not reproduce the live runtime's non-null mappingproxy-backed raw usage shape. Their usage metadata therefore remained serializable by the current recorder.

The missing test is narrow and identifiable:

```text
provider-free live-shape ReasoningUsage
    with non-null raw_provider_usage
    -> reasoner attempt recording serializes successfully
    -> judge attempt recording serializes successfully
```

No benchmark or methodological treatment change is needed to test this.

## 7. Frozen science remains immutable

Do not change:

```text
four cases
candidate actions
expected dispositions
requirement/scope/resolver relations
defer-trigger relations
rubrics
GENERIC / SELECTIVE / FULL_HORIZON treatments
knowledge universe or selective key sets
system-owned provenance contract
model configurations
randomization seed
planned call counts
attempt ceiling and retry policy
hard gates
value signals
complete-design outcome taxonomy
```

Specifications 015-020 remain immutable historical evidence.

## 8. Legitimate repair boundary

A replacement run may be considered only after a provider-free instrumentation repair that:

```text
1. serializes ReasoningUsage explicitly without dataclasses.asdict deep-copying mappingproxy values;
2. covers both reasoner and judge attempt metadata;
3. adds a regression test with non-null live-shaped raw_provider_usage;
4. preserves all frozen Specification 021 scientific inputs and evaluator truth;
5. passes dedicated Ubuntu and Windows Specification 021 CI plus inherited accepted-seam checks;
6. is frozen at a new exact live-source SHA;
7. uses a new one-shot Specification 018 authorization and launch ID.
```

The original live source and run remain immutable evidence and must not be overwritten or reclassified.

## 9. Immediate governance cleanup

Before implementing the repair, retire the consumed one-shot control-plane exposure from `main`:

```text
remove Specification 021 authorization from .github/ads_live_experiments.json
remove temporary default-branch Specification 021 target workflow exposure
remove temporary observer/preservation helper workflows
close launch issue #56 after audit history is retained
```

The historical frozen live-source ref may remain as provenance for run `32727241852`.

## 10. Exact continuation

```text
1. reconcile current routing to Checkpoint 178 / Specification 021 INCOMPLETE
2. retire the consumed main authorization and temporary workflows
3. implement only the narrow usage-serialization repair
4. add provider-free live-shape regression coverage for reasoner and judge metadata
5. validate the repaired branch cross-platform with no provider credential
6. freeze a new exact pre-live/live-source boundary only after all required checks pass
7. use a new governed launch authorization if a replacement run is justified
8. preserve any replacement raw artifact before interpretation
9. do not alter or rescore the frozen Specification 021 scientific contract
```