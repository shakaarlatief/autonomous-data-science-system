# Validation 130: GitHub Fresh Projection Exact Inventory Correction and Schema Capture Opened

**Date:** 2026-09-08
**Status:** PASS / FRESH 89-ACTION PROJECTION CONFIRMED / CHECKPOINT 372 EXACT-NAME RECONSTRUCTION DEFECT CORRECTED / SCHEMA CAPTURE ACTIVE
**Research:** Research 123
**Scope:** Preserve the discovery-only fresh GitHub projection used to begin native schema capture, reconcile it against the Checkpoint 372 reconstructed action-name inventory, and establish the exact next schema-capture boundary without invoking any GitHub action.

## 1. Fresh projection result

A fresh GitHub-only ChatGPT conversation was opened specifically for the Research 123 native schema-capture qualification. The conversation was instructed to inspect the projected GitHub tool surface only and not invoke any action.

Observed result:

```text
projected GitHub actions   89
GitHub actions invoked      0
reported added actions      0
reported missing actions    0
```

The projected count therefore independently reproduces the two 89-action observations already preserved by Validation 128.

## 2. Exact-name comparison exposed one reconstruction defect

The fresh conversation also returned the exact projected action names in projected order. Comparison against the machine-readable inventory created at Checkpoint 372 found one name-level disagreement while preserving the same total count:

```text
fresh projection only
    GitHub.download_user_content

Checkpoint 372 reconstructed inventory only
    GitHub.add_issue_comment
```

The fresh projection contains:

```text
GitHub.add_comment_to_issue
```

and does not contain `GitHub.add_issue_comment`.

Validation 128 had never reproduced all 89 exact names in its public evidence. Checkpoint 372 therefore reconstructed the names from prior qualification transcripts, and that reconstruction introduced one erroneous action name. Because the fresh projection still contains exactly 89 actions and there is no evidence that Validation 128 ever established `GitHub.add_issue_comment`, the correct classification is:

```text
CHECKPOINT372_EXACT_NAME_RECONSTRUCTION=ONE_ACTION_DEFECT
FRESH_ONLY=GitHub.download_user_content
RECONSTRUCTION_ONLY=GitHub.add_issue_comment
INTERPRETATION=RECONSTRUCTION_DEFECT_NOT_CONNECTOR_DRIFT
```

The historical Checkpoint 372 evidence is not rewritten to hide this error. This validation supersedes only its exact-name reconstruction claim.

## 3. Corrected canonical inventory

`docs/research/github_connector_89_action_inventory.json` is now schema version 2 and preserves the fresh 89-action projection in its exact projected order.

The corrected family counts are:

```text
issues                         17
pull requests / reviews        32
repository / Git               29
content download                1
Actions / CI                    9
repository permission           1
TOTAL                           89
```

`GitHub.download_user_content` is provisionally classified as a read-only content-download action. Its exact input/result/transport semantics remain intentionally `PENDING_NATIVE_SCHEMA_CAPTURE` until its host-visible schema is captured from the same fresh GitHub conversation.

The inventory validator now asserts the exact projected order, requires `GitHub.download_user_content`, rejects `GitHub.add_issue_comment`, and retains the 89-action uniqueness and target-name correspondence gates.

## 4. Architecture disposition

The correction does not invalidate the Checkpoint 372 architecture:

```text
exact remote Runtime Bridge parity remains       0 / 89
GitHub App + device-flow auth direction           unchanged
installation-derived repository scope             unchanged
internal REST / GraphQL transport direction       unchanged
caller-supplied credentials / arbitrary HTTP      forbidden
schema capture before implementation               still required
```

Only one action identity and its family allocation changed.

## 5. Exact next gate

Continue in the same fresh GitHub-only conversation so every schema is captured from one fixed projection.

The first schema batch is now the first 15 actions in that actual projected order, beginning with `GitHub.add_comment_to_issue` and ending with `GitHub.create_pull_request`.

No GitHub action is to be invoked. The schema capture must record exact title/description, complete host-visible input schema, required/optional fields, enums, validation constraints, pagination/continuation semantics, read/mutation classification, resource scope, and visible result/error notes. Any genericization or omission is evidence and must not be silently inferred away.

```text
FRESH_GITHUB_ACTION_COUNT=89
GITHUB_ACTIONS_INVOKED=0
CHECKPOINT372_EXACT_NAME_RECONSTRUCTION=CORRECTED
FRESH_ONLY_ACTION=GitHub.download_user_content
RECONSTRUCTION_ONLY_ACTION=GitHub.add_issue_comment
CONNECTOR_DRIFT_INFERRED=NO
NATIVE_SCHEMA_CAPTURE=IN_PROGRESS
IMPLEMENTATION=NOT_STARTED
VALIDATION130=PASS
NEXT=SCHEMA_CAPTURE_BATCH_1
```
