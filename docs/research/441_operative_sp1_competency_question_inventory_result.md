# Research 441: OPERATIVE SP-1 competency-question inventory result

**Date:** 2026-10-02
**Status:** SP-1 COMPLETE / OPERATIVE_GRAMMAR_PLAUSIBLE / SP-0+SP-1 REQUIRE CANDIDATE REVISION BEFORE SP-2
**Protocol:** Research 439
**Fixed evidence base:** 8e8aed19cf3e1c159f74fdef787070688634a221
**Result artifact:** docs/research/project_knowledge_activation_orchestration/ao10/OPERATIVE_SP1_RESULT_V01.json
**Scope:** Record the second frozen small development probe for OPERATIVE V0.1 by inventorying actual machine-consequential Project-system competency questions and deriving the smallest currently plausible accepted-clause grammar without privileging Claude's illustrative forms.
**Authority:** Development evidence only. This result does not select OPERATIVE, amend Specification 028, authorize production implementation, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Source boundary

SP-1 used the exact primary surface frozen by Research 439:

    Research 222 AO-3
    Research 223 AO-4
    Research 224 AO-5
    Research 225 AO-6
    Research 226 AO-7
    Research 257
    Research 258
    Research 276 WARRANT-F V0.2
    Research 315
    Research 318 DRP-09
    Specification 028 §42

No support source was required.

Hidden R2 item-level semantic material remained sealed.

## 2. Inventory result

The frozen extraction rules yield:

    admitted competency questions = 37

By consequence class:

    ROUTING                 7
    ADMISSION               8
    AUTHORITY               4
    CONTINUITY_RECOVERY     7
    EVOLUTION               5
    REALIZATION_COVERAGE    2
    OPERATIONAL_PREDICATE   2
    CUTOVER_MIGRATION       1
    OBSERVABILITY           1

By answer shape:

    STRUCTURED_DECISION    19
    REFERENCE_SET           7
    ENUM                    7
    BOOLEAN                 4

Every admitted question terminates in a bounded answer shape.

No competency question requires free-form prose as its successful machine-operative answer.

## 3. Key architectural finding: OPERATIVE is only one semantic layer

The strongest SP-1 result is a boundary clarification.

The whole Project system cannot and should not be encoded as operative clauses.

Machine-consequential questions fall into at least three distinct families:

    accepted governing consequences
        -> OPERATIVE clause candidates

    runtime/control decisions
        -> EventInterpretation / ControlObligationSet / RouteDecision /
           AuthorityReceipt / ActionContract / continuity / Git control

    natural-owner assurance/realization facts
        -> WARRANT-F policy/claims/evidence/decisions /
           realizer coverage / executable predicates / observations

Therefore:

    OPERATIVE_CLAUSE_GRAMMAR != UNIVERSAL_PROJECT_SYSTEM_SCHEMA

This materially reduces pressure to make the clause language express every AO, recovery, Git, assurance, or runtime state.

## 4. Candidate minimal clause grammar

Starting from no assumed form and admitting a form only where a competency question needs accepted machine-governing meaning, SP-1 derives seven candidate forms:

    REQUIRE
    PROHIBIT
    GATE
    AUTHORIZE
    DEFER
    LIFECYCLE
    SEQUENCE

This is below the Research 439 development guard of ten forms.

Three Message-011 illustrative forms are not retained as standalone forms:

    INVARIANT
        checkable invariants belong to WARRANT-F claims/policy
        or referenced executable predicates

    ASSIGN
        responsibility is a bounded slot or a natural-owner fact
        unless a future competency question demonstrates need
        for a standalone transfer clause

    ROUTE / NEXT
        current routing is normally derived control state rather than
        governing semantic authority; consequential order can use
        REQUIRE / SEQUENCE / GATE

The seven forms are not target architecture. They are the smallest currently plausible development grammar.

## 5. Machine-critical slots may not depend on prose reinterpretation

SP-1 rejects a subtle but important version of the illustrative syntax:

    REQUIRE <free-text effect>
    GATE <transition> ON <free-text condition>

when machines would later need to reinterpret those free-text arguments.

The candidate rule is:

    human-readable text may explain a clause

but:

    machine-critical behavior must bind typed references

such as:

    exact semantic subject/scope
    typed action/consequence
    transition
    predicate
    claim
    assurance decision
    governing decision
    clause identity
    realizer coverage fact
    effective boundary

If no bounded predicate/claim/reference can support automated admission:

    the clause may remain human-governing / coverage-trackable
    but the system must not pretend its free text is a deterministic machine gate

That path produces review/human decision rather than hidden semantic inference.

