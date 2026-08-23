# Checkpoint 164: System-Owned Provenance Recommendation and Action Implementation Gate Cross-Platform Passed

**Date:** 2026-08-23  
**Status:** PROVIDER-FREE IMPLEMENTATION GATE PASSED / PRE-LIVE SOURCE FREEZE  
**Checkpoint class:** IMPLEMENTATION GATE / PRE-LIVE AUTHORIZATION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Records the exact provider-free Specification 019 implementation head that passed the frozen system-owned provenance, recommendation/action, live-workflow, and full-regression gates on Ubuntu and Windows.  
**Authority:** Historical implementation-gate evidence. Research 026, Specification 019 v0.1, the frozen Specification 019 overlay fixture, and immutable Specification 017 benchmark truth remain experiment authority. This checkpoint does not contain a scientific result and does not itself authorize a provider-backed launch.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Development branch:** `v1-recommendation-action-value-system-provenance`  
**PR:** #33 -> `v1-frontend-spike`  
**Starting integration head:** `ecf37585f576a3c4fd84a884dee4650b52ab1519`

## 1. Exact provider-free implementation head

The exact implementation source validated before this checkpoint was:

```text
3c57be6d4b65deb1a89d85fc63d1cc5f73321a20
```

This head contains the complete provider-free Specification 019 experiment implementation and the explicit secret-gated live workflow, but no repository launch authorization.

## 2. Exact CI evidence

Specification 019 cross-platform provider-free workflow:

```text
workflow name   V1 system-owned provenance recommendation action
run             32664302772
source head     3c57be6d4b65deb1a89d85fc63d1cc5f73321a20
Ubuntu job      97255210939  success
Windows job     97255211102  success
```

Both platforms passed:

```text
frozen Specification 019 targeted tests   13 passed
full V1 Python regression suite            116 passed, 2 skipped
OPENAI_API_KEY                              absent
static live-workflow boundary               passed
```

The two full-suite skips are the existing PostgreSQL-environment tests gated on `ADS_TEST_POSTGRES_URL`; they are unrelated to Specification 019.

Checkpoint metadata on the same source head also passed:

```text
run 32664302790
```

## 3. Provider-free implementation established

The implementation now enforces the frozen ownership split:

```text
SYSTEM OWNS
    exact condition
    exact supplied stable_key@revision_id pointers
    exact methodology payload SHA-256
    exact methodology payload byte count
    immutable per-output provenance plan

MODEL OWNS
    summary
    action dispositions
    DEFER dependency pointers
    blocked scopes
    required clarifications
    warnings
    rationales
```

`methodological_basis` is absent from the model-owned result schema.

This prospectively corrects the instrumentation boundary exposed by the incomplete Specification 017 run without changing Specification 017 scientific truth.

## 4. Frozen benchmark continuity verified

The implementation loads Specification 019 as an overlay over the immutable Specification 017 benchmark fixture and verifies its Git object identity rather than trusting platform-dependent working-tree bytes.

Frozen base fixture Git blob:

```text
eac949c47a01878dcc47dcca1116493a02ba9805
```

The effective Specification 019 benchmark inherits unchanged:

```text
RB-01 through RB-04 project states
candidate action menus and costs
expected dispositions
expected DEFER pointers
blocked-scope truth
clarification truth
judge obligations
GENERIC / SELECTIVE / FULL_HORIZON conditions
SELECTIVE exact methodological sets
FULL_HORIZON construction
relative and expansion gates
all preregistered positive-value signals
runtime treatment and provider-attempt budget
```

The previous incomplete Specification 017 outputs and partial scores are not inputs to this benchmark.

## 5. Cross-platform provenance correction

An initial Windows CI attempt revealed that recomputing a Git blob SHA from checked-out file bytes is not platform invariant because checkout line endings may differ.

The correction does not alter the frozen expected fixture identity. The implementation now resolves tracked fixture identity through Git object plumbing and falls back to byte hashing only for untracked external test fixtures.

Therefore:

```text
frozen expected Git blob SHA    unchanged
scientific fixture              unchanged
Windows checkout normalization  no longer changes identity verification
```

This is an implementation portability correction, not experiment tuning.

## 6. Live workflow boundary validated provider-free

The source contains:

```text
.github/workflows/v1-system-owned-provenance-recommendation-action-live.yml
```

The live workflow requires all three repository-derived dispatch inputs:

```text
launch_id
expected_source_sha
confirmation
```

and independently verifies:

```text
launch_id == spec019-system-provenance-001
confirmation == RUN_SPEC_019_FROZEN
github.sha == expected_source_sha
OPENAI_API_KEY is present only inside the explicit live workflow
```

Ordinary CI receives no provider credential.

The live workflow is not yet authorized in the default-branch Specification 018 registry, so no provider execution is authorized by the existence of the workflow itself.

## 7. Technical invariant status

Provider-free evidence supports the frozen implementation invariants through the pre-authorization boundary:

```text
SPRA-INV-01  base fixture Git blob locked                         PASS
SPRA-INV-02  inherited scientific truth unchanged                 PASS
SPRA-INV-03  deterministic 36-call reasoner plan                  PASS
SPRA-INV-04  deterministic independent blinded judge plan         PASS
SPRA-INV-05  GENERIC provenance revisions empty                   PASS
SPRA-INV-06  SELECTIVE exact inherited revision sets              PASS
SPRA-INV-07  FULL_HORIZON exact ten accepted-current revisions    PASS
SPRA-INV-08  provenance frozen before provider calls              PASS
SPRA-INV-09  payload SHA-256 and byte counts exact                PASS
SPRA-INV-10  model schema has no methodological_basis             PASS
SPRA-INV-11  model output cannot mutate provenance                PASS
SPRA-INV-12  matched task/project/action/trigger evidence         PASS
SPRA-INV-13  relation-backed action and pointer validation        PASS
SPRA-INV-14  semantic judge blinded from condition/provenance     PASS
SPRA-INV-15  retry accounting and 90-attempt ceiling              PASS
SPRA-INV-16  complete fake 36 reasoner + 36 judge design          PASS
SPRA-INV-17  ordinary CI contains no provider credential          PASS
SPRA-INV-18  provider SDK import boundary preserved               PASS
SPRA-INV-19  authoritative project state unchanged                PASS
SPRA-INV-20  exact governed live authorization                    NOT YET AUTHORIZED
```

## 8. What is not concluded

This checkpoint provides no evidence yet that:

```text
SELECTIVE adds recommendation/action value over GENERIC
SELECTIVE is safer than FULL_HORIZON
system-owned provenance improves semantic recommendation quality
production recommendation/disposition enums should be adopted
production DEFER or NOT_NOW semantics are final
model-authored knowledge citations are unnecessary in all settings
```

The provider-backed comparison remains unobserved.

## 9. Exact next boundary

The next legitimate sequence is:

```text
1. validate the commit that contains this checkpoint with the same provider-free gates
2. pin that exact green commit to a dedicated immutable live-source branch
3. record the exact live-source ref, SHA, CI run IDs, workflow, launch ID, and confirmation in a separate authorization checkpoint
4. add exactly one enabled Specification 018 registry authorization on main
5. create one owner [ADS LIVE] issue through the connected GitHub interface
6. allow the accepted launcher to dispatch the exact live-source workflow
7. preserve the complete result artifact before interpretation
8. apply only the frozen Specification 019 advancement rules
```

No provider-backed Specification 019 call is authorized at this checkpoint alone.
