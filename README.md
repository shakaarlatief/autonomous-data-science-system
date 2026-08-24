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
checkpoint            166
active branch         v1-frontend-spike
active PR             none
promoted V1 head      e88c41b31788a53c7da115a24b0f9baeea48516b
current boundary      Specification 019 complete live result = FAIL
                      negative evidence integrated without implementation promotion
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
    governed autonomous live-experiment launcher supported and promoted

Specification 019
    system-owned-provenance recommendation/action rerun completed
    provenance instrumentation worked
    frozen advancement outcome FAIL
    implementation rejected; failure evidence preserved on integration
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/
    V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
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

The production-facing recommendation/action layer remains unpromoted after Specifications 015, 017, and 019 failed or incomplete recommendation-value attempts.

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

Specification 018 promotes the first bounded governed live-experiment control plane:

```text
owner-created request
    -> repository authorization registry
    -> exact owner/source/CI/duplicate checks
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

The launcher itself receives no provider credential and does not authorize arbitrary commands, workflows, refs, prompts, models, or secrets from issue text.

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

## Recommendation/action evidence

### Specification 015

The first three-condition recommendation/action-value experiment classified `FAIL`. The failed implementation was not promoted. The main discrepancy was a preregistered `DEFER` versus `NOT_NOW` boundary.

### Specification 016

A prospective construct-validity diagnostic then showed that DEFER-like sequencing can be made reliably distinguishable when it is represented as an already-justified action waiting on one exact activating dependency:

```text
36 / 36 exact dispositions correct
18 / 18 DEFER pointers exact
18 / 18 NOT_NOW pointers null
0 retries
DISPOSITION_BOUNDARY_SUPPORTED
```

The bounded lesson is structural, not a final production-enum decision: deterministic sequencing should carry an explicit activating relation when that distinction matters.

### Specification 017

The relation-backed recommendation/action comparison then ended incomplete:

```text
run                         32656446705
reasoner outputs            29 / 36
judge outputs               29 / 36
provider attempts           77 / 90
complete scored design      false
execution integrity         true
advancement outcome         none
```

The failure mode exposed an instrumentation distinction:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

Model-authored `methodological_basis` was an unnecessary duplicate of context provenance that the system already knew exactly.

### Specification 019

Specification 019 prospectively repaired that boundary by keeping exact supplied-context provenance system-owned while leaving recommendation content model-owned.

The governed live run completed the full frozen design:

```text
source                    6b5e6237b738250458550f95c9f3a6b0d51e86ec
run                       32664534864
reasoner outputs          36 / 36
judge outputs             36 / 36
provider attempts         72 / 90
retries                   0
execution integrity       true
```

Frozen aggregate result:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           0.944444       0.916667        0.944444
semantic score           0.950000       0.950000        0.950000
blocking false positives 4              6               4
```

Frozen outcome:

```text
absolute gates           FAIL
relative gates           FAIL
expansion gates          FAIL
positive value signals   0
advancement outcome      FAIL
```

The central recommendation-calibration problem was RB-02. SELECTIVE repeatedly promoted two useful model-comparison actions from expected `RECOMMENDED` to `BLOCKING_REQUIRED`, while correctly preserving the DEFER dependency for later tuning. GENERIC and FULL_HORIZON showed the same tendency less consistently, so SELECTIVE crossed the frozen per-case non-inferiority margin and accumulated more blocking-scope false positives than FULL_HORIZON.

RB-04 also missed the preregistered per-case semantic floor in all three conditions because the responses omitted one explicit training-only preprocessing/leakage-prevention obligation. That common ceiling does not implicate SELECTIVE specifically, but the frozen contract does not permit a post-hoc exemption.

The Specification 019 recommendation/action implementation is therefore not promoted. Its frozen authority and failure evidence were merged through preservation-only PR #43 at `e88c41b31788a53c7da115a24b0f9baeea48516b`; failed implementation PR #33 is closed without merge.

Primary evidence:

```text
docs/research/026_system_owned_provenance_recommendation_action_value_design.md
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/
    V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## System-owned provenance boundary

Specification 019 did provide positive bounded evidence for one architecture distinction:

```text
SYSTEM-OWNED PROVENANCE
    exact supplied stable_key@revision_id
    methodology payload digest and byte count
    treatment identity

MODEL-OWNED CONTENT
    dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales
```

The complete 36-output design ran without provenance-induced schema failures or retries. Exact supplied-context provenance should remain a deterministic system trace rather than a mandatory duplicate model-authored result field.

This is an instrumentation lesson, not a recommendation-value promotion signal.

---

## Next architecture boundary

The next scientific target is narrower than another generic recommendation rerun:

```text
what makes justified work merely RECOMMENDED
    versus genuinely BLOCKING_REQUIRED
for an exact defended downstream scope?
```

A successor experiment should prospectively test whether blocking status needs stronger explicit system-owned dependency/claim-scope structure or another bounded calibration mechanism. It must preserve strong GENERIC and FULL_HORIZON controls, retain the system-owned provenance boundary, and avoid tuning from repeated Specification 019 outputs.

No new provider-backed recommendation experiment is currently authorized. The Specification 019 one-shot authorization and temporary live/observer/preservation helpers have been retired from `main`.

---

## Exact continuation

```text
1. preregister the next recommendation/blocking-calibration experiment before implementation
2. define the exact represented relation between unresolved work and defended downstream scope
3. preserve the accepted DEFER dependency construction and system-owned provenance boundary
4. retain strong GENERIC and FULL_HORIZON controls
5. do not tune truth, thresholds, or treatment from repeated Specification 019 outputs
6. freeze the successor fixture, gates, call plan, and checkpoint
7. validate its exact implementation head provider-free
8. authorize any future live run only through Specification 018 after the exact head is green
9. make no new recommendation/action provider call before those conditions are met
```

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures and incomplete runs as evidence, and promote only what earns its complexity.
