# Validation 184: Extended GitHub Repository Administration Foundation Design

**Date:** 2026-09-09
**Status:** PASS / BOUNDED FIRST EXTENSION SLICE / TWO READS + ONE CONTROLLED CREATE / HIGH-CONSEQUENCE ADMINISTRATION DEFERRED
**Research:** Research 123

## 1. Purpose

Checkpoint 426 closes the native-parity implementation phase under the currently available provider evidence and account fixtures. Research 123 remains active because its product scope was deliberately expanded before GitHub App creation to include useful GitHub capabilities beyond the provider-owned connector. Repository Administration(write) was selected as the strongest first extension family and the App is already configured with that permission.

This validation freezes the first bounded Repository Administration extension slice before implementation. No GitHub administration mutation is performed here.

## 2. Current authoritative platform baseline

Current GitHub documentation establishes the following relevant contracts for github.com API version `2026-03-10`:

- `POST /user/repos` creates a repository for the authenticated user, supports GitHub App user access tokens, and requires Repository Administration(write).
- Repository names are limited to 100 characters and may contain ASCII letters, digits, `.`, `-`, and `_`.
- `GET /repos/{owner}/{repo}/collaborators` supports GitHub App user and installation access tokens and requires only Metadata(read); it exposes bounded affiliation/permission filters and paginated results.
- `GET /repos/{owner}/{repo}/invitations` lists open repository invitations and supports GitHub App user/installation access tokens with Repository Administration(read) or Private repository invitations(read).
- GitHub states that a GitHub App that creates a repository is automatically granted access to that repository, including when installation repository selection would otherwise be limited.

Primary sources:

```text
https://docs.github.com/en/rest/repos/repos
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
https://docs.github.com/en/rest/collaborators/collaborators
https://docs.github.com/en/rest/collaborators/invitations
https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app
```

The current personal installation uses All repositories and current organization discovery returns zero organizations. The first create action therefore stays personal-account-only rather than inventing organization creation semantics without a live organization fixture.

## 3. First extension slice

The first administration foundation contains exactly three new `github.*` actions:

```text
github.list_repository_collaborators    read
github.list_repository_invitations      read
github.create_repository                write
```

The two reads provide the missing repository-administration discovery surface needed for later collaborator/invitation workflows and may also reveal whether a legitimate reviewer fixture exists in the future. The create action delivers the owner's explicit beyond-parity repository-creation capability while keeping the first mutation contract deliberately narrow.

## 4. `github.list_repository_collaborators`

### Caller contract

```text
repository_full_name  required string, 3..512, owner/name only
affiliation           optional enum all|direct|outside, default all
permission            optional enum pull|triage|push|maintain|admin|null, default null
page_size             optional integer 1..100, default 100
page                  optional integer >=1, default 1
additionalProperties  false
```

### Execution contract

1. Parse and validate exact `owner/name`.
2. Require installation-derived repository authority before request dispatch.
3. Use fixed GET `/repos/{owner}/{repo}/collaborators`.
4. Forward only the bounded affiliation/permission/per-page/page query values.
5. Return a normalized bounded page; never expose response headers, credentials or arbitrary URLs.

### Normalized result

Each collaborator should expose only useful stable fields:

```text
login
id
nodeId
htmlUrl
type
roleName
permissions: pull|triage|push|maintain|admin booleans
```

The tool must not imply that `roleName` proves the source of an organization grant. GitHub explicitly states that the collaborator listing cannot distinguish repository-, team-, organization- or enterprise-level grant source from the response alone.

## 5. `github.list_repository_invitations`

### Caller contract

```text
repository_full_name  required string, 3..512, owner/name only
page_size             optional integer 1..100, default 100
page                  optional integer >=1, default 1
additionalProperties  false
```

### Execution contract

1. Require installation-derived repository authority.
2. Use fixed GET `/repos/{owner}/{repo}/invitations`.
3. Return only currently open invitations supplied by GitHub for that page.
4. Do not accept invitation mutation fields, usernames, permission changes, host/URL/method/header/token or other transport authority.

### Normalized result

```text
id
nodeId
permissions
createdAt
htmlUrl
invitee: login/id/nodeId/htmlUrl/type
inviter: login/id/nodeId/htmlUrl/type
repository: id/fullName/private/htmlUrl
```

No invitation accept/decline/update/delete action belongs in this first slice.

## 6. `github.create_repository`

### Why personal-only first

The documented authenticated-user endpoint is sufficient for the current personal-account target and uses the existing GitHub App user token architecture. The current authorization sees no organizations. Organization creation introduces membership, policy, custom-property and team semantics that should be qualified separately when a real organization installation exists.

