# Research 222: AO-3 Progressive Control Closure Architecture

**Date:** 2026-09-21
**Status:** AO-3 COMPLETE / PROGRESSIVE CONTROL CLOSURE SELECTED AS CONCEPTUAL BASELINE / PROSPECTIVELY AMENDED BY AO-9 P7-D01 / W5-F0 REMAINS PAUSED
**Program:** Research 219
**Prior synthesis:** Research 221 / AO-2
**Machine synthesis:** `docs/research/project_knowledge_activation_orchestration/AO3_PROGRESSIVE_CONTROL_CLOSURE_V01.json`
**Scope:** Select a coherent conceptual control-plane architecture that connects ordinary project events to activation, routing, authority, collaboration, execution, preservation, resume and self-observation without selecting an implementation stack.
**Authority:** Architecture research synthesis. This record does not select a production event schema, router service, rules engine, daemon, database, model API, interaction-envelope schema, Git policy, bridge implementation or authority switch.

## 1. AO-3 design question

AO-2 established eight control responsibilities and eighteen behavioral failure classes. AO-3 must now answer:

> How can those responsibilities compose into one usable control architecture without creating either one giant opaque orchestrator or a separate subsystem for every capability row?

The selected conceptual answer is **Progressive Control Closure**.

The central idea is:

> Every observed project event enters one logical control cycle, but only a small ingress/control screen is universal. The system progressively activates additional obligations, reconstruction, authority, process, collaboration and preservation work only when the event and current project state justify it.

This preserves the owner-facing goal:

```text
owner expresses intent / observation
    ->
system determines what project control behavior is required
```

without requiring whole-repository reconstruction, all control mechanisms, automatic multi-model dispatch, or one monolithic hidden agent on every message.

## 2. The selected control cycle

```text
OWNER INPUT / OBSERVED PROJECT EVENT
        |
        v
1. EVENT INGRESS + EXPLICIT-INTENT BOUNDARY
        |
        v
2. BASELINE CONTROL CONTEXT
        |
        v
3. CONTROL-OBLIGATION SCREENING
        |
        +-----------------------------+
        | no additional obligations  |
        | low consequence / no state |
        +--------------+--------------+
                       |
                       v
                 ORDINARY FAST PATH

otherwise:
        |
        v
4. PROGRESSIVE RECONSTRUCTION + ACTIVATION CLOSURE
        |
        v
5. PROCESS / WORKSTREAM / COLLABORATION / TOOL ROUTING
        |
        v
6. AUTHORITY + ACTION-CONTRACT PREFLIGHT
        |
        v
7. REASONING / EXECUTION / MANUAL HANDOFF
        |
        v
8. PRE-DISPATCH OR PRE-MUTATION CONFORMANCE
        |
        v
9. POSTFLIGHT
        preservation / promotion
        workstream / resume
        Git-lifecycle consequences
        continuation receipt
        control-failure evidence
        architecture-evolution feedback
        |
        +-----------------------------+
        | new material control facts  |
        +--------------+--------------+
                       |
                       v
            bounded control re-evaluation
```

The numbered stages are logical responsibilities, not nine required services, processes or files.

## 3. Why the architecture is progressive rather than one-shot

A one-shot router is insufficient because the correct route may depend on knowledge discovered only after targeted reconstruction.

Example:

```text
owner says:
    "This keeps happening."

initial interpretation:
    REPEATED_FRICTION candidate

compact control state:
    identifies relevant workstream/domain

targeted reconstruction:
    surfaces a previously declared reopen trigger

result:
    ARCHITECTURE_EVOLUTION_EVALUATION becomes mandatory
```

The control plane therefore uses progressive closure:

```text
initial event interpretation
    -> initial obligation set
    -> targeted reconstruction / activation
    -> re-evaluate obligations when new material facts appear
    -> continue until mandatory obligations are satisfied,
       explicitly discharged, or fail-visible unresolved
```

This is not unbounded recursive reasoning. Another pass is justified only when new material control facts add, strengthen or resolve an obligation. A mandatory obligation may not silently disappear merely because a later model pass stops mentioning it.

## 4. Event ingress and explicit owner intent

The control plane accepts **project events**, not only tasks. Event sources may include owner messages, tool results, validator results, collaborator reviews, runtime failures, Git/repository observations, interruption signals and future external automation.

One owner message may contain more than one event facet. AO-3 does not require a single mutually exclusive event label.

