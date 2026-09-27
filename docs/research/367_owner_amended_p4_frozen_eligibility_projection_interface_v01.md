# Research 367: Owner-Amended P4 Frozen Eligibility Projection Interface V0.1

**Date:** 2026-09-27
**Status:** OWNER AMENDMENT ACCEPTED / P4 ELIGIBILITY PROJECTION INTERFACE V0.1 FROZEN / D01 ATTEMPT 003 PREPARATION AUTHORIZED / SEMANTIC EXECUTION NOT YET RELEASED
**Parent:** Research 366 / project-owner explicit AMEND decision
**Scope:** Replace the unstable hidden reclassification bridge in P4 with a minimal mechanically derived eligibility projection from each key author's own frozen BIRTH classifications, freeze the projection contract before further grouping, and authorize deterministic private preparation for D01 attempt 003.
**Authority:** Amended P4 grouping interface only. This does not authorize classification repair, D02, held-out grouping, LEGACY, canonical Key A assembly, commitment generation, Key Author B execution, scoring, production implementation, migration, oracle retirement, or authority switching.

## 1. Owner decision

The project owner explicitly stated:

    I AMEND.

This accepts the Research 366 recommendation to replace grouping-time hidden reclassification with a minimal frozen eligibility projection.

The already-granted P4 phase authorization remains active.

No new classification judgment is authorized.

No frozen P2/P3 semantic artifact may be edited.

## 2. Problem being corrected

Research 363 required every stored grouping endpoint to map to frozen:

    realization_required = true

while withholding all frozen classification-derived eligibility information from the grouping author.

Attempt 001 failed that hidden gate.

Research 365 then instructed the grouping author to independently re-evaluate realization-required eligibility from current-event text.

Attempt 002 still failed the same hidden gate while every observable execution control passed.

The development evidence therefore rejects the assumption that a fresh grouping session can reliably reproduce a frozen classification boundary that it is deliberately prohibited from seeing.

Repeated blind retries are not an acceptable remedy.

## 3. Amended stage interface

P4 is now explicitly conditional on the already-frozen BIRTH classification stage.

For each grouping event, the task owner mechanically derives a private eligibility projection from that same key author's frozen classification state.

The projection contains only:

    protocol metadata
    component
    split
    packet_event_id
    sorted semantic item IDs whose frozen primary classification has:
        realization_required = true

The projection MUST NOT contain:

    presentation IDs
    attention-duplicate identities
    attention mapping
    normative label
    normative kind
    materiality
    restatement status
    decision-time delta
    rationale
    source location beyond ordinary event semantics
    classification confidence
    pair candidates
    pair outcomes
    pair counts
    any other key's information

The grouping author may read this projection.

The grouping author remains prohibited from reading the underlying frozen classification artifact or attention provenance.

## 4. Exact private projection schema

Each released event receives exactly one private projection artifact:

    work/grouping_eligibility/<split>/<packet_event_id>.json

Exact schema:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "BIRTH",
      "split": "development|heldout",
      "packet_event_id": "...",
      "eligibility_basis": "FROZEN_PRIMARY_REALIZATION_REQUIRED_TRUE",
      "eligible_item_ids": [
        "..."
      ]
    }

Rules:

    eligible_item_ids are unique
    eligible_item_ids are lexicographically sorted
    every ID exists in the current packet event
    every ID maps through frozen private provenance to one frozen primary classification
    every included primary classification has realization_required=true
    every current-event semantic item with frozen primary realization_required=true is included
    no noneligible ID is included
    no other semantic field is projected

The projection is a deterministic derivative of already-frozen classifications.

It is not a new semantic artifact authored by the grouping model.

## 5. Projection generation and authority

Projection generation is task-owner mechanical work.

It must use only:

    current event unique-item catalog
    frozen private attention provenance needed to identify each semantic item's primary presentation
    frozen classification artifacts for the same key
    deterministic code

It must not use:

    grouping attempt outputs
    grouping reasons
    grouping pair identities
    model inference
    manual semantic judgment
    the other key
    later-event semantic content beyond the event being prepared

The generator must fail closed if:

    an event item lacks a primary mapping
    a primary presentation lacks a frozen classification
    duplicate eligible IDs occur
    any projected ID is outside the current event
    schema or ordering invariants fail

The private projection may be hashed for provenance.

Its digest and exact eligibility set remain private during key construction.

## 6. Independence and construct validity

The amendment does not reveal a hidden answer to the grouping task.

It reveals only the output boundary of the immediately preceding frozen stage for the same logical key author.

The grouping task remains:

    among eligible realization-requiring semantic items,
    which exact pairs are MUST_JOIN,
    MUST_SPLIT,
    or UNCONSTRAINED?

