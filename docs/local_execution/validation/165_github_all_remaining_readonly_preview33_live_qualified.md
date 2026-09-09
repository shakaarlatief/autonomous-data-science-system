# Validation 165: All Remaining GitHub Read-Only Actions Live on Preview.33

**Date:** 2026-09-09
**Status:** PASS / ALL 48 READ ACTIONS IMPLEMENTED / 25 OF 26 NEW ACTIONS LIVE-SUCCESS LOCALLY / DOWNLOAD-USER-CONTENT POSITIVE FIXTURE GATED / FRESH-HOST NEXT
**Research:** Research 123
**Scope:** Preserve implementation, release, activation and local-live qualification of the final 26 native GitHub read-only actions, including correction of download handoff to MCP resource links.

## 1. Starting boundary

Validation 164 / Checkpoint 407 closed fresh-host coverage for G1 plus G2 at 22 public GitHub read-only tools. The captured native inventory contains 48 read actions and 41 write actions, leaving exactly 26 read actions unimplemented at that boundary. Research 123 deliberately moved from small read-only slices to one larger all-remaining-read phase while keeping GitHub mutations separately unauthorized.

## 2. Initial all-read-only implementation

Private local-runtime head:

```text
9c02076d586722886f5d008e527b2f95bf40b1f8
```

preserved release:

```text
github-all-readonly-expansion-v1
```

with target:

```text
0.1.1-preview.32-github-all-readonly
112 total public tools
48 github.* read-only tools
10 release files
16 regressions
1 runtime dependency
```

The 26 additions cover the remaining native read domains:

```text
content-download       1
actions-ci             6
issues                 5
pull-requests-reviews 14
                      --
new read actions       26
```

The focused all-read-only integration regression exercises all 26 actions under fake GitHub transport and proves GET-only external behavior, installation-derived repository binding and non-disclosure of the synthetic access token. The reconstructed broad public surface regression also passes at 112 tools / 48 GitHub reads.

## 3. Preview.32 activation

Release v1 prepared successfully with manifest SHA-256:

```text
a32aabbe934683cd6189c8601f0133784d5646e24aeaf076fc61c5aa36ba5fc1
```

Prepublication verification reported the expected ten source mismatches. Publication operation:

```text
rm_01cb0b89c12ceeec49453196151908f4
```

succeeded, and restart operation:

```text
rm_e5107659dff8be228341f029883b71d5
```

activated preview.32 without recovery. Postactivation verification returned zero mismatches. Direct health then reported 112 tools and 48 GitHub read-only actions. Protected GitHub authorization remained configured, stored, authorized and non-expired.

## 4. Local live read qualification

A fresh stateless loopback MCP `tools/list` returned exactly:

```text
toolCount   112
githubCount 48
```

Canonical public fixtures already preserved by Research 123 were used instead of touching unrelated private repositories. The live qualification established successful application results for 25 of the 26 newly added actions. Representative evidence includes:

```text
issue fixture                   #82
PR fixture                      #81
workflow-capable PR fixture     #76
PR #81 changed file             github-connector-capability-qualification.md
PR #81 merged discussion items  6
PR #81 review submissions       3
PR #81 review threads           1
issue #82 comments              1
workflow job steps              7
workflow job log bytes          14,756
combined commit status          pending
repository artifact inventory   available
non-expired artifact fixture    available
```

The live actions successfully covered issue fetch/comments/search/reactions; PR metadata, comments, file patch, all-file patch, diff, reactions, changed filenames, reviews and review threads; recent-user PR listing; recent issue listing; workflow runs/jobs/steps/logs/artifacts and combined commit status; and workflow artifact download. Valid empty reaction arrays and zero-artifact run results remained successful reads rather than failures.

No GitHub mutation occurred. No unrelated private repository names were printed or preserved.

## 5. Artifact handoff defect found before fresh-host qualification

The first live preview.32 artifact download succeeded for a non-expired canonical repository artifact:

```text
artifact size      322,868 bytes
artifact SHA-256   8d271d9db840ae4f43ddd8c36766198dbb528118656c567f5d3fcf8ecbb02b2e
```

but the tool result embedded approximately 430,492 base64 characters. The captured native contract explicitly describes `download_workflow_artifact` as returning a reusable file reference, and Research 123 had already frozen artifact resource/file handoff as the intended architecture. The preview.32 behavior therefore remained functional but was not accepted as the professional final handoff.

The project corrected the result before asking the owner to qualify it in a fresh ChatGPT host.

## 6. Resource-link correction

Private local-runtime heads:

```text
aa97ac6bee844f42a357d2aeee927ed7665d5224  resource-link implementation
3be4bfb1bdabecd1833aa42844e7047f0a34f787  corrected release manifest
```

preserve immutable release:

```text
github-all-readonly-expansion-v2
```

targeting:

