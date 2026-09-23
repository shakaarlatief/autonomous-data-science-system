# Research 271: P-R8B-01-R2 Attempt 3 PASS and WMR-H V0.3 Owner-Decision Readiness

**Date:** 2026-09-23
**Status:** CORRECTED PROBE PASS / 18 OF 18 BLOCKING GATES PASS / 2 OF 2 AMENDMENT GATES PASS / WMR-H V0.3 OWNER DECISION READY / NO OWNER ACCEPTANCE YET / NO PHYSICAL MIGRATION
**Parent correction protocol:** Research 266
**Attempt-3 freeze:** Research 270
**Frozen harness commit:** 17c48ac8d7810b5d938532e65367e8aa550e101c
**Execution checkpoint:** Checkpoint 605
**Probe:** P-R8B-01-R2
**Candidate:** WMR-H V0.3
**Scope:** Record the third corrected execution result, reconcile it against the MC-0027 audit requirements and unchanged Research 263 thresholds, and determine whether the representation architecture is ready for explicit owner decision.
**Authority:** Empirical architecture evidence and owner-decision recommendation only. This record does not itself accept WMR-H V0.3, amend Specification 028, authorize AO-10, or authorize physical migration.

## 1. Execution integrity

Attempt 3 executed only after:

    Research 269 classified attempt 2 as HARNESS_INVALID
    the G04 repair was made prospectively
    the repaired harness was AST-parsed
    the repaired harness was committed and pushed
    Research 270 froze exact Git-blob hashes at:
        17c48ac8d7810b5d938532e65367e8aa550e101c
    Checkpoint 604 recorded the freeze before execution

The result binds itself to:

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    HARNESS_COMMIT=17c48ac8d7810b5d938532e65367e8aa550e101c

and records all six frozen harness hashes plus the two real-source fixture hashes.

Observed binding matches Research 270 exactly.

Therefore:

    THRESHOLDS_CHANGED_AFTER_FREEZE=false
    CANDIDATE_CHANGED_AFTER_FREEZE=false
    HARNESS_BINDING_MATCH=true
    REAL_SOURCE_FIXTURE_DRIFT=false

## 2. Attempt-3 result

Command:

    .\.venv\Scripts\python.exe experiments\r8b_representation_probe_v02\probe.py --harness-commit 17c48ac8d7810b5d938532e65367e8aa550e101c --output experiments\r8b_representation_probe_v02\evidence\run_003

Observed:

    P-R8B-01-R2
    overall             PASS
    blocking gates      18 / 18 PASS
    amendment gates      2 / 2 PASS

Durable evidence:

    experiments/r8b_representation_probe_v02/evidence/run_003/

No canonical source was modified.

## 3. G04 repair result

The specific attempt-2 defect is closed.

Real converted definition:

    detected current transition-owned assertions = 0

Injected six-fact negative control:

    detected current transition-owned assertions = 6

Pairing:

    pairing violations = 0

The durable sentence:

    "A PAUSED state is routing..."

is correctly permitted because it explains state semantics rather than asserting the current state of this workstream.

The original Research 263 six-current-fact threshold is unchanged.

## 4. Corrected audit gates

The seven gates Claude classified INVALID now all pass through non-tautological implementations.

### G05

PASS.

A real file-backed transition changed:

    machine state file
        yes

    human definition
        0 bytes

A co-located negative control produced a nonzero human-definition diff.

### G08

PASS.

Measured rejection:

    revision-only mutation
    decrement
    same-revision semantic replacement
    skipped ordinary revision
    invalid merge revision

No-op transition and merge validators are detected by the negative controls.

Committed-history validation:

    valid rev1 / rev2 + rev2 / rev3 merge history
        accepted

    corrupted committed history
        rejected

### G10

PASS.

File-backed capture/review/promotion preserved:

    machine capture bytes
    receipt bytes

while producing:

    separate human review
    natural canonical target

Capture authority remained candidate.

### G13

PASS.

Rule-based real Specification 028 conversion preserves:

    semantic identity        SPECIFICATION:028
    authority               canonical
    lifecycle mapping       frozen
    non-metadata content    preserved
    declared references     11
    provenance entries      2
    authority clause        preserved
    loss manifest           complete

No source material covered by the conversion contract is silently dropped.

### G16

PASS.

The probe:

    materialized derivatives
    deleted the generated/query surfaces
    recovered from project_anchor.json and canonical files only

