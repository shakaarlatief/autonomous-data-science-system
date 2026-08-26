# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 205  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`

## Start here

```text
README.md                         project overview and current stage
docs/CURRENT_STATE.md             exact present state and continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable project routing metadata
docs/VISION.md                    high-level product/system direction
docs/PRINCIPLES.md                accepted high-level design principles
docs/DECISIONS.md                 accepted project-level decisions
docs/OPEN_QUESTIONS.md            unresolved questions
docs/DEVELOPMENT_METHOD.md        current canonical development method v0.5
docs/CONTINUITY.md                provider-neutral continuity procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current route:

```text
promoted integration             v1-frontend-spike @ ed5b60bdc882bed0799ce55228ce8187f9c55aa1
active development branch        v1-frontend-spike
active PR                        none
current checkpoint               205
latest specification             Specification 024
Specification 024 outcome        COLLABORATION_STATE_GUARD_ACCEPTED
latest scientific outcome        INCOMPLETE / EXECUTION INTEGRITY FAILED
current operational boundary     permanent user-controlled source-vault bootstrap
```

---

# Current stage: permanent Source Universe deployment before Course 2

Primary route:

```text
docs/checkpoints/205_multimodel_promotion_postmerge_routing_reconciled.md
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md

docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```

Specification 023 result:

```text
SU-G01 through SU-G23   PASS
SOURCE_SUBSTRATE_ACCEPTED
```

Still required on real user-controlled storage:

```text
choose/verify private locations
compare original VU Machine Learning folder to prospective fingerprints
review MATCH / DIFFERENT / MISSING / ADDITIONAL outcomes
ingest reviewed corpus into permanent registry/vault
audit working store
create independent verified backup
perform clean restore
audit restored store
preserve public-safe deployment evidence
```

Course 2 remains blocked until that sequence succeeds.

Required environment inputs before execution:

```text
ORIGINAL_SOURCE_ROOT
INDEPENDENT_BACKUP_ROOT
```

The permanent registry/vault/clean-restore layout can then be chosen without committing private paths.

Important GitHub interpretation:

```text
PR #75 is shown closed/merged because its planning commit d9437a8ca07a444400a5eb44ac2c89e8108c91c2
is an ancestor of the promoted PR #76 merge.

That means the planning artifacts were promoted.
It does not mean permanent source-vault deployment ran.
```

---

# Governed multi-model development is accepted infrastructure

Primary route:

```text
docs/checkpoints/204_multimodel_collaboration_method_promoted.md
docs/checkpoints/205_multimodel_promotion_postmerge_routing_reconciled.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/DECISIONS.md, D-034
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/specifications/024_v1_model_collaboration_state_guard.md
```

Current collaboration status:

```text
MC-0001   CLOSED
MC-0002   CLOSED
MC-0003   CLOSED
pending review inbox   NONE
GitHub Issue #78       CLOSED / completed
GitHub Issue #79       CLOSED / completed
```

No additional Claude review is currently owed.

Accepted collaboration principles:

```text
repository authority
SOLO remains first-class
selective task-scoped collaboration
one bounded task owner
ROLE != WRITE_SCOPE
one target-state writer at a time
explicit secondary write surfaces
machine-readable collaboration-state coherence guard
transport != authority
durable numbered collaboration provenance
proportional independent/comparative review
known contamination disclosure
explicit disagreement classification/routing
provider-local interaction session identities
human project-intent authority without routine transport burden
deferred review/catch-up with exact targets and explicit gates
API orchestration deferred
unattended scheduled model review deferred
```

Provider-neutral checkpoint provenance begins at Checkpoint 204.

---

# Specification 024: accepted collaboration-state guard

Primary route:

```text
docs/specifications/024_v1_model_collaboration_state_guard.md
schemas/model_collaboration_thread_state_v1.schema.json
scripts/check_model_collaboration_state.py
tests/unit/test_model_collaboration_state.py
.github/workflows/model-collaboration-state.yml
docs/model_collaboration/threads/MC-0002/RESOLUTION.md
```

Evidence:

```text
pre-implementation freeze       9da382d4011ff112b75dec9c456143d798336336
corrected green pre-review head a9efc43d7c441c8283d2cd954cc6fa1abd021689
workflow run                    32902050014
Ubuntu                          PASS
Windows                         PASS
focused tests                   26 PASS per platform
Claude review commit            9cf393f74e02e167d2f80c0381742ebd7e0c318e
final outcome                   COLLABORATION_STATE_GUARD_ACCEPTED
promotion merge                 ed5b60bdc882bed0799ce55228ce8187f9c55aa1
```

The mechanism is a coherence guard, not authenticated model identity or a distributed mutex.

Known future trigger: secondary-vs-secondary write-surface overlap if a real thread introduces multiple simultaneous secondary writers.

---

# MC-0001: architecture review history

Primary route:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
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

Important review-integrity finding: Phase A was only partially independent because current routing documents exposed candidate concepts. Future deliberately blind reviews should normally use an accepted pre-proposal ref plus a neutral brief and explicit exposure audit.

---

# MC-0003: deferred asynchronous catch-up

Primary route:

```text
docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0003/RESOLUTION.md
docs/model_collaboration/threads/MC-0003/messages/002_claude_deferred_catchup_review.md
docs/model_collaboration/threads/MC-0003/messages/003_chatgpt_review_disposition.md
```

Accepted rule:

```text
collaborator unavailable
    !=
