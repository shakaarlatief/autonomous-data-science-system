# Validation 189: GitHub CI Evidence Preview.41 Live Local Qualification

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.41 ACTIVE / 162 PUBLIC TOOLS / 98 GITHUB TOOLS / THREE CHECK READS LIVE / FIVE NO-WRITE GUARDS PASS / ZERO CI-EVIDENCE WRITES
**Scope:** Publish, activate, and locally qualify the six-action CI Evidence Publication foundation frozen by Validation 188, without performing a positive Check Run or commit-status mutation.
**Research:** Research 123

## 1. Purpose

Validation 188 / Checkpoint 431 froze the second beyond-parity GitHub extension family as CI Evidence Publication. The private local-runtime implementation had already advanced to corrected immutable release `github-ci-evidence-v2` before the prior ChatGPT conversation ended, but the release had not yet been prepared or activated.

This validation resumes from the durable repository boundary and qualifies:

```text
Runtime Release prepare / publish / activation
postactivation source verification
live 162-tool / 98-GitHub-tool MCP surface
three Check read actions on a real GitHub Actions fixture
five deterministic invalid no-write guards
postflight proof that no Codexless Check or commit status was created
```

Positive `github.create_check_run`, `github.update_check_run`, and `github.create_commit_status` publication remains outside this validation.

## 2. Source and operational preflight

The public ADS repository was already preserved at current session head `06b8480cc289395e831cb587eba20495c8265b0e` before runtime activation work resumed.

The private local-runtime repository was fetched and confirmed clean and synchronized at:

```text
f35d9049049abc7d2301a0b73c22087f35fb84b3
```

The governing operational procedure `docs/local_execution/OPERATIONS.md` was read before publication/restart work. The accepted semantic Runtime Release and Codexless-only restart path was used, so no ordinary install-path, PID, process, tunnel, credential, or arbitrary host authority was exposed.

## 3. Canonical release-manifest line-ending defect found and contained

The first `prepare` call for `github-ci-evidence-v2` failed definitely before preparation with:

```text
RUNTIME_RELEASE_MANIFEST_NONCANONICAL
runtime release manifest must use canonical JSON encoding
```

Read-only inspection localized the difference to working-tree line endings. The manifest contained 90 CRLF line endings, while the Runtime Release reader requires exact `${JSON.stringify(parsed, null, 2)} + LF` bytes. The repository uses `core.autocrlf=true`, and the committed Git content was already normalized to the canonical LF representation.

The working-tree manifest was rewritten from 90 CRLF sequences to 90 LF sequences with exact SHA guarding. Its resulting SHA-256 was:

```text
c0988d4b9e42d6e09eecc096bf4cf705cf58f9be68c3507dfbf0f76d41ac1186
```

A semantic commit attempt correctly produced no commit because Git staging found no content delta after normalization:

```text
GIT_COMMIT_PATHS_STAGE_MISMATCH
stagedPaths = []
indexRestored = true
```

The repository was clean afterward. The same logical `prepare` request ID was then reused and succeeded. No prepared-state mutation was duplicated.

Because a future Windows checkout or generated manifest could otherwise reproduce this exact canonicality failure, the private local-runtime repository was hardened after activation with one root `.gitattributes` rule:

```text
.ads-private/codexless/runtime-releases/**/release.json text eol=lf
```

`git check-attr` confirms both `text=set` and `eol=lf` for the release manifest. The hardening commit is:

```text
bcbf0e1f612f67c5f56a718098a2828f53588251
```

The private-runtime push passed `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`. This hardening commit is later than the immutable release source head and does not rewrite the already prepared/published release identity.

## 4. Runtime Release v2 publication and activation

The corrected immutable bundle is:

```text
releaseId           github-ci-evidence-v2
targetVersion       0.1.1-preview.41-github-ci-evidence
targetSurface       codexless-public-preview-v2
targetToolCount     162
fileCount           10
runtimeDependencies 1
manifestSha256      c0988d4b9e42d6e09eecc096bf4cf705cf58f9be68c3507dfbf0f76d41ac1186
releaseSourceHead   f35d9049049abc7d2301a0b73c22087f35fb84b3
```

Successful preparation returned `status=prepared`.

The prepublication verifier then returned the expected target-vs-current result:

```text
status         verification_failed
mismatchCount  10
```

This is expected before publication because preview.40 does not yet contain the ten preview.41 release targets. It is not a publication failure.

Publication operation:

```text
operationId       rm_9e3cf60f8ab306bbf7b5bcc7200d92a0
final status      succeeded
recoveryAttempted false
```

Activation restart:

```text
operationId       rm_800505880afb2e808fe67d785f2859fc
final status      succeeded
recoveryAttempted false
```

Postactivation `verify` then returned:

```text
status         verified
mismatchCount  0
```

## 5. Active runtime surface

Fresh loopback `/healthz` reports:

