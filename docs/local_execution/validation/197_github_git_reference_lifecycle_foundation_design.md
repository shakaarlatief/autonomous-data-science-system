# Validation 197: GitHub Git Reference Lifecycle Foundation Design

**Date:** 2026-09-10
**Status:** PASS / FOURTH BEYOND-PARITY FOUNDATION FROZEN / ONE NEW WRITE ACTION / NO BRANCH MUTATION
**Research:** Research 123

## 1. Purpose

Validation 196 / Checkpoint 439 selected **Git Reference Lifecycle** as the fourth beyond-parity GitHub family because branch cleanup is an actual current lifecycle gap. The repository can already create branches through `github.create_branch`, search them through `github.search_branches`, and move them through `github.update_ref`, but Runtime Bridge still cannot delete a completed/disposable branch through a bounded semantic action.

The smallest coherent first foundation is therefore deliberately only one new action:

```text
github.delete_branch
```

No new tag action is included. Tag lifecycle remains deferred because the canonical repository currently has zero tags and no concrete tag/release workflow, while branch cleanup is already needed.

No branch is deleted by this design validation.

## 2. Current official GitHub behavior

Current GitHub REST documentation for API version `2026-03-10` exposes:

```text
DELETE /repos/{owner}/{repo}/git/refs/{ref}
```

For GitHub App user or installation access tokens, the endpoint requires:

```text
Contents(write)
```

The live Runtime Bridge GitHub App already has `Contents=write`, so this foundation requires no permission change.

Documented response semantics include:

```text
204  successful deletion
409  conflict
422  validation failure, including an attempt to delete the default branch
```

The raw endpoint accepts a generic Git reference. Runtime Bridge will **not** expose that generic namespace. The new action is branches-only and server-constructs `heads/<branch>`.

Official source:

```text
https://docs.github.com/en/rest/git/refs
```

## 3. Why one new action is sufficient

Runtime Bridge already provides the other branch-lifecycle primitives needed around deletion:

```text
github.search_branches  read branch names, commit SHA and protected flag
github.create_branch    create refs/heads/<branch>
github.update_ref       move refs/heads/<branch>, force=false only
```

Adding another public exact-branch read is not required for the first foundation merely to support deletion. `github.delete_branch` itself must perform fixed exact server-owned reads before deletion, while callers can use the already-qualified `github.search_branches` for discovery and postflight absence checks.

The resulting practical lifecycle is:

```text
discover branch
    -> create branch
    -> move branch safely
    -> use branch in PR/development workflows
    -> delete branch safely when explicitly authorized
```

This keeps the extension surface minimal rather than duplicating already useful read functionality.

## 4. Public caller contract

The frozen caller contract is:

```text
github.delete_branch

repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hexadecimal string 7..64
additionalProperties  false
```

No optional field is needed.

The action deliberately exposes no:

```text
force flag
ref namespace
raw `refs/...` selector
default-branch override
protected-branch override
ruleset bypass
GitHub host
URL or endpoint
HTTP method/header
API version
credential/token
Authorization header
permission profile
transport
filesystem path
shell/process authority
```

## 5. Branch-name validation

`branch_name` uses the existing Runtime Bridge bounded branch-name rules already applied to `create_branch` and `update_ref`:

