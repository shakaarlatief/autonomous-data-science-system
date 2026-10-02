# Research 442: OPERATIVE V0.2 thin governing semantics and compiled control projection candidate

**Date:** 2026-10-02
**Status:** OPERATIVE V0.2 CANDIDATE FROZEN FOR MICRO-DEVELOPMENT / SP-0+SP-1 RECONCILED / NO TARGET SELECTION
**Parent:** Research 438 / Research 440 / Research 441
**Scope:** Revise OPERATIVE V0.1 using the first two prospectively frozen development probes, especially SP-0's prose-only control findings and SP-1's competency-question boundary.
**Authority:** Development candidate only. This record does not select production architecture, amend Specification 028, authorize production implementation, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Why V0.1 requires amendment

SP-0 and SP-1 jointly reject two opposite designs.

First, the future system cannot merely bless today's terminal KEY=value blocks as the machine contract:

    SP-0 trailing-block prevalence = 0.8913
    SP-0 sampled prose-only consequential share = 0.3578

The culture already writes compact operational summaries, but important controls remain in prose.

Second, the response must not be to copy every consequential sentence into one enormous universal operative block.

SP-1 finds 37 machine-consequential competency questions, but many belong naturally to:

    AO runtime/control records
    continuity/recovery records
    Git/workstream state
    WARRANT-F policy/claims/evidence/decisions
    realization coverage facts
    executable predicates
    control observations

Only a subset is accepted governing meaning.

Therefore V0.2 is a **thin governing-semantics architecture plus deterministic compilation**, not a universal requirements database.

## 2. V0.2 architecture

Conceptually:

    GOVERNING ACCEPTANCE
        |
        +-- human-governing narrative/context/rationale
        |
        +-- thin machine-operative clauses
        |
        +-- exact references to co-governed domain-native contracts
        |       assurance policy
        |       research/qualification protocol
        |       migration/cutover contract
        |       recovery procedure
        |       workstream/Git policy
        |       other bounded machine contract where justified
        |
        v
    CONTROL COMPILATION / PROJECTION
        |
        +-- ActionContract
        +-- ControlObligationSet
        +-- transition/gate requirements
        +-- reconstruction requirements
        +-- coverage expectations
        |
        v
    NATURAL-OWNER RUNTIME FACTS
        |
        +-- workstream/Git state
        +-- realizer coverage
        +-- evidence / warrant / qualification
        +-- activation facts
        +-- continuity/recovery state
        +-- exact revisions / authority facts
        |
        v
    EXECUTABLE PREDICATES / ASSURANCE
        |
        +-- ADMIT / REFUSE / REVIEW_REQUIRED
        +-- coverage gaps
        +-- active prohibitions/gates
        +-- stale/conflict predicates
        +-- orientation views

The compiler/projection layer is non-authoritative.

The authoritative inputs remain the accepted governing object, domain-native accepted policy/contracts, and natural-owner source facts.

## 3. One governing acceptance object, potentially multiple physical components

V0.2 preserves Research 438's semantic "one artifact" refinement:

    one acceptance event
    one accepted meaning boundary
    exact component identities/revisions

It does **not** require one physical file.

A governing acceptance may bind:

    human-readable carrier revision
    operative clause component
    exact domain-native contract revision(s)

provided they are accepted as one governed object and cannot silently diverge.

A generated JSON projection, index, database row or compiled ActionContract is not another authority source.

If accepted components are internally inconsistent:

    acceptance validation fails
    OR
    post-acceptance discovery opens defect/evolution handling

The system does not resolve a conflict by asking a future LLM which component "probably" meant what.

## 4. Thin-clause admission rule

An operative clause is admitted only when all are true:

1. A governing act creates/changes a consequence that must be machine-trackable across its natural consumers.
2. At least one SP-1-style competency question needs the consequence.
3. The consequence is not already fully and unambiguously owned by a more specific accepted domain contract.
4. The machine-critical part can be expressed through bounded identities/references/predicates/decisions.
5. The clause adds operational value beyond copying human prose.

If a domain-native contract already owns the detail:

    reference it
    do not restate it in a generic clause

Examples:

    assurance threshold
        -> WARRANT-F policy owns it
        -> a GATE may reference the policy/decision
        -> clause does not duplicate threshold math

    research no-retry-to-green rule
        -> accepted protocol contract owns exact attempt rule
        -> governing clause may REQUIRE protocol conformance
        -> generic clause does not copy every protocol field

    Git target-head protection
        -> Git lifecycle/integration contract owns exact mechanics
        -> GATE references the integration decision/predicate

This is the main response to SP-0's prose-only detail.

## 5. Candidate clause forms

V0.2 retains the seven SP-1 forms for micro-development:

    REQUIRE
    PROHIBIT
    GATE
    AUTHORIZE
    DEFER
    LIFECYCLE
    SEQUENCE

