# Research 116: Flexible Multi-Repository Codexless Authority and Runtime-Repository Architecture

**Date:** 2026-09-03
**Status:** ACCEPTED / LIVE MULTI-REPOSITORY AUTHORITY QUALIFIED
**Scope:** Define a durable Codexless authority architecture that can safely operate across multiple local repositories and projects, including the new private ADS local-runtime repository, without requiring a new MCP tool release every time a repository, branch, or project changes.
**Authority:** Active Level-2 architecture research. It may define the next Codexless candidate and validation plan but does not itself widen current local authority.
**Declared references:** `research:105`, `research:113`, `research:114`, `research:115`, `checkpoint:276`, `path:docs/local_execution/AUTHORITY_BOOTSTRAP.md`, `path:docs/local_execution/OPERATIONS.md`, `path:docs/local_execution/validation/033_semantic_git_commit_push_surface_publication_and_public_ads_push_verified.md`, `path:docs/local_execution/validation/034_chatgpt_tool_projection_refresh_and_connector_coexistence_observations.md`

## 1. Why this architecture is needed

The first ADS Codexless authority was intentionally narrow. It proved the safety and feasibility of direct local execution on one trusted ADS checkout and later proved bounded semantic Git fetch, pull, commit, and push behavior.

That narrowness is now becoming operational friction. ADS needs to work with at least:

```text
public ADS development repository
private ADS local-runtime repository
private companion knowledge repository when appropriate
future project repositories
future branches inside those repositories
```

The project owner explicitly wants authority to be flexible enough that adding a repository, changing branches, or moving between projects does not require repeatedly redesigning the MCP app and opening another ChatGPT conversation merely to obtain a new action schema.

## 2. Current empirical boundary

The public ADS checkout remains authorized and operational.

The newly created private repository is:

```text
shakaarlatief/autonomous-data-science-system-local-runtime
visibility: private
purpose: versioned preservation of non-secret local runtime / `.ads-private` material
```

The repository was cloned locally as an empty checkout. The first model-free read attempt from the current Codexless runtime failed before file access with:

```text
PERMISSION_APPROVAL_REQUIRED
Codex has no explicitly trusted project/root covering cwd
C:\Projects_Data\autonomous-data-science-system-local-runtime
```

This is useful evidence. The repository is present, but Codexless correctly refuses to use a host profile override outside a Codex-trusted root.

## 3. Important implementation discovery

The current Codexless authority executor is already structurally multi-project aware.

It resolves a requested `cwd`, reads Codex configuration, searches all configured projects for the longest trusted ancestor, and refuses a host profile override if no trusted project covers the requested directory.

Conceptually:

```text
requested cwd
    -> Codex config/read
    -> longest trusted project ancestor
    -> allowed permission profiles
    -> requested read-only/inherit downscope
    -> command/file/agent execution
```

Therefore many existing public tools do not inherently need a new schema for each repository. They already accept `cwd` and can work with another repository once that repository is explicitly trusted and admitted by Codexless policy.

Examples include:

```text
codex.command_exec
codex.read_many
codex.precise_edit
codex.agent_start
codex.agent_bind
codex.thread_unarchive
Browser/Skill operations that already accept cwd
```

The principal hard-coded repository limitation is now the semantic Git layer and the single-project authority bootstrap, not the underlying execution architecture.

## 4. Target architecture: two-layer workspace authority

Future Codexless authority should require both:

```text
Layer 1: Codex trust
    target path is an explicitly trusted Codex project/root

Layer 2: Codexless workspace registry
    target path/repository is explicitly admitted for ChatGPT/Codexless use
    and the requested capability is enabled
```

Permission requires both layers.

This avoids treating every folder trusted by Codex Desktop as automatically available to ChatGPT.

## 5. Stable workspace registry

Introduce durable non-secret local user state outside the install/package tree, analogous in lifecycle spirit to the Codex Call Profile.

Each registered workspace should have a stable ID and server-owned policy. Conceptual example:

