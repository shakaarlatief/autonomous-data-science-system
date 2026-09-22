# MC-0022 Brief: Independent Project-Knowledge Architecture Residency and Reuse Review

**Thread:** MC-0022
**Date opened:** 2026-09-22
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Independent substantive base:** `c7252e182b6068954aca804fb064a10e37e298a4`
**Reviewer control:** persistent Claude project-knowledge architecture-design conversation, candidate-blind to the new PKIA-E01 topology framing
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. This thread does not change Research 218, Research 177, Specification 028, Candidate 01, current operational authority, W5, AO-10 or any project-knowledge authority boundary.

**Reviewer-control amendment:** MC-0022 was initially opened for a fresh `claude-04` conversation, but before any Claude message was sent the owner challenged that choice. The thread now intentionally reuses persistent `claude-03`, which co-designed the project-knowledge architecture through MC-0011 through MC-0018. Its historical context is useful evidence; blindness is required only to the new PKIA-E01 residency framing/candidate.

## 1. Purpose

The project is reconsidering the physical information architecture from first principles before W5-F0 or AO-10 resumes.

This independent phase asks a question one level above internal folder organization:

> What is the natural residency, ownership, reuse and instantiation architecture of the project-development knowledge/control system itself?

The review must independently determine whether the machinery developed through ADS should remain wholly project-native, have a reusable generic source, depend on shared external tooling, materialize fully into each project, use another topology, or reject the premise that a reusable generic layer is useful.

Do not optimize for agreement with ChatGPT. Do not assume that "professional" means more separation, more repositories, more services, or more reuse.

## 2. Independence boundary

The exact independent substantive base is:

```text
c7252e182b6068954aca804fb064a10e37e298a4
```

From the current coordination branch, before Message 001 is frozen, read only:

```text
docs/current_routing.json
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0022/BRIEF.md
docs/model_collaboration/threads/MC-0022/THREAD.md
docs/model_collaboration/threads/MC-0022/STATE.json
```

All substantive repository evidence must come from the exact independent base above. Claude's preserved `claude-03` context from the earlier project-knowledge architecture program, including MC-0011 through MC-0018, is explicitly allowed and desirable. This review is **candidate-blind, not history-blind**: prior participation in Candidate 01 and W5 design is part of the evidence base rather than contamination.

For the independent phase, do **not** read these exact-base files because they contain ChatGPT's new PKIA-E01 residency framing or synthesis:

```text
docs/research/236_project_knowledge_information_architecture_evolution_case_and_residency_boundary.md
docs/research/237_pkia_e01_residency_history_coupling_and_professional_pattern_audit.md
docs/checkpoints/567_pkia_e01_residency_boundary_opened.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

Also do not read any later PKIA-E01 candidate synthesis, later checkpoint/current-state synthesis, descendant Git diff, descendant commit message/file listing, or search result that reveals ChatGPT's candidate comparison before Message 001 is frozen.

If such candidate content is exposed, report the exposure rather than claiming full independence.

## 3. Candidate-neutral owner question

The project owner wants the issue considered from the origin, not from the assumption that the current ADS repository boundary is correct.

The architecture currently includes or is developing project-development concerns such as durable project knowledge, reconstruction, activation, authority resolution, workstreams, collaboration routing, continuity/recovery, Git lifecycle, architecture evolution and control-obligation behavior.

The review must ask:

```text
What is generic architecture?
What is one project's instance/configuration?
What is actual project knowledge/evidence?
Do those layers naturally share one repository and lifecycle?
Could the architecture serve an unrelated project?
If so, how should it be applied?
What must remain available for a project to reconstruct itself?
What should happen when the generic architecture and a project evolve differently?
```

A reusable source does not automatically imply a permanent runtime dependency. Conversely, project self-containment does not automatically imply copying every implementation artifact.

Generate the topology space independently.

## 4. Minimum substantive reads at the independent base

At minimum inspect the exact-base versions of:

```text
docs/research/124_scalable_repository_knowledge_architecture_and_reconstruction_redesign.md
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/130_requirements_evidentiary_provenance_reconciliation.md
docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md
docs/research/176_candidate01_owner_selection_and_implementation_migration_program_opening.md
docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md

docs/research/206_w5_future_knowledge_information_architecture_and_authoring_design.md
docs/research/207_w5_representative_artifact_family_matrix_and_information_architecture_v01.md
docs/research/208_w5_physical_authoring_v02_freeze_and_empirical_gate_program.md
docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md
docs/research/218_w5_final_information_architecture_reconciliation_and_target_freeze.md

docs/research/219_activation_orchestration_self_hosting_bootstrap_program.md
docs/research/221_ao2_control_plane_capability_boundary_and_failure_taxonomy.md
docs/research/222_ao3_progressive_control_closure_architecture.md
docs/research/223_ao4_architecture_evolution_and_frozen_contract_governance.md
docs/research/224_ao5_anchored_interaction_continuity_and_independent_recovery.md
docs/research/225_ao6_purpose_bound_git_lifecycle_and_workstream_orchestration.md
docs/research/226_ao7_authority_preserving_successor_orchestration_bridge.md
docs/research/227_ao8_independent_architecture_review_reconciliation.md
docs/research/235_ao9_p7_owner_decisions_and_ao9_closure.md

docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md

