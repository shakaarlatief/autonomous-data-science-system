# MC-0024 Brief: Comparative Review of Research 218 Versus R7 Target Information Architecture

**Thread:** MC-0024
**Date opened:** 2026-09-22
**Review mode:** COMPARATIVE_ARCHITECTURE_REVIEW
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact review target:** `b0ff5c59411b2fae2786a87d6b93ea722e7cdfe5`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. The project owner has not yet accepted Research 254 / R7-B.

## 1. Why this review exists

Research 218 froze a future Project information architecture on 2026-09-20.

Research 254 now recommends materially superseding that physical architecture only two days later.

The difference is intentionally large.

The owner has correctly asked:

- Is the new architecture actually better?
- Was Research 218 weaker because the earlier design process treated current folders, domain homes and existing `docs/` structure as stronger constraints than the owner intended?
- Or is the difference better explained by a legitimate change in problem scope?
- Has the new R7 design overcorrected by imposing Product/Project and governance/evidence/operations/history abstractions too aggressively?
- Before accepting R7, should the project obtain an independent comparative judgment?

This thread exists to answer those questions directly.

## 2. Exact comparison

Compare at minimum:

### Earlier frozen architecture

`docs/research/218_w5_final_information_architecture_reconciliation_and_target_freeze.md`

and its design path:

`docs/research/206_w5_future_knowledge_information_architecture_and_authoring_design.md`
`docs/research/208_w5_physical_authoring_v02_freeze_and_empirical_gate_program.md`
`docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md`
`docs/research/212_w5_t3_item_registry_identity_carrier_result.md`
`docs/research/214_w5_t4_historical_navigation_preservation_result.md`
`docs/model_collaboration/threads/MC-0018/**`

### Reopened / whole-repository architecture path

`docs/research/240_pkia_e01_whole_repository_physical_architecture_scope_and_design_program.md`
`docs/research/246_whole_repository_r5_owner_acceptance_and_from_scratch_lower_level_boundary.md`
`docs/research/248_g_dual_owner_amendment_acceptance_and_r6_entry_contract.md`
`docs/research/249_r6a_from_scratch_professional_responsibility_model_and_root_bound.md`
`docs/research/250_r6a_responsibility_coupling_bounded_context_and_workspace_synthesis.md`
`docs/research/251_r6_bounded_context_architecture_owner_acceptance_and_r6b_entry.md`
`docs/research/252_r6b_current_to_target_mapping_and_structural_disposition_matrix.md`
`docs/research/253_r7a_from_scratch_project_information_model_authority_and_lifecycle.md`
`docs/research/254_r7b_target_project_information_hierarchy_and_research218_supersession_candidate.md`

Also inspect current repository structure and any prior collaboration evidence you consider materially relevant.

## 3. Questions you must answer

### A. Why are the architectures so different?

Identify the causal reasons, not merely the structural differences.

Distinguish among:

- change in problem scope;
- change in design method;
- new evidence;
- owner clarification;
- path dependence on current repository layout;
- migration-risk conservatism;
- implementation constraints from Specification 028;
- genuine correction of a weaker earlier architecture;
- overcorrection in the newer architecture.

### B. Was Research 218 "wrong"?

Do not answer with a binary slogan.

Assess separately:

- whether Research 218 was internally coherent for its stated W5 problem;
- whether its physical architecture was too constrained by the existing `docs/` structure and current domain folders;
- whether the owner clarification in Research 240/246 materially changes the correct design objective;
- which parts of Research 218 remain strong and should survive;
- which parts should now be superseded.

### C. Is Research 254 actually better?

Evaluate the new target on:

- conceptual coherence;
- professional repository/information-architecture quality;
- future scale;
- human cold-start comprehensibility;
- agent cold-start comprehensibility;
- authority clarity;
- evidence/provenance separation;
- operational knowledge;
- historical preservation;
- avoidance of dumping-ground categories;
- migration feasibility;
- compatibility with Candidate 01 semantics;
- compatibility with PSMF;
- ability to evolve without another disruptive redesign.

### D. Attack the four-class hierarchy

Challenge:

`governance / evidence / operations / history`

Ask whether:

- these are truly orthogonal enough to be stable physical parents;
- `operations` risks becoming a new miscellaneous bucket;
- `history` is too lifecycle-oriented to deserve a physical parent;
- architecture rationale/specifications/decisions/planning are grouped correctly;
- research/qualification/provenance are grouped correctly;
- another professional hierarchy would be materially stronger.

### E. Attack Project System / Project Knowledge separation

Challenge:

`project/system/`
`project/knowledge/`

Ask whether this is a genuinely durable distinction or merely a renamed version of the old project_knowledge split.

Check especially:

- generated views;
- current routing;
- captures;
- declarations;
- machine schemas;
- human-readable system architecture;
- operational procedures;
- collaboration state.

### F. Assess the "current-structure anchoring" hypothesis

Research 208 explicitly retained current domain/subsystem homes and epistemic/lifecycle families.

Determine whether that was:

- a justified evidence-based conclusion;
- a pragmatic migration constraint;
- a hidden assumption inherited from the current tree;
- or some combination.

Use exact evidence from MC-0018 / Research 208 / Research 218.

### G. Strongest alternative

If Research 254 is not the best target, give the strongest alternative.

It may be:

- Research 218 retained with amendments;
- Research 254 amended;
- a different hierarchy;
- a more responsibility-first or artifact-first hybrid.

Do not merely say "it depends"; specify the discriminator.

## 4. Required final disposition

End with one of:

```text
R7_COMPARATIVE_DISPOSITION: ACCEPT|AMEND|REOPEN
RESEARCH218_PHYSICAL_SUPERSESSION_JUSTIFIED: YES|NO
RESEARCH218_WAS_OVERCONSTRAINED_BY_CURRENT_TREE: YES|PARTLY|NO
R254_IS_MATERIALLY_BETTER_TARGET: YES|NO
R254_OVERREACTS_TO_PRIOR_CONSTRAINTS: YES|PARTLY|NO
OWNER_CAN_ACCEPT_R7_AFTER_CHATGPT_RECONCILIATION: YES|NO
```

If AMEND, specify the exact amendment.

If REOPEN, identify the architectural assumption that fails.

## 5. Required output path

Write exactly one response at:

`docs/model_collaboration/threads/MC-0024/messages/001_claude_r218_vs_r254_comparative_review.md`

Include:

- exact reviewed commit;
- collaboration provenance;
- interaction `claude-03`;
- conversation title `03 - Project Knowledge Architecture Foundations and Design Method`.

Do not modify any other repository path.

## 6. Write boundary

Claude may write only:

`docs/model_collaboration/threads/MC-0024/messages/**`

```text
MC0024=OPEN
MODE=COMPARATIVE_ARCHITECTURE_REVIEW
EXACT_REVIEW_TARGET=b0ff5c59411b2fae2786a87d6b93ea722e7cdfe5
R7_OWNER_DECISION=PENDING
PHYSICAL_MIGRATION_AUTHORIZED=false
NEXT=CLAUDE_MESSAGE_001
```
