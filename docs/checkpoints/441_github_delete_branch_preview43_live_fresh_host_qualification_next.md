# Checkpoint 441: GitHub Delete Branch Preview.43 Live, Fresh-Host Qualification Next

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.43 LIVE / LOCAL QUALIFICATION COMPLETE / FRESH-HOST SCHEMA-GUARD GATE NEXT / ZERO BRANCH DELETIONS
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve successful implementation, immutable release publication, activation, exact wire discovery and deterministic no-write qualification of `github.delete_branch`, while keeping positive branch deletion and historical cleanup unauthorized until a disposable fresh-host gate passes.
**Authority:** Validation 198 owns preview.43 implementation/publication/live-local evidence. Validation 197 / Checkpoint 440 own the frozen caller contract and destructive safety design.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-22
**Conversation title:** 22 - GitHub CI Evidence Publication and Qualification
**Primary collaborator:** ChatGPT

The fourth beyond-parity family has advanced from design to a live Runtime Bridge capability. The exact new action is:

```text
github.delete_branch
```

The active runtime is:

```text
version         0.1.1-preview.43-github-git-reference-lifecycle
surface         codexless-public-preview-v2
public tools    169
GitHub tools    105
```

The immutable release is `github-git-reference-lifecycle-v1`, bound to private local-runtime source head `7b426a4844d4d26f995fd2c4964397eb97753533` and manifest SHA-256 `859bd5e339eda29cc151359b4efd41fd11cbbf97651d64d0bef9b98b7577da4f`. Publication, restart activation and postactivation zero-mismatch verification all passed.

The exact live MCP caller contract is now independently visible from fresh stateless discovery:

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hex string 7..64
additionalProperties  false
```

Visible annotations are:

```text
readOnlyHint     false
destructiveHint  true
idempotentHint   false
openWorldHint    true
```

The implementation passed a dedicated 9/9 fake-dependency suite covering successful fake deletion, branch-name validation, default/protected branch rejection, stale expected-head rejection, state drift across the serialized destructive boundary, definite GitHub errors, and uncertain-mutation no-replay behavior.

Two real GitHub no-write guards then passed against the canonical repository. Exact current `main` was rejected with `GITHUB_DEFAULT_BRANCH_DELETE_FORBIDDEN`. Exact active development branch `v1-source-vault-bootstrap-resume` was called with deliberately stale `expected_head_sha=0000000` and rejected with `GITHUB_BRANCH_HEAD_CHANGED`. Both were non-retryable, non-uncertain failures before DELETE. Read-only postflight confirmed both branches remained at their original heads. No branch deletion occurred.

The currently open persistent `chatgpt-22` Plugin projection remains stale and does not directly project `github.delete_branch` even though the fresh stateless MCP surface proves preview.43 is live. This is the already-established host projection-refresh boundary, not a runtime qualification failure.

The next gate therefore requires one **fresh disposable ChatGPT conversation** after normal Plugin refresh/rescan. That fresh host must discover the exact `github.delete_branch` action and capture the complete host-visible schema before any positive deletion. It must then perform only deterministic invalid no-write guards.

The intended fresh-host qualification is:

```text
PART A — projection/schema

confirm exact action:
    github.delete_branch

report:
    exact action name
    title if separately visible
    complete visible description
    complete host-visible input schema
    required fields
    optional fields/defaults
    type/string/pattern/bounds/additionalProperties constraints
    annotations if separately visible
    whether any credential, token, Authorization header, GitHub host,
    arbitrary URL/endpoint, HTTP method/header, generic ref namespace,
    force flag, default/protection bypass, permission profile,
    transport, filesystem path, shell command or process authority is exposed

PART B — deterministic invalid no-write guards

1. default branch:
   repository_full_name = shakaarlatief/autonomous-data-science-system
   branch_name = main
   expected_head_sha = exact current main head read immediately beforehand
   expected result = GITHUB_DEFAULT_BRANCH_DELETE_FORBIDDEN

2. stale active-development head:
   repository_full_name = shakaarlatief/autonomous-data-science-system
   branch_name = v1-source-vault-bootstrap-resume
   expected_head_sha = 0000000
   expected result = GITHUB_BRANCH_HEAD_CHANGED

PART C — read-only postflight

confirm both branches still exist at their exact preflight heads

No positive branch deletion.
No retry or repair of a failed GitHub mutation call.
```

A protected-branch live guard remains unnecessary unless a safe already-existing protected fixture becomes available. The local 9/9 suite is sufficient for that implementation branch until Repository Governance itself creates a separately authorized protection fixture.

Only after this fresh-host gate passes may a positive-live branch deletion fixture be frozen. The positive fixture must be newly created specifically for qualification, currently proposed as:

```text
r123/git-reference-delete-positive-20260910-01
```

It must be created from a freshly frozen exact commit SHA using the already-qualified `github.create_branch`, read back, confirmed unprotected and exact-head matched, then deleted exactly once with `github.delete_branch`. Mutation uncertainty must stop the sequence without replay. Existing historical branches must not be used for this tool qualification.

After positive-live qualification, actual repository branch cleanup remains a separate task. The current historical remote branches need branch-by-branch classification before any deletion. Unknown branches are preserved. That cleanup should happen only if it materially helps close Research 123; it is not a prerequisite to proving the action itself works.

Once Git Reference Lifecycle closes, Research 123 should perform one final value decision around Repository Governance. The current intent is **not** to continue adding every available GitHub API. Repository Governance should be implemented only to the smallest useful protection foundation if the evidence shows it is materially important for ADS. Releases/tags, Security Findings, Deployments/Environments/Variables, Codespaces, Pages, Packages, Discussions, Projects, Agent tasks, organization/team administration and other optional surfaces remain recorded for later need. Secret-value and webhook-management authority remain deferred. AB-030 remains parked unchanged.

```text
CHECKPOINT441=GITHUB_DELETE_BRANCH_PREVIEW43_LIVE
GIT_REFERENCE_LIFECYCLE_IMPLEMENTATION=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.43-github-git-reference-lifecycle
LIVE_PUBLIC_TOOL_COUNT=169
LIVE_GITHUB_TOOL_COUNT=105
GITHUB_DELETE_BRANCH_WIRE_SCHEMA=PASS_1_OF_1
GITHUB_DELETE_BRANCH_LOCAL_TESTS=PASS_9_OF_9
GITHUB_DELETE_BRANCH_LOCAL_LIVE_NO_WRITE_GUARDS=PASS_2_OF_2
GITHUB_DELETE_BRANCH_POSITIVE_WRITES=0_OF_1
GITHUB_DELETE_BRANCH_MUTATION_RETRIES=0
GITHUB_DELETE_BRANCH_MUTATION_UNCERTAIN_RESULTS=0
HISTORICAL_BRANCH_CLEANUP=NOT_AUTHORIZED
TAG_LIFECYCLE=DEFERRED
AB030=PARKED_UNCHANGED
RESEARCH123=ACTIVE
NEXT=FRESH_HOST_GITHUB_DELETE_BRANCH_SCHEMA_GUARD_QUALIFICATION
```