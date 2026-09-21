# Research 223: AO-4 Architecture Evolution and Frozen-Contract Governance

**Date:** 2026-09-21
**Status:** AO-4 COMPLETE / GOVERNED EVOLUTION PATH SELECTED / AO-5 NEXT / W5-F0 REMAINS PAUSED
**Program:** Research 219
**Control-plane baseline:** Research 222 / Progressive Control Closure
**Primary prior evidence:** Foundation 014, Research 124, AB-027, Research 220, Research 221
**Scope:** Define the control semantics that classify trigger evidence against frozen architecture, preserve owner decision authority, govern prospective KEEP/CLARIFY/AMEND/SUPERSEDE/REOPEN outcomes, and connect accepted evolution decisions to realization and qualification without retroactively rewriting historical acceptance.
**Machine synthesis:** docs/research/project_knowledge_activation_orchestration/AO4_ARCHITECTURE_EVOLUTION_GOVERNANCE_V01.json
**Authority:** Architecture research synthesis. This record defines how trigger evidence opens and resolves architecture-evolution evaluation. It does not itself amend Research 218, select an implementation schema, create a background monitor, or switch operational authority.

## 1. AO-4 design question

AO-3 can emit an obligation equivalent to EVALUATE_ARCHITECTURE_EVOLUTION. AO-4 must define what happens next without allowing either of these failure modes:

~~~text
frozen forever
    -> evidence accumulates but architecture cannot adapt

self-modifying architecture
    -> an observed trigger silently changes accepted design
~~~

The selected answer is **Governed Evolution Cases**.

A trigger opens an evaluation case. The current frozen contract remains authoritative unless and until a governed disposition changes the affected scope.

## 2. Core invariant

~~~text
TRIGGER OBSERVED
    !=
ARCHITECTURE CHANGED
~~~

Instead:

~~~text
trigger / pressure / contradiction
    ->
bind evidence to affected accepted contract
    ->
classify implementation defect vs architecture question
    ->
evaluate impact and required review
    ->
explicit disposition
    ->
prospective realization
    ->
qualification of affected scope
    ->
close with evidence
~~~

The default is preservation of the accepted contract, not silent thawing.

## 3. Trigger sources

An evolution case may be nominated by:

~~~text
source-owned known risk / reopen trigger
risk_obligation_index intersection
control-plane failure observation
repeated owner-observed friction
reconstruction or activation failure
validation / integrity failure
scale or maintenance pressure
new requirement
upstream/tool/provider change
new empirical evidence
security/safety concern
repeated exception pressure
obligation-realization gap
explicit owner architecture challenge
~~~

The source may be an owner message, tool result, validation result, collaborator review, periodic reconciliation, or other project event.

No background daemon is required by AO-4. Trigger evaluation must be activatable both event-driven and at meaningful reconciliation boundaries.

## 4. Trigger state versus architecture disposition

AO-4 keeps two concepts separate.

### Trigger state

A source-owned trigger may conceptually be:

~~~text
NOT_OBSERVED
PARTIAL
OBSERVED
SUPERSEDED
~~~

These states describe evidence about the trigger condition. They do not define the architecture response.

### Architecture disposition

The evaluation result is one of:

~~~text
CONFORMANCE_DEFECT
KEEP
CLARIFY
AMEND
SUPERSEDE
REOPEN
~~~

A trigger can be OBSERVED and still result in KEEP if evidence shows the accepted architecture remains appropriate despite the pressure.

## 5. First split: defect or architecture question

Before changing architecture, ask:

> Is the observed problem caused by failure to conform to the accepted design, or by evidence that the accepted design itself needs reconsideration?

### CONFORMANCE_DEFECT

Use when:

~~~text
accepted contract is sufficiently clear
implementation/process violated it
repair can restore conformity without changing accepted semantics
~~~

Result:

~~~text
architecture remains frozen
route to repair / qualification
preserve defect evidence
do not disguise implementation repair as architecture evolution
~~~

If the contract is too ambiguous to determine conformity, the case cannot be closed as a defect until clarification is resolved.

## 6. KEEP

KEEP means the architecture was genuinely reconsidered and remains accepted.

Use when:

~~~text
trigger evidence is real or materially investigated
current assumptions still hold sufficiently
cost/risk of stronger machinery remains unjustified
or existing architecture already addresses the pressure when used correctly
~~~

A KEEP result must preserve:

~~~text
trigger evidence examined
affected contract/revision
reason the current design remains adequate
conditions that would justify another revisit
next reconciliation/monitoring expectation when material
~~~

KEEP is not ignore-the-problem. It is an evidence-backed architecture decision.

## 7. CLARIFY

CLARIFY is allowed only when accepted semantics do not change.

Examples:

~~~text
ambiguous wording
unclear boundary between already-accepted responsibilities
missing explanatory cross-reference
non-normative documentation causing recurrent misreading
~~~

A clarification must prove:

~~~text
no authority change
no obligation change
no new permission/prohibition
no changed acceptance criterion
no changed migration or cutover condition
~~~

If any of those change, the disposition is AMEND or stronger.

