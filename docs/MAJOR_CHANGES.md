# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-25

## Purpose

This file records only changes that materially alter how the project is understood, built, evaluated, preserved, or continued. It is not a commit changelog.

---

## 2026-08-07 to 2026-08-08: Dedicated project and durable preservation method established

The Autonomous Data Science System became a dedicated repository separate from individual data projects. Chat remained the design workspace while Git became the durable source of truth. The project introduced layered preservation, foundations, checkpoints, explicit decisions, proactive checkpointing, and a continuity procedure for new chats.

Core maxim:

> The chat is where we think. The repository is where the system remembers.

Key sources:

```text
docs/DECISIONS.md, D-001 through D-020
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

---

## 2026-08-08 to 2026-08-09: Core system theory became explicit foundations

The project developed dedicated foundations for epistemic integrity, admissibility/risk, project state, initialization, knowledge activation, reusable knowledge, knowledge quality/evolution, and behavioral system evaluation.

Key route:

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

## 2026-08-09 to 2026-08-19: Prototype V0 became a preregistered falsification program and then strongly failed

The project tested an explicit semantic/orchestration architecture against strong simpler controls before building a large platform. The benchmark and falsification criteria were frozen prospectively.

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

The broader ADS vision survived, but the original always-on orchestration machinery did not earn its complexity. The strongest scaling lesson became:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Key sources:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

---

## 2026-08-18: Preservation gained routing, promotion audits, and reconciliation

Development Method v0.3 added explicit promotion audits, `KNOWLEDGE_MAP`, periodic reconciliation, a selective `MAJOR_CHANGES` ledger, and clearer separation between concise current state and detailed historical evidence.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
```

---

## 2026-08-19 to 2026-08-21: ADS product/object model and Project Cockpit became concrete

The target became a professional interactive data-science operating environment in which ADS carries much of the project-memory and methodological-navigation burden while the human can inspect, discuss, select, override, guide, and approve work.

The project object model adopted:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

with durable distinctions such as `Investigation != Run`, `Evidence != Finding`, `Finding != Claim`, and `Claim != Decision`.

Repeated bounded frontend/human-review cycles promoted the Project Cockpit interaction architecture.

Key sources:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
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

The `MethodologicalHorizon` separates the large global methodological universe from the bounded project-specific slice plausibly relevant to current reasoning. Reusable methodological knowledge gained explicit assets, components, narrative facets, relations, conditional rules, collections, exact revisions, and provenance.

Key sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## 2026-08-20 to 2026-08-22: V1 local-first persistence, tooling, interchange, and reasoning runtime became operational

The project accepted:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  deterministic JSON + JSON Schema knowledge interchange with governance
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime
```

The governed reusable-knowledge round-trip closed across SQLite/Linux, SQLite/Windows, and PostgreSQL 18. Runtime-framework authority remained below ADS-owned domain/application boundaries.

---

## 2026-08-22 to 2026-08-23: Retrieval, MethodologicalHorizon, and selective context were validated as bounded seams

The bounded path progressed through lexical retrieval, dense complementarity, hybrid comparison, explained Horizon construction, selective exact-revision context, and real reasoning.

Specification 014 observed equal measured reasoning quality between selective and full-Horizon conditions on its frozen benchmark while reducing provider input by 66.56%.

This supports selective context economy. It does not select the final navigation strategy for a serious knowledge universe.

Key route:

```text
Specification 009 / Checkpoint 135   lexical retrieval
Specification 010 / Checkpoint 137   dense complementarity
Specification 011 / Checkpoint 139   hybrid comparator
Specification 012 / Checkpoint 141   explained MethodologicalHorizon
Specification 013 / Checkpoint 143   selective exact-revision context
Specification 014 / Checkpoint 146   real reasoning-context value
```

---

## 2026-08-23 to 2026-08-25: Recommendation/action experiments exposed bounded calibration and instrumentation failures

The downstream recommendation/action program produced a deliberately mixed evidence chain:

```text
Specification 015  FAIL
Specification 016  dependency-backed DEFER-vs-NOT_NOW construct supported
Specification 017  INCOMPLETE
Specification 019  FAIL after system-owned provenance repair
Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED construct supported
Specification 021  FAIL
```

A central architectural distinction emerged:

```text
supplied-action disposition calibration
    !=
