# Checkpoint 179: Specification 021 Usage Serialization Repair Passed Cross-Platform

**Date:** 2026-08-24  
**Status:** INSTRUMENTATION REPAIR GATE PASSED; SCIENTIFIC OUTCOME REMAINS INCOMPLETE  
**Checkpoint class:** FAILURE REPRODUCTION / NARROW REPAIR / PROVIDER-FREE VALIDATION  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Records the red-before-green reproduction and narrow repair of the `ReasoningUsage.raw_provider_usage` attempt-metadata serialization defect that made the first governed Specification 021 execution incomplete.  
**Authority:** Specification 021's scientific contract, benchmark, treatments, evaluator truth, model settings, call plan, retry policy, gates, and complete-design outcomes remain unchanged. Run `32727241852` remains immutable `INCOMPLETE` evidence. This checkpoint authorizes no provider call.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-dependency-backed-recommendation-value`  
**PR:** #55  
**Specification:** 021

## 1. Preserved failure boundary

Checkpoint 178 froze the first governed Specification 021 execution as incomplete:

```text
frozen live source       b589bad975880b2d3cccc3596fc82539b1b96577
launch issue             56
launcher run             32727227189
live run                 32727241852
live job                 97431195730
artifact                 9520249437
artifact SHA-256         b936fab44a17dc22fb9fe31dacdb6f09104a765fcb2223df8ef517338403fe77
preservation commit      247314916fa028e2d27ea282ee030a26a30a84cc
successful reasoners     0 / 36
successful judges        0 / 36
scored observations      0
reasoner failed attempts 72
provider attempts        72 / 90
advancement outcome      null
classification           INCOMPLETE
```

Every reasoner attempt recorded:

```text
cannot pickle 'mappingproxy' object
```

The frozen failure attribution was that live `ReasoningUsage.raw_provider_usage` is mappingproxy-backed while the Specification 021 success-attempt recorder used `dataclasses.asdict(outcome.usage)` for both reasoner and judge metadata.

## 2. Prospective regression reproduction before repair

The missing provider-free shape was added first, before the production repair.

Test-only head:

```text
7cf41dfd5785d754fa62096ec9bd410b75b5f044
```

The complete provider-free fake runtime and fake judge were changed only so their `ReasoningUsage` objects contained non-null live-shaped `raw_provider_usage`. The integration test also requires the serialized reasoner and judge JSONL attempt records to retain that metadata.

No production code was changed at this head.

Exact red evidence:

```text
Specification 021 CI run     32731748120  failure
Ubuntu job                   97445281173  failure
Windows job                  97445280966  failure
```

On Ubuntu the dedicated frozen suite reported:

```text
1 failed, 9 passed
```

and the full Python regression suite reported:

```text
1 failed, 126 passed, 2 skipped
```

The failing integration assertion observed `complete_scored_design == false`, reproducing the live failure mechanism provider-free when non-null raw provider usage is present. Windows failed the same dedicated and full-suite steps.

This red-before-green ordering demonstrates that the new regression actually exercises the missing live-shaped serialization boundary rather than merely asserting behavior after the repair.

## 3. Narrow production repair

Validated repair head:

```text
44983ab9af4b0b3739043466a19541ae2ac9e7ed
```

Only the Specification 021 attempt-record serialization path changed.

The repair:

```text
ReasoningUsage
    -> explicit _usage_payload(...)
    -> recursive JSON-native copy of raw_provider_usage
    -> reasoner attempt JSONL
    -> judge attempt JSONL
```

Concretely:

1. `ReasoningUsage` is imported into the provider-neutral Specification 021 runner.
2. `_json_safe_metadata(...)` recursively copies mappings into ordinary dictionaries and lists/tuples into ordinary lists while leaving scalar values unchanged.
3. `_usage_payload(...)` explicitly records the normalized usage fields:
   - `input_tokens`
   - `output_tokens`
   - `total_tokens`
   - `cached_input_tokens`
   - `reasoning_tokens`
   - `service_tier`
   - `raw_provider_usage`
