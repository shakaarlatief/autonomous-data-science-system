# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-22

## Purpose

This file records only changes that materially alter how the project is understood, built, evaluated, preserved, or continued. It is not a commit changelog.

---

## 2026-08-07: Dedicated project and layered repository preservation established

The Autonomous Data Science System became a dedicated repository separate from individual data projects.

The initial preservation model distinguished:

```text
chat as exploratory workspace
repository as durable source of truth
canonical documents
foundational design memos
checkpoints
historical provenance
```

This established:

> The chat is where we think. The repository is where the system remembers.

Key sources:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/DECISIONS.md, D-001 through D-010
```

---

## 2026-08-08: Checkpointing and chat rotation became proactive AI responsibilities

Development Method v0.2 made the AI design collaborator responsible for detecting natural preservation checkpoints and recommending session rotation when continuity risk becomes material.

Key sources:

```text
docs/DECISIONS.md, D-018 and D-020
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

---

## 2026-08-08 to 2026-08-09: Core system theory expanded into dedicated foundations

The project moved from a broad vision to explicit theories for epistemic integrity, admissibility/risk, project state and revision, project initialization, knowledge activation, reusable knowledge, knowledge quality/evolution, and behavioral system evaluation.

Key sources:

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
docs/foundations/005_project_initialization_and_universal_bootstrap.md
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
```

---

## 2026-08-09: Prototype V0 became a preregistered falsification experiment

The project chose to test a bounded explicit semantic architecture against strong simpler controls before building a large autonomous platform.

```text
B0: strong LLM + strong generic workflow
B1: B0 + same methodological knowledge supplied statically
P0: same model + typed state + activation + safeguards + dependency repair
    + state-driven action selection
```

The benchmark bundles, run order, model/provider configuration, budgets, replacement policy, semantic rubric, blinded judging procedure, and falsification criteria were frozen before P0 implementation.

Key sources:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

---

## 2026-08-18: System-level LLM/system/human boundary became durable architecture

The project distinguished human-executed data science, interactive LLM-assisted data science, and system-mediated data science.

The LLM became explicitly one reasoning component inside ADS. Every explicit mechanism must justify its complexity empirically.

Key source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## 2026-08-18: Development preservation gained routing, promotion audits, and reconciliation

Development Method v0.3 introduced:

```text
checkpoint promotion audits
KNOWLEDGE_MAP routing
periodic reconciliation
authority/maturity conventions
MAJOR_CHANGES structural history
separation of CURRENT_STATE from detailed experiment ledgers
```

Git + Markdown remains the development-preservation substrate until observed retrieval, dependency, consistency, concurrency, or automation problems justify more complex infrastructure.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
```

---

## 2026-08-18 to 2026-08-19: Prototype V0 gained validated supervision and observability separation

Held-out execution gained a condition-neutral runner/verifier/supervisor architecture and mechanically validated prospective automation.

A reusable execution principle emerged:

```text
execution / reasoning
    -> persisted state/events
    -> read-only observability
    -> human interface
```

Key sources:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/foundations/016_execution_observability_separation.md
docs/PRINCIPLES.md, P-022
```

---

## 2026-08-19: Prototype V0 strongly falsified the current P0 design

Final pooled evidence:

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
```

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

The architectural consequence was simplification, not abandonment of the wider system vision.

The strongest scaling lesson became:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not carry forward unchanged full typed state on every call, large always-on context/frontiers, generic recursive support reassessment, narrow path-sensitive trigger activation, or universal dependency reopening machinery.

Key sources:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

---

## 2026-08-19: Post-V0 product vision became a professional interactive data-science operating environment

The project returned to the broader product goal before selecting another orchestration architecture.

The target became a professional environment in which ADS carries much of the methodological-navigation and project-memory burden while the human can inspect, discuss, select, override, guide, and approve work interactively.

Key source:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

---

## 2026-08-19: Product object model and professional developer workflow were concretized

The central separation became:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