They remain hypotheses.

### REQUIRE

Machine meaning:

    an accepted required effect/control exists
    it has stable identity/scope
    realization/coverage may be tracked

Minimum bounded semantics:

    clause_id
    subject_or_scope_ref
    responsible_domain_or_owner_ref
    effective_boundary

Optional:

    acceptance_or_claim_ref
    required_by_transition_ref

Human rendering may explain the requirement.

Machine admission may not depend on rereading that explanation.

### PROHIBIT

Machine meaning:

    typed action/consequence is not admissible in scope

Slots:

    clause_id
    action_or_consequence_ref
    scope_ref
    effective_boundary

Optional:

    until_predicate_ref
    exception_authority_ref

### GATE

Machine meaning:

    named transition/consequence is admissible only when bounded referenced conditions succeed

Slots:

    clause_id
    transition_or_consequence_ref
    predicate_or_decision_refs
    scope_ref

Optional:

    failure_behavior
    review_route_ref

### AUTHORIZE

Machine meaning:

    explicit bounded permission exists

Slots:

    clause_id
    authorized_action_or_phase_ref
    scope_ref
    authorizing_decision_ref
    effective_boundary

Optional:

    expiry_or_revocation_ref
    constraint_refs

### DEFER

Machine meaning:

    existing clause/consequence is validly deferred under governed authority

Slots:

    clause_id
    target_clause_or_consequence_ref
    scope_ref
    authorizing_decision_ref
    reactivation_predicate_ref

Optional:

    evidence_requirement_ref
    expiry_ref

Validity remains:

    structural validity
    + authority validity
    + scope/revision validity
    + temporal/reactivation validity

### LIFECYCLE

Machine meaning:

    accepted prospective AMEND / SUPERSEDE / RETIRE / REOPEN relation

Slots:

    clause_id
    operation
    target_ref
    scope_ref
    effective_boundary
    decision_ref

Optional:

    successor_ref
    transition_ref
    rollback_ref

### SEQUENCE

Machine meaning:

    order itself is a consequential accepted constraint

Slots:

    clause_id
    ordered_step_refs
    scope_ref

Optional:

    precondition_refs
    return_target_ref

## 6. Forms deliberately not present

### INVARIANT

Not a standalone generic clause.

A checkable invariant belongs to:

    WARRANT-F claim/policy
    executable predicate
    another natural owner

A governing GATE/REQUIRE may reference it.

### ASSIGN

No universal standalone assignment clause yet.

Responsibility can be:

    a slot on REQUIRE/AUTHORIZE
    a natural-owner fact
    a workstream/organizational contract

Add ASSIGN only if a real competency question demonstrates a missing machine consequence.

### ROUTE / NEXT

Not governing semantics by default.

Current route/next action is normally:

    derived RouteDecision
    workstream state
    continuation state

When order is itself accepted authority, use SEQUENCE/GATE/REQUIRE.

## 7. Typed-reference rule

Machine-critical slots must resolve to bounded semantic types.

Candidate reference families include:

    semantic subject / exact revision
    scope
    action class / consequence class
    transition
    predicate
    claim / assurance decision
    accepted governing decision
    operative clause
    workstream
    realizer artifact
    evidence/qualification record
    authority
    effective boundary

Free text may render/explain those values.

It does not replace them for deterministic behavior.

If a consequence cannot be bounded this way:

    keep it human-governing
    and/or
    route REVIEW / owner decision

Do not silently reintroduce semantic inference into a deterministic gate.

## 8. Domain-native contract rule

A domain-native machine contract is preferred over generic operative expansion when:

    one domain clearly owns the semantics
    the contract is already needed by that domain
    cross-domain consumers can reference its exact identity/result
    copying details would create dual maintenance

Examples:

    WARRANT-F gate policy
    research/qualification protocol
    migration/cutover qualification contract
    recovery runbook/procedure
    Git integration contract

The governing acceptance object may co-accept or reference the exact contract revision.

This preserves one meaning boundary without requiring one universal schema.

## 9. Compilation rule

Accepted governing semantics are compiled with current policy/facts into disposable control projections.

Conceptually:

    accepted clauses
    + accepted domain contracts
    + current authoritative facts
        ->
    deterministic compiler
        ->
    ActionContract / ControlObligationSet / gate inputs / coverage expectations

Rules:

    compiler output has no independent authority
    compiler is versioned/tested
    exact inputs and compiler version are inspectable
    stale inputs invalidate consequential projections
    projection conflict with current authority fails visible
    generated projection can be destroyed and rebuilt

This is analogous to a compiler/IR boundary:

    authored accepted source
        -> deterministic operational representation

but the analogy does not require adopting compiler technology literally.

## 10. J1 / J2 / J3 under V0.2

### J1 governing meaning

At acceptance:

    human meaning
    + thin clauses
    + exact domain-contract refs
        -> one accepted governing object

