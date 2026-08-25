# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 190  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
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
promoted integration head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
active branch                  v1-methodological-navigation-coverage-diagnostic
active PR                      #68
Specification 015 PR           #13 closed without merge; preservation #14 merged
Specification 016 PR           #15 merged
Specification 017 PR           #16 closed without merge; preservation #22 merged
Specification 018 PR           #23 merged
Specification 019 PR           #33 closed without merge
Specification 019 preservation #43 merged
Specification 020 PR           #44 merged
routing consistency PR         #54 merged
Specification 021 impl PR      #55 closed without merge; failed implementation rejected
Specification 021 preserve PR  #66 merged at ef6b45a84f43a5dfe33cf5c13351cb1235e6e661
Question A architecture PR     #67 merged at 0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
Question A diagnostic PR        #68 active draft; Specification 022 live-capable source frozen; separate authorization next
main                           governed live-launch control plane; no active Specification 022 authorization
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
    relation-backed recommendation experiment incomplete; raw evidence preserved; implementation rejected

Specification 018 / Checkpoints 160-162
    governed autonomous live-experiment launcher supported and promoted

Specification 019 / Checkpoints 163-166
    system-owned provenance rerun completed; recommendation-value gates FAIL; evidence preserved without implementation promotion

Specification 020 / Checkpoints 167-171
    RECOMMENDED-vs-BLOCKING_REQUIRED contract frozen, provider-free and live boundaries validated, governed live run completed, BLOCKING_BOUNDARY_SUPPORTED preserved and promoted through PR #44

Checkpoint 172 / PR #54
    machine-readable current routing pointers + lightweight cross-platform contradiction validator green and promoted into v1-frontend-spike

Specification 021 / Checkpoints 174-182
    dependency-backed supplied-action recommendation experiment completed; frozen outcome FAIL; raw evidence and stable result preserved; failed implementation rejected

Research 030 / Checkpoint 183
    architectural interpretation clarified: methodological navigation / coverage is not equivalent to downstream disposition calibration over an already supplied action set

Checkpoint 184 / PR #66
    preservation-only promotion candidate carrying Specification 021 evidence/history without the rejected implementation

Checkpoint 185
    PR #66 merged, PR #55 closed without merge, Specification 021 FAIL preserved, and methodological-navigation / coverage architecture-evaluation review is the next legitimate boundary

Research 031 / Checkpoint 186 / PR #67
    state-driven methodological-navigation / coverage architecture and evaluation review completed and promoted through PR #67

Research 032 / Checkpoint 187 / PR #68
    first project-state methodological coverage diagnostic design choices resolved

Specification 022 / Checkpoint 188 / PR #68
    exact project-state-to-methodological-horizon coverage diagnostic contract frozen before implementation or provider execution

Checkpoint 189 / PR #68
    provider-free Specification 022 contract/navigation/request/scoring/artifact machinery green cross-platform; scientific outcome remains unexecuted; no provider call authorized

Checkpoint 190 / PR #68
    exact live-capable source `cf5893d74fefa699296842b0a48326a9cb50161c` frozen at `v1-spec022-methodological-navigation-coverage-live-source`; separate authorization remains required before provider execution
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
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md
docs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md
```

Research 028 is forward research only. It records the distinction that the system owns persistent project state, methodological navigation determines what matters from that state, and the broad knowledge base should be a governed revisioned methodological universe rather than an undifferentiated RAG corpus.

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

The result supports selective context economy on the bounded benchmark. It does not select a final embedding/reranking/vector stack or a universal context budget.

---

## Recommendation/action evidence

### Specification 015

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen result: `FAIL`. Implementation not promoted.

### Specification 016

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

### Specification 017

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

### Specification 019

```text
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/system_owned_provenance_recommendation_action_value/results/spec019-live-20260824-run-32664534864/
```

Frozen result:

```text
source                      6b5e6237b738250458550f95c9f3a6b0d51e86ec
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

Specification 019 closed the provenance instrumentation defect but did not establish recommendation/action value.

### Specification 020

