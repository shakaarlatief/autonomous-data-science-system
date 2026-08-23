# Current State

**Checkpoint:** 151  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-failure-preservation`  
**Active preservation PR:** #14 into `v1-frontend-spike`  
**Rejected experiment PR:** #13 (`v1-recommendation-action-value` -> `v1-frontend-spike`), to close without merge  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`  
**Development stage:** Prototype V0 complete; bounded V1 has an accepted real-model selective-context seam through Specification 014 and a preserved failed first recommendation/action-value experiment under Specification 015. Checkpoint 151 now isolates that negative evidence from the rejected implementation on a preservation-only branch.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the exact Checkpoint 151 preservation head, merge PR #14 only if green, close PR #13 without merge, then preregister a separate `DEFER` versus `NOT_NOW` disposition-semantics/failure-attribution diagnostic before any new live model call.

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

Current methodological path:

```text
large reusable knowledge universe
    -> retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> reasoning evidence                         [accepted bounded seam]
    -> recommendation / REQUIRED-BLOCKING/action [first live seam failed; diagnostic next]
```

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
    first accepted selective exact-revision MethodologicalContextPack seam

Specification 014 v1.0 / Checkpoint 146
    first real-model selective-context value gate passed
```

Specification 014 observed equal frozen semantic quality (`1.000000` versus `1.000000`) while SELECTIVE used an aggregate provider input-token ratio of `0.334379`, a `66.56%` reduction, with no critical-obligation regression.

No final provider/model, multi-agent architecture, production semantic retrieval stack, final Horizon/context budget, task-profile derivation, or production recommendation/REQUIRED-BLOCKING policy is selected.

---

## Specification 015 frozen live result

Research 022, Specification 015 v0.1, `recommendation_action_v1.json`, and Checkpoint 147 preregistered the first downstream recommendation/action-value experiment before implementation and live calls.

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

Frozen benchmark dispositions:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

The provider-free implementation passed cross-platform through Checkpoint 148, and Checkpoint 149 froze the reconciled live-ready boundary.

Live execution:

```text
workflow              V1 recommendation action value live
run                   32642733784
job                   frozen-live-experiment / 97202216781
frozen source head    d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
reasoner outputs      36 / 36
blinded judge outputs 36 / 36
provider attempts     72
retries               0
workflow execution    SUCCESS
```

The exact artifact was preserved before interpretation. GitHub artifact identity:

```text
artifact id      9494161645
artifact SHA-256 30229c8a7f7a00d4c170ba382dcf1817964ede04f61427c057b27d1ac7a78408
```

Frozen advancement result:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0
outcome            FAIL
```

Fourteen of fifteen named gates passed. The single failed gate was `RA-G05`, which required SELECTIVE mean exact disposition accuracy >= `0.80` in every case.

Failure localization:

```text
RA-02 MODEL_CHOICE exact disposition accuracy

GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
```

All three SELECTIVE and all three FULL_HORIZON repetitions classified:

```text
add-generic-bagging-baseline
plot-all-feature-histograms-before-shortlist
```

as `NOT_NOW`, while the frozen evaluator expected `DEFER`. GENERIC showed nearly the same pattern.

The condition-blinded semantic judge nevertheless scored all nine RA-02 outputs `1.000000`. Aggregate SELECTIVE behavior remained strong on the safety-oriented diagnostics:

```text
exact accuracy                  0.916667
semantic score                  0.991667
critical omissions              0
blocking-scope false negatives  0
unsupported basis               0
under-recommendations           0
over-recommendations            0
unnecessary recommended cost    0
clarification false negatives   0
```

This does not change the frozen `FAIL`. It localizes the next question to disposition semantics/benchmark truth versus genuine reasoner calibration.

Descriptive context economy also remained visible:

```text
mean reasoner input tokens
SELECTIVE       1609.25
FULL_HORIZON    3625.42
ratio           0.443880
reduction       55.61%
```

That observation is consistent with Specification 014 but does not rescue the failed recommendation gate.

Primary preserved evidence:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
```

---

## Checkpoint 151 preservation-only boundary

PR #14 starts from the accepted Specification 014 integration head rather than from PR #13's failed implementation branch.

The final pre-checkpoint preservation/routing head:

```text
d843c39a26867c70557b978ff5faf778bda5aaaa
```

passed:

```text
Checkpoint metadata
    run 32644994687
    PASS

V1 reasoning context value
    run 32644994598
    PASS
```

The preservation diff carries frozen research/specification/fixture/checkpoint/result evidence and canonical routing only. It deliberately excludes the failed recommendation application/runtime/harness implementation from PR #13.

`docs/MAJOR_CHANGES.md` was compacted as a navigation/history aid while retaining the major project milestones and adding the Specification 014 pass / Specification 015 fail transition. Detailed historical authority remains in the original foundations, decisions, specifications, checkpoints, experiment reports, and Git history.

---

## Promotion consequence

Specification 015 does **not** earn promotion as an accepted recommendation/action seam.

Do not promote from this result:

```text
production recommendation dispositions
automatic Proposal / Question / Investigation / Decision mutation
automatic execution
final recommendation ranking or priority policy
final provider/model selection
```

PR #13 must close without merging the failed implementation into `v1-frontend-spike`.

The failure itself is durable project evidence and is being preserved separately through PR #14.

---

## Current non-selections

Still deliberately open:

```text
whether DEFER and NOT_NOW are operationally separable enough for production
whether the RA-02 frozen DEFER truth was sufficiently defensible
reasoner calibration on deliberately unambiguous disposition cases
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
final recommendation enum/ranking model
complete Foundation 018 production schema
mapping future accepted recommendations to authoritative project events
automatic execution and human approval/escalation policy
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist recommendation architecture
production semantic retrieval/reranking/vector infrastructure
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

Do not repair Specification 015 in place and do not reinterpret its frozen result by changing expected labels or thresholds after observation.

---

## Exact continuation

```text
1. validate the exact Checkpoint 151 / PR #14 head under normal provider-free CI
2. merge PR #14 into v1-frontend-spike only if that exact head is green
3. close PR #13 without merge
4. create a separate diagnostic branch from the preserved integration head
5. preregister a bounded DEFER-vs-NOT_NOW / failure-attribution diagnostic before new live calls
6. test semantic separability independently from SELECTIVE-vs-control value
7. only after diagnosis decide whether a revised recommendation/action seam deserves another value experiment
```

Primary active checkpoint:

```text
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
```
