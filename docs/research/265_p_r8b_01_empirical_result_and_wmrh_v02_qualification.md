# Research 265: P-R8B-01 Empirical Result and WMR-H V0.2 Qualification

**Date:** 2026-09-23
**Status:** P-R8B-01 PASS / 18 OF 18 BLOCKING GATES PASS / WMR-H V0.2 EMPIRICALLY SUPPORTED / OWNER DECISION STILL HELD FOR INDEPENDENT RESULT AUDIT / NO PHYSICAL MIGRATION
**Parent protocol:** Research 263
**Harness freeze:** Research 264
**Frozen harness commit:** 2572ed76dd16ea2fff56ab907a7bdf80878e7da6
**Probe:** P-R8B-01
**Candidate:** WMR-H V0.2
**Scope:** Record the first execution of the preregistered representation probe, preserve exact gate outcomes, distinguish what was demonstrated from what remains unproven, and define the next decision boundary.
**Authority:** Empirical architecture evidence only. This record does not itself accept the representation architecture, amend Specification 028, authorize AO-10, or authorize physical migration.

## 1. Execution integrity

The probe was executed only after:

    Research 263 preregistered all blocking gates and thresholds
    Research 264 froze the concrete harness
    the harness freeze was committed and pushed at:
        2572ed76dd16ea2fff56ab907a7bdf80878e7da6

The harness and schema SHA-256 values were rechecked after execution and still exactly match Research 264.

Therefore:

    PROTOCOL_CHANGED_AFTER_RESULT=false
    HARNESS_CHANGED_AFTER_RESULT=false
    REAL_SOURCE_FIXTURE_DRIFT=false

## 2. Result

Command:

    .\.venv\Scripts\python.exe experiments\r8b_representation_probe_v01\probe.py --output experiments\r8b_representation_probe_v01\results\run_001

Observed:

    P-R8B-01
    overall = PASS
    passed  = 18
    total   = 18

Local execution output (gitignored):

    experiments/r8b_representation_probe_v01/results/run_001/result.json

Durable copied evidence:

    experiments/r8b_representation_probe_v01/evidence/run_001/result.json

Candidate artifacts under the durable evidence copy:

    artifacts/source_vault_definition.md
    artifacts/source_vault_state.json
    artifacts/specification_028_candidate.md
    artifacts/current.json
    artifacts/sqlite_semantic_rows.json
    artifacts/instance_policy.toml

No canonical source was modified by the probe.

## 3. Real-source fixture integrity

The exact preregistered real-source hashes matched:

    Source Vault workstream
        8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a

    Specification 028
        7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe

The probe therefore did not silently evaluate a changed real corpus.

## 4. Gate summary

### G01 metadata classification precision

PASS.

Eight of eight expected classifications matched.

The governed parser distinguished:

    exact-position governed metadata
    ordinary plain Markdown
    documentation about the format
    example-only fenced metadata
    malformed governed metadata
    misplaced metadata-looking fences
    duplicate immediate governed metadata
    non-H1 documents

No body example became accidental authority.

### G02 JSON-compatible TOML subset

PASS.

Native TOML:

    date
    time
    local datetime
    offset datetime

were all rejected for governed metadata.

Explicitly formatted string representation remained admissible.

### G03 selective structure

PASS.

Plain Markdown without machine metadata remained valid and non-governed.

The architecture does not require metadata on every document.

### G04 real Source Vault definition/state split

PASS.

The candidate split removed all six preregistered transition-owned facts from the human definition while retaining them in machine state:

    current workstream state
    pause reason
    return condition
    resume target
    ingestion milestone state
    Course 2 milestone state

Observed:

    removed transition facts = 6 / 6
    pairing violations       = 0

The human definition retained objective, governing procedure and durable reopen/risk meaning.

### G05 routine transition writer separation

PASS.

A routine control transition produced:

    canonical human-definition bytes changed = 0

while the machine state revision advanced.

This directly supports the central writer-matching claim.

### G06 exact stale-write protection

PASS.

A second writer using the stale exact state hash was rejected before publish.

### G07 cross-branch same-record conflict

PASS.

Two branches changed different semantic fields of the same state record while both incremented the shared revision line.

Git did not silently merge the record.

Observed:

    merge return code = 1
    conflict          = state.json

This supports the dual protection model:

    exact compare-and-swap for local mutation
    revision-line conflict for branch-level concurrency

### G08 revision semantics

PASS.

The probe rejected:

    revision-only fake mutation
    decrement
    same-revision semantic replacement

and accepted a governed merge resolution only at revision 3 after two revision-2 parents.

### G09 natural-owner relation discovery and bound

PASS.

Standalone relation records in three different semantic homes were discovered by kind rather than path.

Observed:

    repository-wide count = 3
    review bound          = 12
    attempted 13th        = REVIEW_REQUIRED

### G10 capture/receipt separation

PASS.

A machine capture stayed machine-structured during review.

Human elaboration was separate.

The capture referenced the receipt rather than reproducing its event payload.

Promotion targeted the natural canonical owner instead of flipping capture authority in place.

### G11 individual receipt identity and concurrency

PASS.

Content-addressed locators were deterministic.

Identical receipt content produced the same locator.

Different content produced different paths.

Two branches adding different receipt files merged cleanly.

Deleting one receipt did not rewrite another.

### G12 public/private receipt safety

PASS.

A public-safe receipt validated.