project globally blocked
```

unless the affected task's review gate has been reached.

Current semantic constraint:

```text
REQUIRED review -> real gate required
OPTIONAL review -> NONE allowed
```

Known future mechanization triggers:

```text
cross-thread dependency metadata / downstream impact discovery
generated REVIEW_INBOX or inbox-state consistency validation
explicit review-obligation and gate fields if backlog scale requires them
stale/superseded obligation validation after repeated real use
```

No Specification 025 is currently justified.

---

# Interaction provenance and naming

Current canonical convention:

```text
shared project/workspace     Autonomous Data Science System
visible title                NN - Main Topic / Stage
ChatGPT session example      chatgpt-06
Claude session example       claude-01
```

Checkpoint provenance:

```text
000-203
    historical ChatGPT-specific fields remain intact

204+
    Interaction environment
    Project / workspace
    Interaction session
    Conversation title
    Primary collaborator
```

Optional model/configuration/effort/surface metadata is preserved only where materially useful and should not be guessed.

---

# Serious methodological knowledge-universe construction

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

Coverage depth is separate from truth, maturity, source authority, freshness, confidence, and enforcement strength.

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
D-033  ADS-owned Source Universe substrate
D-034  governed provider-neutral multi-model development collaboration
```

---

# Retrieval and later experimental evidence

The accepted bounded chain includes lexical retrieval, dense complementarity, hybrid comparison, explained MethodologicalHorizon, selective exact-revision context, and the ADS-owned ReasoningRuntime.

Specification 014 preserved equal measured quality on its bounded benchmark while reducing provider input by 66.56%.

Later recommendation/action results remain deliberately bounded. Specification 022 remains:

```text
INCOMPLETE / EXECUTION INTEGRITY FAILED
```

It contains no legitimate `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` scientific comparison.

---

# Preservation and continuity

Canonical route:

```text
docs/DEVELOPMENT_METHOD.md                version 0.5
docs/CONTINUITY.md                        aligned version 0.5
docs/checkpoints/README.md                provider-neutral from Checkpoint 204
scripts/check_checkpoint_metadata.py       versioned provenance validation
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
```

---

# Exact current continuation

```text
A. obtain/confirm the actual ORIGINAL_SOURCE_ROOT
B. obtain/confirm a genuinely independent backup location
C. choose permanent private registry/vault/clean-restore locations
D. compare the original ML folder against preserved prospective fingerprints
E. inspect every comparison class before any manifest adjustment
F. execute reviewed ingestion, audit, independent backup, clean restore, and restored audit
G. preserve only public-safe deployment evidence in Git
H. admit Course 2 only after permanent recovery integrity is proven
I. continue serious methodological knowledge-universe construction
```
