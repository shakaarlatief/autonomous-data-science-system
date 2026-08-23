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
checkpoint            161
active branch         v1-autonomous-live-experiment-launcher
active PR             #23 -> v1-frontend-spike
promoted V1 head      4385b83b43582ff6466b519b4e96356d220c44bc
current boundary      Specification 018 governed autonomous live-experiment
                      launcher passed its end-to-end provider-free gate
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
    first recommendation/action-value experiment FAIL; implementation rejected

Specification 016
    dependency-backed DEFER-vs-NOT_NOW diagnostic supported

Specification 017
    relation-backed recommendation/action live execution incomplete
    historical evidence preserved; implementation rejected

Specification 018
    governed autonomous live-experiment launcher supported
    exact cross-platform provider-free CI passed
    owner issue -> launcher -> workflow_dispatch -> probe passed
    no manual Actions UI click and no provider call required
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/161_governed_autonomous_live_experiment_launcher_end_to_end_gate_passed.md
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
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

The control-plane problem is now boundedly solved: future explicitly authorized frozen experiments can be launched through the repository-governed Specification 018 mechanism rather than by asking the user to press the GitHub Actions button.

The next scientific boundary returns to recommendation/action value. The next experiment must separate:

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

Before any provider-backed launch, the next experiment must be preregistered, its exact implementation head must pass provider-free gates, and one exact launch authorization must be added to the repository registry.

---

## Exact continuation

```text
1. finish Checkpoint 161 canonical reconciliation
2. clean the one-shot probe authorization and temporary control helpers
3. validate the exact final PR #23 head
4. merge PR #23 into v1-frontend-spike
5. record the exact promoted merge boundary
6. preregister the next recommendation/action-value experiment with system-owned provenance
7. validate its exact provider-free implementation head
8. authorize and launch it through Specification 018
9. make no recommendation/action provider call before the new contract and implementation gate are frozen and green
```

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures and incomplete runs as evidence, and promote only what earns its complexity.
