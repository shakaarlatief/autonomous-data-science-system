# Research 224: AO-5 Anchored Interaction Continuity and Independent Recovery

**Date:** 2026-09-21
**Status:** AO-5 COMPLETE / INTERACTION CONTINUITY + INTERRUPTION + BREAK-GLASS MODEL SELECTED / AO-6 NEXT / W5-F0 REMAINS PAUSED
**Program:** Research 219
**Control-plane baseline:** Research 222 / Progressive Control Closure
**Evolution governance:** Research 223 / Governed Evolution Cases
**Primary evidence:** Source Evidence 001-003, AB-031, Continuity procedure, Research 107, Research 170, local-execution operations runbook, interaction-provenance convention
**Machine synthesis:** docs/research/project_knowledge_activation_orchestration/AO5_INTERACTION_CONTINUITY_AND_RECOVERY_V01.json
**Scope:** Define how unresolved interaction-local material, planned and unplanned context boundaries, interrupted execution, pending external handoffs and operational component failures remain recoverable without making conversation authoritative or making recovery depend exclusively on the failed component.
**Authority:** Architecture research synthesis. This record does not select a production envelope schema, transcript store, provider API, background monitor, break-glass connector, Git lifecycle policy, workstream schema extension, or authority switch.

## 1. AO-5 design question

The project already reconstructs canonical state from the repository. The missing problem is narrower and different:

> How can the system preserve enough continuity to survive interaction boundaries and operational failures when important material has not yet become canonical, without promoting chat history into project authority or depending on the owner to manually transport context?

The selected conceptual model is **Anchored Interaction Continuity and Independent Recovery**.

Its central rule is:

> Canonical project state is reconstructed from canonical project owners. Interaction continuity preserves only the additional non-authoritative state required to recover unresolved work, handoffs, or interruption boundaries.

This avoids both extremes:

~~~text
save every conversation forever
    -> noise, privacy pressure, duplicate truth, accidental authority

save nothing until promotion
    -> important unresolved reasoning disappears at context/session boundaries
~~~

## 2. Two distinct continuity planes

AO-5 separates:

~~~text
PROJECT CONTINUITY
    canonical/current project truth
    workstream state
    governing authority
    branch/revision evidence
    accepted decisions/specifications
    reconstructed from repository authority

INTERACTION CONTINUITY
    which interaction exists
    what bounded unresolved purpose/material remains
    whether content is recoverable
    pending handoff/review state
    last durable project anchor
    return/recovery condition
    non-authoritative by definition
~~~

Interaction continuity may point to project authority. It must not copy itself into authority.

## 3. Four information states

AO-5 refines the preservation boundary into four conceptual states:

~~~text
EPHEMERAL
    transient reasoning with no continuity value

INTERACTION_DURABLE_NON_AUTHORITATIVE
    unresolved material or continuity metadata must survive
    but is not yet accepted project knowledge

CAPTURE_OR_CANDIDATE
    material has crossed into the project knowledge lifecycle
    but remains non-authoritative pending review/promotion

PROMOTED_PROJECT_KNOWLEDGE
    accepted meaning is owned by a canonical semantic owner
~~~

Movement is explicit:

~~~text
ephemeral
    -> interaction-durable when interruption loss would matter

interaction-durable
    -> capture/candidate when project-level review is warranted

capture/candidate
    -> promoted only through existing Candidate 01 promotion governance
~~~

Conversation text never becomes canonical merely because it is preserved.

## 4. InteractionContinuityEnvelope

AO-5 selects a logical **InteractionContinuityEnvelope**.

It is a non-authoritative session/interaction record whose purpose is to tell a future actor whether anything beyond canonical project reconstruction matters.

Conceptually it can carry:

~~~text
interaction identity
provider/environment
visible conversation title
persistent vs disposable classification
durable project anchor at entry
current bounded purpose / mode
related workstream or route reference when material
unpromoted material present?
unresolved material class / short bounded description
content recoverability status
external collaborators / pending handoffs
pending review/capture/promotion
return/resume condition when material
last durable ContinuationReceipt
closure status
~~~

It should reference existing canonical owners rather than duplicate their current state.

The envelope is not required for every disposable interaction. No continuity record is a valid outcome when the interaction leaves no material unresolved state.

## 5. Content recoverability is separate from interaction existence

A critical invariant from AB-031 is:

~~~text
interaction known to exist
    !=
