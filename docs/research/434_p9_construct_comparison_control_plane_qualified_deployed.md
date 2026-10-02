# Research 434: P9 construct-comparison control plane qualified and deployed

**Date:** 2026-10-02
**Status:** P9 QUALIFIED / DEPLOYED / VERIFIED / LIVE COMPARISON NOT RUN
**Parent:** Research 433
**Scope:** Implement, qualify, publish, activate and verify the purpose-specific model-free STATE+BIRTH construct-comparison control plane frozen by Research 433.
**Authority:** Mechanical comparison-control implementation and deployment only. This record does not expose hidden Key A or Key B item-level semantics, perform the live construct comparison, adjudicate disagreements, create the final private key, run decision reviewers, score DRP-03, implement production AO-10, migrate repository state, retire an oracle, or switch authority.

## 1. V1 implementation and failed publication

The first immutable implementation release was committed at private local-runtime source:

    de409fee98f38526578bed257e452c2fafd68534

as:

    p9-construct-comparison-v1
    target version 0.1.1-preview.71-p9-construct-comparison
    target tools   178
    manifest SHA   38bd46ac71fed12649ae9ae39dd3b540b3239fea7f933cdcdf8bb623ac90d904

Managed preparation passed.

Managed publication then failed closed with:

    RUNTIME_RELEASE_REGRESSION_FAILED

Mechanical staging reproduction identified the failure as an inherited public-surface cardinality expectation in:

    test/bounded-git-fetch-origin.mjs
    test/bounded-git-pull-ff-only.mjs

Both tests still expected the pre-P9 public tool count of 177. The new purpose-specific P9 tool correctly raises the surface count to 178.

This was a release-regression compatibility failure, not a semantic comparison result, not a Key A or Key B artifact failure, and not evidence about construct validity.

V1 remains immutable as the failed release attempt.

## 2. Prospective V2 repair

A fresh V2 release was created without mutating V1.

The only additional repair is the mechanically necessary public-surface cardinality update in the two inherited bounded-Git regressions:

    expected public tools 177 -> 178

No bounded-Git behavior, authority rule, path rule, remote rule, ref rule, mutation behavior or semantic behavior changed.

V2 private local-runtime source:

    4596045e4dab239dca931c7027e17f4e83790877

Release:

    p9-construct-comparison-v2
    target version    0.1.1-preview.72-p9-construct-comparison
    surface           codexless-public-preview-v2
    target tool count 178
    manifest SHA-256  02f0f7978ec16592681c6c14104ea8f9f58301c76c2affde227be9c7503b60f5

## 3. P9 implementation boundary

The deployed control plane exposes one purpose-specific action-only tool:

    codex.p9_construct_comparison_operation

with:

    status
    run_comparison

The caller cannot choose key roots, comparison root, paths, items, events, fixtures, labels, grouping pairs, thresholds, formulas, output paths or comparison scope.

The implementation is model-free and invokes no semantic model.

It binds server-side to the exact frozen STATE+BIRTH commitments:

    Key A = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb
    Key B = fe12b806ff28d81171af87d435172495f51a6f45c2164f2eecbc8b58f2f23e84

It verifies exact hashes, byte lengths, canonical serialization, public bindings, event/item/fixture alignment, item and STATE structures, and grouping-pair invariants before computing any agreement metric.

Its public-safe result excludes item-level labels, disagreement item IDs, STATE answers, fact partitions, grouping pairs/reasons, private paths and canonical key bytes.

## 4. Metric and outcome implementation

The implementation follows Research 433:

    normative prevalence per author
    binary normative Cohen kappa
    normative positive specific agreement
    normative-kind Cohen kappa
    material positive specific agreement
    grouping-constraint agreement over the constrained-pair union
    per-event and overall ambiguity accounting
    STATE-REF material structural comparison

Required gates fail closed when undefined.

STATE-REF excludes free-text reason from material equality.

The only public bounded outcomes are:

    CONSTRUCT_UNDERDETERMINED
    CONSTRUCT_GATE_PASS_OWNER_ADJUDICATION_REQUIRED
    CONSTRUCT_GATE_PASS_NO_MATERIAL_ADJUDICATION_REQUIRED

P9 never creates a final key or performs owner adjudication.

## 5. Qualification

The dedicated P9 regression passes known-answer and failure fixtures for:

    binary Cohen kappa
    multi-category Cohen kappa
    positive specific agreement
    grouping union/category agreement
    threshold boundary behavior
    undefined metrics
    ambiguity accounting
    STATE structural equality/disagreement
    reason-only STATE differences
    commitment drift
    event/item alignment
    hidden-detail public projection
    frozen comparison idempotence

The finalized V2 staged runtime also passes the complete declared inherited regression set:

    P8 Key B regression
    P8 headless runner smoke
    P7 component-key regression
    P6 LEGACY regression
    P6 headless runner smoke
    P5 private-ops regression
    P4 private-ops regression
    Codex compatibility RPC-timeout regression
    public surface registration at 178 tools
    flexible authority regression
    bounded Git fetch regression at 178 tools
    bounded Git pull regression at 178 tools
    runtime release regression
    runtime release dependency integration

Managed lifecycle:

    prepare                 PASS
    publish                 SUCCEEDED
    restart / activation    SUCCEEDED
    post-activation verify  VERIFIED
    mismatchCount           0
    live tool count         178

No hidden Key A or Key B semantic content was inspected during implementation, qualification, release repair, deployment or verification.

## 6. Historical LEGACY preservation

Historical LEGACY remains unchanged:

    HISTORICAL_R2_LEGACY_COMPONENT = INCONCLUSIVE
    HISTORICAL_R2_LEGACY_CONSTRUCT_VALIDITY = NOT_ESTABLISHED
    P6C = NOT_RUN

P9 is STATE+BIRTH only.

## 7. Current boundary

    KEY_A_STATE_BIRTH_COMMITMENT = FROZEN
    KEY_B_STATE_BIRTH_COMMITMENT = FROZEN
    P9_CONTROL_PLANE = QUALIFIED / DEPLOYED / VERIFIED
    P9_RUNTIME_VERSION = 0.1.1-preview.72-p9-construct-comparison
    P9_TOOL_COUNT = 178
    P9_MISMATCH_COUNT = 0
    LIVE_CONSTRUCT_COMPARISON = NOT_RUN
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

Research 433 already authorizes the mechanical live comparison after verified deployment.

    NEXT = P9_STATUS_THEN_RUN_COMPARISON
