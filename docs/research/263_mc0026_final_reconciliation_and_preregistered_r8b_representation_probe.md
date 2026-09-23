# Research 263: MC-0026 Final Reconciliation and P-R8B-01 Preregistered Representation Probe

**Date:** 2026-09-23
**Status:** WMR-H AMENDED / PROBE PROTOCOL PREREGISTERED / MC-0026 READY TO CLOSE / NO OWNER REPRESENTATION DECISION / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Shared requirements:** Research 260
**ChatGPT independent candidate:** Research 261 / GCHR-DQI
**Comparative synthesis:** Research 262 / WMR-H
**Claude comparative critique:** MC-0026 Message 003 / commit 0e9225bd957859b4d7a8bb3511e2191a9230900f
**Candidate after reconciliation:** WMR-H V0.2
**Scope:** Apply Claude's bounded comparative amendments, freeze the representation candidate to be tested, preregister falsifiable P-R8B-01 pass/fail criteria before execution, and carry the owner's assurance/CI-CD anti-anchoring clarification into migration and later assurance design.
**Authority:** Architecture research and empirical-probe protocol only. No representation target is owner-accepted by this record. Specification 028 remains unchanged. No physical migration, AO-10 implementation, authority switch or PSMF extraction is authorized.

## 1. Comparative disposition

Claude returned:

    WMR_H_DISPOSITION=AMEND
    DEFINITION_STATE_SPLIT=AMEND
    VISIBLE_TOML_METADATA=KEEP
    INDEPENDENT_FACT_NATURAL_OWNER=KEEP
    HYBRID_CAPTURES=KEEP
    RECEIPT_FORM=JSON
    COMMITTED_CURRENT_JSON=KEEP
    ASSURANCE_ARCHITECTURE_FREEDOM=AMEND
    P_R8B_01_READY=NO
    REPRESENTATION_OWNER_DECISION_READY_AFTER_PROBE=YES

ChatGPT accepts all material findings.

No R5/R6/R7/R8-A premise is reopened.

The representation candidate becomes:

    WMR-H V0.2
    Writer-Matched Hybrid Representation, amended

The owner representation decision remains deliberately deferred until P-R8B-01 is executed against this preregistered protocol.

## 2. V0.2 core representation

### 2.1 Human durable knowledge

    Markdown

Human prose is never rewritten merely because machine control state changes.

### 2.2 Selective governed metadata

    visible fenced TOML project-meta block

A governed block is recognized only when all are true:

    first line is an H1 title
    the metadata block is the first non-title content element
    only blank lines may intervene
    the fenced info string is the exact governed metadata tag
    the TOML parses successfully
    the normalized data satisfies the selected profile

A tagged example later in the document body is never metadata.

Documentation examples must use a distinct example info string.

The metadata semantic model is restricted to a JSON-compatible subset.

Native TOML date/time values are forbidden in governed metadata. Semantic timestamps use explicitly formatted strings.

### 2.3 No duplicate metadata by default

Do not author metadata fields that existing authoritative mechanisms already provide unless the semantic value differs.

Default examples:

    document title
        from H1

    Git author/committer history
        not duplicated as generic author metadata

    Git modification time
        not duplicated as generic modified timestamp

    generated summary
        not duplicated as authored metadata unless independently governed

### 2.4 Representation follows contracted writer

The rule is about the legitimate contract writer, not the physical human or process that happens to type the bytes during a transition period.

Therefore a pre-AO-10 manual edit of a machine-state JSON record is still an override of a machine-owned contract and must follow the same revision/precondition rules.

### 2.5 Definition versus state discriminator

Freeze the operational test:

> If an ordinary state transition can change the field, the field belongs in machine control state rather than the human definition carrier.

For a workstream:

    DEFINITION / human carrier
        objective
        scope
        governing procedure
        durable risks/reopen triggers
        durable semantic relations

    STATE / Project-system JSON
        current state
        milestone realization
        current pause reason
        current return/resume condition
        current resume target
        other transition-mutated values

