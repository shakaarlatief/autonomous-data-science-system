# Research 423: Fresh Key Author B STATE+BIRTH Automated Control-Plane Design

**Date:** 2026-10-01
**Status:** DESIGN FROZEN BEFORE KEY B SEMANTICS / IMPLEMENTATION + QUALIFICATION AUTHORIZED / SEMANTIC EXECUTION NOT STARTED
**Parent:** Research 422 / Research 421 owner acceptance
**Scope:** Freeze the clean, blind, automated Key Author B execution/control architecture for the accepted STATE+BIRTH component scope before any Key B semantic output exists.
**Authority:** Prospectively frozen control-plane design only. Research 421 already authorizes implementation and mechanical qualification of the clean Key B control plane. This record does not itself create a Key B semantic label, start a semantic session, compare keys, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. Key B role

Key Author B is the required fresh independent author.

The Key B semantic executor must have:

    prior_mc0029_exposure = false
    other_key_seen = false
    proposal_author_bias = false

The task owner/dispatcher may know that a Key A commitment exists, but the Key B semantic process must not receive:

    Key A labels
    Key A grouping pairs
    Key A STATE outputs
    Key A semantic transcripts
    Key A private precedents
    Key A attention mappings
    Key A canonical bytes
    Key A evidence results
    the private reason/item identities behind the LEGACY failure
    Key A commitment contents beyond the non-secret fact that the required prior commitment exists

The historical LEGACY component is outside Key B's semantic scope for this R2 attempt.

## 2. Fixed semantic scope

Key B authors only:

    STATE
    BIRTH classification
    BIRTH grouping

Key B does not author:

    LEGACY classification
    LEGACY candidate-gap
    LEGACY evidence
    LEGACY grouping

The current R2 historical LEGACY construct remains:

    INCONCLUSIVE
    CONSTRUCT_VALIDITY_NOT_ESTABLISHED

## 3. Clean fixed private root

The Runtime Bridge resolves one fixed machine-local Key B root server-side.

The caller cannot select:

    root path
    input paths
    output paths
    semantic IDs
    prompts
    labels
    pair candidates
    attention identities
    thresholds
    model
    effort
    tool allowlist

Preparation fails closed if the fixed B root exists in an unexpected or semantically advanced state.

Key A storage is never mounted into a Key B semantic job.

## 4. Frozen input staging

Preparation copies only exact public-frozen R2 assets whose bytes are already bound by Research 332:

    KEY_AUTHOR_INSTRUCTIONS.md
    key_author_schema.json
    packets/state.json
    public_fixtures/state_rules.json
    packets/birth_development_classification_sessions.json
    packets/birth_heldout_classification_sessions.json
    packets/key_author_birth_development.json
    packets/key_author_birth_heldout.json
    packets/birth_development_attention_provenance.json
    packets/birth_heldout_attention_provenance.json
    packets/key_author_packet_manifest.json
    public_freeze_commitment.json
    public_freeze_manifest.json

Every staged byte sequence must match the Research 332 frozen SHA-256 and byte length before preparation passes.

Attention-provenance mappings are mechanical-only inputs. They are never placed in semantic prompts.

## 5. Strong semantic-process isolation

Every semantic judgment is performed by a fresh local Claude Code process with:

    model = claude-opus-5-5
    effort = high
    --print
    --safe-mode
    --restricted
    --no-chrome
    --strict-mcp-config
    empty MCP configuration
    --tools ""
    --permission-mode dontAsk
    --permission-prompts none
    --no-session-persistence
    unique --session-id

No semantic job uses:

    --resume
    --continue
    --add-dir
    Bash
    PowerShell
    REPL
    WebSearch
    WebFetch
    GitHub
    MCP
    Agent/subagent tools
    file Read/Write/Edit/Glob/Grep tools

The exact current bounded semantic input is supplied by stdin.

This is intentionally stronger than merely placing B in a sibling folder: the semantic process receives no filesystem tool at all and therefore cannot inspect Key A storage, repository files, local memory files, prior transcripts, or unrelated machine content.

