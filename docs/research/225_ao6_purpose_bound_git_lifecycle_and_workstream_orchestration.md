# Research 225: AO-6 Purpose-Bound Git Lifecycle and Workstream Orchestration

**Date:** 2026-09-21
**Status:** AO-6 COMPLETE / PURPOSE-BOUND GIT LIFECYCLE SELECTED / LIVE BRANCH ROTATION REQUIRED / AO-7 NEXT
**Program:** Research 219
**Control-plane baseline:** Research 222 / Progressive Control Closure
**Evolution governance:** Research 223 / Governed Evolution Cases
**Interaction/recovery baseline:** Research 224 / Anchored Interaction Continuity and Independent Recovery
**Primary prior evidence:** AB-032, Checkpoint 267, Research 170, current workstream implementation, Continuity branch rules, Project Integration Boundary, P-030
**Machine synthesis:** docs/research/project_knowledge_activation_orchestration/AO6_GIT_WORKSTREAM_ORCHESTRATION_V01.json
**Scope:** Define when a project workstream should create, continue, rotate, freeze, resume, publish, integrate, retire, or exceptionally rewrite a Git branch, and integrate those decisions with workstream pause/resume/concurrency semantics without making branches semantic authority.
**Authority:** Architecture research synthesis. This record defines lifecycle policy and a current self-hosting disposition. It does not make Git branch names semantic identity, does not change the promoted integration boundary, does not authorize destructive history rewriting by default, and does not switch project-knowledge authority.

## 1. AO-6 design question

Candidate 01 already knows branch state that matters to continuity:

~~~text
active development branch
exact execution anchor
paused/frozen branch + head where required
promoted integration branch + exact commit
~~~

What it does not yet govern is:

> When should ADS create a new branch, remain on the current branch, rotate to a new execution lane, freeze or resume one, publish qualified commits, integrate a result, retire an obsolete ref, or rewrite history?

AO-6 selects **Purpose-Bound Git Lifecycle**.

The central distinction is:

~~~text
WORKSTREAM
    semantic project-control identity

BRANCH
    mutable Git execution carrier

COMMIT
    immutable implementation/evidence revision

PROMOTED INTEGRATION BOUNDARY
    separately governed accepted integration pointer
~~~

A branch is never a workstream identity and never project authority merely because work happened there.

## 2. Why branch-per-workstream is rejected

AO-6 does not select a universal one-workstream-one-branch rule.

A new branch is justified only when isolation has concrete value, for example:

~~~text
concurrent independent work
separate risk or experimental boundary
clean review / promotion unit
different integration target
long pause requiring an exact frozen resume lane
material branch-purpose drift
independence-sensitive implementation or review
incompatible mutation cadence
~~~

Sequential sub-stages with one coherent integration objective may remain on one branch.

This preserves simplicity while preventing branch structure from becoming accidental collaborator habit.

## 3. Branch purpose is project-controlled

Git can tell us:

~~~text
ref name
local head
upstream head
ancestor relationships
divergence
commit reachability
working-tree/index state
protection state
~~~

Git cannot tell us why a branch exists or whether its name/purpose still matches the active work.

AO-6 therefore introduces a logical **GitExecutionBinding**:

~~~text
repository
branch ref
exact base revision
current head
upstream / publication expectation
bounded branch purpose
related workstream(s)
target integration boundary when known
lifecycle disposition
mutability / freeze state
resume relationship when material
~~~

The record is operational control evidence, not semantic project authority. Natural project owners still own workstream meaning and integration authority.

## 4. Lifecycle actions

The control plane may select:

~~~text
CREATE
CONTINUE
ROTATE
FREEZE
RESUME
PUBLISH
INTEGRATE
RETIRE
REWRITE_EXCEPTION
~~~

These are lifecycle actions, not a required production enum.

### CREATE

Create a new branch from an exact known commit when a new execution lane is justified by isolation, concurrency, reviewability, risk, pause/resume needs, or a different integration target.

### CONTINUE

Continue the existing branch when its purpose still truthfully covers the current work, the integration target remains compatible, no independent concurrency/isolation need exists, no pause/freeze contract would be violated, and continuation does not mix unrelated promotion units.

### ROTATE

Create a successor branch at the exact current head and move active development routing to it when the old branch remains valid history but is no longer a good active execution carrier.

Typical triggers:

~~~text
branch purpose/name materially drifts from current work
workstream route changes while old lane should become historical
a dedicated paused lane must remain frozen
the branch accumulated unrelated future promotion units
continuation/review becomes harder because the active ref carries obsolete semantics
~~~

Rotation preserves commit history. It does not require rewriting it.

