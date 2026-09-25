# Research 332: DRP-03 R2 V0.3 Public Protocol Asset Freeze

**Date:** 2026-09-25
**Status:** PUBLIC PROTOCOL ASSETS FROZEN / OWNER M-1 DEFERRAL ACTIVE / HIDDEN KEY CONSTRUCTION NEXT / NO HIDDEN SEMANTIC LABELS OR SCORING HARNESS
**Parent:** Research 331 / Research 330
**Protocol directory:** `experiments/ao10_drp03_obligation_units_r2_v03/`
**Public freeze commitment:** `experiments/ao10_drp03_obligation_units_r2_v03/public_freeze_commitment.json`
**Scope:** Freeze every public protocol, segmentation, packet, schema, public fixture, key-author packet, delivery-order and provenance asset required before independent hidden-key construction.
**Authority:** Empirical protocol freeze only. It does not accept V0.7 architecture, qualify DRP-03 R2, authorize production AO-10, authorize physical migration, retire current oracles, or switch authority.

## 1. Freeze identity

The exact public freeze manifest is bound by:

    SHA-256
        f358d03168973c33e31a0c877b3175c6804157f6da5074053767e8a9305c3150

    hash basis
        EXACT_PUBLIC_FREEZE_MANIFEST_BYTES

    manifest bytes
        8998

The same digest is the future deterministic cluster-bootstrap seed source.

The manifest binds:

    36 protocol-directory assets
    4 external architecture/authority bindings

No semantic hidden key or hidden held-out label exists in the public freeze.

## 2. Reproducibility

The full deterministic generation sequence was executed twice:

    generate_packets.py
    generate_key_author_packets.py
    freeze_public_assets.py

The manifest digest was unchanged:

    BEFORE
        f358d03168973c33e31a0c877b3175c6804157f6da5074053767e8a9305c3150

    AFTER
        f358d03168973c33e31a0c877b3175c6804157f6da5074053767e8a9305c3150

Therefore:

    PUBLIC_PACKET_REGENERATION=REPRODUCIBLE

The splitter test vectors also pass.

## 3. BIRTH packet freeze

Unique semantic catalogs:

    development
        2 events
        455 semantic items

    held-out reviewer surface
        11 opaque packet events
        2254 semantic items

The held-out surface contains the nine held-out historical events plus two controlled over-declaration fixtures.

Reviewer classification is session-bounded:

    development
        2 batches
        469 presentations

    held-out
        13 batches
        2347 presentations

No classification batch exceeds 400 presentations.

Attention-check duplicates are deterministically inserted through a separate provenance mapping and are excluded from semantic truth.

Reviewer delivery never exposes the attention mapping.

The unique semantic event catalog is delivered only after all classification batches are frozen, for grouping.

## 4. LEGACY packet freeze

The LEGACY corpus is fixed at:

    source base
        0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

    sources
        17

    semantic items
        3088

    classification batches
        18

    classification presentations
        3210

The corpus is source-disjoint from the R1 hidden witness/control sources and from held-out BIRTH proposal carriers under the V0.3 manifest.

Two source-level negative controls are present.

Hidden material-gap witnesses and already-realized false-gap controls have not yet been selected.

They must be selected independently by the private key-author stage and each must carry independent repository realization/non-realization evidence.

LEGACY remains:

    CANDIDATE_ONLY

even if its later empirical component passes.

## 5. STATE packet freeze

The public STATE surface contains:

    20 synthetic fact-validity / lifecycle fixtures
    4 real-repository candidate-fact cases
    total 24 fixtures

No expected output is stored in the public packet.

Expected outputs require two independent derivations after the public freeze.

The public state rule freezes:

    fact-validity prerequisites
    governed-deferral validity
    REVIEW_REQUIRED conditions
    DEFERRED precedence
    UNLINKED / LINKED / EVIDENCED / QUALIFIED / OPERATIONAL derivation
    owner-waiver non-transition behavior
    governance-lifecycle separation

The real fact cases include:

    AO-6 branch-rotation deferral language
    file-level migration HELD language
    the accepted M-1 governed DeferralRecord
    generic framework-extraction deferred language