The Runtime Bridge records the exact prompt hash, structured-output bytes/hash, process metadata and fresh session UUID in the private B provenance.

## 6. Phase B1: STATE

B1 receives exactly:

    frozen Key Author instructions
    frozen STATE packet
    frozen public STATE rules
    phase-specific output contract

It derives all 24 STATE fixtures independently.

Output fields remain exactly:

    fixture_id
    valid_fact_ids
    invalid_fact_ids
    expected_state
    reason

Mechanical postflight verifies:

    exact fixture set
    no duplicates
    valid/invalid fact IDs are complete and disjoint
    every fact belongs to the fixture
    expected_state is in the frozen state enum
    output schema is exact

Accepted B1 bytes freeze permanently.

## 7. Phase B2: BIRTH classification

BIRTH classification uses the exact 15 frozen batches:

    development = 2
    held-out = 13

Each batch runs in a fresh Claude Code process.

Each process receives only:

    common frozen instructions
    append-only Key B precedent text accepted before the job
    current frozen classification batch
    current packet-event context

It does not receive:

    prior batch output
    future batch input
    attention provenance
    grouping input
    STATE output
    Key A material

Each presentation receives exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required
    restated
    decision_time_delta
    ambiguity

A batch is accepted only after exact-schema/ID/count validation and private output/transcript hashing.

No next batch is started before the current batch is accepted.

## 8. Append-only precedent mechanism

The semantic output contract may include a private bounded list of reusable semantic precedents proposed by the current author.

A precedent is accepted only with the current semantic artifact and is then appended to the Key B precedent record.

The precedent record:

    belongs only to Key B
    never contains Key A material
    never exposes hidden attention identity
    is append-only
    is available to later Key B classification/grouping jobs
    is not part of public status

A job cannot inspect prior raw semantic artifacts merely because it receives the accepted precedent record.

## 9. BIRTH attention-quality gate

Only after all 15 BIRTH classification batches are frozen, the mechanical control plane joins Key B's own frozen presentation labels to the frozen attention-provenance mappings.

Frozen thresholds remain:

    binary normative consistency >= 0.95
    normative-kind consistency >= 0.90
        on duplicate pairs where the primary is normative

The semantic author never sees duplicate identities.

If the gate passes:

    proceed to BIRTH grouping

If it fails:

    stop before grouping
    preserve the failed Key B attempt
    expose only QUALITY_REPLACEMENT_REQUIRED
    do not repair labels
    do not selectively rerun batches

Research 330's one preregistered quality replacement per slot remains available only through a separately governed fresh replacement attempt.

## 10. Phase B3: BIRTH grouping

Grouping begins only after the Key B attention gate passes.

There are exactly 13 event jobs:

    2 development
    11 held-out

Each grouping event runs in a fresh Claude Code process.

The mechanical control plane derives the Research 367 eligibility projection from:

    Key B's own frozen primary BIRTH classifications
    Key B's own frozen attention provenance mapping
    current event unique-item catalog

The semantic process receives only:

    current event semantic context
    sorted eligible_item_ids
    accepted Key B precedents
    grouping rules

It never receives:

    Key A eligibility
    Key A classifications
    Key A grouping
    Key A attention mapping
    Key B underlying presentation-level classification artifact
    attention duplicate identities

Each pair still requires independent semantic confirmation.

Absence of a pair means UNCONSTRAINED.

No padding is allowed.

## 11. BIRTH grouping floor

After all 11 held-out grouping events freeze, the mechanical gate checks:

    held-out MUST_JOIN pairs >= 15
    held-out total constrained pairs >= 30

Counts remain private during execution.

If either floor fails:

    Key B BIRTH grouping = INCONCLUSIVE
    stop before component commitment
    no retry-to-floor
    no pair padding
    no selective grouping rerun

If both pass:

    BIRTH grouping qualifies for component assembly.

## 12. Component-scoped Key B commitment

After:

    B1 STATE PASS
    all 15 BIRTH classification batches accepted
    BIRTH attention gate PASS
    all 13 BIRTH grouping events accepted
    BIRTH grouping floor PASS

the control plane may mechanically assemble the Key B component bundle.

