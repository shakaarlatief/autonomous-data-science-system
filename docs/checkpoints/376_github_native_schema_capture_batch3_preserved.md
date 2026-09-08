# Checkpoint 376: GitHub Native Schema Capture Batch 3 Preserved

**Date:** 2026-09-08
**Status:** PASS / 45 OF 89 NATIVE CONTRACTS CAPTURED / VALID-EMPTY + 404 + ACTIONS PAGINATION SEMANTICS PRESERVED / BATCH 4 NEXT
**Checkpoint class:** RESEARCH EVIDENCE + PREIMPLEMENTATION SCHEMA-CAPTURE BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve projected GitHub actions 31-45 from the fixed 89-action conversation, advance cumulative native schema evidence to 45/89, and retain newly exposed error, pagination, attempt, PR metadata/diff, identity and collaborator-permission semantics without beginning implementation.
**Authority:** Validation 133 owns Batch 3 evidence; `docs/research/github_connector_native_schema_capture.json` owns the cumulative 45-action machine capture.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Schema capture reaches 45 / 89

The same fixed GitHub-only discovery conversation captured projected ordinals 31-45 with zero GitHub action invocations.

```text
captured contracts          45 / 89
completed batches           1, 2, 3
GitHub actions invoked       0
implementation              NOT STARTED
```

## 2. Valid-empty and not-found semantics are now concrete

`fetch_pr_file_patch` establishes a useful native distinction:

```text
valid PR + path not in changed files -> patch=null
repository / PR unresolved           -> 404
404 retry behavior                    -> do not retry alternative paths
```

This is direct evidence for preserving valid-empty versus not-found and for avoiding blind retry behavior in the Runtime Bridge parity layer.

## 3. Pagination and Actions semantics become richer

Batch 3 adds:

```text
fetch_pr_patch                  all changed-file pages
fetch_workflow_run_artifacts    first page only
fetch_workflow_run_jobs         latest attempt + first page only
reaction readers                explicit page + per_page
```

Workflow job logs follow a redirect and decode bytes; workflow job steps return step summaries only. These are distinct semantic read contracts, not one generic Actions response.

## 4. PR metadata and code changes are deliberately separated

`get_pr_info` includes title/description/refs/status and explicitly excludes code changes. `get_pr_diff` exposes `diff | patch` with default `diff`, while `fetch_pr_patch` is the all-pages patch retrieval path.

## 5. Repository and permission evidence

`get_profile` is zero-argument. `get_repo` repeats the exact-one selector contract and Enterprise/GHE.com repository URL support examples. `get_repo_collaborator_permission` does not expose its returned permission values or enum, so those values remain an output-shape evidence gap rather than inferred connector behavior.

## 6. Current machine boundary

```text
docs/research/github_connector_native_schema_capture.json
    status           PARTIAL_45_OF_89
    capturedCount    45
    nextOrdinal      46

scripts/check_github_connector_schema_capture.py
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
    GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=45_OF_89
```

## 7. Exact continuation

Continue the same discovery-only GitHub conversation with projected ordinals 46-60. No GitHub action should be invoked.

```text
CHECKPOINT376=GITHUB_NATIVE_SCHEMA_BATCH3_PRESERVED
SCHEMA_CAPTURE=45_OF_89
BATCH3=PASS
ACTIONS_INVOKED=0
VALID_EMPTY_VS_NOT_FOUND=EXPLICIT
NO_BLIND_RETRY_CONTRACT=EXPLICIT
PAGINATION_POLICY=ACTION_SPECIFIC_CONFIRMED
PERMISSION_RESULT_ENUM=NOT_PROJECTED
IMPLEMENTATION=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=GITHUB_SCHEMA_CAPTURE_BATCH_4
```
