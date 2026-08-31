# Research 098: Codexless Local Execution Bridge Evaluation

**Status:** OPEN / EVALUATION ONLY  
**Date:** 2026-08-31  
**Scope:** Evaluate whether Codexless can provide the active ChatGPT collaboration surface with a safe, bounded local execution bridge for ADS work before permanent Source Vault ingestion continues.  
**Decision state:** Not accepted as an ADS dependency or architecture component. Adoption requires a bounded real-machine evaluation and explicit classification after evidence is collected.

## 1. Why this evaluation exists

The first permanent Source Universe bootstrap has reached a point where most remaining work is machine-local:

```text
local Source Registry
local Source Vault
machine-local private state
source corpus comparison / ingestion / audit
backup staging
client-side encryption
local recovery / restore validation
runtime and test execution
```

Without a local execution bridge, the collaboration loop is currently:

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
project owner remains in the existing ChatGPT conversation
    -> ChatGPT invokes a bounded local tool
    -> local machine executes under pre-existing local authority
    -> structured result returns to ChatGPT
    -> ChatGPT verifies and continues
```

The goal is not generic remote control of the machine. The goal is a governed local execution surface that removes unnecessary manual relay while preserving project authority, safety, provenance and reversibility.

## 2. Candidate: Codexless

Candidate upstream project:

```text
https://github.com/liyana31811/Codexless
```

Codexless describes itself as an independent open-source local execution bridge that exposes a tested subset of the local Codex toolbox to ChatGPT through an MCP / ChatGPT App path. It is not an OpenAI product and is currently described upstream as a Technical Preview.

Upstream documentation reviewed on 2026-08-31 reports:

```text
Windows supported in Technical Preview
Node.js 22+ required
one working local Codex installation required
local HTTP service binds to loopback
remote ChatGPT access uses an authenticated tunnel / remote MCP endpoint
OpenAI Secure MCP Tunnel is one supported transport, not a mandatory dependency
Plus and Pro have passed upstream real-machine product-path testing
that Plus/Pro result is test evidence, not a promise of future OpenAI plan policy
ordinary supported local tools can run without invoking the Codex model
Codex Agent escalation remains a separate explicit path
```

The candidate therefore appears much closer to the needed ADS capability than building a bespoke local bridge immediately.

### Preliminary upstream implementation review

The current upstream `main` package inspected on 2026-08-31 identifies itself as:

```text
codexless 0.1.1-preview.5
Node engine requirement >=22
@openai/codex dependency 0.147.0
MCP packages 2.0.0
```

This identifies the currently inspected source state only. ADS has not yet selected a pinned release/tag/commit for installation.

The Windows entrypoint is a small wrapper around `scripts/install.ps1`. Initial installer inspection confirms that it:

```text
requires Windows
requires Node.js >=22
requires npm
uses a staging directory before activation
uses lifecycle/activation locking
has rollback handling for failed activation
runs doctor checks before accepting the staged installation
uses %LOCALAPPDATA%\Codexless as the default install location
uses user-local state outside the install tree
supports existing-runtime and recommended-runtime modes
```

The initial review found no reason to reject the candidate before local prerequisite testing. This is not yet a full source-code security audit and does not authorize installation by itself.

## 3. Security interpretation

Codexless must be treated as software capable of affecting real files and running real commands.

Relevant upstream security properties include:

```text
local Codex authority remains the permission ceiling
remote caller must not silently widen that authority
permission/trust denials should fail visibly
command execution defaults to a read-only compatibility lane
stronger inherited authority must be requested explicitly
project edits are narrower than unrestricted raw filesystem mutation
trusted-root and symlink/junction escape checks are part of the local path
HTTP entry point binds only to loopback
remote access requires a separately protected tunnel
secrets and tunnel credentials remain local and out of source control
Codex Agent delegation is distinct from model-free local tool execution
```

These are useful properties, but the Technical Preview label means ADS must verify the behavior itself rather than treating upstream claims as sufficient evidence.

## 4. ADS authority boundary for the evaluation

The first evaluation should be intentionally narrower than the maximum capability Codexless can expose.

Conceptual authority policy:

```text
PUBLIC ADS REPOSITORY
    read / inspect
    controlled project edits when explicitly required
    run repository commands and tests

PRIVATE SOURCE UNIVERSE OPERATIONAL ROOT
    read / inspect
    controlled writes required by the governed Source Vault bootstrap

ORIGINAL EDUCATIONAL SOURCE CORPUS
    READ ONLY

ARBITRARY HOST FILESYSTEM
    NOT REQUIRED

SYSTEM / CREDENTIAL / BROWSER PROFILE LOCATIONS
    NOT REQUIRED

BROWSER AUTOMATION
    DEFERRED FROM INITIAL EVALUATION
