# Validation 185: GitHub Repository Administration Preview40 Live Surface Qualified

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.40 LIVE / THREE-TOOL FOUNDATION WIRED / TWO READS LIVE / CREATE NO-WRITE GUARDED / FRESH-HOST NEXT
**Research:** Research 123

## 1. Purpose

Validation 184 / Checkpoint 427 froze the first beyond-parity Repository Administration slice as exactly two read-only actions plus one controlled personal repository-creation action. This validation implements, publishes, repairs, and locally live-qualifies that slice without performing a positive repository-creation mutation.

The qualified action names are:

```text
github.list_repository_collaborators
github.list_repository_invitations
github.create_repository
```

## 2. Bounded implementation

The administration service uses only fixed GitHub REST routes and the existing GitHub App user-token/runtime authority layer.

`github.list_repository_collaborators` requires installation-derived repository authority and calls only the fixed repository collaborator endpoint. Caller controls are limited to repository full name, the documented `all|direct|outside` affiliation enum, optional `pull|triage|push|maintain|admin` permission filter, and bounded page controls.

`github.list_repository_invitations` also requires installation-derived repository authority and calls only the fixed open-invitations endpoint with bounded page controls.

`github.create_repository` is deliberately personal-user-only and calls only the fixed authenticated-user repository-creation endpoint. Its caller contract contains a restricted 1..100 character repository name, optional bounded description/homepage, semantic `visibility=private|public` with private as default, and `auto_init=false|true` with false as default. It exposes no organization owner, template, team, feature, merge, security, ruleset, host, endpoint, method, header, credential, transport, filesystem, shell, or process authority.

Repository creation re-reads authenticated identity inside a same-user/name serialized mutation boundary and rejects identity drift before write dispatch. The mutation uses mutation-aware single-attempt transport, so an uncertain creation is never replayed automatically.

## 3. Focused candidate tests

The focused fake-dependency administration suite passes 4/4:

```text
repository administration uses fixed bounded read routes and normalized outputs                  PASS
create repository is personal-only, private-by-default, and sends only bounded fields            PASS
repository administration semantic guards reject before create mutation dispatch                  PASS
create repository identity drift and uncertain transport never replay mutation                    PASS

pass 4
fail 0
```

The v3 correction also adds a G0 facade regression that requires the outer runtime kernel to expose all three new administration methods rather than merely composing them inside `services()`.

## 4. Publication history and defect localization

The first immutable release candidate exposed a regression-maintenance error: several inherited regression fixtures still asserted the previous 153-tool / 89-GitHub-action counts. Publication therefore did not become the accepted live foundation.

A corrected v2 updated those fixtures and successfully activated preview.39:

```text
releaseId            github-repository-administration-v2
targetVersion        0.1.1-preview.39-github-repository-administration
manifestSha256       b6e84a6fc6eddd43d505afa426fde03bea54ca5e537c3e95f543b2366651e8ab
publishOperation     rm_7aa8b6db34abf3fb374fb8a0ddd5134a
restartOperation     rm_a8098be546b66348cc9f49eb450c329c
postVerifyMismatch   0
```

A live local read immediately found a second integration defect that the v2 regressions had missed. The MCP tools were registered, but the outer `githubRuntime` facade did not delegate the three newly composed service methods. The two read calls therefore returned `githubRuntime.listRepositoryCollaborators is not a function` and `githubRuntime.listRepositoryInvitations is not a function`. The invalid create guard still rejected before dispatch. No GitHub administration write occurred.

The v3 repair is intentionally narrow. It adds the missing public facade delegates and a regression proving their presence. The final immutable release is bound to synchronized local-runtime source head:

```text
5846f02785c97df99c0ba8edc47f160a3710ef2b
```

Final activation evidence:

```text
releaseId            github-repository-administration-v3
targetVersion        0.1.1-preview.40-github-repository-administration
targetToolCount      156
fileCount            3
manifestSha256       a638f715565ebf939cdaa37ea9e1caeb743b1b5939423b68537da0346fd5e778
publishOperation     rm_5ebc427e137f0e8492f4ac5614683473
restartOperation     rm_9996fa2b896186b148b80b2a5a7056e2
postVerifyMismatch   0
recoveryAttempted    false
```

Prepublication `verify` reported three mismatches because the three-file repair intentionally differed from still-live preview.39. Publication then succeeded, restart succeeded, and postactivation verification closed those three expected deltas at zero mismatches.

## 5. Local live qualification

After preview.40 activation, direct local MCP health and `tools/list` report:

```text
runtime version       0.1.1-preview.40-github-repository-administration
public tools          156
GitHub tools          92
new admin tools       3 / 3 projected
```

The two positive read-only administration calls then succeed against `shakaarlatief/autonomous-data-science-system`:

```text
github.list_repository_collaborators
  isError                    false
  repositoryFullName         shakaarlatief/autonomous-data-science-system
  count                      1
  authenticated user present true

github.list_repository_invitations
  isError                    false
  repositoryFullName         shakaarlatief/autonomous-data-science-system
  count                      0
```

These calls perform no repository mutation.

## 6. Create-repository no-write guard

Exactly one deliberately invalid create call was used locally:

```text
name        bad name
visibility  private
auto_init   false
```

It failed input validation before Runtime Bridge/GitHub mutation dispatch:

```text
Invalid arguments for tool github.create_repository:
name: Invalid string: must match pattern /^[A-Za-z0-9._-]+$/
```

No schema-valid `github.create_repository` call has been issued. Therefore no repository was created, no create retry occurred, and no mutation-uncertain create result exists.

## 7. Host projection boundary

The persistent `chatgpt-21` connector projection predates preview.40. Targeted same-chat discovery still does not expose the three newly activated administration tools even though direct local MCP `tools/list` reports them. This is the already-qualified same-chat projection-staleness behavior, not a live-runtime failure.

The next gate is therefore one refreshed disposable fresh-host qualification of all three exact action names and their bounded schemas. That fresh-host qualification may safely execute the two reads and deterministic invalid no-write guards, but it must not perform a schema-valid `github.create_repository` mutation.

Positive repository creation remains separately owner-authorized after the fresh-host gate, for one exact repository name and visibility.

## 8. Disposition

```text
VALIDATION185=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.40-github-repository-administration
LIVE_PUBLIC_TOOL_COUNT=156
LIVE_GITHUB_TOOL_COUNT=92
EXTENDED_REPOSITORY_ADMIN_IMPLEMENTED=3_OF_3
EXTENDED_REPOSITORY_ADMIN_LOCAL_LIVE_READS=PASS_2_OF_2
CREATE_REPOSITORY_NO_WRITE_GUARD=PASS
CREATE_REPOSITORY_POSITIVE_LIVE=0_OF_1
CREATE_REPOSITORY_MUTATION_RETRIES=0
CREATE_REPOSITORY_MUTATION_UNCERTAIN_RESULTS=0
ADMINISTRATION_MUTATION_OCCURRED=false
SAME_CHAT_REPOSITORY_ADMIN_PROJECTION=STALE
NEXT=FRESH_HOST_REPOSITORY_ADMINISTRATION_SCHEMA_QUALIFICATION
```
