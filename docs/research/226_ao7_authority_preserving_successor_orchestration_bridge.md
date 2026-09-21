# Research 226: AO-7 Authority-Preserving Successor Orchestration Bridge

**Date:** 2026-09-21
**Status:** AO-7 COMPLETE / AUTHORITY-PRESERVING SUCCESSOR BRIDGE SELECTED / AO-8 INDEPENDENT REVIEW NEXT
**Program:** Research 219
**Control-plane baseline:** Research 222 / Progressive Control Closure
**Evolution governance:** Research 223 / Governed Evolution Cases
**Interaction/recovery baseline:** Research 224 / Anchored Interaction Continuity and Independent Recovery
**Git/workstream baseline:** Research 225 / Purpose-Bound Git Lifecycle
**Migration authority baseline:** Specification 028, migration_and_cutover.md, Research 165
**Machine synthesis:** docs/research/project_knowledge_activation_orchestration/AO7_SUCCESSOR_ORCHESTRATION_BRIDGE_V01.json
**Scope:** Define how successor activation/orchestration may become operational during the remaining migration while the current continuity architecture remains the sole project-development authority, without creating dual authority, bypassing current procedures, or implying W6/W8 cutover.
**Authority:** Architecture research synthesis. This record selects a conceptual bridge contract only. It does not activate the bridge in production, replace compatibility paths, select a physical host/runtime, change W5/W6/W8 gates, or switch project authority.

## 1. AO-7 design question

Research 219 identified the bootstrapping problem:

~~~text
old authority remains authoritative
    !=
successor activation/routing must remain dormant
~~~

If successor orchestration cannot be used until W8, the project must complete the migration using the exact interaction weaknesses the successor is meant to eliminate.

But if successor control simply starts acting as a new source of truth before W8, the project violates the single-authority invariant.

AO-7 resolves this with an **Authority-Preserving Successor Bridge**.

The bridge permits successor control behavior to operate over current authority while remaining structurally unable to promote its own derived control state into project truth.

## 2. Bridge invariant

The selected invariant is:

~~~text
CONTROL EXECUTION MAY MOVE EARLY
SEMANTIC AUTHORITY MAY NOT
~~~

During the bridge phase:

~~~text
event interpretation
activation
control-obligation formation
process routing
collaboration/tool routing
postflight/self-observation

    may be performed by successor control logic

but

current project truth
governing source selection
accepted procedure constraints
mutation permission
current compatibility contracts
authority transition

    remain governed by current project authority
~~~

The bridge is therefore subordinate control, not a second authority system.

## 3. Bridge state is separate from authority state

AO-7 selects explicit conceptual bridge modes:

~~~text
DISABLED
    successor control not participating

SHADOW
    successor computes plans/receipts for comparison only

ACTIVE_SUBORDINATE
    successor routing/control decisions may drive real project behavior
    but every consequential claim/action binds current authority

SUSPENDED
    bridge temporarily removed from the execution path
    current continuity path remains available
~~~

These modes do not include AUTHORITY_SWITCHED.

Post-W8 authority is a different architecture state governed by Specification 028. A bridge cannot self-promote into it.

A valid live state may therefore be:

~~~text
BRIDGE_MODE=ACTIVE_SUBORDINATE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
~~~

There is no contradiction because bridge mode describes who performs control processing, not who owns accepted project meaning.

## 4. Authority membrane

The bridge has a hard membrane between derived control and governing authority.

### Successor side may own

~~~text
EventInterpretation
ControlObligationSet
ReconstructionContract
RouteDecision
BridgeReceipt
ControlObservation
candidate interaction-continuity metadata
candidate Git lifecycle decision
~~~

These outputs are non-authoritative by default.

### Current authority side owns

~~~text
canonical/current project facts
current workstream state
current compatibility semantics
governing procedures
accepted decisions/specifications
required private authority/freshness
mutation permissions
authority transitions
~~~

The bridge may resolve and consume these facts. It may not redefine them.

## 5. Authority resolution through the bridge

The bridge does not hardcode "legacy files always win."

The current authority architecture already contains natural canonical owners, accepted procedures, migrated semantic owners, compatibility surfaces, and explicit hierarchy/transition rules.

For consequential work the bridge must:

~~~text
form the authority question
    ->
resolve against the currently authoritative source set
    ->
bind exact revision/freshness/private requirements
    ->
produce AuthorityReceipt
    ->
derive ActionContract
    ->