Model-assisted interpretation may infer question/discussion, observation, idea, problem report, investigation request, change request, preservation request, resume request, runtime failure, architecture challenge, new requirement, repeated friction, review result, unexpected validation result or another event hypothesis.

Explicit owner instructions are preserved separately from inference. Examples include "do not modify anything", "ask Claude", "use Codex", "save this for later" and "only investigate".

These directives override inferred routing within the owner's legitimate project authority. They do not silently waive higher project invariants such as explicit authority-transition requirements, required evidence gates or fail-closed safety constraints.

If interpretation uncertainty can materially change consequential routing, that uncertainty must remain visible and be resolved before action.

## 5. Baseline control context

The control plane needs a **small current control context**, not full project reconstruction.

Candidate 01 already provides most of the substrate:

```text
current_state_core
workstream_graph
risk_obligation_index
source_catalog
subject_index
authority_index
identity/revision machinery
current compatibility authority surfaces
```

The baseline context should answer only what is needed to decide whether deeper work is required: current workstream/stage, current authority architecture, current boundary, relevant pending obligations, interruption/recovery state and material degraded-mode facts.

A later implementation may reuse already-fresh interaction-local state rather than reread durable files on every message. AO-3 freezes the semantic requirement for a bounded current context, not a per-message I/O algorithm.

## 6. Control-obligation screening

The central derived concept is a **Control Obligation Set**.

It is not project authority. It is an inspectable derived statement of what the current event requires before, during or after the task.

Conceptual obligation families include:

```text
RECONSTRUCT_CONTEXT
ACTIVATE_GOVERNING_KNOWLEDGE
ACTIVATE_RISK_OR_REOPEN_TRIGGER
RESOLVE_AUTHORITY
PRESERVE_ACTION_CONTRACT
ROUTE_PROJECT_PROCESS
ROUTE_WORKSTREAM_TRANSITION
ROUTE_COLLABORATION
ROUTE_TOOL
REQUIRE_REVIEW
ROUTE_RECOVERY
PRESERVE_INTERACTION_STATE
CAPTURE_OR_PROMOTE
CHECK_GIT_LIFECYCLE
EVALUATE_ARCHITECTURE_EVOLUTION
REQUEST_OWNER_DECISION
EMIT_CONTROL_RECEIPT
```

This is conceptual, not a frozen production enum.

Every obligation should explain why it activated, what evidence/state caused it, whether it is mandatory or optional, what satisfies it and what happens if it cannot be satisfied.

A low-consequence event may legitimately produce `NO_ADDITIONAL_CONTROL_OBLIGATIONS`. That is an explicit fast-path result, not evidence that no control evaluation occurred.

## 7. Hard predicates and model-assisted semantic triggers

AO-3 selects a hybrid trigger boundary.

Project-controlled or deterministic/inspectable predicates include missing/stale required authority, required private evidence unavailable, workstream state/return condition, required review gate reached, known reopen trigger observed, stale expected revision, runtime/tool availability facts and current authority-transition state.

Model-assisted semantic signals include repeated-friction wording, architecture-challenge semantics, bounded-implementation hypotheses, independent-judgment value, potentially durable observations and exploratory-versus-governed task hypotheses.

A model may nominate semantic conditions. Project-controlled policy determines whether they create mandatory obligations.

## 8. Progressive reconstruction and activation closure

When deeper context is required, the control plane delegates to the already-selected Candidate 01 reconstruction contract rather than inventing a second retrieval system.

The existing task classes remain:

```text
BROAD_CONTINUATION
NARROW_GOVERNED_TASK
EXPLORATORY_RESEARCH
```

The planner must be able to produce must-load orientation, must-load governing sources, mandatory risk/deferred-trigger sources, supporting evidence, negative/do-not-load guidance, freshness requirements, receipt requirements and fail/escalate conditions.

AO-3 adds one control-plane requirement:

> Reconstruction is complete only when the current mandatory control obligations have closure, not merely when enough documents were retrieved to answer the surface wording.

Search and semantic retrieval may nominate material. They do not decide mandatory closure.

### Supporting evidence versus governing authority

The Chat 28 near-miss demonstrates that a design task may require stage-critical supporting evidence even when that evidence is non-authoritative.

The reconstruction receipt therefore needs to distinguish conceptually:

```text
governing / mandatory authority
mandatory risk/procedure activation
supporting evidence required by the current task
optional evidence
intentionally latent material
```

This avoids both under-reading and treating supporting evidence as authority.

## 9. Process, workstream, collaboration and tool routing

Once obligation/reconstruction closure is sufficient, the system chooses the project route.