A governed owner decision to defer an accepted obligation is different:

    governing deferral
        -> governance/planning knowledge

    current realization/pause state
        -> Project-system control state

A routine pause must produce zero modification to the human definition carrier.

## 3. Durable control concurrency model

WMR-H V0.2 requires both:

    exact blob/content precondition
    monotonic record revision

They solve different problems.

### 3.1 Exact compare-and-swap

Before JW1 or a manual governed override mutates a state record:

    read current exact blob/content revision
    bind expected value
    re-check immediately before write/commit
    reject stale mutation if the record changed

### 3.2 Cross-branch conflict line

Each state record contains:

    "revision": <integer>

Every mutation to that record MUST increment the revision.

The field is serialized on one stable line in pretty JSON.

Two branches mutating different fields of the same record therefore also mutate the same revision line and Git must surface a merge conflict rather than silently combining consequential state.

### 3.3 Merge-resolution rule

A human/governed reconciliation of concurrent same-record changes must:

    inspect both parent states
    choose an explicit semantic resolution
    set revision > each parent revision
    revalidate the whole record
    record reconciliation evidence when consequence warrants it

Automatic content merge is not accepted as semantic state reconciliation.

Exact final historical revision-validation mechanics remain an implementation/probe question, but silent clean merge of two concurrent same-record state mutations is a probe falsifier.

## 4. Independent semantic facts

Natural-owner placement is retained.

Resolver machinery discovers standalone semantic facts by declared kind/profile, not by one universal directory.

Candidate homes include:

    governance owner
    Project-system instance owner
    evidence owner

depending on semantic responsibility.

### 4.1 Repository-wide boundedness

Preregister:

    RC3_STANDALONE_RELATION_REVIEW_BOUND = 12

This count is repository-wide across all natural-owner homes.

The 13th authored standalone relation record triggers AO-4 architecture review before additional population.

This is a review bound, not a target count.

Ordinary source-owned relations do not count toward this bound.

## 5. Captures and receipts

### 5.1 Writer-matched captures

    human capture
        Markdown + selective visible metadata

    machine capture
        JSON

A machine capture is not converted in place into prose during human review.

Human elaboration is:

    a new human capture referencing the machine capture

or:

    authored directly into the promotion target

according to review intent.

### 5.2 Capture versus receipt

    receipt
        immutable evidence that something happened

    capture
        reviewable candidate about what something may mean

If an event produces both:

    capture references receipt by ID
    capture does not restate the receipt payload as a second event truth

### 5.3 Receipt physical form

Select for V0.2 probe:

    individual immutable JSON record

Recommended locator scheme:

    month partition directory
    content-digest-derived filename

Properties:

    identical receipt content -> identical receipt locator
    different receipts -> different paths
    parallel receipt creation -> no shared-file write
    retention -> remove whole receipt record when policy permits

JSONL remains a rejected comparison arm unless probe evidence materially favors it.

## 6. Committed machine orientation

Retain candidate:

    project/system/generated/orientation/current.md
    project/system/generated/orientation/current.json

Both are:

    derived
    non-authoritative
    source-bound
    rebuildable
    optional for break-glass recovery

current.json must declare enough source-boundary information for a reader to recognize its derivation status.

A state-changing commit that leaves current.json stale must fail the current-era qualification used during migration and, later, the future assurance mechanism selected for the target architecture.

A tool-less reader that cannot verify freshness must treat current.json as advisory.

A reader able to inspect its source revision/digest information must detect mismatch.

## 7. Assurance freedom amended with two transition obligations

The owner's anti-anchoring principle remains accepted:

> Verification requirements and historical evidence may survive; verification mechanisms do not survive by inertia.

Claude correctly identifies two required companion rules.

### 7.1 Migration-oracle obligation

A current validator/check may have no target-preservation right while still being required during migration.

Current verification mechanisms remain available as migration/equivalence oracles until the behavior they cover has been:

    explicitly dispositioned
    represented in the successor assurance model
    equivalence-qualified where preservation is required
    released from oracle duty by a governed cutover gate

