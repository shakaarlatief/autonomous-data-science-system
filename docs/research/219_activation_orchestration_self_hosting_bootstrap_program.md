# Research 219: Activation, Orchestration and Self-Hosting Bootstrap Program

**Date:** 2026-09-20
**Status:** ACTIVE / ARCHITECTURE RESEARCH PROGRAM OPEN / W5-F0 PAUSED BEFORE IMPLEMENTATION
**Selected knowledge architecture:** `PKA-CANDIDATE-01`
**Frozen W5 information architecture:** Research 218
**Current project-development authority:** current continuity architecture
**Source evidence packet:** `docs/research/project_knowledge_activation_orchestration/`
**Primary related backlog:** AB-022 through AB-027, AB-031, AB-032
**Primary frozen requirements:** KA-R07, KA-R09, KA-R10, KA-R45, KA-R48 and related reconstruction/workstream requirements
**Scope:** Determine and implement the missing project control/orchestration layer required so that relevant knowledge, process, collaborator, recovery path, preservation path, and architecture-evolution behavior activate from ordinary owner intent without depending on the owner remembering the architecture.

## 1. Why this program opens now

Research 218 froze the future W5 information architecture and opened W5-F0 production-navigation implementation.

Before W5-F0 mutation began, the owner challenged a more fundamental requirement:

> How will the project recognize when a frozen architecture should be reconsidered, and how will it know when to activate mechanisms such as Claude review without depending on the owner to remember them?

Repository reconstruction then exposed a live failure:

```text
AB-027 and AB-031 already existed
their content was directly relevant
ChatGPT did not activate them
the owner had to remind ChatGPT that the discussion existed
only then did reconstruction surface the prior knowledge
```

This is direct evidence that durability and explicit searchability are not sufficient.

The original redesign already required cognitive activation. The missing piece is the end-to-end control behavior connecting ordinary interaction to the substrate.

## 2. Research 218 is not silently unfrozen

Research 218 remains the frozen baseline for:

```text
physical information architecture
authoring responsibilities
item-carrier model
semantic-subject model
historical-navigation preservation
production navigation direction
```

Research 219 does not silently edit those choices.

Instead, this program investigates a missing operational control plane needed to use and evolve that architecture correctly.

If Research 219 later proves that Research 218 itself requires change, the change must be explicit and classified as KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN.

This program is therefore also the first deliberate exercise of the architecture-evolution discipline it seeks to formalize.

## 3. Central bootstrapping problem

The project currently has:

```text
CURRENT_OPERATIONAL_AUTHORITY = CURRENT_CONTINUITY_ARCHITECTURE
```

That transition invariant remains.

However:

```text
old authority remains authoritative
    !=
successor activation/routing mechanisms must remain dormant
```

If activation/orchestration stays off until authority switch, the same old interaction failures continue during the migration that is supposed to eliminate them.

The core research hypothesis is:

> The successor may need to become operational first as a control/orchestration bridge over the old authority while the old continuity architecture remains the source of project truth.

## 4. Two-plane model

### 4.1 Knowledge plane

```text
what is true
where it is owned
what is current
what is historical
what has authority
identity
provenance
semantic organization
migration
```

Candidate 01 already provides substantial capability here.

### 4.2 Control / orchestration plane

```text
what is happening now
what does the owner's input mean
what project event occurred
what knowledge must activate
what governing process applies
what risks / deferred triggers intersect
which collaborator / tool is appropriate
whether a workstream opens / pauses / resumes
whether something should be captured or promoted
whether architecture itself is being challenged
what evidence / receipt must remain
```

The intended project behavior requires both planes.

## 5. Owner-role requirement

The intended owner role is:

```text
project owner
source of intent
source of observations
decision authority where human judgment is genuinely required
explicit override authority
```

The architecture should minimize dependence on the owner as:

```text
workflow router
file-path memory
model scheduler
continuation transport
recovery-runbook operator
Git lifecycle monitor
known-risk reminder
architecture-backlog librarian
```

## 6. Activation is stronger than search

```text
SEARCH
    given a query, retrieve relevant material

RECONSTRUCTION
    establish safe project orientation / current governing state

ACTIVATION
    given what is happening now, force relevant governing,
    risk-bearing, deferred, or procedural knowledge into reasoning
    even when the owner did not name it
```

Potential activation inputs include:

```text
current owner intent
project event class
consequence
active workstream
current authority
known failure signatures
reopen triggers
tool/runtime state
branch state
collaboration need
interruption state
```

## 7. Existing substrate that must be reused

Research 219 should first assume reuse of existing Candidate 01 mechanisms unless falsified:

```text
source-owned declarations
authority resolution
risk_or_reopen_triggers
risk_obligation_index
workstreams / dependencies / pause-resume
capture / review / promotion
identity / transitions
persistent views
compatibility views
model-collaboration provenance
Git/source evidence
migration-state reconstruction
```

The program must not create a competing second knowledge/control system merely because the interaction layer is new.

## 8. Required repository-wide completeness audit

Before selecting implementation, perform a retrospective audit from Research 124 onward.

At minimum inspect:

```text
Research 124 and Requirements V0.2
Candidate 01 design/qualification research
Specification 028
Foundations referenced by the redesign
OPEN_ARCHITECTURE_BACKLOG
OPEN_QUESTIONS
DECISIONS
DEVELOPMENT_METHOD
continuity/reconstruction research
model-collaboration research/threads
local-execution recovery work
Git lifecycle work
all material later / future / reopen-if / defer-until /
when-pressure-appears / should-eventually statements
```

Classify each relevant capability/obligation:

```text
ALREADY_SOLVED
PARTIALLY_SOLVED
SUBSTRATE_EXISTS_BUT_BEHAVIOR_MISSING
DEFERRED_WITH_TRIGGER
UNSCHEDULED
OBSOLETE
REQUIRED_BEFORE_W6
REQUIRED_IN_THIS_BOOTSTRAP_STAGE
```

The audit must be broad enough that the project stops rediscovering these items one at a time through owner memory.

## 9. Initial capability families to evaluate

```text
intent / project-event recognition
knowledge activation
governing-authority activation
architecture-validity monitoring
known-risk / reopen-trigger monitoring
process routing
collaboration routing
interaction continuity
context-window / interruption recovery
nested workstream orchestration
Git lifecycle governance
break-glass operational recovery
preservation routing
reconstruction-quality evaluation
architecture self-observation
conformance-vs-reopen classification
```

The audit may add, merge, remove, or reframe these.

## 10. Candidate project-event classes

Do not reduce all owner input to task.

Candidate event classes include:

```text
question
observation
idea
problem report
investigation request
change request
preservation request
resume request
runtime failure
architecture contradiction
new requirement
repeated friction
external/upstream change
review result
unexpected validation result
```

The event taxonomy is not frozen.

## 11. Candidate control loop

Current research hypothesis:

```text
OWNER INPUT / PROJECT EVENT
        ->
INTENT + EVENT INTERPRETATION
        ->
ACTIVATION
        ->
PROJECT-CONTROLLED CLOSURE
        current authority
        governing procedures
        known risks / triggers
        workstreams
        relevant decisions/backlog/questions
        recovery constraints
        ->
PROCESS ROUTING
        answer / discussion / research / capture / implementation /
        architecture review / recovery / human decision
        ->
COLLABORATION + TOOL ROUTING
        ->
EXECUTION / REASONING
        ->
VALIDATION / CONFORMANCE
        ->
PRESERVATION / PROMOTION
        ->
CONTINUATION / RESUME RECEIPT
        ->
SELF-OBSERVATION / ARCHITECTURE-EVOLUTION FEEDBACK
```

This is a hypothesis only.

