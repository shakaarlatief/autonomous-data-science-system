# Research 409: Key Author A LEGACY Attention Gate Pass

**Date:** 2026-09-29
**Status:** STAGING REMEDIATION QUALIFIED / LIVE LEGACY ATTENTION GATE PASS / NO REPLACEMENT REQUIRED
**Parent:** Research 408
**Scope:** Preserve qualification and activation of the bounded missing-input staging remediation and the resulting post-P5 Key Author A LEGACY attention-consistency gate outcome.
**Authority:** Mechanical attention-quality disposition only. This record does not authorize label repair, candidate-gap/evidence/grouping execution, canonical Key A assembly, commitment generation, Key Author B, scoring, successor implementation, migration, oracle retirement, or authority switching.

## 1. Remediation qualification

Research 408 prospectively froze the remediation before any live attention metric was observed.

The successor managed Runtime Bridge release is:

    release ID             p5-private-ops-v5
    target version         0.1.1-preview.55-p5-attention-staging-public
    public surface         codexless-public-preview-v2
    public tool count      174
    release manifest SHA   04c135a34c6b44ed7f814ed21583bda538aae414417b3c748d24e8afbc5c11b5
    local-runtime commit   be36965d4a0e507212fcf16deea56ee19a7f1057

The local-runtime repository was synchronized with origin.

Direct qualification returned:

    P5_PRIVATE_OPS_REGRESSION=PASS
    batches=18
    presentations=3210
    attentionPairs=122

and retained:

    P4_PRIVATE_OPS_REGRESSION=PASS

The P5 regression now includes both prior attention-gate cases and the Research 408 remediation cases:

    missing fixed private input stages from the exact frozen source
    staged bytes match the frozen SHA-256
    already-present exact private bytes remain accepted
    public source digest drift fails closed
    pre-existing private target digest drift fails closed
    missing public source fails closed
    no caller-selected staging path/source/destination exists

The release's complete governed regression set ran in the managed publication environment.

Managed publication completed successfully:

    operation               rm_72f1ffc68f1b38e0ca5a4e006943fc77
    status                  succeeded

Verification returned:

    status                  verified
    mismatchCount           0

Runtime activation completed successfully:

    operation               rm_0f9397a733ed11626d78a18732eadfc5
    status                  succeeded
    recoveryAttempted       false

Post-activation release verification again returned:

    status                  verified
    mismatchCount           0

## 2. Live bounded gate

After V5 activation, the task owner invoked only the purpose-specific bounded action:

    action = evaluate_attention

No caller-selected batch, path, mapping, ID, threshold, denominator, session, attempt, or semantic content was supplied.

The evaluator internally staged the exact preregistered provenance bytes only because the fixed private copy was missing, revalidated the accepted 18-batch surface, and returned the bounded aggregate receipt:

    gate                         PASS
    binaryConsistency            1.0
    binaryConsistencyPass        true
    normativeKindConsistency     1.0
    normativeKindConsistencyPass true
    replacementRequired          false
    hiddenSemanticDetailsExposed false

A second identical bounded call returned the same stored receipt, confirming live idempotent readback rather than a different disposition.

No presentation ID, semantic-item ID, attention-pair identity, private denominator, individual semantic label, witness identity, or control identity was exposed.

## 3. Disposition

Both preregistered Research 330 quality thresholds pass:

    binary normative consistency
        1.0 >= 0.95

    normative-kind consistency
        1.0 >= 0.90

Therefore:

    KEY_A_LEGACY_ATTENTION_QUALITY=PASS
    QUALITY_REPLACEMENT_REQUIRED=false
    LABEL_REPAIR_AUTHORIZED=false
    FROZEN_P5_LABELS=UNCHANGED

The earlier V4 ENOENT event remains historical execution evidence and is not a failed semantic quality result.

## 4. New eligibility boundary

Research 384 states that attention PASS makes the unique LEGACY catalog eligible for a later prospectively designed candidate-gap/evidence/grouping phase.

Eligibility is not authorization.

The next phase must therefore be designed before any new semantic authoring or provenance/evidence exposure.

That design must bind the already-frozen requirements for:

    unique semantic-item reconstruction
    candidate_gap
    evidence_refs
    frozen LEGACY evidence horizon
    independent repository evidence
    hidden material-gap witnesses
    already-realized false-gap controls
    the two frozen source-level negative controls
    within-source MUST_JOIN / MUST_SPLIT grouping
    individual confirmation of constrained pairs
    no cross-source grouping
    no pair padding

The exact lifecycle, batching, semantic-session strategy, private-control-plane operations, exposure boundaries and automation strategy remain to be designed prospectively.

The owner's previously identified orchestration-cost requirement is now explicitly relevant: the next phase should preserve semantic independence and evidence integrity without reintroducing unnecessary manual clipboard, scheduling, or deterministic bookkeeping loops.

    KEY_A_P5_CLASSIFICATION=COMPLETE
    KEY_A_LEGACY_ATTENTION_QUALITY=PASS
    KEY_A_LEGACY_REPLACEMENT_REQUIRED=false
    KEY_A_POST_CLASSIFICATION_LEGACY=ELIGIBLE_NOT_AUTHORIZED
    KEY_AUTHOR_B_AUTHORIZED=false
    NEXT=DESIGN_POST_CLASSIFICATION_LEGACY_PHASE_PROSPECTIVELY