Therefore:

    "not future architecture"
        !=
    "safe to delete now"

### 7.2 Invariant-extraction obligation

Before a current assurance mechanism is superseded, extract the invariants it actually enforces.

Each invariant receives:

    KEEP
    GENERALIZE
    SUPERSEDE
    DROP_WITH_REASON

The future assurance architecture is derived from:

    J06/J07 responsibilities
    accepted architecture
    migration/cutover needs
    extracted current invariants
    current mechanism defects/negative evidence
    new target-specific failure modes

It is not derived from headline check names alone.

This prevents subtle current safeguards from disappearing merely because their current implementation is being replaced.

## 8. P-R8B-01 empirical probe purpose

P-R8B-01 is an architecture discriminator, not production implementation and not the future assurance architecture.

It tests whether WMR-H V0.2's central representation claims survive concrete authoring, parsing, Git concurrency, recovery, indexing and real-carrier conversion.

The harness may use current repository tools for convenience.

Using a tool in the probe does not select it for the future target.

## 9. P-R8B-01 real-source boundary

The probe MUST include at least:

    REAL-1
        docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md

    REAL-2
        docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md

The canonical files are not modified.

The probe creates candidate representations in its isolated fixture/output area.

For REAL-1, the probe splits the current mixed workstream carrier into:

    human definition candidate
    machine state candidate

For REAL-2, the probe produces a candidate governed Markdown representation with the visible metadata model while preserving normative body meaning.

Synthetic fixtures remain allowed for edge/failure cases.

## 10. P-R8B-01 preregistered gates

All blocking gates below must pass for the probe to support an owner representation decision.

A failed blocking gate causes:

    WMR-H V0.2 = AMEND_REQUIRED

unless the failure is proven to be a probe-harness defect.

### G01 Metadata classification precision

Fixture set MUST contain:

    valid governed carrier in exact position
    plain Markdown with no metadata
    document ABOUT the metadata format with tagged example in body
    body example using example info string
    malformed TOML in governed position
    governed tag in wrong position
    duplicate governed block
    non-H1 title case

Pass:

    100% expected governed/non-governed/error classification
    zero false-positive body examples
    zero false-negative governed carriers

Any misclassification is blocking failure.

### G02 JSON-compatible TOML semantic subset

Pass:

    native TOML date
    native TOML time
    native TOML local datetime
    native TOML offset datetime

are all rejected in governed metadata.

Equivalent explicitly formatted strings are accepted when schema-valid.

Any native TOML datetime value accepted is blocking failure.

### G03 RR-04 selective-structure negative control

Pass:

    a valid plain Markdown carrier with no metadata block
    remains valid as a non-governed/non-first-class document

If metadata becomes mandatory for every document, blocking failure.

### G04 Real Source Vault definition/state split

From REAL-1, at minimum these currently duplicated transition-owned facts must be represented only in the machine state candidate and absent from the human definition candidate:

    current workstream state
    current pause reason
    current return condition
    current resume target
    SOURCE-VAULT:INGESTION milestone state
    COURSE:2 milestone state

Pass:

    six of six transition-owned facts removed from the human definition
    six of six present in machine state
    zero conflicting duplicate copies in human metadata/body
    state record references the definition's semantic workstream identity
    human definition still preserves objective, scope, governing procedure
    and durable risk/reopen semantics

Any missing state fact, duplicate current-state truth, or broken pairing is blocking failure.

### G05 Routine transition writer separation

Apply a routine pause/resume-state transition to the REAL-1 candidate.

Pass:

    canonical human definition file diff = zero bytes
    machine state record changes
    derived orientation may change
    no human knowledge rewrite is required

Any canonical human-definition change is blocking failure.

### G06 Exact stale-write protection

Given state revision N and exact expected blob/content precondition:

    writer A mutates to N+1
    writer B attempts mutation from stale N

Pass:

    writer B is rejected before publish

Any stale consequential state mutation accepted is blocking failure.

### G07 Cross-branch same-record conflict

Create two Git branches from the same state record revision.

