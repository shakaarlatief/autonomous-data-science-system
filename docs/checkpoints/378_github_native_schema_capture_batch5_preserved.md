# Checkpoint 378: GitHub Native Schema Capture Batch 5 Preserved

**Date:** 2026-09-08
**Status:** PASS / 75 OF 89 NATIVE CONTRACTS CAPTURED / MERGE CONCURRENCY + CURSOR SEARCH PRESERVED / FINAL BATCH NEXT
**Checkpoint class:** RESEARCH EVIDENCE + PREIMPLEMENTATION SCHEMA-CAPTURE BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve projected GitHub actions 61-75 from the fixed 89-action conversation, advance cumulative native schema evidence to 75/89, and retain PR merge/reviewer, review-thread, Actions rerun and search semantics without beginning implementation.
**Authority:** Validation 135 owns Batch 5 evidence; `docs/research/github_connector_native_schema_capture.json` owns the cumulative 75-action machine capture.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Schema capture reaches 75 / 89

The same fixed GitHub-only discovery conversation captured projected ordinals 61-75 with zero GitHub action invocations.

```text
captured contracts          75 / 89
completed batches           1, 2, 3, 4, 5
GitHub actions invoked       0
implementation              NOT STARTED
```

Only fourteen native action contracts remain before final reconciliation.

## 2. Merge parity now has its exact concurrency guard

`merge_pull_request` exposes `merge | squash | rebase` and optional `expected_head_sha`. The description explicitly states that GitHub rejects the merge if the PR head moved when the expected SHA is supplied.

This is now direct native evidence for a fail-closed Runtime Bridge merge contract rather than merely an architecture preference.

The result is semantically described as GitHub's `sha`, `merged`, `message` merge payload, although field types remain unprojected.

## 3. Reviewer and review-thread mutations retain exact constraints

Reviewer request/removal actions support both individual usernames and team slugs, but the projection does not require at least one array or expose array-size limits.

`reply_to_review_comment` explicitly requires the top-level inline review comment ID and rejects the replies-to-replies model at the API-contract level.

`resolve_review_thread` addresses the thread by GraphQL node ID.

## 4. Actions reruns are permission-sensitive mutations

Both exposed rerun actions require GitHub Actions write permission. The native surface remains intentionally limited to rerunning failed jobs in a run or one specific job; Batch 5 exposes no full-workflow rerun action.

## 5. Search has two different continuation models

`search` is a final-`topn` code/file search with no projected continuation interface. Empty query is explicitly a valid no-results case.

`search_branches` is cursor-based, with an opaque prior-search cursor and `page_size=20`. Its `any` result hides the field containing the next cursor.

This adds another concrete example of why the parity layer cannot normalize every search/list action to one paging API.

## 6. Current machine boundary

```text
docs/research/github_connector_native_schema_capture.json
    status           PARTIAL_75_OF_89
    capturedCount    75
    nextOrdinal      76

scripts/check_github_connector_schema_capture.py
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=75_OF_89
```

## 7. Exact continuation

Continue the same discovery-only GitHub conversation with projected ordinals 76-89. No GitHub action should be invoked.

After Batch 6, perform the already-defined final 89-action discovery reconciliation before any Runtime Bridge GitHub implementation starts.

```text
CHECKPOINT378=GITHUB_NATIVE_SCHEMA_BATCH5_PRESERVED
SCHEMA_CAPTURE=75_OF_89
BATCH5=PASS
ACTIONS_INVOKED=0
MERGE_CONCURRENCY_GUARD=CAPTURED
ACTIONS_RERUN_PERMISSION=CAPTURED
BRANCH_SEARCH_CURSOR=CAPTURED
REMAINING_NATIVE_ACTIONS=14
IMPLEMENTATION=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=GITHUB_SCHEMA_CAPTURE_BATCH_6
```
