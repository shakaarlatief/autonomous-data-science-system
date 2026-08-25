# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 192  
**Active development branch:** `v1-spec022-incomplete-preservation`  
**Active PR:** #72  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`

## Start here

```text
README.md                         project overview and current evidence boundary
docs/CURRENT_STATE.md             present state and exact continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable routing metadata only
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
promoted integration head       0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
active branch                   v1-spec022-incomplete-preservation
active PR                       #72
Specification 015 PR            #13 closed without merge; preservation #14 merged
Specification 016 PR            #15 merged
Specification 017 PR            #16 closed without merge; preservation #22 merged
Specification 018 PR            #23 merged
Specification 019 PR            #33 closed without merge; preservation #43 merged
Specification 020 PR            #44 merged
routing consistency PR          #54 merged
Specification 021 impl PR       #55 closed without merge
Specification 021 preserve PR   #66 merged
Question A architecture PR      #67 merged at 0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
Specification 022 impl PR       #68 open draft; must close without merge after preservation
Specification 022 preserve PR   #72 active preservation-only candidate
main                            governed live-launch control plane; no active Specification 022 authorization
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
    dependency-backed DEFER-vs-NOT_NOW diagnostic supported

Specification 017 / Checkpoints 156-159
    relation-backed recommendation experiment INCOMPLETE; implementation rejected

Specification 018 / Checkpoints 160-162
    governed autonomous live-experiment launcher supported and promoted

Specification 019 / Checkpoints 163-166
    system-owned provenance rerun completed; FAIL preserved

Specification 020 / Checkpoints 167-171
    RECOMMENDED-vs-BLOCKING_REQUIRED diagnostic completed; BLOCKING_BOUNDARY_SUPPORTED promoted

Checkpoint 172 / PR #54
    machine-readable current routing pointers + lightweight contradiction validator promoted

Specification 021 / Checkpoints 174-185
    dependency-backed supplied-action recommendation experiment completed; FAIL preserved; failed implementation rejected

Research 031 / Checkpoint 186 / PR #67
    methodological-navigation / coverage architecture and evaluation review completed

Research 032 / Checkpoint 187
    first project-state methodological coverage diagnostic design choices resolved

Specification 022 / Checkpoint 188
    exact project-state-to-methodological-horizon coverage diagnostic contract frozen

Checkpoint 189
    provider-free Specification 022 implementation gate passed cross-platform

Checkpoint 190
    exact live-capable source `cf5893d74fefa699296842b0a48326a9cb50161c` frozen

Checkpoint 191
    governed live execution preserved as INCOMPLETE / EXECUTION INTEGRITY FAILED; no scientific advancement classification; knowledge-universe stage selected next

Checkpoint 192 / PR #72
    preservation-only promotion candidate carrying durable Specification 022 evidence/history while excluding the incomplete experiment implementation
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
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```

Key navigation sequence:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Key scaling rule:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Research 028 is forward research rather than accepted production semantics. It establishes the broad construction direction: persistent project state is system-owned; methodological navigation determines what matters from that state; and the broad knowledge base should be a governed revisioned methodological universe rather than an undifferentiated RAG corpus.

Project Cockpit:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

## Persistence, interchange, and runtime

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

This supports selective context economy on the bounded benchmark. It does not select a final embedding/reranking/vector stack or a universal context budget.

---

## Recommendation/action evidence

Specification 015:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL`. Implementation not promoted.

Specification 016:

```text
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

Supported bounded construct:

```text
DEFER-like sequencing
    -> concrete represented activating dependency/trigger
```

Specification 017:

