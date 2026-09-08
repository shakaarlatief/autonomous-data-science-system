# Checkpoint 375: GitHub Native Schema Capture Batch 2 Preserved

**Date:** 2026-09-08
**Status:** PASS / 30 OF 89 NATIVE CONTRACTS CAPTURED / PAGINATION ASYMMETRY + TREE GENERICIZATION PRESERVED / BATCH 3 NEXT
**Checkpoint class:** RESEARCH EVIDENCE + PREIMPLEMENTATION SCHEMA-CAPTURE BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve projected GitHub actions 16-30 from the fixed 89-action conversation, update the machine schema evidence to 30/89, and retain newly exposed transport, pagination, host-scope and genericization constraints without beginning implementation.
**Authority:** Validation 132 owns Batch 2 evidence; `docs/research/github_connector_native_schema_capture.json` owns the cumulative 30-action machine capture.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Schema capture reaches 30 / 89

The same fixed GitHub-only discovery conversation captured projected ordinals 16-30 with zero GitHub action invocations.

```text
captured contracts          30 / 89
completed batches           1, 2
GitHub actions invoked       0
implementation              NOT STARTED
```

## 2. Important new parity constraints

Batch 2 adds four material design facts.

First, `GitHub.create_tree` exposes `tree_elements` only as `{ [key: string]: any }[]`; exact inner tree-entry schema is not recoverable from this host projection and must remain an evidence gap.

Second, `GitHub.download_user_content` is a narrowly host-bound semantic download action for `https://private-user-images.githubusercontent.com` attachments. This refines the HTTP-authority rule: bounded semantic URL inputs are valid when server-enforced by the exact action contract; arbitrary HTTP authority remains forbidden.

Third, `GitHub.download_workflow_artifact` explicitly follows GitHub's temporary redirect and returns a reusable file reference for ZIP bytes, reinforcing the selected Runtime Bridge file/resource-handoff reuse pattern.

Fourth, pagination is explicitly non-uniform: commit workflow runs are first-page-only, issue comments are internally all-pages, and PR-comments pagination is unspecified.

## 3. Generic fetch remains bounded

The native `fetch(url)` action is broad but not a general HTTP escape hatch. It is described as GET-only over approved GitHub repository resource families, allowlists GitHub public hosts, rejects unlisted/sensitive endpoint families and non-public-GitHub hosts, applies connection repository permissions, returns JSON unchanged, and rejects oversized/non-UTF-8 or binary results.

The parity implementation must reproduce that bounded semantic behavior rather than exposing caller-selected methods, arbitrary hosts, headers or credentials.

## 4. Enterprise-host scope becomes an explicit follow-up

`fetch_issue.repository_url` explicitly documents GitHub Enterprise Server custom hostnames and GHE.com API hosts as valid repository selectors. That evidence does not by itself prove every native action supports Enterprise hosts, and it does not invalidate the selected dedicated GitHub App architecture. It does create an explicit Research 123 scope question: final parity architecture must determine how this endpoint-specific Enterprise selector behavior is preserved instead of assuming github.com-only semantics everywhere.

## 5. Current machine boundary

```text
docs/research/github_connector_native_schema_capture.json
    status           PARTIAL_30_OF_89
    capturedCount    30
    nextOrdinal      31

scripts/check_github_connector_schema_capture.py
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=30_OF_89
```

## 6. Exact continuation

Continue the same discovery-only GitHub conversation with projected ordinals 31-45. No GitHub action should be invoked.

```text
CHECKPOINT375=GITHUB_NATIVE_SCHEMA_BATCH2_PRESERVED
SCHEMA_CAPTURE=30_OF_89
BATCH2=PASS
ACTIONS_INVOKED=0
CREATE_TREE_INNER_SCHEMA=GENERICIZED
PAGINATION_POLICY=ACTION_SPECIFIC_CONFIRMED
BOUNDED_FETCH_NOT_ARBITRARY_HTTP=CONFIRMED
ENTERPRISE_SELECTOR_SCOPE=FOLLOWUP_REQUIRED
IMPLEMENTATION=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=GITHUB_SCHEMA_CAPTURE_BATCH_3
```