```text
workspaceId: ads-public
root: <local public ADS checkout>
kind: git
remote: origin
capabilities:
    read
    write
    agent
    git_fetch
    git_pull_ff_only
    git_commit_paths
    git_push_ff_only
protected paths:
    .git
    .tmp
    .ads-private
integrity gate:
    ADS PUBLIC_REPOSITORY_INTEGRITY
```

A private local-runtime entry can use different protected paths and a different integrity gate.

The model should not be able to register an arbitrary path simply by supplying `cwd` to an ordinary action. Registry mutation is a separate authority-changing operation.

## 6. Stable tools, mutable policy

The key design goal is to stop coupling ordinary repository changes to MCP schema changes.

Future normal flow:

```text
new repository / branch / project
    -> explicit authority-registry update
    -> same existing MCP tools
    -> no tool rescan required
    -> no new conversation required merely for the repository change
```

A fresh app scan/new conversation should be needed only when the actual MCP action schema changes.

## 7. Generalizing semantic Git

The current semantic Git tools intentionally freeze one ADS branch and remote. That was correct for first acceptance but is too narrow as the permanent architecture.

A stable v2 Git schema should select only a **registered workspace ID**, never arbitrary Git parameters.

Conceptually:

```text
git_fetch_origin(workspaceId)

git_pull_ff_only(workspaceId)

git_commit_paths(
    workspaceId,
    expectedHead,
    message,
    paths
)

git_push_ff_only(
    workspaceId,
    expectedHead
)
```

The caller must still be unable to supply:

```text
raw command
absolute cwd
remote URL
refspec
force flag
Git credentials
Git configuration
permission profile
sandbox mode
```

The server resolves those from the registered workspace.

## 8. Branch flexibility without arbitrary refspec authority

A repository should not require a plugin release merely because the active development branch changes.

For registered Git workspaces, the semantic Git layer can derive the current branch and exact upstream from Git itself, then fail closed unless:

```text
HEAD is attached to a branch
configured upstream exists
the upstream remote matches the workspace's allowed remote
local/remote relationship satisfies the operation's ancestry requirements
no merge/rebase/cherry-pick/revert state is active
required cleanliness/index conditions hold
```

Push can publish only current `HEAD` to the same branch name on the registered remote. Pull can fast-forward only from the current branch's registered upstream. The caller still chooses neither branch nor refspec.

This provides branch flexibility while retaining semantic rather than arbitrary Git authority.

## 9. Repository-specific integrity gates

Different repositories need different publication gates.

Examples:

```text
ads-public
    scripts/check_repository_integrity.py
    exact current branch

ads-local-runtime
    secret/sensitivity scan
    runtime manifest/coherence check
    Git cleanliness/ancestry checks

private companion
    private continuity/integrity rules
```

The registry may point to a locally configured server-owned integrity policy. The caller must not supply a command to bypass or replace that policy.

## 10. Authority-management surface

A durable architecture should expose a small explicit authority-management interface rather than require manual JSON editing for every future workspace.

Candidate operations:

```text
show / list
prepare add
prepare update
prepare remove
apply prepared change
```

Authority mutations should use optimistic revision/hash checks and require explicit human intent. A prepared workspace authorization is identity/binding evidence, not automatic permission.

The management surface may coordinate Codex project trust only through a separately verified supported mechanism. It must never silently create trust as a side effect of an ordinary read/write/tool call.

## 11. Bootstrap problem and supported trust mechanism

The new runtime repository demonstrates the bootstrap problem cleanly:

```text
repository exists locally
    but
Codex does not trust it yet
    therefore
normal Codexless cwd tools fail closed
```

The first flexible-authority implementation therefore needs a deliberate bootstrap path that can establish both:

```text
Codex project trust
Codexless workspace-registry admission
```

Current official OpenAI Codex source provides a supported App-Server-owned mechanism. The TUI's `config_update.rs` defines `trusted_project_edit(project_path)` as a `ConfigEdit` at:

```text
projects."<project trust key>".trust_level = "trusted"
```

and its `write_config_batch(...)` helper sends that edit through:

```text
config/batchWrite
```

