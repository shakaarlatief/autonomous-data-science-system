# Research 386: Bounded P5 Private Operations Qualified and Activated

**Date:** 2026-09-28
**Status:** P5 PRIVATE-OPS QUALIFIED / ACTIVE RUNTIME / CURRENT INTERACTION TOOL-SCHEMA REFRESH REQUIRED / NO LEGACY LABEL CREATED
**Parent:** Research 385
**Scope:** Qualify and activate the purpose-specific Runtime Bridge control plane required by Research 384 before any Key Author A P5 LEGACY classification batch is released.
**Authority:** Infrastructure qualification only. This record does not create a LEGACY semantic label, release Batch 1, authorize candidate-gap/evidence/grouping work, assemble canonical Key A, generate a commitment, authorize Key Author B, or authorize migration.

## 1. Result

The Research 384 launch prerequisite is now satisfied at the Runtime Bridge runtime level.

Qualified bounded capability:

    tool
        codex.p5_private_operation

    active release
        p5-private-ops-v3

    active runtime version
        0.1.1-preview.53-p5-private-ops-public

    public surface
        codexless-public-preview-v2

    public tool count
        174

    release verification
        VERIFIED

    mismatchCount
        0

    runtime restart
        SUCCEEDED

The release is sourced from the local-runtime evidence repository at:

    cffdf28e576f3321f125b0b2dd49196554df1be6

No generic shell authority over the fixed Key Author A private workspace was introduced.

## 2. Qualified bounded actions

The P5 surface is purpose-specific and accepts only bounded control inputs.

Qualified actions are:

    activate_phase
    prepare_batch
    postflight_attempt
    accept_attempt
    reject_attempt

The caller cannot provide:

    arbitrary paths
    arbitrary commands
    presentation IDs
    semantic labels
    attention mappings
    provenance mappings
    arbitrary private-root authority

The server fixes the private root to the Key Author A workspace and fixes the complete 18-batch public workload manifest internally.

## 3. Batch-order and source-exposure enforcement

The bounded capability mechanically binds:

    exact 18-batch order
    exact batch IDs
    exact packet-source IDs
    exact part indices
    exact presentation counts
    exact frozen line ranges

Preparation can advance only to the next unaccepted batch.

A prepared batch is recorded as the open P5 batch.

Postflight requires the executor to close that batch before task-owner acceptance.

No later-batch release is performed by the semantic executor.

## 4. Predecessor and immutability hardening

The final qualified V0.2 P5 interface verifies the frozen predecessor surface before launch and during later batch transitions.

It requires the preserved Key Author A predecessor state, including:

    P3 authorization retained
    prior semantic labels retained
    15 frozen BIRTH classification batches retained
    no open classification batch
    P4 authorization retained
    P4 grouping floor PASS retained
    no open grouping event

For every previously accepted P5 batch, the control plane also verifies:

    exact accepted-prefix order
    exactly one accepted provenance record
    valid attempt/session/digest/path provenance
    artifact SHA-256 still matches acceptance
    artifact still satisfies exact schema and frozen presentation-ID order
    accepted predecessor sessions remain unique

This prevents silent mutation of an accepted classification artifact from being treated as a valid predecessor for a later batch.

## 5. Fresh-session and transcript boundary

P5 retains the Research 384 rule:

    one fresh standalone Claude Code session per batch

The bounded verifier conservatively rejects reuse of a P5 session ID from an earlier accepted or rejected attempt.

Postflight also verifies mechanically:

    exact Claude model metadata when observed
        claude-opus-5-5

    default permission mode
    private-workspace cwd when transcript cwd is present
    no compaction
    only Read / Write / Edit executor tools
    no MCP tool invocation
    current frozen batch source was actually read
    every batch-source Read stays inside the exact released line range
    all required common P5 sources were read
    ERRATA is read before PRECEDENTS
    no other semantic source is read
    artifact is written exactly once and not edited afterward
    PRECEDENTS / ERRATA remain append-only
    local settings override remains absent

