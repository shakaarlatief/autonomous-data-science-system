# Research 461: MC-0029 Message 015 reconciliation and thin-centred hybrid amendment

**Date:** 2026-10-03
**Status:** MESSAGE 015 RECONCILED / RESEARCH 460 AMENDED / CORRECTED COMPARISON REQUIRED / NO PRODUCTION SELECTION
**Parent:** Research 459-460 / MC-0029 Message 015
**Repository evidence base:** 7af2f1495fd2ad3896a1b34105a009cccffbc7b7
**Scope:** Reconcile Claude's adversarial critique of the THIN_ACCEPTED versus RICH_ACCEPTED comparison and define the exact corrections required before any owner architecture decision or larger pilot.
**Authority:** Development-reconciliation only. This record does not select a production target, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Overall disposition

Message 015 is:

    ACCEPT_WITH_REFINEMENTS

Research 460's primary routing conclusion:

    THIN_ACCEPTED_SUFFICIENT_RICH_OPTIONAL

is no longer strong enough to carry forward as the current comparison result.

The corrected current development position is:

    THIN_CENTRED_HYBRID = LEADING_AMENDED_CANDIDATE
    HYBRID_REQUIRED = PLAUSIBLE_BUT_REQUIRES_CORRECTED_COMPARISON
    PRODUCTION_TARGET_SELECTED = false

The reason is not a revival of the old ObligationUnit core.

The reason is that Claude identifies several missing or underspecified requirements that survive even after birth-time grouping, generic materiality and authoritative global state are rejected.

## 2. A1: fair rich baseline

Disposition:

    ACCEPT

Research 459/460 used the R1 annotation schema as the concrete rich baseline.

That was too burdensome and not faithful to the later V0.5 design in Research 327.

Research 327 had already moved realization facts to their natural owners:

    REALIZES
    EVIDENCES
    QUALIFIES
    ACTIVATES
    DEFERS

and made realization state derived from those facts.

Therefore the corrected comparison must instantiate RICH_ACCEPTED from Research 327 V0.5 semantics, not from the earlier R1 reviewer schema.

This correction weakens one of Research 460's burden arguments.

It does not restore:

    generic materiality
    exclusive normative-kind necessity
    birth-time realization grouping
    authored realization state

as presumptively desirable.

## 3. A2: per-CQ analysis

Disposition:

    ACCEPT

The Research 460 machine-readable comparison used only two generic reason strings.

The 37/37 headline therefore overstates the discriminatory strength of that audit.

The corrected comparison must:

    mark control-object/domain-owned CQs as NON_DISCRIMINATING where both designs depend on the same external contract;
    provide per-CQ reasoning for every discriminating CQ;
    distinguish CURRENTLY_REALIZED from DESIGN-ROUTABLE answers;
    identify exactly which semantic-core field, if any, each CQ needs.

The original 37-CQ result remains historical development evidence but may not be used as if all 37 independently discriminated between THIN and RICH.

## 4. A3: widen the competency-question boundary

Disposition:

    ACCEPT_WITH_REFINEMENT

SP-1 was a deliberately bounded inventory.

It was sufficient to test whether the seven-form OPERATIVE grammar was plausible against its frozen control-plane evidence surface.

It was not broad enough to settle final semantic-core architecture.

The corrected comparison must additionally test requirement classes supported by:

    Research 235 / KA-R52
    PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02
    Specification 028 identity-transition / compatibility / migration-lineage requirements
    DRP-06 bounded orientation
    DRP-07 Specification 028 lineage / contract partition

Claude's MC-1 through MC-5 are admitted as candidate missing competency questions for evaluation, not automatically accepted as exact final wording.

Cross-decision normative conflict is also admitted as a candidate sixth class.

## 5. A4: completeness-driven tracking

Disposition:

    ACCEPT_WITH_REFINEMENT

KA-R52's exact accepted minimum is:

    every accepted governing MUST-level obligation
    must be deterministically traceable to realization or explicit governed deferral;
    no untracked third state is permitted.

The amended successor must therefore not make tracking depend solely on whether a previously inventoried machine consumer happens to request the obligation.

However, Claude's wording "every accepted realization-requiring obligation" is broader than the literal KA-R52 MUST-level minimum.

For development architecture, the stronger candidate rule is:

    every governing acceptance must deterministically establish either:
        tracked realization-requiring consequences
        OR
        explicit CREATES_NO_REALIZATION_REQUIREMENTS for the relevant acceptance scope

but the exact admission scope must be tested and owner-accepted before production selection.

This avoids both:

    consumer-driven omission

and:

    treating every SHOULD, principle, explanation or research statement as a formal realization obligation.

## 6. A5: governing-side definition of satisfaction

Disposition:

    ACCEPT_WITH_REFINEMENT

Claude identifies a real gap.

SP-3 validates the structure and provenance of realizer coverage, and its predicate fixtures contain:

    evidence_required
    qualification_required
    activation_required

but SP-3 does not itself establish who has authority to set those requirements.

A realizer declaration must not be sufficient to certify the governing requirement as satisfied.

The amended rule is:

    coverage declaration
        = evidence that an artifact claims/declares realization coverage

    satisfaction
        = coverage
          + governing-side or governed-domain completion criterion
          + required independent evidence/qualification
          + required activation/effective facts

If no governing completion criterion/policy exists:

    coverage may be recorded
    but SATISFIED must not be inferred merely from the realizer declaration.

Research 442's optional acceptance_or_claim_ref is therefore too weak for any REQUIRE whose fulfillment can drive consequential machine admission or a claimed completion result.

This amendment does not reintroduce a generic material boolean.

Applicability is consequence/policy-specific.

## 7. A6: requirement granularity

Disposition:

    ACCEPT_AS_CANDIDATE_RULE / REQUIRES_PROBE

