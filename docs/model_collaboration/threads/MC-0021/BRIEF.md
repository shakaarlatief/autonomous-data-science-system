# MC-0021 Brief: Independent Activation/Orchestration Control-Plane Architecture Review

**Thread:** MC-0021
**Date opened:** 2026-09-21
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** v1-source-vault-bootstrap-resume
**Independent substantive base:** b649c1a846d3bf9274fd718e0efd8de9d63bd990
**Integrated candidate target withheld until Phase 2:** f73239ee486132a94701de80514ffd11480b9ecd
**Reviewer control:** fresh Claude architecture-review conversation
**Authority:** Collaboration evidence only. This thread cannot change current project authority, amend Research 218, begin AO-9/AO-10, or switch W5/W6/W8 state.

## 1. Purpose

Research 219 deliberately schedules an independent architecture review after the activation/orchestration design becomes substantial enough to challenge.

The review must not begin by reading ChatGPT's selected AO-3 through AO-7 architecture. Phase 1 asks Claude to reconstruct the problem from the accepted pre-proposal evidence and independently determine what control-plane architecture should exist.

Only after Claude freezes Message 001 will Phase 2 expose the integrated candidate for comparative/adversarial review.

The gate is:

~~~text
REVIEW_REQUIREMENT = REQUIRED
GATE = BEFORE_THREAD_RESOLUTION
AO-9 empirical historical-regression design does not begin
until the independent/comparative review is reconciled.
~~~

## 2. Independence boundary

The exact independent base is:

~~~text
b649c1a846d3bf9274fd718e0efd8de9d63bd990
~~~

This base includes AO-1/AO-2 and the Chat 28 continuation evidence, but predates the selected AO-3 through AO-7 architecture.

From the current coordination branch, before Message 001 is frozen, read only:

~~~text
docs/current_routing.json
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0021/BRIEF.md
docs/model_collaboration/threads/MC-0021/THREAD.md
docs/model_collaboration/threads/MC-0021/STATE.json
~~~

All substantive project/design reads must come from exact Git commit:

~~~text
b649c1a846d3bf9274fd718e0efd8de9d63bd990
~~~

Do not read descendant candidate material before Message 001 is frozen, including:

~~~text
docs/research/222_ao3_progressive_control_closure_architecture.md
docs/research/223_ao4_architecture_evolution_and_frozen_contract_governance.md
docs/research/224_ao5_anchored_interaction_continuity_and_independent_recovery.md
docs/research/225_ao6_purpose_bound_git_lifecycle_and_workstream_orchestration.md
docs/research/226_ao7_authority_preserving_successor_orchestration_bridge.md

docs/research/project_knowledge_activation_orchestration/AO3_*.json
docs/research/project_knowledge_activation_orchestration/AO4_*.json
docs/research/project_knowledge_activation_orchestration/AO5_*.json
docs/research/project_knowledge_activation_orchestration/AO6_*.json
docs/research/project_knowledge_activation_orchestration/AO7_*.json

Checkpoint 559 through Checkpoint 563 bodies
descendant CURRENT_STATE synthesis describing AO-3 through AO-7
any future MC-0021 comparative message
~~~

Do not inspect descendant Git diffs, commit messages, file lists, generated views, or searches in a way that indirectly reveals the candidate.

If candidate content is exposed before Message 001 is frozen, report:

~~~text
INDEPENDENT_CONTROL_PLANE_REVIEW_CONTAMINATED: YES
~~~

and describe the exposure.

## 3. Candidate-neutral owner constraints added after the blind base

Two later owner principles are intentionally supplied because they govern the review method but do not reveal the candidate design.

### No sunk-cost architecture constraint

Existing files, schemas, tools, branch structures, migration paths, and prior implementations are evidence and migration constraints, not automatic design authority. Recommend a materially better design when justified, even if migration is inconvenient. Do not preserve an inferior approach merely because work has already been invested in it.

### Owner-message intent is not automatically a directive

A question, observation, idea, suggestion, preference, decision, and explicit change request are different communicative acts. In particular, a genuine question about whether something should be done is not itself an instruction to do it.

