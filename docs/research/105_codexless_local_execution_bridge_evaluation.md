# Research 105: Codexless Local Execution Bridge Evaluation

**Status:** OPEN / READ-ONLY PATH VERIFIED / WRITE VALIDATION PENDING  
**Date:** 2026-08-31  
**Scope:** Evaluate whether Codexless can provide the active ChatGPT collaboration surface with a safe, bounded local execution bridge for ADS work before permanent Source Vault ingestion continues.  
**Decision state:** Not yet accepted as an ADS dependency or architecture component. The full read-only product path is proven; governed local write behavior remains to be validated before classification.

## 1. Why this evaluation exists

The first permanent Source Universe bootstrap has reached a point where most remaining work is machine-local:

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

This is transparent and safe but increasingly inefficient as ADS becomes more operationally local.

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

Codexless is an independent open-source project, not an OpenAI product, and is currently a Technical Preview.

The ADS evaluation pinned and reviewed:

```text
Codexless version          0.1.1-preview.5
source revision            ae9ee9201431a1241786ca938cb67f2e1b017f2b
runtime mode               existing-only
public MCP tool surface    42 tools
```

The local Codex runtime used by the evaluation is:

```text
Codex CLI                  0.151.0
Codex authentication       ChatGPT
ADS repository trust       explicit repository-root trust
local authority ceiling    workspace
read-only operations       downscoped to read-only
```

The evaluated Windows environment also satisfied the selected Codexless prerequisite boundary with Node.js 24.19.0 and npm 11.17.0.

## 3. Security and authority interpretation

Codexless must be treated as software capable of affecting real files and running real commands. It is therefore evaluated as a transport under existing authority, not as a new authority source.

Current ADS authority policy:

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

The bridge evaluation began before source ingestion at a clean rollback point:

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

If the local bridge is rejected or deferred, Source Vault work can resume from exactly this boundary through the prior manual / Codex / Claude Code execution paths.

## 5. Completed evaluation evidence

The following bounded validations have been completed and preserved under `docs/local_execution/validation/`:

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
011  fresh-chat read-only local operation succeeded
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

## 6. Fresh-chat read-only result

The first invocation attempt from the long-running pre-installation ChatGPT conversation was rejected by the ChatGPT host before reaching the local bridge:

```text
FORBIDDEN: This conversation does not support developer MCPs
```

This did not mutate local state and was not classified as a Codexless/tunnel failure because the transport and tool-discovery layers had already passed.

A fresh ChatGPT conversation created after plug-in installation then successfully performed a read-only inspection of the real local ADS repository through the full product path:

```text
fresh ChatGPT conversation
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

The local checkout was also observed behind the remote branch at that moment because continuity evidence had been committed remotely during setup. The exact current behind count is intentionally not treated as durable state. A reviewed fast-forward-only synchronization is required before the write test.

## 7. Remaining controlled write validation

Read-only success is not sufficient for full ADS adoption. The next test must be deliberately disposable and outside authoritative Source Universe state.

Required sequence:

```text
1. fast-forward the clean local branch to current origin
2. verify local branch == remote and working tree clean
3. create one exact disposable test artifact in an approved non-authoritative test surface
4. read it back and verify exact contents
5. remove only the artifact created by the test
6. verify cleanup
7. verify Git / protected Source Universe state remains unchanged
8. preserve the evidence
```

The first write test must not touch:

```text
Source Registry
Source Vault
original educational corpus
.ads-private credentials/secrets
backup payloads
recovery artifacts
```

## 8. Classification rule

Possible classifications remain:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
    bounded local reads and controlled writes work reliably
    authority remains acceptably constrained
    denials fail visibly
    provenance/results are inspectable
    no secret leakage is observed

ACCEPTED_READ_ONLY_ONLY
    local inspection is useful but mutation is not yet trustworthy

DEFERRED
    product, tunnel, stability, or integration limitations prevent useful adoption now

REJECTED_FOR_CURRENT_USE
    security, authority, or reliability problems make the bridge unsuitable
```

Acceptance as a local execution bridge does not make Codexless a core ADS product dependency. It remains replaceable infrastructure unless a later architectural decision explicitly elevates it.

## 9. Browser policy

Browser automation remains outside this first evaluation because filesystem, Git, command and test execution address the immediate bottleneck while logged-in browser authority introduces a larger privacy and prompt-injection surface.

Browser capability may be evaluated separately later only if a concrete ADS workflow materially benefits from it.

## 10. Relationship to Codex and Claude Code

Codexless does not replace local Codex or Claude Code as engineering agents.

```text
simple local inspection / deterministic execution
    -> direct bridge tools where sufficient

complex multi-file engineering / autonomous coding task
    -> Codex or Claude Code when agent reasoning is useful

ChatGPT
    -> primary reasoning / coordination surface for the current ADS collaboration
```

## 11. Exact next action

The next action is still **not Source Vault ingestion**.

It is:

```text
use the fresh ChatGPT continuation session with ADS Codexless Local Bridge
    -> fast-forward the clean local ADS branch to current origin
    -> verify branch/current working-tree state
    -> perform the controlled disposable write/read/delete test
    -> classify Codexless explicitly
```

Only after explicit classification should Source Vault ingestion resume through the selected execution path. Browser integration remains deferred.

## 12. Numbering correction provenance

This record was initially created under the filename/number `098_codexless_local_execution_bridge_evaluation.md`. During the planned chat-rotation continuity audit, the repository was found to already contain the unrelated accepted historical Research 098 for Cockpit presentation-state recovery.

The Codexless evaluation is therefore canonically renumbered to **Research 105**. This is a clerical identity correction only; it does not alter the evaluation evidence or scientific meaning of either research record.