The owner accepts the governing object.

### J2 realization mapping

Later, natural realizing owners declare:

    REALIZES <clause-ref>

or equivalent coverage facts.

No birth-time canonical grouping is inferred.

A single artifact may cover multiple clauses.

Multiple artifacts may cover one clause when the realization contract permits it.

### J3 operational truth

Executable code evaluates source-owned facts:

    coverage
    deferral
    evidence
    qualification
    activation
    staleness
    conflict

Generated views answer bounded competency questions.

No author selects one global realization-state truth.

## 11. LLM / classifier boundary

Model-assisted systems may:

    interpret incoming project events into bounded hypotheses
    draft clauses before acceptance
    compare a draft against human narrative for omissions
    detect likely machine-consequence leakage
    propose legacy candidates
    propose realizer coverage
    explain derived decisions

They may not:

    turn an unaccepted inference into governing authority
    decide a normative owner choice silently
    overwrite deterministic policy output
    resolve authority conflict by confidence score

Bounded typed probabilistic classifiers are legitimate candidate technologies for nomination/triage/detection where later evidence shows value.

V0.2 selects no model family/provider.

## 12. SP-0 burden response

SP-0 showed 39/109 sampled consequential effect groups were prose-only.

V0.2 does not require hand-copying all 39 into clauses.

For each omitted effect, the target routing is one of:

    ACCEPTED_CLAUSE
        cross-domain machine-governing consequence

    DOMAIN_CONTRACT
        detailed semantics naturally owned elsewhere

    GENERATED_CONTROL
        deterministic projection from accepted semantics/current facts

    HUMAN_GOVERNING_ONLY
        important human meaning with no claimed deterministic machine consequence

    ADVISORY_DETECTION
        semantic risk worth detecting but not promoting automatically

This classification is part of the SP-2 drafting exercise.

## 13. Adoption-economics hypothesis

V0.1's near-zero-cost formalization hypothesis is withdrawn.

V0.2's weaker hypothesis is:

> Existing Project practice already produces enough compact governing summaries and structured domain contracts that a thin cross-domain operative layer may be feasible at acceptable incremental cost.

This must be measured.

Relevant costs include:

    drafting clause/reference details
    owner review
    correction rounds
    parser/schema validation
    domain-contract maintenance
    realization coverage declarations
    leak detection/review
    generated projection/debugging

The detective-only null baseline remains mandatory before an adoption claim.

## 14. V0.2 falsifiers

Abandon or materially redesign V0.2 if small realistic work shows any of:

    F1
        owner cannot judge whether a drafted governing object faithfully captures
        the accepted decision without substantial semantic re-interpretation

    F2
        most consequential details cannot be assigned cleanly to
        clause / domain contract / generated control / human-only meaning

    F3
        typed slots repeatedly require free-text interpretation to drive machine gates

    F4
        clause + domain-contract split creates duplicate authority or unclear conflict rules

    F5
        realizer coverage is harder/more ambiguous than the grouping construct it replaces

    F6
        executable predicates still require semantic adjudication of source facts

    F7
        incremental author/reviewer burden is disproportionate to control value

    F8
        detective-only baseline catches the relevant failures at materially lower cost

These are development falsifiers, not confirmation thresholds.

## 15. SP-2 sequencing amendment

Research 438 originally suggested freezing SP-2 and SP-3 after SP-0/SP-1.

SP-0 returned MIXED and forced a material V0.2 revision.

Therefore the more evidence-efficient sequence is amended prospectively:

    freeze SP-2 against V0.2
    run owner-faithfulness / burden micro-replay
    inspect development disagreements
        ->
    only if V0.2 survives:
        freeze SP-3 against the surviving exact grammar/contracts

Freezing SP-3 now would bind it to a grammar that SP-2 is explicitly allowed to change.

This is consistent with Research 436's progressive-test principle.

## 16. Current disposition

    SP0=MIXED_EXISTING_IDIOM
    SP1=OPERATIVE_GRAMMAR_PLAUSIBLE

    OPERATIVE_V01=SUPERSEDED_AS_DEVELOPMENT_CANDIDATE
    OPERATIVE_V02=FROZEN_FOR_MICRO_DEVELOPMENT

    OPERATIVE_V02_TARGET_STATUS=NOT_SELECTED
    CLAUSE_FORMS=7_CANDIDATE
    OPERATIVE_IS_UNIVERSAL_PROJECT_SCHEMA=false
    DOMAIN_NATIVE_CONTRACTS_RETAINED=true
    GENERATED_CONTROL_AUTHORITY=false
    BIRTH_TIME_GROUPING=false
    LLM_AUTHORITATIVE_INTERPRETATION=false

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED_NOW=false

    NEXT=FREEZE_SP2_OWNER_FAITHFULNESS_MICRO_REPLAY
