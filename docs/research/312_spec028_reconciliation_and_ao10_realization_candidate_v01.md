# Research 312: Specification 028 Reconciliation and AO-10 Realization Candidate V0.1

**Date:** 2026-09-24
**Status:** SPECIFICATION 028 RECONCILIATION V0.1 FROZEN / AO-10 REALIZATION CANDIDATE V0.1 FROZEN / MC-0029 INDEPENDENT REVIEW OPENED / NO PRODUCTION IMPLEMENTATION / NO PHYSICAL MIGRATION
**Parent program:** Research 219 activation/orchestration bootstrap and Research 240 whole-repository architecture evolution
**Accepted architecture inputs:** Research 256, Research 259, Research 272, Research 276, Research 309, Research 310, Research 311
**AO inputs:** Research 222 through Research 235
**Current implementation contract:** Specification 028
**Machine reconciliation:** docs/research/project_knowledge_activation_orchestration/AO10_SPEC028_RECONCILIATION_V01.json
**Independent review:** MC-0029
**Scope:** Reconcile every numbered section of Specification 028 against the accepted R5-R8 architecture and AO-3 through AO-9 decisions, derive a concrete AO-10 realization candidate without inheriting current implementation mechanisms by default, and freeze an independent-review target before any production mutation.
**Authority:** Research candidate only. Specification 028 remains current implementation/migration authority until an explicit prospective successor or amendment is accepted.

## 1. Why reconciliation precedes implementation

AO-10 was intentionally held because its concrete realization depended on architecture that was still being reconsidered. That reconsideration is now complete through R8-C:

~~~
R5      Product / Project Level-1 architecture
R6      bounded contexts and workspace directions
R7      Project information architecture
R8-A    exact physical target direction
R8-B    WMR-H V0.3 representation architecture
R8-C    WARRANT-F V0.2 assurance architecture
~~~

Specification 028 predates those decisions and mixes still-valid semantic contracts with older physical, representation, package, assurance, migration and compatibility choices. Implementing AO-10 directly from it would reintroduce the architecture-inheritance problem the owner explicitly rejected.

## 2. Reconciliation method

Every numbered Specification 028 section receives exactly one primary prospective disposition:

~~~
RETAIN
    semantic contract remains appropriate substantially as written

GENERALIZE
    core contract remains, but carrier/path/tool/representation specifics lose target status

AMEND
    bounded semantic or lifecycle change is required

SUPERSEDE
    target contract is replaced by accepted R5-R8/AO architecture

RETIRE_AFTER_SUCCESSOR_QUALIFICATION
    current mechanism remains a migration oracle or compatibility obligation
    until a qualified successor is explicitly released
~~~

The complete 46-section machine-readable matrix is frozen in AO10_SPEC028_RECONCILIATION_V01.json.

Disposition totals:

~~~
RETAIN                                  8
GENERALIZE                             15
AMEND                                   9
SUPERSEDE                              12
RETIRE_AFTER_SUCCESSOR_QUALIFICATION    2
TOTAL                                  46
~~~

## 3. Principal reconciliation results

The strongest retained semantics are:

~~~
path != identity
selective durable semantic identity
typed source-owned relations
selective joint authority only when irreducible
same-commit generated-view binding without self-reference
deterministic project-controlled authority resolution
public/private fail-visible behavior
no mass historical conversion
explicit qualified owner authority switch
~~~

The strongest generalized semantics are:

~~~
natural semantic ownership without a central copy store
identity transitions
selective temporal semantics
ActionContract semantics
source/revision/provenance binding
derived-view freshness and rebuildability
deterministic machine serialization where applicable
full rebuild and incremental refresh equivalence
capture != authority and explicit promotion
migration-unit parity/provenance/reference/rollback accounting
research evidence remains evidence until explicitly promoted
professional architecture documentation quality
~~~

Material amendments are required for:

~~~
overall purpose and target boundary
schema/profile inventory
definition versus machine-maintained workstream state
interruption/concurrency with monotonic revision history
reconstruction as one stage of AO-3 rather than the whole control architecture
derived SQLite/FTS query acceleration
architecture-documentation residency
cutover qualification scope
legacy non-goals that were old implementation choices rather than target invariants
~~~

Material supersessions include:

~~~
tools/project_knowledge as target home
the old package/module list
docs/project_knowledge target directory structure
embedded strict JSON Markdown declarations
the fixed old generated-view inventory
legacy CLI topology
legacy validation-layer topology
future use of the old W0-W8 migration sequence
historical W0/W1 gates as future target gates
legacy acceptance-state transitions and continuation
~~~

Two current mechanisms remain explicitly transitional:

~~~
current compatibility surfaces
current aggregate repository-integrity machinery
~~~

They remain migration oracles until qualified successor release and do not receive permanent target preservation rights.

## 4. Whole-Specification disposition candidate

The recommended AO-4 disposition for Specification 028 as a whole is:

~~~
SUPERSEDE
~~~

This does not mean Specification 028 was wrong. It means its implementation contract is now narrower and older than the accepted architecture.

