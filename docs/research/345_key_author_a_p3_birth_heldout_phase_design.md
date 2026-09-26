# Research 345: Key Author A P3 BIRTH Held-Out Classification Phase Design and Authorization Boundary

**Date:** 2026-09-26
**Status:** P3 PHASE DEFINED / BIRTH HELD-OUT CLASSIFICATION ONLY / 13 SEQUENTIAL BATCHES / FRESH CLAUDE SESSION REQUIRED / OWNER AUTHORIZATION REQUIRED
**Parent:** Research 344
**Scope:** Prospectively define the next Key Author A semantic phase after P2 BIRTH development PASS, preserve held-out independence from development-label context, freeze the 13-batch sequential-exposure plan, and return to an explicit owner authorization boundary before any held-out semantic label is created.
**Authority:** Operational phase design only. This record does not authorize P3 or any later semantic phase and does not modify the Research 332 public R2 V0.3 freeze or Research 334 execution addendum.

## 1. Why P3 is BIRTH held-out classification

Research 332 freezes BIRTH as:

    development
        2 events
        455 semantic items
        2 classification batches
        469 presentations

    held-out reviewer surface
        11 opaque packet events
        2254 semantic items
        13 classification batches
        2347 presentations

P2 completed the development classification surface.

The next coherent phase is therefore:

    P3 = BIRTH HELD-OUT CLASSIFICATION

P3 does not include:

    BIRTH grouping
    attention-consistency reconciliation
    LEGACY
    canonical Key A assembly
    commitment generation

The unique BIRTH grouping catalog remains hidden until every BIRTH classification batch, including all 13 held-out batches, is frozen.

## 2. Fresh-session requirement

P3 must begin in a new Claude Code session.

The P2 session may not be continued or resumed for P3.

Reason:

    P2's conversation context contains development presentation-level labels.

The held-out surface may reuse or duplicate semantic content for attention control. Allowing the P2 conversational state into P3 would expose exact development-label memory beyond the intended append-only precedent mechanism.

Therefore the only semantic carry-forward from P2 into P3 is:

    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if nonempty
    frozen instructions/schema/addendum

The six P2 precedents are intentionally available.

The P2 batch artifacts and P2 transcript are not.

A fresh P3 session preserves the same logical Key Author A while preventing development-label conversational carry-over.

Launch must therefore use a new local Claude Code session with no:

    --continue
    --resume

## 3. Frozen held-out sources

Classification-session source:

    inputs/r2_v03/packets/birth_heldout_classification_sessions.json

Frozen SHA-256:

    26fda821df686cc002041b1d8ff3a83778a647db09580bdb2479f86cad67595d

Frozen bytes:

    1152118

Frozen total lines:

    23584

Key-author held-out event context:

    inputs/r2_v03/packets/key_author_birth_heldout.json

Frozen SHA-256:

    a81db255411cbda5729eded44f4dc6872fd3d460b3be3ede7f845ac445b01116

Frozen bytes:

    1168175

Frozen total lines:

    20696

No held-out grouping catalog or attention-provenance mapping is exposed during P3.

## 4. Semantic-item versus presentation count

The held-out surface contains:

    2254 unique semantic items
    2347 classification presentations

The difference is intentional.

Research 332 freezes deterministic attention-check duplicates through a separate provenance mapping. Those duplicates are excluded from semantic truth and the mapping remains hidden during classification.

Therefore the semantic executor sees and labels:

    2347 presentations

but must not know which presentations map to repeated semantic items.

The author must not infer or enforce duplicate consistency through:

    repeated text
    text hashes
    presentation similarity
    remembered labels

Attention consistency is evaluated later, after all classification batches are frozen.

## 5. P3 batch plan

The frozen held-out classification sequence is:

