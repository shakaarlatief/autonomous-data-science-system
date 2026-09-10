# Validation 188: Extended GitHub CI Evidence Publication Foundation Design

**Date:** 2026-09-10
**Status:** PASS / CHECKS + COMMIT STATUS FOUNDATION FROZEN / THREE READS + THREE WRITES / NO CI-EVIDENCE MUTATION
**Research:** Research 123

## 1. Purpose

Checkpoint 430 completes the first beyond-parity Repository Administration foundation. Research 123 next returns to the broad professional developer-superset permission plan. The strongest next capability is first-class **CI evidence publication**: GitHub Checks plus bounded commit-status writes.

The existing native connector can already read combined commit statuses and GitHub Actions runs/jobs, but it cannot create rich check runs or publish commit-status contexts. The project-owned GitHub App already has both `Checks=write` and `Commit statuses=write`, confirmed by the live installation metadata.

This validation freezes the first bounded Checks/Statuses extension before implementation. No check run, annotation, check-suite preference, rerequest, or commit-status mutation is performed here.

## 2. Why Checks + Commit Statuses are one foundation

GitHub Checks and commit statuses are two complementary ways to attach machine-readable validation evidence to a commit:

```text
Checks
    richer lifecycle
    structured output
    line annotations
    first-class GitHub App capability

Commit statuses
    lightweight state/context publication
    simple external-status compatibility
    already paired with native get_commit_combined_status read support
```

GitHub documents Checks write access as GitHub-App-capable and exposes create/update check-run endpoints under `Checks(write)`. Commit-status creation requires `Commit statuses(write)`. The current installed App reports both permissions as write.

## 3. First extension slice

The first CI Evidence foundation contains exactly six new actions:

```text
github.get_check_run                  read
github.list_check_runs_for_ref        read
github.list_check_run_annotations     read
github.create_check_run               write
github.update_check_run               write
github.create_commit_status           write
```

This first slice deliberately omits check-suite creation/preferences, check-run/suite rerequest, requested-action buttons, output images, and arbitrary details/target URLs.

## 4. Read contracts

### `github.get_check_run`

Caller contract:

```text
repository_full_name  required string 3..512
check_run_id          required positive safe integer
additionalProperties  false
```

Execution:

1. require installation-derived authority for repository;
2. fixed GET `/repos/{owner}/{repo}/check-runs/{check_run_id}`;
3. normalize bounded check-run metadata/output/app identity/pull-request references;
4. expose no response headers, credential, arbitrary URL, endpoint, or transport control.

### `github.list_check_runs_for_ref`

Caller contract:

```text
repository_full_name  required string 3..512
ref                   required string 1..512
check_name            optional string|null, max 256
status                optional enum queued|in_progress|completed|null
filter                optional enum latest|all, default latest
page_size             optional integer 1..100, default 100
page                  optional positive safe integer, default 1
additionalProperties  false
```

The raw GitHub `app_id` filter is intentionally not exposed in v1. Runtime Bridge is a repository-authorized evidence surface, not a generic App-ID query proxy.

### `github.list_check_run_annotations`

Caller contract:

```text
repository_full_name  required string 3..512
check_run_id          required positive safe integer
page_size             optional integer 1..100, default 100
page                  optional positive safe integer, default 1
additionalProperties  false
```

Execution uses only the fixed check-run annotations endpoint.

## 5. Normalized check-run result

The common normalized check-run object should preserve:

```text
id
nodeId
name
headSha
externalId
htmlUrl
detailsUrl
status
conclusion
startedAt
completedAt
checkSuiteId
output:
    title
    summary
    text
    annotationsCount
app:
    id
    slug
    name
pullRequests[]:
    number
    headRef
    headSha
    baseRef
    baseSha
```

URLs are output evidence from GitHub, never caller-selected transport inputs.

## 6. Check-run write contract

### Common output object

Both create and update may accept a bounded `output` object:

```text
title       required string 1..255
summary     required string, max 65536
text        optional string|null, max 65536
annotations optional array, max 50
```

Each annotation is strictly bounded:

```text
path              required repository-relative POSIX path, 1..4096
start_line        required positive integer
end_line          required positive integer, >= start_line
start_column      optional positive integer|null
end_column        optional positive integer|null
annotation_level  required enum notice|warning|failure
message           required string 1..65536
title             optional string|null, max 255
```

Column coordinates are allowed only for a single-line annotation and must be supplied as a consistent pair. Absolute paths, backslashes, `.`/`..` segments, NULs, and traversal are rejected before dispatch.

The first slice deliberately excludes `raw_details`, output images, and requested-action buttons. Requested-action buttons are especially inappropriate while the App webhook receiver remains disabled because GitHub delivers requested actions through check-run webhook events.

### `github.create_check_run`

Caller contract:

```text
repository_full_name  required
name                  required string 1..256
head_sha              required hex 7..64
status                required enum queued|in_progress|completed
conclusion            optional enum action_required|cancelled|failure|neutral|success|skipped|timed_out|null
output                optional bounded object|null
additionalProperties  false
```

