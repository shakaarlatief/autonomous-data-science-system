# Research 341: Key Author A P2 BIRTH Development Classification Phase Design and Authorization Boundary

**Date:** 2026-09-26
**Status:** P2 PHASE DEFINED / BIRTH DEVELOPMENT CLASSIFICATION ONLY / SEQUENTIAL BATCH EXPOSURE FROZEN / OWNER AUTHORIZATION REQUIRED / NO P2 SEMANTIC WORK STARTED
**Parent:** Research 340
**Scope:** Define the exact next Key Author A semantic phase after P1 STATE PASS, preserve the frozen batch-exposure rule without exposing future BIRTH batches prematurely, specify private working-output structure and task-owner review points, and return to an explicit owner authorization boundary.
**Authority:** Operational phase design only. This record does not authorize P2 or any later semantic phase and does not modify the Research 332 public R2 V0.3 freeze or Research 334 execution addendum.

## 1. Why the next phase is BIRTH development classification

The frozen protocol has three semantic components:

    BIRTH
    LEGACY
    STATE

P1 completed STATE.

For BIRTH and LEGACY, the Research 334 execution addendum binds the already-frozen classification-session files as the deterministic batching and attention-control realization.

The frozen delivery rule is:

    freeze each batch annotation before exposing the next batch

and:

    expose grouping only after all classification batches for that component are frozen

The smallest coherent next phase is therefore:

    P2 = BIRTH DEVELOPMENT CLASSIFICATION

Development is processed before held-out BIRTH classification so the exposed/non-fresh Key Author A can establish any genuinely reusable append-only semantic precedents on the development surface before held-out work.

P2 does not include:

    BIRTH held-out classification
    any BIRTH grouping
    LEGACY
    canonical Key A assembly
    commitment generation

## 2. Frozen P2 workload

Frozen classification source:

    inputs/r2_v03/packets/birth_development_classification_sessions.json

Public-freeze SHA-256:

    c4cae66b7874e2e4459818b17508d5c5bca83d2c593ee07b2069cc9844a31363

Public-freeze bytes:

    227465

Frozen key-author BIRTH context:

    inputs/r2_v03/packets/key_author_birth_development.json

Public-freeze SHA-256:

    0bb1ba499e935b3bdfe7613c1e0c2e50d827072c6b116d672104334c5024af6e

Public-freeze bytes:

    221599

P2 contains exactly two batches:

    batch 1
        batch_id = BAT-2d0805e6c619
        packet_event_id = EVP-ca475c9a5a9d
        part_index = 1
        presentations = 205

    batch 2
        batch_id = BAT-904613dd8a4e
        packet_event_id = EVP-362b09ec98e9
        part_index = 1
        presentations = 264

Total development presentations:

    469

No grouping catalog is exposed during P2.

## 3. Sequential exposure guard

The frozen classification-session file and key-author packet each contain both P2 batches/events.

Reading either entire file before batch 1 freezes would violate the operational intent of:

    freeze each batch annotation before exposing the next batch

Therefore P2 freezes a line-bounded read plan against the exact frozen bytes.

Classification-session file:

    total lines
        4716

    batch 1 exposure
        lines 1-2067 only

    batch 2 begins
        line 2068

    batch 2 exposure
        lines 2068-4716 only
        and only after task-owner acceptance of frozen batch 1

Key-author development packet:

    total lines
        4168

    event 1 exposure
        lines 1-1831 only

    event 2 begins
        line 1832

    event 2 exposure
        lines 1832-4168 only
        and only after task-owner acceptance of frozen batch 1

The line boundaries are operational exposure guards derived mechanically from the exact frozen files. They do not change semantic content.

The semantic executor must not use an unrestricted/full-file Read on either multi-batch file during P2.

Task-owner transcript postflight will verify the actual Read offsets/ranges.

## 4. Allowed common P2 sources

Before batch semantic work, the P2 session may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if needed

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

For each batch, only the line-bounded current-batch/current-event portions from section 3 may be added.

P2 must not read:

    P1 STATE semantic output
    P1 STATE private rule trace
    Research 330
    BIRTH held-out classification sessions
    BIRTH held-out key-author packet
    BIRTH grouping packets
    LEGACY packets or classification sessions
    any attention-provenance mapping
    Claude transcripts
    repository checkouts
    other-key material
    unrelated workspace files

## 5. P2 semantic fields

P2 classification is presentation-level because the attention mapping from presentation to canonical semantic item must remain unseen while labeling.

Each presentation receives exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required
    restated
    decision_time_delta
    ambiguity

The semantic meanings of those fields are unchanged from:

    KEY_AUTHOR_INSTRUCTIONS.md
    key_author_schema.json
    work/CODEBOOK.md

