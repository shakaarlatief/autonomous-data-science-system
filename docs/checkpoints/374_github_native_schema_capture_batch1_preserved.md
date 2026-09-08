# Checkpoint 374: GitHub Native Schema Capture Batch 1 Preserved

**Date:** 2026-09-08
**Status:** PASS / 15 OF 89 NATIVE CONTRACTS CAPTURED / OUTPUT-SCHEMA LIMITATION EXPOSED / BATCH 2 NEXT
**Checkpoint class:** RESEARCH EVIDENCE + PREIMPLEMENTATION SCHEMA-CAPTURE BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve projected GitHub action contracts 1-15 from the fixed fresh 89-action conversation and advance the discovery-only schema-capture boundary without implementation.
**Authority:** Validation 131 owns the Batch 1 evidence; `docs/research/github_connector_native_schema_capture.json` owns the machine-readable partial schema capture; the corrected 89-action inventory remains `docs/research/github_connector_89_action_inventory.json`.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Batch 1 is durably captured

The same fresh GitHub-only discovery conversation used at Checkpoint 373 captured exact host-visible contracts for projected actions 1-15 and invoked no GitHub action.

```text
fresh projection            89 actions
captured contracts          15 / 89
captured ordinals           1-15
GitHub actions invoked      0
implementation              NOT STARTED
```

The machine-readable capture and validator both pass.

## 2. Input contracts are substantially exposed

All fifteen actions expose usable object input contracts with required/optional fields. Real enum evidence includes:

```text
add_review_to_pr.action
    COMMENT | APPROVE | REQUEST_CHANGES

create_blob.encoding
    utf-8 | base64
    default utf-8
```

Several cross-field requirements are only described in prose rather than structurally encoded, including the review-body condition, `create_branch` sha/base_ref XOR, and `create_pull_request` title/issue rule. The parity implementation must preserve such descriptive semantics explicitly rather than assuming the projected JSON schema alone is complete.

## 3. Output/error projection is weaker than input projection

Batch 1 establishes a projection-wide limitation important to the parity design:

```text
separate title metadata        not exposed
return type                    any for 15 / 15
machine output schema          not exposed
structured error schema        not exposed
HTTP/error-code mapping        not exposed
retry contract                 not exposed
```

Some action descriptions still promise semantic result forms such as normalized issue/PR snapshots, a compact compare result, or a commit/blob SHA. Those descriptions are evidence, but their exact property schemas are not yet proven.

This does not block continuing schema discovery. It does mean final Research 123 reconciliation must explicitly decide whether additional live-result evidence is required before claiming faithful output-shape parity.

## 4. Current machine boundary

```text
docs/research/github_connector_native_schema_capture.json
    status           PARTIAL_15_OF_89
    capturedCount    15
    nextOrdinal      16

scripts/check_github_connector_schema_capture.py
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=15_OF_89
```

## 5. Exact continuation

Continue in the same fixed GitHub-only conversation with projected ordinals 16-30:

```text
GitHub.create_tree
...
GitHub.fetch_pr_comments
```

This batch contains `GitHub.download_user_content`, whose exact native contract remains especially important because Checkpoint 373 corrected that action into the baseline.

No GitHub action should be invoked.

```text
CHECKPOINT374=GITHUB_NATIVE_SCHEMA_BATCH1_PRESERVED
SCHEMA_CAPTURE=15_OF_89
BATCH1=PASS
ACTIONS_INVOKED=0
OUTPUT_SCHEMA_LIMITATION=OBSERVED
IMPLEMENTATION=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=GITHUB_SCHEMA_CAPTURE_BATCH_2
```
