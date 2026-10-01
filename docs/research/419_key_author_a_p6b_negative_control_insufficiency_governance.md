# Research 419: Key Author A P6B Negative-Control Insufficiency Governance

**Date:** 2026-10-01
**Status:** P6B FINALIZED / EVIDENCE_INSUFFICIENT / NEGATIVE-CONTROL CHECK FAILED / GOVERNANCE REQUIRED
**Parent:** Research 418
**Scope:** Reconcile the completed Key Author A P6B execution with its frozen postflight gate and identify the next legitimate governance question without inspecting hidden Key A semantic outputs.
**Authority:** Diagnostic and governance-boundary research only. This record does not authorize P5/P6 semantic repair, a same-corpus semantic retry, P6C, canonical Key A assembly, Key A commitment, Key Author B, construct comparison, scoring, successor implementation, migration, oracle retirement, or authority switching.

## 1. P6B execution completed cleanly

After the governed replacement preserved the first three accepted P6B sources, the automated P6B runner completed all seventeen frozen sources.

The bounded completion state was:

    P6B runner = COMPLETE
    accepted sources = 17 / 17
    HOLD = false
    error = null
    hidden semantic details exposed = false

The task owner then invoked the frozen bounded finalize_subphase operation.

## 2. Frozen P6B finalization result

The purpose-specific control plane returned:

    finalizedSubphase = P6B
    subphaseResult = EVIDENCE_INSUFFICIENT

    materialGapWitnessFloorMet = true
    alreadyRealizedControlFloorMet = true
    negativeControlSourceCheckPass = false

    hiddenSemanticDetailsExposed = false
    next = GOVERNED_EVIDENCE_INSUFFICIENCY

The control plane then moved to:

    p6_current_subphase = null
    current phase = P6B_EVIDENCE_INSUFFICIENT_AWAITING_GOVERNANCE
    runner = IDLE

Therefore P6C is not runnable under the currently qualified control plane.

## 3. What failed and what did not

The two positive evidence floors passed:

    hidden material-gap witness floor >= 6
    already-realized false-gap control floor >= 10

The insufficiency is isolated to the frozen source-level negative-control condition.

The qualified implementation derives that condition mechanically from the already-frozen P5 unique classification projection and the frozen public negative-control source mapping. It checks whether any item on either hidden negative-control source is simultaneously:

    normative = true
    realization_required = true

The failure therefore does not establish that P6B repository evidence resolution was defective.

It also does not justify changing any P6A candidate-gap value, P6B evidence result, P5 label, negative-control source identity, corpus membership, threshold, or source role.

No negative-control identity, affected item identity, semantic label, candidate-gap value, evidence disposition, witness identity, control identity, or transcript content has been exposed to ChatGPT during this reconciliation.

## 4. This is not currently classified as HARNESS_INVALID

The observed mechanical check matches the frozen R2 protocol requirement that negative-control realization units equal zero.

Research 330 freezes:

    2 negative-control sources required
    negative-control realization units = 0

Research 410 freezes the post-classification rule that failed evidence qualification stops progression and forbids label repair, evidence-result rewriting, selective rerun-to-floor, and canonical Key A commitment.

The runtime behavior therefore matches the accepted design.

No evidence currently supports reclassifying the result as a runtime implementation defect merely because the empirical result is unfavorable.

## 5. Retry-to-green remains prohibited

The following are not legitimate responses:

    rerun P5 classification
    rerun selected negative-control sources
    change a realization_required label
    selectively rerun P6A or P6B
    reveal hidden negative-control identities to a semantic author
    replace the negative-control sources
    lower or remove the zero-realization requirement
    widen the evidence horizon
    continue into P6C by bypassing the purpose-specific control plane

Research 330 permits a second historical attempt only for HARNESS_INVALID.

That condition has not been established.

## 6. Newly exposed component-boundary tension

The failure exposes a real protocol-orchestration question that was not previously exercised.

Research 330 freezes component-level consequence separation:

    BIRTH, STATE, and LEGACY are independently classified