open-world methodological navigation / coverage
```

Failed/incomplete implementations were not promoted merely because they ran. Their contracts and evidence were preserved separately.

---

## 2026-08-23: Governed autonomous live-experiment launcher was promoted

Specification 018 established a bounded repository-governed launch path for explicitly authorized frozen experiments. The launcher owns mechanical authorization checks without receiving provider credentials or allowing issue text to define arbitrary executable configuration.

Checkpoint 161 classified the bounded outcome:

```text
GOVERNED_LAUNCHER_SUPPORTED
```

---

## 2026-08-25: Specification 022 ended incomplete and shifted project emphasis to the serious methodological universe

Specification 022 moved evaluation upstream to evolving project state and methodological path coverage. Its live workflow completed operationally but all 108 planned reasoner observations failed the frozen structured-output contract after allowed retries, so no judge comparison was scientifically reachable.

Frozen classification:

```text
INCOMPLETE / EXECUTION INTEGRITY FAILED
```

No legitimate `GENERIC`, `ADS_HORIZON`, or `ORACLE_HORIZON` comparison exists from that run.

Checkpoint 191 changed the immediate program from another small mechanism experiment to building the serious governed methodological substrate ADS ultimately requires.

The incomplete experiment implementation was not promoted. Durable evidence was preserved through a preservation-only integration.

---

## 2026-08-25: Serious methodological knowledge-universe construction framework was frozen

Research 033 and Checkpoint 193 established a broad coverage map, proposition-sensitive source policy, layered knowledge QA, explicit construction-depth ladder, and six heterogeneous deep pressure-test slices:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

The knowledge representation is explicitly allowed to change if serious content exposes real deficiencies.

---

## 2026-08-25: Source Universe became a first-class ADS subsystem

Bulk educational-source intake was paused when it became clear that ChatGPT Library or Project Sources should not become the long-term source architecture.

Research 034 and the source/evidence foundation established:

```text
SOURCE UNIVERSE
    !=
METHODOLOGICAL KNOWLEDGE UNIVERSE
```

The source foundation was initially drafted as Foundation 021, but promotion reconciliation detected that Foundation 021 was already occupied by the professional product/interface foundation. The source foundation was therefore canonically renumbered Foundation 022 without semantic change.

The accepted architecture separates logical source identity, exact artifact identity, collections and uncertain membership, locators, ingestion events, derived lineage, rights/access, and later fine-grained evidence provenance.

Key sources:

```text
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

---

## 2026-08-25: Specification 023 source substrate passed provider-free first-corpus acceptance

Specification 023 implemented:

```text
filesystem intake
    -> exact SHA-256 + staging
    -> immutable content-addressed SourceArtifactStore
    -> relational Source Registry
    -> deterministic PRIVATE_SNAPSHOT / PUBLIC_SAFE_CATALOG
    -> integrity audit
    -> verified backup
    -> clean restore
```

The implementation passed on Ubuntu and Windows and retained all inherited V1 regressions.

The first controlled VU Amsterdam Machine Learning corpus produced:

```text
20 / 20 prospective fingerprint matches
20 NEW_ARTIFACT ingests
14 EXACT_DUPLICATE real re-encounters
20 logical sources
20 exact artifacts
20 stored objects
34 ingestion events
20 / 20 clean working-store audit
20 / 20 clean restored audit
SU-G01 through SU-G23 PASS
```

Classification:

```text
SOURCE_SUBSTRATE_ACCEPTED
```

No source PDF, private observed path, private registry snapshot, or backup payload entered public Git.

D-033 now accepts the ADS-owned source-substrate architecture and supersedes D-015 only in its original architectural-uncertainty scope.

Important remaining boundary:

```text
accepted source-substrate architecture / implementation
    !=
permanent user-controlled source vault already instantiated
```

The next operational step is to deploy the accepted source store and registry on durable user-controlled storage, ingest the original local Machine Learning folder, establish an independent backup, and prove clean recovery before Course 2 is admitted.

Key sources:

```text
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/checkpoints/197_source_substrate_canonical_reconciliation_and_promotion_candidate.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```