Historical acceptance remains against the contract that existed at the time. Clarification cannot retroactively invent a gate that was absent.

## 8. AMEND

AMEND is a bounded semantic change to an accepted architecture/contract that remains recognizably the same governing design.

Use when:

~~~text
a limited requirement or rule must change
the affected scope is identifiable
the remainder of the architecture remains valid
a bounded prospective delta is sufficient
~~~

An amendment requires:

~~~text
exact affected contract/revision
explicit semantic delta
rationale and trigger evidence
affected obligations/gates
migration/compatibility consequences
required review
owner approval for the consequential architecture decision
new forward revision / amendment record
qualification of the impacted scope
~~~

Do not rewrite old checkpoints or pretend the new rule existed historically.

## 9. SUPERSEDE

SUPERSEDE replaces an accepted architecture element, contract, representation, or owner with a successor.

Use when:

~~~text
the old element should no longer govern future work
a successor can be stated explicitly
provenance and transition can be preserved
~~~

Supersession requires:

~~~text
old and new authority identities/revisions
effective boundary
reason replacement is stronger
transition/provenance relation
affected downstream obligations
migration/rollback implications
qualification before the successor governs
~~~

The superseded artifact remains historical evidence. It is not deleted merely because it stopped governing.

## 10. REOPEN

REOPEN is the strongest evaluation result.

Use when:

~~~text
a foundational assumption is materially challenged
the design space must be reconsidered
a bounded amendment cannot be justified safely
or evidence undermines the basis for the accepted element
~~~

REOPEN does not automatically discard the whole architecture. It must define the narrowest affected scope:

~~~text
specific rule
architecture component
workstream contract
migration assumption
or foundational architecture boundary
~~~

Unaffected frozen contracts remain frozen.

For the reopened scope:

~~~text
new research/evaluation route opens
future acceptance progression may pause
existing operational behavior may remain temporarily if still safe
or affected consequential action may fail closed / enter HOLD
~~~

The owner makes the genuinely normative decision to reopen the architecture. The system may nominate and support that decision, but cannot self-authorize it.

## 11. Safety hold is not an architecture disposition

Evidence may be serious enough that continued action is unsafe before the architecture decision is resolved.

AO-4 therefore permits a temporary control state:

~~~text
AFFECTED_SCOPE_HOLD
~~~

This is not KEEP/AMEND/REOPEN.

It means:

~~~text
do not continue the affected consequential action
preserve current accepted authority
open/continue the evolution case
resume only when the governing path resolves the safety condition
~~~

A hold prevents "current contract remains authority" from being misread as "continue using it regardless of new evidence".

## 12. EvolutionCase logical record

AO-4 selects a logical **EvolutionCase** boundary.

Conceptually it records:

~~~text
case identity
trigger source(s)
trigger state
affected contract / semantic owner / exact revision
current accepted architecture
observed evidence
consequence / risk of continuing
candidate classification
required review / evidence
owner decision when normative
final disposition
prospective realization obligations
qualification impact
status / closure evidence
~~~

This is a logical control record. AO-4 does not choose its production schema or storage location.

By default it is non-authoritative evidence until an accepted disposition is promoted into the natural authoritative owner/decision/specification.

## 13. Evaluation lifecycle

~~~text
TRIGGER_CANDIDATE
    ->
EVIDENCE_BOUND
    ->
CLASSIFICATION_PENDING
    ->
REVIEW_PENDING when required
    ->
DISPOSITION_PENDING
    ->
DISPOSITIONED
    ->
REALIZATION_PENDING when change required
    ->
QUALIFICATION_PENDING when change required
    ->
CLOSED
~~~

CONFORMANCE_DEFECT routes to repair rather than architecture mutation.

KEEP may close directly after sufficient evidence and required approval/review.

CLARIFY, AMEND, SUPERSEDE, and REOPEN create explicit realization obligations.

## 14. Decision rights

The system may:

~~~text
detect trigger candidates
bind source evidence
resolve affected current authority
identify likely classification
open the governed evaluation route
apply deterministic fail-closed/hold rules
route required review
verify realization/qualification evidence
~~~

The system must not silently make genuinely normative architecture choices.

Explicit owner decision is required for consequential KEEP after an observed material trigger, CLARIFY when governing interpretation materially matters, AMEND, SUPERSEDE, REOPEN, and any authority transition.

Purely mechanical CONFORMANCE_DEFECT repair may proceed under the already-governing contract when ordinary mutation authority permits it.

## 15. Frozen-contract and historical acceptance integrity

AO-4 preserves a strict temporal rule:

> A later discovery does not retroactively rewrite what an earlier acceptance gate required or what evidence was available at that boundary.

Therefore:

~~~text
new obligation discovered later
    -> prospective realization obligation

new clarification
    -> future interpretation unless historical wording already carried it

new amendment
    -> new revision/effective boundary

supersession
    -> old authority preserved historically

reopen
    -> new evaluation boundary
~~~

If later evidence proves an old acceptance claim itself was factually invalid, preserve that as a new invalidation/recovery record. Do not edit history to make it look as though the failure was known earlier.