4. The reasoner success-attempt record uses `_usage_payload(outcome.usage)` instead of `asdict(outcome.usage)`.
5. The judge success-attempt record uses the identical serializer.

`ReasoningUsage` itself remains immutable in the accepted application boundary. The repair serializes a JSON-safe snapshot instead of weakening the mappingproxy-backed model.

`ReasoningTrace` continues to use its existing dataclass serialization because it does not contain the problematic mappingproxy field.

## 4. Frozen science did not change

The repair does not change:

```text
four cases
candidate actions
expected dispositions
requirement/scope/resolver relations
defer-trigger relations
rubrics
GENERIC / SELECTIVE / FULL_HORIZON treatments
knowledge universe
SELECTIVE exact revision sets
system-owned provenance contract
reasoner model configuration
judge model configuration
randomization seed
36 reasoner + 36 judge plan
90-attempt ceiling
one-retry policy
hard gates
value signals
complete-design outcome taxonomy
```

The preserved first live run is not rerun, rescored, or reclassified.

## 5. Exact green cross-platform evidence

Exact repair-head Specification 021 run:

```text
Specification 021 CI run     32732513065  success
Ubuntu job                   97447719364  success
Windows job                  97447719596  success
```

On both operating systems:

```text
live provider credential absent                       pass
Specification 021 repository authorization absent     pass
application/domain provider-neutral boundary           pass
frozen provider-free Specification 021 gates           pass
existing V1 Python regression suite                    pass
```

The updated integration test now completes the full 36-reasoner plus 36-judge provider-free design with non-null raw provider usage, preserves 36 successful reasoner attempt rows and 36 successful judge attempt rows, and verifies the raw provider usage survives JSONL serialization on both paths.

## 6. Inherited accepted-seam validation

All required inherited workflows are green on the exact repair head:

```text
Current routing consistency                32732513022  success
Checkpoint metadata                        32732513054  success
V1 dependency-backed recommendation value  32732513065  success
V1 autonomous live experiment launcher CI 32732513183  success
V1 reasoning context value                 32732513095  success
V1 blocking calibration diagnostic         32732513090  success
V1 disposition semantics diagnostic        32732512948  success
```

No provider credential was supplied to the repair validation.

## 7. Control-plane state after cleanup

The first one-shot Specification 021 exposure has been retired:

```text
.github/ads_live_experiments.json    no Specification 021 authorization
main Spec021 target workflow         absent
temporary live observer              absent
temporary preservation helper        absent
launch issue #56                     closed, audit history retained
```

Temporary maintenance helpers used during continuity recovery were also removed. Issues #57, #58, and #59 are closed and do not represent scientific or live-launch authorizations.

The historical live-source ref for run `32727241852` remains provenance only.

## 8. Interpretation

The narrow instrumentation hypothesis is supported:

> Explicit JSON-safe serialization of `ReasoningUsage` removes the mappingproxy failure on the same provider-free execution shape that reproduced the defect, for both reasoner and judge attempt metadata, without changing frozen Specification 021 science.

This is an engineering/instrumentation conclusion only.

It does **not** establish:

```text
SELECTIVE recommendation value
GENERIC / SELECTIVE / FULL_HORIZON relative quality
PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
scientific FAIL
production recommendation policy
```

Specification 021's scientific status therefore remains:

```text
INCOMPLETE
```

until a separately frozen replacement live execution completes the preregistered design with integrity.

## 9. Legitimate next boundary

Before any replacement provider run:

```text
1. reconcile README, CURRENT_STATE, KNOWLEDGE_MAP, OPEN_QUESTIONS, and current_routing to Checkpoint 179;
2. validate that exact reconciled head with Specification 021 and inherited accepted-seam CI;
3. freeze a new exact replacement live-source boundary and dedicated source ref;
4. keep the original source/ref/run immutable as historical incomplete evidence;
5. create a new one-shot Specification 018 authorization using fresh exact green run IDs;
6. use a new launch ID, never reuse `spec021-dependency-backed-recommendation-value-001`;
7. preserve any replacement raw artifact before scientific interpretation.
```

No provider call is authorized by this checkpoint.
