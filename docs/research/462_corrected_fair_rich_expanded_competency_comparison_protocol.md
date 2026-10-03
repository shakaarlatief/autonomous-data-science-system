# Research 462: corrected fair-rich and expanded-competency comparison protocol

**Date:** 2026-10-03
**Status:** PROTOCOL FROZEN / CORRECTED DESK COMPARISON NEXT
**Parent:** Research 461 / MC-0029 Message 015
**Fixed evidence base:** f3ff5e9a0016acfcd5558bf01f82e0cefe3aa331
**Scope:** Prospectively freeze the corrected semantic-core comparison required by Research 461 before observing the corrected result.
**Authority:** Development-comparison protocol only. This record does not select a production architecture, amend Specification 028, expose hidden R2 item material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Comparison question

The corrected comparison asks whether, after representing RICH_ACCEPTED fairly from Research 327 V0.5 and widening the competency surface beyond SP-1, the Project system requires the full rich core, the original THIN V0.2 core, or a thin-centred hybrid.

## 2. Candidate A: THIN_V02

Use Research 442 exactly as the pre-critique thin core: REQUIRE, PROHIBIT, GATE, AUTHORIZE, DEFER, LIFECYCLE and SEQUENCE; exact domain-contract references; generated non-authoritative control projections; J2 realizer coverage; J3 executable predicates; no birth-time canonical realization grouping; no generic authored materiality; no authoritative global realization-state value.

Do not silently add Research 461 amendments to this arm.

## 3. Candidate B: RICH_V05_ACCEPTED

Use Research 327 V0.5, not the R1 annotation schema.

Authority amendment for this comparison:

    model drafts V0.5 accepted semantics
    + owner sees source meaning and proposal together
    + owner accepts/amends/rejects
    + only accepted structure becomes J1 authority.

Functional V0.5 features include:

    AcceptanceDeclarationSet
        exact acceptance identity
        exact accepted subject/revision
        accepted normative-delta item identities
        normative kind
        resulting ObligationUnits where required
        standing constraint/sequencing bindings
        CREATES_NO_REALIZATION_UNITS where applicable

    natural-owner facts after birth
        REALIZES
        EVIDENCES
        QUALIFIES
        ACTIVATES
        DEFERS

    deterministic derived realization state
    governed split/merge/replacement successor relations.

Do not require realization facts to be J1-authored.

## 4. Existing 37 competency questions

Use exactly the 37 SP-1 questions from OPERATIVE_SP1_RESULT_V01.json.

For each record:

    cq_id
    normalized question
    consequence class
    answer shape
    discrimination = DISCRIMINATING | NON_DISCRIMINATING
    current dependency state
    THIN_V02 support + exact mechanism + deficiency
    RICH_V05_ACCEPTED support + exact mechanism + deficiency
    unique contribution

No DISCRIMINATING row may reuse a generic reason merely because another row has the same clause-form status.

The audit must distinguish a currently realized mechanism from a question that is only routable to a future domain contract.

## 5. Expanded competency candidates

Freeze six candidate questions.

MC-1 COMPLETENESS
Source: KA-R52 / Research 235.
Question: Is every accepted governing MUST-level obligation deterministically represented as a tracked realization path or explicit governed deferral, with no untracked third state?

MC-2 DONE_DEFINITION
Sources: KA-R52 evidence/qualification requirement, WARRANT-F independent assurance principle, Research 447 predicate inputs.
Question: What governing or governed-domain criterion defines when requirement R is complete, and can the system prevent a realizer declaration from certifying its own completion merely by declaring coverage?

MC-3 PARTIAL_COMPLETION
Source: Research 447 FULL/PARTIAL coverage contract.
Question: When several artifacts each partially cover one requirement, what deterministic rule establishes full completion without treating multiple self-declared PARTIAL edges as sufficient by themselves?

MC-4 REQUIREMENT_LINEAGE
Sources: Research 327 split/merge successor rule, Specification 028 lineage requirements, DRP-07.
Question: Which successor requirement identities carry predecessor requirement R after split, merge, carry-forward, replacement or other contract re-partition, with explicit loss/unmapped accounting?

MC-5 OWNER_ACCOUNTING
Sources: KA-R52, DRP-06, Research 327 derived state / AcceptanceDeclarationSet.
Question: Can a bounded generated owner-orientation view answer what the project is currently committed to and which accepted realization obligations are open, deferred, satisfied, conflicted or otherwise unresolved using one governed derivation definition?

MC-6 CROSS_DECISION_CONFLICT
Sources: authority/conflict invariants and lifecycle exact-subject/revision requirements.
Question: Can the system detect mutually incompatible active REQUIRE / PROHIBIT / AUTHORIZE / GATE consequences over the same governed subject/scope without asking a future model to reinterpret prose?

Each candidate receives ADMIT or REJECT with an exact source-based reason.

## 6. Support statuses

Use exactly:

    DIRECT
    DIRECT_WITH_SHARED_DOMAIN
    PARTIAL
    MISSING
    NOT_APPLICABLE

A richer representation gets no credit merely for storing more data. A thin representation gets no credit merely for routing an unanswered question to a future contract.

## 7. Decision logic

THIN_V02_SUFFICIENT only if every admitted question is DIRECT or DIRECT_WITH_SHARED_DOMAIN under THIN_V02 and RICH supplies no unique required capability.

RICH_V05_REQUIRED only if at least one admitted requirement materially requires the V0.5 unit/taxonomy/grouping architecture as a whole and cannot be met by bounded selective amendments to THIN.

THIN_CENTRED_HYBRID_REQUIRED if THIN_V02 has admitted gaps, RICH_V05_ACCEPTED contains concepts that address some gaps, but the full V0.5 core is unnecessary and bounded selective amendments to THIN can provide the needed capability.

SHARED_REDESIGN_REQUIRED if both arms fail the same material admitted requirements and neither contains an adequate reusable mechanism.

EVIDENCE_INSUFFICIENT if source evidence cannot support a defensible comparison.

## 8. Anti-bias rules

Do not count natural-domain/control questions as evidence for either semantic core when both arms use the same mechanism.
Do not count a V0.5 natural-owner fact as J1 burden.
Do not infer hidden R2 item-level disagreement causes.
Do not use R2 failure to reject owner-accepted V0.5.
Do not treat V0.5 grouping as canonical merely because an owner could accept it.
Do not treat Research 461 amendments as already proven.
Do not count future unimplemented domain contracts as current realized capability.
Do not score an arm by field count.

## 9. Output

Produce:

    experiments/ao10_corrected_thin_rich_v01/CORRECTED_COMPARISON_V01.json

plus one research result.

The artifact must contain all 37 original CQ rows, all 6 expanded candidate rows with admission decisions, aggregate counts, unique-value findings, shared gaps and one routing class.

## 10. Current boundary

    PROTOCOL=CORRECTED_THIN_RICH_V01
    ORIGINAL_CQ_COUNT=37
    EXPANDED_CANDIDATE_COUNT=6
    RICH_BASELINE=RESEARCH327_V05
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=EXECUTE_CORRECTED_THIN_RICH_DESK_COMPARISON