This directly generalizes the AO-1 reconstruction-planner finding: W0 was accepted against PKA-G001..G017; the missing reconstruction-planner realization is a prospective obligation-realization gap, not a secret retroactive W0 gate failure.

## 16. Trigger ownership and monitoring surface

AO-4 does not introduce a second central truth registry.

Reuse Candidate 01:

~~~text
source-owned risk_or_reopen_triggers
    ->
derived risk_obligation_index
    ->
Progressive Control Closure activation
~~~

The architecture backlog may remain a compatibility/source surface during migration, but trigger semantics should ultimately live in the natural semantic owner and project-controlled derived index.

Monitoring happens at least:

~~~text
when an incoming event intersects a known trigger
when a control failure observation is emitted
at meaningful stage/reconciliation boundaries
when upstream/tool/provider state changes materially
when repeated-friction evidence accumulates
~~~

The owner should not need to remember that a trigger exists.

## 17. Obligation realization after disposition

Every accepted change disposition must connect to a realization chain:

~~~text
accepted disposition
    ->
affected canonical owner / specification / decision updated prospectively
    ->
implementation or migration gate scheduled when needed
    ->
evidence produced
    ->
qualification performed
    ->
operational activation verified
~~~

This prevents AO-F14 OBLIGATION_REALIZATION_GAP from recurring inside the evolution mechanism itself.

## 18. Qualification impact must be proportional

AO-4 rejects both extremes:

~~~text
tiny clarification -> rerun every project qualification forever
major supersession -> test only the edited file
~~~

The evolution case must identify impacted obligations and qualification surfaces.

Rules:

~~~text
CLARIFY
    -> prove no semantic contract change + ordinary integrity

AMEND
    -> requalify affected obligations/gates + dependent behavior

SUPERSEDE
    -> qualify successor and transition/compatibility/rollback as applicable

REOPEN
    -> define fresh research/qualification contract before acceptance resumes
~~~

Broader regression may still be required when dependency closure cannot be bounded safely.

## 19. Relationship to Progressive Control Closure

AO-4 plugs into AO-3 as follows:

~~~text
S3 Control Obligation Set
    -> EVALUATE_ARCHITECTURE_EVOLUTION

S4 Reconstruction / activation
    -> current frozen contract + trigger evidence + prior rationale

S5 RouteDecision
    -> conformance repair OR EvolutionCase

S6 Authority
    -> resolve current contract owner and decision/mutation boundary

S9 Postflight
    -> preserve EvolutionCase evidence
    -> create realization obligations
    -> update trigger state
    -> emit control observations when the process fails
~~~

A new material fact may return to bounded control re-evaluation.

## 20. Failure-class coverage

AO-4 directly strengthens:

~~~text
AO-F12 EVOLUTION_TRIGGER_MISS
AO-F13 FROZEN_CONTRACT_DRIFT
AO-F14 OBLIGATION_REALIZATION_GAP
AO-F16 CONTROL_OBSERVABILITY_GAP
AO-F18 OWNER_REMINDER_DEPENDENCY
~~~

It also protects AO-F17 BRIDGE_AUTHORITY_LEAK because successor control may open an evolution case without becoming architecture authority.

## 21. Explicit non-decisions

AO-4 does not select:

~~~text
production EvolutionCase schema
central trigger database
background polling daemon
trigger-scoring algorithm
automatic architecture amendment
automatic owner approval
exact collaboration threshold
Git representation for amendments
exact compatibility migration mechanics
~~~

## 22. Regression consequences

Later historical/implementation qualification should include:

~~~text
known trigger observed -> evaluation opens without owner hint
false/partial trigger -> architecture does not mutate
implementation defect -> repair route, not architecture rewrite
ambiguous wording -> CLARIFY only if semantics unchanged
bounded new requirement -> AMEND with prospective gate
replacement design -> SUPERSEDE with preserved provenance
foundational contradiction -> REOPEN only affected scope
severe new evidence -> affected-scope HOLD without implicit authority switch
new obligation after old acceptance -> prospective realization, no retroactive gate rewrite
accepted amendment -> implementation/evidence/activation closure is traceable
~~~

## 23. Disposition

~~~text
AO_4=COMPLETE
EVOLUTION_MODEL=GOVERNED_EVOLUTION_CASES
TRIGGER_OBSERVED_AUTO_MUTATES_ARCHITECTURE=false
CLASSIFICATIONS=CONFORMANCE_DEFECT|KEEP|CLARIFY|AMEND|SUPERSEDE|REOPEN
AFFECTED_SCOPE_HOLD=SUPPORTED
TRIGGER_STATE_DISTINCT_FROM_DISPOSITION=true
OWNER_NORMATIVE_DECISION_PRESERVED=true
HISTORICAL_ACCEPTANCE_REWRITTEN=false
SOURCE_OWNED_TRIGGERS_REUSED=true
RISK_OBLIGATION_INDEX_REUSED=true
OBLIGATION_REALIZATION_CLOSURE_REQUIRED=true
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_5_INTERACTION_CONTINUITY_INTERRUPTION_AND_BREAK_GLASS_DESIGN
~~~