interaction content recoverable
~~~

AO-5 therefore requires explicit recoverability semantics.

Conceptual states include:

~~~text
NOT_REQUIRED
RECOVERABLE
PARTIALLY_RECOVERABLE
OWNER_RELAY_REQUIRED
UNAVAILABLE
UNKNOWN
~~~

The exact production enum is deferred.

Rules:

~~~text
repository marker cannot pretend unavailable chat content is recoverable
missing content must not be reconstructed from model memory as fact
owner relay is a valid recovery path when no stronger accessible source exists
canonical project work may continue without recovering old interaction
when the unresolved interaction material is not actually required
~~~

A new interaction should recover only the unresolved non-authoritative material needed for the current task.

## 6. ContinuationReceipt

AO-3 selected a logical ContinuationReceipt. AO-5 refines when it is required.

A receipt is warranted when an interaction boundary would otherwise make one or more of these ambiguous:

~~~text
what canonical boundary was definitely durable
what unresolved non-authoritative work remains
what external handoff/review is pending
what next return condition matters
whether execution was in flight
whether a recovery path is required
what content is and is not recoverable
~~~

A receipt is not a giant chat summary.

It should be bounded and anchor-first:

~~~text
durable project anchor
interaction/session provenance
reason for boundary
unresolved material marker
recoverability
pending handoff/review references
safe next recovery/reconstruction action
~~~

Canonical facts already owned elsewhere should be referenced, not recopied.

## 7. Planned rotation

Planned rotation remains governed by the existing chat-rotation preflight:

~~~text
PASS
HOLD
FAIL
~~~

AO-5 integrates it with Progressive Control Closure:

~~~text
rotation pressure / owner request / natural stage boundary
    ->
PRESERVE_INTERACTION_STATE obligation when needed
    ->
ensure canonical project boundary is durable
    ->
preserve unresolved interaction-only material through envelope/receipt
    ->
run public/private continuity preflight as required
    ->
close old persistent interaction
    ->
new interaction gets fresh provider-local identity/title
    ->
repository-first reconstruction
    ->
recover only required unresolved interaction material
~~~

A planned rotation does not require that every open thought be promoted. It requires that important unpromoted state be clearly marked as non-authoritative and recoverable enough for the intended continuation.

## 8. Unplanned context loss without mutation evidence

When a conversation ends unexpectedly and there is no evidence that a repository mutation may have been in flight:

~~~text
fresh interaction
    ->
new interaction identity/title
    ->
repository-first project reconstruction
    ->
inspect surviving interaction-continuity evidence
    ->
determine whether unresolved non-authoritative material matters
    ->
recover it if available and required
    ->
continue
~~~

The canonical repository boundary dominates any recollection of what the old conversation intended.

If no interaction receipt exists, the absence is itself evidence. Do not invent one after the fact from model memory.

## 9. Abnormal execution interruption

If repository/tool mutation may have been in flight, ordinary continuation is insufficient.

AO-5 reuses the accepted Research 107 / Continuity recovery sequence:

~~~text
inspect current HEAD
identify last independently trusted durable boundary
enumerate commits/files/actions actually completed
compare with intended staged plan where recoverable
classify apparent inconsistencies:
    EXPECTED / DEFERRED
    KNOWN DEFECT / PLANNED REPAIR
    INTERRUPTION RESIDUE
    NEW UNPLANNED DEFECT
repair only current-stage findings
rerun required verification
preserve recovery result when material
~~~

Routing rule:

> When evidence cannot establish that no mutation was in flight, prefer the abnormal-execution recovery path over optimistic ordinary continuation.

This protects against partially completed logical workflows being mistaken for completed transitions.

## 10. Pending external handoff

Manual collaboration/tool transport creates a special interruption state.

Example:

~~~text
system routes bounded implementation to Codex
    ->
owner manually relays prompt
    ->
primary interaction is waiting for external result
~~~

AO-5 requires that the waiting state be reconstructable when material:

~~~text
handoff purpose
exact bounded project/revision anchor
collaboration mode/role
external interaction/thread reference when known
result status: PENDING / RETURNED / ABANDONED / UNKNOWN
required return/review action
~~~

A handoff request is never completion evidence.

When the external result returns, it enters Progressive Control Closure as a new project event and must still pass review/conformance/preservation as applicable.

## 11. Break-glass independence principle

AO-5 freezes the resilience rule:

> A recovery procedure must not depend exclusively on the component whose failure it is intended to recover.

Break-glass therefore begins by identifying the **failure domain** and an **independent authority/access path**.

Conceptually:

~~~text
component/tool unavailable
    ->
classify operational incident
    ->
preserve parent project/workstream anchor
    ->
resolve recovery authority
    ->
prove recovery authority is reachable independently of failed component
    ->
execute bounded recovery
    ->
verify restored capability through fresh evidence
    ->
preserve materially new recovery evidence
    ->
return to parent route
~~~

Independent does not necessarily mean a different provider. It means the only path to the governing recovery procedure or essential recovery action is not the failed component itself.

## 12. Recovery authority versus recovery transport

AO-5 separates:

~~~text
RECOVERY AUTHORITY
    the governing runbook/procedure and constraints

RECOVERY TRANSPORT
    the currently available path used to read/execute that procedure
~~~

For example, if Codexless is unavailable, the authoritative public runbook may remain in Git while the transport could be a local checkout, GitHub-access path, or another available repository reader. The exact provider is not frozen here.

A fallback transport cannot invent a different recovery procedure merely because the preferred component is unavailable.

If no independent path can establish required recovery authority:

~~~text
RECOVERY_AUTHORITY_UNAVAILABLE
    -> fail visibly
    -> request the narrowest human assistance needed
    -> do not improvise destructive recovery
~~~

## 13. Degraded mode

Component unavailability does not always block the entire project.

AO-5 requires consequence-sensitive degraded mode:

~~~text
failed capability irrelevant to current task
    -> continue unaffected work

failed optional collaborator/tool
    -> reroute or continue SOLO if policy permits

failed required evidence/authority path
    -> affected consequential action blocks

failed private complement
    -> preserve public RESOLVED_PRIVATE status
       and mark freshness NOT_VERIFIED where appropriate

failed primary orchestration component
    -> use independent break-glass route if qualified
~~~

Degraded mode must never silently weaken mandatory authority, review, privacy, or conformance obligations.

## 14. RecoveryCase logical record

Material operational recovery may create a non-authoritative **RecoveryCase** evidence record.

Conceptually it can contain:

~~~text
incident/failure class
failed component/capability
parent project/workstream anchor
last trusted durable boundary
recovery authority source/revision
independent access path used
actions actually performed
verification evidence
residual uncertainty
result: RECOVERED / DEGRADED / BLOCKED / ABANDONED
return/resume target
new reusable lesson?
~~~

Routine transient failures do not require permanent case records. Preserve one when the incident materially affects continuity, exposes a new failure mode, changes a runbook, or provides qualification evidence.

## 15. Privacy and bounded preservation

AO-5 rejects automatic raw-transcript archival as the default continuity mechanism.

Rules:

~~~text
store only the least information needed for continuity
do not duplicate secrets/private coordinates into public continuity
route private continuity material to the accepted private layer
do not copy canonical project truth into interaction metadata unnecessarily
prefer semantic receipts over transcript dumps
retain provenance sufficient to distinguish who/where/when without making provider identity authority
~~~

Content recoverability can legitimately be UNAVAILABLE when preserving the content would violate privacy or when the product never exposed a durable access path.

## 16. Closure and garbage collection

Interaction continuity must not grow monotonically forever.

An envelope/receipt can close when:

~~~text
all material unresolved content was promoted/captured/rejected
or no longer matters to any active/resumable route

pending external handoffs are resolved/abandoned
recovery obligations are closed
canonical state contains everything needed for future work
~~~

Closed interaction metadata may remain as provenance when justified, but active reconstruction should not load it merely because it exists historically.

AO-5 selects the semantic need for closure, not a storage-retention schedule.

## 17. Relationship to AO-3 and AO-4

Progressive Control Closure integrates AO-5 as follows:

~~~text
S1 event interpretation
    -> recognize rotation, context loss, interruption, handoff return, runtime failure

S3 ControlObligationSet
    -> PRESERVE_INTERACTION_STATE
    -> ROUTE_RECOVERY
    -> REQUEST_OWNER_DECISION when content cannot otherwise be recovered

S4 reconstruction
    -> canonical project state first
    -> interaction continuity only when relevant

S5 routing
    -> planned rotation / unplanned recovery / abnormal execution /
       pending handoff / break-glass / degraded mode

S6 authority
    -> recovery procedure authority when consequential

