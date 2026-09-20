# MC-0018 Brief: W5 Future Knowledge Information Architecture Co-Design

**Thread:** MC-0018
**Date opened:** 2026-09-20
**Review mode:** REVIEWED / CURRENT_CONTEXT_CO_DESIGN
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact design target:** `ac45bc7078cd23af85f243cb61ba6a8b499f284d`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. Candidate 01, Specification 028, Requirements V0.2 and accepted W0-W4 results remain stronger within their scopes. This thread cannot switch operational authority or begin broad migration by itself.
**Purpose:** Re-engage the persistent Claude architecture collaborator after W0-W4 and jointly pressure-test W5's concrete future information architecture before it is frozen.

## 1. What changed since MC-0017

MC-0017 reconciled W0 implementation architecture. Since then:

```text
W0  implementation substrate                         ACCEPTED / Checkpoint 542
W1  live control semantics                          ACCEPTED / Checkpoint 551
W2  persistent shadow derived views                 ACCEPTED / Checkpoint 552
W3  compatibility shadow                            ACCEPTED AND FINALIZED / Checkpoint 553
W4  real capture -> review -> promotion -> archive  ACCEPTED AND FINALIZED / Checkpoint 554
```

Current invariant:

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

W5 is open, but broad semantic migration is deliberately paused. The owner explicitly asked that we first decide how durable project knowledge should actually be saved from now on: physical folders/files, file families, naming, granularity, natural ownership, lifecycle and multi-axis subjects/hierarchies. Candidate 01 should not merely sit on top of the old physical structure forever.

## 2. Exact-target reading set

Use the coordination branch only to locate the obligation. Bind substantive review/design to exact target `ac45bc7078cd23af85f243cb61ba6a8b499f284d`.

At minimum inspect:

```text
docs/research/206_w5_future_knowledge_information_architecture_and_authoring_design.md
docs/research/207_w5_representative_artifact_family_matrix_and_information_architecture_v01.md
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
docs/research/124_scalable_repository_knowledge_architecture_and_reconstruction_redesign.md
docs/research/176_candidate01_owner_selection_and_implementation_migration_program_opening.md
docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md
docs/project_knowledge/architecture/README.md
docs/project_knowledge/architecture/whole_architecture.md
docs/project_knowledge/architecture/semantic_authority_model.md
docs/project_knowledge/architecture/knowledge_lifecycle.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/project_knowledge/architecture/migration_and_cutover.md
docs/research/193_w0_complete_unit_suite_g017_and_w0_acceptance_result.md
docs/research/202_w1_public_repository_integrity_g109_and_w1_acceptance_result.md
docs/research/203_w2_shadow_derived_views_acceptance_result.md
docs/research/204_w3_compatibility_shadow_acceptance_result.md
docs/research/205_w4_production_capture_promotion_acceptance_result.md
```

Inspect representative repository families as needed. You may use your preserved MC-0011 through MC-0017 context. This is intentionally current-context co-design, not an independence-sensitive blind review.

## 3. V0.1 proposal to challenge

Research 207 currently proposes a hybrid:

```text
small project-global singleton set at docs/
+ numbered epistemic/lifecycle families
+ top-level natural domain/subsystem homes
+ narrow docs/project_knowledge infrastructure
+ generated multi-axis navigation instead of folder-as-taxonomy
```

It also proposes prospective naming/granularity rules, an ordinary authoring decision tree, optional explicit subject membership, subject polyhierarchy, and one preferred/default route that is not exclusive parentage.

Nothing in V0.1 is frozen.

## 4. Questions for Claude

Think architecturally with ChatGPT rather than merely proofreading Research 207.

### A. Physical structure

Would you keep the root singleton set? Are foundations/specifications/research/checkpoints genuinely principled future families or legacy familiarity? Are top-level domain homes preferable to a generic `domains/` wrapper? Is `docs/project_knowledge/` still narrow enough? What physical structure would you choose today under Candidate 01?

### B. All prospective artifact families

Review the entire current family landscape, including vision, principles, decisions, open questions, architecture backlog, development method, continuity, workstreams, procedures, research, foundations, specifications, checkpoints, experiments/results, validation, runbooks, implementation provenance, collaboration, captures, transitions, joint authority, private-delegated knowledge, generated views and domain-local ledgers/manifests.

For each class, identify what should be retained, refined, split, merged, retired prospectively, historical-only, generated, or newly introduced.

### C. Naming and granularity

Pressure-test numeric IDs, filename conventions, dates, semantic IDs in filenames, when a new file is warranted, when to update an existing owner, and how rename/move continuity should work without cosmetic churn.

### D. Subjects, hierarchy and navigation

Attack the proposed subject-catalog/per-source-membership idea. Could it become a disguised central ontology or registry? Which subjects deserve authored identity versus generated grouping? Where should memberships live? How should identity-free sources participate? How should multiple parents, preferred routes, aliases/renames/merges work? Keep subject, domain, workstream, artifact family, lifecycle, authority, provenance and task facets distinct.

### E. Historical knowledge and migration

Which historical carriers should remain untouched? Which still contain live meaning that must migrate? When are physical moves/renames worthwhile? How should successor navigation cover history without mass retrofitting? How do we prove no current responsibility remains trapped in evidence/history?

### F. Ordinary future authoring

The final design must answer: if important knowledge appears tomorrow, what exactly should a collaborator create or update? Test the proposed decision tree against ambiguous real ADS cases and identify where two reasonable collaborators could choose different homes/families.

### G. Architecture versus implementation

Distinguish what W5 must freeze before migration from schema/data-model choices, generated-view implementation details and cosmetic organization that can safely remain open.

### H. W0-W4 feedback

Use real implementation evidence to ask whether earlier assumptions should change. Did selective declarations remain selective? Did generated views validate multi-axis organization? Did W3 expose navigation/current-state limits? Did W4 capture/promotion suggest better authoring ergonomics?

## 5. Required first response

Write exactly one response at:

```text
docs/model_collaboration/threads/MC-0018/messages/001_claude_w5_information_architecture_review_and_counterdesign.md
```

Include collaboration provenance and the exact reviewed commit. Cover:

1. reconstruction of what changed since MC-0017;
2. strongest V0.1 properties;
3. MUST-FIX issues before freezing;
4. SHOULD-REFINE issues;
5. artifact-family disposition changes;
6. your preferred physical architecture;
7. your preferred subject/polyhierarchy architecture;
8. naming/granularity/authoring rules;
9. historical migration implications;
10. smallest next design/prototype tests;
11. explicit questions for ChatGPT where dialogue is useful;
12. whether V0.1 is ready to freeze or needs another iteration.

Do not implement or mutate target-state docs.

## 6. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0018/messages/**
```

ChatGPT remains task owner/integrator.

```text
MC0018=OPEN
MODE=REVIEWED_CURRENT_CONTEXT_CO_DESIGN
EXACT_DESIGN_TARGET=ac45bc7078cd23af85f243cb61ba6a8b499f284d
W5_INFORMATION_ARCHITECTURE=NOT_FROZEN
BROAD_W5_MIGRATION=NOT_STARTED
MESSAGE_001=CLAUDE_NEXT
```
