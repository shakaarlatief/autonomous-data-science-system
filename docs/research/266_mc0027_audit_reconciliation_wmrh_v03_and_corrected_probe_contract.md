# Research 266: MC-0027 Audit Reconciliation, WMR-H V0.3 Narrow Amendments, and Corrected P-R8B-01 Rerun Contract

**Date:** 2026-09-23
**Status:** CLAUDE AUDIT ACCEPTED / ORIGINAL 18-OF-18 RESULT RECLASSIFIED / WMR-H V0.3 CORRECTION CANDIDATE / CORRECTED PROBE REQUIRED / NO OWNER REPRESENTATION DECISION / NO PHYSICAL MIGRATION
**Parent protocol:** Research 263
**Original harness freeze:** Research 264
**Original result:** Research 265
**Claude audit:** MC-0027 Message 001 / commit 902fcfd15450a7ba3fb9f3e3542ef33790cf9af9
**Scope:** Reconcile the independent result audit, preserve the authentic original run without overclaiming it, apply two narrow representation-contract amendments, and freeze the correction requirements for a successor harness before implementation.
**Authority:** Architecture-research and corrected-probe contract only. This record does not accept the representation architecture, amend Specification 028, authorize AO-10, or authorize physical migration.

## 1. Audit disposition

Claude returned:

    P_R8B_01_AUDIT_DISPOSITION=AMEND
    PROTOCOL_FIDELITY=PASS
    HARNESS_INTEGRITY=PARTIAL
    REAL_SOURCE_DISCRIMINATION=PARTIAL
    CONCURRENCY_EVIDENCE=PARTIAL
    METADATA_EVIDENCE=PARTIAL
    RECEIPT_EVIDENCE=PARTIAL
    CURRENT_JSON_EVIDENCE=PARTIAL
    BREAK_GLASS_EVIDENCE=UNSUPPORTED
    PSMF_SEAM_EVIDENCE=UNSUPPORTED
    WMR_H_V02_ARCHITECTURE_SUPPORT=AMEND
    OWNER_REPRESENTATION_DECISION_READY=NO

ChatGPT accepts the audit.

No valid gate failed.

The defect is primarily evidentiary:

    7 gates VALID
        G01 G03 G06 G07 G11 G12 G14

    4 gates WEAK_BUT_DIRECTIONAL
        G02 G04 G09 G15

    7 gates INVALID
        G05 G08 G10 G13 G16 G17 G18

Therefore the first run remains authentic evidence, but the statement:

    P_R8B_01_GATES=18_OF_18_VALIDLY_PASS

is withdrawn.

The accurate statement is:

    ORIGINAL_RUN=AUTHENTIC_AND_REPRODUCIBLE
    ORIGINAL_REPORTED_GATE_RESULTS=18_OF_18_PASS
    ORIGINAL_CONFIRMATORY_VALIDITY=INSUFFICIENT_FOR_OWNER_DECISION

Research 265 is preserved as historical evidence and is not rewritten to hide the defect.

## 2. Why the audit matters

The audit demonstrates a distinction this project must preserve:

    check name
        !=
    invariant actually enforced

A test can contain the right vocabulary, return PASS, and still fail to exercise the mechanism it claims to qualify.

The corrected probe must therefore be mutation-sensitive where practical and must measure rather than hardcode every central falsifier.

This is direct evidence for the already accepted transition obligation:

    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

## 3. Hash-basis correction

Research 264 mixed two undeclared byte bases:

    new harness files
        Windows CRLF working-tree bytes

    existing real sources
        LF bytes

Claude independently established that converting the committed LF harness blobs back to CRLF reproduces every Research 264 hash exactly.

Therefore:

    HARNESS_CHANGED_AFTER_RESULT=false

still holds semantically.

But the freeze mechanism itself is defective for cross-platform verification.

Successor freeze rule:

    all frozen harness hashes are SHA-256 of exact Git blob bytes
    at an explicitly named commit

The freeze record MUST say:

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

The successor result MUST bind:

    harness commit
    each harness/schema path
    each exact Git-blob SHA-256
    real-source fixture hashes

A reader on Windows, Linux or through the repository API must obtain the same values.

## 4. WMR-H V0.3 candidate

WMR-H V0.2 remains directionally intact.

Two narrow contract amendments are accepted into the candidate before owner decision.

### A-M1 Governance recognition must fail visibly, not open

The future governed-Markdown recognizer must not silently turn an intended governed carrier into ordinary prose because of superficial encoding/title variation.

Requirements:

    UTF-8 BOM
        normalize before recognition

    leading blank lines before title
        normalize for recognition

    ATX H1
        supported

    Setext H1
        supported or explicitly rejected as a hard governed-format error
        when a governed metadata fence follows

    governed fence in the metadata position
        parse successfully or fail visibly

    indented code block containing the governed info string
        must not be mistaken for the governed fence

    metadata-looking body example
        remains ordinary body content when it is not in governed position