```

Exact private filesystem coordinates remain in the accepted private-state layers and must not be copied into public Git merely to configure this evaluation.

The local bridge must not become a new authority layer for ADS data. It is an execution transport. The public repository remains the project-development authority, the private companion remains the private continuity complement, `.ads-private` remains machine-local operational configuration, and the Source Registry / Source Vault remain the canonical source substrate.

## 5. Evaluation sequence

### Phase A: freeze the pre-evaluation Source Vault boundary

The bridge evaluation begins before source ingestion.

Required frozen state:

```text
permanent Source Registry migrated to 0003_source_universe
registry migration verified
first permanent corpus prospectively compared
20 / 20 MATCH
0 DIFFERENT_ARTIFACT
0 MISSING_LOCAL_SOURCE
0 ADDITIONAL_LOCAL_SOURCE
source ingestion NOT STARTED
working-store audit not yet applicable to ingested corpus
independent encrypted backup round trip not yet verified
Course 2 BLOCKED
```

This provides a clean stop point. If the bridge evaluation fails, Source Vault work can resume manually from exactly this boundary.

### Phase B: prerequisite and upstream review

Before installation:

```text
verify Windows environment is supported by the selected Codexless release/tag
verify Node.js >= 22
verify local Codex runtime/CLI is present and healthy
inspect selected release/tag rather than blindly installing HEAD
review README, SECURITY, installer and relevant configuration behavior
verify ChatGPT Developer Mode / App path is actually available on the current account
select authenticated tunnel mechanism
ensure no tunnel secret is committed to either ADS repository
```

The current ChatGPT plan must be tested empirically. Upstream Plus compatibility evidence is useful but not treated as a durable product-policy guarantee.

### Phase C: install and local doctor checks

Use the selected reviewed release/tag and the upstream Windows installer.

Then:

```text
run Codexless doctor against the ADS repository
verify the service binds only to loopback
verify the intended project/trust root
verify local authority is not broader than intended
verify no ADS file or configuration has been modified unexpectedly
```

Do not connect a public unauthenticated endpoint directly to the local service.

### Phase D: connect ChatGPT through authenticated MCP transport

Connect the local loopback service through the selected secure tunnel / MCP endpoint to ChatGPT Developer Mode / App infrastructure.

Verify:

```text
ChatGPT can see only the expected exposed tools
connection survives a normal request/response cycle
no tunnel token or endpoint secret appears in Git or public documentation
local denials remain visible rather than silently escalating
```

### Phase E: harmless read-only ADS smoke test

Before any local write through ChatGPT, prove read-only operation.

Suggested smoke checks:

```text
read current Git branch
read git status
read a known public repository file
run python --version
run uv --version
run a non-mutating repository inspection command
return stdout / stderr / exit status accurately
```

Acceptance requires the observed local result to match independently known state.

### Phase F: controlled disposable write test

Only after the read-only path passes, exercise one deliberately disposable write inside an approved non-authoritative test surface.

Required behavior:

```text
create exact test artifact
read it back
verify exact contents
remove only the artifact created by the test
verify cleanup
verify Git status / protected state remains as expected
```

No Source Registry, Source Vault, original educational source, credential file or backup artifact should be used as the first write test.

### Phase G: classify the bridge

Possible classifications:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
    bounded local tools work reliably
    authority is acceptably constrained
    denials fail visibly
    provenance/results are inspectable
    no secret leakage observed

ACCEPTED_READ_ONLY_ONLY
    inspection path is useful but mutation path is not yet trustworthy

DEFERRED
    product-plan, tunnel, stability or integration limitations prevent useful adoption now

REJECTED_FOR_CURRENT_USE
    security, authority or reliability problems make the bridge unsuitable
```

Acceptance of Codexless as an execution bridge does not make it an ADS product dependency. It remains replaceable infrastructure unless a later architectural decision explicitly elevates it.

## 6. Initial browser policy

Browser automation is deliberately outside the first ADS evaluation.

Reason:

```text
filesystem / Git / command / test execution addresses the immediate bottleneck
browser session authority introduces a larger privacy and security surface
browser content is untrusted input and may contain prompt injection
logged-in browser state should not be exposed without a concrete project need
```

Browser capability may be evaluated separately later if ADS has a specific workflow that materially benefits from it.

## 7. Relationship to Codex and Claude Code

Codexless does not replace local Codex or Claude Code as engineering agents.

The intended distinction is:

```text
simple local inspection / deterministic execution
    -> direct bridge tools where sufficient

complex multi-file engineering / autonomous coding task
    -> Codex or Claude Code when their agent reasoning is useful

ChatGPT
    -> remains the primary reasoning / coordination surface for the current ADS collaboration
```

The point is to avoid unnecessary handoff for operations that do not require a separate coding agent while retaining those agents for tasks that genuinely benefit from them.

## 8. Failure and rollback rule

The Source Vault bootstrap must not become dependent on successful Codexless adoption.

If any stage fails:

```text
stop the bridge evaluation
preserve evidence needed to understand the failure
remove / disable tunnel exposure
uninstall or leave Codexless dormant as appropriate
confirm ADS repository and private operational state remain intact
resume Source Vault bootstrap through the existing manual / Codex / Claude Code execution paths
```

The pre-evaluation Source Vault boundary is therefore intentionally frozen before ingestion.

## 9. Exact next action

The next action is **not Source Vault ingestion**.

It is:

```text
verify local Node.js version
verify local Codex installation/version/path
inspect the selected Codexless release/tag and installer boundary
confirm the current ChatGPT account exposes the required Developer Mode / App connection path
then decide whether to install
```

No browser integration should be configured in the first pass.

No source ingestion should begin until either:

```text
Codexless evaluation reaches an explicit adoption/defer/reject classification
```

or the project owner explicitly decides to abandon the evaluation and resume the existing Source Vault execution workflow.
