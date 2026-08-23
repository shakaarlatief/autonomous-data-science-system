# Current State

**Checkpoint:** 150  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-value`  
**Active evaluation PR:** #13 into `v1-frontend-spike`; **not eligible for promotion as the accepted recommendation seam**  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted retrieval/Horizon/selective-context/reasoning seams, while the first downstream recommendation/action-value experiment has now completed with frozen outcome **FAIL**.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** preserve and validate the Specification 015 failure record, close PR #13 without promoting the recommendation seam, then start a separately preregistered diagnostic of disposition semantics and failure attribution before another live recommendation experiment or authoritative project-state coupling.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails active V1 work except for explicit manual-workflow dispatcher exposure.

---

## Durable post-V0 constraint

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore P0's large always-on context/frontier, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

Accepted methodological path through the last promoted boundary:

```text
large reusable knowledge universe
    -> retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> bounded real reasoning evidence
```

The attempted next step:

```text
reasoning evidence
    -> recommendation / REQUIRED-BLOCKING / bounded action
```

has **not** yet earned promotion.

---

## Accepted V1 boundaries already promoted

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030 + Specification 003
    pyproject.toml + uv + committed uv.lock + uv_build

D-031 + Specification 004
    deterministic governed reusable-knowledge interchange

Specification 008
    promoted Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port

Specification 012 v1.0 / Checkpoint 141
    first explained MethodologicalHorizon

Specification 013 v1.0 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack seam

Specification 014 v1.0 / Checkpoint 146
    first real-model selective-context value gate passed
```

Specification 014 observed equal frozen semantic quality (`1.000000` versus `1.000000`) while SELECTIVE used an aggregate provider input-token ratio of `0.334379`, a `66.56%` reduction, with no critical-obligation regression.

The accepted integration branch therefore remains at the Specification 014 promotion boundary.

---

## Specification 015 completed live result

Research 022, Specification 015 v0.1, the frozen fixture, and Checkpoints 147-149 governed the first downstream recommendation/action experiment.

Frozen conditions:

```text
GENERIC
    same project/task/action envelope
    no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact-revision context

FULL_HORIZON
    all ten exact current accepted Horizon revisions
```

Frozen plan:

```text
4 cases
3 conditions
3 repetitions
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
maximum 90 provider attempts
```

Live workflow:

```text
V1 recommendation action value live
run 32642733784
source head d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
```

Observed execution:

```text
36 / 36 reasoner outputs
36 / 36 judge outputs
36 / 36 scored observations
72 provider attempts
0 retries
```

The complete Actions artifact was preserved before interpretation at commit:

```text
611237d8d412b977a6c66755411dd97bcc22627e
```

Durable result route:

```text
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
```

Frozen advancement:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0
outcome            FAIL
```

Fourteen of fifteen gates passed. The sole failed gate was `RA-G05`, requiring SELECTIVE mean exact disposition accuracy >= `0.80` in every case.

`RA-02 MODEL_CHOICE` observed:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
```

The failure came from two noncritical actions expected as `DEFER` but repeatedly classified as `NOT_NOW`:

```text
add-generic-bagging-baseline
plot-all-feature-histograms-before-shortlist
```

All three SELECTIVE and all three FULL_HORIZON repetitions showed the same two-label pattern. GENERIC showed nearly the same pattern.

The blinded semantic judge nevertheless scored every RA-02 output `1.000000`, and SELECTIVE had zero critical omissions, zero blocking false negatives, zero unsupported basis references, zero under/over-recommendations, zero unnecessary recommended cost, and zero required-clarification misses.

Supported interpretation:

```text
Specification 015 FAILS its frozen contract.
The measured failure is narrow and concentrated in exact DEFER-vs-NOT_NOW calibration.
The discrepancy is not selective-context-specific.
The bounded recommendation/action seam is not promoted.
The four benchmark dispositions are not production-ready.
```

No post-hoc relabeling of the frozen result is allowed.

---

## Current diagnostic hypothesis, not accepted decision

The live result raises a concrete failure-attribution question:

```text
Does the RA-02 failure reflect:

A. insufficiently operational distinction between DEFER and NOT_NOW,
B. questionable benchmark truth for those two actions,
C. genuine model calibration weakness on an otherwise valid distinction,
or
D. some combination of these?
```

The fact that GENERIC, SELECTIVE, and FULL_HORIZON converged on essentially the same classification makes a selective-context-specific failure unlikely on this benchmark, but this remains diagnosis rather than a rewritten result.

A new diagnostic must be separately versioned and preregistered before any additional live calls.

---

## Current non-selections

Still deliberately open:

```text
production recommendation/disposition vocabulary
natural-language/project-state -> reasoning-function derivation
open-world proposal generation
final recommendation ranking/priority policy
complete Foundation 018 production schema
mapping recommendations to authoritative Proposal/Question/Decision events
automatic execution
human approval/escalation policy
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist recommendation architecture
production semantic retrieval/reranking/vector infrastructure
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

Do not couple recommendation output into authoritative project mutation while the recommendation semantics are unresolved.

---

## Exact continuation

```text
1. validate the exact Checkpoint 150/result-routing head under normal provider-free CI
2. preserve the final PR #13 failure state and close PR #13 without merging it into v1-frontend-spike
3. keep v1-frontend-spike at the accepted Specification 014 boundary
4. create a separate diagnostic branch from that accepted integration boundary
5. preregister a bounded disposition-semantics / failure-attribution diagnostic before new live calls
6. test whether DEFER and NOT_NOW can be operationalized with unambiguous sequencing counterfactuals
7. only then decide whether a revised recommendation/action seam deserves a new live value experiment
```

Primary active sources:

```text
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
```
