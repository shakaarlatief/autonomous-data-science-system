# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 199  
**Active development branch:** `v1-multimodel-development-collaboration`  
**Active PR:** #76  
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
docs/DEVELOPMENT_METHOD.md        current accepted development/preservation method
docs/CONTINUITY.md                current accepted continuity procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current branch relationship:

```text
promoted integration             v1-frontend-spike @ 8215718db3e44f000cc6ed53d6a051522d429dbd
paused deployment branch         v1-source-vault-bootstrap @ d9437a8ca07a444400a5eb44ac2c89e8108c91c2
paused deployment PR             #75
active collaboration branch      v1-multimodel-development-collaboration
active collaboration PR          #76
current checkpoint               199
```

---

# Current stage: multi-model development collaboration architecture review

Primary route:

```text
docs/checkpoints/199_multi_model_collaboration_architecture_candidate_frozen_for_independent_review.md
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/model_collaboration/threads/MC-0001/THREAD.md
docs/model_collaboration/threads/MC-0001/messages/001_chatgpt_review_request.md
```

Optional live transport:

```text
GitHub Issue #77
MC-0001: ChatGPT-Claude collaboration architecture review exchange
```

Important authority distinction:

```text
Research 035
    candidate architecture

Model Collaboration Exchange
    collaboration provenance / review channel

Development Method / Continuity / checkpoint contract
    still current accepted method until explicit promotion
```

The project is deliberately not canonizing the ChatGPT-authored proposal before Claude has challenged the same problem independently.

## First cross-model trial: MC-0001

Review mode:

```text
INDEPENDENT_THEN_COMPARATIVE
```

Phase A:

```text
Claude reads neutral BRIEF + accepted governing method
Claude does not read Research 035 yet
Claude records its own preferred architecture first
```

Preferred Phase-A path:

```text
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
```

Phase B:

```text
Claude reads Research 035
Claude compares the architectures
Claude preserves convergence, disagreement, omissions,
complexity concerns, must-change items, and change-of-mind evidence
```

Preferred Phase-B path:

```text
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
```

Only after those are frozen should ChatGPT answer materially and the project decide whether a Development Method v0.5 is justified.

## Candidate collaboration direction under review

```text
repository remains project authority
one bounded task owner
serialized canonical writes
explicit per-task roles
reviewer does not silently become co-owner
independent-first review for high-impact questions
agreement and disagreement both require calibrated reasoning
material disagreement remains explicit
human remains project-intent/normative authority
dedicated model collaboration exchange
GitHub issues/PR comments optional as live transport
API orchestration deferred until measured need/value
```

No accepted multi-model project decision exists yet.

## Real Level-2 pressure already exposed

The current checkpoint contract requires ChatGPT-specific interaction provenance:

```text
Design session
ChatGPT project
Session title
```

The contract already says a different development environment should trigger deliberate revision rather than silent metadata drift.

If MC-0001 succeeds, likely promotion targets include:

```text
DEVELOPMENT_METHOD.md v0.5
CONTINUITY.md
checkpoints/README.md
checkpoint metadata validator
docs/model_collaboration/README.md
MAJOR_CHANGES.md
```

Exact provider-neutral provenance fields are intentionally not frozen before the trial.

---

# Source Universe: accepted substrate, permanent deployment paused

Primary accepted route:

```text
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/checkpoints/195_specification_023_source_substrate_contract_frozen.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/checkpoints/197_source_substrate_canonical_reconciliation_and_promotion_candidate.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```

Foundation 022 is the canonical numbering of the source-universe foundation. The original draft was numbered Foundation 021 before a collision with the existing professional product/interface Foundation 021 was detected during promotion reconciliation. The renumbering changes no source-architecture semantics.

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

The accepted implementation is promoted into `v1-frontend-spike` at `8215718db3e44f000cc6ed53d6a051522d429dbd`.

Important boundary:

```text
accepted + promoted implementation
    !=
permanent user-controlled vault already instantiated
```

---

## Paused permanent source-vault bootstrap route

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
branch  v1-source-vault-bootstrap
PR      #75
```

Required private locations remain:

```text
ORIGINAL_SOURCE_ROOT
SOURCE_REGISTRY_DATABASE
SOURCE_VAULT_ROOT
INDEPENDENT_BACKUP_ROOT
CLEAN_RESTORE_ROOT
```

The project must not invent these paths or commit them to Git. The original course folder remains read-only input from ADS's perspective.

No deployment operation is currently running.

Course 2 remains blocked when this stage resumes until compare, reviewed ingestion, clean audit, independent verified backup, clean restore, and restored audit are complete.

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

The collaboration architecture is a temporary Level-2 interruption. It does not change Research 033's target-system sequence.

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

No multi-model development decision has yet been promoted.

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

---

# Preservation and continuity

Current accepted sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
```

The multi-model architecture is explicitly challenging this layer, but no accepted method change has occurred yet.

Repository artifacts, exact Git history, checkpoints, and canonical routing remain the continuation authority. Chat history and model-specific private context do not replace them.

---

# Exact current continuation

```text
A. Claude reconstructs the current development method from repository authority
B. Claude reads MC-0001/BRIEF.md but not Research 035
C. Claude preserves an independently derived collaboration architecture
D. freeze that Phase-A result before cross-conditioning
E. Claude reads Research 035 and records a comparative Phase-B review
F. preserve genuine convergence, material disagreement, omissions, and change-of-mind conditions
G. ChatGPT responds to the preserved Claude artifacts
H. classify remaining disagreements by fact / interpretation / requirement / architecture / risk / evidence sufficiency / normative intent / scope
I. route unresolved points to evidence, experiment, human decision, or deferral
J. perform promotion audit for Development Method v0.5, Continuity, checkpoint provenance, validator changes, and MAJOR_CHANGES
K. only after that decide the immediate return point for paused PR #75
L. do not upload Course 2 while the permanent source-vault gate remains unresolved
M. do not rerun or rescore Specifications 015-022 as part of this Level-2 collaboration transition
```