### FREEZE

A branch associated with paused/resumable work may be frozen at an exact head. Unrelated work must not advance that frozen ref merely for convenience.

### RESUME

Resume from the exact preserved branch/head when that remains compatible. If the original branch must remain frozen or the integration target materially changed, create an explicit continuation branch from a known base instead of silently moving the historical resume point.

### PUBLISH

Publish qualified committed work to the authorized remote. Publication improves independent recoverability but is not promotion.

### INTEGRATE

Move accepted work into its intended integration boundary only under the relevant authority, qualification, and target-head guards. Whole-branch merge is not automatically correct merely because a branch contains the desired change.

### RETIRE

Remove/archive a branch ref only after proving it is no longer required for active/resumable work and no unique durable history would become unreachable or operationally undiscoverable.

### REWRITE_EXCEPTION

History rewriting is permitted only as an explicit exceptional action when its concrete benefit exceeds its provenance/migration cost and all affected references can be handled safely.

## 5. Durability and promotion are different axes

AO-6 distinguishes:

~~~text
WORKTREE_ONLY
    mutable, not durable

LOCAL_COMMIT
    durable on one checkout
    not independently recoverable if that machine is lost

REMOTE_PUBLISHED_COMMIT
    independently recoverable through authorized remote
    still not promoted/accepted merely because it was pushed

PROMOTED_OR_INTEGRATED_REVISION
    accepted at a separately governed integration boundary
~~~

The architecture must never collapse commit == push == promotion. They are different events with different authority.

## 6. Publication policy

Qualified project-development commits should normally be published promptly enough that recovery does not depend on one local checkout.

Publication becomes strongly indicated when:

~~~text
a meaningful checkpoint/stage boundary is earned
a collaboration/review needs an exact shared SHA
planned interaction rotation is approaching
work is about to pause
a recovery-sensitive boundary has been reached
multiple qualified local commits are accumulating
another machine/actor must reconstruct exact state
~~~

Bounded local-only exceptions remain valid for sensitive/private material, deliberately disposable experiments, known incomplete/unsafe states where publication would create misleading durability, temporary repair/rewrite preparation, or another explicitly justified case.

An exception must be visible and bounded. "We forgot to push" is not a policy.

## 7. Unpublished accumulation is a control condition

AO-6 adds a Git lifecycle condition:

~~~text
QUALIFIED_UNPUBLISHED_ACCUMULATION
~~~

The exact threshold is not frozen here.

Evaluation should consider:

~~~text
number and importance of qualified commits
time / interaction boundaries crossed
recovery risk
external collaborator needs
whether the local-only state is intentional
whether the branch can still be published fast-forward safely
~~~

When triggered, the control plane should route to publication or an explicit local-only disposition.

## 8. Workstream integration

Git lifecycle decisions are downstream of workstream semantics, not substitutes for them.

### Workstream open

~~~text
new workstream/event
    ->
evaluate branch-isolation need
    ->
CONTINUE existing lane
or CREATE dedicated lane
~~~

### Pause

If a paused workstream has a dedicated branch:

~~~text
record exact branch + head
FREEZE
do not advance with unrelated work
~~~

If several logical workstreams intentionally share one branch, pausing one does not automatically freeze the whole branch. Its resume boundary must instead be preserved through exact commit/workstream receipts.

### Child side-route

A child/recovery/review workstream may share the parent branch when execution is sequential and one integration unit remains coherent.

Use a dedicated branch when the parent continues concurrently, the child is risky/experimental, the child requires independent review history, the child has a distinct promotion target, or the parent branch must remain frozen.

### Child completion

Branch completion does not imply parent completion.

The child result returns through an explicit workstream return edge:

~~~text
child result
    ->
review/conformance
    ->
integrate if required
    ->
close child
    ->
resume/re-evaluate parent
~~~

No merge is inferred merely because the child workstream closed.

## 9. Concurrent branches

When multiple branches advance concurrently:

~~~text
each lane binds an exact base
each lane has a declared purpose
each consequential integration revalidates the target head
stale-target integration fails closed
branch naming/order never decides priority
workstream graph and project authority decide readiness
~~~

Candidate 01's existing DAG/readiness logic remains the semantic substrate.

Git provides revision evidence. It does not decide which ready workstream is primary.

## 10. Pause/resume continuity

AO-6 reuses Research 170's real interruption result and AO-5 receipts.

A resumable workstream should be reconstructable from:

~~~text
workstream identity/state
exact execution anchor
branch/ref when material
exact durable commit
return condition
resume target
completed durable-step receipts
pending next step
~~~