It uses the same accepted canonical serialization family as P7:

    AO10-DRP03-R2-V03-COMPONENT-BUNDLE-V01-CANONICAL-JSON

Included components:

    BIRTH
    STATE

Excluded component:

    LEGACY = INCONCLUSIVE
    reason = HISTORICAL_R2_LEGACY_CONSTRUCT_VALIDITY_NOT_ESTABLISHED
    p6c_run = false

The Key B commitment is frozen before any A/B comparison.

## 13. Automation and stop semantics

The control plane is sequential and single-author.

The intended purpose-specific actions are:

    status
    prepare
    authorize_phase
    run_until_boundary
    resume_after_hold
    finalize_component

`run_until_boundary` starts or continues an automated sequential runner and returns without exposing semantic output.

It stops on:

    semantic process failure
    schema failure
    transcript/provenance failure
    unexpected input drift
    artifact-write failure
    attention quality failure
    grouping floor failure
    isolation invariant failure
    component-completion boundary

For technical/attempt HOLDs:

    preserve accepted prefix
    preserve failed attempt
    require governed disposition
    any replacement job uses a fresh Claude process
    no automatic retry-to-green

## 14. Public-safe status surface

The task owner may see only bounded mechanical information such as:

    prepared true/false
    authorized true/false
    current phase
    runner RUNNING/HOLD/COMPLETE/IDLE
    STATE accepted true/false
    accepted classification batch count
    attention gate PASS/FAIL/NOT_RUN
    accepted grouping event count
    grouping floor PASS/FAIL/NOT_RUN
    commitment frozen true/false
    error code
    hiddenSemanticDetailsExposed = false

The surface must not expose:

    semantic labels
    normative-kind counts
    material counts
    realization-required counts
    precedent text
    eligible IDs/counts
    grouping pairs/reasons/counts during execution
    attention identities
    STATE outputs
    private semantic transcripts

## 15. Authorization interpretation

Research 421 is the owner's accepted protocol amendment.

It authorizes:

    clean Key B control-plane preparation
    implementation
    mechanical qualification

and holds semantic execution only until those controls qualify.

Therefore successful qualification does not itself start Key B semantics. A separate task-owner `authorize_phase` operation is still required.

No additional protocol amendment or semantic owner vote is required merely because the already-accepted Research 421 precondition has been satisfied.

## 16. Qualification requirements

Before live Key B semantic execution:

    P8 unit/regression suite PASS
    exact frozen-public-input verification PASS
    clean-root preparation regression PASS
    no-Key-A-input regression PASS
    zero-semantic-tool invocation regression PASS
    stdin prompt transport regression PASS
    unique-session / no-resume / no-continue regression PASS
    STATE schema validator PASS
    15-batch sequential classifier state machine PASS
    hidden attention gate PASS on synthetic fixture
    quality-failure stop path PASS
    Key-B-own eligibility projection PASS
    13-event grouping state machine PASS
    grouping-floor failure stop path PASS
    component-bundle canonicalization PASS
    frozen-artifact drift detection PASS
    P7/P6/P5/P4 regressions PASS
    public surface registration PASS
    bounded Git regressions PASS
    runtime release regressions PASS
    managed publish/restart/verify PASS
    mismatchCount = 0

A live non-semantic Claude smoke must additionally confirm the selected CLI accepts the frozen hardening flags and structured stdin flow before semantic activation.

## 17. Current boundary

    KEY_A_COMPONENT_COMMITMENT = FROZEN
    KEY_A_HIDDEN_DETAILS_EXPOSED = false

    KEY_B_CONTROL_PLANE_DESIGN = FROZEN
    KEY_B_CONTROL_PLANE_IMPLEMENTATION = AUTHORIZED
    KEY_B_CONTROL_PLANE_QUALIFICATION = AUTHORIZED
    KEY_B_SEMANTIC_EXECUTION = NOT_STARTED

    CONSTRUCT_COMPARISON = NOT_STARTED

    NEXT = IMPLEMENT_AND_QUALIFY_P8_KEY_B_CONTROL_PLANE