### Caller contract

```text
name                  required string 1..100
                      regex ^[A-Za-z0-9._-]+$
description           optional string|null, max 512, default null
homepage              optional http(s) URL string|null, max 2048, default null
visibility            optional enum private|public, default private
auto_init             optional boolean, default false
additionalProperties  false
```

The Runtime Bridge intentionally exposes `visibility`, not GitHub's raw `private` boolean. It maps `private -> true` and `public -> false`, avoiding conflicting aliases and making the safety default explicit.

The first slice does **not** expose:

```text
organization owner selector
team_id
visibility=internal
template source
gitignore template
license template
feature toggles
merge-method settings
auto-merge setting
branch-deletion setting
repository rulesets
custom properties
security settings
repository rename
archive/transfer/delete
arbitrary request fields
```

### Execution contract

1. Resolve the authenticated GitHub user server-side.
2. Validate `name` using the documented 100-character ASCII repository-name envelope.
3. Reject homepage values that are not explicit `http://` or `https://` URLs.
4. Serialize repository creation by lowercase authenticated-login/name key so concurrent same-name requests cannot race inside one Runtime Bridge instance.
5. Dispatch exactly one mutation-aware POST `/user/repos`.
6. Body contains only `name`, optional description/homepage, mapped `private`, and `auto_init`.
7. Never automatically retry an uncertain creation.
8. A classifiable GitHub HTTP error remains definite (`mutationUncertain=false`); transport failure before a classifiable response remains `mutationUncertain=true`.
9. Validate the 201 response as one repository object whose owner equals the authenticated user and whose name/full name are present.
10. Return the normalized repository response without making a second write.

GitHub documents that Apps that create repositories automatically receive access to those repositories. Positive-live qualification should nevertheless perform a separate read-only `github.get_repo` postflight rather than treating that guarantee as a mutation prerequisite.

### Safety defaults

```text
visibility default  private
auto_init default   false
owner selection     server-owned authenticated user only
mutation retry      never automatic
```

Creating a repository is durable remote state. Therefore a future positive-live create call requires explicit owner authorization for the exact repository name/visibility. The first implementation qualification should not create a junk repository merely for coverage. Prefer either a real repository the owner wants or a deliberately named qualification repository with a separately agreed lifecycle.

## 7. Explicitly deferred administration mutations

The following capabilities are valuable but are not safe or necessary in the first foundation:

```text
add/remove repository collaborator
update/delete repository invitation
rename repository
change repository visibility
archive repository
transfer repository
delete repository
ruleset create/update/delete
branch-protection/rules-policy writes
repository Actions-policy writes
```

Collaborator writes can notify third parties or revoke access, so they require exact real identities and user authorization. Visibility, archive, transfer and delete have substantially higher consequence and need dedicated semantic contracts, read-before-write checks and stronger confirmation. Rulesets can block pushes/merges across a repository and deserve their own later family.

## 8. First-release qualification plan

Implementation should target a three-tool preview without any positive administration mutation during publication. Qualification order:

```text
1. local schema registration: 3/3
2. integration tests with fake REST/token/authority dependencies
3. no-write guards for invalid repository name/homepage/page values
4. publish immutable runtime release
5. fresh-host projection/schema qualification: 3/3
6. positive-live reads on canonical ADS repository:
   - list collaborators
   - list repository invitations
7. create_repository remains positive-live pending separate explicit owner authorization
```

The two new reads can be exercised safely once live. Any create test must use one exact separately authorized repository name and must stop on mutation uncertainty without replay.

## 9. Disposition

```text
VALIDATION184=PASS
EXTENDED_REPOSITORY_ADMIN_FOUNDATION_ACTIONS=3
EXTENDED_REPOSITORY_ADMIN_READS=2
EXTENDED_REPOSITORY_ADMIN_WRITES=1
FIRST_CREATE_SCOPE=AUTHENTICATED_PERSONAL_USER_ONLY
CREATE_DEFAULT_VISIBILITY=PRIVATE
CREATE_DEFAULT_AUTO_INIT=false
COLLABORATOR_WRITES=DEFERRED
REPOSITORY_DELETION=DEFERRED_HIGH_CONSEQUENCE
RULESET_WRITES=DEFERRED_HIGH_CONSEQUENCE
ADMINISTRATION_MUTATION_OCCURRED=false
NEXT=IMPLEMENT_EXTENDED_REPOSITORY_ADMINISTRATION_FOUNDATION
```
