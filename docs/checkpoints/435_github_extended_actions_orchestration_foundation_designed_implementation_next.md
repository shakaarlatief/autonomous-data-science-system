# Checkpoint 435: Extended GitHub Actions Orchestration Foundation Designed, Implementation Next

**Date:** 2026-09-10
**Status:** PASS / THIRD BEYOND-PARITY FAMILY FROZEN / SIX ACTIONS / NO ACTIONS MUTATION
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Freeze the third beyond-parity GitHub extension family as bounded Actions workflow/run orchestration: workflow discovery, exact workflow/run reads, manual dispatch, whole-run rerun and ordinary cancellation.
**Authority:** Validation 192 owns family selection, the six caller contracts, optimistic-concurrency guards, mutation semantics and explicit deferrals. Checkpoint 434 remains authoritative for completion of CI Evidence Publication. AB-030 remains a separate parked integration idea.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-22
**Conversation title:** 22 - GitHub CI Evidence Publication and Qualification
**Primary collaborator:** ChatGPT

The third beyond-parity GitHub family is frozen as **GitHub Actions Orchestration**. It contains exactly six new actions:

```text
github.list_repository_workflows
github.get_workflow
github.get_workflow_run
github.dispatch_workflow
github.rerun_workflow_run
github.cancel_workflow_run
```

The selection is strongly supported by the current ADS repository and live GitHub App. The repository contains 34 workflow files, 27 of which declare `workflow_dispatch`. The live App installation reports `Actions=write` and `Workflows=write`; current GitHub REST documentation requires only Actions read/write for the selected operations, so no App permission change is needed.

The family deliberately adds the missing orchestration layer around the already-implemented native Actions inspection and partial-rerun surface. `list_repository_workflows`, `get_workflow`, and `get_workflow_run` establish exact object identity. `dispatch_workflow` launches an exact numeric workflow ID on an explicit branch/tag and requires `expected_ref_sha` so a movable ref cannot silently change between inspection and dispatch. Optional dispatch inputs use a strict maximum-25 entry array, primitive values only, unique names and the current 65,535-character GitHub payload ceiling rather than exposing an arbitrary nested object.

Whole-run rerun and cancellation are similarly concurrency-bound. Both require the exact workflow run ID plus expected head SHA and expected run attempt. Rerun requires a completed run, leaves raw debug logging disabled in the first slice, and never attempts to bypass GitHub's rerun eligibility policy. Cancel rejects an already completed run, treats HTTP 202 as request acceptance rather than proof of final cancelled state, preserves 409 state races as definite, and never silently escalates to force-cancel.

The mutation rule remains the established Runtime Bridge pattern: installation-authorized preflight, smallest stable serialization key, exact reread/revalidation inside the mutation boundary, one fixed GitHub mutation request, no automatic replay after mutation uncertainty, then read-only reconciliation through `get_workflow_run` where needed.

Several adjacent Actions powers remain intentionally outside the foundation. Force-cancel is a separate recovery/escalation concern because GitHub says to use it only when normal cancellation is not responding. Enable/disable changes persistent workflow activation policy. Run/log/artifact/cache deletion is destructive evidence/storage lifecycle. Fork-run approval is a trust decision. Deployment approvals belong with Deployments/Environments. `repository_dispatch` is a broader custom event/client-payload surface. Workflow YAML editing remains repository-content mutation. Actions policy/default-permission changes remain administration/policy work.

Current GitHub API `2026-03-10` gives one especially useful improvement for the dispatch design: the workflow-dispatch endpoint returns HTTP 200 with the exact new `workflow_run_id` and run URLs. Runtime Bridge can therefore bind a successful dispatch directly to the created run instead of heuristically searching recent runs after mutation.

The current repository already contains promising future qualification fixtures. `Repository integrity` and `Knowledge map integrity` both support `workflow_dispatch` and declare `permissions: contents: read`. No workflow mutation is authorized by this checkpoint. Positive dispatch/rerun/cancel testing remains behind implementation, fresh-host qualification, and a separately frozen owner-authorized safe fixture.

AB-030 remains parked exactly as requested. This Actions Orchestration family expands GitHub capability breadth; it does not start the later workflow that publishes ADS validation evidence through the CI Evidence primitive.

```text
CHECKPOINT435=GITHUB_EXTENDED_ACTIONS_ORCHESTRATION_FOUNDATION_DESIGNED
THIRD_BEYOND_PARITY_FAMILY=GITHUB_ACTIONS_ORCHESTRATION
ACTIONS_ORCHESTRATION_FOUNDATION_ACTIONS=6
ACTIONS_ORCHESTRATION_READS=3
ACTIONS_ORCHESTRATION_WRITES=3
LIVE_ACTIONS_PERMISSION=WRITE_CONFIRMED
REPOSITORY_WORKFLOW_FILES=34
REPOSITORY_WORKFLOW_DISPATCH_FILES=27
DISPATCH_EXPECTED_REF_SHA_GUARD=REQUIRED
RERUN_EXPECTED_HEAD_SHA_GUARD=REQUIRED
RERUN_EXPECTED_RUN_ATTEMPT_GUARD=REQUIRED
CANCEL_EXPECTED_HEAD_SHA_GUARD=REQUIRED
CANCEL_EXPECTED_RUN_ATTEMPT_GUARD=REQUIRED
FORCE_CANCEL=DEFERRED
WORKFLOW_ENABLE_DISABLE=DEFERRED
REPOSITORY_DISPATCH=DEFERRED
AB030=PARKED_UNCHANGED
ACTIONS_ORCHESTRATION_MUTATION_OCCURRED=false
RESEARCH123=ACTIVE
NEXT=IMPLEMENT_EXTENDED_GITHUB_ACTIONS_ORCHESTRATION_FOUNDATION
```