The task owner therefore verifies execution contract compliance without reading hidden label values.

## 6. Artifact verification

Each attempt is mechanically checked against the Research 384 private artifact contract.

Checks include:

    exact top-level fields
    exact protocol/component/phase/batch/source/part metadata
    exact presentation count
    exact frozen presentation-ID sequence
    unique presentation IDs
    exact per-presentation field set
    boolean field types
    normative_kind frozen enum
    normative=false implies normative_kind=null
    normative=true implies normative_kind non-null

No semantic correctness re-adjudication is performed by the task owner.

## 7. Qualification evidence

The P5 V0.2 staged qualification suite passes:

    P5 private-ops regression
        PASS

    retained P4 private-ops regression
        PASS

    public-surface registration
        PASS / tools=174

    flexible-authority regression
        PASS

    bounded Git fetch regression
        PASS / tools=174

    bounded Git pull regression
        PASS / tools=174

    runtime-release regression
        PASS

    runtime-release dependency integration
        PASS

The governed release lifecycle then returned:

    prepare
        PASS

    publish
        SUCCEEDED

    verify
        VERIFIED / mismatchCount=0

    restart
        SUCCEEDED

## 8. Earlier release attempts

Two earlier infrastructure iterations remain historical evidence:

    p5-private-ops-v1
        publish failed closed because retained public-surface count assertions had not all been updated

    p5-private-ops-v2
        publication and verification succeeded
        then underwent further launch-safety hardening before semantic use

Neither iteration released a semantic batch or created a LEGACY label.

The active qualified release is V3.

## 9. Current-interaction tool-surface boundary

After V3 publication, verification, and runtime restart, the currently open ChatGPT interaction still exposes its pre-refresh Runtime Bridge tool schema.

Observed in this interaction:

    installed runtime contains codex.p5_private_operation
    active release verification mismatchCount = 0
    Runtime Bridge restart = SUCCEEDED
    current interaction tool registry does not expose codex.p5_private_operation

Therefore this interaction must not substitute:

    generic command execution
    generic private-workspace shell
    direct filesystem access to the Key Author A workspace

for the missing bounded P5 call.

The safe next transition is a fresh ChatGPT interaction with a refreshed Runtime Bridge tool schema.

Only after that fresh interaction confirms the bounded P5 tool is actually callable may task-owner control advance to:

    activate_phase
    prepare_batch L01
    release L01 semantic prompt

## 10. Current boundary

    KEY_A_P5_DESIGN=ACCEPTED
    KEY_A_P5_AUTHORIZED=true
    KEY_A_P5_PRIVATE_OPS_RUNTIME_READY=true
    KEY_A_P5_PRIVATE_OPS_RELEASE=p5-private-ops-v3
    KEY_A_P5_PRIVATE_OPS_VERSION=0.1.1-preview.53-p5-private-ops-public
    KEY_A_P5_PRIVATE_OPS_VERIFY_MISMATCH_COUNT=0
    CURRENT_CHAT_P5_TOOL_EXPOSED=false
    KEY_A_P5_PRIVATE_PHASE_ACTIVATED=false
    KEY_A_P5_BATCH1_RELEASED=false
    KEY_A_P5_LABELS_CREATED=false

    LEGACY_CANDIDATE_GAP=NOT_STARTED
    LEGACY_EVIDENCE=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED
    CANONICAL_KEY_A_ASSEMBLY=NOT_AUTHORIZED
    COMMITMENT_GENERATION=NOT_AUTHORIZED
    KEY_AUTHOR_B=NOT_AUTHORIZED
    MIGRATION=NOT_AUTHORIZED

    NEXT=FRESH_CHATGPT_TOOL_SURFACE_THEN_BOUNDED_P5_ACTIVATION_AND_L01_PREPARATION
