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
checkpoint            168
active branch         v1-blocking-calibration-diagnostic
active PR             #44 draft
promoted V1 head      b9c9c3a38935983075a9ca88632177980bb20ede
current boundary      Specification 020 provider-free implementation green
                      RECOMMENDED vs dependency-backed BLOCKING_REQUIRED diagnostic
                      exact reconciled pre-live boundary next
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

Specification 020
    RECOMMENDED-vs-BLOCKING_REQUIRED calibration contract frozen
    provider-free implementation cross-platform green
    no live workflow or provider call authorized yet
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/checkpoints/167_recommended_vs_blocking_required_calibration_contract_frozen.md
docs/checkpoints/168_recommended_vs_blocking_required_calibration_implementation_gate_cross_platform_passed.md
tests/fixtures/reasoning/blocking_calibration_v1.json
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

The production-facing recommendation/action layer remains unpromoted after Specifications 015, 017, and 019 failed or incomplete recommendation-value attempts. Specification 020 is a construct-validity diagnostic, not production recommendation promotion.

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

The central recommendation-calibration problem was RB-02. SELECTIVE repeatedly promoted two useful model-comparison actions from expected `RECOMMENDED` to `BLOCKING_REQUIRED`, while correctly preserving the DEFER dependency for later tuning. GENERIC and FULL_HORIZON showed the same tendency less consistently.

RB-04 also missed the preregistered per-case semantic floor in all three conditions because the responses omitted one explicit training-only preprocessing/leakage-prevention obligation. The frozen contract does not permit a post-hoc exemption.

The Specification 019 recommendation/action implementation is not promoted. Its frozen authority and failure evidence were merged through preservation-only PR #43; failed implementation PR #33 is closed without merge.

Primary evidence:

```text
docs/research/026_system_owned_provenance_recommendation_action_value_design.md
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/
    V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

### Specification 020

Specification 020 isolates the remaining calibration question before another recommendation-value comparison.

Frozen distinction:

```text
BLOCKING_REQUIRED
    candidate action is currently justified
    + exact unresolved supplied requirement
    + exact active defended supplied downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action resolves that requirement for that scope
    + exact requirement and scope pointers

RECOMMENDED
    action is materially worthwhile now or soon
    + no exact active supplied downstream scope is represented as blocked on it
    + both blocking pointers null
```

High priority, high expected value, common best practice, and possible future usefulness are explicitly insufficient on their own for blocking status.

The frozen benchmark contains six contrastive pairs across prediction-time feature availability, temporal validation sensitivity, missing-data treatment sensitivity, subgroup error analysis, probability calibration, and nonlinear model-family comparison.

Frozen planned live shape, only if a later pre-live and live-capable boundary earns authorization:

```text
6 pairs x 2 variants x 3 repetitions
36 planned successful reasoner calls
45 maximum provider attempts
seed 2026082401
one reasoner condition
no reusable methodology
no semantic judge
no tools
no project mutation
```

Allowed outcomes are only:

```text
BLOCKING_BOUNDARY_SUPPORTED
BLOCKING_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

Provider-free implementation evidence at exact head `fb8327aae859f53bbb0c4d7bba70b32b6033343e`:

```text
V1 blocking calibration diagnostic   run 32697487230   success
Ubuntu dedicated                     16 passed
Windows dedicated                    16 passed
Ubuntu full V1                       115 passed, 2 skipped
Windows full V1                      115 passed, 2 skipped
provider credential                  absent
```

The same exact head also passed the checkpoint, accepted reasoning-context, prior disposition, and governed-launcher regression workflows. Persistent retryable failure is now verified to stop at exactly 45 attempts and return `INCOMPLETE` with all failed attempts preserved.

No live runtime default, live CLI, live workflow, or Specification 020 authorization exists at Checkpoint 168.

---

## System-owned provenance boundary

Specification 019 provided positive bounded evidence for one architecture distinction:

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

Specification 020 preserves that separation and additionally makes the system own the supplied candidate-action, requirement, and downstream-scope identities used by the diagnostic. The model selects only among supplied IDs and does not create authoritative project relations.

---

## Current architecture boundary

The frozen diagnostic is now implemented provider-free and cross-platform green.

Current task:

```text
reconcile and validate the exact post-Checkpoint-168 branch head
    -> Specification 020 Ubuntu/Windows gate
    -> accepted V1 regression seams
    -> checkpoint metadata

then
    -> freeze a separate pre-live boundary
```

Only after that pre-live boundary is frozen may a live runtime entry path and workflow be added. Any provider-backed run must then be independently provider-free validated and authorized through Specification 018.

---

## Exact continuation

```text
1. finish canonical reconciliation to Checkpoint 168
2. validate the exact reconciled head cross-platform and across accepted V1 regression workflows
3. freeze a separate pre-live boundary checkpoint
4. only after that checkpoint add the explicit live runtime entry path and workflow
5. validate the live-capable source provider-free
6. authorize at most one frozen live run through Specification 018
7. preserve raw evidence before interpretation or tuning
8. do not modify or rescore Specification 019
9. make no new provider call before the live boundary and governance checks are complete
```

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures and incomplete runs as evidence, and promote only what earns its complexity.
