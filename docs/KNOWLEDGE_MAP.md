# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-24  
**Current checkpoint:** 177  
**Active development branch:** `v1-dependency-backed-recommendation-value`  
**Active PR:** #55 draft, Specification 021 exact live-capable source frozen; one governed authorization next  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`  
**Latest experiment:** Specification 021 `LIVE_SOURCE_FROZEN`

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
promoted integration merge     a639cfc570290a2169425f43078bbb242fa398e9
routing closure checkpoint     8f29894667467e6ef58a02eb8f5d580c895968e6
active branch                  v1-dependency-backed-recommendation-value
active PR                      #55 draft
Specification 015 PR           #13 closed without merge; preservation #14 merged
Specification 016 PR           #15 merged
Specification 017 PR           #16 closed without merge; preservation #22 merged
Specification 018 PR           #23 merged
Specification 019 PR           #33 closed without merge
Specification 019 preservation #43 merged
Specification 020 PR           #44 merged
routing consistency PR         #54 merged
Specification 021 PR           #55 active
Spec021 live-source ref        v1-spec021-dependency-backed-recommendation-value-live-source
main                           governed live-launch control plane; no Spec021 authorization yet
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
    RECOMMENDED-vs-BLOCKING_REQUIRED contract frozen, provider-free and live boundaries validated, governed live run completed, BLOCKING_BOUNDARY_SUPPORTED preserved and promoted

Checkpoints 172-173 / PR #54
    narrow machine-readable routing pointers + cross-platform contradiction guard accepted, promoted, and closed

Specification 021 / Checkpoints 174-177 / PR #55
    dependency-backed recommendation-value contract frozen prospectively;
    provider-free implementation green cross-platform;
    fully reconciled exact pre-live boundary frozen;
    exact provider-capable source b589bad975880b2d3cccc3596fc82539b1b96577 pinned to dedicated live-source ref;
    no provider call authorized yet
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

Navigation sequence:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Research 028 is forward research only. It records the distinction that the system owns persistent project state, methodological navigation determines what matters from that state, and the broad knowledge base should be a governed revisioned methodological universe rather than an undifferentiated RAG corpus.

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

The result supports selective context economy on the bounded benchmark. It does not establish downstream recommendation value.

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

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
```

Frozen result:

```text
reasoner outputs                     36 / 36
aggregate exact disposition accuracy 1.000000
joint blocking-pointer accuracy      1.000000
RECOMMENDED null-pointer correctness 1.000000
outcome                              BLOCKING_BOUNDARY_SUPPORTED
```

Accepted bounded construction:

```text
exact unresolved requirement
+ exact active defended downstream scope
+ explicit scope DEPENDS_ON requirement relation
+ candidate action RESOLVES requirement
```

This does not promote production recommendation enums or prove methodological-context recommendation value.

### Specification 021, exact live source frozen

Primary sources:

```text
docs/research/029_dependency_backed_recommendation_value_design.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
docs/checkpoints/174_specification_021_dependency_backed_recommendation_value_contract_frozen.md
docs/checkpoints/175_specification_021_provider_free_implementation_gate_cross_platform_passed.md
docs/checkpoints/176_specification_021_pre_live_boundary_frozen.md
docs/checkpoints/177_specification_021_live_source_frozen.md
```

Current status:

```text
LIVE_SOURCE_FROZEN
```

The frozen design keeps GENERIC / SELECTIVE / FULL_HORIZON and the same ten-asset methodological universe, while making the known disposition relations explicit and system-owned:

```text
BLOCKING_REQUIRED
    scope DEPENDS_ON unresolved requirement
    action RESOLVES requirement

DEFER
    action WAITS_FOR unresolved trigger
```

The model returns action-local pointers only among supplied identities. Exact methodological provenance remains system-owned.

Frozen cases:

```text
DBRA-01 future validity and model sequence
DBRA-02 compact nonlinear model shortlist
DBRA-03 distribution evidence before transformation
DBRA-04 missingness / class-imbalance decision framework
```

Frozen complete outcomes:

```text
PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Exact live-source evidence:

```text
provider-free implementation head           8e199c29e3f082b353f92f27868aedca0ebbbf74
pre-live source                             aa830eda4fe80bc349afcb4f3bd0ab53f37bfcc7
live-capable source                         b589bad975880b2d3cccc3596fc82539b1b96577
live-source ref                             v1-spec021-dependency-backed-recommendation-value-live-source
Specification 021 provider-free CI          32724242554  success
Windows job                                 97421896915  success
Ubuntu job                                  97421897042  success
routing and inherited accepted-seam checks  all green on the exact live source
```

The first live-plumbing validation run `32724023671` exposed only that the implementation-stage "no live surface" invariant had to transition to a "no repository authorization" invariant after Checkpoint 176 permitted the live wrapper/workflow. The repair did not change frozen science.

No provider call is authorized by Checkpoint 177. The next governed step is one exact Specification 018 authorization and owner issue after the checkpointed routing head is validated.

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

Specification 021's frozen authorization values are recorded only in Checkpoint 177 until the exact routing head is green.

---

## Preservation and continuity

Primary sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/checkpoints/README.md
docs/checkpoints/172_machine_checkable_current_routing_consistency_guard_passed.md
docs/checkpoints/173_routing_consistency_hardening_promoted_and_closed.md
```

Accepted narrow hardening:

```text
docs/current_routing.json
scripts/check_current_routing.py
.github/workflows/current-routing-consistency.yml
```

Final closure evidence was push run `32719182489` on exact integration head `09670d5127c14cf3cece727b31823d5de4572211`, with Ubuntu and Windows successful.

Markdown remains the substantive source of truth. The routing manifest is not a replacement for canonical documents, foundations, specifications, checkpoints, results, or Git history.

---

## Current exact continuation

```text
A. validate the exact Checkpoint 177 routing reconciliation head
B. expose the identical frozen Specification 021 target workflow on main
C. add one exact enabled Specification 018 authorization on main
D. create one owner-authored [ADS LIVE] issue containing only the frozen launch ID and confirmation
E. verify launcher acceptance and exact target run identity
F. make no scientific interpretation from partial outputs
G. preserve the complete raw provider artifact before scientific interpretation
H. classify only with the frozen Specification 021 gates
I. retire the one-shot authorization/default-branch target exposure after preservation
J. do not modify or rescore Specifications 015-020
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
172  machine-checkable current-routing consistency guard passed; promotion candidate
173  routing-consistency hardening promoted and closed after final exact integration push validation
174  Specification 021 dependency-backed recommendation-value contract and benchmark frozen
175  Specification 021 provider-free implementation gate passed cross-platform
176  Specification 021 fully reconciled exact pre-live boundary frozen
177  Specification 021 exact live-capable source frozen and pinned; no provider call authorized
```