```text
non-empty
maximum 512 characters
no CR/LF/NUL
must not begin or end with `/`
must not end with `.`
must not contain `..`
must not contain `@{`
must not contain whitespace
must not contain ~ ^ : ? * [ or backslash
no empty path segment
no segment ending in `.lock`
```

The caller supplies only the branch name, for example:

```text
r123/branch-delete-positive-20260910-01
```

Runtime Bridge constructs and encodes the fixed Git reference itself:

```text
heads/r123/branch-delete-positive-20260910-01
```

A caller cannot redirect deletion into `refs/tags`, `refs/notes`, or another Git namespace.

## 6. Exact server-owned preflight

Before mutation, Runtime Bridge must perform all of the following fixed reads:

### 6.1 Installation-authorized repository resolution

Resolve the caller's `repository_full_name` through existing installation-derived authority. No repository outside current GitHub App scope is eligible.

### 6.2 Repository metadata read

Read the exact repository through GitHub's fixed repository endpoint and obtain the current `default_branch`.

If the requested branch name equals the current default branch, reject locally with a definite no-write error before DELETE:

```text
GITHUB_DEFAULT_BRANCH_DELETE_FORBIDDEN
```

GitHub itself also rejects default-branch deletion, but local preflight makes the Runtime Bridge contract explicit and avoids deliberately sending a known-invalid destructive request.

### 6.3 Exact branch read

Read:

```text
GET /repos/{owner}/{repo}/branches/{branch}
```

and require a well-formed exact branch response containing at least:

```text
name
commit.sha
protected
```

The returned branch name must equal the requested branch name exactly after normal GitHub name handling. The current commit SHA is the authoritative deletion target identity.

### 6.4 Expected-head optimistic concurrency

Require the actual branch head SHA to match `expected_head_sha` using the established Runtime Bridge GitHub-SHA rule: a caller may provide a 7..64 hexadecimal object identifier, and a shorter expected SHA is accepted only when it is a prefix of GitHub's full returned SHA.

A mismatch rejects before mutation with:

```text
GITHUB_BRANCH_HEAD_CHANGED
```

This prevents deleting a branch that has moved since the caller inspected it.

### 6.5 Protected branch fail-closed rule

If GitHub's branch response reports:

```text
protected = true
```

reject locally before DELETE with:

```text
GITHUB_PROTECTED_BRANCH_DELETE_FORBIDDEN
```

The first foundation intentionally does not expose a caller override. A branch can be protected by classic branch protection or a ruleset, and bypassing that policy is not ordinary lifecycle cleanup. Repository Governance remains a separate future family.

This is stricter than merely relying on GitHub to decide whether the authenticated App can bypass deletion protection.

## 7. Serialized mutation boundary

Deletion is serialized on the smallest stable destructive-object key:

```text
repository_full_name + branch_name
```

Inside that serialization boundary Runtime Bridge must repeat the relevant state checks immediately before mutation:

```text
1. re-read repository default branch;
2. reject if target has become the default branch;
3. re-read exact branch;
4. require the same expected head SHA;
5. require protected=false;
6. only then dispatch one fixed DELETE request.
```

This second read closes ordinary time-of-check/time-of-use drift between the outer preflight and destructive request.

## 8. Fixed mutation

The only mutation request is:

```text
DELETE /repos/{owner}/{repo}/git/refs/heads/{encoded_branch_name}
```

No request body is needed.

A successful HTTP 204 is normalized to a bounded receipt:

```text
schemaVersion
repositoryFullName
branchName
deletedHeadSha
protected       false
deleted         true
```

The receipt proves only that GitHub accepted the exact reference deletion. The commit object itself is not deleted because Git objects are immutable/reachable independently of one branch ref.

## 9. Error and uncertainty semantics

Classifiable GitHub responses remain definite. Important examples:

```text
404 branch/reference no longer exists
409 GitHub conflict
422 GitHub validation/policy failure
```

A branch disappearing before mutation should not be converted into success merely because the desired end state happens to be absence. This action qualifies one exact deletion operation against one exact expected branch identity. If the branch disappears after preflight but before DELETE, the operation fails definitely rather than pretending this invocation deleted it.

The established mutation rule applies:

```text
one underlying DELETE dispatch maximum
no automatic retry after mutation dispatch
transport ambiguity after dispatch -> mutationUncertain=true
mutationUncertain=true -> caller must reconcile read-only before considering any new mutation
```

Because a successful DELETE returns no body, transport failure after dispatch is especially important: the branch may already be gone. Runtime Bridge must never replay that uncertain DELETE automatically.

## 10. Qualification plan

Implementation and activation should use the same layered evidence process as the previous beyond-parity families.

### Local implementation qualification

At minimum test:

```text
wire schema strictness
branch-name rejection
installation-authorized repository binding
default-branch local rejection
protected-branch local rejection
stale expected-head rejection
exact reread inside serialization boundary
state drift between preflight and mutation rejection
one successful fake DELETE 204 normalization
404 / 409 / 422 definite error mapping
mutation uncertainty after exactly one DELETE dispatch
zero automatic replay
```

### Local live non-writing qualification

Use real GitHub state only for:

```text
search/read existing branch identities
invalid default-branch deletion guard
invalid stale-head deletion guard
invalid protected-branch guard only if a safe protected fixture exists
```

No positive branch deletion is required before fresh-host projection qualification.

### Fresh-host qualification

Require the exact new action to project with the bounded three-field schema and exercise deterministic invalid no-write guards. No existing project branch should be deleted in this gate.

### Positive-live qualification

The safest positive fixture is not one of the 59 historical branches. Create a new disposable qualification branch from an exact known commit using the already-qualified `github.create_branch`, read it back through `github.search_branches`, then delete exactly that branch with the returned exact head SHA.

Candidate branch name:

```text
r123/git-reference-delete-positive-20260910-01
```

The exact source commit must be frozen immediately before creation. Positive-live execution must then be:

```text
create disposable branch once
read exact branch once
require protected=false and exact source SHA
delete exact branch once
stop on mutation uncertainty, never replay
read-only confirm exact branch no longer appears
```

This creates no repository content or commit object; it adds then removes only one disposable ref. Existing historical branches remain untouched during tool qualification.

## 11. Historical branch cleanup is separate

Completion of `github.delete_branch` does not automatically authorize deletion of the currently observed 59 remote branches.

After the tool itself is qualified, actual repository cleanup should use a separate read-only branch classification that distinguishes, for example:

```text
known disposable qualification branch
merged historical development branch
still-referenced evidence branch
active/in-use branch
unknown branch requiring preservation
```

Only branches positively classified as disposable should be proposed for deletion. Unknowns fail closed.

This prevents a capability qualification from becoming an implicit bulk-cleanup operation.

## 12. Tag lifecycle disposition

Tag lifecycle remains deferred from this foundation.

Reasons:

```text
canonical repository currently has zero tags
no active release/tag workflow exists
branch deletion solves a current known lifecycle gap
tag deletion can destroy a version/release reference and deserves its own release semantics
```

If Release/Tag Management becomes useful later, tags should be designed with release-object relationships and versioning policy rather than simply exposing generic Git-ref deletion.

## 13. Relationship to Repository Governance

The protected-branch fail-closed rule intentionally preserves the boundary between lifecycle and policy:

```text
Git Reference Lifecycle
    delete one explicitly selected unprotected non-default branch at an exact expected SHA

Repository Governance
    create/update rulesets, branch protection, required checks/reviews and related durable policy
```

`github.delete_branch` must never acquire a `bypass_protection=true` style escape hatch as a convenience. Any future governance change is a separate explicitly authorized policy mutation.

## 14. Disposition

```text
VALIDATION197=PASS
FOURTH_BEYOND_PARITY_FAMILY=GIT_REFERENCE_LIFECYCLE
GIT_REFERENCE_LIFECYCLE_NEW_ACTIONS=1
GIT_REFERENCE_LIFECYCLE_ACTION=github.delete_branch
DELETE_BRANCH_REQUIRED_FIELDS=repository_full_name,branch_name,expected_head_sha
DELETE_BRANCH_DEFAULT_BRANCH_REJECTION=REQUIRED
DELETE_BRANCH_PROTECTED_BRANCH_REJECTION=REQUIRED
DELETE_BRANCH_STALE_HEAD_GUARD=REQUIRED
DELETE_BRANCH_SERIALIZED_REREAD=REQUIRED
DELETE_BRANCH_FORCE_OVERRIDE=NOT_EXPOSED
DELETE_BRANCH_REF_NAMESPACE=SERVER_OWNED_HEADS_ONLY
DELETE_BRANCH_MUTATION_REPLAY=FORBIDDEN_AFTER_UNCERTAINTY
TAG_LIFECYCLE=DEFERRED_TO_RELEASE_TAG_FAMILY
HISTORICAL_BRANCH_CLEANUP=NOT_AUTHORIZED
GITHUB_MUTATION_OCCURRED=false
AB030=PARKED_UNCHANGED
NEXT=IMPLEMENT_GITHUB_DELETE_BRANCH_FOUNDATION
```
