# DRP-03 R2 V0.3 Key-Author Execution Addendum V0.1

**Date:** 2026-09-26
**Status:** FROZEN BEFORE KEY A / OPERATIONAL INTERPRETATION ONLY / PUBLIC PROTOCOL SEMANTICS UNCHANGED
**Parent public freeze:** Research 332
**Public-freeze SHA-256:** `f358d03168973c33e31a0c877b3175c6804157f6da5074053767e8a9305c3150`
**Applies to:** Key Author A, Key Author B, and any protocol-authorized pre-score replacement for either key-author slot.
**Authority:** This addendum resolves execution and serialization details left underspecified by the public freeze. It does not change the corpus, semantic definitions, thresholds, sample floors, result classes, reviewer boundary, attempt rules, or hidden-key construct.

## 1. Execution environment

Private key authoring must occur in a local, owner-controlled workspace outside every Git repository and outside storage exposed to future decision reviewers or the other key author.

For Key Author A:

    SLOT                 EXPOSED / NON-FRESH
    DISPATCHER           claude-04
    EXECUTOR             Claude Code local
    EXECUTOR_REPO_WRITE  NONE
    REPOSITORY_KEY_WRITE PROHIBITED

A Claude Code cloud session is not used for hidden-key authoring because its repository/branch return path and ephemeral VM lifecycle create unnecessary key-leak and artifact-recovery risk.

The executor may use multiple sequential local Claude Code sessions as one logical author only when all of these remain fixed:

    exact model identity / model selection
    semantic codebook
    this addendum
    frozen public inputs
    append-only precedent record
    no other-key exposure

Every phase/session identifier is recorded in private provenance.

A model/configuration change during semantic labeling requires STOP and owner review. It is not silently treated as the same author.

No subagent or parallel worker may make semantic judgments.

## 2. Input and repository boundary

Key authoring uses only:

    the frozen public R2 V0.3 assets bound by the Research 332 digest

    the bounded BIRTH key-author packets already generated at public freeze

    the frozen LEGACY corpus/evidence base defined below

    the frozen STATE packet and public state rules

    this addendum

The private workspace must not contain a writable ADS checkout.

The LEGACY evidence workspace is a separate read-only checkout at:

    0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

with remote mutation disabled/removed.

Web search, web fetch, GitHub connectors, MCP servers and unrelated local repositories are not key-author evidence sources.

## 3. Deterministic batching and attention checks

Research 330 section 24 applies to key authors as written.

The already-frozen classification-session files are the deterministic batch/attention realization for both key authors:

    packets/birth_development_classification_sessions.json
    packets/birth_heldout_classification_sessions.json
    packets/legacy_classification_sessions.json

The corresponding frozen attention-provenance files provide the presentation-to-semantic-item mapping for mechanical quality checking and final assembly.

The semantic author must not inspect the attention mapping while labeling.

For each batch:

    load the batch presentations
    load only the event/source context and bounded evidence allowed for that component
    label each presentation independently
    freeze the batch bytes and digest
    only then proceed to the next batch

A frozen batch is not edited after a later batch is exposed.

Corrections discovered while the current batch is still open may be logged and applied before that batch is frozen.

A later-discovered issue is logged as an erratum but does not retroactively rewrite a frozen batch.

Attention-check consistency is computed only after all classification batches for that component are frozen.

Quality-gate failure does not authorize label repair. It invokes the preregistered replacement semantics from Research 330.

## 4. Logical key shape

Both authors use the same canonical logical structure:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "author": { ... },
      "packet_digests": [ ... ],
      "birth": {
        "events": [
          {
            "packet_event_id": "...",
            "items": [ ... ],
            "must_join_pairs": [ ... ],
            "must_split_pairs": [ ... ]
          }
        ]
      },
      "legacy": {
        "sources": [
          {
            "packet_source_id": "...",
            "items": [ ... ],
            "must_join_pairs": [ ... ],
            "must_split_pairs": [ ... ]
          }
        ]
      },
      "state_expected_outputs": [ ... ],
      "provenance": { ... }
    }

