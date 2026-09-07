# Research 122: Runtime Self-Maintenance, Lifecycle Supervision, and Device-Independent Access

**Date:** 2026-09-07
**Status:** ACTIVE / ARCHITECTURE BASELINE OPENED
**Scope:** Revisit the previously preserved runtime-maintenance and mobile/device-independent access gaps as the next active ADS stage after Research 120/121 closed. Determine how to remove repeated manual `%LOCALAPPDATA%` publication/restart/tunnel-shell work without broad host authority, and determine what is actually possible from a phone under the current ChatGPT/MCP product boundary.
**Primary backlog owners:** AB-001, AB-002, AB-006, AB-017.
**Authority:** Public ADS repository is sole development authority. Private runtime repository may preserve non-secret implementation evidence only.

## 1. Why this stage is active now

The direct local-file phase is complete for the accepted PDF and Office scope. The remaining operator friction is no longer document transport; it is host lifecycle and cross-device continuity.

Two previously preserved issues now become active together:

```text
AB-002 / AB-017
    Codexless cannot treat %LOCALAPPDATA% or process lifecycle as an ordinary workspace.
    Repeated runtime publications therefore needed guarded ordinary-host PowerShell helpers.

AB-001 / AB-006
    the connector worked from desktop web while the same conversation on phone returned
    401 tunnel_active_organization_required even though the laptop and tunnel remained running.
```

The project owner explicitly wants more automation/authority, but not by granting arbitrary user-profile or host-process control.

## 2. Current topology and the restart paradox

The accepted path is:

```text
ChatGPT developer MCP app
    -> OpenAI Secure MCP Tunnel service
    -> local tunnel-client
    -> Codexless Streamable HTTP MCP
    -> Codex App Server / local authority
```

The current public `codex.command_exec` surface intentionally exposes no general host-process control. This is correct.

A lifecycle action implemented only inside the Codexless process also has an intrinsic self-restart problem:

```text
ChatGPT calls Codexless
    -> Codexless stops itself before returning
    -> the request transport disappears
    -> result becomes uncertain / unavailable
```

The same dependency is even stronger if the action stops the tunnel that carries the request. Therefore the permanent solution cannot simply be “give command_exec permission to kill/restart everything.”

The architecture needs a separately owned lifecycle mechanism that can accept a bounded operation while the normal MCP path is alive, then complete process recovery independently after the request has been acknowledged.

## 3. Runtime-maintenance authority must remain semantic

Research 116 deliberately stopped at ordinary workspace/project authority. This stage preserves that separation.

Target authority classes:

```text
workspace authority
    read/write/agent/browser/Git inside explicitly admitted project roots

runtime-maintenance authority
    exact installed Codexless tree only
    qualified candidate -> publish -> verify -> rollback

lifecycle authority
    exact Codexless runtime process
    exact managed tunnel-client runtime
    health/readiness checks
    no arbitrary PID/process kill surface

credential mediation
    exact tunnel runtime credential reference
    no secret value exposed through MCP/tool results
```

Candidate semantic surface remains conceptually:

```text
codex.runtime_maintenance
    show
    publish
    verify
    rollback
    restart/status only if a safe separate lifecycle owner is proven
```

Do not register `%LOCALAPPDATA%` or the whole user profile as an ordinary workspace.

## 4. New upstream evidence: tunnel-client already owns managed runtime lifecycle

The installed tunnel-client is v0.0.13. A read-only local probe of the exact installed binary confirms that it already exposes native managed-runtime commands:

```text
tunnel-client runtimes connect
tunnel-client runtimes list
tunnel-client runtimes status
tunnel-client runtimes stop
tunnel-client runtimes rm
tunnel-client runtimes cleanup
```

`runtimes connect --help` explicitly says it is the supported path for a long-lived local runtime managed by Codex rather than `nohup`/`disown`.

Current upstream OpenAI tunnel-client documentation says the same. Relevant official sources include:

```text
https://github.com/openai/tunnel-client/blob/master/docs/onboarding.md
https://github.com/openai/tunnel-client/blob/master/plugins/tunnel-mcp/skills/tunnel-mcp/references/runtime-flows.md
https://github.com/openai/tunnel-client/blob/master/plugins/tunnel-mcp/skills/tunnel-mcp/references/profiles-state-and-keys.md
```