only then permit consequential guidance/action
~~~

Candidate 01's deterministic authority resolver may be used before W8 because a resolver is not itself authority. It is acceptable only when its admitted source set and precedence rules reproduce the currently governing authority contract.

If authority cannot be resolved, the bridge fails visibly. It may not use its own cached/derived state as emergency authority.

## 6. Current compatibility surfaces remain live

Until the later migration gates change their roles:

~~~text
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
~~~

retain their current contracts.

Bridge activation does not authorize successor generation to overwrite them.

The bridge may read them, route through them, update them through the same currently governed authored process when a legitimate project transition requires it, and compare successor projections against them.

That is different from declaring successor-generated replacements authoritative.

Therefore:

~~~text
bridge active
    !=
W6 cutover candidate

bridge active
    !=
compatibility path takeover

bridge active
    !=
W8 authority switch
~~~

## 7. Bootstrap direction

The bridge must be reachable from the current continuity architecture rather than requiring successor authority to bootstrap itself.

Conceptually:

~~~text
current repository bootstrap
    ->
current CONTINUITY / routing boundary
    ->
explicit qualified bridge-activation state
    ->
successor control loop
    ->
current authority membrane
~~~

This provides a safe bootstrap chain:

~~~text
old authority delegates bounded control processing
rather than
new control plane declaring itself active
~~~

The physical location of the bridge-activation flag/state is deferred to AO-10. It must be current-authority controlled and must not be writable only by the bridge itself.

## 8. Read path

The bridge read path is:

~~~text
owner/project event
    ->
bounded current control context
    ->
fresh successor derived views where useful
    ->
targeted reconstruction
    ->
current authority resolution
~~~

Derived views may accelerate discovery but never close authority by themselves.

If a successor view is stale, missing, or conflicts with current authoritative sources:

~~~text
do not average
do not silently repair
do not prefer successor because it is newer software

rebuild/fallback/reconstruct from current authority
or fail visibly when consequential closure is impossible
~~~

Research 168's stale-derived-authority behavior remains the model.

## 9. Write/action path

The bridge write path is:

~~~text
RouteDecision
    ->
AuthorityReceipt
    ->
ActionContract
    ->
existing governed mutation/tool/collaboration surface
    ->
precondition / expected-revision check
    ->
action
    ->
postcondition verification
    ->
current canonical/compatibility reconciliation when required
    ->
BridgeReceipt / ControlObservation
~~~

The bridge itself does not gain arbitrary repository-write authority merely because it selected the route.

A tool invocation, Codex handoff, Claude review, Git mutation, capture, promotion, or architecture-evolution action remains subject to its own governing contract.

## 10. Staleness and re-planning

Bridge decisions must be tied to an inspectable project snapshot.

A conceptual bridge decision carries enough binding to detect material drift, such as:

~~~text
repository / project boundary
source commit or exact source revisions where required
current workstream
current authority state
bridge mode/version
activated obligations
authority receipts used
expected mutation target revisions
~~~

If material current state changes before consequential dispatch:

~~~text
invalidate stale control plan
reconstruct/re-resolve
do not execute from old intent cache
~~~

The bridge may reuse interaction-local state only while its freshness assumptions still hold.

## 11. Conflict rule

If successor control state conflicts with current authority:

~~~text
CURRENT AUTHORITY WINS
BRIDGE DOES NOT AUTO-REPAIR AUTHORITY
CONTROL OBSERVATION IS EMITTED
~~~

Examples:

~~~text
bridge cache says checkpoint 561
current routing says checkpoint 562
    -> 562 governs; bridge cache is stale

successor view says workstream runnable
current governing dependency says blocked
    -> blocked

bridge suggests architecture amendment
frozen contract still governs
    -> open AO-4 EvolutionCase; no silent amendment
~~~

Repeated disagreement becomes qualification/evolution evidence.

## 12. Degraded mode and fallback

The bridge is not allowed to become a single point of failure for project continuity.

If the bridge is unavailable:

~~~text
current continuity bootstrap remains usable
current authoritative sources remain readable
recovery runbooks remain reachable independently
manual/current governed project operations remain possible
bridge can later reconstruct from durable evidence
~~~

If an optional successor acceleration layer fails, the bridge may fall back to canonical/current sources.

If a required authority source is unavailable, only the affected consequential action blocks.

This reuses AO-5's independent-recovery principle.

## 13. Bridge enable/disable governance

The bridge must not self-enable.