## 6. Natural-language event interpretation remains allowed

AO-3 explicitly permits model-assisted event hypotheses.

SP-1 does not mistake that for the old DRP-03 failure.

The distinction is:

    event interpretation
        model may propose bounded non-authoritative hypotheses
        uncertainty remains visible
        project-controlled policy decides mandatory control obligations

versus:

    governing meaning
        accepted machine consequence is explicitly authored/admitted
        future LLM interpretation does not silently create authority

Therefore the existence of natural-language user/project events does not force a general semantic interpreter back into the governing-authority path.

This leaves open future use of deterministic rules, general LLMs, or bounded typed classifier models on non-authoritative event/detection surfaces. No model technology is selected by SP-1.

## 7. Owner decisions remain owner decisions

Some machine-consequential questions terminate not in an autonomous answer but in:

    OWNER_DECISION_REQUIRED

Examples include genuinely normative AO-4 dispositions.

The Project system may:

    bind evidence
    identify affected authority
    route review
    validate the accepted decision
    derive consequences afterward

It may not turn the closed grammar into a mechanism for silently choosing architecture on the owner's behalf.

## 8. SP-1 result class

Research 439 defines OPERATIVE_GRAMMAR_PLAUSIBLE when:

    every machine-critical competency question can be answered
    from explicit bounded inputs

    <= 10 clause forms are required

    no required clause slot fundamentally requires
    unconstrained prose interpretation at decision time

Observed:

    bounded-answer inventory              PASS
    candidate clause forms                7 <= 10
    required machine-critical prose slot  NONE

Therefore:

    SP1 = OPERATIVE_GRAMMAR_PLAUSIBLE

This is a development result, not architecture acceptance.

## 9. Interaction with SP-0

SP-0 was:

    MIXED_EXISTING_IDIOM

SP-1 is:

    OPERATIVE_GRAMMAR_PLAUSIBLE

Under Research 439 combined routing, a MIXED result requires revising OPERATIVE before owner-facing SP-2 even when the grammar itself appears bounded.

The reason is now concrete.

Current Project practice already contains compact operative summaries, but those summaries omit many detailed controls.

SP-1 shows that not all omitted controls need to become clauses.

Some belong in:

    generated ActionContracts
    control rules
    recovery policy
    Git lifecycle state
    assurance policy
    executable predicates
    realizer facts

The next candidate therefore needs to distinguish:

    authored accepted clauses
    generated machine control contracts
    natural-owner machine facts

rather than expanding the operative block until it duplicates the whole Project system.

## 10. Revision requirements for OPERATIVE V0.2

Before SP-2, revise the candidate around these requirements:

    O2-1
        operative clauses represent accepted governing consequences only

    O2-2
        machine-critical clause slots are typed references,
        not prose to be reinterpreted

    O2-3
        generated control contracts may project accepted clauses
        plus policy/current state but gain no independent semantic authority

    O2-4
        runtime/control records remain in AO/continuity/Git natural owners

    O2-5
        assurance semantics remain in WARRANT-F

    O2-6
        realization facts/predicates remain with natural owners
        and executable code

    O2-7
        human-governing prose may remain outside machine-operative semantics

    O2-8
        current KEY=value closing blocks are evidence/cultural precedent,
        not the target grammar

    O2-9
        authoring-cost claims must include the extra structured detail
        that SP-0 found prose-only

    O2-10
        owner-facing SP-2 must test actual faithfulness and burden,
        not merely parser validity

## 11. What this probe does not establish

SP-1 does not establish:

    that seven forms are the final grammar
    that authors can write them faithfully
    that owner review catches material errors
    that realizer coverage is natural or cheap
    that executable predicates are complete
    that leak detection is adequate
    that OPERATIVE beats the detective-only baseline
    that current prose can be losslessly converted

Those remain downstream development questions.

## 12. Current route

No SP-2 or SP-3 execution is authorized by this result.

The next work is to derive OPERATIVE V0.2 from the combined SP-0/SP-1 evidence before asking the owner to judge real drafted operative clauses.

    SP0=MIXED_EXISTING_IDIOM
    SP1=OPERATIVE_GRAMMAR_PLAUSIBLE
    OPERATIVE_V01=AMEND_BEFORE_SP2
    COMPETENCY_QUESTION_COUNT=37
    CLAUSE_FORM_COUNT=7
    GENERAL_SEMANTIC_INTERPRETER_REQUIRED_FOR_GOVERNING_AUTHORITY=false
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED_NOW=false
    NEXT=DESIGN_OPERATIVE_V02_FROM_SP0_SP1