The target property is:

    intended governed carrier
        -> GOVERNED or ERROR

never:

    intended governed carrier
        -> silently PLAIN

### A-M2 Revision discipline requires enforced history semantics

The revision-line branch-conflict mechanism is only reliable if every consequential state mutation changes the revision.

Target contract:

    ordinary semantic mutation
        revision = parent revision + 1

    revision-only mutation
        invalid

    decrement
        invalid

    same-revision semantic replacement
        invalid

    skipped ordinary revision
        invalid

    two-parent semantic merge resolution
        revision = max(parent revisions) + 1

    merge result
        must validate against both parent states

    committed history
        validator rejects violations rather than relying on writer discipline

The validator must operate over committed state history, not only over an in-memory before/after pair.

## 5. Migration-contract implication

The audit also identifies a migration rule, not a representation-format rule:

> Real-carrier conversion must be rule-based and loss-accounted.

For every converted carrier:

    existing structured fields
    authority clauses
    status/lifecycle meaning
    declared references
    provenance
    durable human prose
    operational/current state

must each be:

    mapped
    preserved verbatim where appropriate
    deliberately moved to another canonical owner
    or explicitly dispositioned with reason

A conversion must not appear successful merely because the target parses.

This requirement will feed the later Specification 028 amendment and file-level migration manifest.

## 6. Corrected probe strategy

Do not edit the frozen V0.1 harness.

Create:

    experiments/r8b_representation_probe_v02/

The successor run is:

    P-R8B-01-R2

It remains bound to the original Research 263 blocking thresholds.

The seven invalid gates must be corrected.

The four weak gates should be strengthened where doing so is bounded and directly addresses the audit.

Previously valid gates must be retained or rerun so the successor result is one coherent evidence package.

## 7. Mandatory corrected gate implementations

### G05 routine-transition writer separation

Materialize definition and state as separate canonical files in a temporary Git repository.

Execute a real transition procedure that reads and writes the state file.

Measure the human-definition diff using Git.

Pass remains:

    human-definition bytes modified by routine transition = 0

Required negative control:

    co-located representation + equivalent transition
        -> nonzero human-definition diff
        -> zero-diff criterion would fail

### G08 revision semantics and committed history

Rewrite negative checks so a validator returning success cannot be accidentally interpreted as rejection.

Include:

    revision-only mutation rejects
    decrement rejects
    same-revision semantic replacement rejects
    skipped ordinary revision rejects
    invalid merge revision rejects
    valid merge resolution accepts

Add a committed-history validator.

Construct:

    valid history
        base rev1
        branch A rev2
        branch B rev2
        explicit merge resolution rev3

and at least one corrupted committed history.

Pass only if:

    valid history accepted
    corrupted history rejected

A no-op transition validator and no-op merge validator must make the gate's negative-check routine fail.

### G10 capture/review/promotion

Operate on files.

Procedure:

    create immutable receipt
    create machine JSON capture referencing receipt
    run review procedure
    run promotion procedure
    write/update natural canonical owner

Pass:

    machine-capture bytes unchanged
    receipt bytes unchanged
    human elaboration separate
    canonical target written
    capture remains non-authoritative
    event payload not duplicated as a second canonical event truth

### G13 real Specification 028 conversion

Conversion must be rule-based from the real source.

The converter must:

    derive identity/authority metadata from existing source declarations
    retain all non-legacy-metadata human content
    account for existing status/lifecycle
    account for authority clause
    account for declared references
    account for provenance
    emit a conversion/loss manifest

Pass:

    semantic identity preserved
    governing/canonical role preserved
    non-metadata source content preserved
    no authority clause silently dropped
    no declared reference silently dropped
    no provenance silently dropped
    lifecycle/status mapping explicit
    visible metadata parses

### G16 break-glass without derivatives

Materialize an on-disk canonical candidate layout including:

    project_anchor.json
    workstream definition
    workstream state
    governing specification
    ADS instance policy

Generate derivatives.

Delete/withhold:

    generated orientation
    SQLite index
    optional query/cache surfaces

Recovery must start from:

    project_anchor.json only

and follow repository locators by file reads.

Pass remains:

    declared canonical recovery questions can be answered
    no derivative required

Negative control:

    anchor locator changed to deleted generated-only file
        -> visible recovery failure

### G17 PSMF framework/instance separation

Use on-disk framework and instance trees.

A framework refresh procedure must replace actual framework contract/parser/schema material while never writing the instance tree.

After refresh:

    verify instance policy/state bytes unchanged
    validate instance under refreshed framework

Pass:

    compatible refresh -> validates
    incompatible refresh -> explicit migration_required
    instance bytes unchanged in both cases