with durable distinctions including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
workspace section != fundamental object
```

ADS should complement VS Code rather than replace it, and generated project code should remain independently runnable and professionally maintainable.

Key source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## 2026-08-19 to 2026-08-20: Methodological navigation became a bounded-horizon architecture

The methodological brain adopted:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The **MethodologicalHorizon** separates a large global knowledge universe from the bounded project-specific slice plausibly relevant to current reasoning.

Reusable knowledge gained a promoted representation around:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
ExecutionCapability
```

Key sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## 2026-08-20: V1 persistence/retrieval architecture and implementation tooling were selected empirically

The project accepted:

```text
D-028
SQLite-centered local-first operational architecture
FTS5 lexical retrieval seam
rebuildable embeddings / initial exact semantic retrieval
application rule evaluation
selective LLM context assembly

D-029
SQLAlchemy Core 2.0 + Alembic 1.x

D-030
pyproject.toml + uv + committed uv.lock + uv_build
```

The first production persistence slice passed SQLite/Linux, SQLite/Windows, and PostgreSQL 18, including exact historical project-to-knowledge revision pinning.

Key sources:

```text
docs/DECISIONS.md, D-028 through D-030
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
```

---

## 2026-08-20: Reusable knowledge gained an accepted deterministic interchange contract

D-031 and Specification 004 established:

```text
JSON
+ JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic normalization/serialization
```

Candidate/benchmark import cannot silently create accepted methodological authority.

The heterogeneous benchmark corpus passed its frozen interchange gate across Linux/Windows and multiple Python versions. A richer governed import/accept/export round-trip then became a separate cross-backend closure gate.

Key sources:

```text
docs/DECISIONS.md, D-031
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
```

---

## 2026-08-20: Agentic ecosystem audit separated ADS semantics from replaceable runtime infrastructure

The audit established the durable split:

```text
ADS owns
    project semantics
    methodological semantics
    governance
    provenance
    Questions / Findings / Decisions
    methodological-horizon meaning

Replaceable infrastructure includes
    agent runtimes
    runtime checkpointing
    MCP
    AG-UI adapters
    A2A when independently deployed agents are real
```

This produced P-027 through P-029 and Specification 005.

---

## 2026-08-20: Professional frontend became an early parallel V1 product track

Foundation 021 made the interface a first-class reasoning, control, and quality surface.

React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest became the leading implementation hypothesis while final frontend and chart-stack promotion remained empirical questions.

---

## 2026-08-20: Project Cockpit became the strongly preferred primary active-work interface

Human review exposed a missing product layer: ADS needed a primary place where the user actively works with the evolving data-science process, not only pages that inspect it.

Research 002 introduced the Project Cockpit as:

```text
living project-process map
+ native system interaction
+ focused analytical work surface
```

Direct project views remained alternative entry/inspection paths rather than mandatory escape hatches.

---

## 2026-08-20: Unexpected Session 02 boundary validated preservation but exposed routing drift

Session 02 reached the platform conversation-length limit after substantive Cockpit work had been preserved but before final routing reconciliation.

Session 03 reconstructed the state from repository authority and repaired stale current routing through Checkpoint 120.

The incident demonstrated:

```text
checkpoint/specification preservation protects substantive knowledge
    and
current routing/reconciliation remains necessary for reliable continuation
```

Key source:

```text
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```

---

## 2026-08-20 to 2026-08-21: Cockpit evolved into a scalable spatial operating surface

Successive human reviews and bounded implementation gates established:

```text
large two-dimensional project extent
horizontal + vertical navigation
true fullscreen
geometric zoom + fit/reset/recovery
native trackpad pan/pinch capability
scalable Jump/search
canvas-dominant floating composer/controls
compact fold-away primary HUD
FiniteNavigableGridWorld != SemanticProjectPlane
viewport-aware semantic stage orientation
world-owned restrained ambient depth
collision-safe floating surfaces
```

The seventh real-browser review accepted the core interaction architecture. A reproducible rapid-zoom stage-ruler timing defect was found and repaired before promotion.

