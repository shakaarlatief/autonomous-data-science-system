# Validation 201: Repository Governance Value Decision and Branch-Safety Design

**Date:** 2026-09-10
**Status:** PASS / FINAL IMPORTANT GITHUB FAMILY SELECTED / BRANCH-SAFETY FOUNDATION FROZEN / ZERO GOVERNANCE MUTATION
**Research:** Research 123

## 1. Decision question

Checkpoint 443 completed Git Reference Lifecycle as the fourth beyond-parity GitHub family. The remaining question is intentionally narrow: does Repository Governance materially improve ADS enough to justify one final GitHub extension family before Research 123 closes, or should all remaining GitHub APIs stay deferred?

The answer is **yes, but only for a minimal branch-safety foundation**. Full required-review, required-status-check, merge-queue, signed-commit, deployment, ruleset, organization, and security-policy administration is not justified now.

## 2. Current repository evidence

Read-only GitHub inspection on 2026-09-10 confirms:

```text
repository rulesets                 0
main branch protection              absent
v1-frontend-spike protection        absent
GitHub App Administration permission write
```

The repository development model makes the distinction important:

```text
main                     default/control-plane branch that intentionally trails V1 work
v1-frontend-spike        promoted integration branch
v1-source-vault-bootstrap-resume current development/continuity branch
```

The promoted integration branch is a durable accepted-state boundary. Many workflows explicitly target `v1-frontend-spike`. At least one maintained workflow, `.github/workflows/refresh-frontend-visual-baselines.yml`, performs an ordinary `git push origin HEAD:v1-frontend-spike`, so a governance design that suddenly requires every update to arrive through a pull request or required-status-check merge would disrupt an existing project workflow.

The correct current protection goal is therefore narrower:

```text
allow ordinary fast-forward updates
block force pushes
block branch deletion
apply the restrictions to repository administrators as well
```

This adds GitHub-side defense against destructive branch-history/ref operations without replacing the existing ADS validation and promotion process.

## 3. Why classic branch protection is selected over a broad ruleset family

GitHub rulesets are more expressive and can layer multiple policies, but that flexibility is not currently needed. A broad ruleset mutation surface would introduce targeting expressions, bypass actors, enforcement states, required workflows/checks, merge methods, metadata restrictions, and other policy dimensions that ADS does not currently need.

Classic exact-branch protection is sufficient for the present requirement and is available for this public repository. Current GitHub documentation states that protected branches can block deletion and force pushes; `Update branch protection` requires `Administration(write)` for GitHub App tokens. The installed App already has that permission.

The fixed REST resources used by this foundation are:

```text
GET    /repos/{owner}/{repo}/branches/{branch}
GET    /repos/{owner}/{repo}/branches/{branch}/protection
PUT    /repos/{owner}/{repo}/branches/{branch}/protection
DELETE /repos/{owner}/{repo}/branches/{branch}/protection
```

Current GitHub REST documentation uses API version `2026-03-10`.

Official source:

```text
https://docs.github.com/en/rest/branches/branch-protection
```

## 4. Selected fifth and final important family

The selected family is:

```text
Repository Branch-Safety Governance
```

It contains exactly three new public actions:

```text
github.get_branch_protection
github.create_branch_safety_protection
github.delete_branch_safety_protection
```

This is intended to be the final important GitHub extension family for the current ADS stage. Other GitHub capability families remain recorded for future need but are not scheduled now.

## 5. Fixed Codexless branch-safety baseline

`github.create_branch_safety_protection` does **not** expose GitHub's general branch-protection body. Runtime Bridge owns one exact baseline:

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

Meaning:

```text
ordinary fast-forward direct pushes remain allowed
pull requests are not required by this baseline
status checks are not made merge requirements by this baseline
administrators do not bypass the configured protection
force pushes are blocked
branch deletion is blocked
branch is not locked/read-only
```

The profile identifier used internally and in normalized receipts is:

```text
codexless.branch-safety-baseline.v1
```

No caller can alter any baseline field.

## 6. Read action contract

### `github.get_branch_protection`

Caller fields:

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
additionalProperties  false
```

Runtime Bridge:

```text
1. resolves installation-authorized repository scope;
2. validates bounded branch name;
3. reads the exact branch and current head SHA;
4. reads exact branch protection;
5. normalizes protection absence (GitHub 404 after successful exact branch read) as protected=false;
6. when protected, returns only bounded policy fields needed to audit this foundation;
7. reports whether the protection exactly matches the Codexless branch-safety baseline.
```

Normalized result:

```text
repositoryFullName
branchName
headSha
protected
codexlessSafetyBaseline
profileId|null
policy|null
```

## 7. Create action contract

### `github.create_branch_safety_protection`

Caller fields:

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hexadecimal string 7..64
additionalProperties  false
```

The action is deliberately **create-only**, even though GitHub's raw endpoint is PUT/create-or-replace. It must reject any branch that is already protected instead of overwriting unknown protection policy.

Preflight:

```text
resolve installation-authorized repository
read exact branch
require current head matches expected_head_sha
GET exact current protection
require protection absent
```

If protection already exists:

```text
GITHUB_BRANCH_PROTECTION_ALREADY_PRESENT
```

Deletion/force/review/check settings are not caller-selectable.

## 8. Serialized create boundary

Create is serialized by:

```text
repository_full_name + branch_name
```

Inside the serialized boundary Runtime Bridge repeats:

```text
exact branch read
expected-head check
exact protection read
require protection still absent
```

Only then may it dispatch one fixed PUT containing the server-owned baseline body.

After a 200 response Runtime Bridge normalizes the returned protection and requires it to exactly equal the baseline. An unexpected post-write policy shape must be fail-visible and treated as a state requiring read-only reconciliation rather than silently accepted.