S9 postflight
    -> ContinuationReceipt / envelope update
    -> RecoveryCase evidence
    -> parent resume
    -> ControlObservation if recovery or continuity failed
~~~

A new recovery failure or repeated continuity miss can feed AO-4 Governed Evolution Cases without automatically changing architecture.

## 18. Failure-class coverage

AO-5 directly strengthens:

~~~text
AO-F08 PRESERVATION_MISS
    material unresolved interaction state gets an appropriate durable path

AO-F09 PREMATURE_AUTHORITY_PROMOTION
    interaction continuity stays structurally/non-semantically non-authoritative

AO-F10 RESUME_TARGET_LOSS
    receipts preserve bounded return/recovery information

AO-F11 RECOVERY_PATH_DEPENDENCY_FAILURE
    independent recovery path is a first-class requirement

AO-F16 CONTROL_OBSERVABILITY_GAP
    boundary/recovery decisions are inspectable

AO-F18 OWNER_REMINDER_DEPENDENCY
    rollover/recovery behavior activates from event state rather than owner memory
~~~

It also supports AO-F04/AO-F05 by requiring recovery actions to use governing procedure authority rather than improvised fallback guidance.

## 19. Interfaces intentionally left for AO-6

AO-5 preserves but does not fully define:

~~~text
how parent/child workstream state is represented during incident side-routes
exact workstream transition operations for pause/return/resume
branch publication/rotation consequences of interruption
Git lifecycle policy for local-only or unpublished qualified commits
~~~

Those are AO-6 responsibilities.

AO-5 requires only that interaction/recovery continuity can reference the parent route and return condition without taking ownership of the workstream model.

## 20. Explicit non-decisions

AO-5 does not select:

~~~text
production InteractionContinuityEnvelope schema
production ContinuationReceipt schema
production RecoveryCase schema
raw conversation archive
provider conversation API
background context-window monitor
fixed token threshold for rotation
specific break-glass connector/provider
persistent transcript database
automatic owner-message export
workstream schema changes
Git lifecycle policy
successor bridge transport
authority switch
~~~

## 21. Regression consequences

Later AO-9/AO-10 qualification must include:

~~~text
planned rotation with no unresolved material
    -> no unnecessary interaction payload

planned rotation with unresolved design reasoning
    -> bounded non-authoritative receipt survives

unexpected context loss
    -> canonical state reconstructed first

interaction existence but content unavailable
    -> no fabricated recovery

Chat 28-style continuation
    -> stage-specific supporting evidence + unresolved interaction state recovered when required

abnormal mutation interruption
    -> intended vs completed work reconstructed from durable evidence

manual Codex/Claude handoff across chat boundary
    -> pending result does not become false completion

Codexless unavailable
    -> recovery authority reachable independently
    -> exact runbook route activated

failed optional collaborator
    -> safe degraded mode where policy permits

required authority/recovery evidence unavailable
    -> affected consequential action fails visibly

resolved private fact inaccessible
    -> remains RESOLVED_PRIVATE, not reset to unknown

completed continuity envelope
    -> does not remain permanently active
~~~

## 22. AO-5 disposition

~~~text
AO_5=COMPLETE
CONTINUITY_MODEL=ANCHORED_INTERACTION_CONTINUITY_AND_INDEPENDENT_RECOVERY
INTERACTION_CONTINUITY_AUTHORITY=NON_AUTHORITATIVE
CANONICAL_RECONSTRUCTION_FIRST=true
RAW_TRANSCRIPT_ARCHIVE_REQUIRED=false
INTERACTION_EXISTENCE_EQUALS_CONTENT_RECOVERABILITY=false
PLANNED_ROTATION_PREFLIGHT=REUSED
UNPLANNED_CONTEXT_LOSS=SUPPORTED
ABNORMAL_EXECUTION_RECOVERY=REUSED
MANUAL_HANDOFF_WAIT_STATE=SUPPORTED
BREAK_GLASS_INDEPENDENCE_REQUIRED=true
RECOVERY_AUTHORITY_SEPARATE_FROM_TRANSPORT=true
DEGRADED_MODE=CONSEQUENCE_SENSITIVE
INTERACTION_CLOSURE_REQUIRED=true
WORKSTREAM_DETAIL=DEFERRED_TO_AO6
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_6_GIT_LIFECYCLE_AND_WORKSTREAM_ORCHESTRATION_INTEGRATION
~~~