The author labels each presentation independently.

The author must not use repeated text, text hashes, presentation similarity, or remembered earlier labels as a mechanism to force duplicate consistency.

Attention consistency is computed only after all BIRTH classification batches are frozen and cannot be used to repair labels.

## 6. Private batch artifact shape

Each frozen P2 batch is written as a separate private file:

    out/birth_development/BAT-2d0805e6c619.json
    out/birth_development/BAT-904613dd8a4e.json

Logical working shape:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "BIRTH",
      "split": "development",
      "batch_id": "...",
      "packet_event_id": "...",
      "part_index": 1,
      "presentations": [
        {
          "presentation_id": "...",
          "normative": true | false,
          "normative_kind": "OBLIGATION" | "CONSTRAINT" | "DISPOSITION" | "SEQUENCING" | "PRINCIPLE" | null,
          "material": true | false,
          "realization_required": true | false,
          "restated": true | false,
          "decision_time_delta": true | false,
          "ambiguity": true | false
        }
      ]
    }

This is a private working representation only.

It does not amend the canonical key schema. Later mechanical assembly uses the frozen attention mapping to translate presentation-level frozen classifications into canonical item-level Key Author material.

## 7. Batch 1 stop gate

P2 does not expose batch 2 immediately.

The executor must:

    read only common sources
    read only batch-1 classification lines
    read only event-1 key-author-context lines
    classify all 205 presentations independently
    write the batch-1 private artifact
    mark batch 1 frozen in private progress
    STOP

The executor returns a bounded non-secret batch-1 report.

It must not print:

    any presentation label
    normative-kind counts
    material counts
    realization-required counts
    restated identities/counts
    decision-time-delta identities/counts
    ambiguity identities/counts
    semantic reasons or precedents

The task owner then:

    mechanically checks artifact shape/count/IDs
    computes an opaque private digest
    verifies transcript read boundaries/tool use
    verifies IDE/config isolation
    records the frozen batch in private progress/provenance

Only after that review may the task owner tell the already-authorized P2 session to expose batch 2.

No second human semantic authorization is required if P2 itself has been explicitly authorized, because batch 2 is within the prospectively frozen P2 scope. The task-owner continuation gate remains mandatory.

## 8. Batch 2 and P2 completion

After batch-1 acceptance, the same P2 Claude Code session may continue, or a sequential replacement session may be used under the Research 334 same-logical-author rules.

Batch 2 must then:

    expose only the batch-2/current-event ranges
    classify all 264 presentations
    write the separate batch-2 artifact
    freeze it
    STOP

Task-owner postflight repeats the mechanical and transcript checks.

P2 passes only if both batch artifacts are accepted and frozen.

After P2 PASS:

    BIRTH development classification
        complete

    BIRTH held-out classification
        still not authorized

    BIRTH grouping
        still prohibited because not all BIRTH classification batches are frozen

## 9. Execution configuration

P2 preserves the qualified Key A execution environment:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default / INTERACTIVE_APPROVAL

    terminal
        standalone external Windows Terminal / PowerShell

    IDE attachment
        prohibited

    web / MCP / GitHub
        disabled / denied

    settings.local.json
        absent

    subagents / parallel semantic workers
        prohibited

BIRTH classification needs no shell, Git, Python, web or repository query.

Therefore:

    P2 semantic shell use
        PROHIBITED

If the executor believes a shell command is required:

    STOP / HOLD

Batch hashing and other mechanical validation are performed by the task owner after the semantic executor stops.

## 10. P1 confidentiality carry-forward

P2 must not read or consume the private P1 STATE output.

Therefore P2 cannot be influenced by the limited P1 semantic preview that reached chatgpt-31.

The P1 output remains frozen for later canonical assembly.

The Research 340 exposure restriction remains:

    chatgpt-31
        exposed task-owner, not eligible as fresh decision reviewer

    future Key Author B
        must not receive chatgpt-31 or Key A private materials

## 11. Authorization boundary

This research defines P2 before any P2 semantic label exists.

It does not authorize execution.

Current state:

    P1_STATE=PASS
    P1_STATE_OUTPUT=PRIVATE_FROZEN

    P2_SCOPE=BIRTH_DEVELOPMENT_CLASSIFICATION
    P2_BATCH_COUNT=2
    P2_PRESENTATION_COUNT=469
    P2_SEQUENTIAL_EXPOSURE_PLAN=FROZEN

    P2_READY=true
    P2_AUTHORIZED=false

    BIRTH_HELDOUT_LABELS=NONE
    LEGACY_LABELS=NONE
    GROUPING_PAIRS=NONE
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_P2_AUTHORIZATION_DECISION
