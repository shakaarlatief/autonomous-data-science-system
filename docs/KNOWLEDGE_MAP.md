# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 193  
**Active development branch:** `v1-methodological-knowledge-universe`  
**Active PR:** #73  
**Promoted V1 integration branch:** `v1-frontend-spike` at `bb5d0640fff633e87a6a8c024b1a842fadd85a9d`

## Start here

```text
README.md                         project overview and current stage
docs/CURRENT_STATE.md             exact present state and continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable routing metadata only
docs/VISION.md                    high-level system/product direction
docs/PRINCIPLES.md                accepted high-level design principles
docs/DECISIONS.md                 accepted project-level decisions
docs/OPEN_QUESTIONS.md            unresolved questions
docs/DEVELOPMENT_METHOD.md        project development/preservation method
docs/CONTINUITY.md                cross-session continuation procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current branch relationship:

```text
promoted integration head       bb5d0640fff633e87a6a8c024b1a842fadd85a9d
active branch                   v1-methodological-knowledge-universe
active PR                       #73
Specification 022 impl PR       #68 closed without merge
Specification 022 preserve PR   #72 merged at bb5d0640fff633e87a6a8c024b1a842fadd85a9d
main                            governed live-launch control plane; no active Specification 022 authorization
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; its incomplete implementation was not promoted.

---

# Current stage: serious methodological knowledge universe

Primary active sources:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

Current sequence:

```text
KU-0  broad coverage map                              ESTABLISHED
KU-1  six deep representation pressure tests          NEXT
KU-2  revise representation/source/lifecycle rules
KU-3  build accepted supervised-data-science core
KU-4  expand specialized domains and model families
KU-5  real project trials against materially larger coverage
KU-6  governed knowledge evolution from project gaps
```

First six deep slices:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

The next design artifact should establish the source-register/source-bundle candidate contract and the coordinated six-slice pressure-test packet.

---

## Coverage-map route

```text
docs/methodological_knowledge/COVERAGE_MAP.md
```

The coverage map is a planning/gap-visibility layer, not methodological authority.

Coverage depth:

```text
C0  MAPPED
C1  SOURCED
C2  DECOMPOSED
C3  OPERATIONALIZED
C4  CONNECTED
C5  BEHAVIORALLY_TESTED
C6  PROJECT_EXPOSED
```

Coverage depth must not be interpreted as truth, maturity, source authority, freshness, or enforcement authority.

---

## Reusable-knowledge architecture

Primary conceptual sources:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```

Current durable representation direction:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
exact revision identity
provenance
```

Important separations:

```text
global reusable knowledge != project-specific state
knowledge identity != reasoning function
asset != component != narrative facet
static relation != conditional rule
retrieval cue != applicability != required context != project relevance
methodological knowledge != execution implementation
coverage depth != epistemic maturity
```

Research 033 deliberately allows serious content to challenge this representation before broad catalog scale makes changes expensive.

---

## Source, provenance, and knowledge governance

Primary source:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
```

Governing earlier source:

```text
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Current construction direction:

```text
source authority is proposition-sensitive
component-level provenance for consequential reusable claims
LLM extraction/proposal != independent authority
freshness sensitivity belongs to the proposition/source relation
candidate knowledge must use accepted governance/interchange paths
```

The next step must resolve a practical source-register/source-bundle candidate representation through the six-slice pressure test.

---

## Knowledge QA route

Research 033 requires eventual QA at multiple levels:

```text
structural
source support
semantic scope / claim strength
cross-knowledge duplicate / contradiction / alias / cycle checks
behavioral regression cases
real-project coverage behavior
```

Foundation 008 provides the broader maturity, challenge, counterexample, minimum-generalization, and enforcement framework.

---

# Product and project-object architecture

Primary sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

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

Project Cockpit:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

# Persistence, interchange, and runtime

Accepted decisions:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind ADS-owned ReasoningRuntime
```

Primary sources:

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

Accepted authority distinction:

```text
operational database authority
    !=
interchange representation
    !=
