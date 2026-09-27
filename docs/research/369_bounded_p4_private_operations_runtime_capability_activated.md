# Research 369: Bounded P4 Private Operations Runtime Capability Activated

**Date:** 2026-09-27
**Status:** QUALIFIED / ACTIVATED / PURPOSE-SPECIFIC P4 PRIVATE OPERATIONS AVAILABLE
**Parent:** Research 366 deferred capability observation / Research 367 amended P4 interface
**Scope:** Record implementation and activation of a narrowly bounded Runtime Bridge capability that performs repeated P4 private mechanical preparation, postflight, acceptance, and rejection operations without requiring the project owner to execute ad hoc PowerShell scripts.
**Authority:** Operational P4 support capability only. This does not alter P4 semantic truth, classification labels, grouping rules, event ordering, held-out separation, Key B independence, migration authority, or any later-phase authorization.

## 1. Motivation

Research 366 preserved a deferred architecture observation after the task owner could not directly inspect the private Key-A workspace through the then-available Runtime Bridge surface.

The immediate P4 workflow would otherwise require the project owner to repeatedly run local PowerShell/Python scripts for:

    eligibility projection preparation
    grouping postflight
    attempt acceptance
    attempt rejection

P4 contains multiple remaining grouping events, so repeated manual script relay would create avoidable operational friction and transcription risk.

The selected solution is not generic host PowerShell authority.

The selected solution is one purpose-specific deterministic capability.

## 2. Runtime implementation

Private runtime repository:

    autonomous-data-science-system-local-runtime

Accepted source commit:

    ee574111c6c1fac8a13deb999ee15dab8ad6afb1

Qualified release:

    p4-private-ops-v2

Target runtime contract:

    version       0.1.1-preview.48-p4-private-ops-public
    surface       codexless-public-preview-v2
    tool count    173

The release was:

    prepared
    staged against the live runtime
    regression-qualified
    published
    activated through the managed Codexless restart path
    post-activation verified with zero release-file mismatches

The first release candidate, p4-private-ops-v1, failed closed during publication because two preserved bounded-Git regressions still asserted the previous 172-tool surface count. No runtime source change was activated from that failed candidate. The corrected v2 release updated those regression expectations to 173 and passed the complete declared regression set before activation.

## 3. Purpose-specific tool

The activated public surface adds:

    codex.p4_private_operation

The tool accepts only:

    action
        prepare_event
        postflight_attempt
        accept_attempt
        reject_attempt

    eventKey
        D01
        D02
        H01-H11

and, only where required:

    bounded attempt number
    UUID session ID
    bounded governed rejection reason

The caller cannot supply:

    filesystem path
    command
    executable
    credential
    semantic item ID
    pair identity
    eligibility count
    arbitrary source
    arbitrary destination
    another private workspace root

The private root is fixed server-side as:

    LOCALAPPDATA/ADS-R2-KeyAuthor-A

## 4. Fixed event manifest

The capability freezes the already-approved P4 event universe and range metadata.

It cannot invent or select another packet event.

Each event key maps server-side to:

    split
    packet_event_id
    unique-item cardinality
    bounded catalog line range

This preserves Research 363 / Research 367 event ordering and prevents caller-selected cross-event expansion.

## 5. Preparation operation

prepare_event mechanically:

    verifies P4 authorization/interface state
    verifies the event is the next unaccepted event
    derives the event eligibility projection from the same-key frozen primary classifications
    validates complete primary mapping and classification coverage
    writes or verifies the exact event-scoped projection
    records private projection provenance
    leaves semantic execution unopened
    returns only a bounded PASS-style receipt

It does not return:

    eligible item IDs
    eligibility count
    frozen labels
    attention mappings
    projection digest
    pair data

## 6. Postflight operation

postflight_attempt mechanically verifies, without publishing hidden semantics:

    expected P4 progress boundary
    same-key projection provenance
    exact projection equality to frozen eligibility truth
    artifact schema
    endpoint event scope
    endpoint membership in the eligibility projection
    endpoint distinctness/order
    pair reason presence
    duplicate/disjointness/sort invariants
    local-settings absence
    transcript session/model/permission identity
    no compaction
    no prohibited semantic tools
    bounded grouping-catalog reads
    eligibility-projection use
    no forbidden-source read
    errata-before-precedents ordering
    one-write frozen artifact behavior
    append-only precedent/errata behavior

The returned receipt exposes only booleans and bounded event/attempt metadata.

It does not expose:

    eligibility IDs/counts
    pair IDs/counts/reasons
    classification labels
    attention identities
    transcript semantic content
    private digests

## 7. Acceptance and rejection operations

accept_attempt:

    reruns the complete postflight
    refuses acceptance unless every postflight check passes
    appends the event to accepted-event state
    records exact private artifact/session provenance
    advances only to the next preparation boundary

reject_attempt:

    requires one bounded governed reason
    preserves the frozen artifact
    records immutable rejection provenance
    does not mutate semantic pair content
    leaves the same event as the next unaccepted event

Both operations fail closed on event-order drift.

## 8. Qualification

The candidate regression suite covers:

    deterministic projection derivation
    hidden-detail non-disclosure
    event-order enforcement
    passing postflight
    failing endpoint eligibility
    prohibited tool detection
    out-of-range catalog detection
    acceptance only after full PASS
    idempotent rejection provenance
    artifact immutability / drift refusal

The staged release additionally passed:

    public-surface registration at 173 tools
    flexible-authority regression
    bounded Git fetch regression
    bounded Git pull regression
    runtime-release regression
    runtime-release dependency integration

Managed publication and restart then succeeded, followed by release verification:

    mismatchCount = 0

## 9. Authority discipline

This capability exists to remove repetitive owner-side mechanical scripting.

It is not a semantic author.

It cannot decide:

    MUST_JOIN
    MUST_SPLIT
    UNCONSTRAINED
    classification truth
    protocol amendments

Claude remains the semantic grouping author.

ChatGPT remains the task owner for event-level release and acceptance.

The project owner retains phase/amendment authority.

## 10. Broader architecture status

Research 366's broader future-architecture question remains open.

The present tool solves the narrow P4 operational problem.

It does not settle the final successor Project Development System design for:

    generic local workspace admission
    capability delegation
    private workspace lifecycle
    revocation
    audit
    tool-runtime boundaries

Those remain later architecture concerns.

## 11. Current result

    P4_PRIVATE_OPERATIONS_CAPABILITY=ACTIVE
    PURPOSE_SPECIFIC=true
    GENERIC_POWERSHELL_AUTHORITY=false
    FIXED_PRIVATE_ROOT=true
    HIDDEN_SEMANTIC_DISCLOSURE=false
    RUNTIME_RELEASE=p4-private-ops-v2
    RELEASE_VERIFICATION=PASS