BIRTH item objects contain exactly the fields required by `key_author_schema.json`.

LEGACY item objects contain exactly the fields required by `key_author_schema.json`.

STATE objects contain exactly the fields required by `key_author_schema.json`.

Additional private working traces may exist outside the canonical key but are not added to the canonical semantic key unless this addendum explicitly requires them.

## 5. Field interpretations

### 5.1 ambiguity

Canonical key field:

    ambiguity: boolean

`true` means the author identifies a genuinely non-material equivalent interpretation allowed by Research 330.

Material disagreement is never represented as ambiguity.

Any rationale is retained only in private working evidence.

### 5.2 LEGACY candidate_gap and evidence_refs

For every LEGACY item:

    candidate_gap
        boolean

For non-normative or non-realization-requiring items:

    candidate_gap = false

Evidence references may be empty unless the item is selected as a hidden material-gap witness or already-realized false-gap control.

A LEGACY evidence reference uses the frozen schema fields:

    evidence_type
    path
    revision
    locator_or_search_spec
    result

The `result` field is a canonical object:

    {
      "status": "REALIZED" | "NOT_REALIZED",
      "match_count": integer | null,
      "output_sha256": string
    }

Witness/control roles are derived, not authored as a new semantic field:

    hidden material-gap witness
        material = true
        realization_required = true
        candidate_gap = true
        at least one evidence_ref with result.status = NOT_REALIZED

    already-realized false-gap control
        realization_required = true
        candidate_gap = false
        at least one evidence_ref with result.status = REALIZED

The two negative-control sources remain mechanically identified by `legacy_corpus_manifest.json`; no new role field is added to item labels.

## 6. LEGACY temporal evidence horizon

All realization/non-realization evidence used for the hidden LEGACY witness/control truth is evaluated at:

    0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

This is the frozen LEGACY source/evidence horizon.

Later repository history may not be used to convert a historically unrealized obligation into an already-realized control.

Allowed evidence forms remain those frozen by Research 330:

    exact path + revision
    exact test/validator evidence already present at the frozen revision
    exact accepted realization record
    deterministic absence-search specification + frozen result
    exact successor/retirement evidence

Read-only Git queries may be used to derive the frozen evidence result.

The exact query/search specification, path/revision, result count where applicable, and hash of exact result bytes are retained in the private evidence record.

## 7. Grouping scope and non-quadratic construction

Grouping constraints are scoped exactly to the reviewer grouping surface:

    BIRTH
        within one packet_event_id only

    LEGACY
        within one packet_source_id only

Cross-event and cross-source pairs are not scored and therefore are not stored as grouping constraints.

For every pair, endpoints are lexicographically ordered:

    item_id_a < item_id_b

No pair may appear in both MUST_JOIN and MUST_SPLIT.

Candidate generation may use private working attributes such as realization owner, realization effect/artifact, qualification boundary and independent failure boundary.

However:

    every pair stored as MUST_JOIN must be individually reviewed and confirmed

    every pair stored as MUST_SPLIT must be individually reviewed and confirmed

Sampling may guide which candidate classes are worth inspecting, but an unsampled pair is never promoted by class inference.

All unreviewed or genuinely uncertain pairs remain UNCONSTRAINED.

The minimum-pair floors are reported, never targeted. No padding is allowed.

## 8. STATE independence

STATE expected outputs are derived from:

    packets/state.json
    public_fixtures/state_rules.json

and the frozen bounded STATE provenance already authorized for key authors.

Each author derives all 24 fixtures independently.

The other key author's expected outputs remain unseen.

A private rule trace may be retained for audit, but only the canonical expected-output fields enter the key.

## 9. Canonical ordering and serialization

Before hashing, the key is normalized as follows.

Object keys:

    lexicographic Unicode key order at every object level

