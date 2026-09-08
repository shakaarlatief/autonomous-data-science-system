# Checkpoint 377: GitHub Native Schema Capture Batch 4 Preserved

**Date:** 2026-09-08
**Status:** PASS / 60 OF 89 NATIVE CONTRACTS CAPTURED / INSTALLATION + OFFSET PAGINATION + LOCK ENUM PRESERVED / BATCH 5 NEXT
**Checkpoint class:** RESEARCH EVIDENCE + PREIMPLEMENTATION SCHEMA-CAPTURE BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve projected GitHub actions 46-60 from the fixed 89-action conversation, advance cumulative native schema evidence to 60/89, and retain newly exposed identity, installation, repository-pagination, review-listing and conversation-lock semantics without beginning implementation.
**Authority:** Validation 134 owns Batch 4 evidence; `docs/research/github_connector_native_schema_capture.json` owns the cumulative 60-action machine capture.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Schema capture reaches 60 / 89

The same fixed GitHub-only discovery conversation captured projected ordinals 46-60 with zero GitHub action invocations.

```text
captured contracts          60 / 89
completed batches           1, 2, 3, 4
GitHub actions invoked       0
implementation              NOT STARTED
```

## 2. Installation-aware discovery is further confirmed

Batch 4 captures `list_installations`, `list_installed_accounts`, and `list_repositories_by_installation` directly. `list_installations` exposes `manageable_only`; `list_installed_accounts` is zero-argument; installation-scoped repository listing requires `installation_id`.

This strengthens the earlier architectural conclusion that faithful parity should be built around a GitHub App/user-token model rather than treating ordinary Git transport credentials as sufficient GitHub API authority.

## 3. Pagination semantics continue to vary per action

Batch 4 confirms:

```text
recent PRs                       internal pagination to final limit
changed PR filenames             all pages internally
recent issues                    until top_k or source exhaustion
repository listing               zero-based offset pagination
repository-by-affiliation        zero-based offset pagination
repository-by-installation       zero-based offset pagination
review threads / reviews         pagination unspecified
organization lists               pagination unspecified
```

The parity layer must reproduce these action contracts rather than normalize them into one invented paging scheme.

## 4. Example strings remain distinct from real enums

The projection names `open`, `closed`, `all` as examples for recent-PR state and `owner`, `collaborator`, `organization_member` as examples for affiliation. Those inputs remain unrestricted strings in the projected schema.

By contrast, `lock_issue_conversation.lock_reason` exposes a real enum of exactly:

```text
off-topic
too heated
resolved
spam
```

This distinction is mechanically preserved.

## 5. Output-schema limitation remains unresolved

Every Batch 4 action still projects return type `any`. Review threads, reviews, repository search-index enrichment, installation/account collections and conversation-lock mutation results therefore remain semantically described but not structurally typed.

This remains a final Research 123 reconciliation question rather than a reason to halt the six-batch input-schema capture.

## 6. Current machine boundary

```text
docs/research/github_connector_native_schema_capture.json
    status           PARTIAL_60_OF_89
    capturedCount    60
    nextOrdinal      61

scripts/check_github_connector_schema_capture.py
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=60_OF_89
```

## 7. Exact continuation

Continue the same discovery-only GitHub conversation with projected ordinals 61-75. No GitHub action should be invoked.

```text
CHECKPOINT377=GITHUB_NATIVE_SCHEMA_BATCH4_PRESERVED
SCHEMA_CAPTURE=60_OF_89
BATCH4=PASS
ACTIONS_INVOKED=0
INSTALLATION_DISCOVERY=CAPTURED
ZERO_BASED_OFFSET_PAGINATION=CAPTURED
REVIEW_PAGINATION=UNSPECIFIED
LOCK_REASON_ENUM=CAPTURED
IMPLEMENTATION=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=GITHUB_SCHEMA_CAPTURE_BATCH_5
```