with:

```text
filePath / file_path = null
expectedVersion / expected_version = null
reloadUserConfig / reload_user_config = true
```

The public helper `write_trusted_project(...)` uses that path rather than editing `config.toml` directly. This is strong upstream evidence that project trust is legitimately writable through the App Server configuration API.

Official source:

```text
https://github.com/openai/codex/blob/main/codex-rs/tui/src/config_update.rs
```

Evidence class: `B / OFFICIAL_SOURCE`.

The implementation direction is therefore refined to:

```text
1. add a narrow internal App Server config/batchWrite trust helper
2. bind it only to an explicit workspace-registration operation
3. verify the exact project trust entry through config/read afterward
4. persist the independent Codexless workspace-registry admission only after both sides are proven
5. never create trust as a side effect of ordinary read/write/agent/Git use
```

The current upstream source uses no optimistic expected-version guard for this TUI trust write. ADS should nevertheless add its own registry revision/hash guard and read-before/write-after checks around the combined authority change. Before live adoption, the exact installed Codex runtime must be qualified for `config/batchWrite`; current upstream `main` evidence alone does not prove local-version compatibility.

Do not mutate private Codex databases or write raw Codex configuration files directly when the supported App Server configuration path is available.

## 12. Private local-runtime repository role

The new private runtime repository solves a separate preservation problem.

Target role:

```text
PUBLIC ADS REPOSITORY
    sole project-development authority
    architecture, decisions, research, checkpoints, public implementation/contracts

PRIVATE COMPANION REPOSITORY
    durable private knowledge/continuity complement

PRIVATE LOCAL-RUNTIME REPOSITORY
    versioned non-secret machine-local/runtime implementation state
    `.ads-private` candidates and activation/regression material
    runtime manifests and exact private implementation evidence

LOCAL .ads-private
    execution-ready materialization used by the current machine
```

The local-runtime repository is not a competing `CURRENT_STATE` or product-development authority. Public ADS records what is accepted and why; the runtime repository preserves the exact private/local implementation bytes and deployment evidence.

## 13. Security rule for runtime preservation

Private Git is not secret storage.

Before the first import, audit `.ads-private` and exclude/redact any:

```text
passwords
API keys
tokens
cookies
private keys
encryption secrets
recovery codes
credential-manager exports
other authentication material
```

Machine-specific non-secret paths/configuration may be preserved when useful, because that is one purpose of the private runtime repository.

## 14. ChatGPT tool-snapshot implication

The recently published Codexless server exposes 50 public MCP tools, including the new semantic commit/push actions. A fresh disposable ChatGPT conversation discovered those actions successfully.

This existing long-lived `chatgpt-16` conversation retained its earlier projected tool snapshot and still cannot invoke the two new action names directly.

Therefore the project should treat **MCP schema refresh** and **workspace-policy refresh** as different events:

```text
MCP action schema changed
    -> restart / tunnel readiness / app refresh
    -> fresh disposable discovery
    -> new persistent chat when the old chat lacks the new projected actions

only workspace registry/policy changed
    -> same stable action schemas
    -> no new persistent chat should be required
```

This is a central design reason for the registry architecture.

## 15. Native ChatGPT connector coexistence finding

Current OpenAI help documentation says a chat can invoke multiple first-party and third-party apps in one prompt and that app selection applies to the message, not permanently to the entire conversation.

ADS repeatedly observed a different runtime behavior when combining the developer MCP with the native GitHub connector:

```text
GitHub may appear in available tool definitions
but invocation can fail with:
FORBIDDEN: This conversation is restricted to developer MCPs
```

An independent OpenAI Developer Community report reproduces the same exact error with a different developer MCP and ordinary connected apps.

Current classification:

```text
likely ChatGPT host/runtime limitation or bug
not evidence of a Codexless implementation defect
supported coexistence path not yet identified
```

Official reference:
`https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta`

Independent reproduction:
`https://community.openai.com/t/openai-s-own-developer-mode-documentation-says-multiple-apps-can-be-combined-but-actual-custom-mcp-openai-apps-behavior-does-not-match/1383485`