A synthetic private-only field and a synthetic private-only sentinel embedded in an otherwise allowed text field were both rejected.

### G13 real Specification 028 metadata conversion

PASS.

The isolated candidate preserved:

    semantic identity = SPECIFICATION:028
    authority         = canonical
    Section 1+ body   = unchanged

The new metadata was visible and parseable.

A metadata-looking example later in the body did not change the governing metadata interpretation.

### G14 committed current.json freshness

PASS.

The generated orientation self-declared:

    derived = true
    authoritative = false

Initial freshness passed.

After source state changed without regeneration:

    freshness failed
    listed revision = 1
    source revision = 2

A reader can therefore detect at least revision-level staleness without invoking the generator.

### G15 derived SQLite rebuild

PASS.

The local SQLite/FTS index was deleted and rebuilt from canonical fixtures.

The semantic rows were equivalent across rebuild.

FTS returned the real Specification 028 carrier.

The typed relation edge was present.

No unique accepted truth existed only in SQLite.

### G16 derivative-free break-glass recovery

PASS.

With no generated/query layer required, the probe reconstructed the declared recovery facts from:

    canonical workstream definition
    canonical state
    canonical specification
    authored instance policy

Recovered:

    workstream = WS-SOURCE-VAULT-BOOTSTRAP
    state      = PAUSED
    spec       = SPECIFICATION:028
    authority  = current-continuity

### G17 PSMF framework/instance separation

PASS.

A compatible framework refresh left ADS instance policy/state bytes unchanged.

An incompatible framework refresh produced:

    migration_required

rather than overwriting instance meaning.

### G18 narrow Git review shape

PASS.

The probe verified:

    routine state transition -> zero human-definition diff
    metadata-only change     -> metadata-only body-preserving change
    receipt addition         -> one new JSON text file
    specification metadata   -> visible in Markdown rather than hidden

## 5. Central falsifier result

Research 263 preregistered the most important definition/state threshold as:

    duplicated transition facts removed = 6 / 6 required
    pairing violations tolerated        = 0
    human-definition bytes changed       = 0

Observed:

    6 / 6
    0
    0

Therefore the central WMR-H writer/state split is supported by this probe rather than merely surviving synthetic examples.

## 6. What the PASS supports

The result supports the following WMR-H V0.2 direction:

    Markdown for durable human knowledge
    visible selective TOML metadata
    JSON-compatible TOML governed subset
    TOML for human-authored instance policy
    sharded pretty JSON for machine-maintained control state
    exact stale-write preconditions
    monotonic revision line for cross-branch state conflict
    natural-owner standalone semantic facts
    repository-wide bounded standalone-fact admission
    writer-matched captures
    individual immutable JSON receipts
    committed bounded current.json orientation accelerator
    JSON Schema structural validation
    derived SQLite/FTS query layer
    no canonical Project SQL database
    no canonical graph database
    generate-independent break-glass recovery
    explicit PSMF framework/instance representation seam

## 7. What the PASS does not prove

The probe does NOT prove:

    production implementation quality
    full repository migration safety
    performance at a much larger future corpus
    multi-user distributed transaction semantics
    long-run repository growth economics
    complete AO-10 behavior
    final assurance/test/CI-CD architecture
    final Specification 028 replacement text
    full file-level migration disposition
    W6/W7/W8 cutover readiness
    post-W8 architecture

The probe is architecture discrimination and bounded empirical support, not production acceptance.

## 8. Assurance implications remain separate

The owner's assurance clarification remains in force.

Current:

    tests
    check scripts
    repository-integrity aggregator
    CI workflows
    GitHub Actions topology
    validators

remain migration-era evidence/mechanisms, not automatically target architecture.

But Research 263's two companion obligations now govern transition:

    CURRENT_ASSURANCE_MIGRATION_ORACLE_OBLIGATION=true

    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

No current validator may be removed merely because WMR-H passed this representation probe.

## 9. Independent result-audit recommendation

The representation decision is material and the probe harness was authored inside the same ChatGPT-led reconciliation that defined the candidate.

Preregistration materially reduces self-confirmation risk, but it does not make independent interpretation valueless.

Recommended before asking the owner to accept WMR-H V0.2:

    one bounded independent Claude audit of:
        protocol fidelity
        harness/result integrity
        whether each PASS actually supports its claimed architecture point
        whether any gate accidentally tests only its own construction
        whether the real-source use is sufficiently discriminating
        whether the result is strong enough for owner decision

The audit must not change the already observed thresholds retrospectively.

A discovered harness defect may invalidate a gate/run but cannot be repaired by redefining success after observation.

## 10. Current state

    P_R8B_01=PASS
    P_R8B_01_GATES=18_OF_18_PASS
    HARNESS_CHANGED_AFTER_RESULT=false
    SOURCE_FIXTURE_DRIFT=false

    WMR_H_V0_2=EMPIRICALLY_SUPPORTED
    REPRESENTATION_OWNER_DECISION=HELD_FOR_INDEPENDENT_RESULT_AUDIT

    CURRENT_ASSURANCE_MECHANISMS_TARGET_PRESERVATION_RIGHT=false
    CURRENT_ASSURANCE_MIGRATION_ORACLE_OBLIGATION=true
    ASSURANCE_INVARIANT_EXTRACTION_BEFORE_REPLACEMENT=true

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=BOUNDED_INDEPENDENT_P_R8B_01_RESULT_AUDIT