Branch A and Branch B mutate different semantic fields.

Both MUST increment the same revision line.

Pass:

    Git merge does not complete cleanly
    revision-line conflict is surfaced
    explicit semantic reconciliation is required

If Git silently produces a clean merged consequential record, blocking failure.

### G08 Revision semantics

Pass:

    ordinary mutation increments revision exactly once
    unchanged record cannot claim a new semantic revision through the
    probe mutation API
    decrement is rejected
    same/lower revision replacement is rejected
    governed merge resolution uses revision above both parent revisions

Any accepted non-monotonic consequential state update is blocking failure.

### G09 Natural-owner standalone relation discovery

Create standalone relation fixtures in:

    governance
    Project-system instance
    evidence

Pass:

    all are discovered by kind/profile independent of path
    semantic resolver produces the same relation model
    repository-wide standalone count is 3

Then test the bound:

    12 authored standalone relation records
        -> within review bound

    attempted 13th
        -> review trigger raised before normal admission

Per-directory counting that allows >12 repository-wide is blocking failure.

### G10 Capture/receipt separation

Pass:

    machine capture remains JSON through review
    human elaboration is separate
    capture references receipt ID
    receipt event payload is not duplicated as second capture event truth
    promotion updates/creates natural canonical owner rather than
    flipping capture authority in place

Any in-place JSON-to-prose conversion or authority flip is blocking failure.

### G11 Individual receipt identity/concurrency

Pass:

    receipt locator is deterministic from content digest
    identical receipt produces same locator
    distinct receipt produces distinct locator
    two branches adding distinct receipt files merge cleanly
    deleting one retained receipt does not rewrite another retained receipt

Any same-path collision for different receipt content is blocking failure.

A JSONL union-merge comparator MAY be measured, but it is non-gating unless it reveals a material falsifier of the selected JSON design.

### G12 Public/private receipt safety

Use only synthetic public/private sentinels.

Pass:

    known public-safe receipt payload validates
    payload containing explicitly disallowed private-only field/sentinel
    is rejected fail-closed by structural or semantic validation

Any accepted disallowed private-only sentinel is blocking failure.

### G13 Real Specification 028 metadata conversion

From REAL-2, build an isolated candidate governed carrier.

Pass:

    semantic identity remains SPECIFICATION:028
    authority role remains canonical/governing-equivalent
    normative body beginning at Section 1 remains semantically unchanged
    candidate metadata is visible and parseable
    body examples cannot be misclassified as metadata
    no operational state is introduced into descriptive metadata

A metadata conversion that changes normative body meaning or loses identity/authority is blocking failure.

### G14 Generated current.json freshness

Generate current.json from canonical state.

Pass:

    generated file declares derived/non-authoritative role
    source record identity + revision are included
    source boundary digest/version is included
    unchanged sources reproduce deterministic semantic content
    changing canonical state without regenerating current.json causes
    freshness validation failure
    a reader comparing listed source revision against source record can
    detect a mismatch without running the generator

If stale generated state passes freshness qualification, blocking failure.

### G15 Derived SQLite rebuild

Pass:

    SQLite index is deletable
    rebuild from canonical fixtures succeeds
    identity/relation/workstream rows match expected semantic model
    FTS query returns expected real/synthetic carrier
    typed edge traversal returns expected relation
    repeated rebuild from unchanged inputs yields equivalent semantic rows

If unique accepted truth exists only in SQLite or rebuild cannot recover the expected model, blocking failure.

### G16 Break-glass without derivatives

Delete/withhold:

    SQLite index
    generated current.md
    generated current.json
    optional graph/vector cache

Pass:

    canonical workstream definition + state
    canonical governing specification
    canonical instance policy

remain directly inspectable and sufficient for the probe's declared recovery questions.

If a derivative is required to determine the tested canonical state/authority, blocking failure.

### G17 PSMF framework/instance separation

Synthetic framework refresh updates generic parser/schema/mechanism fixtures while preserving ADS instance policy/state fixture bytes.