```text
ok              true
service         codexless-public
transport       streamable-http
version         0.1.1-preview.41-github-ci-evidence
surfaceVersion  codexless-public-preview-v2
toolCount       162
```

A separate stateless loopback MCP `tools/list` reports:

```text
public tools     162
GitHub tools      98
CI-evidence tools  6 / 6 present
```

The six exact names are:

```text
github.get_check_run
github.list_check_runs_for_ref
github.list_check_run_annotations
github.create_check_run
github.update_check_run
github.create_commit_status
```

Protected GitHub authorization survived activation. Metadata remains `configured=true`, `initialized=true`, `authorized=true`, `storedAuthorization=true`, with non-expired access and refresh state and no credential value exposed.

## 6. Positive live read-only Check qualification

The public ADS commit used as the read fixture is:

```text
06b8480cc289395e831cb587eba20495c8265b0e
```

`github.list_check_runs_for_ref` succeeded against that exact SHA with `filter=all`, returning four completed GitHub Actions Check Runs. All four had `conclusion=success` and `app.slug=github-actions`.

One exact Check Run was then read through `github.get_check_run`:

```text
checkRunId  102790611224
name        repository-integrity (ubuntu-latest)
status      completed
conclusion  success
headSha     06b8480cc289395e831cb587eba20495c8265b0e
annotations 0
```

`github.list_check_run_annotations` on the same Check Run succeeded and returned a valid empty page with `count=0`.

Therefore all three new read actions have one positive local-live application result on installation-authorized GitHub state.

## 7. Deterministic invalid no-write guards

Five deliberately invalid write calls were exercised only to prove fail-closed behavior:

```text
1. create_check_run
   annotation path = ../README.md
   -> input validation rejects traversal/non-repository-relative path

2. create_check_run
   status = completed, conclusion omitted
   -> input validation rejects: completed status requires conclusion

3. create_check_run
   status = in_progress, conclusion = success
   -> input validation rejects: conclusion requires status=completed

4. create_commit_status
   context_suffix = bad/name
   -> input validation rejects suffix outside ^[A-Za-z0-9._-]+$

5. update_check_run
   existing completed Check Run -> in_progress
   -> GITHUB_CHECK_STATUS_REGRESSION
      retryable=false
      mutationUncertain=false
      githubRequestId=null
```

The fifth guard intentionally reads the live completed Check Run before rejecting the backward lifecycle transition. No PATCH is dispatched.

No guard result was mutation-uncertain and no invalid call was replayed as a positive mutation.

## 8. No-mutation postflight

After all guard calls, the same commit still reports exactly four Check Runs, all owned by `github-actions`, and zero Check Runs from the Codexless App identity.

The existing combined commit-status read reports:

```text
totalCount  0
statuses    []
```

Therefore this validation produced:

```text
positive create_check_run writes     0
positive update_check_run writes     0
positive create_commit_status writes 0
CI-evidence mutations                 0
```

## 9. ChatGPT host projection boundary

The already-open `chatgpt-22` conversation still does not project the six new action names through its callable developer-MCP tool surface after preview.41 activation. This is consistent with the established AB-008 same-conversation projection-staleness class and is not evidence of a local runtime failure because direct loopback MCP discovery proves all six tools are live.

The next gate is therefore the normal tool-surface procedure from `docs/local_execution/OPERATIONS.md`:

```text
1. confirm Codexless health and tunnel readiness;
2. refresh/rescan the existing Codexless Runtime Bridge Plugin;
3. open one fresh disposable ChatGPT conversation;
4. qualify all six exact host-visible schemas;
5. run the three read-only Check actions on safe fixtures;
6. exercise deterministic invalid no-write guards only;
7. perform zero positive CI-evidence writes.
```

Positive Check/status publication remains a later separately authorized gate using one exact commit SHA and exact visible evidence payload.

## 10. Disposition

```text
VALIDATION189=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.41-github-ci-evidence
LIVE_PUBLIC_TOOL_COUNT=162
LIVE_GITHUB_TOOL_COUNT=98
CI_EVIDENCE_TOOLS=6_OF_6
CI_EVIDENCE_READS_LOCAL_LIVE=PASS_3_OF_3
CI_EVIDENCE_NO_WRITE_GUARDS=PASS_5_OF_5
CI_EVIDENCE_POSITIVE_WRITES=0_OF_3
CI_EVIDENCE_MUTATION_OCCURRED=false
POSTACTIVATION_VERIFY=PASS_ZERO_MISMATCH
PROTECTED_GITHUB_AUTHORIZATION=HEALTHY
RUNTIME_RELEASE_MANIFEST_EOL_HARDENING=bcbf0e1f612f67c5f56a718098a2828f53588251
SAME_CHAT_CI_EVIDENCE_PROJECTION=STALE
NEXT=FRESH_CHAT_CI_EVIDENCE_SCHEMA_READ_GUARD_QUALIFICATION
```