The generated-only locator negative control failed visibly.

### G17

PASS.

The framework refresh actually replaced:

    framework.json
    policy.schema.json
    parser_rules.json

A compatible refresh validated the unchanged ADS instance.

An incompatible refresh produced:

    migration_required

Instance policy/state bytes remained unchanged.

### G18

PASS.

Git-computed review shapes verify:

    routine transition
        zero human-definition diff

    metadata-only change
        body preserved and visible bounded diff

    receipt addition
        one new JSON text file

    Specification 028 conversion
        visible metadata in Git diff

## 5. Strengthened previously weak gates

### G02

PASS.

Native TOML date/time values are tested in a schema-permitted location.

They fail because of the JSON-compatible TOML rule, not because the schema rejects the key.

A no-op compatibility checker makes the negative case valid, isolating the intended mechanism.

### G04

PASS.

In addition to the corrected current-assertion detector:

    removed transition facts       6
    current assertions detected    0
    negative-control assertions    6
    pairing violations             0
    provenance preserved           6
    references preserved           4
    loss manifest                  complete

### G09

PASS.

Repository-wide relation discovery feeds the admission bound directly.

Observed:

    discovered records             12
    attempted 13th                 REVIEW_REQUIRED
    malformed relation             rejected visibly

### G15

PASS.

SQLite/FTS is built by rereading canonical files from disk.

The index is deleted, canonical files are reread, and the rebuild produces equivalent semantic rows.

## 6. Previously valid gates retained

The previously valid gates continue to pass.

### G01

Visible governed metadata classification works across the original eight preregistered positive/negative cases.

### G03

Plain Markdown remains valid without governed metadata.

### G06

Exact stale-write precondition rejects a stale writer.

### G07

The branch-level revision-line experiment now includes a permanent control arm:

    revision bump present
        merge conflict

    revision bump absent
        clean merge

The control cleanly produces the concrete hazard:

    state = ACTIVE
    pause_reason still present
    ingestion = IN_PROGRESS

This is direct causal evidence for the shared revision line.

### G11

Individual content-addressed JSON receipts retain:

    deterministic identity
    distinct-content path separation
    clean parallel creation
    isolated retention

The evidence claim remains deliberately narrow and does not claim universal superiority over every JSONL design.

### G12

Public-safe receipt validation accepts the public fixture and rejects both:

    disallowed private-only field
    private-only sentinel hidden in an otherwise allowed text field

### G14

Generated current.json remains:

    deterministic
    derived
    non-authoritative

Staleness is detected for:

    revisioned machine state
    revisionless human definition via source hash

The tool-less comparison claim remains scoped to revisioned sources only.

## 7. WMR-H V0.3 amendment gates

### AM1-G1

PASS.

Governance recognition now handles:

    UTF-8 BOM
    leading blank line
    Setext H1

as GOVERNED rather than silently plain.

An indented pseudo-fence remains plain.

A body example remains plain.

The fail-open authority gap identified by Claude is closed in the candidate contract/probe.

### AM2-G1

PASS.

Committed revision-history validation is required and exercised.

Observed:

    valid branch/merge history
        accepted

    skipped committed revision
        rejected

The revision-line design therefore no longer relies only on writer discipline.

## 8. Real-carrier evidence

The two real carriers are now used in a materially more discriminating way than in the original probe.

### Source Vault workstream

The conversion is rule-driven over its existing declaration and current-state block.

It produces:

    human workstream definition
    machine control state
    loss/disposition manifest

The manifest covers every legacy structured field.

Durable semantics, public/private boundary, risk/reopen triggers, provenance, references and expected-to-resume meaning are explicitly retained or moved.

### Specification 028

The conversion is rule-driven over its existing declaration and human content.

It preserves all non-legacy-metadata content and explicitly maps:

    identity
    authority
    frozen lifecycle/status
    references
    provenance

This is architecture-discriminating conversion evidence, not merely hand-authored target illustration.

It is still not production migration proof.

## 9. Evidence scope

The corrected PASS supports selection of the representation architecture direction.

It does NOT establish:

    production implementation quality
    complete repository migration safety
    final assurance/test/CI-CD architecture
    final Specification 028 amendment text
    final file-by-file disposition manifest
    complete AO-10 behavior
    W6/W7/W8 cutover readiness
    performance at arbitrary future repository scale

