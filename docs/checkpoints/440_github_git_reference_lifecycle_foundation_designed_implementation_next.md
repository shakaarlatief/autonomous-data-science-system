# Checkpoint 440: GitHub Git Reference Lifecycle Foundation Designed, Implementation Next

**Date:** 2026-09-10
**Status:** PASS / FOURTH FAMILY FOUNDATION FROZEN / ONE NEW ACTION / IMPLEMENTATION NEXT / ZERO BRANCH MUTATION
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Freeze the smallest useful Git Reference Lifecycle foundation as one bounded branch-deletion action, while deferring tag lifecycle and preserving historical branches until separately classified.
**Authority:** Validation 197 owns the exact `github.delete_branch` caller contract, preflight, destructive serialization, uncertainty semantics, qualification plan, tag deferral and cleanup boundary. Validation 196 / Checkpoint 439 own fourth-family selection and the remaining-capability ranking.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-22
**Conversation title:** 22 - GitHub CI Evidence Publication and Qualification
**Primary collaborator:** ChatGPT

The fourth beyond-parity family is now frozen at its smallest useful foundation. Only one new public action is required:

```text
github.delete_branch
```

This is intentionally small because Runtime Bridge already has `github.search_branches`, `github.create_branch`, and `github.update_ref`. The missing lifecycle operation is safe deletion of one exact branch. Adding a duplicate public branch-read action would not materially improve the first foundation.

The public caller contract is exactly:

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hexadecimal string 7..64
additionalProperties  false
```

No force option, arbitrary ref namespace, default-branch override, protection/ruleset bypass, raw URL/endpoint, credential, transport, filesystem or process authority is exposed.

Runtime Bridge must resolve the installation-authorized repository, read current repository metadata to identify the default branch, read the exact branch and its current commit/protection state, reject default or protected branches, and require current head SHA to match `expected_head_sha`. Deletion is serialized by repository + branch. Inside that boundary the repository default branch and exact branch are read again and all guards are re-evaluated immediately before one fixed DELETE of `git/refs/heads/<branch>`.

A successful GitHub HTTP 204 becomes a bounded receipt containing repository, branch name, deleted head SHA, `protected=false`, and `deleted=true`. A classifiable 404/409/422 remains a definite result. Transport ambiguity after the DELETE becomes mutation uncertainty and is never automatically replayed.

Protected branches are deliberately rejected even if the GitHub App might possess policy-bypass authority. Branch cleanup and Repository Governance remain separate capability families. A lifecycle tool should not contain a hidden governance bypass.

Tag mutation remains deferred. The canonical repository currently has zero tags and no release/tag workflow, whereas the branch-deletion gap is already concrete. A future Release/Tag family should design tag/release semantics together rather than expose generic ref deletion simply for API completeness.

Positive-live tool qualification will use a newly created disposable branch rather than deleting one of the existing historical branches. The candidate branch is `r123/git-reference-delete-positive-20260910-01`, created from an exact frozen commit, read back, then deleted exactly once with that returned head SHA. No existing historical branch is part of the tool-qualification mutation fixture.

After `github.delete_branch` itself is fully qualified, actual cleanup of the currently observed historical branches is a separate repository-specific task. Branches must first be classified as disposable, still-referenced evidence, active, or unknown. Unknown branches are preserved. Therefore this checkpoint does not authorize bulk cleanup.

This also sharpens the route toward ending Research 123 rather than expanding it indefinitely. Git Reference Lifecycle is an important current operational gap. Repository Governance remains the strongest likely later family. The other candidate surfaces from Validation 196 remain recorded for future need and are not automatically scheduled.

```text
CHECKPOINT440=GITHUB_GIT_REFERENCE_LIFECYCLE_FOUNDATION_DESIGNED
FOURTH_BEYOND_PARITY_FAMILY=GIT_REFERENCE_LIFECYCLE
NEW_ACTION=github.delete_branch
DELETE_BRANCH_EXPECTED_HEAD_SHA=REQUIRED
DELETE_BRANCH_DEFAULT_BRANCH_GUARD=REQUIRED
DELETE_BRANCH_PROTECTED_BRANCH_GUARD=REQUIRED
DELETE_BRANCH_SERIALIZED_REREAD=REQUIRED
DELETE_BRANCH_ARBITRARY_REF_NAMESPACE=false
DELETE_BRANCH_FORCE_OR_POLICY_BYPASS=false
TAG_LIFECYCLE=DEFERRED
HISTORICAL_BRANCH_CLEANUP=NOT_AUTHORIZED
GITHUB_MUTATION_OCCURRED=false
AB030=PARKED_UNCHANGED
RESEARCH123=ACTIVE
NEXT=IMPLEMENT_GITHUB_DELETE_BRANCH_FOUNDATION
```