## 12. Model-assisted vs project-controlled behavior

Likely model-assisted:

```text
intent interpretation
event-class candidates
semantic relevance candidates
possible prior-knowledge matches
```

Must remain project-controlled / inspectable:

```text
governing authority
mandatory preflight
mutation permission
fail-visible conditions
required independent review
source closure
preservation class
state transition
authority transition
```

The exact boundary is a design question for this program.

## 13. Frozen-contract / architecture-evolution handling

The program must distinguish:

```text
CONFORMANCE DEFECT
    implementation violates frozen design

CLARIFICATION
    design is sound but wording is ambiguous

AMENDMENT
    bounded architecture change

SUPERSESSION
    accepted replacement of a prior design element

REOPEN
    foundational assumption requires renewed architecture research
```

Possible evidence triggers include:

```text
repeated exception
scale failure
reconstruction failure
authoring ambiguity
integrity/safety failure
new requirement
upstream/tool change
maintenance pressure
owner-observed recurring friction
```

A trigger does not automatically change architecture. It opens the appropriate governed evaluation path.

## 14. Collaboration routing

The program must formalize when collaboration is useful without turning use-more-models into a default.

Candidate routing factors:

```text
task/event class
consequence
uncertainty
novelty
implementation boundedness
independence value
adversarial-review value
machine-local evidence requirement
provider/tool availability
quota/capacity
```

Candidate role mapping:

```text
ChatGPT
    architecture / integration / orchestration / synthesis

Codex
    bounded implementation / repair

Claude
    independent architecture research / critique / second judgment

Claude Code
    independent reasoning + direct machine/repository evidence

no second model
    when extra collaboration has insufficient value
```

This must become reconstructable policy rather than owner memory.

## 15. Interaction continuity

Investigate a non-authoritative interaction envelope capable of recording:

```text
interaction ID
provider/environment/session
durable project anchor at entry
mode / purpose
workstream
unpromoted material present?
recoverability status
external collaborators
pending capture/review
return condition
last durable receipt
```

The envelope must not make conversational text canonical.

Candidate information classes:

```text
EPHEMERAL
INTERACTION-DURABLE / NON-AUTHORITATIVE
PROMOTED PROJECT KNOWLEDGE
```

## 16. Break-glass / degraded-mode recovery

Required principle:

> Recovery instructions must be accessible independently of the component whose failure they repair.

Candidate scenarios:

```text
Codexless/local runtime unavailable
GitHub access unavailable
private companion unavailable
provider quota exhausted
Claude unavailable
Codex unavailable
partial migration interrupted
```

Recovery should preserve and later resume the parent workstream.

## 17. Git lifecycle integration

AB-032 becomes part of this control-plane audit rather than isolated housekeeping.

The system should eventually reason about:

```text
branch create / continue / rotate / merge / archive / retire
commit/push cadence
bounded local-only exceptions
unpublished qualified-commit accumulation
local/remote divergence
branch staleness
handoff/recovery implications
```

## 18. Self-observation and activation-miss evidence

The project should be able to treat its own operating misses as qualification evidence.

The 2026-09-20 incident is the first explicit bootstrap case:

```text
relevant durable architecture knowledge existed
owner event made it relevant
assistant failed to activate it
owner reminder was required
repository search then recovered it
```

Potential future event type:

```text
ACTIVATION_MISS
```

The production representation is not selected yet.

## 19. Real regression suite

The program should build qualification from historical/real cases, including:

```text
runtime restart -> exact runbook activation
recurring problem -> known trigger activation without hint
architecture concern -> current architecture + related backlog activation
consequential architecture choice -> independent review when warranted
bounded implementation -> implementation workflow routing
runtime unavailable -> break-glass recovery
child workstream close -> deterministic parent resume
context limit -> non-authoritative interaction continuity
fresh continuation into evidence-rich active research -> stage-specific supporting evidence activates without owner path hints
unpublished qualified commits -> Git lifecycle warning
repeated frozen-design exceptions -> architecture reopen evaluation
```

