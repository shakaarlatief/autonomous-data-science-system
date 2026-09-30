# Research 411: Key Author A P6 Automated Control Plane Qualified and Activated

**Date:** 2026-09-30
**Status:** P6 AUTOMATED CONTROL PLANE QUALIFIED / PUBLISHED / ACTIVATED / LIVE P6 SEMANTICS NOT STARTED
**Parent:** Research 410
**Scope:** Preserve implementation, regression qualification, publication, verification and runtime activation of the bounded automated Key Author A P6 post-classification LEGACY control plane.
**Authority:** Non-semantic control-plane qualification only. This record does not authorize P6 semantic execution, create candidate-gap labels, create evidence dispositions, create grouping pairs, select witnesses/controls, assemble canonical Key A bytes, generate a Key A commitment, authorize Key Author B, score DRP-03, implement the successor architecture, migrate repository state, or switch authority.

## 1. Frozen design implemented

Research 410 froze the P6 execution architecture before any P6 semantic output existed.

The implementation preserves three isolated semantic subphases:

    P6A
        candidate-gap authoring

    P6B
        independent frozen-horizon evidence substantiation

    P6C
        within-source MUST_JOIN / MUST_SPLIT grouping

The control plane fixes server-side:

    private Key Author A root
    17-source order
    unique-item reconstruction rules
    evidence horizon
    semantic prompt templates
    Claude model and effort
    fresh-session lifecycle
    headless invocation flags
    tool allowlists
    output schemas
    transcript verification
    artifact verification
    stop-on-exception behavior
    phase transition rules

The caller cannot select:

    private paths
    public source paths
    semantic source IDs
    item IDs
    pair IDs
    labels
    evidence statuses
    prompts
    shell commands
    repository revisions
    thresholds
    witness identities
    control identities

## 2. Purpose-specific public operation

The qualified release adds one public Runtime Bridge tool:

    codex.p6_private_operation

Its bounded action-only surface is:

    status
    prepare
    authorize_phase
    run_until_boundary
    resume_after_hold
    finalize_subphase

The semantic execution guard is structural:

    prepare
        may perform deterministic non-semantic staging and reconstruction

    authorize_phase
        is the explicit owner-authorization transition

    run_until_boundary
        is rejected until P6 is prepared and explicitly authorized

Therefore activating the runtime capability does not itself authorize live P6 semantic work.

## 3. Automated sequential runner

The implementation replaces the P5 owner clipboard and scheduling loop with a bounded local runner.

For each semantic job the runner starts a fresh Claude Code process using:

    claude --print
    model = claude-opus-5-5
    effort = high
    structured JSON output
    fresh UUID session
    safe mode
    restricted mode
    Chrome disabled
    strict empty MCP configuration
    no resume
    no continue
    no parallel semantic worker

Tool exposure is phase-specific:

    P6A
        Read only

    P6B
        Read / Glob / Grep only
        plus the fixed read-only frozen evidence checkout

    P6C
        Read only

The semantic model does not write canonical artifacts directly.

Its structured output is validated first. The bounded worker then writes the accepted canonical artifact mechanically.

This reduces writable semantic surface compared with P5.

## 4. P6A isolation

P6A receives:

    current source unique catalog
    mechanically derived eligible item IDs
    fixed instructions
    execution addendum
    P6A-specific generic precedents

Eligibility remains mechanically derived from frozen P5 primary classifications:

    normative = true
    realization_required = true

P6A does not receive repository evidence.

It authors exactly:

    item_id
    candidate_gap

for eligible items.

No P6A result is available to P6B before P6A freezes.

## 5. P6B evidence isolation

P6B receives the same eligible semantic items but not P6A candidate-gap values.

It receives bounded read/search access only to:

    LOCALAPPDATA/ADS-R2-KeyAuthor-A/legacy_search/ads_legacy_0a68787a

The control plane verifies before use:

    exact HEAD
        0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

    no Git remotes

    clean working tree

The author can return only the frozen evidence dispositions:

    REALIZED
    NOT_REALIZED
    NO_DECISIVE_EVIDENCE

and bounded declarative evidence requests.

Evidence requests are mechanically resolved against the frozen checkout. Canonical evidence refs bind:

    evidence type
    relative path
    exact frozen revision
    locator/search specification
    status
    match count where applicable
    deterministic output SHA-256

No live repository, network, web, GitHub or later repository history enters P6B.

## 6. P6C isolation

P6C receives only the current source grouping material, fixed instructions, addendum and P6C-specific generic precedents.

It does not receive:

    P5 classifications
    attention mappings
    P6A candidate gaps
    P6B evidence
    material truth
    witness identities
    control identities
    source control roles

Every stored MUST_JOIN or MUST_SPLIT pair must be:

    same-source
    distinct
    lexicographically ordered
    unique
    disjoint between relations
    individually reasoned
    mechanically checked against frozen realization-required eligibility

Uncertain or unreviewed pairs remain unconstrained.

## 7. Stop-on-exception and recovery

Automatic retry-to-green is not implemented.

