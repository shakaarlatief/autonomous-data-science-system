# Validation 192: Extended GitHub Actions Orchestration Foundation Design

**Date:** 2026-09-10
**Status:** PASS / ACTIONS ORCHESTRATION FOUNDATION FROZEN / THREE READS + THREE WRITES / NO ACTIONS MUTATION
**Research:** Research 123

## 1. Purpose

Validation 191 / Checkpoint 434 complete the second beyond-parity GitHub family, CI Evidence Publication. Research 123 now returns to the broader developer-superset capability plan while AB-030 remains parked as a later ADS-integration idea.

The third beyond-parity family is selected as **GitHub Actions Orchestration**. The existing native-parity surface can inspect jobs, steps, logs and artifacts and can rerun failed jobs or one failed/cancelled job, but the captured 89-action connector does not expose:

```text
workflow discovery by repository
exact workflow metadata reads
exact workflow-run metadata reads
workflow_dispatch
whole-run rerun
workflow-run cancellation
```

These are a coherent operational family: identify the exact workflow/run, launch a deliberately selected manual workflow, rerun an exact completed run, or cancel an exact active run.

No workflow is dispatched, rerun, cancelled, enabled, disabled or otherwise mutated by this design validation.

## 2. Current repository and permission evidence

The canonical ADS repository currently contains:

```text
workflow files               34
workflow_dispatch workflows  27
```

The repository therefore has substantial existing manual-run surface that cannot currently be invoked through the captured native connector.

Two especially useful future qualification candidates are already repository-owned validation workflows:

```text
.github/workflows/repository-integrity.yml
.github/workflows/knowledge-map-integrity.yml
```

Both declare `workflow_dispatch`; both use `permissions: contents: read`; neither is selected for a positive mutation by this design record.

The live Runtime Bridge GitHub App installation was re-read during this design pass. It remains installed on personal account `shakaarlatief` with All repositories and reports:

```text
Actions    write
Workflows  write
```

Current official GitHub REST documentation requires Actions(read) for listing/getting workflows and workflow runs, and Actions(write) for workflow dispatch, whole-run rerun and cancellation. The selected third family therefore requires no GitHub App permission change.

`Workflows(write)` is already present but is not used as justification for this slice: the selected REST operations are governed by the Actions permission. Editing workflow YAML remains a repository-content/workflow-file concern and is outside this family.

## 3. Current official GitHub behavior relevant to the design

The current github.com Runtime Bridge REST baseline remains API version `2026-03-10`.

Official GitHub documentation establishes:

```text
List repository workflows
    GET /repos/{owner}/{repo}/actions/workflows
    Actions(read)

Get a workflow
    GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}
    Actions(read)

Get a workflow run
    GET /repos/{owner}/{repo}/actions/runs/{run_id}
    Actions(read)

Create a workflow dispatch event
    POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
    Actions(write)
    required ref = branch or tag
    inputs optional, maximum 25 properties
    current response = 200 including workflow_run_id/run URLs

Re-run a workflow
    POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun
    Actions(write)
    optional debug logging in raw GitHub API
    current response = 201

Cancel a workflow run
    POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel
    Actions(write)
    current response = 202 or 409
```

GitHub separately documents that `workflow_dispatch` is available only when the workflow file exists on the repository default branch. A dispatch may target a branch or tag. Workflow-dispatch inputs have at most 25 top-level properties and a maximum payload of 65,535 characters.

GitHub also documents whole workflow reruns as available for up to 30 days after the initial run. Runtime Bridge should not attempt to bypass GitHub's own eligibility window.

## 4. Third extension slice

The first Actions Orchestration foundation contains exactly six new actions:

```text
github.list_repository_workflows   read
github.get_workflow                read
github.get_workflow_run            read
github.dispatch_workflow           write
github.rerun_workflow_run          write
github.cancel_workflow_run         write
```

This gives the family a complete bounded loop:

```text
discover exact workflow
    -> read exact workflow
    -> dispatch exact workflow/ref
    -> read exact returned run
    -> cancel or later rerun exact run when semantically eligible
```

## 5. Read contracts

### `github.list_repository_workflows`

Caller contract:

```text
repository_full_name  required string 3..512
page_size             optional integer 1..100, default 100
page                  optional positive safe integer, default 1
additionalProperties  false
```

