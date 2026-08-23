# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-23  
**Current checkpoint:** 161  
**Active development branch:** `v1-autonomous-live-experiment-launcher`  
**Active PR:** #23 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 017 preservation merge `4385b83b43582ff6466b519b4e96356d220c44bc`

## Start here

```text
README.md                         project overview and current evidence boundary
docs/CURRENT_STATE.md             present state and exact continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/VISION.md                    high-level system and product direction
docs/PRINCIPLES.md                accepted high-level design principles
docs/DECISIONS.md                 accepted project-level decisions
docs/OPEN_QUESTIONS.md            unresolved design/evaluation questions
docs/DEVELOPMENT_METHOD.md        checkpoint/promotion method
docs/CONTINUITY.md                continuation procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current branch relationship:

```text
promoted integration head      4385b83b43582ff6466b519b4e96356d220c44bc
active branch                  v1-autonomous-live-experiment-launcher
active PR                      #23 -> v1-frontend-spike
Specification 015 PR           #13 closed without merge; preservation #14 merged
Specification 016 PR           #15 merged
Specification 017 PR           #16 closed without merge; preservation #22 merged
main                           intentionally behind V1 application code except narrow launcher exposure
```

---

## Current V1 progression

```text
Foundations 018-020
    project objects / methodological navigation / reusable knowledge

D-028 through D-031 / Checkpoint 127
    local-first persistence and governed knowledge interchange

Specification 008 / Checkpoints 126, 130
    promoted Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Specifications 009-012 / Checkpoints 135-141
    lexical -> dense complementarity -> hybrid comparator -> explained Horizon

Specification 013 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack

Specification 014 / Checkpoint 146
    real-model selective-context gate PASS

Specification 015 / Checkpoints 147-151
    recommendation/action experiment FAIL; negative evidence preserved

Specification 016 / Checkpoints 152-155
    dependency-backed disposition diagnostic supported

Specification 017 / Checkpoints 156-159
    relation-backed recommendation experiment incomplete; raw evidence preserved; implementation rejected

Specification 018 / Checkpoints 160-161
    governed autonomous live-experiment launcher frozen, implemented, cross-platform validated, and end-to-end provider-free probe passed
```

---

## Core architecture routes

Product/object/system:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Methodological navigation and reusable knowledge:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Navigation sequence:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Project Cockpit:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

## Retrieval -> Horizon -> selective context -> reasoning

```text
Specification 009 / Checkpoint 135   lexical retrieval baseline
Specification 010 / Checkpoint 137   dense semantic complementarity
Specification 011 / Checkpoint 139   bounded RRF comparator
Specification 012 / Checkpoint 141   explained MethodologicalHorizon
Specification 013 / Checkpoint 143   selective exact-revision context
Specification 014 / Checkpoint 146   real reasoning-context value
```

Key invariant:

```text
known false -> INAPPLICABLE
unknown required information -> MISSING_CONTEXT
unknown != false
```

Specification 014 result:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
aggregate token ratio   0.334379
input-token reduction   66.56%
```

---

## Recommendation/action evidence

Specification 015 failed first live recommendation/action test:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Specification 016 dependency-backed disposition evidence:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

Specification 017 incomplete relation-backed comparison:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
experiments/relation_backed_recommendation_action_value/V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/relation_backed_recommendation_action_value/results/spec017-live-20260823-run-32656446705/
```

Stable next-experiment boundary:

```text
SYSTEM-OWNED PROVENANCE
    exact supplied stable_key@revision_id
    context digest
    treatment identity

MODEL-OWNED CONTENT
    dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales
```

---

## Specification 018: governed autonomous live-launch route

```text
docs/research/025_governed_autonomous_live_experiment_launcher_design.md
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
docs/checkpoints/160_governed_autonomous_live_experiment_launcher_contract_frozen.md
docs/checkpoints/161_governed_autonomous_live_experiment_launcher_end_to_end_gate_passed.md
scripts/ads_live_experiment_launcher.py
.github/ads_live_experiments.json
.github/workflows/v1-autonomous-live-experiment-launcher.yml
.github/workflows/v1-live-launcher-probe.yml
tests/unit/test_ads_live_experiment_launcher.py
```

Exact evidence:

```text
implementation source   27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
provider-free CI        32660168566
launch issue            31
launcher run            32660333663
probe run               32660340429
probe job               97245432893
observer issue          32
observer run            32660375449
outcome                 GOVERNED_LAUNCHER_SUPPORTED
```

Accepted control-plane sequence:

```text
owner request transport
    -> repository authorization registry
    -> exact owner/source/CI/duplicate checks
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

The launcher receives no provider credential. A provider-backed experiment may be authorized only after its own contract is frozen and its exact implementation head is green.

---

## Current exact continuation

```text
A. reconcile Checkpoint 161 and Specification 018 v1.0
B. clean one-shot probe authorization and temporary main-branch observer/validation helpers
C. validate exact final PR #23 head
D. merge PR #23 into v1-frontend-spike
E. record exact promoted merge boundary
F. preregister next recommendation/action-value experiment with system-owned provenance
G. do not make a new recommendation/action provider call before the new contract and exact implementation head are frozen and green
```

Do not modify or rescore Specifications 015-017. Do not use partial Specification 017 scores as advancement evidence.

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
159  Specification 017 live execution incomplete; provenance boundary identified
160  governed autonomous launcher contract frozen
161  governed autonomous launcher end-to-end provider-free gate passed
```