This materially changes the design space. ADS should not invent a custom tunnel daemon supervisor if the native tunnel-client runtime manager can own that lifecycle safely.

## 5. Managed runtime state exposes the next authority seam

A direct read-only `tunnel-client runtimes list --json` from the current ADS command sandbox failed before listing anything because the binary attempted to create its platform state directory under the user profile and the ordinary workspace authority denied it.

The same exact command succeeded when `TUNNEL_CLIENT_STATE_DIR` was redirected to a bounded ADS `.tmp` probe directory. The response showed an empty native alias inventory and a state root exactly inside that temporary directory.

Therefore the blocker is not lack of native lifecycle support. It is that the managed runtime owns state outside ordinary project roots by default. This is precisely the AB-002/AB-017 authority-class problem.

The professional direction is to give a server-owned runtime-maintenance component access to one dedicated tunnel-runtime state/profile root, rather than widening normal project access.

## 6. Candidate lifecycle architecture

The first design to qualify is:

```text
small ADS runtime supervisor / maintenance owner
    |
    |-- owns exact Codexless install path
    |-- owns exact tunnel-client managed-runtime state/profile roots
    |-- knows exact launcher identities
    |-- receives only semantic maintenance requests
    |-- stores/retrieves tunnel secret through a private credential reference
    |-- records bounded operation receipts
    |-- performs exact health/readiness verification
    |-- rolls back on failed publication/startup
    |-- cannot execute arbitrary caller commands

normal Codexless MCP process
    -> delegates a qualified lifecycle job
    -> returns an accepted operation receipt before destructive lifecycle begins

supervisor
    -> performs restart/recovery independently
    -> records terminal receipt for later readback
```

A persistent Windows service is not assumed yet. Compare at least:

```text
A. user-level long-lived supervisor started at logon
B. Windows scheduled-task supervisor
C. narrow detached one-shot restart helper plus native tunnel managed runtime
D. a small stable local MCP/front-door supervisor that remains up while Codexless worker restarts
```

The acceptance criterion is minimum authority and minimum custom lifecycle code, not maximum autonomy at any cost.

## 7. Tunnel foreground Git Bash should become optional if managed runtime qualifies

The current runbook intentionally keeps tunnel credentials in one foreground Git Bash shell and requires manual Ctrl+C/restart. That was safe for the first accepted topology.

Native `tunnel-client runtimes connect` creates a managed local runtime and can use generated profiles plus a runtime-key reference. Upstream documentation says the fallback launcher can use a detached background process when tmux is unavailable and records PID/log/runtime state.

If ADS qualifies this exact installed behavior, the permanent operator path can potentially become:

```text
no dedicated Git Bash tunnel window
no manual tunnel Ctrl+C
managed runtime alias + status
server-owned stop/connect/recovery
```

Secrets remain a separate design problem. Official tunnel-client supports runtime key references such as `env:NAME` or `file:/path`; ADS must choose a Windows-appropriate private credential mediation strategy without committing or returning the key.

## 8. Phone/mobile finding: current official product support is a real constraint

Current OpenAI Help Center documentation for Developer Mode/MCP apps explicitly states:

```text
MCP apps on mobile: No - web only.
```

Official source:

```text
https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta
```

That means the previously observed native-phone failure must not be treated only as a local tunnel bug. Even a perfectly healthy laptop/tunnel cannot make an unsupported ChatGPT mobile-client MCP surface become supported.

The previously observed error is nevertheless meaningful. Current official tunnel-client OpenAPI documents `tunnel_active_organization_required` as an organization-context error for organization-backed tunnels. The historical phone result is therefore consistent with a client/request path that did not supply the organization context required by the tunnel service. It does not prove the laptop tunnel was down.

Do not weaken tunnel principal/organization validation to work around this.

## 9. Phone research matrix

The next empirical device matrix should separate product surfaces:

```text
A. desktop ChatGPT web
    known baseline PASS

B. native ChatGPT mobile app
    reproduce current behavior
    current official expectation: custom MCP unavailable

C. mobile browser -> chatgpt.com normal web view
    test whether the web MCP surface is actually available on a phone browser

D. mobile browser -> desktop-site mode if materially different
    test only if C fails and the product UI offers the relevant app surface
```

For each attempt capture only safe diagnostics:

```text
ChatGPT-side error/classification
local tunnel /healthz and /readyz
local tunnel channel probe status
whether a corresponding MCP command reaches the local daemon
whether Codexless sees a request
laptop -> phone -> laptop continuity
```

If mobile web works, it is the preferred phone solution because it preserves the normal ChatGPT product and existing tunnel security.

If both mobile web modes fail, native direct ADS access from a phone is currently product-blocked. At that point compare explicit alternatives instead of weakening tunnel auth:

```text
remote desktop into desktop ChatGPT web
separate phone-accessible ADS operator/PWA surface
custom mobile/web client using the OpenAI API + bounded ADS backend
wait/monitor for official ChatGPT mobile MCP support
```

## 10. Relationship to task recovery

AB-001 only asks whether the connector can be reached from another device. AB-006 remains distinct: a task already accepted under Codexless should survive caller/device interruption and be inspectable after reconnect.

Once phone/web access is characterized, separately test:

```text
existing idle task/card inspection across devices
ready-in-chat handoff across devices
pending approval visibility
recovery after tunnel restart
no replacement task before surviving state is inspected
```

Do not conflate connector reachability with task continuity.

## 11. Initial acceptance direction

This research begins with three strong constraints:

```text
1. More authority means more semantic authority classes, not broad filesystem/process access.
2. Prefer native tunnel-client managed runtime lifecycle over custom daemon control where it satisfies ADS requirements.
3. Native ChatGPT mobile MCP access is currently documented as unsupported; first test mobile web before designing a custom remote-phone system.
```

## 12. Immediate next work

```text
1. qualify the exact installed tunnel-client managed-runtime state/process semantics without touching the active production tunnel
2. inspect the current Codexless publication/lifecycle seams and design the minimum separate supervisor contract
3. define the private credential/state ownership boundary
4. build a non-destructive prototype around an isolated test runtime/process before touching the live tunnel
5. run the phone surface matrix with safe local diagnostics
6. only then decide whether to implement runtime self-maintenance and/or a phone fallback product surface
```

## 13. Managed tunnel survives local MCP target outage and recovers without reconnect

The first isolated functional lifecycle discriminator is now complete. It used the exact installed tunnel-client v0.0.13 with all state/profile material redirected into the private runtime workspace `.tmp`, a fake loopback control plane implementing the published OpenAI poll/response contract, a dummy runtime-key reference, and a temporary loopback reverse proxy in front of the already-running Codexless MCP. No production tunnel ID/key, remote tunnel state, or live Codexless process was mutated.

The probe sent real MCP commands through the isolated managed tunnel rather than relying only on `/readyz`:

```text
1. initialize + tools/list through the isolated managed tunnel
   -> PASS, 61 tools

2. remove the local MCP path by stopping/destroying the proxy
   -> a new queued tools/list returned an HTTP-style 502 failure
   -> managed tunnel process remained alive

3. restore the local MCP path on the same endpoint
   -> new initialize succeeded
   -> new tools/list succeeded, 61 tools
   -> no runtimes connect/restart was issued between outage and recovery
```

Exact functional result:

```text
preOutageToolsList=true
outageFailureObserved=true
outageRespCode=502
postRecoveryNewInitialize=true
postRecoveryToolsList=true
tunnelProcessRunning=true
tunnelHealthy=true
tunnelReady=true
sameManagedRuntimeStayedUp=true
beforeToolCount=61
afterToolCount=61
```

This is decisive for the main restart architecture. A managed tunnel does not need to be restarted merely because its local MCP target temporarily disappears. It can remain connected to the control plane, fail requests visibly during the outage, and forward newly initialized MCP traffic after the target returns.

Therefore the preferred normal publication/restart path is now:

```text
managed tunnel remains running
    -> bounded external one-shot helper restarts Codexless only
    -> helper verifies local Codexless health
    -> subsequent MCP initialize/tools calls flow through the same tunnel runtime
```

A full tunnel stop/connect is reserved for tunnel-client/profile/credential/runtime changes or a failed tunnel itself. This materially narrows the authority needed for ordinary Codexless publications.

One caveat remains: tunnel readiness may remain positive while a previously healthy backend is temporarily absent. The stronger evidence is therefore the actual command failure/recovery result above, not a readiness flag alone. Operational health design must not use tunnel `/readyz` as the only proof that a restarted local backend is usable.