No automatic replay occurs after mutation uncertainty.

## 9. Delete action contract

### `github.delete_branch_safety_protection`

Caller fields:

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hexadecimal string 7..64
additionalProperties  false
```

This is **not** a generic delete-any-protection action.

Before DELETE Runtime Bridge must:

```text
resolve installation-authorized repository
read exact branch
require expected head SHA
read exact protection
require protection exists
require protection exactly matches codexless.branch-safety-baseline.v1
```

If protection is absent:

```text
GITHUB_BRANCH_SAFETY_PROTECTION_NOT_FOUND
```

If protection exists but differs from the Codexless baseline:

```text
GITHUB_BRANCH_PROTECTION_POLICY_CHANGED
```

That prevents this tool from destroying a protection policy created or strengthened outside Runtime Bridge.

The action serializes by repository + branch and repeats branch-head and exact-baseline checks immediately before one fixed DELETE.

A successful HTTP 204 becomes a bounded removal receipt. Uncertain deletion is never automatically replayed.

## 10. Branch and SHA validation

Branch-name validation reuses the established Runtime Bridge branch rules from Git Reference Lifecycle. Caller branch names cannot select wildcard patterns or another Git ref namespace.

`expected_head_sha` uses the established 7..64 hexadecimal optimistic-concurrency rule. A short caller SHA is accepted only when it is a prefix of GitHub's full branch-head SHA.

## 11. Authority explicitly not exposed

None of the three actions exposes:

```text
GitHub credential/token
Authorization header
GitHub host
arbitrary URL/endpoint
HTTP method/header
GraphQL document
branch wildcard/pattern
ruleset target expression
status-check name
required-review count
bypass actor
force-push allowance
deletion allowance
admin-bypass toggle
push restriction
merge queue
required deployment
commit-signature rule
lock/read-only toggle
permission profile
transport
filesystem path
shell/process authority
```

## 12. Qualification plan

### Fake-dependency implementation tests

At minimum:

```text
exact three-action declaration
unprotected read normalization
baseline-protected read normalization
create on unprotected exact-head branch
already-protected create guard
stale-head create guard
state drift during serialized create revalidation
post-write baseline verification
remove exact baseline protection
remove-absent guard
remove-nonbaseline guard
stale-head remove guard
state drift during serialized remove revalidation
definite 403/404/422 mapping
mutation uncertainty after exactly one PUT/DELETE and zero replay
```

### Local-live non-writing qualification

Use canonical repository reads to prove:

```text
main currently unprotected
v1-frontend-spike currently unprotected
stale expected-head create guard fails before PUT
remove-absent guard fails before DELETE
```

No positive protection mutation is required before fresh-host qualification.

### Fresh-host qualification

A fresh disposable ChatGPT host must project all three new actions with bounded contracts, run positive reads on `main` and `v1-frontend-spike`, and exercise deterministic invalid no-write guards only.

### Positive-live qualification

Use a new disposable branch, not `main` or `v1-frontend-spike`:

```text
r123/branch-safety-governance-positive-20260910-01
```

Sequence:

```text
create disposable branch at exact frozen commit
get protection -> protected=false
create branch-safety protection exactly once
get protection -> exact baseline, protected=true
remove branch-safety protection exactly once
get protection -> protected=false
delete disposable branch exactly once with github.delete_branch
confirm branch absent
```

No positive mutation to `main` or `v1-frontend-spike` is part of capability qualification.

## 13. Permanent canonical protection is a separate final authorization

After the tool family itself is qualified, the project should freeze current exact SHAs for:

```text
main
v1-frontend-spike
```

and propose applying the same minimal baseline to both branches.

That permanent repository-policy mutation requires explicit owner authorization because it changes GitHub's enforcement behavior on durable project branches.

The baseline is deliberately chosen to preserve current direct fast-forward workflows while preventing destructive force-push/deletion behavior.

## 14. Other GitHub capabilities remain deferred

The value review does not reopen the broader extension catalog. These remain documented for another stage if a concrete need appears:

```text
Release/Tag Management
Security Findings
Deployments/Environments/Variables
Codespaces
Pages
Packages
Discussions
Projects
GitHub Agent Tasks / Copilot cloud agent
organization/team administration
other optional GitHub surfaces
```

Secret-value and webhook-management authority remain deliberately excluded/deferred.

AB-030 remains parked unchanged.

## 15. Disposition

```text
VALIDATION201=PASS
REPOSITORY_GOVERNANCE_VALUE_DECISION=BUILD_MINIMAL_BRANCH_SAFETY
FIFTH_BEYOND_PARITY_FAMILY=REPOSITORY_BRANCH_SAFETY_GOVERNANCE
FIFTH_FAMILY_ACTIONS=3
GET_BRANCH_PROTECTION=github.get_branch_protection
CREATE_BRANCH_SAFETY_PROTECTION=github.create_branch_safety_protection
DELETE_BRANCH_SAFETY_PROTECTION=github.delete_branch_safety_protection
BRANCH_SAFETY_PROFILE=codexless.branch-safety-baseline.v1
BLOCK_FORCE_PUSHES=true
BLOCK_DELETIONS=true
ENFORCE_ADMINS=true
REQUIRE_PULL_REQUESTS=false
REQUIRE_STATUS_CHECKS=false
LOCK_BRANCH=false
MAIN_CURRENTLY_PROTECTED=false
PROMOTED_INTEGRATION_CURRENTLY_PROTECTED=false
CANONICAL_PROTECTION_MUTATION_AUTHORIZED=false
GITHUB_GOVERNANCE_MUTATION_OCCURRED=false
AB030=PARKED_UNCHANGED
NEXT=IMPLEMENT_REPOSITORY_BRANCH_SAFETY_GOVERNANCE_FOUNDATION
```
