# Research 321: DRP-01 Shared Semantic Substrate Review Harness Freeze

**Date:** 2026-09-25
**Status:** DRP-01 CORPUS/SEMANTIC REVIEW HARNESS FROZEN / TWO-REVIEWER BLIND ANNOTATION REQUIRED / NO DRP-01 RESULT OBSERVED
**Parent protocol:** Research 316 / AO10-DRP-V01
**Previous valid results:** DRP-09 PASS; DRP-05a PASS; DRP-05b PASS_DETECTIVE_FIRST
**Probe:** DRP-01 Shared Semantic Substrate Sufficiency
**Corpus base:** 870689734673e6e8c2212035afcdf27daf733c15
**Scope:** Freeze the 30-carrier corpus identities, semantic roles/statuses, seam inventory, candidate/negative-control concepts, annotation schema, independent-review protocol and scoring harness before semantic annotations are produced.
**Authority:** Probe harness freeze only. No V0.3 semantic primitive, role vocabulary or status token is accepted by this record.

## 1. Why DRP-01 uses two independent semantic reviewers

DRP-01 is not a purely mechanical probe.

It asks whether:

    two or more bounded domains genuinely require the same primitive meaning
    real mixed carriers can be decomposed into practical semantic units
    the proposed information-role model is reproducible
    domain-internal concepts can remain outside the shared substrate

Those questions require semantic judgment.

A single candidate author grading the same candidate would create avoidable confirmation risk.

Research 321 therefore adds a stricter pre-result requirement to the Research 316 minimum:

    ChatGPT and Claude independently annotate the frozen corpus
    neither reads the other's annotation before committing its own
    final scoring compares both annotations

This does not weaken any Research 316 threshold.

## 2. Frozen corpus

The exact 30 carriers are those preregistered by Research 316.

Every carrier is read from:

    870689734673e6e8c2212035afcdf27daf733c15

not from the moving coordination head.

The corpus manifest stores for each carrier:

    path
    byte length
    SHA-256
    format
    heading count / bounded heading preview

Corpus summary:

    carriers       30
    Markdown       27
    JSON            3
    total bytes    976759

Research 315 remains the candidate under test and is not silently added to the empirical carrier count.

## 3. Frozen information-role model under test

Candidate roles:

    GOVERNING
        durable normative meaning that can constrain project decisions,
        authority, obligations, policy, architecture or procedure

    EVIDENCE
        observation, qualification, analysis or result supporting a
        claim/decision without becoming normative merely by existence

    CONTROL
        current operational/workflow/machine control facts whose ordinary
        transition changes project state

    DERIVED
        rebuildable projection/index/summary/navigation representation that
        is not unique accepted truth

    CAPTURE
        unpromoted candidate/input/capture awaiting governed promotion

A homogeneous carrier may remain one unit.

A mixed carrier is split only into stable, consequential semantic units with durable anchors.

A reviewer must not split a carrier merely to make the candidate role model pass.

## 4. Provisional governing statuses

Only GOVERNING units receive governing status.

The tested vocabulary is:

    PROPOSED
    IN_FORCE
    EFFECT_WITHHELD
    SUPERSEDED
    RETIRED
    REJECTED

These tokens are provisional.

EFFECT_WITHHELD is intentionally chosen instead of HELD or SUSPENDED to avoid immediate collision with AO affected-scope hold, workstream pause and bridge SUSPENDED semantics.

The probe may still conclude that this vocabulary is semantically poor.

## 5. Frozen shared-primitive candidates

    semantic_identity
    exact_subject_revision_binding
    provenance_descriptor
    governing_lifecycle_reference
    obligation_reference
    governed_relation_reference

No primitive is presumed admitted.

For each primitive, each reviewer must define one canonical meaning and judge all nine seams.

A primitive may be admitted only on evidence, not because V0.3 proposed it.

## 6. Frozen domain seams

    S1 knowledge <-> AO authority/reconstruction
    S2 AO <-> WARRANT-F admission
    S3 AO <-> workstream/continuity
    S4 AO <-> collaboration
    S5 AO <-> transition management
    S6 transition <-> Engineering/delivery
    S7 knowledge <-> retrieval/navigation
    S8 assurance <-> evidence/delivery
    S9 evolution <-> governing lifecycle