## 16. Why Chat 17 should not open yet

A fresh persistent chat will be useful because `chatgpt-16` does not inherit newly scanned MCP action schemas.

However, rotating immediately would be wasteful because this flexible-authority work is likely to produce one more deliberate tool-surface change.

Accepted sequencing:

```text
finish flexible multi-repository authority candidate
publish it
restart / tunnel / app refresh once
validate new stable surface in disposable chat
preserve exact boundary
then open chatgpt-17 with the complete refreshed tool set
```

After that, ordinary new-workspace registrations should not require repeated chat rotation.

## 17. Accepted implementation result

All seven implementation questions were resolved and live-qualified.

The accepted architecture is:

```text
Codex trust
    supported App Server config/batchWrite + config/read verification

Codexless workspace registry
    durable user-local canonical JSON outside the install tree
    optimistic revision + SHA-256 concurrency guard
    explicit register / update / remove
    longest canonical-root admission

stable workspace capabilities
    read
    write
    agent
    browser
    git_fetch
    git_pull_ff_only
    git_commit_paths
    git_push_ff_only

semantic Git
    caller selects only workspaceId
    branch and same-name upstream derived dynamically
    registered allowed remote remains server-owned
    no caller cwd/URL/refspec/credentials/config/profile/sandbox/force

repository-specific integrity
    ads-public
    runtime-private-bootstrap

private runtime preservation
    reviewed non-secret `.ads-private/codexless` material
    README + RUNTIME_STATE provenance
    Source Vault bootstrap state excluded from bulk Git preservation
```

The live public surface is Codexless `0.1.1-preview.8` with 51 MCP tools. Fresh ChatGPT discovery qualified the new `codex.workspace_authority` contract and generalized Git contracts without regressing Call Profile, Rich Card/handoff, Browser, or model-free project tools.

The registry now contains both `ads-public` and `ads-local-runtime`. The private runtime workspace was admitted at registry revision `2`, content hash:

```text
588cd49a5f4cc57386781b2c5432996df9ba391d711e551df453570078f8e2d8
```

The private runtime repository was bootstrapped with reviewed non-secret runtime evidence and root commit:

```text
0ce61ba794929ee71c555d480a936fdced28ef2e
```

After the one-time host creation of remote `main`, authenticated-private semantic Git was qualified through the stable generalized surface. `codex.git_fetch_origin(workspaceId="ads-local-runtime")` succeeded through the bounded host network substrate, and `codex.git_push_ff_only` returned up-to-date with:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
retried=false
headAfter == remoteTrackingHeadAfter == 0ce61ba794929ee71c555d480a936fdced28ef2e
trackedWorkingTreeCleanAfter=true
postflightOk=true
```

This closes the Research 116 core question. Adding a future ordinary filesystem/project workspace no longer requires a new MCP action schema. It requires an explicit workspace-registry mutation with the desired supported capabilities. Removing or reducing access is likewise a registry mutation.

The accepted scope is deliberately not universal arbitrary-host authority. Codexless self-maintenance, process lifecycle, Windows services/registry, credential stores, and other non-workspace host capabilities remain separate future authority classes if the project chooses to generalize them.

## 18. Exact continuation

The accepted Research 116 boundary is now preserved and synchronized in both repositories:

```text
public ADS
    81c03f90617800ca4fdd862964bc0007b9a7acfa

private local-runtime
    8d33e5408fde10dde1a974f0f1d5da11b84b8f9f
```

Continue with:

```text
1. publish the updated MC-0010 routing that points Claude to both public ADS authority and private runtime implementation evidence
2. verify the fresh Claude environment can actually access the private runtime repository before starting Message 001
3. deliberately rotate to chatgpt-17 with the stable 51-tool schema after continuity preflight
4. resume the broader Research 113 upstream ecosystem study
5. keep Validation 035 supervision/wakeup and active-turn writer-transfer research explicitly open
6. resume Source Vault only when the broader Level-2 research route is deliberately closed
```