A branch name alone is never sufficient resume state.

## 11. Integration and promotion safety

AO-6 preserves the Checkpoint 267 lesson:

> Do not merge a continuity branch wholesale merely because it contains a desired subproject change.

A branch can contain repository/governance work that is not appropriate for the target integration boundary.

Before integration:

~~~text
resolve exact desired delta / semantic owner
resolve target branch + target head
verify qualification evidence
verify source revision
verify target head has not moved unexpectedly
choose integration mechanism explicitly
perform postflight
~~~

The selected mechanism may be fast-forward, merge, cherry-pick, content-level migration, or another bounded method. AO-6 does not select one universal merge strategy.

## 12. Retirement and destructive cleanup

A branch may be retired only after proving:

~~~text
no active or paused resumable workstream requires the ref
no pending collaboration/review is bound to it
all required commits remain reachable through retained refs
exact historical provenance is preserved
current routing no longer points to it
specialized runbooks/automation do not still require it as a live branch
destructive expected-head/protection/default-branch guards pass
~~~

Historical files mentioning the old branch as historical evidence do not need to be rewritten merely because the branch is no longer active.

## 13. History rewriting policy

P-030 explicitly allows reconsidering historical Git structure. AO-6 evaluates that permission rather than treating either "never rewrite" or "always clean up" as dogma.

History rewriting may be justified for cases such as:

~~~text
secret/security purge
clearly disposable unshared experiment history
severe structural corruption
bounded pre-publication cleanup with no downstream references
other cases where provenance impact is fully controlled
~~~

For already-published, heavily referenced project-development history, rewriting carries a high burden because it can invalidate checkpoint SHAs, collaboration review targets, validation evidence, external links, synchronization anchors, resume points, and historical comparisons.

Default response to branch-purpose drift is therefore ROTATE or supersede the ref, not rewrite history.

## 14. Current branch audit

The live branch provides a direct AO-6 case.

Checkpoint 267 created:

~~~text
v1-source-vault-bootstrap-resume
base = v1-cockpit-design-exploration@04f2a907...
purpose = preserve Cockpit-era repository improvements while returning active work to Source Vault
~~~

Since then the same branch has carried materially different programs, including Source Vault continuation, Codexless/local-execution work, Git/GitHub connector qualification, repository integrity/governance, model-collaboration architecture, Candidate 01 project-knowledge redesign, W0-W5 migration work, and activation/orchestration AO-0 through AO-6.

The branch remains technically valid Git history, but its active name/purpose no longer truthfully describes the current work.

This is **BRANCH_PURPOSE_DRIFT**.

The drift is not evidence that the commit history itself is wrong.

## 15. Current history-rewrite disposition

AO-6 explicitly evaluates whether the long-lived current history should be rewritten.

Disposition:

~~~text
REWRITE_CURRENT_HISTORY = NO
~~~

Reason:

~~~text
the history is valid provenance
many checkpoints/validation/collaboration records bind exact commits/branch history
the current problem is active-ref purpose drift, not corrupt commit meaning
rewriting would create large reference migration cost
rotation solves the active-control problem with much lower risk
~~~

This is not preserving the old approach for convenience. It is a merits-based decision under P-030.

A future security/provenance defect could reopen this disposition.

## 16. Current self-hosting branch decision

AO-6 selects a live rotation at its own closure.

After Research 225 and its machine synthesis are committed on the current branch:

~~~text
freeze historical execution lane
    v1-source-vault-bootstrap-resume
    at exact AO-6 research head

create successor active branch
    v1-project-knowledge-activation-orchestration

base
    exact frozen AO-6 research head

update
    current_routing.active_development_branch
    Candidate 01 active workstream execution anchor
    CURRENT_STATE
    live collaboration routing index
~~~

Do not rewrite or delete the old branch during this transition.

The new name is deliberately bounded to Research 219's AO program. When AO-12 closes and the project returns to broader W5 migration, branch purpose should be reevaluated rather than allowed to drift indefinitely again.

This live rotation is the first self-hosting use of AO-6.

## 17. Branch-specific operational contracts

Some historical operational acceptance records are intentionally branch-specific.

Example:

~~~text
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
~~~

Its exact frozen contract names v1-source-vault-bootstrap-resume. AO-6 does not rewrite that historical qualification to pretend it covered a new branch.

After rotation:

~~~text
historical acceptance remains true for its exact tested branch
current dynamic Git capabilities may still operate if independently qualified
any branch-specific capability required for the new active lane must be requalified or generalized explicitly
~~~

This preserves empirical integrity.

## 18. Logical records

AO-6 adds conceptual records:

