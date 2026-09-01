# Research 105: Codexless Local Execution Bridge Evaluation

**Status:** CLOSED / `ACCEPTED_FOR_ADS_LOCAL_EXECUTION`  
**Opened:** 2026-08-31  
**Closed:** 2026-09-01  
**Scope:** Evaluate whether Codexless can provide the active ChatGPT collaboration surface with a safe, bounded local execution bridge for ADS work before permanent Source Vault ingestion continues.  
**Decision state:** Accepted as a replaceable bounded local execution transport. Read-only local access, direct command execution within the current sandbox, a permission-aware local write path, exact disposable write/read/delete behavior, visible denial, cleanup, and protected-state preservation have been proven. Acceptance does not make Codexless a core ADS dependency or authority layer.

## 1. Why this evaluation exists

The first permanent Source Universe bootstrap reached a point where most remaining work is machine-local:

```text
local Source Registry
local Source Vault
machine-local private state
source corpus ingestion / audit
backup staging
client-side encryption
local recovery / restore validation
runtime and test execution
```

Without a local execution bridge, the collaboration loop is:

```text
ChatGPT reasons
    -> emits terminal command
    -> project owner runs command locally
    -> project owner returns output
    -> ChatGPT inspects output
    -> repeat
```

The desired execution shape is:

```text
project owner remains in ChatGPT
    -> ChatGPT invokes a bounded local tool
    -> local machine executes under pre-existing local authority
    -> structured result returns to ChatGPT
    -> ChatGPT verifies and continues
```

The goal is not generic remote control of the machine. The goal is a governed local execution surface that removes unnecessary manual relay while preserving project authority, safety, provenance and reversibility.

## 2. Candidate and evaluated build

Candidate upstream project:

```text
https://github.com/liyana31811/Codexless
```

Codexless is an independent open-source project, not an OpenAI product, and was evaluated as Technical Preview infrastructure.

The ADS evaluation pinned and reviewed:

```text
Codexless version          0.1.1-preview.5
source revision            ae9ee9201431a1241786ca938cb67f2e1b017f2b
runtime mode               existing-only
public MCP tool surface    42 tools
```

The local Codex runtime used by the evaluation was:

```text
Codex CLI                  0.151.0
Codex authentication       ChatGPT
ADS repository trust       explicit repository-root trust
local authority ceiling    workspace
read-only operations       downscoped to read-only
```

The evaluated Windows environment also satisfied the selected Codexless prerequisite boundary with Node.js 24.19.0 and npm 11.17.0.

## 3. Security and authority interpretation

Codexless must be treated as software capable of affecting real files and running real commands. It is therefore accepted as a transport under existing authority, not as a new authority source.

ADS authority policy remains:

```text
PUBLIC ADS REPOSITORY
    read / inspect
    controlled project edits only when explicitly required
    repository commands and tests within the accepted local ceiling

PRIVATE SOURCE UNIVERSE OPERATIONAL ROOT
    controlled operational access only when required by the governed Source Vault bootstrap

ORIGINAL EDUCATIONAL SOURCE CORPUS
    READ ONLY

ARBITRARY HOST FILESYSTEM
    NOT REQUIRED

SYSTEM / CREDENTIAL / BROWSER PROFILE LOCATIONS
    NOT REQUIRED

BROWSER AUTOMATION
    DEFERRED FROM INITIAL EVALUATION
```

Authority remains layered:

```text
public repository              project-development authority
private companion              durable private continuity complement
.ads-private                   machine-local operational configuration
Source Registry / Vault        canonical source substrate
Codexless                      replaceable local execution transport only
```

No bridge result may weaken Source Vault governance, provenance requirements, secret handling, or original-source immutability.

## 4. Frozen Source Vault boundary

The bridge evaluation began and ended before source ingestion at a clean rollback point:

```text
permanent Source Registry      migrated / verified
Alembic head                   0003_source_universe
registry table count           33
first permanent corpus compare 20 / 20 MATCH
DIFFERENT_ARTIFACT             0
MISSING_LOCAL_SOURCE           0
ADDITIONAL_LOCAL_SOURCE        0
source ingestion               NOT STARTED
working-store audit            pending ingestion
independent backup round trip  not yet verified
Course 2                       BLOCKED
```

The local execution evaluation did not modify authoritative Source Universe state.