The durable private candidate currently preserves the 12-test semantic coordinator/managed-tunnel adapter at private head `413fba007de7c1d763ef4412921369d96e7131af`. The functional probe source is staged for the next private evidence commit with SHA-256 `422905f509466f56ddf3dc00b8c352a0fe6fa40d30bafcea96718db2854d9995`.

## 14. Refined immediate next work

```text
1. implement the minimum detached one-shot lifecycle owner for Codexless-only restart
2. give that helper a durable bounded operation ledger and exact process identity contract
3. qualify helper survival + dummy service restart without touching production
4. define private tunnel credential/state bootstrap for eventual managed-runtime migration
5. only after helper qualification, decide the one-time production migration sequence
6. run the phone native-app vs mobile-web matrix with safe local diagnostics
```

## 15. Detached one-shot helper and durable operation layer qualified in isolation

The next private candidate layer is now preserved at private runtime head:

```text
22773bb9d39f29f091b06f90f970730e01bd46d9
```

It adds a file-backed operation ledger and a detached one-shot launcher around the previously qualified semantic coordinator. The new focused suite passes:

```text
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
```

The durable ledger uses a server-owned absolute state root, hashes request IDs before they become filenames, persists request-to-operation identity across independent instances, performs same-directory atomic JSON replacement, and rejects unexpected host-shaped fields or malformed persisted receipts.

The detached launcher exposes only one variable at dispatch time: the already-bound opaque operation ID. Node executable, supervisor script, working directory, state root and environment are server-owned configuration. The helper is spawned detached with ignored stdio and is unref'd; caller-selected PID/path/command/action/secret fields are absent.

A real two-turn dummy-service probe then tested whether an external helper can outlive the invocation that launched it. The launch invocation started service generation A and a delayed detached helper. The surrounding generic `command_exec` call itself timed out rather than returning a clean acceptance result. Despite that caller timeout, an independent later inspection found that the detached helper had continued execution, terminated generation A, started generation B on the same endpoint, verified the replacement healthy, and written a terminal durable receipt:

```text
receiptStatus=succeeded
replacementGeneration=B
replacementHealthy=true
replacementProcessAlive=true
```

Cleanup removed the dummy listener and state, while the real Codexless service remained healthy at 61 tools and the production tunnel remained ready.

The timeout is an important boundary. It proves the helper can survive a caller/execution-wrapper failure, but it also shows that generic `codex.command_exec` must not be used as the permanent detached-lifecycle launcher. The production `codex.runtime_maintenance` implementation should spawn the one-shot helper directly from the long-lived Codexless server process, record the durable operation before dispatch, return the accepted receipt before the fixed destructive delay, and make a later status/read path authoritative if delivery is uncertain.

This separates three claims clearly:

```text
detached helper survival after caller failure       QUALIFIED
durable operation receipt across invocations       QUALIFIED
clean synchronous launch from generic command_exec  NOT QUALIFIED / NOT TARGET ARCHITECTURE
direct Codexless-owned helper dispatch               NEXT IMPLEMENTATION STEP
```

The previously staged managed-tunnel recovery probe was formatting-cleaned before private preservation. Its final preserved SHA-256 is `e3707abc0ff49864d8217b92c03300b74effba9f718ab85bb388bcc234881648`; Validation 099's earlier `422905...` value remains accurate only for the pre-preservation copy explicitly described there.

## 16. Refined lifecycle sequence

The preferred architecture is now concrete enough to implement in production-shaped private code:

```text
normal Codexless publication
    -> validate exact qualified candidate/manifest
    -> durable operation record
    -> direct Codexless-owned detached helper launch
    -> return accepted operation receipt
    -> fixed short delay
    -> helper verifies exact managed Codexless process identity
    -> helper restarts Codexless only
    -> helper polls local /healthz for expected version/tool count
    -> helper records terminal receipt
    -> managed tunnel remains running throughout
    -> next ChatGPT MCP initialization uses recovered Codexless backend

full tunnel restart
    only for tunnel/profile/credential/runtime changes or tunnel failure
```

The next hard requirement is therefore exact process identity and a production-shaped one-shot supervisor entrypoint. Do not move to live publication before those checks are qualified on an isolated Codexless-style worker.

## 17. Production-shaped direct dispatch and exact-instance restart qualified