docs/project_knowledge/architecture/README.md
docs/project_knowledge/architecture/whole_architecture.md
docs/project_knowledge/architecture/semantic_authority_model.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/project_knowledge/architecture/migration_and_cutover.md
```

Inspect the actual `tools/project_knowledge/`, `schemas/project_knowledge/`, `docs/project_knowledge/` and relevant tests at the exact base as needed.

You may inspect additional exact-base sources when material. You may use external sources if a concrete architecture discriminator benefits from them, but distinguish external precedent from ADS evidence and do not copy a framework merely because it exists.

## 5. Independent architecture task

Independently answer the following.

### A. Define the thing being architected

Determine whether the current project-knowledge plus activation/orchestration work is best understood as:

```text
ADS-specific repository infrastructure
generic AI-assisted project-development infrastructure
a generic core with project-specific layers
several separate concerns that should not be packaged together
or another decomposition
```

Explain the natural ownership and lifecycle boundaries, not just the current paths.

### B. Generate the topology space from first principles

Propose genuinely different residency/instantiation architectures without starting from ChatGPT's later candidate list.

For each serious topology, explain:

```text
where the generic design/code lives, if any
what exists inside one concrete project
what remains external after project creation
how project authority is reconstructed
whether the project works offline/alone
how versions are bound
how upgrades work
how divergence works
how rollback works
how project-specific extensions work
how reusable discoveries can flow back
what happens if the generic source disappears
```

### C. Challenge reuse itself

Do not assume cross-project reuse is valuable merely because mechanisms look generic.

Identify which current mechanisms are genuinely reusable, which only appear generic because ADS is the sole real instance, and what evidence a second unrelated project would need to establish.

### D. Self-containment versus shared infrastructure

Determine how strongly a project should be self-contained.

Distinguish:

```text
source ownership
runtime dependency
distribution mechanism
project authority
bootstrap
upgrade channel
provenance lineage
```

Do not collapse them into one inside/outside decision.

### E. Framework-instance-knowledge boundary

Define the cleanest conceptual separation, if any, among:

```text
generic mechanisms
project-specific architecture/policy/configuration
project-specific knowledge/evidence/state
migration/compatibility adapters
provider/tool integrations
```

Identify where the current ADS realization violates or blurs that separation and whether the blur is harmful.

### F. Evolution across many projects

Assume several unrelated projects eventually use the architecture.

Address:

```text
framework releases
project-local customization
breaking schema/control changes
security/correctness fixes
upgrade selection
conflict resolution
intentional long-term divergence
project-to-framework contribution
framework retirement/replacement
```

Avoid hidden global authority over individual projects unless justified.

### G. Disaster recovery and independence

Test each preferred topology when:

```text
the external framework repository is unavailable
the framework is abandoned
the project is cloned to a clean machine
the AI provider changes
a runtime integration disappears
the project has been untouched for years
```

A project that cannot reconstruct its governing knowledge/control semantics under these conditions needs an explicit justification.

### H. Current ADS migration consequences

If your preferred topology differs from Research 177/218/Specification 028, identify the narrowest affected contracts and what would need prospective amendment, supersession or reopening.

Do not silently redesign deeper Candidate 01 semantics unless this question genuinely reaches them.

### I. Internal hierarchy sequencing

State whether the project should decide this residency/instantiation boundary before redesigning Research 218's internal hierarchy, or whether those decisions are independent enough to proceed in parallel.

## 6. Stress-test requirement

Use at least two concrete instances:

```text
1. ADS as the existing large, highly evolved project
2. one hypothetical unrelated project with materially different subject matter
```

Show how the preferred architecture would be initialized, used, evolved and recovered for both.

## 7. Required challenge output

Message 001 must include:

1. preferred architecture and why;
2. strongest alternative;
3. strongest criticism of the preferred architecture;
4. which current ADS mechanisms are truly generic versus project-specific;
5. the three most dangerous long-term failure modes;
6. the three highest-value simplifications;
7. what evidence would falsify the preferred topology;
8. whether a second real project is required before extracting/generalizing anything;
9. exact impact, if any, on Research 177, Research 218 and Specification 028;
10. whether residency should be decided before the internal hierarchy;
11. any external professional patterns that materially informed the judgment, clearly separated from ADS evidence.

End with exactly:

```text
INDEPENDENT_PKIA_RESIDENCY_REVIEW_CONTAMINATED: YES|NO
PREFERRED_RESIDENCY_TOPOLOGY_READY_FOR_COMPARISON: YES|NO
GENERIC_REUSABLE_LAYER_JUSTIFIED: YES|NO
PROJECT_SELF_CONTAINMENT_REQUIRED: YES|NO
MATERIAL_RESEARCH218_IMPACT_FOUND: YES|NO
MATERIAL_SPECIFICATION028_IMPACT_FOUND: YES|NO
```

## 8. Required output

Write exactly one durable response at:

```text
docs/model_collaboration/threads/MC-0022/messages/001_claude_independent_residency_and_reuse_architecture.md
```

Include collaboration provenance, interaction `claude-03`, conversation title `03 - Project Knowledge Architecture Foundations and Design Method`, and exact independent base.

Do not modify any other repository path.

## 9. After Message 001

After Claude's independent Message 001 is committed and pushed, ChatGPT may freeze its own topology candidate synthesis and then expose that candidate for comparative/adversarial review.

Until Message 001 is frozen, ChatGPT will not commit a substantive topology recommendation to the coordination branch.

```text
MC0022=OPEN
MODE=INDEPENDENT_THEN_COMPARATIVE
PHASE=CLAUDE_INDEPENDENT_RESIDENCY_ARCHITECTURE
INDEPENDENT_BASE=c7252e182b6068954aca804fb064a10e37e298a4
PKIA_E01=OPEN
RESEARCH218=FROZEN_BASELINE_RETAINED
AO10=HELD
W5_F0=PAUSED
NEXT=CLAUDE_MESSAGE_001
```