Removing ObligationUnit grouping does not remove decomposition.

The drafter still must decide how many REQUIRE identities one governing decision creates.

The candidate J1 rule is:

    one REQUIRE identity per independently acceptable effect

where "independently acceptable" means that the governing side can define and later judge completion separately without requiring another sibling effect to be true.

This is better aligned with J1 than V0.5's realization-boundary grouping rule because it does not require implementation knowledge at governing birth.

It is not yet qualified.

A small prospective granularity probe is required.

## 8. A7: partial and multi-artifact completion

Disposition:

    ACCEPT

Research 447 explicitly allowed:

    FULL
    PARTIAL

but froze all satisfying SP-3 edges as FULL.

PARTIAL composition therefore remains undefined and untested.

The amended candidate must define:

    partial coverage never satisfies a REQUIRE merely by aggregation of self-declared percentages/edges;

    completion requires either:
        an explicit governed completion relation/fact
        OR
        satisfaction of the governing acceptance criterion by qualified evidence.

A prospective partial-composition probe is required.

## 9. A8: N:M requirement lineage

Disposition:

    ACCEPT

Clause-to-realizer many-to-many coverage solves realization topology.

It does not by itself solve requirement identity across semantic succession.

The successor architecture must support N:M governed lineage such as:

    SPLIT
    MERGE
    CARRY_FORWARD
    REPLACE / SUPERSEDE where applicable

with explicit loss/unmapped accounting.

This belongs in the identity/lifecycle relation layer rather than being forced into the realization-coverage graph.

The exact representation remains open pending DRP-01 seam compatibility and successor DRP-07 qualification.

## 10. A9: shared status semantics

Disposition:

    ACCEPT_WITH_REFINEMENT

Research 460 remains correct that realization status values should be generated from source facts rather than authored as independent truth.

However, consumer-specific status definitions would create semantic drift.

The amended rule is:

    control decisions consume exact predicates/facts;

    human orientation may expose one accepted, versioned, code-defined realization-status projection;

    projection values are generated/non-authoritative;
    the derivation definition is governed and versioned.

The old V0.5 enum is not automatically selected.

DRP-06 / owner-orientation requirements must determine the smallest useful vocabulary.

## 11. A10: optional-rich burden

Disposition:

    ACCEPT

"Optional" is not equivalent to "free."

If richer owner-accepted metadata survives as optional or selectively mandatory:

    its review burden
    maintenance burden
    correction frequency
    and synchronization risk

must be measured before production adoption.

SP-2 LOW review burden applies only to the tested thin cases.

It cannot be transferred automatically to richer metadata.

## 12. What remains rejected from the earlier rich core

Message 015 does not supply evidence to restore the following as mandatory core semantics:

    birth-time realization-based canonical grouping
    generic authored materiality
    exclusive normative-kind taxonomy as the sole operational type system
    independently authoritative global realization-state values
    later unaccepted semantic reconstruction as authority

Owner acceptance can make a chosen rich structure authoritative.

It does not prove that those structures are necessary, canonical, or low-burden.

## 13. Corrected candidate shape

The leading amended candidate is now provisionally:

    GOVERNING ACCEPTANCE / J1
        human-governing source meaning
        accepted machine consequences
        stable requirement identities
        governing completion criteria where required
        explicit no-realization declaration where appropriate
        effective/lifecycle relations
        N:M requirement-lineage relations

    NATURAL REALIZATION / J2
        realizer-declared coverage
        evidence mechanism
        implementation / migration / procedure bindings
        many-to-many realization topology

    OPERATIONAL TRUTH / J3
        executable predicates
        independent qualification/admission
        activation facts
        governed deferrals
        generated canonical orientation/status projection

    DETECTIVE SAFETY NET
        recital leak detection
        missing-obligation completeness checks
        realization-gap audits
        policy/claim integrity checks

This is THIN-centred because the accepted core remains consequence-specific and bounded.

It is hybrid because a small number of properties previously associated with richer obligation architecture become selectively mandatory:

    completeness accounting
    explicit requirement identity/granularity
    governing completion criteria
    governed N:M lineage
    one shared derived orientation definition

## 14. Evidence status

Research 460 is not deleted or rewritten.

Its result is now interpreted as:

    useful first-pass desk comparison
    materially weakened by unfair rich instantiation and under-discriminating CQ audit
    superseded for routing by Research 461 until corrected comparison is complete

Message 015 is collaboration evidence, not architecture authority.

Research 461 is the current ChatGPT reconciliation candidate.

## 15. Next discriminating work

Before any owner architecture decision or larger pilot:

    C1  re-instantiate fair RICH_ACCEPTED from Research 327 V0.5
    C2  rebuild the CQ audit with per-question reasoning
    C3  evaluate MC-1..MC-5 plus cross-decision conflict
    C4  freeze/test J1 granularity
    C5  freeze/test governing-side completion criteria vs realizer self-certification
    C6  freeze/test PARTIAL multi-artifact composition
    C7  design/qualify N:M requirement lineage against the DRP-01 seam
    C8  derive the minimal canonical orientation/status projection from DRP-06 needs
    C9  measure owner burden for any surviving richer metadata before adoption

The immediate next step is a prospectively frozen corrected comparison covering C1-C3.

No owner participation is required for that desk analysis.

## 16. Current disposition

    MESSAGE015=ACCEPT_WITH_REFINEMENTS
    RESEARCH460=AMENDED_FOR_ROUTING

    LEADING_CANDIDATE=THIN_CENTRED_HYBRID
    HYBRID_REQUIRED=PLAUSIBLE_NOT_YET_FINAL
    PRODUCTION_TARGET_SELECTED=false

    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=FREEZE_CORRECTED_THIN_RICH_COMPETENCY_COMPARISON
