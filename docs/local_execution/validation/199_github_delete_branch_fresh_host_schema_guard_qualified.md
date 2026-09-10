# Validation 199: GitHub Delete Branch Fresh-Host Schema and Guard Qualification

**Date:** 2026-09-10
**Status:** PASS / FRESH-HOST PROJECTION + BOUNDED CONTRACT + TWO NO-WRITE GUARDS / ZERO BRANCH MUTATION
**Research:** Research 123

## 1. Fresh-host projection

The owner supplied the result of a disposable fresh ChatGPT-host qualification after preview.43 activation.

Exact projected action:

```text
github.delete_branch
```

The host-visible caller contract contained exactly the three required fields:

```text
repository_full_name
branch_name
expected_head_sha
```

Visible machine-readable constraints were:

```text
repository_full_name  string  minLength=3  maxLength=512
branch_name           string  minLength=1  maxLength=512
expected_head_sha     string  minLength=7  maxLength=64  pattern=^[0-9a-fA-F]+$
```

No optional fields/defaults were visible. The fresh host did not visibly expose a separate `additionalProperties` constraint or separate annotations, so this validation does not infer them from local MCP evidence.

The projected contract exposed no caller-selected credential/token, Authorization header, GitHub host, arbitrary URL/endpoint, HTTP method/header, GraphQL document, generic Git ref namespace, force flag, default-branch override, protected-branch/ruleset bypass, permission profile, transport, filesystem path, shell command, or process authority.

The description separately stated semantic protections for exact current-head validation, default/protected branch rejection, repeated destructive-boundary checks, server-owned `refs/heads/<branch>` construction, and no automatic retry after uncertain deletion.

## 2. Read-only preflight

The fresh host read the exact canonical repository branches before any guard call:

```text
main
    sha        3c7bcc51b10bfac787aee4b12cc3cd0f6b553400
    protected  false

v1-source-vault-bootstrap-resume
    sha        058a7cf28d2ba5adc5d8cffb9d5b65a14f9dd19e
    protected  false
```

## 3. Exactly two invalid no-write guards

### Default-branch guard

Input used the exact current `main` SHA and returned:

```text
errorCode          GITHUB_DEFAULT_BRANCH_DELETE_FORBIDDEN
retryable          false
mutationUncertain  false
```

No retry was made.

### Stale-head guard

Input targeted `v1-source-vault-bootstrap-resume` with deliberately stale:

```text
expected_head_sha  0000000
```

and returned:

```text
errorCode          GITHUB_BRANCH_HEAD_CHANGED
retryable          false
mutationUncertain  false
```

No retry was made.

Exactly two `github.delete_branch` calls occurred, both deterministic failures before the positive branch-deletion mutation.

## 4. Read-only postflight

The fresh host re-read both branches and observed exactly the preflight state:

```text
main
    3c7bcc51b10bfac787aee4b12cc3cd0f6b553400
    protected=false

v1-source-vault-bootstrap-resume
    058a7cf28d2ba5adc5d8cffb9d5b65a14f9dd19e
    protected=false
```

Reconciliation:

```text
positive branch deletions   0
branch creations            0
ref updates                 0
mutation retries            0
mutation-uncertain results  0
unexpected guard codes      0
postflight branch changes   0
```

## 5. Positive-live fixture preflight

A separate read-only Runtime Bridge branch search in the persistent development conversation confirmed that the proposed disposable fixture name does not currently exist:

```text
r123/git-reference-delete-positive-20260910-01
count=0
totalCount=0
```

The exact source commit frozen for the positive fixture is the Checkpoint 441 public commit:

```text
058a7cf28d2ba5adc5d8cffb9d5b65a14f9dd19e
```

This fixture is safe because qualification will create one new disposable branch ref at that exact existing commit and then delete only that exact branch after readback proves the same SHA and `protected=false`.

No positive create/delete sequence is authorized by this validation. It requires separate explicit owner authorization.

## 6. Disposition

```text
VALIDATION199=PASS
GITHUB_DELETE_BRANCH_FRESH_HOST=PASS
GITHUB_DELETE_BRANCH_FRESH_HOST_PROJECTION=PASS_1_OF_1
GITHUB_DELETE_BRANCH_FRESH_HOST_CONTRACT=BOUNDED
GITHUB_DELETE_BRANCH_FRESH_HOST_NO_WRITE_GUARDS=PASS_2_OF_2
GITHUB_DELETE_BRANCH_FRESH_HOST_POSTFLIGHT=PASS
GITHUB_DELETE_BRANCH_POSITIVE_WRITES=0_OF_1
POSITIVE_FIXTURE_BRANCH=r123/git-reference-delete-positive-20260910-01
POSITIVE_FIXTURE_SOURCE_SHA=058a7cf28d2ba5adc5d8cffb9d5b65a14f9dd19e
POSITIVE_FIXTURE_CURRENTLY_EXISTS=false
HISTORICAL_BRANCH_CLEANUP=NOT_AUTHORIZED
AB030=PARKED_UNCHANGED
NEXT=EXPLICIT_OWNER_AUTHORIZATION_FOR_DISPOSABLE_CREATE_DELETE_QUALIFICATION
```