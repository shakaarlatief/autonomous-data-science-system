# Checkpoint 168: RECOMMENDED versus BLOCKING_REQUIRED Calibration Implementation Gate Cross-Platform Passed

**Date:** 2026-08-24  
**Status:** PROVIDER-FREE IMPLEMENTATION GATE PASSED  
**Checkpoint class:** IMPLEMENTATION / CROSS-PLATFORM VALIDATION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Records the exact Specification 020 provider-free implementation head and cross-platform validation after the frozen Checkpoint 167 contract, including deterministic plan construction, strict pointer validation, retry/attempt-cap behavior, and accepted-seam regression checks.  
**Authority:** Establishes that the Specification 020 provider-free implementation is eligible for a later separately frozen live boundary. It does not itself authorize a provider call or promote production recommendation semantics.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-blocking-calibration-diagnostic`  
**PR:** #44 draft  
**Specification:** 020

## 1. Exact validated implementation head

The exact provider-free implementation head validated before this checkpoint is:

```text
fb8327aae859f53bbb0c4d7bba70b32b6033343e
```

The branch remains based on the reconciled accepted V1 integration boundary:

```text
b9c9c3a38935983075a9ca88632177980bb20ede
```

No live provider call occurred between Checkpoint 167 and this implementation gate.

## 2. Implemented provider-free seam

Specification 020 now has a bounded experiment-only implementation:

```text
experiments/blocking_calibration/__init__.py
experiments/blocking_calibration/harness.py
experiments/blocking_calibration/runner.py
tests/unit/test_blocking_calibration_harness.py
tests/unit/test_blocking_calibration_runner.py
tests/integration/test_blocking_calibration_vertical_slice.py
.github/workflows/v1-blocking-calibration.yml
```

The implementation adds no production Proposal/Recommendation object and no authoritative project mutation path.

## 3. Mechanically enforced frozen construction

The harness validates before execution:

```text
exactly 6 contrastive pairs
exactly 2 variants per pair
one BLOCKING_REQUIRED and one RECOMMENDED variant per pair
same action identity within each pair
supplied requirement identities
supplied downstream-scope identities
shared project evidence distinct from variant-only evidence
blocking truth points only to supplied IDs
recommended truth contains no blocking pointers
36-call frozen design
45-attempt frozen ceiling
one retry maximum per planned call
```

Reasoner requests contain:

```text
candidate action
supplied requirement menu
supplied downstream-scope menu
shared project evidence
variant project evidence
condition-neutral nonce
```

and contain no evaluator truth, frozen gate thresholds, reusable methodological context, or knowledge revisions.

## 4. Deterministic plan and structured-output boundary

The complete 36-call plan is globally randomized from frozen seed:

```text
2026082401
```

and deterministically serialized and SHA-256 hashed before any injected runtime call.

The ADS-owned experiment output type is:

```text
BlockingCalibrationResult
    disposition: BLOCKING_REQUIRED | RECOMMENDED
    blocking_requirement_id: str | None
    blocked_scope_id: str | None
    rationale: str
```

The existing ADS-owned `ReasoningRuntime` abstraction accepts that structured output type without adding provider imports to application/domain layers.

## 5. Strict supplied-ID validation

Provider-neutral validation enforces:

```text
BLOCKING_REQUIRED
    -> blocking_requirement_id must be one supplied requirement
    -> blocked_scope_id must be one supplied downstream scope

RECOMMENDED
    -> blocking_requirement_id must be null
    -> blocked_scope_id must be null
```

Semantic disagreement that remains structurally valid is preserved as an observation and is never retried.

## 6. Retry and global attempt-cap behavior

The runner implements only the frozen retry classes:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

One retry maximum applies per planned call.

A provider-free defect review identified and repaired one important edge case before this checkpoint: exhausting the global 45-attempt ceiling now produces a preserved `INCOMPLETE` result rather than raising beyond the scientific result boundary.

The exact validated behavior is:

```text
persistent retryable failure
    -> stop at exactly 45 attempts
    -> preserve all 45 failed attempt records
    -> complete_scored_design = false
    -> advancement_outcome = INCOMPLETE
```

This matches the frozen Specification 020 contract.

## 7. Dedicated cross-platform evidence

Exact workflow:

```text
V1 blocking calibration diagnostic
run 32697487230
```

Ubuntu job:

```text
97342266664
provider credential check        passed; OPENAI_API_KEY absent
dedicated Specification 020      16 passed
full V1 Python suite             115 passed, 2 skipped
job                              success
```

Windows job:

```text
97342266436
provider credential check        passed; OPENAI_API_KEY absent
dedicated Specification 020      16 passed
full V1 Python suite             115 passed, 2 skipped
job                              success
```

The two full-suite skips are the existing PostgreSQL tests gated by `ADS_TEST_POSTGRES_URL`; they are unrelated to Specification 020.

## 8. Accepted-seam regression evidence on the same exact head

The exact PR head also passed:

```text
Checkpoint metadata                         run 32697487221   success
V1 reasoning context value                  run 32697487202   success
V1 disposition semantics diagnostic         run 32697487256   success
V1 autonomous live experiment launcher CI  run 32697487239   success
V1 blocking calibration diagnostic          run 32697487230   success
```

This preserves the accepted selective-context, prior disposition, checkpoint, and governed-launcher seams while adding the new provider-free diagnostic.

## 9. Provider boundary remains closed

At this checkpoint:

```text
live runtime default in Specification 020 runner    absent
Specification 020 CLI live entry point              absent
Specification 020 live workflow                     absent
OPENAI_API_KEY in ordinary CI                       absent
live authorization on main for Specification 020    absent
provider calls made by Specification 020            0
```

The runner requires an explicitly injected `ReasoningRuntime`; ordinary CI uses provider-free fakes and adapter doubles only.

## 10. Frozen scientific truth remains unchanged

Nothing in implementation changes Checkpoint 167:

```text
6 pairs
12 variants
36 planned successful outputs
45 maximum attempts
seed 2026082401
BC-G01 through BC-G06
BLOCKING_BOUNDARY_SUPPORTED / BLOCKING_BOUNDARY_NOT_SUPPORTED / INCOMPLETE
```

The effective strictness remains intentional: BC-G05 and BC-G06 require exact correctness on all 18 blocking and all 18 recommended observations respectively.

Specification 019 remains immutable `FAIL` evidence and has not been rescored or used to tune observed repetitions.

## 11. Promotion audit

### Implementation capability established

Provider-free evidence supports only that:

```text
the frozen diagnostic can be constructed deterministically;
truth can remain evaluator-only;
supplied requirement/scope identities can be validated strictly;
the frozen result can be recomputed mechanically;
retry and attempt-cap behavior preserves scientific outcomes;
the existing runtime adapter can carry the custom structured type provider-free.
```

### Not promoted

Do not promote:

```text
production RECOMMENDED semantics
production BLOCKING_REQUIRED semantics
production dependency persistence
recommendation-system value
SELECTIVE methodological-context recommendation value
automatic project mutation or execution
final provider/model policy
multi-agent recommendation architecture
```

## 12. Exact continuation

```text
1. reconcile README / KNOWLEDGE_MAP / CURRENT_STATE / OPEN_QUESTIONS to Checkpoint 168
2. validate that reconciled exact branch head provider-free
3. freeze a separate exact pre-live boundary only after that head is green
4. only after the pre-live boundary is frozen may a Specification 020 live entry path/workflow be added
5. validate any live-capable source provider-free before authorization
6. authorize at most one frozen live run through accepted Specification 018 governance
7. preserve raw evidence before interpretation or tuning
8. make no provider call before those boundaries are complete
```