If a job fails semantically, operationally, or mechanically, the runner stores:

    HOLD
    failure code
    accepted source prefix
    frozen accepted artifacts
    prior session provenance

The orchestration stops.

A later governed `resume_after_hold` action first validates the accepted prefix and artifact hashes, then starts a new orchestration UUID and fresh model sessions for only the unfinished suffix.

Accepted work is not silently rerun.

No held attempt is edited into acceptance.

## 8. Qualification results

Direct bounded staged tests returned:

    P6_LEGACY_OPS_REGRESSION=PASS
        sources=17
        items=3088
        subphases=3
        freshSessions=51

    P6_HEADLESS_RUNNER_SMOKE=PASS
        cliFlags=PASS
        structuredOutput=PASS
        transcript=PASS

    P5_PRIVATE_OPS_REGRESSION=PASS
        batches=18
        presentations=3210
        attentionPairs=122

    P4_PRIVATE_OPS_REGRESSION=PASS

The P6 regression suite covers, among other cases:

    deterministic unique-item reconstruction
    exact 17-source / 3088-item workload
    P6 preparation idempotence
    semantic execution rejection before owner authorization
    isolated P6A / P6B / P6C output schemas
    fresh session uniqueness
    headless runner invocation shape
    forbidden resume/continue absence
    tool-boundary verification
    transcript-boundary verification
    P6A candidate-gap item-set validation
    P6B decisive-evidence requirements
    P6C source and eligibility constraints
    exact frozen evidence revision verification
    no evidence remotes
    clean evidence checkout requirement
    exact-path evidence hashing
    deterministic absence-search evidence
    absence-search false-absence rejection
    stop-on-HOLD behavior
    accepted-prefix preservation
    governed resume behavior
    retained P5 behavior
    retained P4 behavior

An isolated direct invocation of the copied public-surface registration test cannot resolve every runtime module from the partial release-bundle directory by itself. That is expected for this delta bundle and is not the governed release execution environment.

The managed release publisher composes the candidate delta over the live runtime and executes the full registered regression list in that staged runtime.

Managed publication succeeded, so the complete governed release regression set, including public-surface registration and retained Runtime Bridge regressions, passed before publication.

## 9. Managed release

Final local-runtime source state:

    repository
        autonomous-data-science-system-local-runtime

    commit
        e522a4bbe05083b03290a33f1fbb56e7ce081d94

    origin/main
        e522a4bbe05083b03290a33f1fbb56e7ce081d94

Managed release:

    release ID
        p6-private-ops-v2

    target version
        0.1.1-preview.57-p6-private-ops-public

    target surface
        codexless-public-preview-v2

    target tool count
        175

    manifest SHA-256
        8dc49b3a8c03179da38ea51d3c6b726ac9e86b316d83f99fabe043d994ddcefb

Publication operation:

    rm_0c3b8a2024d13f6323c0c718fd61b37b
    SUCCEEDED

Pre-activation release verification:

    VERIFIED
    mismatchCount = 0

Runtime activation:

    operation
        rm_a5c0717734d62917d70dd4ca3f0a4f56

    status
        SUCCEEDED

Post-activation release verification:

    VERIFIED
    mismatchCount = 0

## 10. Live semantic boundary remains intact

No live P6 semantic action has been invoked.

No live P6 source packet has been exposed to Claude Code.

No P6 candidate-gap label exists.

No P6 evidence disposition exists.

No P6 grouping pair exists.

No P6 witness/control selection has occurred.

No canonical Key A assembly has begun.

The already-running ChatGPT host still has the pre-release Runtime Bridge tool metadata snapshot, so `codex.p6_private_operation` is not yet present in this chat's tool list even though the qualified server bytes are published, activated and verified.

This is only a host-schema refresh boundary.

## 11. Exact next step

After the ChatGPT Runtime Bridge tool metadata is refreshed, invoke the bounded non-semantic action:

    action = prepare

That action may:

    verify the frozen P5 PASS state
    verify/stage exact frozen P6 public inputs
    verify the frozen evidence checkout
    reconstruct the 3088-item unique classification projection mechanically
    create phase-specific empty precedent surfaces
    set P6_PREPARED=true

It must leave:

    P6_AUTHORIZED=false
    P6A_NOT_STARTED
    P6B_NOT_STARTED
    P6C_NOT_STARTED

After successful preparation, return to the project owner for the frozen Research 410 decision:

    ACCEPT
    AMEND
    HOLD

Only an explicit owner ACCEPT may permit:

    action = authorize_phase

and only after that may:

    action = run_until_boundary

start live P6 semantic execution.

    KEY_A_P6_CONTROL_PLANE=QUALIFIED_ACTIVATED
    KEY_A_P6_PREPARED=false
    KEY_A_P6_AUTHORIZED=false
    KEY_A_P6_SEMANTIC_OUTPUT_EXISTS=false
    NEXT=REFRESH_HOST_TOOL_SCHEMA_AND_RUN_BOUNDED_P6_PREPARE
