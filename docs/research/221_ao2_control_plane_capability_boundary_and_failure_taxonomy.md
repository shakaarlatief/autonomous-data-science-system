# Research 221: AO-2 Control-Plane Capability Boundary and Failure Taxonomy

**Date:** 2026-09-20
**Status:** AO-2 COMPLETE / AO-3 CONTROL-PLANE CONCEPTUAL ARCHITECTURE NEXT / W5-F0 REMAINS PAUSED
**Scope:** Reduce AO-1's 31 capability rows into the smallest architecture-neutral control responsibilities and behavioral failure taxonomy needed to design the activation/orchestration control plane without selecting an implementation stack.
**Program:** Research 219
**AO-1 input:** Research 220
**Machine synthesis:** `docs/research/project_knowledge_activation_orchestration/AO2_CONTROL_BOUNDARY_AND_FAILURE_TAXONOMY_V01.json`
**Authority:** Architecture-neutral research synthesis. This record does not select an implementation stack, accept the successor orchestration bridge, amend Research 218, or switch operational authority.

## 1. AO-2 purpose

AO-1 reconstructed 31 capability families. Treating those as 31 separate subsystems would reproduce the fragmentation problem.

AO-2 therefore asks a smaller question:

> What are the minimum distinct control responsibilities the project must satisfy, and what failure classes prove that those responsibilities are not working?

## 2. Eight control responsibilities

AO-2 collapses all 31 AO-1 rows into eight overlapping responsibilities.

### AO-R1 Project-event interpretation and explicit-intent boundary

Recognize what kind of project event occurred without requiring command syntax, while preserving explicit owner directives and exposing material uncertainty.

### AO-R2 Reconstruction and knowledge-activation closure

Select task-shaped context and force governing/risk-bearing/deferred knowledge into reasoning when applicability requires it. Search may nominate candidates but cannot define mandatory closure.

### AO-R3 Authority, action-contract and conformance gate

Resolve governing authority for consequential work, activate material constraints, and verify the proposed guidance/action remains conformant before dispatch.

### AO-R4 Process, workstream, recovery and Git-lifecycle routing

Choose the correct project process, maintain parent/child/return semantics, handle side incidents through independent recovery paths, and govern branch/publication lifecycle when relevant.

### AO-R5 Collaboration and tool routing

Choose SOLO/review/independent/adversarial/implementation/local-evidence topology according to consequence and evidence needs while keeping transport separate from routing policy.

### AO-R6 Preservation, promotion and interaction continuity

Distinguish ephemeral reasoning, interaction-durable non-authoritative continuity, capture/candidate material and promoted project authority.

### AO-R7 Self-observation, obligation closure and architecture evolution

Observe control-plane misses and pressure, reconcile accepted obligation -> implementation gate -> evidence -> operational realization, and classify architecture change without silent drift.

### AO-R8 Successor bridge and authority-transition safety

Allow successor control behavior to operate/qualify over current authority without implicitly becoming semantic authority.

## 3. Why responsibilities overlap

Some AO-1 capabilities intentionally map to more than one responsibility.

For example:

```text
known-risk activation
    belongs to reconstruction/activation
    and architecture evolution

context interruption
    belongs to workstream/recovery routing
    and interaction continuity

capability drift
    belongs to collaborator/tool routing
    and bridge/degraded-mode safety
```

The overlap is semantic, not duplication of authority. AO-3 should prefer one composable control loop over one service per row.

## 4. Owner/system boundary

AO-2 preserves the Chat 26/27 principle:

```text
OWNER
    supplies intent
    supplies observations
    makes genuinely normative/consequential project decisions
    may override inferred routing explicitly

SYSTEM
    interprets project event
    reconstructs/activates project knowledge
    chooses governed process
    chooses collaborator/tool topology
    enforces authority/conformance gates
    preserves the right evidence/continuation state
    observes its own control failures
```

The system must not convert inference into authority. The owner should not have to operate the routing machinery manually.

## 5. Manual transport is compatible with automated routing

A key boundary is:

```text
manual transport
    != manual orchestration
```

For example, the accepted Codex workflow may remain:

```text
system recognizes bounded implementation task
    -> selects Codex workflow
    -> prepares exact prompt/branch/contract
    -> owner manually relays prompt
```

The owner does not need to decide that Codex is appropriate merely because the actual transport remains manual.

This avoids turning optional direct-dispatch conveniences into architecture blockers.

## 6. Search, reconstruction and activation remain distinct

AO-2 freezes this conceptual distinction for AO-3:

```text
SEARCH
    nominate material relevant to a query

RECONSTRUCTION
    establish the bounded project state required for safe work

ACTIVATION
    force mandatory governing/risk/procedural knowledge into reasoning
    because the current event makes it applicable
```

Semantic retrieval can support all three, but only project-controlled policy may decide mandatory activation for consequential cases.

## 7. Deterministic/project-controlled boundary

AO-2 does not require deterministic natural-language understanding.

Model-assisted behavior may include:

```text
intent interpretation
event-class hypotheses
semantic relevance candidates
prior-knowledge nominations
draft routing explanation
```

Project-controlled/inspectable behavior must include:

```text
authority resolution
mandatory activation rules
required review gates
mutation permission
fail-closed conditions
source/revision closure
promotion authority
state/authority transition
```

When model classification uncertainty can change consequential routing, the uncertainty itself must be visible and resolved before action.

## 8. Failure taxonomy

AO-2 defines 18 failure classes so qualification tests behavior rather than merely file presence.

```text
AO-F01 EVENT_MISCLASSIFICATION
AO-F02 ACTIVATION_MISS
AO-F03 ACTIVATION_OVERREACH
AO-F04 AUTHORITY_BYPASS
AO-F05 CONTRACT_FIDELITY_LOSS
AO-F06 PROCESS_MISROUTE
AO-F07 COLLABORATION_MISROUTE
AO-F08 PRESERVATION_MISS
AO-F09 PREMATURE_AUTHORITY_PROMOTION
AO-F10 RESUME_TARGET_LOSS
AO-F11 RECOVERY_PATH_DEPENDENCY_FAILURE
AO-F12 EVOLUTION_TRIGGER_MISS
AO-F13 FROZEN_CONTRACT_DRIFT
AO-F14 OBLIGATION_REALIZATION_GAP
AO-F15 GIT_LIFECYCLE_DRIFT
AO-F16 CONTROL_OBSERVABILITY_GAP
AO-F17 BRIDGE_AUTHORITY_LEAK
AO-F18 OWNER_REMINDER_DEPENDENCY
```

## 9. The owner-reminder dependency is now an explicit failure class

AO-F18 is deliberately first-class:

> Correct project behavior occurs only after the owner remembers and names a mechanism or knowledge source that should have activated independently.

The 2026-09-20 AB-027/AB-031 incident is a direct example.

This converts the project's motivating frustration into something that can be tested and regressed.

## 10. Consequence-sensitive response classes

Not every miss should block all work.

AO-2 distinguishes responses such as:

```text
FAIL_CLOSED
FAIL_VISIBLE_AND_RECONSTRUCT
ROUTE_REPAIR
ROUTE_REPAIR_AND_EVIDENCE
REPLAN_CONTEXT
EVIDENCE_AND_REVIEW_TRIGGER
SCHEDULE_RECONCILIATION
BREAK_GLASS
CAPTURE_OR_RECOVER
EVIDENCE_REQUIRED
```

High-consequence authority/conformance failures fail closed. Lower-risk routing mistakes may be repaired and preserved as evidence without halting unrelated project work.

## 11. Architecture-evolution semantics

AO-2 preserves the distinction introduced in Research 219:

```text
CONFORMANCE DEFECT
CLARIFICATION
AMENDMENT
SUPERSESSION
REOPEN
```

A detected trigger opens evaluation. It does not automatically mutate frozen architecture.

This is important because self-observation must not become self-authorizing architecture change.

## 12. Obligation-to-realization closure becomes part of the control plane

Research 220's reconstruction-planner discovery exposed a gap not named explicitly in Research 219's opening capability list.

The project must be able to trace:

```text
accepted architecture/spec obligation
    -> scheduled implementation gate
    -> implementation evidence
    -> operational activation
```

AO-F14 `OBLIGATION_REALIZATION_GAP` covers the case where that chain breaks.

This is how the project should prevent another selected requirement from remaining indefinitely present in documents but absent from production behavior.

## 13. What AO-2 intentionally does not decide

AO-2 does not select:

```text
one central router service
LLM prompt format
event schema
rules engine
database
graph store
vector store
daemon
scheduled background worker
CLI syntax
interaction-envelope schema
trigger-storage schema
Git policy details
Claude/Codex scoring formula
```

Those are AO-3/AO-4/AO-5/AO-6 implementation/design questions.

## 14. AO-3 design constraints

Any AO-3 conceptual architecture must satisfy at least:

```text
1. ordinary natural language can enter the control loop
2. explicit owner directives remain overrides
3. task/event interpretation may be model-assisted
4. mandatory knowledge closure remains project-controlled
5. consequential work passes authority + conformance gates
6. process/collaboration routing is inspectable
7. manual transport remains allowed
8. non-authoritative interaction continuity is possible
9. owner reminders become testable failures, not normal control flow
10. architecture triggers open governed evaluation rather than auto-change
11. successor control behavior cannot imply authority switch
12. existing Candidate 01 substrate is reused unless evidence falsifies reuse
```

## 15. AO-2 disposition

```text
AO_2=COMPLETE
AO_1_CAPABILITIES_MAPPED=31_OF_31
CONTROL_RESPONSIBILITIES=8
FAILURE_CLASSES=18
OWNER_REMINDER_DEPENDENCY=FIRST_CLASS_FAILURE
OBLIGATION_REALIZATION_CLOSURE=CONTROL_REQUIREMENT
MANUAL_TRANSPORT_COMPATIBLE_WITH_AUTOMATIC_ROUTING=true
CONTROL_PLANE_IMPLEMENTATION=NOT_SELECTED
SUCCESSOR_ORCHESTRATION_BRIDGE=NOT_YET_ACCEPTED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
RESEARCH218=FROZEN_BASELINE_RETAINED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_3_CONTROL_PLANE_CONCEPTUAL_ARCHITECTURE
```
