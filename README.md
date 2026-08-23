# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

```text
checkpoint            159
active branch         v1-recommendation-action-value-relation-backed
active PR             #16 -> v1-frontend-spike
promoted V1 head      6bda0c1efcf078476859b2c2c64fb0586964899d
current boundary      Specification 017 live execution incomplete;
                      raw evidence preserved; no advancement classification
```

Current progression:

```text
Prototype V0
    strong falsification of the original P0 design

Specification 013
    accepted selective exact-revision MethodologicalContextPack

Specification 014
    real-model selective context preserved frozen reasoning quality
    while reducing provider input tokens by 66.56%

Specification 015
    first recommendation/action-value experiment
    frozen result FAIL
    failed implementation rejected
    negative evidence preserved

Specification 016
    dependency-backed DEFER-vs-NOT_NOW diagnostic
    outcome DISPOSITION_BOUNDARY_SUPPORTED
    promoted as a bounded construct/evaluation constraint

Specification 017
    second recommendation/action-value experiment
    relation-backed action sequencing
    first live execution incomplete at the model-authored provenance field
    29/36 reasoner outputs and 29/36 judge outputs completed
    no PROMOTE / SAFE / FAIL advancement outcome assigned
    raw artifact preserved
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
experiments/relation_backed_recommendation_action_value/V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## Durable post-V0 constraint

Prototype V0 strongly falsified the current P0 design. The broader ADS vision survived, but the original orchestration machinery did not earn its complexity.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore large always-on project/methodological context, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current V1 architecture

### Project semantics

Foundation 018 distinguishes:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

### Methodological navigation

Foundation 019 establishes:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The bounded executable path currently reaches:

```text
reusable methodological knowledge
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

The next production-facing recommendation/action layer remains unpromoted after the Specification 017 incomplete execution.

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## Accepted infrastructure and interaction boundaries

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
```

The governed reusable-knowledge round-trip is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

Specification 008 promotes the **Project Cockpit** as the V1 primary immersive active-work interaction model. It remains the intended user-facing environment for chat, project navigation, analytical workspaces, evidence, recommendations, decisions, and project state. Final frontend/chart/canvas choices and production backend/API architecture remain open.

---

## Accepted selective-context evidence

Specification 013 accepted a bounded selector that reduces a deliberately wide ten-asset MethodologicalHorizon to 2-3 exact current revisions per task while retaining explicit omission evidence.

Specification 014 tested the downstream real-model consequence:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
retries                 0
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
critical regressions    none
```

Supported conclusion:

> Selective exact-revision methodological context preserved every frozen reasoning obligation while materially reducing real provider input burden on the bounded benchmark.

This does not establish a universal context budget or final provider/model.

---

## Recommendation/action evidence so far

Specification 015 was the first three-condition recommendation/action-value test. Its frozen advancement result was `FAIL`, localized to an exact `DEFER` versus `NOT_NOW` distinction. The failed implementation was not promoted.

Specification 016 isolated that semantic boundary prospectively. When DEFER was represented as an already-justified action waiting on one exact activating trigger, the live diagnostic produced:

```text
36 / 36 exact dispositions correct
18 / 18 DEFER pointers exact
18 / 18 NOT_NOW pointers null
0 retries
DISPOSITION_BOUNDARY_SUPPORTED
```

The bounded lesson is not that DEFER/NOT_NOW are final production enums. It is that deterministic sequencing should carry an explicit dependency relation.

Specification 017 then returned to the system-value comparison with prospectively relation-backed sequencing. Its first live run was incomplete rather than scientifically classified:

```text
run                         32656446705
source head                 bf041f4b4a485382d0e6e5c508ad916199601ee8
reasoner outputs            29 / 36
judge outputs               29 / 36
provider attempts           77 / 90
complete scored design      false
execution integrity         true
advancement outcome         none
```

All SELECTIVE and FULL_HORIZON reasoner outputs succeeded. GENERIC completed 5/12. The remaining GENERIC attempts repeatedly placed the requested reasoning-function label into the model-authored `methodological_basis`, while the frozen GENERIC condition supplied zero reusable knowledge revisions and therefore required that field to be empty.

Observed boundary:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

The system already owns exact context provenance. The next design must not make completion depend on an unnecessary duplicate model-authored provenance representation.

No Specification 017 `PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM`, `SAFE_BUT_NOT_DIFFERENTIATED`, or `FAIL` classification is assigned because the complete matched design was not obtained.

Primary evidence:

```text
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
experiments/relation_backed_recommendation_action_value/V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/relation_backed_recommendation_action_value/results/spec017-live-20260823-run-32656446705/
```

---

## Next architecture boundary

Two separate tracks are now justified.

First, the next recommendation/action-value experiment must separate system-owned provenance from model-owned recommendation content:

```text
SYSTEM TRACE
    exact supplied stable_key@revision_id
    context digest
    treatment identity

MODEL RESULT
    action dispositions
    dependency pointers
    scopes
    clarifications
    rationales
```

Second, the repeated manual GitHub `workflow_dispatch` step is now a tractable control-plane problem. During Specification 017 result preservation, an owner-created GitHub issue successfully triggered a default-branch workflow through the connected GitHub interface. That workflow downloaded a prior Actions artifact, verified its hashes, and pushed preserved evidence to the target branch.

This is feasibility evidence only, not yet a production launcher. A governed launcher must use an allowlisted experiment registry, verify the owner/actor and exact frozen source SHA, reject arbitrary commands from issue text, verify required CI gates, and keep every launch auditable.

---

## Exact continuation

```text
1. preserve Specification 017 evidence through a preservation-only integration PR
2. do not merge the unpromoted experimental recommendation/action implementation
3. close PR #16 without merge after preservation integration is green
4. clean temporary one-shot preservation workflows/issues
5. design and provider-free validate a governed autonomous live-experiment launcher
6. separately preregister the next recommendation/action-value experiment with system-owned provenance
7. make no new recommendation/action live provider call before the new contract and exact implementation head are frozen and green
```

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures and incomplete runs as evidence, and promote only what earns its complexity.
