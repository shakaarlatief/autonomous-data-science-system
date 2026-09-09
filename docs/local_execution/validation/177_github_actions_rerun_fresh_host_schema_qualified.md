# Validation 177: GitHub Actions Rerun Fresh-Host Schema Qualified

**Date:** 2026-09-09
**Status:** PASS / FRESH HOST 2 OF 2 / BOUNDED CALLER AUTHORITY / INVALID NO-WRITE GUARDS 2 OF 2 / ZERO MUTATIONS
**Research:** Research 123

## 1. Scope

Validation 176 / Checkpoint 419 activated Runtime Bridge preview.37 with all 89 captured native GitHub action names implemented. The next gate required a refreshed disposable ChatGPT host to qualify exactly the two newly live GitHub Actions rerun mutation contracts without performing any positive rerun.

The owner returned the fresh-host qualification transcript for:

```text
github.rerun_failed_workflow_run_jobs
github.rerun_workflow_job
```

No third GitHub call was made.

## 2. Fresh-host projection

Both exact actions projected: 2/2. No separate title was visible for either action.

### github.rerun_failed_workflow_run_jobs

Visible description:

```text
Re-run failed jobs for one completed GitHub Actions workflow run in an installation-authorized repository. Runtime Bridge preflights the fixed workflow-run resource, requires completed status, and then uses GitHub's fixed rerun-failed-jobs endpoint. The caller supplies only repository and positive run ID; credentials, host, endpoint, method, headers and transport remain server-owned.
```

Host-visible schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "repo_full_name": { "type": "string", "minLength": 3, "maxLength": 512 },
    "run_id": { "type": "integer", "minimum": 1, "maximum": 9007199254740991 }
  },
  "required": ["repo_full_name", "run_id"]
}
```

No optional fields/defaults were exposed. No separate annotations were visible.

### github.rerun_workflow_job

Visible description:

```text
Re-run exactly one completed failed or cancelled GitHub Actions job in an installation-authorized repository. Runtime Bridge reads the fixed job resource, derives and serializes by its workflow-run ID, revalidates job identity/state, and dispatches GitHub's fixed job-rerun endpoint. The caller supplies only repository and positive job ID.
```

Host-visible schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "repo_full_name": { "type": "string", "minLength": 3, "maxLength": 512 },
    "job_id": { "type": "integer", "minimum": 1, "maximum": 9007199254740991 }
  },
  "required": ["repo_full_name", "job_id"]
}
```

No optional fields/defaults were exposed. No separate annotations were visible.

For both tools the caller-visible contract exposes no credential/token, Authorization header, GitHub host, arbitrary URL/endpoint, HTTP method/header, GraphQL document, permission profile, transport selector, filesystem path, shell command or process authority.

## 3. Invalid no-write guards

Exactly two invalid calls were attempted, once each, with no repair or retry.

### Call 1

```text
github.rerun_failed_workflow_run_jobs
repo_full_name = shakaarlatief/autonomous-data-science-system
run_id = 0
```

Exact host rejection:

```text
Arguments do not match schema:

0 is less than the minimum of 1

Failed validating 'minimum' in schema['properties']['run_id']:
    {'type': 'integer', 'minimum': 1, 'maximum': 9007199254740991}

On instance['run_id']:
    0
```

The request was rejected by host-side schema validation before Runtime Bridge/GitHub mutation dispatch. No separate error code or `mutationUncertain` field was returned. Retry count was zero and no workflow/job changed.

### Call 2

```text
github.rerun_workflow_job
repo_full_name = shakaarlatief/autonomous-data-science-system
job_id = 0
```

Exact host rejection:

```text
Arguments do not match schema:

0 is less than the minimum of 1

Failed validating 'minimum' in schema['properties']['job_id']:
    {'type': 'integer', 'minimum': 1, 'maximum': 9007199254740991}

On instance['job_id']:
    0
```

This request also failed at host-side schema validation before Runtime Bridge/GitHub mutation dispatch. No separate error code or `mutationUncertain` field was returned. Retry count was zero and no workflow/job changed.

## 4. Qualification result

```text
projected actions                     2 / 2
bounded schemas                       2 / 2
invalid no-write guards               2 / 2
positive GitHub mutations             0
mutation retries                      0
mutation-uncertain results            0
secret/credential authority exposed   no
arbitrary transport authority exposed no
GitHub workflow/job changes           0
```

All PASS conditions were satisfied. Combined with Validation 176, all 89 implemented Runtime Bridge GitHub action names now have their local wire layer complete, and the final two action names have fresh-host projection/boundedness evidence. This does not complete positive-live qualification of either rerun mutation.

```text
VALIDATION177=PASS
ACTIONS_RERUN_MUTATION_FRESH_HOST_SCHEMA=PASS_2_OF_2
ACTIONS_RERUN_MUTATION_FRESH_HOST_GUARDS=PASS_2_OF_2
ACTIONS_RERUN_MUTATION_POSITIVE_LIVE=0_OF_2
ACTIONS_RERUN_MUTATION_OCCURRED=false
NATIVE_ACTION_NAMES_IMPLEMENTED=89_OF_89
NATIVE_WRITE_ACTIONS_IMPLEMENTED=41_OF_41
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=ACTIONS_RERUN_POSITIVE_LIVE_FIXTURE_PREFLIGHT
```
