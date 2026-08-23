# Current State

**Checkpoint:** 147  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-value`  
**Active promotion PR:** #13 into `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`  
**Development stage:** Prototype V0 complete; bounded V1 now connects governed methodological knowledge, an explained Horizon, selective exact-revision context, and an ADS-owned reasoning runtime to the first frozen recommendation/action-value experiment.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** implement Specification 015 provider-free only, preserving the frozen GENERIC / SELECTIVE / FULL_HORIZON recommendation-action design, exact deterministic evaluator, bounded action menus, and no-authoritative-mutation boundary before any new live model call.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails active V1 work.

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
    -> reasoning evidence
    -> recommendation / REQUIRED-BLOCKING / action evidence [active]
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

No final provider/model, multi-agent architecture, production semantic retrieval stack, final Horizon/context budget, task-profile derivation, or recommendation/REQUIRED-BLOCKING production policy is selected.

---

## Specification 015 recommendation/action contract is frozen

Research 022, Specification 015 v0.1, `recommendation_action_v1.json`, and Checkpoint 147 preregister the first downstream recommendation/action experiment before implementation or live calls.

Frozen question:

> Given the same project microstate, explicit task profile, candidate action menu, model/runtime configuration, and evaluation rubric, does the accepted ADS methodological path help a strong reasoner choose and calibrate the right methodological actions, preserve blocking dependencies, and avoid unnecessary work relative to strong simpler controls?

Frozen conditions:

```text
GENERIC
    same task/project/action envelope
    no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact-revision context

FULL_HORIZON
    all ten exact current accepted Horizon revisions
    same compact reasoning projection
```

Benchmark-only dispositions:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

The distinction is explicit: `BLOCKING_REQUIRED` is tied to a named validity/dependency scope and is not merely a stronger recommendation.

Frozen cases:

```text
RA-01 VALIDITY_GATE
RA-02 MODEL_CHOICE
RA-03 EVIDENCE_PLAN
RA-04 MISSINGNESS_IMBALANCE
```

Frozen design:

```text
4 cases
3 conditions
3 repetitions
36 planned reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
maximum 90 provider attempts
```

Primary evaluation is deterministic:

```text
exact disposition accuracy
critical action omissions
under-recommendations
over-recommendations
unnecessary recommended cost units
blocking-scope false negatives / positives
required-clarification false negatives
basis-provenance failures
```

The blinded semantic judge is secondary for rationale/dependency correctness.

Advancement is explicitly three-way:

```text
PROMOTE_BOUNDED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

A promotion claim requires all safety/non-regression/expansion gates plus at least one preregistered positive value signal. A three-way ceiling result must not be relabeled as added system value after the fact.

---

## Current non-selections

Still deliberately open:

```text
natural-language/project-state -> reasoning-function derivation
open-world proposal generation
final recommendation enum/ranking model
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

Do not return to retrieval/relevance tuning merely because more tuning is possible. Add complexity only when downstream evidence exposes a concrete deficiency.

---

## Exact continuation

```text
1. implement ADS-owned RecommendationActionResult / disposition types provider-free
2. implement the exact deterministic evaluator
3. implement GENERIC / SELECTIVE / FULL_HORIZON condition construction
4. implement deterministic reasoner/judge plans and blinded semantic-judge contracts
5. add fake-runtime unit/integration coverage for the complete 36 + 36 observation shape
6. add ordinary Ubuntu/Windows provider-free workflow coverage with no live API key
7. validate the exact implementation head
8. only then establish the explicit secret-gated live boundary
9. preserve the live result before any treatment or threshold change
```

No live Specification 015 reasoner or judge call has occurred.

Primary active sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
```
