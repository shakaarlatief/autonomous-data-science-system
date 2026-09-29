# Research 407: Key Author A LEGACY Attention Evaluator Qualified and Activated

**Date:** 2026-09-29
**Status:** BOUNDED ATTENTION EVALUATOR QUALIFIED / PUBLISHED / ACTIVATED / LIVE GATE NOT YET EXECUTED
**Parent:** Research 406
**Scope:** Preserve implementation, regression qualification, publication, verification and activation of the prospectively frozen Key Author A LEGACY attention-quality evaluator without observing the live Key A attention metric.
**Authority:** Mechanical evaluator qualification and activation only. This record does not execute the live attention gate, expose hidden mapping identities, modify semantic labels, authorize replacement, authorize candidate-gap/evidence/grouping work, assemble Key A, generate a commitment, authorize Key Author B, score DRP-03, implement the successor architecture, or migrate repository state.

## 1. Qualified implementation

Research 406 froze the evaluator design before any live Key A attention metric was observed.

The implementation was prepared in the managed `ads-local-runtime` repository as release:

    release ID             p5-private-ops-v4
    target version         0.1.1-preview.54-p5-attention-public
    public surface         codexless-public-preview-v2
    public tool count      174
    release manifest SHA   2f242c57b58c24f1214a1190fae8cfd51198a43c01459e7eac5b19091f269759
    local-runtime commit   699a2927f81ba8569444a1707e9ed578f1f00ef4

The local-runtime commit was pushed and synchronized with `origin/main`.

The existing purpose-specific `codex.p5_private_operation` service is extended with one bounded action:

    evaluate_attention

It accepts action only. It accepts no caller-selected:

    path
    presentation ID
    semantic-item ID
    label
    mapping
    threshold
    denominator
    batch
    attempt
    session
    command

The implementation binds the frozen LEGACY attention-provenance SHA-256 from Research 406, revalidates all 18 accepted artifacts and acceptance records, reconstructs the 122 exact duplicate-primary attention pairs mechanically, applies the frozen 0.95 / 0.90 gates using integer threshold comparisons, persists only the bounded aggregate disposition, and returns no hidden pair identity or private denominator.

## 2. Regression qualification

Direct staged regression results included:

    P5_PRIVATE_OPS_REGRESSION=PASS
        batches=18
        presentations=3210
        attentionPairs=122

    P4_PRIVATE_OPS_REGRESSION=PASS

The P5 regression suite covers:

    valid attention PASS
    binary-threshold failure
    normative-kind-threshold failure
    empty normative-kind denominator
    malformed attention mapping
    missing/ambiguous primary mapping
    frozen attention digest drift
    accepted-artifact digest drift
    incomplete accepted prefix
    wrong progress phase
    caller attempt to widen evaluate_attention inputs
    bounded-result non-disclosure
    idempotent stored result
    retained P5 classification behavior

The release's governed regression set also retains:

    P4 private-operation regression
    public-surface registration
    flexible-authority regression
    bounded Git fetch regression
    bounded Git pull-ff-only regression
    runtime-release regression
    runtime-release dependency integration

Managed release publication completed successfully. Because the release mechanism runs the fixed staged/live regression contract before atomic publication, successful publication is the governed full-regression qualification receipt.

## 3. Publication and activation

Managed release preparation returned PASS-equivalent `prepared`.

Managed publication completed:

    status                  succeeded
    operation               rm_b0560984dbd38b2767304326ed238d7f

Verification returned:

    status                  verified
    mismatchCount           0

The bounded Runtime Bridge restart then completed successfully:

    operation               rm_827c8e7e47633b848c035428e83a16a5
    status                  succeeded
    recovery attempted      false

A post-activation release verification again returned:

    status                  verified
    mismatchCount           0

Therefore the new runtime bytes are qualified, published and activated.

## 4. Live gate remains unobserved

No live Key A attention evaluation has run.

After activation, this already-running ChatGPT turn still held the pre-release cached tool schema, whose client-side enum did not include `evaluate_attention`. An attempted bounded invocation was rejected by that stale host schema before reaching the Runtime Bridge operation.

This is a host tool-schema refresh condition, not a gate result and not an evaluator failure.

It caused:

    no private mapping read by the semantic author
    no live attention metric observation
    no PROGRESS attention disposition write
    no semantic label mutation
    no candidate-gap/evidence/grouping execution

The scientific pre-result boundary therefore remains intact.

## 5. Exact next step

The next ChatGPT turn/session with refreshed Runtime Bridge tool metadata must confirm that `codex.p5_private_operation` exposes:

    evaluate_attention

Then the task owner may invoke exactly:

    action = evaluate_attention

No additional semantic author session is required for this mechanical gate.

Only the bounded aggregate receipt may be recorded publicly.

On PASS:

    post-classification LEGACY work becomes eligible for prospective phase design
    it is not automatically authorized

On FAIL:

    no label repair or selective rerun is permitted
    replacement governance is required

The owner's Key Author B execution requirement remains active: preserve the independent semantic safeguards while eliminating unnecessary manual clipboard, scheduling and deterministic bookkeeping work.

    KEY_A_P5_CLASSIFICATION=COMPLETE
    KEY_A_P5_ATTENTION_EVALUATOR=QUALIFIED_ACTIVATED
    KEY_A_P5_LIVE_ATTENTION_METRIC_OBSERVED=false
    KEY_A_POST_CLASSIFICATION_LEGACY_AUTHORIZED=false
    KEY_AUTHOR_B_AUTHORIZED=false
    NEXT=EXECUTE_BOUNDED_LEGACY_ATTENTION_GATE_AFTER_HOST_SCHEMA_REFRESH
