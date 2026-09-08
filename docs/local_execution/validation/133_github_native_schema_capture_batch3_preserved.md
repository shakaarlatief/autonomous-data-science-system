# Validation 133: GitHub Native Schema Capture Batch 3 Preserved

**Date:** 2026-09-08
**Status:** PASS / 45 OF 89 HOST-VISIBLE CONTRACTS PRESERVED / DISCOVERY-ONLY / BATCH 4 NEXT
**Research:** Research 123
**Scope:** Preserve projected GitHub connector contracts 31-45 from the same fixed fresh 89-action GitHub-only conversation, including PR patch validation/error semantics, Actions pagination/attempt limits, reaction pagination, PR diff format enum, zero-argument profile lookup, repository selector XOR, and collaborator-permission result omissions, without invoking any GitHub action.

## 1. Qualification conditions

```text
projected GitHub action count      89
schema batch                        3
projected ordinals                  31-45
cumulative captured contracts       45 / 89
GitHub actions invoked               0
Browser / web / shell / ADS          not used
```

The batch begins with `GitHub.fetch_pr_file_patch` and ends with `GitHub.get_repo_collaborator_permission`, exactly matching canonical inventory ordinals 31-45.

## 2. Projection-wide limitations remain stable

All fifteen actions again expose their input contracts while result/error metadata is largely descriptive:

```text
separate action title metadata                 0 / 15 exposed
projected return type                         any for 15 / 15
machine-readable output schema                0 / 15 exposed
structured error schema                       0 / 15 exposed
```

Batch 3 therefore reinforces that exact input parity can be reconstructed substantially from host discovery, while output/result/error parity still needs separate evidence treatment where descriptions are insufficient.

## 3. First concrete valid-empty versus 404 contract

`GitHub.fetch_pr_file_patch` provides especially important parity evidence:

```text
workflow
    call list_pr_changed_filenames first
    pass one exact returned path
    do not guess paths

valid PR but path absent
    patch = null

404
    repository or pull request could not be resolved
    do not retry alternative paths
```

This is the clearest discovery-only example so far of the Research 123 requirement to preserve valid-empty versus not-found semantics and no-blind-retry behavior.

## 4. Additional pagination and attempt semantics

Batch 3 extends the action-specific pagination matrix:

```text
GitHub.fetch_pr_patch
    ALL CHANGED-FILE PAGES internally

GitHub.fetch_workflow_run_artifacts
    FIRST PAGE ONLY
    no continuation control

GitHub.fetch_workflow_run_jobs
    LATEST ATTEMPT ONLY
    FIRST PAGE ONLY
    no previous-attempt selector
    no continuation control

reaction readers
    page + per_page inputs
    page described as 1-based
    no cursor / opaque continuation token
    no projected maximum for per_page
```

This further disproves any one-size-fits-all pagination layer for parity.

## 5. Actions transport/result distinctions

`GitHub.fetch_workflow_job_logs` explicitly follows GitHub's temporary redirect before decoding returned bytes. `GitHub.fetch_workflow_job_steps` explicitly returns only step summaries rather than the complete workflow-job payload.

The connector therefore exposes at least three different Actions read result classes across Batches 2-3:

```text
artifact ZIP     -> reusable file reference
job logs         -> redirect + decoded content
job steps        -> normalized summaries only
```

Those distinctions should be preserved by semantic Runtime Bridge tools rather than collapsed into one generic Actions response type.

## 6. Exact PR/read contracts

Batch 3 also establishes:

```text
GitHub.get_pr_diff.format
    diff | patch
    default = diff

GitHub.get_pr_info
    title / description / refs / status
    explicitly excludes actual code changes

GitHub.fetch_pr_patch
    dedicated all-pages patch path for code changes
```

The native connector intentionally separates PR metadata from code-change retrieval.

## 7. Identity/repository/permission evidence

`GitHub.get_profile` is a true zero-argument action. The profile result remains hidden behind `any`.

`GitHub.get_repo` repeats the descriptive repository selector XOR:

```text
exactly one of
    repository_full_name
    repository_id
    repository_url
```

Its repository URL description again explicitly includes GitHub Enterprise Server custom hosts and GHE.com API hosts, strengthening the Batch 2 endpoint-specific Enterprise-support evidence.

`GitHub.get_repo_collaborator_permission` says it returns a permission level, but the host does not expose the possible permission values, result field name, or result type. No enum such as read/write/admin may be inferred from discovery alone.

## 8. Machine-readable preservation

`docs/research/github_connector_native_schema_capture.json` now records:

```text
status               PARTIAL_45_OF_89
capturedCount        45
batchesCompleted     [1, 2, 3]
nextOrdinal          46
```

The validator now additionally guards:

```text
fetch_pr_file_patch patch=null + documented 404
fetch_pr_patch all-pages behavior
workflow artifacts first-page-only behavior
workflow jobs latest-attempt + first-page-only behavior
reaction page/per_page pagination
get_pr_diff diff|patch enum + default
a zero-argument get_profile contract
get_repo selector XOR
absence of a projected collaborator-permission result enum
```

Observed result:

```text
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=45_OF_89
```

## 9. Exact continuation

Continue the same fixed GitHub-only conversation with projected ordinals 46-60, beginning with `GitHub.get_user_login` and ending with `GitHub.lock_issue_conversation`.

No GitHub action is to be invoked.

```text
VALIDATION133=PASS
NATIVE_SCHEMA_CAPTURE=45_OF_89
BATCH3=PASS
ACTIONS_INVOKED=0
VALID_EMPTY_VS_404=EXPLICITLY_OBSERVED
NO_BLIND_RETRY_SEMANTIC=OBSERVED
PAGINATION_POLICY=FURTHER_DIFFERENTIATED
ENTERPRISE_SELECTOR_SCOPE=REINFORCED
PERMISSION_RESULT_ENUM=NOT_PROJECTED
IMPLEMENTATION=NOT_STARTED
NEXT=SCHEMA_CAPTURE_BATCH_4_ORDINALS_46_60
```
