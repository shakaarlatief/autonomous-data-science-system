# Research 422: Key Author A Component-Scoped Commitment Frozen

**Date:** 2026-10-01
**Status:** P7 PASS / KEY A STATE+BIRTH COMMITMENT FROZEN / KEY B CONTROL-PLANE PREPARATION NEXT
**Parent:** Research 421
**Scope:** Preserve the qualified component-scoped Key Author A commitment after owner acceptance of Research 420 and the prospective P7 implementation/qualification work.
**Authority:** Mechanical commitment-freeze disposition only. This record does not expose Key A semantic bytes, authorize Key A LEGACY repair/P6C, start Key Author B semantic execution, perform construct comparison, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. P7 implementation and activation

The component-scoped Key A control plane has been implemented in the private local-runtime repository and released through the governed Runtime Bridge lifecycle.

Qualified release:

    release_id = p7-component-key-ops-v3
    source_head = 47cdd33d457d20cc370e8f801d79480832dfaa2e
    target_version = 0.1.1-preview.63-p7-component-key-public
    target_surface = codexless-public-preview-v2
    target_tool_count = 176

The release qualification covered:

    P7 component-key regression
    P6 legacy regression
    P6 headless-runner smoke
    P5 private-operations regression
    P4 private-operations regression
    public-surface registration
    flexible-authority regression
    bounded Git fetch-origin regression
    bounded Git pull-ff-only regression
    runtime-release regression
    runtime-release dependency-integration regression

All passed.

Managed publication succeeded, the Runtime Bridge restart/activation succeeded, and post-activation verification returned:

    mismatchCount = 0

The purpose-specific surface is:

    codex.p7_component_key_operation

with actions:

    status
    qualify
    freeze_commitment

## 2. Live P7 qualification

The purpose-specific bounded P7 status first confirmed:

    qualified = false
    frozen = false
    componentScope = [BIRTH, STATE]
    excludedComponent = LEGACY
    excludedComponentStatus = INCONCLUSIVE
    legacyNegativeControlCheck = FAIL
    p6cRun = false
    hiddenSemanticDetailsExposed = false
    next = QUALIFY

The task owner then invoked the qualified mechanical `qualify` action.

Result:

    qualified = true
    keyAuthorSlot = KEY_AUTHOR_A
    componentScope = [BIRTH, STATE]
    excludedComponent = LEGACY
    excludedComponentStatus = INCONCLUSIVE
    legacyNegativeControlCheck = FAIL
    p6cRun = false
    serializationId = AO10-DRP03-R2-V03-COMPONENT-BUNDLE-V01-CANONICAL-JSON
    commitmentSha256 = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb
    canonicalByteLength = 643247
    birthAttentionPass = true
    birthGroupingFloorPass = true
    hiddenSemanticDetailsExposed = false
    next = FREEZE_COMMITMENT

No Key A semantic payload was returned.

## 3. Commitment freeze

The task owner then invoked the bounded `freeze_commitment` action.

The same exact canonical digest and byte length were returned and the receipt reported:

    frozen = true
    next = KEY_B_CONTROL_PLANE_PREPARATION

A subsequent bounded status call independently confirmed the frozen commitment without exposing semantic bytes.

Therefore the accepted Key A qualifying scope is now cryptographically frozen as:

    BIRTH
    STATE

The historical LEGACY component remains explicitly excluded:

    LEGACY = INCONCLUSIVE
    reason = FROZEN_NEGATIVE_CONTROL_CHECK_FAILURE
    p6c_run = false

The failed LEGACY negative-control result remains FAIL. Nothing in P7 converts, repairs, retries, or obscures that result.

## 4. Confidentiality boundary

The task owner has not opened:

    the private canonical Key A component bundle
    Key A STATE expected outputs
    Key A BIRTH item labels
    Key A grouping pairs
    Key A private semantic transcripts
    Key A private precedents

The P7 surface returned only the public-safe commitment metadata allowed by the frozen protocol.

Therefore:

    HIDDEN_SEMANTIC_DETAILS_EXPOSED=false
    KEY_B_BLINDNESS_BOUNDARY_PRESERVED=true

## 5. Current boundary

    KEY_A_STATE = PRIVATE_FROZEN
    KEY_A_BIRTH = PRIVATE_FROZEN
    KEY_A_BIRTH_ATTENTION = PASS
    KEY_A_BIRTH_GROUPING_FLOOR = PASS

    KEY_A_LEGACY = INCONCLUSIVE / FROZEN
    KEY_A_P6C = NOT_RUN

    KEY_A_COMPONENT_SCOPE = STATE + BIRTH
    KEY_A_COMPONENT_COMMITMENT = FROZEN
    KEY_A_COMPONENT_COMMITMENT_SHA256 = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb
    KEY_A_COMPONENT_CANONICAL_BYTES = 643247

    KEY_AUTHOR_B_CONTROL_PLANE = AUTHORIZED_TO_PREPARE_AND_QUALIFY
    KEY_AUTHOR_B_SEMANTIC_EXECUTION = NOT_STARTED
    CONSTRUCT_COMPARISON = NOT_STARTED

    NEXT = FREEZE_AND_IMPLEMENT_KEY_B_CONTROL_PLANE
