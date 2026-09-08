# Validation 132: GitHub Native Schema Capture Batch 2 Preserved

**Date:** 2026-09-08
**Status:** PASS / 30 OF 89 HOST-VISIBLE CONTRACTS PRESERVED / DISCOVERY-ONLY / BATCH 3 NEXT
**Research:** Research 123
**Scope:** Preserve projected GitHub connector contracts 16-30 from the same fixed fresh 89-action GitHub-only conversation, including the corrected `download_user_content` contract, pagination asymmetries, genericized tree-entry schema, bounded generic fetch behavior, and file-handoff semantics, without invoking any GitHub action.

## 1. Qualification conditions

```text
projected GitHub action count      89
schema batch                        2
projected ordinals                  16-30
cumulative captured contracts       30 / 89
GitHub actions invoked               0
Browser / web / shell / ADS          not used
```

The batch begins with `GitHub.create_tree` and ends with `GitHub.fetch_pr_comments`, exactly matching canonical inventory ordinals 16-30.

## 2. Projection-wide limitations remain stable

Batch 2 reproduces the Batch 1 host-projection pattern:

```text
separate action title metadata                 0 / 15 exposed
projected return type                         any for 15 / 15
machine-readable output schema                0 / 15 exposed
structured error schema                       0 / 15 exposed
error-code enum / HTTP mapping / retry schema 0 / 15 exposed
connector-level pagination input fields        0 / 15 exposed
```

Descriptions still carry important semantic output, validation, transport and pagination behavior that is not represented structurally.

## 3. `download_user_content` is now resolved

Checkpoint 373 corrected this exact action into the 89-action baseline. Batch 2 now establishes its native contract:

```text
input
    url: string

allowed target
    https://private-user-images.githubusercontent.com only

purpose
    private GitHub user-image attachments from issues / pull requests

repository files
    use fetch or fetch_file instead

result
    any
    no projected file-reference / byte / MIME schema
```

The Runtime Bridge mapping should therefore use a narrowly allowlisted GitHub user-content downloader rather than treating this action as ordinary REST repository access. This refines, but does not weaken, the existing rule against arbitrary caller-controlled HTTP authority: a semantic action may accept a URL only inside its exact server-enforced GitHub host/resource contract.

## 4. Workflow artifact handoff contract confirmed

`GitHub.download_workflow_artifact` confirms an explicit file-delivery semantic:

```text
GitHub artifact endpoint
    -> temporary redirect
    -> connector follows redirect
    -> reusable file reference for ZIP bytes
```

The projected return schema remains `any`, so exact file-reference fields are not visible. The already-selected Runtime Bridge resource/file-handoff architecture remains the correct reuse direction.

## 5. Generic `fetch` is bounded, not arbitrary HTTP

`GitHub.fetch` accepts a URL but its description exposes a substantial server-side allowlist and behavior boundary:

```text
supported public GitHub hosts
    github.com
    api.github.com
    raw.githubusercontent.com

method/resource authority
    approved GitHub repository resource families
    GET only for described API subresources
    unlisted endpoints rejected
    non-public-GitHub hosts rejected
    user / organization / secrets families unsupported

response handling
    JSON unchanged
    UTF-8 textual response supported
    oversized response rejected
    non-UTF-8 response rejected
    binary download unsupported

permissions
    active repository permissions still apply
    managed GitHub App installations lack administration permission
```

No exact oversized-response byte threshold is projected. This action is a bounded semantic GitHub GET facade, not permission to expose a general-purpose HTTP client in Codexless.

## 6. First explicit pagination asymmetry is captured

Batch 2 confirms that pagination behavior is action-specific:

```text
GitHub.fetch_commit_workflow_runs
    pull-request-triggered runs only
    FIRST PAGE ONLY
    no continuation mechanism exposed

GitHub.fetch_issue_comments
    ALL PAGES internally
    no caller page/cursor/limit fields

GitHub.fetch_pr_comments
    pagination behavior UNSPECIFIED
    no all-pages guarantee may be inferred
```

This directly validates the Research 123 design decision not to impose one global pagination policy across the parity surface.

## 7. Strong input-schema genericization discovered

`GitHub.create_tree.tree_elements` is projected only as:

```text
{ [key: string]: any }[]
```

The host therefore omits the inner Git tree-entry properties, required fields, enums, modes, types and path rules. This is stronger genericization than the Batch 1 contracts and is a real preimplementation evidence gap. The missing inner contract must not be guessed from generic Git knowledge and will require explicit later reconciliation from stronger evidence.

## 8. Additional exact contracts

Batch 2 also establishes:

```text
GitHub.fetch_file
    encoding = utf-8 | base64
    default utf-8
    start_line > 0
    end_line > 0
    line numbering is 1-based
    no projected end_line >= start_line rule

GitHub.fetch_issue
    exactly one repository selector:
        repository_full_name
        repository_id
        repository_url
    XOR is descriptive rather than structurally encoded
    repository_url description explicitly mentions GitHub Enterprise Server and GHE.com hosts

GitHub.fetch_pr
    description says comments are optional output content
    no include-comments control or inclusion condition is projected

GitHub.fetch_pr_comments
    normalized array merges issue comments, inline review comments and review submissions
    entry/discriminator/order schemas remain hidden behind any

GitHub.enable_auto_merge
    merge method inferred from repository settings
    no merge-method input
    description says result is only success
```

The explicit Enterprise-host examples in `fetch_issue.repository_url` are preserved as an architecture follow-up rather than silently assumed to be covered by the current github.com-focused GitHub App design.

## 9. Machine-readable preservation

`docs/research/github_connector_native_schema_capture.json` now records:

```text
status               PARTIAL_30_OF_89
capturedCount        30
batchesCompleted     [1, 2]
nextOrdinal          31
```

The validator now guards the Batch 2 tree genericization, `download_user_content` host restriction, first-page/all-pages/unspecified pagination distinctions, `fetch_file` encoding and line bounds, and `fetch_issue` selector XOR.

Observed result:

```text
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=30_OF_89
```

## 10. Exact continuation

Continue in the same fixed GitHub-only conversation with projected ordinals 31-45, beginning with `GitHub.fetch_pr_file_patch` and ending with `GitHub.get_repo_collaborator_permission`.

No GitHub action is to be invoked.

```text
VALIDATION132=PASS
NATIVE_SCHEMA_CAPTURE=30_OF_89
BATCH2=PASS
ACTIONS_INVOKED=0
CREATE_TREE_INNER_SCHEMA=GENERICIZED
DOWNLOAD_USER_CONTENT_CONTRACT=RESOLVED
PAGINATION_ASYMMETRY=CONFIRMED
ENTERPRISE_HOST_EXAMPLES=OBSERVED_IN_FETCH_ISSUE_SELECTOR
IMPLEMENTATION=NOT_STARTED
NEXT=SCHEMA_CAPTURE_BATCH_3_ORDINALS_31_45
```