| # | Batch ID | Packet event | Part | Presentations | Classification lines | Event-context lines |
|---:|---|---|---:|---:|---|---|
| 1 | BAT-373ed51c1abb | EVP-1b6edca704fa | 1 | 20 | 1-217 | 1-157 |
| 2 | BAT-d9a702f46dee | EVP-1b53b3b00c6c | 1 | 223 | 218-2455 | 158-2138 |
| 3 | BAT-145d2d76772f | EVP-819a9953b12b | 1 | 383 | 2456-6293 | 2139-5519 |
| 4 | BAT-5b6b88a6e3c6 | EVP-d8bfe7b48f85 | 1 | 70 | 6294-7001 | 5520-6141 |
| 5 | BAT-ba93d18c7368 | EVP-ba08dc62e616 | 1 | 68 | 7002-7689 | 6142-6745 |
| 6 | BAT-63443a6cadb8 | EVP-dca0fcb4fb4d | 1 | 129 | 7690-8987 | 6746-7898 |
| 7 | BAT-9b3c5b51818c | EVP-838a4c21407b | 1 | 129 | 8988-10285 | 7899-9066 |
| 8 | BAT-7dc61c90a939 | EVP-3ad3b2e576e0 | 1 | 129 | 10286-11583 | 9067-10219 |
| 9 | BAT-903fa5c8a8e6 | EVP-ffd3c3f9f874 | 1 | 392 | 11584-15511 | 10220-14185 |
| 10 | BAT-ece1bc9728dc | EVP-ffd3c3f9f874 | 2 | 61 | 15512-16129 | already exposed for batch 9 |
| 11 | BAT-89df08a20c3b | EVP-e9498b2ad950 | 1 | 25 | 16130-16387 | 14186-14379 |
| 12 | BAT-20aa129a94ca | EVP-63516d4b5c63 | 1 | 392 | 16388-20315 | 14380-20696 |
| 13 | BAT-3ab72b275f68 | EVP-63516d4b5c63 | 2 | 326 | 20316-23584 | already exposed for batch 12 |

Total:

    13 batches
    2347 presentations

No batch exceeds the frozen 400-presentation maximum.

## 6. Event-context rule for split events

Two held-out packet events span two classification batches:

    EVP-ffd3c3f9f874
        batch 9
        batch 10

    EVP-63516d4b5c63
        batch 12
        batch 13

The event context is indivisible and is exposed when the first batch for that event begins.

Therefore:

    batch 9
        may read event-context lines 10220-14185

    batch 10
        receives no new event-context exposure

    batch 12
        may read event-context lines 14380-20696

    batch 13
        receives no new event-context exposure

If the same P3 Claude session continues across the split-event boundary, it should rely on already-visible event context rather than rereading it.

If a fresh sequential P3 session is required at batch 10 or batch 13, rereading the already-authorized same-event context is permitted because that context was exposed before the prior part was frozen. The classification-session range for the new part remains strictly gated.

## 7. Sequential-exposure invariant

For every batch:

    expose current classification range only
    expose current event context only when first entering that event
    classify every presentation
    write the current private batch artifact
    freeze the artifact
    STOP
    task owner mechanically reviews artifact and transcript
    only then release the next batch

No later classification range may be read before the current batch is accepted.

A P3 owner authorization covers all 13 prospectively defined batches.

It does not eliminate the 12 intermediate task-owner continuation gates.

No additional human authorization is required between P3 batches after P3 itself is explicitly authorized.

## 8. Allowed common sources

Every P3 session may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if needed

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

The six P2 append-only precedents are valid carry-forward semantic guidance.

