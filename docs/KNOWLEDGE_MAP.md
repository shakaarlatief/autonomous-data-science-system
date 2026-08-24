# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-24  
**Current checkpoint:** 168  
**Active development branch:** `v1-blocking-calibration-diagnostic`  
**Active PR:** #44 draft  
**Promoted V1 integration branch:** `v1-frontend-spike` at reconciled head `b9c9c3a38935983075a9ca88632177980bb20ede`

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
promoted integration head      b9c9c3a38935983075a9ca88632177980bb20ede
active branch                  v1-blocking-calibration-diagnostic
active PR                      #44 draft
Specification 015 PR           #13 closed without merge; preservation #14 merged
Specification 016 PR           #15 merged
Specification 017 PR           #16 closed without merge; preservation #22 merged
Specification 018 PR           #23 merged
Specification 019 PR           #33 closed without merge
Specification 019 preservation #43 merged
Specification 020 PR           #44 active diagnostic
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

Specification 018 / Checkpoints 160-162
    governed autonomous live-experiment launcher frozen, implemented, cross-platform validated, end-to-end provider-free probe passed, and promoted to integration

Specification 019 / Checkpoints 163-166
    system-owned provenance rerun frozen, cross-platform validated, autonomously launched, completed, classified FAIL, and preserved without implementation promotion

Specification 020 / Checkpoints 167-168
    RECOMMENDED-vs-BLOCKING_REQUIRED construct-validity diagnostic frozen and provider-free implementation validated cross-platform
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
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```

Research 028 is a research-only forward synthesis. It records the architectural distinction that the system owns persistent project state, methodological navigation determines what matters from that state, and the broad knowledge base should be built as a governed revisioned methodological universe rather than an undifferentiated RAG corpus. It does not modify Specification 020 or authorize provider execution.

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

Specification 019 system-owned-provenance rerun:

```text
docs/research/026_system_owned_provenance_recommendation_action_value_design.md
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/system_owned_provenance_recommendation_action_value/results/spec019-live-20260824-run-32664534864/
```

Frozen Specification 019 result:

```text
source                      6b5e6237b738250458550f95c9f3a6b0d51e86ec
run                         32664534864
reasoner outputs            36 / 36
judge outputs               36 / 36
retries                     0
execution integrity         true
GENERIC exact               0.944444
SELECTIVE exact             0.916667
FULL_HORIZON exact          0.944444
semantic all conditions     0.950000
SELECTIVE blocking FP       6
FULL_HORIZON blocking FP    4
outcome                     FAIL
```

Stable instrumentation boundary after Specifications 017-019:

```text
SYSTEM-OWNED PROVENANCE
    exact supplied stable_key@revision_id
    methodology payload digest and bytes
    treatment identity

MODEL-OWNED CONTENT
    dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales
```

Specification 019 closed the provenance instrumentation defect but did not establish recommendation/action value.

---

## Specification 020: recommendation/blocking calibration diagnostic

Frozen and implementation-gate sources:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
tests/fixtures/reasoning/blocking_calibration_v1.json
docs/checkpoints/167_recommended_vs_blocking_required_calibration_contract_frozen.md
docs/checkpoints/168_recommended_vs_blocking_required_calibration_implementation_gate_cross_platform_passed.md
experiments/blocking_calibration/harness.py
experiments/blocking_calibration/runner.py
.github/workflows/v1-blocking-calibration.yml
```

Frozen semantic boundary:

```text
BLOCKING_REQUIRED
    currently justified action
    + exact unresolved supplied requirement
    + exact active defended supplied downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action resolves that requirement
    + exact requirement and scope pointers

RECOMMENDED
    materially worthwhile action now or soon
    + no exact active supplied downstream scope blocked on it
    + both blocking pointers null
```

The fixture contains six contrastive pairs:

```text
BC-01  prediction-time feature availability
BC-02  temporal validation sensitivity
BC-03  missing-data treatment sensitivity
BC-04  subgroup error analysis
BC-05  probability calibration assessment
BC-06  nonlinear model-family comparison
```

Frozen planned live shape, only if later boundaries earn authorization:

```text
36 planned successful reasoner calls
45 maximum provider attempts
seed 2026082401
one reasoner condition
no methodological assets
no retrieval/Horizon/selective context
no semantic judge
no tools
no project mutation
```

Frozen hard gates require structural validity, aggregate/per-variant/per-pair correctness, exact requirement/scope pointers for all 18 blocking observations, and both pointers null for all 18 recommended observations.

Allowed outcomes:

```text
BLOCKING_BOUNDARY_SUPPORTED
BLOCKING_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

Exact provider-free implementation boundary:

```text
head                                fb8327aae859f53bbb0c4d7bba70b32b6033343e
V1 blocking calibration             32697487230  success
Ubuntu dedicated                    16 passed
Windows dedicated                   16 passed
Ubuntu full V1                      115 passed, 2 skipped
Windows full V1                     115 passed, 2 skipped
Checkpoint metadata                 32697487221  success
V1 reasoning context value          32697487202  success
V1 disposition semantics            32697487256  success
V1 autonomous launcher CI           32697487239  success
provider credential                 absent
```

A provider-free edge-case repair ensures the frozen 45-attempt ceiling produces a preserved `INCOMPLETE` result rather than escaping the scientific outcome boundary as an exception.

Current provider boundary:

```text
live runtime default       absent
live CLI                    absent
live workflow               absent
Spec020 authorization      absent
provider calls             0
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

Exact accepted evidence:

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

The launcher receives no provider credential. A provider-backed experiment may be authorized only after its own contract is frozen and its exact implementation/live-capable head is provider-free green.

Specification 019 used this path successfully for its one authorized provider-backed run. Its one-shot authorization is retired, the temporary Specification 019 live/observer/preservation helpers have been removed from `main`, and temporary issues 34-42 are closed with audit history retained.

---

## Current exact continuation

```text
A. validate the fully reconciled Checkpoint 168 branch head on Specification 020 Ubuntu/Windows CI and accepted V1 regression seams
B. freeze a separate pre-live boundary checkpoint only after that head is green
C. only after the pre-live checkpoint add an explicit live runtime entry path and workflow
D. validate the live-capable source provider-free
E. authorize at most one frozen run through Specification 018
F. preserve raw live evidence before interpretation or tuning
```

Do not modify or rescore Specifications 015-019. Do not weaken Specification 020 gates after implementation or results. No new recommendation/action provider call is currently authorized.

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
162  governed autonomous launcher promoted to V1 integration
163  Specification 019 system-owned-provenance contract frozen
164  Specification 019 provider-free/live source boundary validated
165  Specification 019 governed live authorization frozen
166  Specification 019 complete live result classified FAIL and preserved
167  RECOMMENDED-vs-BLOCKING_REQUIRED diagnostic contract frozen
168  Specification 020 provider-free implementation gate passed cross-platform
```