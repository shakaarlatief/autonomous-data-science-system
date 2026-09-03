# Flexible authority live source published and runtime/tunnel healthy

**Date:** 2026-09-03
**Status:** `51-TOOL DISCOVERY QUALIFIED / RUNTIME WORKSPACE ADMISSION PENDING`
**Scope:** Preserve the exact publication, restart failure/hotfix, successful 51-tool runtime bootstrap, and tunnel-readiness state of the Research 116 flexible multi-repository Codexless candidate before downstream ChatGPT discovery refresh.
**Authority:** Local execution evidence. This record proves the live source tree and restarted runtime reached the qualified 51-tool state after one exact constructor-wiring hotfix. It does not yet claim refreshed ChatGPT schema discovery or live workspace-registry admission.

## Publication result

The user executed the guarded host-terminal activation script:

```powershell
& .\.ads-private\codexless\activate-flexible-authority-publication.ps1 -Confirm:$false
```

The script completed:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=51
FLEXIBLE_AUTHORITY_PUBLICATION_PREFLIGHT=PASS
LIVE_BASELINE_VERIFIED=true
CANDIDATE_HASHES_VERIFIED=true
FLEXIBLE_AUTHORITY_PUBLICATION_RESULT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.8
EXPECTED_PUBLIC_TOOL_COUNT=51
```

## Independently re-read live source hashes

Immediately afterward, ChatGPT re-read the installed `%LOCALAPPDATA%\Codexless\src` files through the existing live bridge. All nine qualified source files exactly matched the candidate hashes:

```text
codex-app-server-client.mjs
641EC966F3A9E18857E0B0551DE0298BC120AE18F30A73D2EC50D3D9CFC5D84C

codex-authority-executor.mjs
011337776824D280BC41694CA8D7920223CF8C92B54E707344A3923FD767C315

codexless-runtime.mjs
3FE7392B875366BBE2BFAB7EE2FF978B72B6536EFDEDCCDF72E7160F530F2B9A

json-file.mjs
0CD2AE6ACC150ACE398169C23C291B28591B5789ABDCD524E7785F8808BC918C

mcp-server-factory.mjs
9D887AEE40E1D8FF0FCFAE3378A2281E8F8A275AD2B9B3C33EDCA2039E70190D

semantic-git.mjs
781BCB998782FCED786FDFFE7897779E1A1C942F30706C3CCE023DD5FCBC284A

surface-contracts.mjs
03FDB3B82B4C1E486D8459EC4575F187B79D9FB4365924AFE8B0E27C90DE54DA

workspace-authority.mjs
8DCEA6B65F818E7B95FEC3E3CBDBE9936ECFB3F573FE348D72029D2773DA9590

workspace-registry.mjs
6ED61579FB7730EA0C1990965B44239CACA4B08A91D18DF0D5D5C77AC604F2E7
```

This includes the three newly introduced live modules:

```text
semantic-git.mjs
workspace-authority.mjs
workspace-registry.mjs
```

## Running process still serves old in-memory build

The existing HTTP process was intentionally not restarted before verification. Its `/healthz` response still reported:

```text
ok          true
service     codexless-public
transport   streamable-http
version     0.1.1-preview.7
surface     codexless-public-preview-v1
toolCount   50
defaultCwd  C:\Projects_Data\autonomous-data-science-system
```

This is expected because source replacement does not hot-reload the already-running Node process.

## Restart failure and exact wiring hotfix

The first restart attempt failed immediately with:

```text
WorkspaceAuthorityManager requires a workspace registry
```

Read-only inspection showed an exact constructor-wiring defect:

```text
runtime passed:
    { workspaceRegistry, trustProject }

constructor required:
    { registry, trustProject }
```

The candidate and live runtime were both changed only to:

```text
{ registry: workspaceRegistry, trustProject }
```

The resulting candidate/live `codexless-runtime.mjs` hash matched exactly:

```text
F510E9EA59594A6EC9A5611F1638955C2FC153F2E539547DC592B62A23AAD718
```

The focused flexible-authority regression remained:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
```

A direct invocation of `public-surface-registration.mjs` from the partial candidate overlay failed because unchanged live modules such as `agent-tools.mjs` are intentionally absent from that overlay. That is a verification-route defect, not a runtime implementation failure; the guarded publication preflight had already exercised the correct complete-live-tree-plus-candidate-overlay staging path.

## Restarted runtime and tunnel result

After the hotfix, the restarted Codexless HTTP runtime returned:

```text
ok          true
service     codexless-public
transport   streamable-http
version     0.1.1-preview.8
surface     codexless-public-preview-v1
toolCount   51
defaultCwd  C:\Projects_Data\autonomous-data-science-system
```

The restarted tunnel then returned:

```text
/healthz   HTTP 200 / live
/readyz    HTTP 200 / ready
```

ChatGPT independently re-read both states through the reconnected bridge and observed the same `0.1.1-preview.8`, `toolCount 51`, and HTTP 200 tunnel liveness/readiness.

Therefore the current boundary is:

```text
installed live source tree            QUALIFIED 51-TOOL BUILD
running Codexless HTTP process         0.1.1-preview.8 / 51 TOOLS / HEALTHY
source publication                     PASS
constructor wiring hotfix              PASS
process restart                        PASS
tunnel reconnect                       PASS
tunnel liveness/readiness              PASS / PASS
ChatGPT app refresh                     PENDING
fresh-chat schema discovery             PENDING
workspace-registry live admission       NOT YET USED
```

## Fresh ChatGPT discovery qualification

After refreshing the developer MCP app, a fresh disposable ChatGPT conversation independently discovered the restarted live server as:

```text
server version          0.1.1-preview.8
live MCP tool count     51
protocol version        2025-06-18
public preview          true
```

The refreshed live MCP `tools/list` contained all 51 tools. The ChatGPT connector projection exposed 47 callable recipients in that disposable conversation; the four non-projected live-server compatibility actions were:

```text
codex.agent_card_state
codex.agent_commit
codex.agent_decline
codex.agent_handoff_prepare
```

The new stable surface was nevertheless fully usable for the Research 116 goal because `codex.workspace_authority` and the generalized semantic Git actions were projected. Discovery verified:

```text
codex.workspace_authority           PRESENT
workspace authority schemas         CLOSED / additionalProperties=false
semantic Git optional workspaceId   PRESENT
arbitrary cwd/remote/refspec/etc.    ABSENT
Call Profile                         PRESERVED
Rich Card / agent handoff            PRESERVED
Browser family                       PRESERVED
model-free project/read/edit tools   PRESERVED
```

A read-only workspace-authority `show` returned the initial registry at revision `1`, content hash:

```text
5277ba1f08bf7e1973c30758267ea376478f1d61f30d45eceeffed0c333a6652
```

with only the expected `ads-public` workspace.

## Private runtime workspace admission

Using that exact optimistic-concurrency pair, the user explicitly authorized and the fresh disposable ChatGPT conversation registered exactly:

```text
workspaceId
    ads-local-runtime

root
    C:\Projects_Data\autonomous-data-science-system-local-runtime

capabilities
    agent
    git_commit_paths
    git_fetch
    git_pull_ff_only
    git_push_ff_only
    read
    write

allowedRemote
    origin

integrityPolicyId
    runtime-private-bootstrap

browser
    NOT GRANTED
```

The resulting registry advanced exactly once:

```text
revision
    2

contentHash
    588cd49a5f4cc57386781b2c5432996df9ba391d711e551df453570078f8e2d8
```

and the server-owned derived protected-path policy was:

```text
id     runtime-private-bootstrap-v1
paths  [.git]
```

No Git mutation or Codex model turn was used for this admission.

## Independent post-admission authority verification

The long-running project chat then used ordinary model-free tools against the sibling runtime checkout. `codex.project_context` succeeded and reported:

```text
cwd                  C:\Projects_Data\autonomous-data-science-system-local-runtime
permission profile   ads-direct-git
approval policy      on-request
reviewer             user
sandbox              workspaceWrite
writable Git root    <runtime repo>\.git
network access       true
Codex CLI            0.152.1
```

A separate read-only `git status --short --branch` through `codex.command_exec` succeeded with the new Codexless registry binding visible in the receipt:

```text
workspaceId          ads-local-runtime
trustedAncestor      C:\Projects_Data\autonomous-data-science-system-local-runtime
codexTrustedAncestor C:\Projects_Data\autonomous-data-science-system-local-runtime
status               ## No commits yet on main...origin/main [gone]
```

A read-only `git remote -v` independently verified the exact expected origin:

```text
https://github.com/shakaarlatief/autonomous-data-science-system-local-runtime.git
```

This also closes the earlier `safe.directory` concern for the tested live registration/read path: registration's Git inspection succeeded and ordinary post-admission Git reads succeeded without adding or modifying Git configuration.

Therefore the current boundary is:

```text
installed live source tree            QUALIFIED 51-TOOL BUILD
running Codexless HTTP process         0.1.1-preview.8 / 51 TOOLS / HEALTHY
tunnel liveness/readiness              PASS / PASS
fresh ChatGPT discovery                PASS
stable workspace/Git schemas           PASS
ads-public registry entry               PRESENT
ads-local-runtime registry entry        PRESENT / REVISION 2
Codex trust for runtime repo             PASS
Codexless admission for runtime repo     PASS
ordinary runtime-repo read authority     PASS
runtime repository Git state             UNBORN main
first root/bootstrap commit               PENDING
secret/sensitivity inventory              PENDING
```

## Required next sequence

```text
1. inventory the current `.ads-private` tree without mutating it;
2. run a deliberate local secret/sensitivity audit that reports classifications without exposing secret values;
3. decide preserve / exclude / transform for the first runtime-repository import;
4. create README + RUNTIME_STATE provenance in the private runtime repository;
5. create the one controlled bootstrap/root commit required because semantic `expectedHead` cannot operate before commit zero;
6. after commit zero, use the generalized semantic Git contracts for ordinary commit/push operations;
7. preserve the resulting runtime-repository commit in public ADS / MC-0010 routing;
8. rotate to the new persistent ChatGPT conversation only after this stable authority boundary is durably preserved.
```