derived retrieval indexes
```

Normal candidate/benchmark import cannot silently create accepted methodological authority.

---

# Retrieval -> Horizon -> selective context -> reasoning

```text
Specification 009 / Checkpoint 135   lexical retrieval baseline
Specification 010 / Checkpoint 137   dense semantic complementarity
Specification 011 / Checkpoint 139   bounded RRF comparator
Specification 012 / Checkpoint 141   explained MethodologicalHorizon
Specification 013 / Checkpoint 143   selective exact-revision context
Specification 014 / Checkpoint 146   real reasoning-context value
```

Key applicability invariant:

```text
known false -> INAPPLICABLE
unknown required information -> MISSING_CONTEXT
unknown != false
```

Specification 014 result:

```text
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
```

The current stage does not tune retrieval further. Navigation should be revisited after the knowledge universe is materially larger.

---

# Recommendation/action evidence

## Specification 015

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL`.

## Specification 016

```text
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

Supported bounded construct:

```text
DEFER-like sequencing
    -> concrete represented activating dependency / trigger
```

## Specification 017

```text
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
```

Frozen result: `INCOMPLETE`.

Instrumentation lesson:

```text
reasoning function / task profile
    !=
reusable knowledge provenance
```

## Specification 019

```text
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL` after provenance instrumentation was repaired.

## Specification 020

```text
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
```

Frozen result: `BLOCKING_BOUNDARY_SUPPORTED` for deliberately unambiguous dependency-backed microstates.

## Specification 021

```text
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/research/029_dependency_backed_recommendation_value_design.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
docs/checkpoints/182_specification_021_complete_live_result_failed.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL`.

Important interpretation:

```text
supplied-action disposition calibration
    !=
open-world methodological navigation / coverage
```

---

# Specification 022 preserved route

Design and frozen contract:

```text
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md
docs/checkpoints/187_project_state_methodological_coverage_design_choices_resolved.md
docs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md
docs/checkpoints/190_specification_022_live_capable_source_frozen.md
```

Incomplete live result and transition:

```text
docs/checkpoints/191_specification_022_live_execution_incomplete_knowledge_universe_next.md
docs/checkpoints/192_specification_022_incomplete_result_preservation_promotion_candidate.md
experiments/methodological_navigation_coverage/V1_METHODOLOGICAL_NAVIGATION_COVERAGE_RESULT.md
experiments/methodological_navigation_coverage/results/spec022-live-20260825-run-32815726116/PRE_INTERPRETATION_ARTIFACT_COMMITMENT.md
```

Frozen classification:

```text
INCOMPLETE / EXECUTION INTEGRITY FAILED
```

Observed counts:

```text
planned reasoner observations     108
valid reasoner observations         0
planned judge observations        108
valid judge observations            0
provider attempts                 216
advancement outcome              none
```

No substantive `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison is valid.

The incomplete experiment implementation remained on PR #68 and was closed without merge after preservation-only PR #72 succeeded.

---

# Governed live-launch route

```text
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
docs/checkpoints/160_governed_autonomous_live_experiment_launcher_contract_frozen.md
docs/checkpoints/161_governed_autonomous_live_experiment_launcher_end_to_end_gate_passed.md
scripts/ads_live_experiment_launcher.py
.github/ads_live_experiments.json
.github/workflows/v1-autonomous-live-experiment-launcher.yml
```

The Specification 022 one-shot authorization is retired. No new provider run is authorized by the knowledge-universe construction stage.

---

# Preservation and continuity

Primary sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/checkpoints/README.md
docs/checkpoints/172_machine_checkable_current_routing_consistency_guard_passed.md
```

Current Level-2 lesson:

```text
substantive preservation failure      NO
routing/current-state drift           repaired through Checkpoint 192
```

The current stage begins cleanly from the preserved integration head `bb5d0640fff633e87a6a8c024b1a842fadd85a9d`.

---

# Prototype V0

Authoritative result:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Do not restart or tune P0 against the completed benchmark.

---

# Exact current continuation

```text
A. validate the reconciled Checkpoint 193 / Research 033 / coverage-map head
B. design a source-register / source-bundle candidate contract
C. construct one coordinated six-slice representation pressure-test packet
D. register existing controlled source material before accepting extracted knowledge
E. add external authoritative sources when proposition support requires them
F. record representation defects instead of forcing content into the current schema
G. revise representation only where observed content pressure warrants it
H. after the six-slice review, begin broader accepted-core construction
I. revisit navigation/selection against the serious universe
J. begin real project trials before the knowledge universe is complete
K. do not rerun Specification 022 as the immediate next step
L. do not modify or rescore Specifications 015-022
```
