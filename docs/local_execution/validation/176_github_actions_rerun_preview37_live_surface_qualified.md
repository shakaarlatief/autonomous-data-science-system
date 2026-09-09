# Validation 176: GitHub Actions Rerun Preview.37 Live Surface Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.37 LIVE / ALL 89 CAPTURED GITHUB ACTION NAMES IMPLEMENTED / TWO ACTIONS RERUN TOOLS LIVE / NO ACTIONS RERUN WRITE / FRESH-HOST SCHEMA GATE NEXT
**Research:** Research 123

## 1. Starting boundary

Validation 175 / Checkpoint 418 preserves the PR/review positive-live uncertainty stop and explicitly permits independent implementation of the final two unimplemented GitHub Actions rerun names while leaving PR #84 untouched. The remaining native actions were:

```text
github.rerun_failed_workflow_run_jobs
github.rerun_workflow_job
```

This validation implements, tests, publishes and activates both actions without performing a positive workflow rerun.

## 2. Runtime Bridge contracts

Both actions are repository-scoped through GitHub App installation-derived authority and fixed server-owned REST endpoints. Callers provide only `repo_full_name` plus one positive integer run/job ID. No credential, GitHub host, URL, endpoint, HTTP method/header, GraphQL document, filesystem path, shell command, permission profile or transport implementation is caller-selectable.

`github.rerun_failed_workflow_run_jobs` first reads the fixed workflow-run resource and requires the run to be completed before dispatching GitHub's fixed `/actions/runs/{run_id}/rerun-failed-jobs` mutation endpoint.

`github.rerun_workflow_job` reads the fixed job resource, derives the owning workflow-run ID, serializes rerun mutation by that run, rereads and revalidates job identity/state, and requires the job to be completed with `failure` or `cancelled` conclusion before dispatching GitHub's fixed `/actions/jobs/{job_id}/rerun` endpoint. This is an explicit Runtime Bridge narrowing aligned with the captured native action description.

Both POST requests use the existing mutation-aware transport. Uncertain mutation results remain single-attempt and fail-visible.

## 3. Focused and broad regression qualification

Focused Actions mutation integration tests pass all four cases:

```text
fixed installation-scoped run/job rerun endpoints          PASS
completed/run and failed-or-cancelled job guards            PASS
invalid positive-ID guards before transport                 PASS
uncertain mutation single-attempt/no-retry behavior          PASS
```

Reconstructed broad current-source qualification passes:

```text
GITHUB_READONLY_WIRE_SCHEMA=PASS tools=48
GITHUB_REPOSITORY_GIT_MUTATION_WIRE_SCHEMA=PASS tools=8
GITHUB_ISSUE_MUTATION_WIRE_SCHEMA=PASS tools=12
GITHUB_PR_REVIEW_MUTATION_WIRE_SCHEMA=PASS tools=19
GITHUB_ACTIONS_RERUN_MUTATION_WIRE_SCHEMA=PASS tools=2
PUBLIC_SURFACE_REGISTRATION=PASS tools=153
Actions rerun integration PASS 4/4
PR/review integration PASS 4/4
issue integration PASS 4/4
repository Git integration PASS 4/4
all-read integration PASS
G0 integration PASS
read-only foundation PASS
bounded semantic Git count guards PASS tools=153
```

The public wire schema for both new actions is a strict object with `additionalProperties=false`, bounded repository name and positive integer identifier.

## 4. Immutable preview.37 release

Private local-runtime source head:

```text
f29241ce1be4368fcd956c197e5d976eef6f15b8
```

preserves immutable release:

```text
releaseId               github-actions-rerun-mutations-v1
targetVersion           0.1.1-preview.37-github-actions-rerun-mutations
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         153
fileCount               10
regressionCount         16
runtimeDependencyCount  1
manifestSha256          eb8393734f0d9af0ebd33ea32e7b6cbd950bbe27f8c7e540a62e10ca4f314eaf
```

Manifest hash binding and canonical JSON formatting passed before commit. Runtime Release `prepare` succeeded. Prepublication verification returned the expected ten target mismatches. Publication operation `rm_7ed8b32ea3b9c8c8196bf066516b8a43` succeeded without recovery. Restart operation `rm_e6ed454622ddfb9c5ab6f0eb9680eba7` succeeded without recovery. Postactivation verification returned `status=verified`, `targetToolCount=153`, `mismatchCount=0`.

## 5. Live local MCP qualification

Postactivation loopback health reports:

```text
ok              true
version         0.1.1-preview.37-github-actions-rerun-mutations
surfaceVersion  codexless-public-preview-v2
toolCount       153
```

Stateless MCP `tools/list` reports exactly 153 public tools and 89 GitHub tools. Both exact Actions rerun mutation names are present. This is the first Runtime Bridge release in Research 123 with all 89 captured native GitHub action names implemented simultaneously.

Two deliberate no-write live probes used ID `0` and were rejected at MCP input validation before GitHub dispatch:

```text
github.rerun_failed_workflow_run_jobs
  run_id: Too small: expected number to be >=1

github.rerun_workflow_job
  job_id: Too small: expected number to be >=1
```

No workflow run or job was rerun.

Protected authorization remains configured/stored/authorized with non-expired access and refresh authorization and no refresh recommendation after restart.

## 6. Disposition

Runtime Bridge now implements all 89 captured native GitHub action names and all 41 captured native write action names. This is implementation-name coverage, not exact wrapper parity. Exact native output envelopes remain hidden and several deliberate Runtime Bridge narrowings remain explicit, so `EXACT_NATIVE_PARITY_ROWS_CLOSED` remains zero.

Positive-live coverage is also not complete. The PR/review family remains stopped at 13/19 after an explicit mutation-uncertain dismissal result, and the two Actions rerun mutations remain positive-live 0/2 pending fresh-host schema qualification and a separately authorized rerun fixture.

The current persistent `chatgpt-21` host predates preview.37 and must not be used to infer projection of the two new actions. The next gate is one refreshed disposable ChatGPT fresh-host schema/guard qualification for both exact rerun names, with deterministic invalid no-write calls only.

```text
VALIDATION176=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.37-github-actions-rerun-mutations
LIVE_PUBLIC_TOOL_COUNT=153
LIVE_GITHUB_TOOL_COUNT=89
ACTIONS_RERUN_MUTATION_WIRE_SCHEMA=PASS_2_OF_2
ACTIONS_RERUN_MUTATION_FRESH_HOST_SCHEMA=PENDING
ACTIONS_RERUN_MUTATION_POSITIVE_LIVE=0_OF_2
ACTIONS_RERUN_MUTATION_OCCURRED=false
NATIVE_WRITE_ACTIONS_IMPLEMENTED=41_OF_41
NATIVE_WRITE_ACTIONS_UNIMPLEMENTED=0
NATIVE_ACTION_NAMES_IMPLEMENTED=89_OF_89
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
PR_REVIEW_MUTATION_POSITIVE_LIVE=PASS_13_OF_19
PR_REVIEW_MUTATION_UNCERTAIN_RESULTS=1
PR_REVIEW_MUTATION_REPLAY_AFTER_UNCERTAINTY=0
NEXT=FRESH_CHAT_ACTIONS_RERUN_MUTATION_SCHEMA_QUALIFICATION
```