No pair relationship is mechanically supplied.

No candidate pair is supplied.

No grouping reason is supplied.

Every stored pair still requires individual semantic review.

Therefore the amendment changes the stage interface from:

    grouping independently reclassifies endpoint eligibility and is later checked against hidden frozen eligibility

to:

    grouping consumes frozen eligibility as an explicit upstream input and authors only downstream relation truth

This is the selected construct.

## 7. Symmetry across Key A and Key B

The same interface must apply to Key Author B.

Key B must receive only a projection derived from:

    Key B's own frozen classifications

Key B must never receive:

    Key A eligibility projection
    Key A classifications
    Key A grouping artifacts
    Key A pair outcomes
    Key A attention mappings

This preserves cross-key independence.

The projection algorithm and schema must be frozen before Key B begins.

## 8. Development and held-out separation

The amended projection mechanism is frozen now, during development grouping.

For Key A D01 attempt 003:

    create only the D01 development eligibility projection

Do not create or expose D02 or held-out projections yet.

After accepted D01:

    D02 projection may be mechanically created and released

After accepted D02:

    retire the development grouping session
    start held-out grouping in the already-required fresh session
    create/release held-out projections one event at a time

No running held-out pair floor or hidden grouping result is exposed.

## 9. Revised endpoint acceptance gate

The task-owner grouping acceptance gate now verifies:

    every stored endpoint appears in the frozen event eligibility projection

instead of asking the semantic author to independently reproduce the hidden classification and then comparing that reclassification to frozen truth.

The task owner additionally verifies that the projection itself was mechanically generated exactly from the frozen primary realization_required=true classifications.

This preserves the underlying frozen requirement while separating responsibilities correctly:

    classification stage
        owns eligibility

    grouping stage
        owns relation truth among eligible items

No classification repair follows from a grouping disagreement.

## 10. Attempt 001 and attempt 002 disposition

Both earlier D01 attempts remain:

    PRIVATE
    FROZEN
    REJECTED
    NONCANONICAL

They must never be reread by the semantic author.

They must never be mechanically filtered into an accepted result.

Attempt 001's PRE-012 remains quarantined by the existing erratum.

Attempt 002 added no precedent and requires no new precedent erratum.

The attempt-002 artifact is recorded as a rejected attempt in private progress before attempt 003 begins.

## 11. D01 attempt 003 preparation

Before semantic execution, the project owner runs one deterministic private preparation script that:

    verifies the attempt-002 completion boundary
    records attempt 002 as rejected
    creates the D01 eligibility projection from frozen Key A classification truth
    validates exact projection completeness and exclusivity
    preserves all earlier frozen artifacts
    does not expose eligible IDs or counts in console output
    leaves open_grouping_event = null
    sets current_phase = P4_BIRTH_GROUPING_D01_ATTEMPT_003_PREPARED_AWAITING_RELEASE

The preparation step does not itself open D01 attempt 003.

After the owner returns the bounded PASS receipt, the ChatGPT task owner may release a fresh D01 attempt-003 Claude Code session under the existing P4 authorization and this amendment.

## 12. D01 attempt 003 semantic contract

When released, attempt 003 must:

    use a fresh Claude Code session
    read the D01 current-event range
    read the D01 eligibility projection
    treat only eligible_item_ids as grouping endpoints
    never independently relabel endpoint eligibility
    never read prior classification artifacts
    never read attention provenance
    never read attempts 001 or 002
    never read prior transcripts
    preserve all existing MUST_JOIN/MUST_SPLIT semantic tests
    preserve individual pair confirmation
    preserve UNCONSTRAINED-by-absence semantics
    preserve no-padding rule
    write a distinct attempt-003 artifact
    stop before D02

## 13. Deferred capability observation remains active

Research 366's deferred architecture observation remains active:

    capability-scoped, owner-authorized access to private local workspaces
    should be reconsidered during later Project Development System/tooling design

That topic is not part of this amendment's execution mechanics.

## 14. Current boundary

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS
    P3_BIRTH_HELDOUT=PASS
    KEY_A_BIRTH_ATTENTION_QUALITY=PASS

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN_OWNER_AMENDED

    D01_ATTEMPT_001=HOLD_REJECTED
    D01_ATTEMPT_002=HOLD_REJECTED
    D01_ATTEMPT_003_PREPARATION=AUTHORIZED
    D01_ATTEMPT_003_SEMANTIC_EXECUTION=NOT_YET_RELEASED

    D02_RELEASED=false
    HELDOUT_GROUPING_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_RUN_D01_ELIGIBILITY_PROJECTION_PREPARATION