Execution:

1. require installation-derived repository authority;
2. fixed GET `/repos/{owner}/{repo}/actions/workflows`;
3. fixed pagination only;
4. normalize repository workflow metadata;
5. expose no credential, header, host, arbitrary URL, endpoint, query expression or transport control.

Normalized list result:

```text
totalCount
count
page
pageSize
workflows[]:
    id
    nodeId
    name
    path
    state
    createdAt
    updatedAt
    htmlUrl
    badgeUrl
```

### `github.get_workflow`

Caller contract:

```text
repository_full_name  required string 3..512
workflow_id           required positive safe integer
additionalProperties  false
```

The first slice deliberately accepts only the stable positive numeric workflow ID. GitHub's raw endpoint also accepts a workflow filename, but Runtime Bridge does not need to expose a second path-like selector when `list_repository_workflows` already provides exact IDs and paths. This avoids filename/path ambiguity without reducing the actual orchestration capability.

Execution uses only fixed GET `/repos/{owner}/{repo}/actions/workflows/{workflow_id}` and returns the normalized workflow object above.

### `github.get_workflow_run`

Caller contract:

```text
repository_full_name  required string 3..512
run_id                required positive safe integer
additionalProperties  false
```

Execution uses fixed GET `/repos/{owner}/{repo}/actions/runs/{run_id}`.

Normalized run result should preserve the fields needed for exact later mutation preflight and useful inspection:

```text
id
nodeId
name
displayTitle
workflowId
checkSuiteId
path
headBranch
headSha
event
status
conclusion
runNumber
runAttempt
runStartedAt
createdAt
updatedAt
htmlUrl
actor:
    login
    id
triggeringActor:
    login
    id
pullRequests[]:
    number
    headRef
    headSha
    baseRef
    baseSha
```

Raw API operation URLs such as cancel/rerun/jobs URLs are not caller authority and do not need to be surfaced merely because GitHub returns them.

## 6. Workflow dispatch write contract

### `github.dispatch_workflow`

Caller contract:

```text
repository_full_name  required string 3..512
workflow_id           required positive safe integer
ref_type              required enum branch|tag
ref_name              required string 1..512
expected_ref_sha      required hex 7..64
inputs                 optional array|null, max 25
additionalProperties  false
```

Each optional input entry is a strict object:

```text
name   required string 1..256
value  required string|max65535 OR boolean OR bounded JSON number
additionalProperties false
```

Runtime-owned input rules:

```text
input names must be unique within the request
no input value may be null or a nested object/array
at most 25 entries
canonical serialized inputs object <= 65535 characters
```

The array representation is deliberate. It lets the host expose a strict repeated `{name,value}` schema instead of accepting an arbitrary caller-defined nested object while Runtime Bridge still sends GitHub the required object map.

Dispatch execution:

1. require installation-derived repository authority;
2. fixed-read the exact numeric workflow ID;
3. require workflow `state=active`;
4. resolve `ref_type + ref_name` through fixed GitHub branch/tag semantics;
5. resolve/peel the selected ref to one exact commit SHA;
6. require that exact resolved SHA to match `expected_ref_sha`;
7. serialize by repository + workflow ID + ref type/name;
8. re-read workflow state and re-resolve the ref inside the serialized mutation boundary;
9. reject state/SHA drift before POST;
10. build the bounded inputs object from the strict input-entry array;
11. fixed POST `/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches`;
12. normalize the current API response containing the exact new workflow-run identity;
13. never automatically replay a mutation-uncertain dispatch.

Normalized successful result:

```text
accepted          true
repositoryFullName
workflowId
workflowName
workflowPath
refType
refName
resolvedRefSha
workflowRunId
runUrl
htmlUrl
```

`runUrl` and `htmlUrl` are returned evidence from GitHub, not caller-selected transport destinations.

The caller cannot select:

```text
credential/token
GitHub host
endpoint or HTTP method
headers
API version
arbitrary event type
repository_dispatch event
client_payload
raw ref namespace
raw commit SHA as the dispatch ref
arbitrary request body
workflow file path
workflow state
transport implementation
```

The explicit `expected_ref_sha` is the optimistic-concurrency guard. A branch or tag name alone is insufficient for governed orchestration because a movable branch can change after a human/model inspects it but before dispatch.

