# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-23  
**Current checkpoint:** 159  
**Active development branch:** `v1-recommendation-action-value-relation-backed`  
**Active PR:** #16 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 016 promotion merge `6bda0c1efcf078476859b2c2c64fb0586964899d`

## Start here

```text
README.md
    project overview and current evidence boundary

docs/CURRENT_STATE.md
    present state and exact continuation

docs/KNOWLEDGE_MAP.md
    routing/index layer

docs/VISION.md
    high-level system and product direction

docs/PRINCIPLES.md
    accepted high-level design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved design/evaluation questions

docs/DEVELOPMENT_METHOD.md
    development/checkpoint/promotion method

docs/CONTINUITY.md
    continuation and unexpected-boundary recovery

docs/MAJOR_CHANGES.md
    selective structural history
```

Current branch relationship:

```text
promoted integration head      6bda0c1efcf078476859b2c2c64fb0586964899d
active experiment branch       v1-recommendation-action-value-relation-backed
active PR                      #16 -> v1-frontend-spike
Specification 015 PR           #13 closed without merge
Specification 015 preservation #14 merged
Specification 016 PR           #15 merged
Specification 017 PR           #16 will close without implementation merge
main                           intentionally behind V1 except control-plane workflow exposure
```

---

## Current project stage

Prototype V0 final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

Durable post-V0 constraint:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Current V1 progression:

```text
Foundations 018-020
    project object/state model
    methodological navigation
    reusable methodological knowledge

D-028 through D-031 / Checkpoint 127
    local-first persistence and governed knowledge interchange

Specification 008 / Checkpoints 126,130
    promoted Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Checkpoints 135 -> 137 -> 139 -> 141
    lexical retrieval -> dense complementarity -> hybrid comparator -> explained Horizon

Specification 013 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack

Specification 014 / Checkpoint 146
    real-model selective-context gate PASS

Specification 015 / Checkpoints 147-151
    recommendation/action experiment FAIL
    failed implementation rejected
    negative evidence preserved

Specification 016 / Checkpoints 152-155
    dependency-backed DEFER-vs-NOT_NOW diagnostic
    DISPOSITION_BOUNDARY_SUPPORTED
    bounded construct constraint promoted

Specification 017 / Checkpoints 156-159
    relation-backed recommendation/action comparison
    provider-free implementation passed
    first live execution incomplete
    raw evidence preserved
    no advancement classification
    implementation not promoted
```

---

## Core architecture routes

### Product/object/system boundary

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Key distinctions:

```text
OBJECTS / RELATIONS / EVENTS / VIEWS
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
```

### Methodological navigation and reusable knowledge

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Navigation sequence:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Current accepted executable chain:

```text
knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> bounded relevance selection
    -> exact selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
```

The recommendation/action persistence and production seam remains open.

---

## Persistence, interchange, runtime, and Cockpit

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
D-032 + docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

Governed round-trip closure:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

Project Cockpit route:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

The Cockpit remains the promoted primary immersive active-work model. Final backend/API wiring and frontend technology choices remain open.

---

## Retrieval -> Horizon -> selective context route

```text
Specification 009 / Checkpoint 135
    lexical retrieval baseline

Specification 010 / Checkpoint 137
    dense semantic complementarity

Specification 011 / Checkpoint 139
    bounded RRF hybrid comparator

Specification 012 / Checkpoint 141
    first explained MethodologicalHorizon

Specification 013 / Checkpoint 143
    selective exact-revision MethodologicalContextPack
```

Key Horizon invariant:

```text
known false -> INAPPLICABLE
unknown required information -> MISSING_CONTEXT
unknown != false
```

---

## Accepted real reasoning-context route

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
docs/checkpoints/145_reasoning_context_value_implementation_gate_cross_platform_passed.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
```

Observed:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
aggregate token ratio   0.334379
input-token reduction   66.56%
```

---

## Specification 015: failed recommendation/action route

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Live result:

```text
run                 32642733784
reasoner outputs    36 / 36
judge outputs       36 / 36
advancement         FAIL
```