```text
0.1.1-preview.33-github-all-readonly-resource-links
112 total public tools
48 github.* read-only tools
```

GitHub download bytes are now retained only in a bounded ephemeral server-owned resource store. Ordinary tool results contain compact metadata plus an MCP `resource_link`; bytes are materialized separately only through `resources/read`. The resource URI is server-generated, time-limited and caller-unselectable.

Both `github.download_workflow_artifact` and `github.download_user_content` use this path.

## 7. Corrected release qualification

The first v2 prepare attempt failed closed with:

```text
RUNTIME_RELEASE_MANIFEST_INVALID
```

because the draft listed unchanged files as `replace` entries whose current and target hashes were identical. The release contract was not weakened. The manifest was corrected to contain only six distinct source/test replacements. Because the failed prepare had not created immutable prepared state, the same v2 release ID remained valid.

Successful preparation then froze manifest SHA-256:

```text
73ce28ba375fc8919b5ef57e6b59369a37e9bdab56b2da29220a56c88e33de4a
```

with:

```text
fileCount              6
regressions            16
runtimeDependencyCount 1
targetToolCount        112
```

Prepublication verification returned the expected six mismatches. Publication operation:

```text
rm_d2e0f3c538d998568f565c7fb3da3211
```

succeeded. Restart operation:

```text
rm_80b337298f3835bdc6d13275cf2be235
```

activated preview.33 without recovery. Fresh postactivation verification is `verified` with `mismatchCount=0`. `/healthz` reports preview.33 with 112 tools and `/readyz` returns HTTP 200. Protected GitHub authorization remains stored, authorized and non-expired.

## 8. Live resource-link qualification

After preview.33 activation, stateless local MCP again returned exactly 112 tools / 48 GitHub reads. `github.download_workflow_artifact` was then invoked on the same bounded canonical artifact fixture. The result contained:

```text
content types          text, resource_link
structured base64      absent
resource size          322,868 bytes
resource media type    application/zip
```

A separate MCP `resources/read` of that exact server-generated resource returned 322,868 bytes whose SHA-256 was exactly:

```text
8d271d9db840ae4f43ddd8c36766198dbb528118656c567f5d3fcf8ecbb02b2e
```

matching the compact tool-result metadata. No artifact bytes/base64 were embedded in the tool result.

## 9. `download_user_content` fixture boundary

No suitable `https://private-user-images.githubusercontent.com/...` fixture was found in the bounded canonical public issue/PR comment material inspected for this qualification. The project therefore does not invent a positive live URL or inspect unrelated private repository content merely to force a green live call.

Positive resource-link behavior for this action is covered by the focused synthetic integration regression. A live negative guard probe using a non-allowlisted host failed before download with the expected semantic restriction:

```text
download_user_content supports only https://private-user-images.githubusercontent.com URLs
```

The action is therefore implementation/test qualified but remains positive-live-fixture-gated until an appropriate authorized source URL naturally exists.

## 10. Same-chat projection

This persistent `chatgpt-21` conversation still does not project the newly added GitHub action names after runtime activation. Targeted rediscovery for `download_workflow_artifact` returned unrelated previously projected tools rather than the exact new GitHub action. This reproduces AB-008 same-chat projection staleness and is not treated as a runtime failure.

A refreshed fresh disposable ChatGPT conversation is required for the 26-action host projection/schema gate.

## 11. Disposition

All 48 captured native read actions now have corresponding live Runtime Bridge implementations. Fresh-host qualification is complete for 22 and pending for the 26-action final read batch. The remaining native inventory consists of 41 write actions, which remain a separate later mutation-risk phase.

Exact native-wrapper parity remains conservatively `0 / 89` because hidden native output envelopes and unresolved option semantics are not inferred from capability success.

```text
VALIDATION165=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.33-github-all-readonly-resource-links
LIVE_PUBLIC_TOOL_COUNT=112
LIVE_GITHUB_READONLY_TOOL_COUNT=48
NATIVE_READ_ACTIONS_TOTAL=48
NATIVE_READ_ACTIONS_IMPLEMENTED=48
NATIVE_READ_IMPLEMENTATION_REMAINING=0
FRESH_HOST_QUALIFIED_READS=22
FRESH_HOST_PENDING_READS=26
NEW_READ_LOCAL_LIVE_SUCCESS=25_OF_26
DOWNLOAD_USER_CONTENT_POSITIVE_LIVE=FIXTURE_GATED
DOWNLOAD_WORKFLOW_ARTIFACT_RESOURCE_LINK=PASS
RESOURCE_READ_SHA_MATCH=PASS
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
SAME_CHAT_NEW_READ_PROJECTION=STALE
NATIVE_WRITE_ACTIONS_REMAINING=41
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_ALL_REMAINING_READONLY_SCHEMA_AND_LIVE_QUALIFICATION
```