Conceptual transition:

~~~text
DISABLED
    ->
SHADOW after implementation exists

SHADOW
    ->
ACTIVE_SUBORDINATE only after bounded qualification
    + explicit current-authority-controlled enable decision

ACTIVE_SUBORDINATE
    ->
SUSPENDED on material control failure, integrity failure,
or explicit governed disable decision

SUSPENDED
    ->
SHADOW or ACTIVE_SUBORDINATE only after repair/requalification
~~~

AO-10 will define the exact qualification/activation mechanism.

AO-11 may use ACTIVE_SUBORDINATE during the remaining W5 migration only after AO-10 qualifies it.

## 14. No authority laundering

AO-7 explicitly prohibits authority laundering.

Forbidden pattern:

~~~text
model inference
    ->
BridgeReceipt
    ->
treated as project fact because bridge emitted it
~~~

Also forbidden:

~~~text
successor derived view
    ->
copied into live compatibility file
    ->
treated as authority without migration gate
~~~

Accepted pattern:

~~~text
derived control observation
    ->
capture/review when durable meaning is warranted
    ->
promotion into natural canonical owner
    ->
future authority resolution may then use it
~~~

The existing capture/promotion lifecycle remains the only path from non-authoritative control evidence to accepted project knowledge.

## 15. BridgeReceipt

AO-7 selects a logical **BridgeReceipt** for inspectability.

Conceptually:

~~~text
bridge mode/version
event/control-cycle identity
bounded project snapshot
explicit owner directives
activated obligations
route selected
authority receipt references
action contract reference
execution/handoff result
postconditions
fallback/degraded behavior
control observations
authority state before/after
authority switch requested? false unless separately governed
~~~

BridgeReceipt is evidence, not project authority.

Not every low-consequence fast-path interaction needs a persistent receipt. Persistence is proportional to consequence, recovery value, and qualification need.

## 16. Owner decision rights

The bridge may automate routing where policy is already established.

It must still request owner judgment for genuinely normative decisions, including:

~~~text
architecture KEEP / AMEND / SUPERSEDE / REOPEN where AO-4 requires it
authority switch
material objective/trade-off decisions
other explicit human-decision gates
~~~

The bridge should reduce owner workflow memory, not remove owner decision authority.

## 17. Collaboration/tool routing

The bridge may select:

~~~text
SOLO
Codex bounded implementation
Claude independent review
Claude Code / machine-evidence review
recovery tool path
human decision
~~~

Selection does not imply transport automation.

Manual owner relay remains compatible where that is the accepted transport, but the owner should receive a bounded, already-routed handoff package rather than having to remember which collaborator or process was needed.

Returned external results re-enter the bridge as new project events.

## 18. Git/workstream integration

AO-6 remains subordinate input to the bridge.

The bridge may detect:

~~~text
branch-purpose drift
qualified unpublished accumulation
workstream pause/resume
child workstream close
concurrent lane
integration request
retirement request
~~~

and route the appropriate Git lifecycle obligation.

The current branch attach/switch realization gap remains visible. The bridge must not claim that ROTATE completed merely because a remote branch could be created.

## 19. Relationship to W5-W8

### During remaining W5

Bridge can be shadow-qualified and later ACTIVE_SUBORDINATE while:

~~~text
Research 218 remains frozen baseline
W5 semantic migration continues
current continuity remains authority
live compatibility paths remain under current contracts
~~~

### W6

W6 cutover-candidate rules are unchanged. Bridge operation before W6 does not satisfy W6.

### W7

W7 must include bridge behavior in production qualification, including authority leakage, fallback, stale-view conflict, interruption, provider/tool portability and rollback.

### W8

Only W8 may change:

~~~text
CURRENT_OPERATIONAL_AUTHORITY
AUTHORITY_SWITCH_ALLOWED
~~~

After W8, the subordinate bridge architecture may be retired, simplified, or transformed. AO-7 does not pre-decide the post-switch shape.

## 20. Rollback

Bridge rollback is simpler than authority rollback because the bridge owns no unique semantic truth.

To suspend the bridge:

~~~text
disable/suspend bridge control path
preserve bridge evidence needed for diagnosis
return project interaction to current continuity path
verify current authority surfaces remain intact
resume only after requalification
~~~

No semantic reverse migration should be necessary merely to disable the bridge.

This is a major safety advantage of keeping bridge outputs non-authoritative.

## 21. Qualification obligations for AO-10