Candidate process families include ordinary answer/discussion, exploratory research, capture/preservation, governed change, bounded implementation, independent architecture review, adversarial review, human decision, workstream resume/transition, operational recovery and architecture-evolution evaluation.

The route decision must be inspectable.

Collaboration topology remains separate from transport:

```text
bounded implementation
    -> Codex implementation workflow
    -> manual owner relay may remain transport

consequential architecture formation
    -> independent/comparative review when policy requires it
    -> Claude may be selected
    -> manual owner relay may remain transport

routine bounded question
    -> SOLO
```

Manual handoff may suspend the cycle. The returned collaborator/tool result becomes a new project event. Completion is never inferred merely because a handoff was requested.

## 10. Authority, action contract and conformance

For consequential guidance or mutation, routing alone is insufficient.

The existing Candidate 01 authority machinery remains the control mechanism:

```text
AuthorityQuery
    -> deterministic authority resolution
    -> AuthorityReceipt
    -> activated ActionContract
```

Before action: resolve governing sources, bind required revisions/freshness/private state, activate constraints/prohibitions and establish mutation permission.

After a proposed consequential result exists but before dispatch/mutation: verify all mandatory constraints survive, ordered constraints remain ordered, prohibitions are preserved and required verification/postconditions remain present.

This two-sided gate addresses both AO-F04 `AUTHORITY_BYPASS` and AO-F05 `CONTRACT_FIDELITY_LOSS`.

## 11. Reasoning, execution and manual handoff

Execution may be ordinary reasoning, repository/tool inspection, governed repository mutation, Codex implementation handoff, Claude review handoff, recovery procedure, human-decision request or another bounded process.

The control plane selects the route. It does not require direct automation of every transport.

No execution path may infer that successful routing grants semantic authority.

## 12. Postflight

Control does not end after execution.

Postflight asks proportionately whether the intended action completed, required postconditions were verified, workstream state changed, a parent resume target became eligible, unresolved interaction knowledge needs preservation, capture/promotion is required, Git lifecycle became relevant, a known trigger became observed, a control failure occurred, or a continuation receipt must survive interruption.

Postflight is where preservation, resume and self-observation connect back into the same cycle.

## 13. Control self-observation

The control plane should be able to create evidence about its own misses.

```text
owner names a governing mechanism after system omission
    -> AO-F18 OWNER_REMINDER_DEPENDENCY candidate

required risk existed but was not activated
    -> AO-F02 ACTIVATION_MISS

event routed to wrong lifecycle
    -> AO-F06 PROCESS_MISROUTE

accepted obligation has no implementation/evidence path
    -> AO-F14 OBLIGATION_REALIZATION_GAP

system cannot explain what activated or stayed latent
    -> AO-F16 CONTROL_OBSERVABILITY_GAP
```

A control observation is evidence. It does not automatically modify architecture. Material observations feed AO-4 architecture-evolution governance.

## 14. Logical control records

AO-3 selects the following logical records as useful semantic boundaries. It does not select their storage representation or require each to become a persisted file/object.

```text
EventInterpretation
    explicit owner directives
    event/task hypotheses
    consequence/uncertainty relevant to routing

ControlObligationSet
    activated obligations + reasons + satisfaction/failure conditions

ReconstructionContract
    existing Candidate 01 contract

RouteDecision
    process, workstream transition, collaboration topology, tool/transport

AuthorityReceipt
    existing Candidate 01 receipt

ActionContract
    existing governing constraints

Execution / Handoff Receipt
    what was actually dispatched/performed and against what boundary

ContinuationReceipt
    enough bounded state to resume when interruption requires it

ControlObservation
    failure/pressure/trigger evidence for qualification/evolution
```

Derived control records are non-authoritative unless an existing canonical source explicitly owns the represented fact. Unique accepted understanding still crosses the normal capture/promotion boundary.

## 15. Candidate 01 substrate reuse

```text
Need                              Existing substrate

compact current orientation       current_state_core
workstream route/resume           workstream graph + workstream engine
governing authority               authority engine + authority index
known risks / obligations         risk_obligation_index
discovery                         source catalog + subject index
source continuity/provenance      identity + revision binding
action fidelity                   governing procedure / ActionContract
capture/promotion                 capture + PromotionPlan lifecycle
public/private safety             private dependency / leakage checks
migration authority boundary      current compatibility + migration contract
```

Known missing behavior remains explicit:

```text
production reconstruction planner surface
general event/control-obligation interpreter
architecture-evolution route
interaction-continuity envelope
Git lifecycle policy
successor bridge
empirical control-plane regression program
```

AO-3 does not solve those gaps by creating a parallel knowledge registry.

## 16. Responsibility coverage

```text
AO-R1  event ingress + explicit-intent boundary

AO-R2  obligation screening
       + reconstruction / activation closure

AO-R3  authority preflight
       + action-contract activation
       + pre-dispatch conformance

AO-R4  process/workstream/recovery/Git routing
       + postflight resume

AO-R5  collaboration/tool topology
       + handoff suspension/resume

AO-R6  postflight preservation
       + interaction continuity route

AO-R7  control observations
       + obligation-realization checks
       + architecture-evolution feedback

AO-R8  cross-cutting authority membrane over every stage
```

AO-R8 is deliberately cross-cutting rather than a final box.

## 17. Failure detection seams

```text
AO-F01 EVENT_MISCLASSIFICATION
    ingress / route comparison

AO-F02 ACTIVATION_MISS
AO-F03 ACTIVATION_OVERREACH
    reconstruction/activation closure

AO-F04 AUTHORITY_BYPASS
AO-F05 CONTRACT_FIDELITY_LOSS
    authority/conformance gate

AO-F06 PROCESS_MISROUTE
AO-F07 COLLABORATION_MISROUTE
    route decision / result review

AO-F08 PRESERVATION_MISS
AO-F09 PREMATURE_AUTHORITY_PROMOTION
    postflight / promotion boundary

AO-F10 RESUME_TARGET_LOSS
AO-F11 RECOVERY_PATH_DEPENDENCY_FAILURE
    workstream/recovery route + postflight

AO-F12 EVOLUTION_TRIGGER_MISS
AO-F13 FROZEN_CONTRACT_DRIFT
AO-F14 OBLIGATION_REALIZATION_GAP
AO-F16 CONTROL_OBSERVABILITY_GAP
    self-observation / reconciliation

AO-F15 GIT_LIFECYCLE_DRIFT
    Git route + postflight

AO-F17 BRIDGE_AUTHORITY_LEAK
    cross-cutting authority membrane

AO-F18 OWNER_REMINDER_DEPENDENCY
    cross-stage comparison between owner intervention
    and obligations that should already have activated
```

## 18. Fast path and escalation economics

AO-3 rejects running every mechanism on every prompt.

```text
LOW-CONSEQUENCE ORDINARY INTERACTION
    event interpretation
    + bounded control screening
    -> no additional obligations
    -> ordinary response

PROJECT-STATE-SENSITIVE INTERACTION
    + compact control context
    + targeted reconstruction

GOVERNED / CONSEQUENTIAL INTERACTION
    + authority
    + action contract
    + conformance

RECOVERY / EVOLUTION / INTERRUPTION
    + specialized route
```

Future implementation/qualification must demonstrate that ordinary events do not require whole-corpus scans, normal reconstruction does not require a full generated-view rebuild, optional retrieval failure cannot bypass mandatory closure, and deeper work activates for a stated reason.

## 19. Authority membrane and successor bridge boundary

Progressive Control Closure may route using current authority without becoming authority itself.

Until a later explicit switch:

```text
semantic authority
    CURRENT_CONTINUITY_ARCHITECTURE

successor control output
    derived / non-authoritative routing and control evidence

mutation authority
    case-specific under currently governing procedure/authority

authority switch
    false
```

Better routing is not a new truth owner, a control receipt is not automatically canonical project knowledge, successor activation is not compatibility-path overwrite, and bridge execution is not a W8 authority switch.

AO-7 will design the concrete bridge. AO-3 freezes only this membrane.

## 20. Interfaces deferred to later AO stages

AO-3 establishes interfaces without consuming later-stage scope.

AO-4 receives `ARCHITECTURE_EVOLUTION_EVALUATION_REQUIRED` and defines KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN governance.

AO-5 receives `INTERACTION_CONTINUITY_REQUIRED` and `RECOVERY_REQUIRED` and defines the non-authoritative envelope, context rollover and independent recovery path.

AO-6 receives `WORKSTREAM_TRANSITION_REQUIRED` and `GIT_LIFECYCLE_CHECK_REQUIRED` and defines detailed lifecycle policy/integration.

AO-7 designs the successor orchestration bridge over the authority membrane.

## 21. Explicit non-decisions