The incompatibility result must come from validation under refreshed framework contracts, not an inline hand-coded membership branch.

### G18 Git review quality

Compute rather than hardcode every observation.

Use Git diffs for:

    routine state transition
    metadata-only governing change
    receipt addition

Pass remains:

    routine transition -> zero human-definition diff
    metadata-only change -> body preserved and bounded metadata diff
    receipt addition -> one new receipt file
    specification metadata visibly reviewable

## 8. Central F2 measurement correction

The successor harness MUST compute pairing violations.

Discovery:

    enumerate governed workstream definitions
    enumerate workstream state records
    resolve each state.workstream_id
    require exactly one matching definition

Pass remains:

    removed transition facts = 6 / 6
    pairing violations = 0
    human-definition bytes changed by routine transition = 0

None of these may be literal result constants.

## 9. Strengthening of previously weak gates

These strengthen evidence without weakening any original threshold.

### G02

Place native TOML date/time values in a schema-permitted extension field.

Pass only because the JSON-compatible-value rule rejects them.

A no-op JSON-compatibility checker must make the negative test fail.

### G04

The real Source Vault conversion must emit a loss/disposition manifest covering:

    structured declaration fields
    durable prose sections relevant to current/durable semantics
    references
    provenance
    expected-to-resume meaning
    public/private boundary meaning

The transition-field split remains the original six-field blocking threshold.

### G09

Feed discovered standalone relations into the repository-wide admission check.

At count 12:

    still within bound

Attempting 13:

    REVIEW_REQUIRED

A malformed declared standalone-relation record must fail visibly rather than disappear from counting.

### G15

Build the derived SQLite/FTS index by rereading canonical files from disk and discovering relation records.

Delete the database.

Rebuild by rereading the canonical files again.

Pass remains semantic rebuild equivalence.

## 10. Additional non-retrospective diagnostics

The corrected harness should also include:

    G07 control arm
        same two branch changes without revision bump
        must merge cleanly and demonstrate the hazard

    current.json mixed-source freshness
        include revisioned state and non-revisioned human definition

    optional cold-start read-count observation
        diagnostic only, not an original blocking threshold

The JSONL comparison arm remains optional because the architecture claim is narrowed:

    individual content-addressed JSON receipts behave as designed

not:

    the probe proved individual JSON superior to every JSONL design

## 11. Governance-recognition amendment tests

Because A-M1 is a new architecture amendment after the original P-R8B-01 preregistration, test it as a separately labeled amendment gate:

    AM1-G1

Cases:

    UTF-8 BOM + governed carrier
    leading blank line + governed carrier
    Setext H1 + governed fence
    four-space-indented pseudo-fence
    metadata body example

Pass:

    first three are GOVERNED or explicit ERROR, never silently PLAIN
    indented pseudo-fence is not governing metadata
    body example is not governing metadata

## 12. Revision-history amendment test

A-M2 is tested by the corrected G08 committed-history validator and separately reported as:

    AM2-G1

Pass:

    committed-history validation is not optional
    valid rev1/rev2+rev2/rev3 history accepts
    skipped/non-monotonic history rejects

## 13. Successor outcome classes

    PASS
        all original Research 263 blocking thresholds pass through
        non-tautological corrected implementations
        AND AM1-G1 passes
        AND AM2-G1 passes

    AMEND_REQUIRED
        architecture-relevant corrected gate fails

    HARNESS_INVALID
        successor harness defect proven

If a new harness defect is discovered, do not reinterpret success.

Fix it prospectively and rerun.

## 14. Decision sequence

After P-R8B-01-R2:

    PASS
        -> reconcile MC-0027
        -> determine owner-decision readiness
        -> explicit owner representation decision

    AMEND_REQUIRED
        -> amend architecture or probe claim
        -> no owner acceptance request

No Specification 028 amendment or physical migration begins merely because R2 passes.

## 15. Current state

    ORIGINAL_P_R8B_01=AUTHENTIC_BUT_CONFIRMATORILY_INSUFFICIENT
    CLAUDE_AUDIT=AMEND_ACCEPTED

    WMR_H_V0_2=AMENDED
    WMR_H_V0_3=CORRECTION_CANDIDATE
    A_M1_FAIL_VISIBLE_GOVERNANCE_RECOGNITION=REQUIRED
    A_M2_COMMITTED_REVISION_HISTORY_VALIDATION=REQUIRED
    RULE_BASED_LOSS_ACCOUNTED_MIGRATION=REQUIRED

    P_R8B_01_R2=CORRECTION_PROTOCOL_FROZEN
    OWNER_REPRESENTATION_DECISION=HELD

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=IMPLEMENT_AND_FREEZE_P_R8B_01_R2_HARNESS
