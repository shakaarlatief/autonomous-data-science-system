# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 203  
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
docs/DEVELOPMENT_METHOD.md        current canonical development method
docs/CONTINUITY.md                current canonical continuity procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current branch relationship:

```text
promoted integration             v1-frontend-spike @ 8215718db3e44f000cc6ed53d6a051522d429dbd
paused deployment branch         v1-source-vault-bootstrap / PR #75
active collaboration branch      v1-multimodel-development-collaboration / PR #76
current checkpoint               203
latest specification             Specification 024
latest scientific outcome        INCOMPLETE / EXECUTION INTEGRITY FAILED
```

---

# Current stage: Specification 024 direct implementation review

Primary route:

```text
docs/checkpoints/203_specification_024_implementation_green_pre_review_head_frozen.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/model_collaboration/threads/MC-0002/BRIEF.md
docs/model_collaboration/threads/MC-0002/THREAD.md
docs/model_collaboration/threads/MC-0002/STATE.json
docs/model_collaboration/threads/MC-0002/messages/001_chatgpt_implementation_review_request.md
schemas/model_collaboration_thread_state_v1.schema.json
scripts/check_model_collaboration_state.py
tests/unit/test_model_collaboration_state.py
.github/workflows/model-collaboration-state.yml
GitHub Issue #78
```

Current machine-readable state:

```text
thread                  MC-0002
review mode             REVIEWED
lifecycle               WAITING
phase                   REVIEW_REQUESTED
task owner              chatgpt
target write owner      chatgpt
next actor              claude
Claude secondary write  MC-0002/messages/**
```

Implementation contract and evidence:

```text
Specification 024 frozen at 9da382d4011ff112b75dec9c456143d798336336
initial implementation          bf33aab15d9300836280f01ebd9b6db0951f3e9a
corrected green pre-review head a9efc43d7c441c8283d2cd954cc6fa1abd021689
workflow run                     32902050014
Ubuntu                           PASS
Windows                          PASS
focused unit tests               26 PASS on each platform
```

MC-G01 through MC-G15 have current implementation/CI support. MC-G16 is the pending direct Claude implementation review.

The guard is explicitly a coherence mechanism, not an authenticated distributed lock.

---

# Resolved MC-0001 collaboration architecture

Primary route:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/model_collaboration/threads/MC-0001/THREAD.md
docs/model_collaboration/threads/MC-0001/RESOLUTION.md
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
docs/model_collaboration/threads/MC-0001/messages/005_claude_phase_d_challenge.md
docs/model_collaboration/threads/MC-0001/messages/006_chatgpt_phase_d_resolution.md
docs/checkpoints/199_multi_model_collaboration_architecture_candidate_frozen_for_independent_review.md
docs/checkpoints/200_mc_0001_phase_a_recorded_partial_independence_contamination_phase_b_opened.md
docs/checkpoints/201_mc_0001_phase_b_and_c_recorded_bounded_phase_d_challenge_opened.md
docs/checkpoints/202_mc_0001_resolved_specification_024_frozen_mc_0002_opened.md
```

Resolved candidate principles:

```text
repository authority
selective collaboration with SOLO as first-class mode
one bounded task owner
ROLE != WRITE_SCOPE
scoped target-state write ownership
allowed secondary review/provenance surfaces
machine-readable collaboration state before routine scale-up
transport != authority
append-only relied-upon review provenance
proportional anti-anchoring review
explicit disagreement classification/routing
provider-local self-describing session identities
human project-intent authority without routine transport burden
API orchestration deferred
```

Phase A of MC-0001 was only partially independent because current routing files already exposed candidate architecture content. Future deliberately blind reviews should normally reconstruct from an accepted pre-proposal ref plus a neutral brief and exposure audit.

No multi-model Development Method revision or accepted decision has been promoted yet.

---

# Interaction provenance and naming

Candidate convention exercised by the first threads:

```text
ChatGPT project/workspace  Autonomous Data Science System
ChatGPT session            chatgpt-06
ChatGPT title              06 - Methodological Knowledge Universe Construction

Claude project/workspace   Autonomous Data Science System
Claude session             claude-01
Claude title               01 - ADS Development Review & Collaboration

collaboration thread       MC-NNNN
```

Model/configuration and interaction surface are useful optional provenance. Effort/reasoning-mode values should preserve whether they were model-reported, human-reported, system-reported, or unknown instead of being guessed.

The checkpoint metadata contract remains historically ChatGPT-specific until a prospective provider-neutral migration is explicitly promoted.

---

# Source Universe substrate and paused permanent deployment

Accepted route:

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

Specification 023 result:

```text
SU-G01 through SU-G23   PASS
SOURCE_SUBSTRATE_ACCEPTED
```

The accepted implementation is promoted at `8215718db3e44f000cc6ed53d6a051522d429dbd`.

PR #75 remains paused, not abandoned. Permanent Source Registry, private Source Vault, independent backup, and clean restore still need to be instantiated on user-controlled storage before Course 2 is admitted.

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

First six deep slices:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

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

---

# Product, persistence, runtime, and source storage

Important primary sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Accepted V1 decisions:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime
D-033  ADS-owned Source Universe substrate with private artifact store + relational registry
```

No multi-model development decision has yet been promoted.

---

# Retrieval and later experimental evidence

The accepted bounded chain includes lexical retrieval, dense complementarity, hybrid comparison, explained MethodologicalHorizon, selective exact-revision context, and the ADS-owned ReasoningRuntime.

Specification 014 preserved equal measured quality on its bounded benchmark while reducing provider input by 66.56%.

Later recommendation/action results remain deliberately bounded. Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; it contains no legitimate `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` scientific comparison.

---

# Preservation and continuity

Canonical method remains:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
```

These remain authoritative until Specification 024 is classified and the collaboration-method promotion audit explicitly changes them.

---

# Exact current continuation

```text
A. Claude performs the bounded MC-0002 direct implementation review
B. Claude writes messages/002_claude_implementation_review.md only
C. ChatGPT integrates bounded required corrections, if any
D. rerun frozen MC-G01 through MC-G15 after correction
E. decide MC-G16 from durable review evidence
F. classify Specification 024
G. only then perform the canonical Development Method / Continuity / checkpoint-provenance / decision promotion audit
H. keep PR #75 paused until permanent source-vault deployment resumes
I. after source operationalization, continue the serious methodological knowledge-universe program
```