Primary sources:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/checkpoints/167_recommended_vs_blocking_required_calibration_contract_frozen.md
docs/checkpoints/168_recommended_vs_blocking_required_calibration_implementation_gate_cross_platform_passed.md
docs/checkpoints/169_recommended_vs_blocking_required_calibration_pre_live_boundary_frozen.md
docs/checkpoints/170_recommended_vs_blocking_required_calibration_live_source_frozen.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
```

Frozen live result:

```text
source                               82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
reasoner outputs                     36 / 36
provider attempts                    36 / 45
aggregate exact disposition accuracy 1.000000
all 12 variants                      3 / 3 correct
all 6 pair sides                     3 / 3 correct
joint blocking-pointer accuracy      1.000000
RECOMMENDED null-pointer correctness 1.000000
outcome                              BLOCKING_BOUNDARY_SUPPORTED
```

Accepted bounded experiment-design evidence:

```text
BLOCKING_REQUIRED-like cases
    exact unresolved requirement
    + exact active defended downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action resolves the requirement
```

This does not promote production recommendation enums or prove methodological-context recommendation value. Specification 019 remains historical `FAIL` evidence and is not rescored.

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

The launcher receives no provider credential. A provider-backed experiment may be authorized only after its own contract is frozen and its exact implementation/live-capable source is provider-free green.

Specification 019 and Specification 020 both exercised the accepted launcher path for exactly one frozen provider-backed run each. Specification 020 one-shot authorization and temporary live/control helpers are retired from `main`; audit issues remain in GitHub history.

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
routing/current-state drift           YES, observed repeatedly
```

Checkpoint 172 records the first green bounded hardening:

```text
docs/current_routing.json
    routing metadata only

scripts/check_current_routing.py
    validates manifest shape, checkpoint existence, and key human-facing pointers

.github/workflows/current-routing-consistency.yml
    cross-platform validation on routing-sensitive pushes and pull requests
```

Final exact PR #54 head `44d92d73029ad56925bd2c49bb373be5bdef44ce` passed checkpoint metadata, routing consistency on Ubuntu and Windows, and all applicable accepted V1 regression seams before merge into `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`.

Markdown remains the substantive source of truth. The manifest is not a replacement for canonical documents, foundations, specifications, checkpoints, results, or Git history. Development Method remains v0.4 because its existing partial-automation rule already covers this bounded hardening.

---

## Current exact continuation

```text
A. preserve Checkpoint 190 as the exact live-capable Specification 022 source boundary
B. keep `v1-spec022-methodological-navigation-coverage-live-source` fixed at `cf5893d74fefa699296842b0a48326a9cb50161c`
C. validate one clean post-reconciliation Checkpoint 190 head across Specification 022 and inherited V1 regressions
D. stop before creating a registry authorization at this boundary
E. any later provider execution requires separate one-shot Specification-018 authorization plus an owner launch request
F. preserve raw artifact bytes unchanged before live scientific interpretation
G. do not modify or rescore Specifications 015-021
```

The live-capable engineering question is closed at Checkpoint 190. The next scientific question remains Specification 022 itself, which is still unexecuted. Provider execution is a separate governed boundary rather than an automatic consequence of freezing the source.

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
169  Specification 020 exact pre-live boundary frozen
170  Specification 020 exact live-capable source frozen
171  Specification 020 live diagnostic completed; BLOCKING_BOUNDARY_SUPPORTED
172  machine-checkable current-routing consistency guard passed and promoted through PR #54
183  supplied-action disposition calibration separated explicitly from open-world methodological navigation / coverage
186  Question A methodological-navigation architecture/evaluation review completed and promoted through PR #67
187  first project-state methodological coverage diagnostic design choices resolved
188  Specification 022 exact scientific contract and fixtures frozen before implementation
189  Specification 022 provider-free implementation gate passed cross-platform; no provider call authorized
190  Specification 022 exact live-capable source frozen; no provider authorization or call
```

## Specification 021 preservation and interpretation route

```text
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
    frozen supplied-action experiment contract

docs/research/029_dependency_backed_recommendation_value_design.md
    prospective experiment rationale

docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
    architectural interpretation guardrail after the result

docs/checkpoints/182_specification_021_complete_live_result_failed.md
    frozen complete scientific FAIL boundary

docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
    Question A vs downstream disposition-calibration clarification

docs/checkpoints/184_specification_021_negative_result_preservation_promotion_candidate.md
    preservation-only promotion boundary

experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
    stable interpreted result

experiments/dependency_backed_recommendation_action_value/results/
    immutable first incomplete and complete replacement raw evidence
```

The failed experiment implementation remains historical on PR #55 and is intentionally absent from the preservation branch.