At minimum test:

~~~text
ordinary low-consequence event
    -> bridge fast path, no unnecessary heavy reconstruction

"proceed"
    -> bridge reconstructs active route from current authority

stale successor view conflicts with current routing
    -> current authority wins

bridge-derived control record conflicts with canonical source
    -> control record loses

known reopen trigger intersects owner event
    -> AO-4 evaluation route activates

bounded implementation request
    -> correct Codex route selected without owner reminder

independent review condition
    -> correct Claude route selected

bridge unavailable
    -> current continuity fallback works

required current authority unavailable
    -> consequential action fails visible

bridge restarts after interruption
    -> reconstructs from durable current state/receipts

capture-worthy bridge observation
    -> remains non-authoritative until review/promotion

branch rotation requested
    -> missing attach/switch surface remains visible until actually realized

attempted authority switch through bridge
    -> blocked

bridge enable/disable
    -> no live compatibility corruption

private complement unavailable
    -> public RESOLVED_PRIVATE state not reset; required freshness handled correctly
~~~

## 22. Historical regression coverage

The bridge design directly addresses:

~~~text
Chat 17 exact runbook existed but did not activate
Chat 23 Claude collaboration process existed but did not activate
known architecture reopen triggers required owner rediscovery
Chat 27 AB-027 / AB-031 activation miss
Chat 28 stage-specific evidence packet required owner path reminder
AO-6 current branch-purpose drift required explicit lifecycle recognition
~~~

AO-9 will formalize these into the empirical regression program.

## 23. Failure-class coverage

AO-7 is the principal design response to:

~~~text
AO-F02 ACTIVATION_MISS
AO-F03 ACTIVATION_OVERREACH
AO-F04 AUTHORITY_BYPASS
AO-F05 CONTRACT_FIDELITY_LOSS
AO-F06 PROCESS_MISROUTE
AO-F07 COLLABORATION_MISROUTE
AO-F08 PRESERVATION_MISS
AO-F10 RESUME_TARGET_LOSS
AO-F11 RECOVERY_PATH_DEPENDENCY_FAILURE
AO-F12 EVOLUTION_TRIGGER_MISS
AO-F14 OBLIGATION_REALIZATION_GAP
AO-F15 GIT_LIFECYCLE_DRIFT
AO-F16 CONTROL_OBSERVABILITY_GAP
AO-F17 BRIDGE_AUTHORITY_LEAK
AO-F18 OWNER_REMINDER_DEPENDENCY
~~~

AO-F17 is the defining bridge falsifier.

## 24. Explicit non-decisions

AO-7 does not select:

~~~text
physical bridge service/process
daemon
event bus
database
LLM prompt format
bridge enable-state storage schema
provider-specific chat hook
automatic Claude/Codex transport
production BridgeReceipt schema
production EventInterpretation schema
rules-engine technology
background polling cadence
W6 cutover implementation
W8 authority switch
post-W8 architecture
~~~

Those belong to AO-10 implementation or later migration/cutover stages.

## 25. AO-7 disposition

~~~text
AO_7=COMPLETE
BRIDGE_ARCHITECTURE=AUTHORITY_PRESERVING_SUCCESSOR_BRIDGE
BRIDGE_CAN_OPERATE_BEFORE_W8=true
BRIDGE_OUTPUT_AUTHORITY=NON_AUTHORITATIVE_BY_DEFAULT
BRIDGE_MODES=DISABLED|SHADOW|ACTIVE_SUBORDINATE|SUSPENDED
BRIDGE_SELF_ENABLE=false
CURRENT_AUTHORITY_GATE_REQUIRED_FOR_CONSEQUENTIAL_ACTION=true
SUCCESSOR_VIEW_CAN_CLOSE_AUTHORITY_BY_ITSELF=false
CURRENT_AUTHORITY_WINS_ON_CONFLICT=true
COMPATIBILITY_PATH_TAKEOVER=false
W6_SATISFIED_BY_BRIDGE=false
W8_SATISFIED_BY_BRIDGE=false
BRIDGE_FALLBACK_TO_CURRENT_CONTINUITY=REQUIRED
BRIDGE_RECEIPT=SELECTED_LOGICAL_RECORD
NO_AUTHORITY_LAUNDERING=true
AO6_BRANCH_ATTACH_GAP_REMAINS_OPEN=true
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_8_INDEPENDENT_ARCHITECTURE_REVIEW
~~~