Semantic rules:

- caller cannot select GitHub-Action-only statuses `waiting`, `requested`, or `pending`;
- caller cannot set `stale` conclusion;
- `status=completed` requires a conclusion;
- queued/in-progress states forbid a conclusion;
- Runtime Bridge first resolves `head_sha` through the fixed repository commit endpoint and sends the exact resolved commit SHA;
- no caller timestamp is exposed;
- no caller `details_url`, `external_id`, actions, images, webhook, App ID, endpoint, or transport field is exposed;
- same repository/resolved-SHA/check-name creation is serialized;
- mutation-aware transport is single-attempt; uncertain create is never replayed automatically.

### `github.update_check_run`

Caller contract:

```text
repository_full_name  required
check_run_id          required positive safe integer
status                optional enum queued|in_progress|completed|null
conclusion            optional bounded conclusion enum|null
output                optional bounded object|null
additionalProperties  false
```

At least one update is required.

Runtime Bridge performs a fixed read before write. Status transitions are monotonic:

```text
queued       -> queued | in_progress | completed
in_progress  -> in_progress | completed
completed    -> completed
```

A completed check cannot be reopened. Any target completed state requires a conclusion; non-completed target state forbids conclusion. Output-only updates preserve current state. The owning repository and exact check-run ID are re-read inside the serialized mutation boundary immediately before PATCH. GitHub itself remains final authority on whether the authenticated App owns a writable check run; classifiable 403/404/422 responses remain definite, not mutation-uncertain.

## 7. Commit-status write contract

### `github.create_commit_status`

Caller contract:

```text
repository_full_name  required
commit_sha            required hex 7..64
state                 required enum error|failure|pending|success
context_suffix        optional string 1..64, pattern ^[A-Za-z0-9._-]+$, default runtime-bridge
description           optional string|null, max 140
additionalProperties  false
```

Runtime Bridge maps:

```text
context_suffix = X
-> context = codexless/X
```

This prevents the caller from impersonating or overwriting another CI provider's status context. GitHub treats status context case-insensitively and uses the latest status per context in the combined result, so namespace ownership matters.

The first slice deliberately does not expose `target_url`; no arbitrary link destination is written into the repository UI.

Execution:

1. require installation-derived repository authority;
2. fixed read resolves `commit_sha` to one exact repository commit;
3. serialize by repository + resolved SHA + lowercase `codexless/<suffix>` context;
4. fixed POST `/repos/{owner}/{repo}/statuses/{sha}`;
5. body contains only `state`, server-prefixed context, and optional description;
6. never auto-retry mutation uncertainty.

GitHub documents a limit of 1000 statuses per SHA/context. Runtime Bridge should preserve the GitHub 422 as a definite validation response rather than trying to bypass or rotate contexts automatically.

## 8. Explicitly deferred Checks capabilities

The following are useful but not part of the first foundation:

```text
create check suite manually
update automatic check-suite preferences
rerequest check run
rerequest check suite
requested-action buttons
check output images
arbitrary details_url
arbitrary commit-status target_url
check-suite webhook orchestration
```

Creating a check run already lets GitHub create the appropriate check suite automatically. Manual check-suite lifecycle is unnecessary for the first implementation.

Rerequest endpoints trigger check-run/check-suite webhook events. The current App webhook receiver is deliberately disabled, so exposing rerequest now would create an event the Runtime Bridge does not own end-to-end.

## 9. Qualification plan

The first release should expose six tools without positive CI-evidence mutation during publication:

```text
1. local wire schemas: 6/6
2. fake-dependency fixed-route/normalization tests
3. semantic no-write tests:
   - invalid annotation path
   - completed without conclusion
   - conclusion on in-progress
   - backward update transition
   - invalid status context suffix
4. uncertain create/update/status transport: exactly one mutation dispatch, no replay
5. immutable runtime publication
6. fresh-host projection/schema qualification 6/6
7. positive-live reads on canonical ADS repository
8. positive-live writes only after separate explicit owner authorization
```

A future positive-live fixture can attach one Codexless check run and one `codexless/...` status context to an existing disposable or explicitly selected commit without modifying code or moving refs. The exact target SHA and visible check/status text must be separately authorized before the writes.

## 10. Disposition

```text
VALIDATION188=PASS
EXTENDED_CI_EVIDENCE_FOUNDATION_ACTIONS=6
EXTENDED_CI_EVIDENCE_READS=3
EXTENDED_CI_EVIDENCE_WRITES=3
CHECKS_PERMISSION=LIVE_WRITE_CONFIRMED
COMMIT_STATUSES_PERMISSION=LIVE_WRITE_CONFIRMED
CHECK_REREQUEST=DEFERRED_WEBHOOK_DEPENDENCY
CHECK_SUITE_MANAGEMENT=DEFERRED_NOT_FOUNDATIONAL
CALLER_WRITABLE_EXTERNAL_URLS=DEFERRED
CI_EVIDENCE_MUTATION_OCCURRED=false
NEXT=IMPLEMENT_EXTENDED_CI_EVIDENCE_FOUNDATION
```