Checkpoint 343 / Validation 101 now close the isolated lifecycle questions left by Checkpoint 342. The private runtime repository is synchronized at `610fb6c1480012b0db80965239493348e5de5a58` and contains the direct semantic dispatch service, durable active-operation lock, private runtime instance identity, authenticated fixed-loopback graceful shutdown, production-shaped one-shot supervisor entrypoint, fixed replacement worker launcher, and a 62-tool preview.18 integration candidate.

The exact safety shape is:

```text
Codexless request handler
    -> persist requestId / operationId
    -> acquire durable active-operation lock
    -> mark operation armed
    -> launch detached helper directly
    -> return armed receipt before destructive delay

helper
    -> read private runtime identity
    -> require /healthz to match exact instance/PID/version/surface/tool count
    -> POST fixed loopback shutdown endpoint with private token + exact instanceId
    -> wait for old instance to disappear
    -> launch one fixed server-owned Codexless worker definition
    -> require different instanceId and expected version/surface/tool count
    -> record durable succeeded/failed state
    -> release durable active-operation lock

managed tunnel
    -> remains running throughout ordinary Codexless-only restart
```

Focused suites pass 12/12, 7/7 and 6/6. Functional probes separately prove graceful exact-instance replacement, direct acceptance before restart, idempotent replay without a second restart, private shutdown-token handling, wrong-token rejection and clean identity removal after shutdown. No arbitrary PID kill is part of the accepted candidate.

The public integration target is `0.1.1-preview.18-runtime-maintenance`, still on `codexless-public-preview-v2`, with 62 tools. `codex.runtime_maintenance` accepts only `restart_codexless` or `status` plus caller-stable `requestId`; it exposes no general process/filesystem/tunnel/credential authority. The staged 62-tool public surface and existing Office/PDF/Git regressions pass. Production remains preview.17 / 61 tools and is not yet evidence of live self-restart.

The next step is an exact guarded preview.18 publication preflight. Live publication must remain hash-bound, backup/rollback capable and restart-free until independently verified. The first live use of the new mutation tool must occur only after the preview.18 source is published, the current runbook-controlled bootstrap restart activates it, local/tunnel health is verified, the ChatGPT app surface is refreshed, and a fresh chat discovers the new tool.

## 18. Refined immediate next work

```text
1. build and qualify the exact preview.18 guarded publication package
2. publish source without restarting; independently verify exact installed hashes
3. perform the one final runbook-controlled bootstrap restart needed to activate codex.runtime_maintenance
4. verify preview.18 / 62 tools and tunnel recovery
5. refresh the developer MCP app and use a fresh chat for discovery
6. invoke one bounded restart_codexless qualification and recover its durable status after reconnection
7. if that live test passes, ordinary future Codexless-only restarts move to codex.runtime_maintenance
8. keep full tunnel restart only for tunnel/profile/credential/runtime changes or tunnel failure
9. continue the separate mobile-web/device matrix afterward
```

## 19. Preview.18 guarded publication preflight qualified

Checkpoint 344 / Validation 102 now qualify the exact source-only preview.18 publication package. The protected helper is bound to private head `610fb6c1480012b0db80965239493348e5de5a58` and helper SHA-256 `5c1de81279e4dbf4fb009aa585ca8d832cfd863dbe8765e6139ab75a0542802f`. It requires the exact running preview.17 / 61-tool baseline, exact old/new file hashes, seven absent new source paths, the unchanged AB-020 semantic-Git hash and a live/ready production tunnel before any mutation is possible.

Two complete no-publish runs passed all eight staged public regressions, the 12/12 + 7/7 + 6/6 lifecycle suites, all three isolated lifecycle probes and a direct smoke test of the same Windows `File.Replace` forward/rollback primitive used by publication. No live file was changed and no restart occurred.

Publication remains a separate ordinary-host action because preview.17 intentionally has no runtime-maintenance install authority. The helper will replace four source files and three matching regression files and add seven source modules, using timestamped atomic backups, exact post-write hashes, live-disk regressions and fail-closed rollback. A successful source publication must still be independently verified before the one final runbook-controlled bootstrap restart that activates `codex.runtime_maintenance`.

## 20. Preview.18 source published, activation restart pending

Checkpoint 345 / Validation 103 preserve successful guarded source publication of the preview.18 runtime-maintenance package. The publication helper reran all staged/public/lifecycle tests, wrote exact timestamped backups, installed the qualified four changed source files, seven new runtime-maintenance modules and three matching regression files, then reran live-disk regressions. It explicitly performed no restart.