Treat these as fixed owner constraints for the review.

## 4. Minimum substantive reads at the independent base

At minimum inspect the exact-base versions of:

~~~text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/219_activation_orchestration_self_hosting_bootstrap_program.md
docs/research/220_ao1_retrospective_activation_orchestration_completeness_audit.md
docs/research/221_ao2_control_plane_capability_boundary_and_failure_taxonomy.md

docs/research/project_knowledge_activation_orchestration/001_chat26_owner_source_interaction_orchestration_evidence.md
docs/research/project_knowledge_activation_orchestration/002_chat27_activation_self_hosting_bootstrap_evidence.md
docs/research/project_knowledge_activation_orchestration/003_chat28_continuation_reconstruction_activation_gap.md
docs/research/project_knowledge_activation_orchestration/AO1_COMPLETENESS_MATRIX_V01.json
docs/research/project_knowledge_activation_orchestration/AO2_CONTROL_BOUNDARY_AND_FAILURE_TAXONOMY_V01.json

docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md
docs/OPEN_ARCHITECTURE_BACKLOG.md
docs/OPEN_QUESTIONS.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md

docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md
docs/research/168_q1_q2_q5_integrated_fresh_collaborator_result_and_revision_binding_amendment.md
docs/research/170_q4_real_workstream_concurrency_interruption_result.md
docs/research/178_mc0017_independent_w0_implementation_architecture.md
docs/research/179_mc0017_reconciled_w0_implementation_architecture.md
docs/research/205_w4_production_capture_promotion_acceptance.md

docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
docs/project_knowledge/architecture/whole_architecture.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/project_knowledge/architecture/migration_and_cutover.md

docs/model_collaboration/README.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
~~~

If an exact filename differs at that base, locate the corresponding numbered artifact by number/name without reading descendant candidate material.

You may inspect additional exact-base sources when they materially help answer the architecture question.

Do not restart broad web research unless a concrete architecture choice actually depends on current external evidence.

## 5. Independent review task

From the evidence above, independently determine the architecture you would choose for the activation/orchestration/self-hosting control plane.

Do not optimize for agreement with ChatGPT. Challenge whether the staged AO program itself is framing the problem correctly.

Address at least the following.

### A. Control-loop shape

Determine whether project interaction should be modeled as one closed control loop, staged escalation, several cooperating control loops, event-driven rules plus model interpretation, or another architecture. Explain which responsibilities should occur on every project event and which should activate only conditionally.

### B. Model-assisted versus project-controlled boundary

Define where probabilistic interpretation is appropriate and where behavior must become deterministic, fail-visible, or project-controlled. Pay special attention to natural-language intent, question versus directive, event classification, activation, authority, mutation permission, required review, preservation, resume, and architecture evolution.

### C. Activation versus search/reconstruction

Design how the system forces relevant governing, risk-bearing, procedural, and deferred knowledge into reasoning without reading the whole repository on every prompt, depending on owner path hints, turning search rank into authority, or creating one giant manually maintained registry.

Use the Chat 17, Chat 23, Chat 27 and Chat 28 failures as real falsification targets.

### D. Authority and action fidelity

Explain how consequential guidance/action remains subordinate to current governing source, exact revision/freshness, private dependencies when required, ordered constraints/prohibitions, and postconditions. Address both authority bypass and the separate failure where the right source is read but final guidance loses its contract.

### E. Process/workstream/Git routing

Integrate ordinary discussion/research, bounded implementation, independent review, capture/promotion, pause/resume, parent/child workstreams, interruption recovery, branch lifecycle, and publication/integration. Do not assume branch identity equals workstream identity.

### F. Collaboration/tool routing

Define when a second model or implementation agent should activate without making multi-agent activity mandatory. Manual owner transport may remain a transport mechanism. The owner should not have to remember which collaborator/process was required.

### G. Architecture evolution

Define how known risks/reopen triggers and newly observed failures challenge a frozen architecture without either freezing forever or self-modifying silently. Distinguish implementation conformance defects from genuine architecture change.

