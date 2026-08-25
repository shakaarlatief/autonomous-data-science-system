# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-25  
**Current checkpoint:** 201  
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
current checkpoint               201
latest specification             Specification 023
latest scientific outcome        INCOMPLETE / EXECUTION INTEGRITY FAILED
```

---

# Current stage: MC-0001 bounded Phase D challenge

Primary route:

```text
docs/checkpoints/201_mc_0001_phase_b_and_c_recorded_bounded_phase_d_challenge_opened.md
docs/checkpoints/200_mc_0001_phase_a_recorded_partial_independence_contamination_phase_b_opened.md
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/model_collaboration/threads/MC-0001/THREAD.md
docs/model_collaboration/threads/MC-0001/messages/001_chatgpt_review_request.md
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
```

Live transport:

```text
GitHub Issue #77
```

Authority separation:

```text
issue / PR comments
    optional transport

Model Collaboration Exchange
    durable collaboration provenance

Research 035
    candidate architecture only

DEVELOPMENT_METHOD / CONTINUITY / accepted decisions
    current canonical method until explicit promotion
```

## MC-0001 evidence accumulated so far

### Phase A

Claude completed its first counter-design directly through repository access:

```text
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
```

Claude did not read Research 035 or ChatGPT message 001 before freezing the artifact. However, the required reconstruction documents already summarized multiple candidate Research 035 ideas.

Therefore:

```text
independent from full Research 035 proposal       YES
independent from ChatGPT message 001              YES
blind to all ChatGPT candidate architecture       NO
```

Checkpoint 200 preserves this review-integrity limitation. Convergence on already exposed ideas is not clean independent confirmation.

### Phase B

Claude completed:

```text
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
```

The review identifies genuine Phase-B convergence, omissions on both sides, revised Claude positions, dangerous under-specification, must-change items, and remaining disagreements.

Important Claude contributions include:

```text
machine-checkable collaboration state is missing
blind-review contamination needs an explicit protocol
HIGH / LOW impact triggers are useful working defaults
Issue transport should be pointer-first with disclosed fallback
routine human authorization should be reduced
provider-local session numbering + environment-prefixed IDs is preferable
role taxonomy / lifecycle vocabulary are useful but should stay proportional
```

The user reported that this Phase-B pass used Claude Sonnet 5 with `Extra` effort. That effort fact is preserved in Checkpoint 201 rather than rewriting Claude's frozen message.

### Phase C

ChatGPT completed:

```text
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
```

Key ChatGPT dispositions:

```text
accept machine-readable collaboration-state support as a pre-routine requirement
reject one global active-writer field as too coarse
prefer scoped per-thread target-write ownership + allowed write surfaces
classify JSON/validator as coherence guard, not true distributed lock
strengthen blind review around accepted base refs + neutral problem packets
accept HIGH / LOW as provisional, not universal
route REQUIREMENT to canonical authority before human arbitration
reject blanket "more risk-averse wins" routing
reject blanket "narrow scope wins" routing
accept ROLE != WRITE_SCOPE
accept provider-local environment-prefixed session IDs
```

None of these are yet promoted into the canonical Development Method.

## MC-0001 Phase D

Expected next artifact:

```text
docs/model_collaboration/threads/MC-0001/messages/005_claude_phase_d_challenge.md
```

The challenge is deliberately bounded to:

```text
scoped collaboration state versus a single global active writer
JSON as coherence guard versus true lock
canonical requirement authority before human arbitration
risk/scope routing defaults
ROLE != WRITE_SCOPE
accepted-base-ref + neutral-brief blind-review design
provider-local session/provenance convergence
```

After message 005, unresolved items should be routed to design/prototype, evidence, human project-intent decision, or explicit deferral rather than continuing open-ended debate.

---

# Candidate interaction provenance and naming

Current candidate design:

```text
ChatGPT project/workspace  Autonomous Data Science System
ChatGPT sessions           provider-local numbered conversations, e.g. chatgpt-06

Claude project/workspace   Autonomous Data Science System
Claude sessions            provider-local numbered conversations, e.g. claude-01

MC-NNNN                    globally unique collaboration-thread identity
```

Current live sessions participating in MC-0001:

```text
chatgpt-06
06 - Methodological Knowledge Universe Construction

claude-01
01 - ADS Development Review & Collaboration
```

Likely substantive-message provenance includes author, role, interaction environment, project/workspace, interaction session, conversation title, repository head, thread/message identity, and in-reply-to. Model/configuration, interaction surface, effort/reasoning mode, timestamp, and artifacts read are candidate optional fields when known and material.

The exact provider-neutral provenance schema remains candidate-only until MC-0001 resolves.

Historical ChatGPT-specific checkpoint metadata is not to be rewritten merely for future visual uniformity.

---

# Candidate mechanical collaboration-state direction

A machine-readable mechanism is now considered a must-address design problem before routine multi-model canonical development, but no exact schema is frozen.

Likely design neighborhood:

```text
docs/model_collaboration/threads/MC-XXXX/STATE.json
```

Candidate concerns:

```text
thread identity
review mode
lifecycle state
target branch
task owner
target write owner
allowed collaborator/role write surfaces
next expected actor
last transition
independence status where applicable
```

A validator could provide coherence checks. It would not automatically become a true distributed lock because current model connectors share the user's GitHub authority.

Stronger branch-protection/server-side machinery remains deferred pending evidence.

---

# Source Universe substrate and paused permanent deployment

Accepted source route:

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

The accepted implementation is promoted in `v1-frontend-spike` at `8215718db3e44f000cc6ed53d6a051522d429dbd`.

Draft PR #75 is paused, not abandoned. The permanent Source Registry, private Source Vault, independent backup, and clean restore still need to be instantiated on user-controlled storage before Course 2 is admitted.

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

The source and collaboration work are Level-2 / substrate prerequisites for conducting this program professionally and durably.

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

Specification 014 preserved equal measured quality on its bounded benchmark while reducing provider input by 66.56%.

---

# Later recommendation/action evidence

Historical downstream results remain bounded:

```text
Specification 015  FAIL
Specification 016  dependency-backed DEFER-vs-NOT_NOW construct supported
Specification 017  INCOMPLETE
Specification 019  FAIL after provenance repair
Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED construct supported
Specification 021  FAIL
Specification 022  INCOMPLETE / EXECUTION INTEGRITY FAILED
```

Specification 022 contains no legitimate `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` scientific comparison.

---

# Preservation and continuity

Primary sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
```

These remain canonical until MC-0001 completes and any multi-model changes are explicitly promoted.

---

# Exact current continuation

```text
A. Claude reads messages/004_chatgpt_response_to_claude.md
B. Claude performs one bounded Phase-D challenge
C. preserve messages/005_claude_phase_d_challenge.md
D. mark each unresolved item AGREE / DISAGREE / PARTIAL with strongest reason + change-of-mind evidence
E. route remaining disagreement to bounded design/prototype, evidence, human decision, or explicit deferral
F. perform the promotion audit only after the cross-model exchange resolves
G. if mechanical collaboration-state support remains required, design and test it before routine multi-model canonical development is declared ready
H. do not promote Development Method v0.5, provider-neutral checkpoint provenance, or API orchestration prematurely
I. keep PR #75 paused until the user chooses to resume the source-vault bootstrap
J. after source operationalization, continue the serious methodological knowledge-universe program
```