Specification 028 should remain unchanged as historical and current transition authority until an accepted successor specification exists. The stronger path is a prospective successor contract rather than editing the old specification until its provenance becomes unclear.

Candidate successor role:

~~~
Integrated Project Development System
Realization, Assurance, Migration and Cutover Contract
~~~

A possible Specification 029 number is only a candidate direction. This research does not create or accept it.

## 5. AO-10 realization candidate V0.1

AO-10 should realize a cooperating Project-plane system rather than one monolithic project-knowledge package.

### 5.1 JW1 Project Development System

Target residency:

~~~
project/system/
~~~

JW1 is independently resolved from Product.

Its conceptual responsibilities are:

~~~
cold-start/bootstrap and project-anchor resolution
event ingress and event/intent interpretation boundary
baseline control context
Control Obligation Set evaluation
targeted reconstruction
deterministic authority resolution
AuthorityReceipt production
ActionContract derivation
process/workstream routing
collaboration/tool routing
interaction continuity and recovery
architecture-evolution routing
Git/workstream lifecycle orchestration
successor-bridge control
capture/promotion orchestration
generated orientation and query adapters
transition/migration orchestration
postflight and ControlObservation production
~~~

These are responsibility boundaries, not an instruction to create one Python module per line.

### 5.2 Project Engineering and Assurance

Target residency:

~~~
project/engineering/
~~~

This is the independently resolved Python project accepted at R8-C.

The deliberately small assurance kernel contains:

~~~
claim catalog
effective policy plus base-revision ratchet
gate evaluation
record validation
neutral result adapters
~~~

Engineering-owned capabilities outside the small kernel include:

~~~
verifier execution planning
repository-engineering validation
provider/host adapters
artifact/evidence publication adapters
delivery/release integration
deployment/recovery qualification
stochastic campaign management
~~~

Product and JW1 are not co-installed into Engineering merely to run assurance. Product and JW1 emit native results; Engineering adapts them consumer-side.

## 6. AO and WARRANT-F interface

AO and WARRANT-F remain distinct.

Logical AO request:

~~~
AssuranceRequest
    exact candidate subject/revision
    base revision when ratchet comparison applies
    intended consequence
    applicable profile
    activated claims
    required capability/trust constraints
    AO cycle or ActionContract reference
~~~

Logical assurance result:

~~~
AssuranceDecisionEnvelope
    exact subject binding
    effective policy revision
    evaluated claim set
    cited warrant/evidence references
    freshness/provenance result
    trust result
    decision = ADMIT | REFUSE | REVIEW_REQUIRED
    failures or unresolved conditions
~~~

Exact wire schema remains a realization detail after independent review.

Hard separations:

~~~
raw test success != admission decision
Engineering decision != workstream transition
AO transition != assurance evidence
delivery mutation != assurance policy
~~~

## 7. Integrated AO-10 control cycle

The production-oriented candidate cycle is:

~~~
OWNER / AGENT / EXTERNAL EVENT
    ->
EventInterpretation
    ->
BaselineControlContext
    ->
ControlObligationSet
    ->
ordinary fast path when no mandatory obligation fires
OR targeted reconstruction / authority closure
    ->
RouteDecision
    ->
AuthorityReceipt
    ->
ActionContract when consequence requires it
    ->
independent pre-dispatch output/action-shape screen
    ->
AssuranceRequest when consequence/profile requires admission
    ->
WARRANT-F decision
    ->
AO advance / hold / review route
    ->
governed execution or delivery
    ->
postcondition verification
    ->
preservation/promotion as required
    ->
ContinuationReceipt
    ->
ControlObservation
    ->
bounded architecture-evolution feedback
~~~

This makes the accepted AO-9 P7-D01 amendment executable rather than prose-only.

## 8. WMR-H realization mapping

Candidate physical representation follows the accepted writer/semantics/lifecycle model:

~~~
durable human Project knowledge
    Markdown

selective machine semantics on governed human carriers
    visible TOML metadata using the accepted JSON-compatible subset

human-authored Project-system instance policy
    TOML

machine-maintained durable Project control state
    sharded pretty JSON
    exact stale-write precondition
    monotonic revision line over committed history

bounded consequential receipts/evidence
    selective immutable individual JSON records

generated orientation
    bounded current.md / current.json
    derived, freshness-qualified, non-authoritative

query acceleration
    rebuildable SQLite / FTS

vector retrieval
    optional derived cache only
~~~

No canonical Project SQL database, canonical graph database or broad event-sourcing system is selected.

## 9. KA-R51 realization candidate

KA-R51 must become mechanically observable enough to qualify control misses without relying only on owner memory.

Candidate logical records:

~~~
ControlExpectation
    deterministic expectation from applicable project-controlled
    trigger/obligation/authority rules

ControlTrace
    obligations activated, discharged, deferred or unresolved

ControlObservation
    postflight comparison and control-failure evidence
~~~

Mechanical miss sources can include:

~~~
known deterministic trigger applicable but not activated
mandatory obligation computed but absent from route
pre-dispatch shape screen had to recover a missed earlier obligation
shadow successor disagrees with a qualified expected route
owner correction/reminder reveals a mandatory obligation that was applicable
at the prior bound snapshot
~~~

The last case requires exact prior-cycle binding. An owner correction must not automatically be labeled a system defect. Precision and false-positive burden are AO-10 qualification requirements.

## 10. KA-R52 realization candidate

KA-R52 eliminates the hidden state:

~~~
accepted MUST
but no known realization or governed deferral
~~~

Candidate logical record:

~~~
ObligationRealization
    obligation identity
    governing source/revision
    realization class
    responsible subsystem
    implementation/migration/procedure/decision target
    qualification/evidence path
    operational activation condition
    status
    explicit deferral reason plus reactivation condition when deferred
~~~

Physical ownership follows the natural governing source where practical. A derived obligation-realization index may exist for audit/search, but it contains no unique accepted truth.

This avoids a universal central requirements database while making accepted obligations mechanically traceable.

## 11. AO-6 branch-rotation obligation is revalidated, not blindly executed

Research 225 selected ROTATE under then-current workflow assumptions and exposed a local attach/switch capability gap.

R8-C now explicitly gives branch/PR/workflow mechanics no target preservation right. AO10-O01 therefore becomes:

~~~
reconstruct current Git/workstream state
re-evaluate the lifecycle obligation under provider/workflow-neutral architecture
qualify any required local attach/switch capability
perform only the currently justified governed transition
~~~

Historical ROTATE remains evidence, not automatic present mutation authority.

## 12. Current assurance/oracle transition

Current tests, checkers and workflows remain useful as:

~~~
invariant sources
migration oracles
negative evidence about current coupling/topology
~~~

Retirement sequence:

~~~
extract invariant
    ->
map to claim/warrant/verifier or explicit non-retention disposition
    ->
implement successor
    ->
shadow compare where applicable
    ->
qualify sensitivity/specificity and exact-subject behavior
    ->
explicit oracle-retirement decision
~~~

P-D4 current routing is the concrete exemplar.

## 13. Candidate realization lifecycle

The old future W0-W8 sequence is replaced by this candidate lifecycle:

~~~
AR0  contract reconciliation and AO-10 architecture freeze

AR1  independent architecture review plus owner disposition
     no production mutation

AR2  accepted target Project-system and Engineering environment skeletons

AR3  semantic kernel realization
     authority/action contracts
     WMR-H state/receipt primitives
     WARRANT-F kernel/result adapters
     KA-R52 traceability substrate

AR4  shadow control loop
     AO-3 control closure
     P7 output/action-shape screen
     KA-R51 observations
     no successor semantic authority

AR5  assurance/admission shadow integration
     exact subjects
     profiles
     missing/stale/contradictory behavior
     policy ratchet
     oracle comparisons

AR6  Authority-Preserving Successor Bridge SHADOW qualification
     fallback/recovery/conflict/continuity/Git lifecycle

AR7  ACTIVE_SUBORDINATE eligibility
     explicit current-authority-controlled enable decision
     provider/host qualification where required

AR8  broader semantic/file migration by responsibility
     loss-accounted and reference-safe

AR9  cutover candidate plus full production qualification

AR10 explicit owner authority-switch decision
~~~

These stages are a candidate control structure, not authorization to advance.

## 14. Independent review requirement

This candidate proposes:

~~~
whole-contract Specification 028 SUPERSEDE
a new integrated successor specification
concrete JW1 / Engineering boundaries
KA-R51 and KA-R52 realization mechanisms
replacement realization/migration lifecycle
~~~

That consequence level warrants independent design before owner acceptance or production implementation.

MC-0029 is therefore opened in INDEPENDENT_THEN_COMPARATIVE mode.

Claude's substantive evidence boundary is:

~~~
0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d
~~~

This contains accepted architecture through Research 311 but not Research 312. Claude may read MC-0029 routing/brief files for instructions but must derive Message 001 from the frozen base before inspecting this candidate.

## 15. Current boundary

~~~
SPEC028_RECONCILIATION_V01=FROZEN_CHATGPT_CANDIDATE
SPEC028_SECTION_COUNT=46
SPEC028_WHOLE_CONTRACT_DISPOSITION_CANDIDATE=SUPERSEDE

AO10_REALIZATION_V01=FROZEN_CHATGPT_CANDIDATE
AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
AO10_SHADOW_ACTIVATION_AUTHORIZED=false

MC0029=OPEN
MC0029_MODE=INDEPENDENT_THEN_COMPARATIVE
MC0029_INDEPENDENT_BASE=0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

SPECIFICATION028=CURRENT_UNCHANGED_AUTHORITY
CURRENT_ORACLES=RETAIN
FILE_LEVEL_MIGRATION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false
AUTHORITY_SWITCH_ALLOWED=false

NEXT=MC0029_CLAUDE_INDEPENDENT_SPEC028_AO10_DESIGN
~~~