## 5. Completed evaluation evidence

The bounded validation chain is preserved under `docs/local_execution/validation/`:

```text
001  local prerequisite preflight
002  pinned Codexless install + project-authority doctor
003  loopback MCP health/readiness
004  Secure MCP Tunnel provisioning
005  official tunnel-client checksum + Sigstore provenance
006  tunnel-client runtime identity
007  restricted runtime-key configuration + doctor
008  foreground Secure MCP Tunnel health/readiness
009  ChatGPT developer plug-in connection + tool discovery
010  pre-existing chat host rejected developer-MCP invocation
011  fresh disposable-chat read-only local operation succeeded
012  controlled permission-aware write/read/delete local operation succeeded
```

Important verified properties include:

```text
Codexless local service        loopback-only
Codexless doctor               PASS
Secure MCP Tunnel              provisioned / ready
OpenAI tunnel-client           v0.0.13
Tunnel runtime key             Restricted / Tunnels Read + Use only
Admin-key authority            not used by runtime
ChatGPT Developer Mode         enabled
custom plug-in                 ADS Codexless Local Bridge / connected
MCP tool discovery             PASS
browser integration            deferred
```

No runtime API key, token, tunnel credential, browser profile, encryption secret, source binary, or private filesystem coordinate is stored in the public repository.

## 6. Read-only local path result

The first invocation attempt from a long-running pre-installation ChatGPT conversation was rejected by the ChatGPT host before reaching the local bridge:

```text
FORBIDDEN: This conversation does not support developer MCPs
```

That did not mutate local state and was not classified as a Codexless/tunnel failure.

A fresh **disposable diagnostic interaction** created after plug-in installation then successfully performed a read-only inspection of the real local ADS repository through the full product path:

```text
fresh disposable ChatGPT interaction
  -> ADS Codexless Local Bridge
  -> OpenAI Secure MCP Tunnel
  -> tunnel-client
  -> Codexless loopback MCP
  -> real local ADS repository
  -> read-only result returned to ChatGPT
```

Observed read-only result:

```text
repository access             PASS
branch                        v1-source-vault-bootstrap-resume
working tree                  clean
repository-root enumeration   PASS
local modifications           none
```

The successful diagnostic interaction did not consume a persistent ADS ChatGPT session number. Validation 011 has been reconciled accordingly after the provenance correction already preserved in Checkpoint 269 and Research 107.

## 7. Controlled synchronization and local write result

Before the write test, the real local checkout was clean but one commit behind its matching origin-tracking branch:

```text
local HEAD   284c99e094a44750404fa197da127bfaf6d9b93a
origin HEAD  063fdc99c76d7821efc58bb83823bcad33c068c5
```

A direct bridge `command_exec` attempt reached the local repository but could not complete `git pull --ff-only` because the active `:workspace` / `workspaceWrite` sandbox denied the `.git/FETCH_HEAD` write:

```text
error: cannot open '.git/FETCH_HEAD': Permission denied
```

The failed attempt left the working tree clean.

The formal Codex agent lane was then used specifically so the blocked Git metadata operation could enter the normal permission-request path. It paused at one exact approval request for:

```text
git pull --ff-only origin v1-source-vault-bootstrap-resume
```

No additional permissions were requested. The project owner granted a one-time approval only.

The strict fast-forward succeeded:

```text
284c99e094a44750404fa197da127bfaf6d9b93a
    ->
063fdc99c76d7821efc58bb83823bcad33c068c5
```

No merge, rebase, reset, commit, push, or GitHub write occurred.

The controlled test then created exactly one non-authoritative artifact:

```text
tests/research105_disposable_probe_20260901_7f3c9a2e.txt
```

Exact UTF-8 content, including the final newline:

```text
Research 105 disposable controlled-write proof.
Nonce: 20260901-7f3c9a2e
```

Exact verification result:

```text
text-exact match   True
byte-exact match   True
byte count         73
SHA-256            2489c0a51e8c8f003043b8bd59f75fbf46590301a243d316645b4e2f990be564
```

The first verification attempt encountered a PowerShell parser error before reading or modifying anything. A Base64 byte-comparison verification then passed.

The agent deleted only the disposable artifact. Final state:

```text
artifact exists                                False
local HEAD                                     063fdc99c76d7821efc58bb83823bcad33c068c5
origin/v1-source-vault-bootstrap-resume        063fdc99c76d7821efc58bb83823bcad33c068c5
working tree                                   clean
staged changes                                 none
unstaged changes                               none
protected Source Universe mutation             none
```

The full evidence is preserved in validation 012.

## 8. Final classification

Research 105 is classified:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

The acceptance criteria are satisfied at the evaluated boundary:

```text
bounded local reads work                       PASS
controlled local write works                   PASS
exact readback is inspectable                  PASS
delete-only cleanup works                      PASS
permission denial fails visibly                PASS
permission-aware approved operation works      PASS
protected state remains unchanged              PASS
no secret leakage observed                     PASS
```

Acceptance is intentionally scoped. It means ADS may use Codexless as a replaceable local execution transport where its resolved authority is appropriate. It does **not** mean:

```text
Codexless is a core ADS architectural authority
all local operations are permitted
all direct command/exec mutations work
browser automation is accepted
arbitrary host filesystem access is required
formal Codex agents must be used for every task
```

## 9. Direct lane versus formal Codex agent lane

The evaluation established an important routing distinction:

```text
simple local inspection / deterministic execution
    -> direct bridge tools where the current authority permits the operation

operation blocked by command/exec sandbox but legitimately eligible for approval
    -> formal Codex agent lane can enter the explicit permission-request workflow

complex multi-file engineering / autonomous coding
    -> Codex or Claude Code only when agent reasoning adds value
```

The current direct command lane cannot perform at least the Git metadata write required by `.git/FETCH_HEAD` under the present sandbox projection. This is a concrete follow-up engineering question, not a hidden acceptance assumption.

The project owner has selected a bounded post-acceptance audit to reconstruct the bridge/tunnel/Codex permission architecture from durable repository evidence and determine whether routine ADS-local writes and normal Git operations can be enabled safely through the direct ChatGPT -> bridge lane without invoking a formal Codex model for every mutation.

## 10. Observability and host-runtime limitations

The formal agent task exposed a UI/observability limitation: the visible Call Codex card remained in a `Codex running` state while the underlying agent was actually `awaitingApproval`. Reading the bounded agent state exposed the exact pending command immediately.

Future supervision should therefore distinguish presentation state from authoritative agent state when progress appears stalled.

The persistent `chatgpt-14` interaction also experienced intermittent ChatGPT host rejection of Developer MCP invocation after earlier successful bridge calls:

```text
FORBIDDEN: This conversation does not support developer MCPs
```

Fresh disposable conversations remained able to invoke the bridge. This remains a ChatGPT host/runtime integration limitation and should be investigated separately from the accepted local transport behavior.

The formal Call Codex card also reported a high token-usage figure for the bounded task. That observation may matter to efficiency, but its exact accounting semantics and cause have not been audited and no architectural conclusion is inferred from it yet.

## 11. Browser policy

Browser automation remains outside this evaluation because filesystem, Git, command and test execution address the immediate operational bottleneck while logged-in browser authority introduces a larger privacy and prompt-injection surface.

Browser capability may be evaluated separately later only if a concrete ADS workflow materially benefits from it.

## 12. Exact continuation after acceptance

The local-execution acceptance prerequisite is now closed. Source Vault ingestion is no longer blocked by Research 105 itself.

The selected immediate continuation is:

```text
preserve Research 105 acceptance evidence
    -> reconcile public/private continuity for the new boundary
    -> reconstruct the direct-lane permission architecture from repository evidence
    -> determine the smallest safe authority change, if any, for routine direct local writes / Git
    -> fast-forward the local checkout after any new public preservation commit
    -> resume permanent Source Vault bootstrap/ingestion from the unchanged pre-ingestion boundary
```

If the direct-lane authority refinement is deferred or rejected, that does not reopen Research 105 automatically. The accepted formal permission-aware lane remains available as the proven governed local write path.

## 13. Numbering correction provenance

This record was initially created under the filename/number `098_codexless_local_execution_bridge_evaluation.md`. During the planned chat-rotation continuity audit, the repository was found to already contain the unrelated accepted historical Research 098 for Cockpit presentation-state recovery.

The Codexless evaluation is therefore canonically Research 105. This was a clerical identity correction only and did not alter the evaluation evidence or scientific meaning of either research record.