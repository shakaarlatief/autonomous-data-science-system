# Validation 131: GitHub Native Schema Capture Batch 1 Preserved

**Date:** 2026-09-08
**Status:** PASS / 15 OF 89 HOST-VISIBLE CONTRACTS PRESERVED / DISCOVERY-ONLY / BATCH 2 NEXT
**Research:** Research 123
**Scope:** Preserve the first projected-order batch of exact native GitHub connector contracts from the already-fixed 89-action fresh GitHub-only conversation, without invoking any GitHub action.

## 1. Qualification conditions

The same fresh GitHub-only conversation used for the Checkpoint 373 exact inventory correction continued in discovery/schema-inspection mode only.

```text
projected GitHub action count      89
schema batch                        1
projected ordinals                  1-15
GitHub actions invoked              0
Browser / web / shell / ADS         not used
```

The batch began with `GitHub.add_comment_to_issue` and ended with `GitHub.create_pull_request`, exactly matching inventory ordinals 1-15.

## 2. Projection-wide host limitations established by Batch 1

All fifteen action contracts expose a host-visible input object schema, but the projection is materially weaker on result/error metadata:

```text
separate action title metadata                 0 / 15 exposed
input object contract                         15 / 15 exposed
projected return type                         any for 15 / 15
machine-readable output schema                0 / 15 exposed
structured error schema                       0 / 15 exposed
error-code enum / HTTP mapping / retry schema 0 / 15 exposed
pagination/cursor/continuation inputs          0 / 15 exposed
```

Where an action description states a semantic result contract, that description is preserved separately instead of inventing a machine-readable output schema.

Conditional validation also appears partly as prose rather than structural schema. The captured examples include:

```text
add_review_to_pr
    review required for COMMENT and REQUEST_CHANGES

create_branch
    exactly one of sha or base_ref

create_pull_request
    title required unless issue is supplied
    head_repo required by GitHub for some same-organization cross-repository PRs
```

No stronger structural rule is inferred where the projection does not expose one.

## 3. Exact enums and defaults observed

The first batch exposes two real enums that must be preserved exactly:

```text
GitHub.add_review_to_pr.action
    COMMENT
    APPROVE
    REQUEST_CHANGES

GitHub.create_blob.encoding
    utf-8
    base64
    default = utf-8
```

Reaction fields in the reaction actions remain plain strings. Values such as `+1` and `eyes` are examples only and are not promoted to enums.

## 4. Important action-specific contracts

The captured contracts preserve, among other details:

```text
GitHub.add_issue_assignees
    additive assignee mutation
    description states endpoint supports up to 10 assignees
    no schema-level maxItems is projected

GitHub.add_issue_labels
    additive label mutation
    explicitly contrasted with replacement semantics of update_issue(labels=...)

GitHub.add_review_to_pr
    optional inline file_comments with required path/body
    optional position/line/side/start_line/start_side
    LEFT/RIGHT are examples, not projected enums
    no structural position-vs-line rule is exposed

GitHub.compare_commits
    descriptive result promises stable compact per-file statistics + compare metadata
    exact output properties/types are not projected

GitHub.create_branch
    sha/base_ref XOR requirement is descriptive

GitHub.create_file
    UTF-8 text creation through contents API
    target path must not already exist
    optional branch must already exist
    result description says commit SHA only

GitHub.create_pull_request
    head_branch/base_branch are compatibility aliases for head/base
    no projected precedence/conflict rule between aliases and canonical fields
    projected schema does not mark head/head_branch/base/base_branch as unconditionally required
```

## 5. Result-shape evidence remains descriptive

The clearest result contracts visible in Batch 1 are:

```text
add_issue_assignees             normalized issue snapshot
add_issue_labels                normalized issue snapshot
compare_commits                 stable compact compare metadata + per-file stats
convert_pull_request_to_draft   normalized PR snapshot
create_blob                     blob SHA
create_file                     resulting commit SHA only
create_issue                    normalized issue snapshot
create_pull_request             normalized PR snapshot
```

The host still projects the return type as `any`, so the exact normalized snapshot property schemas remain unproven by discovery alone. Research 123 must preserve that distinction when later deciding whether additional live-result evidence is needed for practical parity.

## 6. Machine-readable preservation

The new specialized evidence artifact is:

```text
docs/research/github_connector_native_schema_capture.json
```

At this boundary it records:

```text
schemaVersion        1
status               PARTIAL_15_OF_89
capturedCount        15
batchesCompleted     [1]
nextOrdinal          16
```

The corresponding validator is:

```text
scripts/check_github_connector_schema_capture.py
```

It verifies the captured names/order against inventory ordinals 1-15, the fixed 89-action/zero-invocation context, projection-wide title/output/error limitations, the exact `add_review_to_pr.action` enum, and the exact `create_blob.encoding` enum/default.

Observed result:

```text
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=15_OF_89
```

## 7. Exact continuation

The fixed GitHub-only conversation should now capture projected ordinals 16-30, beginning with `GitHub.create_tree` and including the previously unresolved `GitHub.download_user_content` contract.

No GitHub action is to be invoked.

```text
VALIDATION131=PASS
NATIVE_SCHEMA_CAPTURE=15_OF_89
BATCH1=PASS
ACTIONS_INVOKED=0
HOST_OUTPUT_SCHEMA=NOT_PROJECTED
HOST_STRUCTURED_ERROR_SCHEMA=NOT_PROJECTED
IMPLEMENTATION=NOT_STARTED
NEXT=SCHEMA_CAPTURE_BATCH_2_ORDINALS_16_30
```