AO-3 does not select a central router service, microservices, event bus, daemon/background worker, LLM prompt format, production event schema, production ControlPlan schema, rules engine, graph/SQL/vector database, scheduler, automatic Claude/Codex dispatch, fixed collaborator scoring formula, interaction-continuity storage format, Git lifecycle rules, architecture-evolution schema, bridge transport or authority switch.

It also does not require one persistent ControlPlan artifact per message. Logical records may remain ephemeral unless preservation is justified.

## 22. Qualification consequences

Later AO-9/AO-10 qualification must test at least:

```text
ordinary question -> fast path without unnecessary expansion
"proceed" -> active route/resume reconstruction without owner file hints
runtime restart -> exact governing runbook activation
repeated friction -> known trigger activation without owner reminder
architecture design -> independent-review obligation when policy requires it
bounded implementation -> Codex workflow routing without owner reminder
runtime unavailable -> independent break-glass route
child workstream close -> deterministic parent resume
context-limit rollover -> unresolved non-authoritative continuity survives
fresh Chat 28-style continuation -> stage-specific supporting evidence activates
qualified unpublished commits -> Git lifecycle condition surfaces
frozen-design pressure -> evolution evaluation opens without silent mutation
```

Qualification must inspect both false negatives and false positives: missing required activation and unnecessary activation/context overreach.

## 23. AO-3 disposition

```text
AO_3=COMPLETE
CONCEPTUAL_ARCHITECTURE=PROGRESSIVE_CONTROL_CLOSURE
CONTROL_MODEL=CLOSED_LOOP_WITH_STAGED_ESCALATION
UNIVERSAL_HEAVY_PIPELINE=false
CONTROL_OBLIGATION_SET=SELECTED_LOGICAL_BOUNDARY
BOUNDED_REEVALUATION=REQUIRED_WHEN_NEW_MATERIAL_CONTROL_FACTS_APPEAR
FAST_PATH=ALLOWED_FOR_LOW_CONSEQUENCE_NO_ADDITIONAL_OBLIGATIONS
TASK_SHAPED_RECONSTRUCTION=REUSED
AUTHORITY_RESOLVER=REUSED
ACTION_CONTRACT=REUSED
CAPTURE_PROMOTION=REUSED
WORKSTREAM_ENGINE=REUSED
DERIVED_CONTROL_RECORDS=NON_AUTHORITATIVE_BY_DEFAULT
MANUAL_TRANSPORT=SUPPORTED
SUCCESSOR_BRIDGE=NOT_YET_DESIGNED
IMPLEMENTATION_STACK=NOT_SELECTED
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_4_ARCHITECTURE_EVOLUTION_AND_FROZEN_CONTRACT_GOVERNANCE
```

## 24. Prospective amendment accepted at AO-9 P7-D01

**Decision date:** 2026-09-22
**Owner disposition:** `AMEND`
**Evidence basis:** Research 227 AO8-E01, Research 228-234 AO-9 regression and reconciliation evidence
**Affected scope:** AO-3 pre-dispatch control path only

The owner accepts the narrowly supported AO8-E01 amendment. The original AO-3 architecture above remains the historical baseline; this section prospectively amends the transition from proposed result to normal conformance.

Before final dispatch or consequential mutation, the control plane MUST independently inspect the proposed output/action for consequential shape. Candidate shapes include:

```text
ordered operational/procedural steps
repository/tool/runtime mutation
frozen-design assertion or change
Git ref action
external dispatch or handoff
authoritative current-project assertion
```

If a relevant shape fires and sufficient `AuthorityReceipt` / `ActionContract` closure is absent, the cycle MUST re-enter bounded reconstruction/authority closure and then return to normal pre-dispatch conformance.

This screen is independent of the earlier S3 obligation classification. It exists specifically so an early event/control-classification miss cannot propagate unchallenged when the proposed result itself reveals consequential structure.

The amendment does **not**:

```text
replace event/state activation
infer owner mutation permission
authorize the proposed action
make derived control evidence authoritative
adopt other Arm-D-only refinements
require deep reconstruction for ordinary low-consequence output
```

AO-10 must qualify this amendment for precision, false-positive behavior and bounded read/tool cost, including negative controls proving that ordinary low-consequence explanation, topical adjacency and a question by itself do not trigger unnecessary authority closure.

```text
AO9_P7_D01=AMEND
AO8_E01=ACCEPTED_PROSPECTIVE_AMENDMENT
INDEPENDENT_OUTPUT_ACTION_SHAPE_REENTRY=REQUIRED
AO10_Q02=REQUIRED
RESEARCH222_AMENDED=true
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
