# Research 424: Fresh Key Author B P8 Control Plane Deployed, Live Smoke Pending

**Date:** 2026-10-01
**Status:** P8 IMPLEMENTATION + MANAGED RELEASE QUALIFICATION PASS / LIVE NON-SEMANTIC SMOKE PENDING / KEY B SEMANTICS NOT STARTED
**Parent:** Research 423 / Research 421 owner acceptance
**Scope:** Preserve implementation, release-lifecycle qualification, recovery evidence, and the remaining provider-local tool-schema boundary for the fresh Key Author B STATE+BIRTH control plane.
**Authority:** Mechanical control-plane implementation and deployment evidence only. This record does not assert live-smoke PASS, authorize a bypass of the purpose-specific P8 surface, create Key B semantic labels, compare Key A and Key B, score DRP-03, implement successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. P8 implementation

The fresh Key Author B purpose-specific control plane has been implemented in the private local-runtime repository under the frozen Research 423 design.

The public-safe surface is:

    codex.p8_key_b_operation

with action-only operations:

    status
    prepare
    authorize_phase
    run_until_boundary
    resume_after_hold
    finalize_component

The caller cannot supply semantic IDs, paths, labels, prompts, thresholds, model selection, tools, commands, evidence, grouping pairs, or Key A semantic material.

The implementation preserves the Research 423 component boundary:

    included components = STATE + BIRTH
    excluded component  = LEGACY / terminal INCONCLUSIVE
    P6C                 = NOT RUN

## 2. Qualified implementation controls

The P8 implementation and regression suite exercise the frozen mechanical design, including:

    fixed isolated Key B root
    exact public-frozen input binding
    mechanical verification of the frozen Key A component prerequisite
    fresh-session invocation construction
    zero semantic tools
    stdin-only semantic prompt transport
    no resume / continue / add-dir
    no session persistence
    exact STATE schema validation
    15-batch sequential BIRTH classification state machine
    hidden BIRTH attention gate
    quality-failure stop path
    Key-B-own grouping eligibility projection
    13-event sequential BIRTH grouping state machine
    grouping-floor failure stop path
    private structured-output and process provenance
    canonical component-bundle assembly
    frozen-artifact drift detection
    governed HOLD / fresh-replacement behavior

Local release-bundle regression results include:

    P8_KEY_B_OPS_REGRESSION = PASS
    classificationBatches = 15
    groupingEvents = 13
    isolation = PASS
    gateFailures = PASS
    resume = PASS

and:

    P8_HEADLESS_RUNNER_SMOKE = PASS
    cliFlags = PASS
    zeroTools = PASS
    stdin = PASS
    noPersistence = PASS
    liveSmokeWorker = PASS

These are implementation/regression qualifications. They are not a substitute for the required live non-semantic Claude smoke against the actual purpose-specific Runtime Bridge process.

## 3. Initial P8 release

The first qualified publication was:

    release_id = p8-key-b-ops-v1
    source_head = c6581153f6b56763d2581f15531641936f124de3
    target_version = 0.1.1-preview.64-p8-key-b-public
    target_surface = codexless-public-preview-v2
    target_tool_count = 177

Managed publication succeeded, Runtime Bridge activation succeeded, and post-activation verification returned:

    mismatchCount = 0

This established the 177-tool surface including codex.p8_key_b_operation.

## 4. Live-smoke hardening and fail-closed release recovery

Research 423 requires a live non-semantic Claude smoke before semantic activation. A generic Codex command-sandbox probe using the frozen invocation family timed out. The same project-context surface reports:

    networkAccess = false

That generic sandbox observation is therefore not accepted as evidence about the server-owned purpose-specific P8 execution environment. It created no production Key B semantic state and is not classified as a P8 semantic failure.

The P8 control plane was then hardened so prepare itself owns the live smoke. The server-side smoke is non-semantic, uses the frozen hardened Claude invocation family, records only bounded mechanical provenance, and must PASS before frozen public inputs are staged and before authorize_phase can succeed.

An intermediate release attempt correctly failed closed during activation:

    release_id = p8-key-b-ops-v2
    source_head = 6ab1f85e959ae935a07fcbabc437be9dbb3eeaf2
    activation_error = RUNTIME_REPLACEMENT_CONTRACT_MISMATCH
    recoveryAttempted = true
    recoverySucceeded = true

