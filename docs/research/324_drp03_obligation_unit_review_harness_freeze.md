# Research 324: DRP-03 Obligation-Unit Review Harness Freeze

**Date:** 2026-09-25
**Status:** DRP-03 REVIEW HARNESS FROZEN / CLAUDE INDEPENDENT REVIEWER A NEXT / NO DRP-03 RESULT OBSERVED
**Parent protocol:** Research 316 / AO10-DRP-V01
**Previous valid results:** DRP-09 PASS; DRP-05a PASS; DRP-05b PASS_DETECTIVE_FIRST; DRP-01 PASS
**Probe:** DRP-03 Obligation-Unit Granularity and Birth
**Source base:** 870689734673e6e8c2212035afcdf27daf733c15
**Scope:** Freeze the source set, realization-state derivation, annotation schema, proposition/grouping comparison method, hidden false-gap/evaluator key, known-witness contract and reviewer independence boundary before either DRP-03 reviewer annotation is produced.
**Authority:** Probe harness freeze only. No obligation-unit granularity, realization mapping or V0.3 amendment is accepted by this record.

## 1. Probe purpose

DRP-03 tests two failure modes at once:

    accepted obligation exists
        but nobody delimits it
        -> upstream KA-R52 blind spot

    accepted obligation is already realized
        but the traceability model calls it missing
        -> false gap / adoption noise

The probe therefore evaluates:

    normative proposition detection
    ObligationUnit grouping
    realization-state derivation
    known-gap sensitivity
    false-gap specificity
    negative-control behavior

## 2. Frozen source set

Primary accepted events:

    Research 217
    Research 235
    Research 256
    Research 259
    Research 272
    Research 311

Governing trace source:

    Specification 028
    only the exact review headings frozen in review_scope.json

Supplemental known-witness source:

    Research 225 section 16
    AO-6 branch rotation / attach-switch realization gap

Negative controls:

    Research 308
    Research 314

Support realization evidence:

    Research 193
    Research 202
    Research 203
    Research 204
    Research 205

Every source is bound to protocol base 870689734673e6e8c2212035afcdf27daf733c15 by SHA-256 in review_scope.json.

## 3. Frozen implementation snapshot

The harness includes a base-bound listing of tools/project_knowledge.

For Specification 028 section 3, the named package surface at the frozen base includes the existing modules plus these exact absent module names:

    reconstruction.py
    migration.py
    validation.py
    git.py

This is only a sensitivity fact.

The reviewer must still judge semantic obligation/realization meaning rather than equating filename absence with architecture failure.

## 4. Obligation-unit rule

The frozen rule remains Research 315/316:

    ObligationUnit
        =
    smallest semantic group of accepted normative propositions
    sharing one realization boundary and one evidence path

Reviewers must not:

    create units merely because the word MUST appears
    omit units merely because MUST is absent
    merge propositions whose realization/evidence paths differ
    split propositions merely to maximize agreement

## 5. Fully derived realization state

Reviewers do not author RealizationState.

They provide source facts:

    realization_relation_refs
    deferral_refs
    evidence_refs
    qualification_refs
    activation_refs

The harness derives:

    deferral present                         -> DEFERRED
    no realization relation                 -> UNLINKED
    relation but no evidence                 -> LINKED
    evidence but no qualification            -> EVIDENCED
    qualification but no activation          -> QUALIFIED
    all required realization facts           -> OPERATIONAL

Seven frozen state fixtures verify this derivation, including deferral precedence.

## 6. Independent proposition comparison

Both reviewers independently write normalized propositions close to source wording.

A proposition match requires:

    same source
    same exact source heading
    max(token Jaccard, sequence similarity) >= 0.58

One-to-one matching is greedy by descending similarity.

Frozen proposition-set threshold:

    F1 >= 0.85

The harness does not use a later hand-built reconciliation to improve this score.

## 7. Independent unit-grouping comparison

For matched propositions, the harness compares whether each reviewer places every proposition pair in the same or different ObligationUnit.

Frozen metric:

    pairwise same-unit F1

Frozen threshold:

    >= 0.70

If neither reviewer groups any comparable proposition pair together, the degenerate score is 1.0.

## 8. Known sensitivity witnesses

Research 316 requires both reviewers to surface three known witness families:

    Specification 028 section-3 named-responsibility realization gap
    AO-6 branch rotation / attach-switch realization gap
    Research 311 Engineering obligations despite zero uppercase MUST tokens

The reviewer packet exposes the witness tags because the protocol itself preregistered these sensitivity witnesses.

Their existence is not hidden-test evidence.

## 9. Hidden specificity/evaluator key

A separate evaluator key is frozen before reviewer work.

It contains:

    ten already-realized W0-W4 false-gap controls
    exact matching/evidence expectations
    seven realization-state derivation fixtures

Claude reviewer A must not inspect evaluator_key.json before committing its annotation.

This strengthens the false-gap result beyond the minimum Research 316 requirement.

ChatGPT, as harness author, is not independent of the hidden key. Therefore reviewer-specific false-gap interpretation will explicitly distinguish:

    Claude blind specificity evidence
    ChatGPT corroborating reviewer evidence

The final primary rule still follows the frozen harness and requires both reviewers to remain within the <=10% false-gap bound.

## 10. Reviewer sequence

Frozen sequence:

    1. commit Research 324 + harness
    2. Claude produces reviewer A
       blind to evaluator_key.json
       blind to future ChatGPT annotation
    3. freeze Claude reviewer A
    4. ChatGPT independently annotates without reading Claude A
    5. freeze ChatGPT reviewer B
    6. validate both
    7. run frozen comparison harness
    8. reconcile DRP-03 result

ChatGPT must not inspect Claude reviewer A before completing reviewer B.

The reviewer order is intentionally reversed from DRP-01 so the reviewer who did not author Research 315/316 also remains blind to the specificity key.

## 11. Frozen harness artifacts

    experiments/ao10_drp03_obligation_units_v01/review_scope.json
        sha256 02bea4deb610c3792388219f549fd2c2b59238cb3ca91d58a8cd6a4c0cb0d01f

    implementation_snapshot.json
        sha256 aae5277cca7a7d9fe6a974d92829ba5205618966c09135ffa55115d345c21db0

    definitions.json
        sha256 93412c206efc046cf0311c08bf75c1a043f91719db9b1d6aaaa4ad821519e6b9

    annotation_schema.json
        sha256 e4173fc8bb7c2bbe052b6f1948ec20ef37acce2d83d00804d78a5462bf19c426

    evaluator_key.json
        sha256 1a6049938d9751c6fd476621870c54c85875899e7fe748354d95bffbc4aebb42

    REVIEWER_PACKET.md
        sha256 4bd96830f400e948764246e25697ba7169e5ef50b751d1e6a4dc9ed8d84632c5

    probe.py
        sha256 f082f3f75d17c485d5d8e70d6e169cb17e69e2639b85541146f631aeb15092b7

Pre-execution validation:

    Python AST parse       PASS
    JSON fixture parse     PASS

No reviewer annotation exists and no comparison has run.

## 12. Current boundary

    DRP09=PASS
    DRP05A=PASS
    DRP05B=PASS_DETECTIVE_FIRST
    DRP01=PASS

    DRP03_HARNESS=FROZEN
    DRP03_CLAUDE_REVIEWER_A=NOT_STARTED
    DRP03_CHATGPT_REVIEWER_B=NOT_STARTED
    DRP03_RESULT=NONE

    OWNER_DECISION=HELD
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=CLAUDE_DRP03_BLIND_REVIEWER_A