### H. Interaction continuity and break-glass

Design continuity across planned chat rotation, unexpected context loss, unpromoted but important reasoning, pending Claude/Codex handoff, partial repository mutation, runtime/tool failure, and degraded mode. Conversation state must not become project authority. Recovery must not depend exclusively on the failed component.

### I. Successor-before-authority-switch bootstrapping

Current continuity must remain operational authority until later W8 qualification, but the successor should ideally help execute the remaining migration.

Design how successor control behavior could become useful before the authority switch without creating dual authority, authority laundering, compatibility takeover, self-enabling successor state, or a new single point of failure.

If you believe successor control should not operate before W8, defend that alternative and explain how the remaining migration avoids owner-reminder dependency.

### J. Self-observation and obligation closure

Design how the architecture notices that the owner had to remind it of an existing mechanism, an accepted requirement never reached implementation, control behavior cannot explain why something activated, or branch/process drift recurs, and turns those into evidence without automatically changing architecture.

### K. Efficiency and complexity

Identify the smallest architecture that still satisfies the evidence. Challenge unnecessary logical records, too many control stages, too many persistent indexes, premature services/daemons, and excessive per-message work. Do not remove complexity required for correctness.

### L. Migration and self-hosting

Explain how this architecture can redesign itself across conversations, interruptions, implementation waves, authority migration, and rollback while preserving one explicit project authority.

### M. Implementation and qualification implications

Do not choose a technology stack unless architecture correctness requires it. Instead identify what must become executable, what may remain conceptual, what must be inspectable, what requires deterministic tests, what needs real historical regression, what requires independent review, and what should fail closed.

Call out accepted-obligation-to-realization gaps explicitly.

## 6. Required challenge output

Message 001 must also include:

1. the strongest alternative architecture considered;
2. the strongest criticism of the preferred architecture;
3. the three most dangerous failure modes;
4. the three highest-value simplifications;
5. anything in AO-1/AO-2 that seems over-scoped or missing;
6. what evidence would falsify the preferred architecture;
7. whether the successor should operate before W8 and under what exact authority relationship;
8. the minimal historical regression suite required before implementation;
9. any requirement/specification/backlog item that should be amended before implementation.

End with exactly:

~~~text
INDEPENDENT_CONTROL_PLANE_REVIEW_CONTAMINATED: YES|NO
PREFERRED_ARCHITECTURE_READY_FOR_COMPARISON: YES|NO
SUCCESSOR_CONTROL_BEFORE_W8: YES|NO
CURRENT_AUTHORITY_MUST_REMAIN_SOLE_SEMANTIC_AUTHORITY: YES|NO
MATERIAL_REQUIREMENTS_GAP_FOUND: YES|NO
MATERIAL_SPECIFICATION_028_AMENDMENT_REQUIRED_NOW: YES|NO
~~~

## 7. Required output

Write exactly one durable response at:

~~~text
docs/model_collaboration/threads/MC-0021/messages/001_claude_independent_control_plane_architecture.md
~~~

Include collaboration provenance and the exact independent base. Do not modify any other repository path.

## 8. After Message 001

After Claude's independent Message 001 is committed and pushed, ChatGPT will freeze a comparison request that intentionally exposes Research 222 through Research 226, their machine syntheses, and the exact integrated candidate target.

Claude will then perform an explicit comparative/adversarial review against its already-frozen independent position.

Until Message 001 exists, do not read those candidate artifacts.

~~~text
MC0021=OPEN
MODE=INDEPENDENT_THEN_COMPARATIVE
PHASE=CLAUDE_INDEPENDENT_CONTROL_PLANE_ARCHITECTURE
INDEPENDENT_BASE=b649c1a846d3bf9274fd718e0efd8de9d63bd990
CANDIDATE_TARGET=f73239ee486132a94701de80514ffd11480b9ecd
AO8=ACTIVE
AO9=BLOCKED_BY_AO8_REVIEW
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=CLAUDE_MESSAGE_001
~~~