A seam assertion that consequential correctness requires shared meaning must cite frozen source anchors.

## 7. Frozen negative controls

Reviewers independently judge:

    workstream_state
    bridge_execution_mode
    warrant_claim_internal_state
    stochastic_campaign_statistic

They are called negative controls because V0.3 predicts they remain domain-owned.

The reviewer is explicitly allowed to admit one if the frozen evidence really supports a shared cross-domain contract.

Doing so triggers the preregistered architecture consequence rather than being marked reviewer error.

## 8. Annotation rules

For every carrier, reviewer output contains:

    path
    one or more semantic units
    stable anchor per unit
    one candidate role
    governing status or null
    concise rationale
    irreducibly_multirole flag
    path-used-as-identity-or-authority flag

For every primitive:

    admitted
    canonical meaning
    all S1-S9 judgments
    source references for required shared seams
    semantic-conflict flag

Long copied source passages are not required.

Stable repository references use:

    repository/path::heading-or-json-field

## 9. Frozen scoring

Research 316 criteria remain:

    each admitted primitive >= 2 consequential seam citations
    coherent meaning across admitted seams
    all four domain-internal controls rejected
    no incompatible shared definition
    role representability >= 90% of carriers
    carriers needing >4 units solely for role model <= 25%
    irreducibly multi-role units <= 10%
    path-as-identity/authority misuse = 0

Research 321 adds one independent-review robustness criterion before any annotation exists:

    Jaccard agreement between reviewer admitted-primitive sets >= 0.80

If the reviewers cannot substantially agree on what belongs in the shared substrate under the same frozen definitions/evidence, the substrate boundary is not deterministic enough for the proposed contract.

Primary class:

    PASS
        both reviewer-specific Research 316 checks pass
        AND admission-set Jaccard >= 0.80

    AMEND
        otherwise, provided annotations/harness are valid

    HARNESS_INVALID
        annotation schema/evidence boundary/blinding is violated

## 10. Independence sequence

Sequence is frozen as:

    1. commit Research 321 + harness
    2. ChatGPT produces annotation A without Claude annotation
    3. commit/freeze ChatGPT annotation A
    4. Claude receives reviewer packet and frozen corpus instructions
    5. Claude must not inspect annotation A before committing annotation B
    6. validate both annotations
    7. execute frozen comparison harness
    8. reconcile result

Claude's current conversation may be reused.

The independence requirement is about annotation exposure, not chat freshness.

## 11. Harness

    experiments/ao10_drp01_shared_semantic_substrate_v01/corpus.json
        sha256 cf418fd79a1ee563bc0e9ff3fb303dcbc354b7b173031948aee5b8588ed5166c

    definitions.json
        sha256 84415717fc1c8d250c5b5a38fff7ec995f027770777d8828b9906e0199c136a0

    annotation_schema.json
        sha256 a9632ac16a1d5b86402eef0e62858c1cd190dd42e17f34b25bd3572a1ca4f17f

    REVIEWER_PACKET.md
        sha256 d33d0bbe036a3b006083c8112a03a04999d73f13c3165b188cd4ea11184570cb

    probe.py
        sha256 81d120453bcbf3b2fd4855ddfddeaea8aa8ee7d79b4528af2dc7ab0f4d2ff256

Pre-execution validation:

    Python AST parse       PASS
    JSON fixture parse     PASS

No semantic annotation has been scored.

## 12. Current boundary

    DRP09=PASS
    DRP05A=PASS
    DRP05B=PASS_DETECTIVE_FIRST

    DRP01_CORPUS=FROZEN_30
    DRP01_HARNESS=FROZEN
    DRP01_CHATGPT_ANNOTATION=NOT_STARTED
    DRP01_CLAUDE_ANNOTATION=NOT_STARTED
    DRP01_RESULT=NONE

    OWNER_DECISION=HELD
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=DRP01_CHATGPT_BLIND_ANNOTATION