~~~text
GitExecutionBinding
    branch purpose + workstream/integration binding + exact Git state

GitLifecycleDecision
    event / evidence
    selected action
    alternatives rejected
    exact precondition revision/ref state
    publication/integration/retirement consequences

GitPublicationReceipt
    exact local head
    exact remote head
    fast-forward relation
    postflight state
~~~

These are control/evidence records, not new semantic authority stores.

Production schemas are deferred.

## 19. Progressive Control Closure integration

~~~text
S1 event interpretation
    -> workstream open/pause/resume/close, branch drift, unpublished accumulation,
       concurrent work, integration request, cleanup request

S2 bounded control context
    -> current workstream + branch/upstream/head/divergence/protection summary

S3 obligations
    -> CHECK_GIT_LIFECYCLE
    -> ROUTE_WORKSTREAM_TRANSITION
    -> PUBLISH / INTEGRATE / HOLD when policy requires

S4 reconstruction
    -> load workstream contract, integration boundary, relevant Git policy/history

S5 routing
    -> CREATE / CONTINUE / ROTATE / FREEZE / RESUME / PUBLISH /
       INTEGRATE / RETIRE / REWRITE_EXCEPTION

S6 authority
    -> exact mutation/integration/destructive authority and expected heads

S9 postflight
    -> publication receipt, workstream state, resume edge, branch retirement state,
       control observation if drift/accumulation recurs
~~~

## 20. Failure-class coverage

AO-6 directly strengthens:

~~~text
AO-F06 PROCESS_MISROUTE
AO-F10 RESUME_TARGET_LOSS
AO-F11 RECOVERY_PATH_DEPENDENCY_FAILURE
AO-F14 OBLIGATION_REALIZATION_GAP
AO-F15 GIT_LIFECYCLE_DRIFT
AO-F16 CONTROL_OBSERVABILITY_GAP
AO-F18 OWNER_REMINDER_DEPENDENCY
~~~

## 21. Explicit non-decisions

AO-6 does not select:

~~~text
one branch per workstream
one universal merge strategy
mandatory PR for every change
mandatory branch protection for every development lane
fixed numeric unpublished-commit threshold
automatic branch deletion
automatic force push
automatic history rewrite
production GitExecutionBinding schema
production workstream schema extension
remote branch cleanup program
W8 project-knowledge authority switch
~~~

Old remote branches may deserve a later cleanup audit, but AO-6 will not delete them opportunistically.

## 22. Regression consequences

Later AO-9/AO-10 qualification should include:

~~~text
same coherent work continues -> CONTINUE, no gratuitous branch
independent risky child workstream -> CREATE dedicated lane
dedicated workstream pauses -> FREEZE exact branch/head
parent continues while child is paused -> frozen child branch does not move
branch purpose drifts materially -> ROTATE without rewriting valid history
qualified local commits accumulate -> publication obligation surfaces
published commit -> not mistaken for promotion
child branch closes -> explicit return/integration edge, no inferred merge
target head moves before integration -> stale integration fails closed
retirement request with unique/referenced history -> deletion blocked
heavily referenced public branch with stale name -> rotation preferred over rewrite unless stronger evidence exists
current AO-6 self-hosting case -> old Source Vault-named branch freezes and new AO-purpose branch becomes active from exact same history
~~~

## 23. AO-6 disposition

~~~text
AO_6=COMPLETE
GIT_LIFECYCLE_MODEL=PURPOSE_BOUND_GIT_LIFECYCLE
WORKSTREAM_IDENTITY_EQUALS_BRANCH_IDENTITY=false
BRANCH_PER_WORKSTREAM_REQUIRED=false
BRANCH_PURPOSE_PROJECT_CONTROLLED=true
GIT_REF_STATE_FROM_GIT=true
PUBLICATION_DISTINCT_FROM_PROMOTION=true
QUALIFIED_UNPUBLISHED_ACCUMULATION=CONTROL_CONDITION
PAUSED_DEDICATED_BRANCHES_FREEZE=true
WHOLE_BRANCH_MERGE_INFERRED=false
HISTORY_REWRITE=EXCEPTION_ONLY
CURRENT_BRANCH_PURPOSE_DRIFT=OBSERVED
REWRITE_CURRENT_HISTORY=false
LIVE_BRANCH_ROTATION=REQUIRED_AT_AO6_CLOSURE
SUCCESSOR_ACTIVE_BRANCH=v1-project-knowledge-activation-orchestration
OLD_BRANCH_DELETE_NOW=false
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_7_SUCCESSOR_ORCHESTRATION_BRIDGE_DESIGN
~~~