The failed implementation was not promoted.

---

## Specification 016: dependency-backed disposition route

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
tests/fixtures/reasoning/disposition_semantics_v1.json
docs/checkpoints/152_disposition_semantics_failure_attribution_contract_frozen.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

Live result:

```text
run                               32652636943
36 / 36 exact dispositions        correct
18 / 18 expected-DEFER pointers   exact
18 / 18 expected-NOT_NOW pointers null
outcome                           DISPOSITION_BOUNDARY_SUPPORTED
```

Promoted merge:

```text
6bda0c1efcf078476859b2c2c64fb0586964899d
```

---

## Specification 017: incomplete relation-backed recommendation/action route

Frozen design/history:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
docs/checkpoints/157_relation_backed_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/158_specification_017_live_boundary_frozen.md
```

Live incomplete-result boundary:

```text
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
experiments/relation_backed_recommendation_action_value/V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/relation_backed_recommendation_action_value/results/spec017-live-20260823-run-32656446705/
```

Mechanical result:

```text
run                         32656446705
frozen source head          bf041f4b4a485382d0e6e5c508ad916199601ee8
reasoner outputs            29 / 36
judge outputs               29 / 36
provider attempts           77 / 90
complete scored design      false
execution integrity         true
advancement outcome         none
```

Completion by condition:

```text
SELECTIVE       12 / 12
FULL_HORIZON    12 / 12
GENERIC          5 / 12
```

All 19 failed reasoner attempts were GENERIC `INVALID_STRUCTURED_RESPONSE` cases in which the model placed a requested reasoning-function label into `methodological_basis`. The system had supplied zero reusable knowledge revisions to GENERIC.

Key newly exposed boundary:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

No Specification 017 PROMOTE / SAFE / FAIL classification is assigned. The complete matched design was not obtained.

---

## Control-plane route: autonomous live-launch feasibility

During Specification 017 artifact preservation, a temporary default-branch issue-triggered workflow was successfully activated by an issue created through the connected GitHub interface.

Successful preservation workflow run:

```text
32658108544
```

It:

```text
received an owner-created issue event
    -> downloaded artifact 9497737594
    -> verified every extracted SHA-256 digest
    -> committed the raw bundle to the target experiment branch
```

This is not experiment evidence. It is control-plane feasibility evidence for a future governed autonomous live-experiment launcher.

A production-quality launcher must not accept arbitrary shell commands from issue text. It should use a fixed allowlisted experiment registry and verify actor/owner identity, exact frozen source SHA, frozen contract identity, required CI evidence, and launch uniqueness before provider execution.

---

## Current exact continuation

```text
A. reconcile PR #16 to Checkpoint 159
B. create a preservation-only branch from v1-frontend-spike
C. carry Specification 017 frozen sources, Checkpoints 156-159, stable result, raw evidence, and current routing
D. exclude the unpromoted experiment implementation from integration
E. validate and merge the preservation-only PR
F. close PR #16 without merge
G. remove temporary one-shot preservation workflows and close their issues
H. design/provider-free validate a governed autonomous live-experiment launcher
I. separately preregister the next recommendation/action-value experiment with system-owned provenance
```

Do not modify or rescore Specifications 015-017. Do not use partial Specification 017 condition scores as advancement evidence.

---

## Recent continuity checkpoints

```text
127  governed knowledge round-trip closed across SQLite/PostgreSQL
133  initial V1 reasoning runtime selected
135  lexical retrieval baseline passed
137  dense semantic comparator preserved
139  hybrid retrieval comparator passed
141  first explained MethodologicalHorizon passed
143  selective-context gate passed and promoted
146  real reasoning-context gate passed
150  first recommendation/action live gate failed
151  failed evidence preserved without implementation promotion
155  dependency-backed disposition live gate supported
156  relation-backed recommendation/action contract frozen
157  relation-backed provider-free gate passed
158  Specification 017 live boundary frozen
159  Specification 017 live execution incomplete; provenance boundary identified
```
