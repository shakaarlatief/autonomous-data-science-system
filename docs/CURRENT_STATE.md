# Current State

**Checkpoint:** 149  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-value`  
**Active promotion PR:** #13 into `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`  
**Development stage:** Prototype V0 complete; bounded V1 now has a frozen recommendation/action-value contract, complete cross-platform provider-free implementation, and a validated pre-live boundary ready for the first unchanged live recommendation experiment.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** keep the frozen Specification 015 treatment unchanged, validate this final routing-only head, then manually execute the secret-gated 72-call live plan once and preserve the complete result before any tuning or promotion decision.

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

## Specification 015 contract and provider-free implementation

Research 022, Specification 015 v0.1, `recommendation_action_v1.json`, and Checkpoint 147 freeze the first downstream recommendation/action experiment.

Frozen conditions:

```text
GENERIC
    same task/project/action envelope
    no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact-revision context

FULL_HORIZON
    all ten exact current accepted Horizon revisions
```

Benchmark-only dispositions:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

`BLOCKING_REQUIRED` is tied to a named validity/dependency scope and is not merely a stronger recommendation.

Frozen plan:

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
unnecessary recommended cost
blocking-scope false negatives / positives
required-clarification false negatives
basis-provenance failures
```

The blinded semantic judge is secondary for rationale/dependency correctness.

Advancement remains exactly:

```text
PROMOTE_BOUNDED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

A promotion claim requires all safety/non-regression/expansion gates plus at least one preregistered positive value signal.

Checkpoint 148 records the complete provider-free implementation gate at implementation head:

```text
6ccfd15d194a4205b2f554268ccad05fbd38edda
```

Cross-platform evidence:

```text
V1 recommendation action value
run 32640518712

Ubuntu   12 dedicated passed; full suite 63 passed, 2 skipped
Windows  12 dedicated passed; full suite 63 passed, 2 skipped
```

The two skips are the existing PostgreSQL-dependent tests without `ADS_TEST_POSTGRES_URL`.

The complete fake-runtime shape executes 36 reasoner + 36 blinded judge observations and deliberately produces a perfect three-way ceiling. The evaluator correctly returns `SAFE_BUT_NOT_DIFFERENTIATED`, proving that the advancement machinery does not manufacture a value claim when all conditions are equal.

The provider-free runner also verifies:

```text
GENERIC       no reusable methodological assets
SELECTIVE     exact accepted 2-3 revision sets
FULL_HORIZON  exact ten-revision Horizon
reasoner      evaluator truth absent from input
judge         treatment/evaluator truth blinded
authority     reusable-knowledge state unchanged
project state prj_project/prj_entity/prj_finding/prj_knowledge_ref unchanged
```

---

## Checkpoint 149 live-ready boundary

Checkpoint 149 freezes the pre-live boundary after implementation, routing, and live-workflow reconciliation.

The checkpoint commit itself passed:

```text
Checkpoint metadata
    run 32641146841   PASS

V1 recommendation action value
    run 32641146842   PASS
    Ubuntu            PASS
    Windows           PASS

V1 reasoning context value
    run 32641146840   PASS
```

The dedicated recommendation/action workflow again verified that ordinary CI had no `OPENAI_API_KEY` and passed the complete provider-free suite on both operating systems.

The explicit live workflow is exposed on the default branch only as the GitHub manual-dispatch surface. It still requires the experiment branch and refuses to run from another ref:

```text
workflow      V1 recommendation action value live
branch        v1-recommendation-action-value
secret        OPENAI_API_KEY
confirmation  RUN_SPEC_015_FROZEN
```

No live Specification 015 reasoner or judge call has occurred.

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
1. validate this final routing-only branch head with Checkpoint metadata and the Ubuntu/Windows recommendation/action workflow
2. make no change to Specification 015, fixture, model, prompts, action menus, rubric, gates, repetitions, randomization, retry policy, context construction, or evaluator
3. manually execute V1 recommendation action value live from v1-recommendation-action-value with RUN_SPEC_015_FROZEN
4. preserve the complete uploaded raw/result bundle before any tuning
5. classify the result exactly as PROMOTE_BOUNDED_RECOMMENDATION_SEAM, SAFE_BUT_NOT_DIFFERENTIATED, or FAIL
6. create the live-result checkpoint before merge, repair, or subsequent experiment design
```

Primary active sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
.github/workflows/v1-recommendation-action-value-live.yml
```