---

## 2026-08-21: Project Cockpit interaction architecture was promoted

Checkpoint 126 closed the bounded Specification 007 interaction spike after seven real-browser human review cycles.

The promoted V1 interaction contract became:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promotion deliberately left final canvas/gesture libraries, auto-layout, semantic zoom/grouping, minimap, final stage taxonomy, final chrome styling, final URL contract, frontend stack promotion, and visual identity open.

A later bounded normal-window Jump/composer and pinch-sensitivity repair passed automated and human retesting through Checkpoint 130 and was accepted as good enough to continue.

Key sources:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

## 2026-08-21: Governed reusable-knowledge round-trip closed across SQLite and PostgreSQL

The richer governed reusable-knowledge persistence/interchange seam was validated on:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

Final closure gate:

```text
V1 governed knowledge roundtrip closure gate
run 32496856945
```

The gate validates candidate import, explicit acceptance, accepted-current pointers, deterministic trusted accepted-snapshot export/reload, provenance, relation governance, collections, migration compatibility, and historical project revision pinning across later knowledge acceptance.

Two PostgreSQL portability defects were discovered and repaired, including an overlong Alembic revision identity. A permanent regression guard now requires unique Alembic revision IDs no longer than 32 characters.

Checkpoint 127 closes the current governed persistence/interchange seam.

Key sources:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

---

## 2026-08-22: Initial V1 reasoning runtime selected after executable three-way bakeoff

Specification 005 compared:

```text
ADS-owned direct model calls
OpenAI Agents SDK 0.19.4
LangGraph 1.2.10
```

All candidates were tested as real ADS-shaped runtime paths rather than resolved from framework feature lists.

D-032 accepts:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

The decision preserves:

```text
ADS owns
    project and methodological semantics
    context construction and exact revision provenance
    human-control policy
    authoritative idempotency/domain events
    stable RuntimeTrace/provenance

runtime owns
    replaceable execution mechanics
```

Direct model calls remain the fallback/reference path. LangGraph remains a future escalation path if materially stronger workflow durability becomes necessary. No final LLM provider/model or multi-agent architecture is selected.

Key sources:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

---

## 2026-08-22: First production methodological-knowledge lexical retrieval channel passed

Research 016 and Specification 009 froze the retrieval/Horizon benchmark before implementation and separated:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval diagnostics
RH-R    relational horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

The first production slice implemented a storage-neutral retrieval port over a rebuildable SQLite FTS5 accepted-current projection.

Observed quality:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-L critical omissions  0 / 10
RH-S diagnostic Recall@3 0.75
```

The lexical miss on semantic paraphrase `class-imbalance` was preserved as a measured target instead of being patched after observation.

Key sources:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```

---

## 2026-08-22: Dense semantic retrieval demonstrated complementary signal, not replacement

Specification 010 tested FastEmbed 0.8.0 with `BAAI/bge-small-en-v1.5` as an experiment-only exact dense comparator over the unchanged ten-asset accepted-current corpus.

Observed:

```text
RH-L Recall@3  1.00
RH-L MRR       1.00
RH-S Recall@3  0.75
RH-S MRR       0.75
```

Dense retrieval recovered the lexical `class-imbalance` miss at rank 1 but displaced lexical `ecdf` from the semantic top three.

Conclusion:

```text
dense-only does not replace lexical retrieval
```

The complementary failure pattern, rather than a generic preference for embeddings, justified one bounded fusion comparator.

Key sources:

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
```

---

## 2026-08-22: Bounded hybrid retrieval preserved both measured semantic signals

Specification 011 preregistered equal-weight Reciprocal Rank Fusion over the unchanged lexical and dense top-three rankings.

Workflow `32561118325` passed on Ubuntu and Windows:

```text
RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S critical omissions  0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

`class-imbalance` survives through dense retrieval and `ecdf` survives through lexical retrieval.

