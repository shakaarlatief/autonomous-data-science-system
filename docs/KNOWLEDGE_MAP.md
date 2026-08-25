# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 198  
**Active development branch:** `v1-source-vault-bootstrap`  
**Active PR:** #75  
**Promoted V1 integration branch:** `v1-frontend-spike` at `8215718db3e44f000cc6ed53d6a051522d429dbd`

## Start here

```text
README.md                         project overview and current stage
docs/CURRENT_STATE.md             exact present state and continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable routing metadata only
docs/VISION.md                    high-level product/system direction
docs/PRINCIPLES.md                accepted high-level design principles
docs/DECISIONS.md                 accepted project-level decisions
docs/OPEN_QUESTIONS.md            unresolved questions
docs/DEVELOPMENT_METHOD.md        development/preservation method
docs/CONTINUITY.md                cross-session continuation procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current branch relationship:

```text
promoted integration          v1-frontend-spike @ 8215718db3e44f000cc6ed53d6a051522d429dbd
active deployment branch      v1-source-vault-bootstrap
active PR                     #75
current checkpoint            198
```

---

# Current stage: permanent Source Universe deployment before Course 2

Primary route:

```text
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/checkpoints/195_specification_023_source_substrate_contract_frozen.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/checkpoints/197_source_substrate_canonical_reconciliation_and_promotion_candidate.md
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```

Foundation 022 is the canonical numbering of the source-universe foundation. The original draft was numbered Foundation 021 before a collision with the already existing professional product/interface Foundation 021 was detected during promotion reconciliation. The renumbering changes no source-architecture semantics.

Central separation:

```text
SOURCE UNIVERSE
    !=
METHODOLOGICAL KNOWLEDGE UNIVERSE
```

Accepted source identities and provenance concepts:

```text
SourceRecord
SourceArtifact
SourceCollection
SourceCollectionMembership
SourceLocator
SourceIngestionEvent
DerivedSourceArtifact
```

Accepted source path:

```text
filesystem input
    -> exact SHA-256 + byte count
    -> immutable content-addressed SourceArtifactStore
    -> relational Source Registry
    -> deterministic private/public-safe exports
    -> integrity audit
    -> verified backup
    -> clean restore
```

Specification 023 result:

```text
SU-G01 through SU-G23   PASS
SOURCE_SUBSTRATE_ACCEPTED
```

The accepted implementation is provider-free for source-integrity correctness and is now promoted into `v1-frontend-spike` at `8215718db3e44f000cc6ed53d6a051522d429dbd`.

Important boundary:

```text
accepted + promoted implementation
    !=
permanent user-controlled vault already instantiated
```

The active operational task is to instantiate the accepted substrate on durable user-controlled storage, ingest the original local VU Machine Learning folder, create an independent backup, and prove clean restoration before Course 2 is admitted.

---

## Permanent source-vault bootstrap route

Operational checkpoint:

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
```

Operational runbook:

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

Required private locations:

```text
ORIGINAL_SOURCE_ROOT
SOURCE_REGISTRY_DATABASE
SOURCE_VAULT_ROOT
INDEPENDENT_BACKUP_ROOT
CLEAN_RESTORE_ROOT
```

The project must not invent these paths or commit them to Git. The original course folder remains read-only input from ADS's perspective.

Course 2 remains blocked until the permanent deployment has completed compare, reviewed ingestion, clean audit, independent verified backup, clean restore, and restored audit.

---

## First source-corpus route

Diagnostic pre-substrate fingerprint snapshot:

```text
docs/source_universe/intake_snapshots/001_vu_machine_learning_chat_intake.md
```

Reviewed intake manifest:

```text
docs/source_universe/manifests/001_vu_machine_learning.json
```

Validation result:

```text
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```

Observed first-corpus evidence:

```text
20 / 20 files matched prospective fingerprints
20 NEW_ARTIFACT initial ingests
14 EXACT_DUPLICATE real re-encounters
20 logical sources
20 exact artifacts
20 stored binary objects
34 ingestion events
20 / 20 clean pre-backup audit
20 / 20 clean restored audit
```

The source binaries, private observed paths, private registry snapshots, and backup payload were not committed to Git.

---

# Methodological knowledge-universe construction

Primary route:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

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

Coverage depth is not truth, maturity, source quality, freshness, or enforcement authority.

The first six deep slices remain:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

The source-universe operationalization step precedes broad source-backed authoring so exact evidence identity and recovery do not depend on ChatGPT history.

---

# Reusable methodological knowledge architecture

Primary conceptual sources:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```

Current representation direction:

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
asset != component != narrative facet
static relation != conditional rule
retrieval cue != applicability != required context != project relevance
methodological knowledge != source artifact
methodological knowledge != execution implementation
coverage depth != epistemic maturity
```

Serious content is allowed to expose representation defects before broad catalog scale makes revision expensive.

---

# Product and project-object architecture

Primary sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Core object distinction:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Project Cockpit route:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

# Persistence, interchange, runtime, and source storage

Accepted V1 decisions:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime
D-033  ADS-owned Source Universe substrate with private artifact store + relational registry
```

The operational database, interchange representations, source artifact store, and rebuildable indexes remain different authority layers.

---

# Retrieval -> Horizon -> selective context -> reasoning

```text
Specification 009 / Checkpoint 135   lexical retrieval baseline
Specification 010 / Checkpoint 137   dense complementarity
Specification 011 / Checkpoint 139   bounded hybrid comparator
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

Specification 014 preserved equal measured quality on its bounded benchmark while reducing provider input by 66.56%. Navigation is not being tuned further until the methodological universe becomes materially larger.

---

# Recommendation/action and methodological-navigation evidence

The downstream diagnostic chain remains historically bounded:

```text
Specification 015  FAIL
Specification 016  dependency-backed DEFER-vs-NOT_NOW construct supported
Specification 017  INCOMPLETE
Specification 019  FAIL after provenance repair
Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED construct supported
Specification 021  FAIL
Specification 022  INCOMPLETE / EXECUTION INTEGRITY FAILED
```

Important interpretation:

```text
supplied-action disposition calibration
    !=
open-world methodological navigation / coverage
```

Specification 022 has no legitimate `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` scientific comparison because all planned reasoner observations failed the frozen structured-output contract before judge execution.

Primary transition route:

```text
docs/checkpoints/191_specification_022_live_execution_incomplete_knowledge_universe_next.md
docs/checkpoints/192_specification_022_incomplete_result_preservation_promotion_candidate.md
docs/research/033_methodological_knowledge_universe_construction_framework.md
```

---

# Preservation and continuity

Primary sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
```

Repository artifacts, exact Git history, checkpoints, and canonical routing remain the continuation authority. Chat history and external file-management surfaces do not replace them.

---

# Exact current continuation

```text
A. identify the original local VU Machine Learning folder
B. choose permanent Source Registry and Source Vault locations outside public Git
C. choose a genuinely independent backup destination
D. choose a temporary clean-restore target
E. verify capacity and location separation
F. compare the original folder against the prospectively frozen manifest/fingerprints before ingestion
G. preserve and review every MATCH / DIFFERENT_ARTIFACT / MISSING_LOCAL_SOURCE / ADDITIONAL_LOCAL_SOURCE result
H. ingest the reviewed intended corpus
I. run the working-store integrity audit
J. create and verify the independent backup
K. clean-restore and run the restored integrity audit
L. preserve only safe deployment evidence and classify the bootstrap
M. only then admit Course 2 and continue course-sized corpus intake
N. map the resulting source universe against the coverage map
O. resume the six deep methodological representation pressure tests
P. revise knowledge representation only when content pressure warrants it
Q. do not rerun or rescore Specifications 015-022 as part of this source transition
```