Pass:

    instance policy/state unchanged
    refreshed framework still validates supported instance version or
    fails with explicit compatibility/migration requirement
    no silent overwrite of ADS instance meaning

Any silent instance overwrite is blocking failure.

### G18 Git review quality

This gate is deliberately narrow and objective.

Pass:

    routine REAL-1 state transition changes no canonical human definition
    metadata-only governing change produces a bounded text diff
    receipt addition is one new text file
    real specification conversion exposes metadata visibly rather than
    only through hidden/non-rendered structure

No scalar aesthetic score is used.

## 11. F2 definition/state falsifier threshold

Claude correctly requests an explicit pre-run threshold for the central split.

The split is supported only if:

    REAL-1 removes all 6 preregistered duplicated transition-owned facts
    from the human definition
    AND
    introduces 0 pairing violations
    AND
    a routine transition modifies 0 bytes of the canonical human definition

Therefore:

    duplicated transition facts removed = 6 / 6 required
    pairing violations tolerated = 0
    human-definition bytes modified by routine transition = 0

Any failure on those numbers falsifies the tested split at V0.2.

## 12. Probe outcome classes

After execution:

    PASS
        G01-G18 all pass

    AMEND_REQUIRED
        one or more blocking gates fail for an architecture reason

    HARNESS_INVALID
        observed failure is proven to arise from probe implementation
        rather than the candidate; fix harness and rerun against unchanged
        preregistered gates

No gate thresholds may be weakened after seeing results without recording that change as a new protocol version and invalidating the original confirmatory claim.

## 13. Post-probe decision sequence

If PASS:

    ChatGPT reconciles evidence
    owner receives explicit representation decision candidate
    owner decides KEEP / AMEND / REOPEN as applicable
    accepted representation then informs:
        from-scratch assurance architecture
        Specification 028 amendment
        exact file-level migration manifest
        AO-10 implementation/qualification
        physical W5 migration later

If AMEND_REQUIRED:

    classify defect
    amend representation architecture
    preregister successor probe where needed
    do not request owner acceptance of the failed candidate

## 14. MC-0026 disposition

MC-0026 has satisfied its collaboration purpose.

Claude's final critique is accepted into WMR-H V0.2 and the empirical handoff.

No further Claude response is required before P-R8B-01.

Claude may be re-engaged after probe evidence if a material interpretation dispute remains.

## 15. Current state

    MC0026=READY_TO_RESOLVE
    CHATGPT_CANDIDATE=GCHR-DQI
    CLAUDE_CANDIDATE=WMR
    COMPARATIVE_V01=WMR-H
    COMPARATIVE_V02=WMR-H_V0_2

    REPRESENTATION_FOLLOWS_CONTRACTED_WRITER=true
    DEFINITION_STATE_OPERATIONAL_TEST=IF_TRANSITION_CHANGES_IT_STATE
    STATE_BLOB_PRECONDITION=REQUIRED
    STATE_MONOTONIC_REVISION=REQUIRED
    STATE_CROSS_BRANCH_CONFLICT=REQUIRED

    VISIBLE_TOML_METADATA=RETAINED_WITH_STRICT_POSITION
    TOML_JSON_COMPATIBLE_SUBSET=REQUIRED
    RC3_STANDALONE_RELATION_REVIEW_BOUND=12
    HYBRID_CAPTURES=RETAINED
    RECEIPT_FORM=INDIVIDUAL_JSON
    RECEIPT_CONTENT_ADDRESSING=CANDIDATE
    COMMITTED_CURRENT_JSON=RETAINED_CANDIDATE

    CURRENT_ASSURANCE_MECHANISMS_TARGET_PRESERVATION_RIGHT=false
    CURRENT_ASSURANCE_MIGRATION_ORACLE_OBLIGATION=true
    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

    P_R8B_01=PREREGISTERED
    P_R8B_01_GATES=18
    REPRESENTATION_OWNER_DECISION=AFTER_PROBE
    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=COMMIT_PREREGISTRATION_THEN_EXECUTE_P_R8B_01