```text
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
experiments/relation_backed_recommendation_action_value/V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `INCOMPLETE`. Instrumentation lesson:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

Specification 019:

```text
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL`. System-owned provenance repair succeeded but recommendation/action value did not.

Specification 020:

```text
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
```

Frozen result: `BLOCKING_BOUNDARY_SUPPORTED` for deliberately unambiguous dependency-backed microstates. This does not establish production recommendation enums or selective-context recommendation value.

Specification 021:

```text
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/research/029_dependency_backed_recommendation_value_design.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
docs/checkpoints/182_specification_021_complete_live_result_failed.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL`. The supplied-action benchmark tested downstream disposition calibration, not open-world methodological path discovery from evolving project state.

---

## Specification 022 route

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

Frozen benchmark evidence retained by preservation PR #72:

```text
tests/fixtures/methodological_navigation/spec022_contract_fixture_manifest_v1.json
tests/fixtures/methodological_navigation/spec022_coverage_oracle_v1.json
tests/fixtures/methodological_navigation/spec022_methodological_universe_v1.json
tests/fixtures/methodological_navigation/spec022_oracle_representation_map_v1.json
tests/fixtures/methodological_navigation/spec022_project_state_episodes_v1.json
```

Live result and raw-before-interpretation commitment:

```text
docs/checkpoints/191_specification_022_live_execution_incomplete_knowledge_universe_next.md
experiments/methodological_navigation_coverage/V1_METHODOLOGICAL_NAVIGATION_COVERAGE_RESULT.md
experiments/methodological_navigation_coverage/results/spec022-live-20260825-run-32815726116/PRE_INTERPRETATION_ARTIFACT_COMMITMENT.md
```

Scientific classification:

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

The frozen schema accepted only `CURRENT | MISSING_CONTEXT`; the live model repeatedly returned alternative state vocabularies and every result failed structured validation. No substantive comparison among `GENERIC`, `ADS_HORIZON`, and `ORACLE_HORIZON` is valid.

The failure is execution-contract evidence, not evidence for or against the methodological-navigation hypothesis.

The experiment implementation remains historical on PR #68 and is intentionally excluded from preservation PR #72.

---

## Governed autonomous live-launch route

```text
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
docs/checkpoints/160_governed_autonomous_live_experiment_launcher_contract_frozen.md
docs/checkpoints/161_governed_autonomous_live_experiment_launcher_end_to_end_gate_passed.md
scripts/ads_live_experiment_launcher.py
.github/ads_live_experiments.json
.github/workflows/v1-autonomous-live-experiment-launcher.yml
```

Accepted control-plane sequence:

```text
owner request transport
    -> repository authorization registry
    -> exact owner/source/CI/duplicate checks
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

Specification 022 exercised this accepted path once. Its one-shot authorization has been retired, the registry is empty, and Issues #69-#71 are closed with audit history preserved.

---

## Preservation and continuity

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
routing/current-state drift           YES, observed again at the unexpected Session-05 boundary
```

Checkpoint 191 preserved the substantive result and strategic shift before the conversation ended. Checkpoint 192 and PR #72 perform the missing preservation-only routing reconciliation.

Markdown remains the substantive source of truth. The routing manifest is not a replacement for canonical documents, foundations, specifications, checkpoints, results, or Git history.

---

## Methodological knowledge-universe construction route

Primary conceptual sources:

```text
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/checkpoints/191_specification_022_live_execution_incomplete_knowledge_universe_next.md
```

The next chronological architecture is:

```text
1. serious governed methodological knowledge universe
2. navigation / selection over that universe
3. project-specific concern / question / option generation
4. prioritization / disposition
5. execution and project-state update
6. real end-to-end project trials
7. governed knowledge evolution
```

Before bulk authoring, the next branch should freeze a construction framework covering:

```text
broad data-science coverage map
knowledge package/component pressure tests
source and authority policy
component-level provenance policy
maturity/lifecycle policy
duplicate and contradiction handling
knowledge QA/review workflow
breadth-versus-depth strategy
deep heterogeneous vertical-slice priorities
```

Initial deep slices should deliberately differ structurally. Current candidates include validation, missing data, feature selection, model families/tree ensembles, class imbalance/metrics/calibration, and time-series methodology.

---

## Current exact continuation

```text
A. validate preservation-only PR #72 on its exact head
B. merge PR #72 only if the evidence/history-only boundary remains clean and green
C. close Specification 022 implementation PR #68 without merge
D. reconcile v1-frontend-spike to the preserved Checkpoint 192 boundary
E. create a dedicated methodological-knowledge-universe branch from the clean integration head
F. freeze the construction framework before bulk knowledge authoring
G. do not immediately rerun the 216-call Specification 022 matrix
H. do not modify or rescore Specifications 015-022
```

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
162  governed autonomous launcher promoted to V1 integration
166  Specification 019 complete live result classified FAIL and preserved
171  Specification 020 live diagnostic completed; BLOCKING_BOUNDARY_SUPPORTED
172  machine-checkable current-routing consistency guard promoted
183  supplied-action disposition calibration separated from open-world methodological navigation / coverage
185  Specification 021 FAIL preserved and failed implementation closed
186  Question A methodological-navigation architecture/evaluation review completed
187  first project-state methodological coverage design choices resolved
188  Specification 022 exact scientific contract and fixtures frozen
189  Specification 022 provider-free implementation gate passed
190  Specification 022 exact live-capable source frozen
191  Specification 022 live execution INCOMPLETE; knowledge-universe stage next
192  Specification 022 incomplete evidence preservation-only promotion candidate
```