and specifically:

    LEGACY does not gate V0.7 BIRTH/STATE owner-decision readiness

while LEGACY does gate:

    obligation-unit lineage
    legacy migration/reconciliation assistance
    oracle-retirement uses that depend on legacy units

However, the later Research 410 P6 control plane stops before canonical Key A commitment whenever the LEGACY evidence gate is insufficient.

Research 332 also freezes a monolithic concealment sequence:

    Key A canonical bytes
    -> Key A commitment
    -> Key B canonical bytes
    -> Key B commitment
    -> construct-validity comparison

If a failed LEGACY hidden control prevents any Key A commitment, then the current orchestration can indirectly prevent BIRTH/STATE construct-validity work from reaching Key B even though Research 330 says LEGACY should not gate BIRTH/STATE owner-decision readiness.

This is not evidence that either rule should simply be ignored. It is a newly observed interaction between two accepted rules that requires explicit reconciliation.

## 7. Candidate governance paths

### Path A: terminate the entire R2 key-construction sequence

This follows Research 410 most literally.

Consequence:

    Key A commitment remains absent
    Key B does not start
    BIRTH/STATE construct comparison does not occur

Risk:

    LEGACY thereby becomes a procedural gate on BIRTH/STATE despite Research 330's component-independence rule.

### Path B: prospective component-bounded continuation amendment

Preserve the failed LEGACY result permanently, with no semantic retry or repair, but amend only the post-result packaging/orchestration boundary so that failed LEGACY cannot silently block independent BIRTH/STATE construct-validity work.

A safe version would require all of the following:

    Key A semantic bytes remain exactly frozen
    LEGACY negative-control failure remains permanently recorded
    no LEGACY qualification claim is made
    no LEGACY reviewer scoring is enabled from the failed component
    no obligation-unit lineage or LEGACY migration authority is unlocked
    Key B remains blind to Key A
    any Key A commitment is explicitly non-qualifying for failed LEGACY
    BIRTH/STATE comparison is allowed only if the amendment is accepted before Key B execution
    the amendment cannot improve or erase the observed LEGACY result

This path would be a substantive protocol amendment after an observed outcome. It therefore cannot be silently enacted by the task owner.

### Path C: semantic repair or same-corpus retry

This would attempt to make the negative-control check pass by changing semantic outcomes or selectively rerunning work.

Disposition:

    PROHIBITED

## 8. Preliminary governance recommendation

The strongest next step is not a retry and not immediate P6C execution.

The next step should be an explicit review of whether a narrowly quarantined, component-bounded continuation can reconcile:

    Research 330 component independence
    Research 332 dual-key concealment order
    Research 410 no-retry / no-commit-on-insufficiency rule
    the already-observed failed LEGACY negative-control result

Any amendment must preserve the unfavorable LEGACY result exactly rather than converting it into PASS.

Until that reconciliation is accepted:

    P6C remains NOT STARTED
    Key A canonical assembly remains NOT AUTHORIZED
    Key A commitment remains NOT AUTHORIZED
    Key Author B remains NOT AUTHORIZED
    construct comparison remains NOT STARTED
    reviewer scoring remains NOT STARTED

## 9. Current boundary

    KEY_A_P6A = PASS / FROZEN
    KEY_A_P6B_EXECUTION = 17_OF_17_ACCEPTED
    KEY_A_P6B_FINALIZATION = EVIDENCE_INSUFFICIENT
    MATERIAL_GAP_WITNESS_FLOOR = PASS
    ALREADY_REALIZED_CONTROL_FLOOR = PASS
    NEGATIVE_CONTROL_SOURCE_CHECK = FAIL
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    KEY_A_P6C = NOT_STARTED
    KEY_A_CANONICAL_ASSEMBLY_AUTHORIZED = false
    KEY_A_COMMITMENT_AUTHORIZED = false
    KEY_AUTHOR_B_AUTHORIZED = false

    SAME_CORPUS_SEMANTIC_RETRY = PROHIBITED
    NEXT = GOVERNED_COMPONENT_BOUNDARY_RECONCILIATION