Their expected states remain unlabelled.

## 6. Segmentation freeze

The splitter is now executable and frozen.

It applies the Message 009 mechanical rules:

    headings are context only

    prose, list text and blockquotes use the same sentence splitter

    structured blocks split at blank lines and minimum-indentation top-level lines

    deeper-indented lines attach to the preceding top-level line

    Markdown tables split by body row with the header retained as context

    no semantic merge/split predicate exists

Frozen sentence-splitter vectors cover:

    V0.7 version tokens
    decimals
    section-symbol references
    e.g.
    i.e.
    dotted identifiers
    URLs
    Markdown links
    colon-led prose

## 7. Reviewer exposure freeze

Fresh blind reviewers receive only the files permitted by:

    delivery_plan.json

They do not receive:

    source-path provenance
    acceptance commits
    pre-acceptance snapshot IDs
    controlled-negative identities
    attention-check mappings
    key-author packets
    hidden key material
    repository/Git/web access

BIRTH and LEGACY classification batches are sequential:

    batch N annotation freezes
        before
    batch N+1 exposure

Grouping catalogs are exposed only after component classification batches freeze.

STATE is exposed separately.

## 8. Reviewer-quality controls

Classification-session generation implements:

    primary items per batch
        <= 380

    total presentations per batch
        <= 400

    duplicate attention presentations
        3% target
        minimum 5 where batch size permits
        maximum 20

The later result must apply Research 330's within-rater consistency gates.

A quality replacement remains:

    pre-semantic-score only
    at most one replacement per slot

and all failed quality annotations remain evidence.

## 9. Key-author surface freeze

Two independent key-author slots remain required.

At least one must be fresh to:

    MC-0029
    R1 annotations/results
    the other key author's output

The bounded BIRTH key-author packets contain:

    frozen proposal semantic catalogs
    exact decision token
    proposal-source cluster
    exact acceptance commit and parent
    bounded acceptance diffs
    RESTATED rule
    DECISION_TIME_DELTA rule

The proposal/protocol author may participate only with:

    PROPOSAL_AUTHOR_BIAS_PRESENT=true

and cannot be the sole or unchecked source of truth.

LEGACY key authors receive the frozen candidate catalog and provenance sufficient to bind later independent repository evidence.

STATE key authors receive the public state packet and state rules.

No key output exists yet.

## 10. Key concealment sequence

The next stage is now allowed to create private key-author outputs.

Required order remains:

    Key A private canonical bytes
        ->
    public Key A hash commitment

    Key B private canonical bytes, blind to A
        ->
    public Key B hash commitment

    construct-validity comparison
        ->
    owner material adjudication where necessary
        or
    CONSTRUCT_UNDERDETERMINED

    final private key
        ->
    public final-key commitment

    two fresh blind reviewer annotations
        ->
    only then publish full key bytes and score

No private key may be placed in reviewer-accessible repository storage before reviewer freeze.

## 11. M-1 deferral remains active

The owner accepted:

    ACCEPT_DEFERRAL

The M-1 owner-review efficacy risk remains empirically unresolved.

The accepted DeferralRecord requires reactivation before:

    V0.7 production activation
    authority switch
    operational reliance on agent-drafted accepted declaration semantics

Future evidence remains:

    prospective seeded-error owner-review efficacy trial

The public protocol freeze does not weaken this requirement.

## 12. Still not created or authorized

    R2_HIDDEN_KEY=false
    R2_HIDDEN_LABELS=false
    R2_SCORING_HARNESS=false
    R2_REVIEWER_ANNOTATIONS=0

    V07_ACCEPTED=false
    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

## 13. Next stage

The public pre-key protocol is now frozen.

Next:

    DRP-03 R2 dual independent hidden-key construction

The first key-author action must preserve the two-author independence boundary and the reviewer concealment boundary.

At least one key author must be genuinely fresh to MC-0029/R1.

    PUBLIC_R2_FREEZE=COMPLETE
    PUBLIC_FREEZE_SHA256=f358d03168973c33e31a0c877b3175c6804157f6da5074053767e8a9305c3150
    NEXT=DUAL_PRIVATE_KEY_CONSTRUCTION