A separate read-only verification rehashed every installed publication target. All eleven preview.18 source files and all three preview.18 regression files exactly match the qualified candidate hashes; the existing Office/PDF/image regressions remain unchanged; AB-020 `semantic-git.mjs` remains exactly `3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02`.

The active process is deliberately still `0.1.1-preview.17-office-file-link` / 61 tools, while the tunnel is still `live/ready`. The next boundary is therefore one final full runbook-controlled bootstrap restart. Only after preview.18 / 62 tools is active, tunnel health/readiness is re-established, the developer MCP app is refreshed and a fresh chat discovers `codex.runtime_maintenance` may production self-restart be tested.

## 21. Preview.18 bootstrap activation and local discovery qualified

Checkpoint 346 / Validation 104 preserve successful activation of preview.18 after the one final runbook-controlled bootstrap restart. The active runtime now reports `0.1.1-preview.18-runtime-maintenance` / 62 tools, with a private instance identity bound exactly to the listening process and a shutdown token that remains absent from public health output. The production tunnel is again `live/ready`.

A separate direct local MCP initialize and tools/list against the active process returned exactly 62 tools and included `codex.runtime_maintenance` with the intended closed two-action schema. This is active local registration evidence rather than source-only evidence.

No production self-restart has been invoked. The next discriminator is ChatGPT host projection after refreshing the existing developer MCP app. A fresh disposable chat must discover `codex.runtime_maintenance` before the first live mutation.

## 22. Fresh-host union schema projection failed closed

The first refreshed fresh-chat discovery of active preview.18 successfully exposed `codex.runtime_maintenance`, but ChatGPT projected its top-level discriminated-union schema as `{ [key: string]: any }`. The fresh chat therefore could not verify the action enum, required `requestId`, or `additionalProperties: false` from the callable schema. It invoked no ADS tool and correctly classified the requested qualification as FAIL.

Direct local MCP evidence remains narrow: preview.18 `tools/list` still contains the strict two-branch `oneOf`. This makes the result a host schema-fidelity problem, not server authority widening. The current host also projects `codex.workspace_authority`, another top-level discriminated union, as the same generic map while ordinary top-level object tools remain structured. Research 122 therefore blocks the live restart and avoids top-level union/`oneOf` for this mutation-sensitive surface where a flat object is semantically equivalent.

## 23. Preview.19 flat schema candidate qualified

The private runtime repository now preserves the corrective candidate at `ac3e05de0ebd9553eafb322ce19ec17539f1c09d`. Preview.19 remains a 62-tool `codexless-public-preview-v2` surface and changes only the runtime-maintenance schema/version/test integration relative to preview.18. The new tool schema is one strict object with required `action` and `requestId`; `action` is the enum `restart_codexless | status`; additional properties remain forbidden.

A new actual MCP wire regression sends initialize + tools/list through linked MCP transports and proves that the serialized schema has top-level object properties/required, the action enum, the requestId bounds/pattern, no top-level `oneOf`, and `additionalProperties: false`. The eight staged public compatibility scripts and all 12/7/6 lifecycle suites plus three functional probes pass. Production remains preview.18 / 62 tools and no live mutation has been attempted. Guarded preview.19 publication is the next gate.

## 24. Preview.19 guarded publication preflight qualified

Checkpoint 349 / Validation 107 now qualify the exact three-file source-only publication package for the preview.19 flat-schema correction. The helper is bound to private head `ac3e05de0ebd9553eafb322ce19ec17539f1c09d` and helper SHA-256 `3ce8d4561886a8101525666cc6c084ed94b2f9607d36ec5a7ea797961b2be165`. Two complete no-publish runs passed the actual MCP wire-schema regression, all eight public regressions, all lifecycle suites/probes, and the exact Windows atomic forward/rollback primitive.

Publication replaces only `mcp-server-factory.mjs`, `surface-contracts.mjs`, and `public-surface-registration.mjs`, uses verified timestamped backups, performs no restart, and requires the current preview.18 / 62-tool process plus live/ready tunnel throughout. Because preview.18's ChatGPT host schema projection was rejected for mutation use, preview.19 activation will still use a manual runbook-controlled restart after source publication/verification.