Those remain later stages.

## 10. Representation architecture now supported for owner decision

WMR-H V0.3 consists of the following accepted-candidate direction.

    durable human Project knowledge
        Markdown

    selective machine-readable descriptors on governed human carriers
        visible fenced TOML metadata
        only where machine semantics are required

    governed TOML semantics
        restricted to a JSON-compatible value subset

    human-authored Project-system instance policy
        TOML

    machine-maintained durable Project control state
        sharded pretty JSON

    state concurrency
        exact stale-write/content precondition
        plus monotonic committed revision history

    machine contracts
        versioned JSON Schema over normalized structured representations

    standalone independent semantic facts
        natural-owner structured records
        repository-wide review bound = 12

    captures
        representation follows contracted writer
        human captures in human-readable carriers
        machine captures in JSON

    receipts
        selective immutable individual JSON records
        content-addressed locator candidate

    generated orientation
        committed bounded current.md/current.json acceleration
        derived and non-authoritative
        source-bound and freshness-qualified
        never required for break-glass recovery

    query/search acceleration
        derived rebuildable SQLite/FTS

    graph semantics
        typed canonical relations
        derived graph projection
        no canonical graph database required

    vector retrieval
        optional derived cache only

    canonical Project SQL database
        no

    broad event-sourcing architecture
        no

    break-glass recovery
        canonical source + stable anchor
        derivative-independent

    PSMF seam
        framework mechanism and ADS instance meaning remain independently replaceable

    governance recognition
        intended governed carrier is GOVERNED or ERROR
        never silently downgraded to plain by BOM/leading-whitespace/title variation

    real-carrier migration
        rule-based and loss-accounted

## 11. Assurance anti-anchoring remains unchanged

The corrected probe itself does not become future assurance architecture.

Current verification machinery still has:

    TARGET_PRESERVATION_RIGHT=false

but may retain:

    MIGRATION_ORACLE_DUTY=true

until released by later equivalence/cutover gates.

Before replacement:

    actual enforced invariants must be extracted and dispositioned

The defects found in the first two harness attempts reinforce rather than weaken this rule.

## 12. Owner-decision readiness

Claude's MC-0027 audit stated that owner readiness was blocked because seven original gates had not validly passed.

The audit explicitly prescribed correcting those gates against unchanged thresholds.

That requirement is now satisfied.

Attempt 2 additionally exposed and isolated a false-positive G04 implementation defect.

Attempt 3 prospectively repaired that defect and passes:

    18 / 18 original blocking gates
    2 / 2 WMR-H V0.3 amendment gates

with exact frozen Git-blob binding.

No valid empirical result currently falsifies the WMR-H V0.3 direction.

Therefore:

    OWNER_REPRESENTATION_DECISION_READY=YES

Recommended owner disposition:

    ACCEPT

The recommendation means accept WMR-H V0.3 as the R8-B target representation architecture direction.

It does NOT mean:

    accept current temporary probe implementation as production code
    begin physical migration
    switch authority
    freeze future architecture permanently

AO-4 remains available if later evidence justifies amendment or reopening.

## 13. Sequence after owner acceptance

If the owner ACCEPTS:

    close MC-0027
    freeze R8-B as accepted
    begin from-scratch assurance / verification / CI-CD architecture design
    reconcile Specification 028 against accepted R8-A/R8-B
    complete exact file-level migration/disposition planning
    reconcile and implement AO-10 against the final target
    only later authorize physical W5 migration

If the owner AMENDS or REOPENS:

    record exact owner concern
    apply AO-4
    do not advance to downstream architecture realization

## 14. Current state

    P_R8B_01_R2_ATTEMPT_1=HARNESS_INVALID
    P_R8B_01_R2_ATTEMPT_2=HARNESS_INVALID
    P_R8B_01_R2_ATTEMPT_3=PASS

    BLOCKING_GATES=18_OF_18_PASS
    AMENDMENT_GATES=2_OF_2_PASS
    HARNESS_BINDING_MATCH=true
    THRESHOLDS_CHANGED=false

    WMR_H_V0_3=OWNER_DECISION_CANDIDATE
    OWNER_REPRESENTATION_DECISION_READY=true
    CHATGPT_RECOMMENDATION=ACCEPT
    OWNER_REPRESENTATION_DECISION=PENDING

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=OWNER_REPRESENTATION_DECISION
