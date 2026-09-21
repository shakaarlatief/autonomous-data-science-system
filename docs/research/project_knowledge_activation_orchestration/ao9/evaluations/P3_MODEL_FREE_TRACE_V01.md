# AO-9 P3 Model-Free Mechanism Trace Evaluation

**Date:** 2026-09-21
**Protocol:** Research 228
**Scenario packet:** Research 229 / 76f5d6e7...
**Arm contracts:** Research 230 / 80b05a8a...
**Result:** traces/P3_MODEL_FREE_TRACE_V01.json
**Status:** MODEL-FREE TRACE COMPLETE / FRESH REPLAY STILL REQUIRED

P3 does not infer probabilistic model behavior from evaluator knowledge. P4 means the frozen architecture has relevant capability, but a fresh behavioral replay is required to determine whether the capability actually activates and at what cost.

| Scenario | A | B | C | D |
| --- | --- | --- | --- | --- |
| R1 | HIST/FAIL | P4 | P4 | P4 |
| R2 | HIST/PARTIAL | P4 | P4 | P4 |
| R3 | HIST/FAIL | P4 | P4 | P4 |
| R4 | HIST/FAIL | P4 | P4 | P4 |
| R5 | HIST/PARTIAL | P4 | P4 | P4 |
| R6 | HIST/PASS | P4 | P4+ROUTE | P4+ROUTE |
| R7 | HIST/FAIL | P4 | GAP/FAIL | GAP/FAIL |
| R8 | HIST/FAIL | P4 | P4 | P4 |
| R9 | N/A | N/A | GAP/FAIL | CLOSE/PASS |
| R10 | N/A | P4 | P4 | CLOSE/PASS |
| R11 | HIST/PARTIAL | P4 | PART/PARTIAL | PART/PARTIAL |
| N1 | N/A | P4 | P4 | P4 |
| N2 | N/A | N/A | N/A | N/A |
| N3 | N/A | P4+SAFE | P4+SAFE | P4+SAFE |
| N4 | N/A | P4 | P4 | P4 |

## Hard model-free findings

1. R9 exposes the exact AO8-E01 seam. Arm C has no independent post-output re-entry path once the induced S3 fast path is fixed. Arm D does. This is a deterministic architecture delta, not a model-quality claim.
2. R10 gives D a deterministic structural-verification capability. C may still reject the invalid receipt through ordinary authority reasoning, but that is behavioral and therefore remains P4-required.
3. R7 exposes a real realization-traceability guarantee gap in both C and D. Neither frozen arm contains a deterministic cross-artifact join from accepted MUST to gate/evidence/activation. This is mechanistic support for the R52 requirement candidate, not yet a final requirements decision.
4. R11 is deterministically partial for C/D. AO-6 correctly preserves selected ROTATE versus completed rotation, but the frozen candidate still lacks an executable realization gate for the attach/switch obligation.
5. Historical A is mixed rather than uniformly weak. The current architecture has demonstrated successful collaboration discovery, exact-source fidelity and abnormal-interruption recovery under some prompts, while still showing restart-output fidelity, trigger activation and continuation-supporting-evidence misses.

## What P3 cannot decide

P3 cannot honestly decide most B/C comparisons because task interpretation and semantic nomination remain model-assisted. It therefore does not convert capability presence into PASS.

The B-vs-C stopping rule remains open on R2/R3/R6/R7/R8.

The AO8-E01 decision remains open because Research 228 requires D to pass N1, N3 and N4 behaviorally in addition to the deterministic R9 closure.

## P4 minimum replay set

P3 narrows the fresh-collaborator work. The minimum decision-relevant replay set is:

```text
B vs C:
    R2 collaboration activation
    R3 architecture trigger activation
    R6 abnormal interruption routing
    R7 obligation-realization audit
    R8 known-risk activation

D negative controls:
    N1 ordinary low-consequence question
    N3 question is not mutation authorization
    N4 adjacent runtime topic
```

High-value additional replays are R1 (final ordered action fidelity), R4 (Chat-28 supporting evidence), R5 (exact-source depth/cost), and R10-C (whether ordinary candidate authority reasoning rejects the malformed receipt without the D verifier).

Fresh replay should not read this evaluation, evaluator keys, or prior scored outputs.

```text
AO9_P3=COMPLETE
MODEL_FREE_TRACE=COMPLETE
AO8_E01=NOT_FINAL
B_VS_C_STOPPING_RULE=NOT_FINAL
R52_MECHANISTIC_SUPPORT=YES
P4_MINIMUM_DECISION_REPLAY_COUNT=13
NEXT=AO9_P4_FRESH_COLLABORATOR_REPLAY
```