## 20. Transitional self-hosting hypothesis

The most important transition hypothesis is:

```text
SUCCESSOR ORCHESTRATION BRIDGE

authority input
    CURRENT_CONTINUITY_ARCHITECTURE

activation/routing machinery
    successor control plane

mutation authority
    governed case-by-case

semantic authority
    remains current continuity architecture until later explicit switch
```

The bridge would allow successor mechanisms to operate during migration without violating the single-authority invariant.

This must be designed and empirically qualified before adoption.

## 21. Work program

```text
AO-0  source-evidence preservation
      COMPLETE for Chat 26/27 source evidence + Chat 28 continuation near-miss

AO-1  repository-wide retrospective completeness audit
      COMPLETE / Research 220 + machine-readable matrix/snapshots

AO-2  capability boundary and failure taxonomy
      COMPLETE / Research 221 + machine-readable responsibility/failure model

AO-3  control-plane conceptual architecture
      COMPLETE / Research 222 + Progressive Control Closure machine synthesis

AO-4  architecture evolution + frozen-contract governance
      COMPLETE / Research 223 + Governed Evolution Cases machine synthesis

AO-5  interaction continuity + interruption + break-glass design
      COMPLETE / Research 224 + Anchored Interaction Continuity and Independent Recovery

AO-6  Git lifecycle + workstream orchestration integration
      NEXT / governed branch lifecycle integrated with pause/return/resume semantics

AO-7  successor orchestration bridge design

AO-8  independent architecture review

AO-9  empirical historical-regression program

AO-10 bounded implementation and shadow/bridge qualification

AO-11 operational use during remaining W5 migration

AO-12 reconcile results back into W5 migration / cutover requirements
```

The work program may be refined after AO-1/AO-2.

## 22. Immediate sequencing change

Until Research 219 says otherwise:

```text
W5-F0_PRODUCTION_NAVIGATION_SUBSTRATE
    PAUSED_BEFORE_IMPLEMENTATION

Research 218
    REMAINS_FROZEN_BASELINE

Current operational authority
    CURRENT_CONTINUITY_ARCHITECTURE

Authority switch
    NOT ALLOWED

Immediate next work
    AO-6 GIT LIFECYCLE + WORKSTREAM ORCHESTRATION INTEGRATION
```

No production navigation-schema/view code should be mutated merely to keep the old sequence moving.

## 23. Success criterion

This program is not complete merely because the repository contains an intent classifier or another index.

A credible result must demonstrate that, for representative real project interactions:

```text
owner can express intent naturally
relevant governing/risk-bearing knowledge activates without manual hint
correct project process is selected
collaborator/tool routing is appropriate and inspectable
important unresolved interaction can survive interruption without becoming authority
known deferred triggers become actionable when conditions occur
parent/child workstreams resume deterministically
operational failures route into resilient recovery
frozen architecture can be challenged without silent drift
project behavior leaves inspectable receipts/evidence
owner is not required to remember the architecture to use it
```

## 24. Boundary

```text
RESEARCH219=ACTIVE
ACTIVATION_ORCHESTRATION_BOOTSTRAP=OPEN
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
FULL_CONTROL_PLANE_DESIGN=NOT_YET_SELECTED
CONCEPTUAL_CONTROL_ARCHITECTURE=PROGRESSIVE_CONTROL_CLOSURE
SUCCESSOR_ORCHESTRATION_BRIDGE=HYPOTHESIS
RESEARCH218=FROZEN_BASELINE_RETAINED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
AO_1=COMPLETE
AO_2=COMPLETE
AO_3=COMPLETE
AO_4=COMPLETE
AO_5=COMPLETE
NEXT=AO_6_GIT_LIFECYCLE_AND_WORKSTREAM_ORCHESTRATION_INTEGRATION
```
