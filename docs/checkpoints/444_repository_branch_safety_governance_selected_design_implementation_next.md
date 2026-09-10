# Checkpoint 444: Repository Branch-Safety Governance Selected, Implementation Next

**Date:** 2026-09-10
**Status:** PASS / FINAL IMPORTANT GITHUB FAMILY SELECTED / THREE-ACTION FOUNDATION FROZEN / IMPLEMENTATION NEXT
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve the final Repository Governance value decision and freeze the smallest useful branch-safety foundation without changing canonical branch protection.
**Authority:** Validation 201 owns the value decision, exact three-action design, fixed branch-safety baseline, qualification plan, and permanent-protection authorization boundary. Checkpoint 443 remains authoritative for completion of Git Reference Lifecycle.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-22
**Conversation title:** 22 - GitHub CI Evidence Publication and Qualification
**Primary collaborator:** ChatGPT

The final Repository Governance value decision is complete. Repository Governance is important enough to build, but only as a deliberately narrow **Repository Branch-Safety Governance** family. It is intended to be the final important GitHub extension family for the current ADS stage.

Current GitHub state remains:

```text
repository rulesets          none
main protection              absent
v1-frontend-spike protection absent
Administration permission    write
```

The project does not currently need a broad policy engine. In particular, `v1-frontend-spike` remains the promoted integration branch and maintained workflows still include an ordinary direct fast-forward push to that branch. Requiring PR-only updates or mandatory status-check gates at GitHub enforcement level now would risk breaking an existing project workflow.

The useful present policy is therefore exactly:

```text
ordinary fast-forward pushes allowed
force pushes blocked
branch deletion blocked
protection enforced for administrators
no required PR reviews
no required status checks
branch not locked
```

The foundation contains exactly three new actions:

```text
github.get_branch_protection
github.create_branch_safety_protection
github.delete_branch_safety_protection
```

The create/delete actions expose only repository, exact branch name, and expected branch-head SHA. They do not expose GitHub's general branch-protection policy body. Runtime Bridge owns one fixed internal profile:

```text
codexless.branch-safety-baseline.v1
```

with:

```text
required_status_checks           null
enforce_admins                   true
required_pull_request_reviews    null
restrictions                     null
required_linear_history          false
allow_force_pushes               false
allow_deletions                  false
block_creations                  false
required_conversation_resolution false
lock_branch                      false
allow_fork_syncing               false
```

`github.create_branch_safety_protection` is create-only at the semantic layer. If any protection already exists, Runtime Bridge rejects rather than overwriting it. This avoids clobbering a stronger or externally managed policy even though GitHub's raw endpoint is PUT/create-or-replace.

`github.delete_branch_safety_protection` may remove protection only when the current protection exactly matches the Codexless baseline. Any stronger or externally changed policy fails closed with `GITHUB_BRANCH_PROTECTION_POLICY_CHANGED`. This prevents the cleanup action from becoming generic branch-protection deletion authority.

Both mutations use exact branch-head optimistic concurrency, serialize by repository + branch, repeat branch/head/protection checks immediately before one fixed mutation, and never automatically replay uncertain results.

Positive capability qualification will use a newly created disposable branch:

```text
r123/branch-safety-governance-positive-20260910-01
```

The fixture will be created at a freshly frozen exact public commit, read as unprotected, protected with the fixed baseline, read back as the exact baseline, have only that exact baseline removed, be read back as unprotected, and finally be deleted with the already qualified `github.delete_branch` action. Neither `main` nor `v1-frontend-spike` will be mutated merely to qualify the tools.

After the family itself is fully qualified, applying the baseline permanently to `main` and `v1-frontend-spike` remains a separate final owner-authorization gate. Their exact current head SHAs must be re-read immediately before any permanent policy mutation.

Other GitHub surfaces remain recorded but are not scheduled now. This family is intended to close the set of important GitHub extensions needed before the user-defined next ADS stage. AB-030 remains parked unchanged.

```text
CHECKPOINT444=REPOSITORY_BRANCH_SAFETY_GOVERNANCE_SELECTED
COMPLETED_BEYOND_PARITY_FAMILIES=4
FIFTH_BEYOND_PARITY_FAMILY=REPOSITORY_BRANCH_SAFETY_GOVERNANCE
FIFTH_FAMILY_ACTIONS=3
BRANCH_SAFETY_PROFILE=codexless.branch-safety-baseline.v1
BLOCK_FORCE_PUSHES=true
BLOCK_DELETIONS=true
ENFORCE_ADMINS=true
REQUIRE_PULL_REQUESTS=false
REQUIRE_STATUS_CHECKS=false
CANONICAL_MAIN_PROTECTION_MUTATION=NOT_AUTHORIZED
CANONICAL_INTEGRATION_PROTECTION_MUTATION=NOT_AUTHORIZED
GITHUB_GOVERNANCE_MUTATION_OCCURRED=false
AB030=PARKED_UNCHANGED
RESEARCH123=ACTIVE
NEXT=IMPLEMENT_REPOSITORY_BRANCH_SAFETY_GOVERNANCE_FOUNDATION
```