This makes hybrid lexical + exact semantic retrieval the leading current hypothesis for the frozen benchmark, while deliberately not selecting FastEmbed, BGE, RRF `k=60`, embedding persistence, ANN, or a vector database as permanent production architecture.

Key sources:

```text
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

---

## 2026-08-22: First production-facing explained MethodologicalHorizon passed

Specification 012 v1.0 / Checkpoint 141 validate the first production-facing Horizon seam:

```text
stable/revision-transparent direct candidates
    -> accepted-current KnowledgeNavigationRepository reads
    -> outbound one-hop accepted relation expansion
    -> deterministic TRUE / FALSE / UNKNOWN applicability evaluation
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained included/excluded MethodologicalHorizon
```

Cross-platform result:

```text
workflow 32561727632
Ubuntu PASS
Windows PASS
RH-R relation cases       4 / 4 PASS
RH-A applicability cases  5 / 5 PASS
authoritative knowledge   unchanged
```

The key executable semantic invariant is:

```text
unknown != false
```

PR #10 containing the dense-complementarity, hybrid-fusion, and first-Horizon progression was merged into `v1-frontend-spike` at:

```text
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

Key sources:

```text
docs/research/019_first_methodological_horizon_application_seam.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
```

---

## 2026-08-22: First selective MethodologicalContextPack gate validated the system/model context boundary

Research 020 and Specification 013 v0.1 froze the first RH-C gate before selector/context implementation.

The tested minimum-complexity hypothesis was:

```text
explicit task reasoning functions
    -> primary Horizon matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current compact reasoning projection
    -> MethodologicalContextPack
```

A deliberately wide ten-asset Horizon was used so context selection could not pass trivially by starting from only relevant assets.

Observed cross-platform result:

```text
Ubuntu   PASS
Windows  PASS
full suite 42 passed, 2 skipped on each OS
```

Per-case context ratios:

```text
RH-C01 MODEL_OPTION         2 / 10 selected   ratio 0.20020477
RH-C02 EVIDENCE_OPTION      2 / 10 selected   ratio 0.16462054
RH-C03 VALIDITY_CONSTRAINT  3 / 10 selected   ratio 0.34635417
RH-C04 DECISION_FRAMEWORK   2 / 10 selected   ratio 0.28222057
```

Equivalent canonical-context reduction was approximately:

```text
65% to 84%
```

Across all cases:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected assets         0
selected assets                    <= 3
unexplained omissions              0
```

The gate also validated stale-revision fail-closed reads, explicit `BUDGET_LIMIT`, full-content materialization only after budget selection, deterministic canonical serialization, identical cross-platform digests, preservation of `MISSING_CONTEXT`, and omission of retrieval metadata from the model-facing pack.

The most important architecture is the separation:

```text
SYSTEM
    retains the wider Horizon
    retains selection and omission decisions

MODEL-FACING PACK
    contains selected exact methodological revisions only
```

Checkpoint 143 promotes Specification 013 to accepted bounded v1.0.

This does not establish that reasoning functions solve general semantic relevance, that `max_assets = 3` is a universal budget, or that selective context improves actual LLM reasoning.

Key sources:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

---

## 2026-08-22: The next methodological boundary moved from context mechanics to real reasoning value

After the RH-C pass, the project explicitly stopped treating more retrieval or selector tuning as the next justified step.

The next experiment should be preregistered before model calls and compare:

```text
same frozen project/task evidence
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> one concrete model configuration

versus

same frozen project/task evidence
    -> strong full-Horizon/simple context control
    -> same ReasoningRuntime
    -> same concrete model configuration
```

The target evidence is now:

```text
reasoning quality against frozen obligations
critical methodological omissions
exact supplied knowledge revisions
exact provider/model tokens
latency and cost where observable
whether selective omission creates real quality loss
whether full-Horizon context creates distraction or unnecessary cost
```

This is the first experiment that can establish whether the mechanically demonstrated context compression earns value at the actual reasoning layer.

Key sources:

```text
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
docs/CURRENT_STATE.md
```
