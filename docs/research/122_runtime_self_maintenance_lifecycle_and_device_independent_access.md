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