The cause was mechanical: the target server version advanced while the version-bearing surface contract had not been included in the replacement set. The managed restart supervisor rejected the inconsistent replacement and restored the previous runtime.

No Key B semantic process was started by this failed activation.

## 5. Corrected active P8 release

The corrected release is:

    release_id = p8-key-b-ops-v3
    source_head = 056a11807e1e0ff652fa4797657e37072b85631d
    target_version = 0.1.1-preview.65-p8-key-b-live-smoke
    target_surface = codexless-public-preview-v2
    target_tool_count = 177
    manifest_sha256 = 88ee4f60d1c375058c67f02987ef60ee881f8454df8817395f46164b90f5c16e

For this corrected release:

    prepare = PASS
    publish = SUCCEEDED
    restart / activation = SUCCEEDED
    recoveryAttempted = false
    post-activation verify = VERIFIED
    mismatchCount = 0

The active Runtime Bridge therefore contains the corrected P8 implementation and the server-owned live-smoke gate.

## 6. Current provider-local tool-schema boundary

After successful P8 V3 activation and exact post-activation verification, this existing ChatGPT interaction still does not expose codex.p8_key_b_operation in its bound connector tool schema.

The server release and the provider-local chat tool schema are therefore currently out of sync in this interaction:

    Runtime Bridge active P8 release = VERIFIED
    server target tool count         = 177
    current chat P8 callable         = NOT EXPOSED

The task owner must not bypass this by importing P8 code or using generic command execution against the production Key B root. The purpose-specific action-only surface is part of the frozen confidentiality and authority boundary.

The next legitimate step is a provider-local tool-schema refresh, normally by continuing from a fresh ChatGPT interaction with the Runtime Bridge connector, then confirming the bounded P8 surface is exposed.

## 7. Execution boundary after schema refresh

Once codex.p8_key_b_operation is actually exposed, the governed sequence is:

    status
    prepare

If prepare starts the server-owned live smoke, bounded status is observed until it reaches PASS or HOLD.

Only after:

    live smoke = PASS
    preparation = PASS

may the already-authorized Research 421 flow invoke:

    authorize_phase
    run_until_boundary

A HOLD or quality/floor failure remains fail-closed and requires governed disposition. No automatic retry-to-green is allowed.

finalize_component is permitted only after the P8 runner reaches COMPLETE and all frozen gates pass.

## 8. Confidentiality and semantic state

No Key B semantic output has been created or inspected in this interaction.

The task owner has not opened:

    Key A hidden semantic bytes
    Key B labels
    Key B STATE outputs
    Key B grouping pairs
    Key B precedents
    Key B semantic transcripts

Therefore:

    KEY_B_BLINDNESS_BOUNDARY_PRESERVED = true
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false
    KEY_B_SEMANTIC_EXECUTION = NOT_STARTED
    CONSTRUCT_COMPARISON = NOT_STARTED

## 9. Current boundary

    KEY_A_COMPONENT_COMMITMENT = FROZEN
    KEY_A_COMPONENT_COMMITMENT_SHA256 = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb

    P8_IMPLEMENTATION = COMPLETE
    P8_ACTIVE_RELEASE = p8-key-b-ops-v3
    P8_ACTIVE_RUNTIME_VERSION = 0.1.1-preview.65-p8-key-b-live-smoke
    P8_ACTIVE_TOOL_COUNT = 177
    P8_MANAGED_ACTIVATION = PASS
    P8_POST_ACTIVATION_VERIFY = PASS
    P8_MISMATCH_COUNT = 0

    P8_LIVE_NON_SEMANTIC_SMOKE = NOT_RUN_ON_PRODUCTION_PURPOSE_SPECIFIC_SURFACE
    CURRENT_CHAT_P8_TOOL_SCHEMA = NOT_EXPOSED
    KEY_B_SEMANTIC_EXECUTION = NOT_STARTED
    CONSTRUCT_COMPARISON = NOT_STARTED

    NEXT = REFRESH_PROVIDER_TOOL_SCHEMA_THEN_RUN_P8_STATUS_AND_PREPARE