P3 must not read:

    out/P1_STATE_EXPECTED_OUTPUTS.json
    work/P1_STATE_RULE_TRACE.md
    out/birth_development/**
    P2 Claude transcript
    inputs/research330/**
    BIRTH grouping packets
    attention-provenance mappings
    LEGACY files
    repository checkouts
    other-key material
    unrelated workspace files

## 9. P3 semantic output

Each held-out presentation receives exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required
    restated
    decision_time_delta
    ambiguity

with the frozen meanings from the Key Author instructions, schema, CODEBOOK and append-only precedents.

Each batch is written separately:

    out/birth_heldout/<batch_id>.json

with the same private working shape used in P2, except:

    component
        BIRTH

    split
        heldout

and the exact current batch/event/part metadata.

The P3 batch files are private working artifacts and do not amend the canonical key schema.

## 10. Progress state

Before P3 begins, expected state is:

    current_phase
        P2_BIRTH_DEVELOPMENT_COMPLETE_AWAITING_REVIEW

    p2_authorized
        true

    frozen_batches
        includes both P2 development batches

    open_batch
        null

Once P3 is explicitly authorized, the fresh P3 session records:

    p3_authorized
        true

Before each batch:

    current_phase
        P3_BIRTH_HELDOUT_BATCH_<NN>_IN_PROGRESS

    open_batch
        current batch ID

After each batch freezes:

    append current batch ID to frozen_batches

    open_batch
        null

    current_phase
        P3_BIRTH_HELDOUT_BATCH_<NN>_COMPLETE_AWAITING_REVIEW

After the thirteenth batch freezes:

    current_phase
        P3_BIRTH_HELDOUT_COMPLETE_AWAITING_REVIEW

P4 or later authorization must not be introduced during P3.

## 11. Compaction and sequential-session rule

P3 is substantially larger than P2.

Because 2347 presentations are spread across 13 gated batches, a single Claude Code context may become large.

Research 334 already permits sequential local sessions for the same logical Key Author A if model, frozen inputs, addendum, codebook and append-only precedents remain unchanged.

Therefore:

    continuation in same session
        permitted between accepted batches

    fresh replacement P3 session at a batch boundary
        permitted

    compaction while no batch is open
        task-owner review before continuation

    compaction while a batch is open
        HOLD

    model change
        HOLD

    parallel semantic sessions
        prohibited

    subagent semantic workers
        prohibited

A replacement session must not reread prior frozen semantic batch artifacts.

It reconstructs only from common sources, append-only precedents and the newly released current-batch source/context.

## 12. Shell and external-tool boundary

P3 semantic classification requires no shell.

Therefore P3 prohibits:

    Bash
    PowerShell
    Git
    Python
    terminal execution
    repository queries
    external process execution
    WebSearch
    WebFetch
    GitHub
    MCP
    IDE tools

Task-owner postflight performs hashing and mechanical validation after each stop.

The qualified environment remains:

    claude-opus-5-5
    effort high
    permissionMode default / INTERACTIVE_APPROVAL
    standalone external terminal
    IDE disconnected
    Chrome disabled
    .claude/settings.local.json absent

## 13. Per-batch return boundary

Each batch returns only a bounded non-secret report containing:

    P3_BATCH_RESULT=PASS|HOLD|FAIL
    BATCH_NUMBER=<1-13>
    SESSION_ID=<id or NOT_EXPOSED>
    MODEL=<exact model>
    EFFORT=<exact effort>
    PERMISSION_MODE=<exact mode>
    EXTERNAL_TERMINAL=PASS|FAIL
    IDE_CONTEXT_ABSENT=PASS|FAIL
    MCP_DISABLED=PASS|FAIL
    WEB_DENIED=PASS|FAIL
    LOCAL_SETTINGS_ABSENT=PASS|FAIL
    BATCH_ID=<current batch>
    PRESENTATIONS_EXPECTED=<count>
    PRESENTATIONS_COMPLETED=<count>
    OUTPUT_PATH=<private relative path>
    OUTPUT_SCHEMA_COMPLETE=PASS|FAIL
    PRECEDENTS_ADDED_THIS_BATCH=<count>
    ERRATA_ADDED_THIS_BATCH=<count>
    BATCH_FROZEN=true|false
    NEXT_BATCH_EXPOSED=false
    SHELL_USED=false
    GROUPING_STARTED=false
    LEGACY_STARTED=false
    P3_COMPLETE=true|false

The executor must not return:

    presentation labels
    semantic category counts
    attention identities
    semantic precedents
    semantic excerpts
    grouping information

The human owner must paste only the bounded final report to ChatGPT, not Claude Code tool previews.

## 14. Completion boundary

P3 passes only after all 13 held-out batch artifacts have separately passed task-owner mechanical and transcript review.

Only then is:

    all BIRTH classification
        frozen

At that point the unique BIRTH grouping catalog becomes eligible for a separately defined later phase.

P3 itself must not expose or execute grouping.

## 15. Authorization boundary

This research defines P3 before any held-out Key Author A semantic label exists.

Current state:

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS

    P3_SCOPE=BIRTH_HELDOUT_CLASSIFICATION
    P3_BATCH_COUNT=13
    P3_PRESENTATION_COUNT=2347
    P3_UNIQUE_SEMANTIC_ITEM_COUNT=2254
    P3_SEQUENTIAL_EXPOSURE_PLAN=FROZEN
    P3_FRESH_SESSION_REQUIRED=true

    P3_READY=true
    P3_AUTHORIZED=false

    BIRTH_HELDOUT_LABELS=NONE
    BIRTH_GROUPING=NOT_STARTED
    LEGACY_LABELS=NONE
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_P3_AUTHORIZATION_DECISION
