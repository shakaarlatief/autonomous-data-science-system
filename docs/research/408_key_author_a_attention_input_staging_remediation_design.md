# Research 408: Key Author A Attention-Input Staging Remediation Design

**Date:** 2026-09-29
**Status:** REMEDIATION DESIGN FROZEN BEFORE LIVE ATTENTION METRIC / IMPLEMENTATION AND QUALIFICATION NEXT
**Parent:** Research 407
**Scope:** Freeze the bounded remediation for the missing private LEGACY attention-provenance input discovered by the first live `evaluate_attention` dispatch, without inspecting private semantic data or changing any frozen gate semantics.
**Authority:** Input-staging remediation design only. This record does not execute the attention gate, expose hidden mapping identities, modify semantic labels, authorize replacement, authorize candidate-gap/evidence/grouping work, assemble Key A, generate a commitment, authorize Key Author B, score DRP-03, implement the successor architecture, or migrate repository state.

## 1. Observed failure

After host tool metadata refresh, the purpose-specific Runtime Bridge action:

    evaluate_attention

was dispatched successfully to Codexless.

The operation failed before evaluation with:

    errorCode = ENOENT

for the fixed private target:

    %LOCALAPPDATA%/ADS-R2-KeyAuthor-A/inputs/r2_v03/packets/legacy_attention_provenance.json

No live metric was returned or observed.

No hidden attention mapping, label, semantic-item identity, presentation identity, private denominator or pair identity was exposed.

The failure is therefore an input-staging defect, not a quality-gate result.

## 2. Cause

Research 406 correctly froze the evaluator against a fixed private copy of the LEGACY attention provenance.

The earlier P5 classification preparation intentionally did not place that mapping inside the Key Author A semantic-author workspace because the semantic author was forbidden from seeing attention identities during classification.

After all 18 classification batches froze, the mapping became eligible for mechanical use only, but the qualified V4 evaluator assumed the post-classification private copy already existed.

That assumption was false.

## 3. Frozen remediation

The public repository already contains the exact preregistered provenance carrier:

    experiments/ao10_drp03_obligation_units_r2_v03/packets/legacy_attention_provenance.json

Its frozen identity is:

    SHA-256  bfc35235ab1aa0a325018fe66c03b14facf43f9ab710ec587ad3901850b459f6
    bytes    540084

The remediation must remain inside the purpose-specific Runtime Bridge control plane.

No generic shell copy into the private Key Author A workspace is authorized.

Instead, the bounded evaluator will internally ensure the fixed private copy before evaluation:

    if the private target exists:
        require exact frozen SHA-256
        otherwise fail closed

    if the private target is absent:
        read only the fixed public provenance carrier
        require exact frozen SHA-256
        create the exact fixed private parent path
        stage the bytes to a fixed temporary sibling
        atomically rename into the exact private target
        re-read and require the same frozen SHA-256
        expose no file content

The operation remains zero-choice from the caller's perspective:

    action = evaluate_attention

No new caller-selected path, source, destination, ID, threshold, denominator or mapping is introduced.

## 4. Independence and semantic integrity

The remediation does not weaken the frozen blindness model.

The Key Author A semantic sessions are complete and remain frozen.

The attention mapping is still never returned to the semantic author.

The staged bytes are public preregistered protocol bytes, not Key Author A semantic labels.

The private copy exists only so the bounded mechanical evaluator can join those fixed control identities to already-frozen accepted Key A artifacts.

No label repair, semantic rerun, selective rerun-to-green or semantic-model intervention is permitted.

## 5. Qualification requirements

Before another live gate dispatch, the updated release must demonstrate at minimum:

    V4 attention behavior retained when private input already exists
    missing-private-input staging succeeds from exact frozen source
    staged private bytes exactly match frozen SHA-256
    source digest drift fails closed
    pre-existing private digest drift fails closed
    no caller-selectable path/source/destination
    valid PASS fixture
    binary threshold failure
    normative-kind threshold failure
    empty normative-kind denominator
    malformed mapping
    ambiguous/missing primary
    accepted-artifact digest drift
    incomplete accepted prefix
    wrong progress phase
    bounded non-disclosure
    idempotent stored result
    retained P5 classification behavior
    retained P4 behavior
    public-surface registration
    governed managed-release regressions

No live Key A metric may be observed during remediation implementation or staged qualification.

## 6. Exact next step

Create a successor managed runtime release from V4, implement only the bounded staging remediation, run the frozen regression suite, commit and synchronize the local-runtime repository, then use the managed release pipeline to prepare, publish, verify and activate it.

Only after successful activation may `evaluate_attention` be dispatched again.

    ATTENTION_INPUT_STAGING_REMEDIATION=FROZEN
    LIVE_ATTENTION_METRIC_OBSERVED=false
    KEY_A_LABELS_CHANGED=false
    NEXT=IMPLEMENT_QUALIFY_PUBLISH_AND_ACTIVATE_ATTENTION_STAGING_REMEDIATION