GitHub remains final authority on whether the selected workflow actually supports `workflow_dispatch` and on configured workflow input names/types. A classifiable GitHub validation response remains definite and is not converted into mutation uncertainty.

## 7. Whole-run rerun write contract

### `github.rerun_workflow_run`

Caller contract:

```text
repository_full_name  required string 3..512
run_id                required positive safe integer
expected_head_sha     required hex 7..64
expected_run_attempt  required positive safe integer
additionalProperties  false
```

Runtime Bridge intentionally does not expose raw GitHub's `enable_debug_logging` option in this first slice. Debug reruns can materially increase log verbosity and are not required to establish whole-run orchestration. The server-owned behavior is ordinary rerun with debug logging disabled.

Execution:

1. require installation-derived repository authority;
2. fixed GET the exact workflow run;
3. require exact `headSha == expected_head_sha`;
4. require exact `runAttempt == expected_run_attempt`;
5. require `status=completed` before a whole-run rerun;
6. serialize by repository + run ID;
7. re-read exact run identity/state/attempt inside the mutation boundary;
8. reject head/attempt/state drift before mutation;
9. fixed POST `/repos/{owner}/{repo}/actions/runs/{run_id}/rerun`;
10. return a bounded accepted receipt tied to the preflight run identity;
11. never automatically replay mutation uncertainty.

GitHub's current rerun-age/policy rules remain GitHub-owned. Runtime Bridge does not invent a bypass when GitHub refuses an otherwise structurally valid rerun.

The required `expected_run_attempt` is important because reruns retain the same workflow run ID while incrementing attempt state. It prevents a caller from unknowingly rerunning a newer attempt than the one it inspected.

## 8. Workflow-run cancellation contract

### `github.cancel_workflow_run`

Caller contract:

```text
repository_full_name  required string 3..512
run_id                required positive safe integer
expected_head_sha     required hex 7..64
expected_run_attempt  required positive safe integer
additionalProperties  false
```

Execution:

1. require installation-derived repository authority;
2. fixed GET exact workflow run;
3. require exact head SHA and run attempt;
4. reject a run already in `completed` state before mutation;
5. require an active/non-terminal GitHub Actions run status;
6. serialize by repository + run ID;
7. re-read identity/state/attempt inside the mutation boundary;
8. reject drift or completed state before POST;
9. fixed POST `/repos/{owner}/{repo}/actions/runs/{run_id}/cancel`;
10. normalize HTTP 202 as accepted, not as proof the run has already reached final `cancelled` conclusion;
11. preserve a GitHub 409 race/state conflict as definite;
12. never automatically retry mutation uncertainty.

Cancellation must **not** silently escalate to GitHub's force-cancel endpoint. GitHub explicitly documents force-cancel as a recovery path only when ordinary cancellation is not responding. That stronger operation is deferred to a separately designed recovery capability if ever needed.

## 9. Shared mutation and uncertainty rules

All three write actions follow the existing Runtime Bridge GitHub mutation model:

```text
preflight exact installation-authorized object
    -> serialize on the smallest stable mutation key
    -> revalidate exact object/state inside the lock
    -> one fixed GitHub mutation request
    -> classifiable HTTP/state errors remain definite
    -> transport ambiguity after dispatch becomes mutationUncertain=true
    -> never automatically replay an uncertain mutation
```

For dispatch, the stable key is repository + workflow ID + explicit ref identity. For rerun/cancel, the stable key is repository + workflow run ID.

The tools do not promise that an accepted asynchronous GitHub operation has already reached its final state. Callers use `github.get_workflow_run` for read-only reconciliation.

## 10. Explicitly deferred Actions capabilities

The following remain outside the first Actions Orchestration foundation:

```text
force-cancel workflow run
workflow enable / disable
workflow-run deletion
workflow-run log deletion
artifact/cache deletion
approve fork pull-request workflow run
review pending deployments
review custom deployment protection rules
repository_dispatch
arbitrary custom event/client_payload
workflow YAML creation/editing/deletion
raw workflow debug rerun controls
Actions policy/default-permission administration
```

Reasons:

```text
force-cancel
    escalation/recovery operation; GitHub says use only when ordinary cancel is not responding

workflow enable/disable
    changes persistent workflow activation policy rather than one run

run/log/artifact/cache deletion
    destructive evidence/storage lifecycle

fork approval
    trust/security decision involving external contributor code

deployment review
    belongs with Deployments/Environments and release governance

repository_dispatch
    broader custom event surface with arbitrary event/client payload semantics

workflow file mutation
    repository content change already belongs to guarded Contents/Git workflows

Actions policy changes
    administration/policy authority, not run orchestration
```

## 11. Qualification plan

Implementation/publication should preserve the same evidence layering used for the first two beyond-parity families:

```text
1. local wire schemas: 6/6
2. fake-dependency route and normalization tests for all six actions
3. dispatch no-write guards:
   - workflow_id <= 0 rejected by schema
   - invalid ref_type rejected by enum
   - >25 inputs rejected by schema
   - duplicate input names rejected before dispatch
   - serialized input payload >65535 rejected before dispatch
   - expected_ref_sha mismatch rejected before dispatch
   - inactive workflow rejected before dispatch
4. rerun no-write guards:
   - non-completed run rejected
   - expected_head_sha mismatch rejected
   - expected_run_attempt mismatch rejected
5. cancel no-write guards:
   - completed run rejected
   - expected_head_sha mismatch rejected
   - expected_run_attempt mismatch rejected
6. mutation-uncertainty tests prove exactly one underlying mutation dispatch and zero replay
7. immutable Runtime Release publication
8. local positive reads for all three read actions
9. fresh-host projection/schema qualification 6/6
10. fresh-host positive reads and deterministic no-write guards
11. positive-live dispatch/rerun/cancel only after separate explicit owner authorization and exact safe workflow/run fixture design
```

A promising future positive-live fixture is the existing `Repository integrity` workflow because it already supports `workflow_dispatch`, declares only `contents: read`, and performs repository validation rather than deployment/publication. That is not yet the accepted mutation fixture. The exact target ref/SHA, workflow ID, expected external effects, and a reliable way to obtain an eligible active run for cancellation must be frozen separately before any positive Actions mutation.

## 12. Relationship to AB-030

AB-030 remains deliberately parked.

Actions Orchestration is a new GitHub capability family:

```text
launch / rerun / cancel GitHub Actions execution
```

AB-030 is a later ADS integration using the already completed CI Evidence Publication primitive:

```text
publish already-earned ADS validation evidence to GitHub
```

This design does not merge those tracks and does not activate AB-030.

## 13. Official sources

Current official GitHub documentation consulted for this design:

```text
https://docs.github.com/en/rest/actions/workflows
https://docs.github.com/en/rest/actions/workflow-runs
https://docs.github.com/en/actions/how-tos/manage-workflow-runs
https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow
https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
```

## 14. Disposition

```text
VALIDATION192=PASS
THIRD_BEYOND_PARITY_FAMILY=GITHUB_ACTIONS_ORCHESTRATION
ACTIONS_ORCHESTRATION_FOUNDATION_ACTIONS=6
ACTIONS_ORCHESTRATION_READS=3
ACTIONS_ORCHESTRATION_WRITES=3
LIVE_ACTIONS_PERMISSION=WRITE_CONFIRMED
LIVE_WORKFLOWS_PERMISSION=WRITE_CONFIRMED_NOT_REQUIRED_FOR_SELECTED_ENDPOINTS
REPOSITORY_WORKFLOW_FILES=34
REPOSITORY_WORKFLOW_DISPATCH_FILES=27
DISPATCH_EXPECTED_REF_SHA_GUARD=REQUIRED
RERUN_EXPECTED_HEAD_SHA_GUARD=REQUIRED
RERUN_EXPECTED_RUN_ATTEMPT_GUARD=REQUIRED
CANCEL_EXPECTED_HEAD_SHA_GUARD=REQUIRED
CANCEL_EXPECTED_RUN_ATTEMPT_GUARD=REQUIRED
FORCE_CANCEL=DEFERRED_SEPARATE_RECOVERY_ACTION
WORKFLOW_ENABLE_DISABLE=DEFERRED_POLICY_MUTATION
REPOSITORY_DISPATCH=DEFERRED_BROADER_EVENT_SURFACE
AB030=UNCHANGED_PARKED
ACTIONS_ORCHESTRATION_MUTATION_OCCURRED=false
NEXT=IMPLEMENT_EXTENDED_GITHUB_ACTIONS_ORCHESTRATION_FOUNDATION
```