Arrays:

    packet_digests
        sort by path

    birth.events
        sort by packet_event_id

    birth event items
        sort by item_id

    legacy.sources
        sort by packet_source_id

    legacy source items
        sort by item_id

    must_join_pairs / must_split_pairs
        first order each endpoint so item_id_a < item_id_b
        then sort by (item_id_a, item_id_b, reason)

    evidence_refs
        sort by (
            evidence_type,
            path,
            revision,
            canonical locator_or_search_spec,
            canonical result
        )

    state_expected_outputs
        sort by fixture_id

    provenance string lists / session IDs / tool lists
        sort lexicographically unless represented as an explicitly keyed chronology object

Canonical JSON encoding:

    JSON
    UTF-8
    no BOM
    ensure_ascii = false
    sort_keys = true
    separators = (",", ":")
    no trailing newline

The commitment SHA-256 and byte length are computed over those exact bytes.

## 10. Private storage and recovery

The canonical key, per-batch labels, precedent log, STATE traces, LEGACY evidence results and Claude Code transcripts are private key-derived material.

They must not enter:

    ADS Git history
    any reviewer-accessible repository
    MC-0029 collaboration messages
    GitHub branches
    connector-readable shared storage
    the future Key Author B environment

The owner retains the final private package outside all repositories.

After completion it should be encrypted and backed up in owner-controlled storage that is not exposed through the AI connectors used for Key Author B or decision review.

A later Key Author B environment must have no read access to Key A workspace, archive or local Claude Code transcript storage. A separate OS/profile is one sufficient mechanism but not the only acceptable isolation mechanism.

## 11. Key Author A provenance

Key Author A remains:

    exposed / non-fresh

The dispatcher is:

    claude-04
    conversation: 04 - Assurance and Delivery Architecture Design

The semantic executor is:

    Claude Code local
    exact model/version recorded at launch

Required provenance includes:

    Claude Code version
    exact model selection / model identifier as exposed by the product
    operating-system class
    plan / execution surface
    phase session IDs
    private permission configuration digest
    MCP/web status
    public-freeze digest
    key-author-packet digests
    frozen LEGACY revision
    batch counts
    compaction events
    restarts
    open-batch corrections / later errata counts
    within-rater quality metrics

Required flags:

    prior_mc0029_exposure = true
    other_key_seen = false

Proposal-author-bias provenance must distinguish the exposed dispatcher history from the semantic executor's own authorship history.

## 12. Completion and repository return

The local executor returns only a non-secret commitment block to the owner/dispatcher.

Allowed commitment information includes:

    exact Key A SHA-256
    exact canonical byte length
    canonical serialization identifier
    public-freeze digest
    key-author packet manifest digest
    LEGACY revision
    executor surface/version/model
    phase session IDs
    permission-configuration digest
    prior exposure / author-bias / other-key-seen flags
    aggregate workload counts
    validation PASS/FAIL per mechanical check
    within-rater consistency values
    statement that private artifact is preserved outside repositories and reviewer-accessible storage

Forbidden repository/message content includes:

    item labels
    normative kinds
    material flags
    realization-required flags
    RESTATED / DECISION_TIME_DELTA flags
    ambiguity identities
    grouping pairs
    witness/control identities
    LEGACY evidence results
    STATE expected outputs
    precedents
    per-event/per-kind semantic counts that materially narrow hidden truth
    full or partial key bytes

Only after this return may claude-04 author Message 010 under its existing repository write boundary.

## 13. Freeze consequence

This addendum is frozen before any Key A semantic label exists.

It binds both key authors symmetrically.

It does not modify the Research 332 public-freeze digest.

It resolves only previously underspecified execution/representation details required to create comparable independently authored keys.

    PUBLIC_PROTOCOL_SHA256=f358d03168973c33e31a0c877b3175c6804157f6da5074053767e8a9305c3150
    PUBLIC_PROTOCOL_SEMANTICS=UNCHANGED
    KEY_AUTHOR_EXECUTION_ADDENDUM=V0.1
    KEY_A_LABELS_CREATED=false
    NEXT=OWNER_LAUNCH_LOCAL_CLAUDE_CODE_KEY_A
