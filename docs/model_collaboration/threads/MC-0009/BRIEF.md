# MC-0009 Brief: ChatGPT Local Git Through MCP Feasibility and Safety Architecture

**Thread:** MC-0009  
**Date opened:** 2026-09-01  
**Review mode:** INDEPENDENT_THEN_COMPARATIVE  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Exact pre-proposal repository target:** `cb48c1ac539592e63b13cbc8e4e2413cb0b196a0`  
**Intended reviewer environment:** fresh normal Claude Project interaction with repository access  
**Intended interaction session:** `claude-03`  
**Intended conversation title:** `03 - ChatGPT Local Git MCP Feasibility Research`  
**Authority:** Neutral independent-research brief. It records the observed execution boundary and asks for an architecture/research judgment; it does not freeze a ChatGPT solution and does not make Claude authoritative.  
**Purpose:** Determine whether ordinary ChatGPT Chat, through a trusted local MCP bridge, can practically and safely perform bounded local Git operations without a Codex model-agent turn, and identify the smallest supported architecture and experiment that can falsify or validate that possibility.

## Why this review exists

ADS has been validating Codexless as a replaceable local execution transport rather than a project authority. Research 105 accepted Codexless for bounded local execution, after which the project owner chose to audit whether routine Git synchronization could also use the model-free direct lane rather than requiring a formal Codex agent for every Git operation.

The direct-lane investigation has now separated several distinct authority layers. The unresolved question is no longer whether ChatGPT can reach the local machine at all, nor whether the formal Codex route can perform Git operations. The unresolved question is whether the ordinary ChatGPT conversation plus a local MCP bridge can expose a sufficiently bounded Git operation that ChatGPT will actually dispatch through the outer tool-safety layer.

This matters because ADS should not institutionalize a more expensive or indirect execution path merely because one generic MCP command shape was blocked, if a narrower supported MCP contract can perform the same bounded operation safely. Conversely, ADS should not build a custom Git façade if the platform imposes an immutable prohibition that makes such a façade ineffective or misleading.

The project owner explicitly requested a second-model research pass before ChatGPT implements its own preferred solution.

## Independence boundary

Claude's substantive repository evidence base is the repository exactly as it existed at:

```text
cb48c1ac539592e63b13cbc8e4e2413cb0b196a0
```

Read this `BRIEF.md`, `THREAD.md`, `STATE.json`, `docs/current_routing.json`, and `docs/model_collaboration/REVIEW_INBOX.md` from the coordination branch only to locate and understand the request. For substantive ADS repository evidence, inspect the exact frozen target above.

No ChatGPT implementation proposal for a new Git-specific MCP surface has been frozen in the repository. Do not search later coordination-branch artifacts for a candidate design before preserving the independent position.

This is intended as `BLIND_TO_CANDIDATE`, not blind to the observed diagnostic facts below or to existing Codexless/Codex architecture.

## Observed facts that define the problem

Treat these as diagnostic evidence and constraints, not as a proposed solution.

### 1. ChatGPT can already execute local work through Codexless

The existing Codexless bridge exposes model-free local command/file capabilities backed by Codex App Server. Local reads, ordinary local commands, and controlled workspace writes have already been demonstrated against the real ADS checkout.

The formal `Call Codex` / Codex-agent lane is separate and has already successfully performed Git metadata operations, including a strict fast-forward pull, under explicit agent lifecycle/approval handling.

Therefore the question is not whether any local route works. It is specifically whether the model-free ChatGPT-to-local route can support bounded Git operations.

### 2. The custom direct profile is genuinely active

The machine-local profile `ads-direct-git` is based on `:workspace`, keeps the trusted ADS repository root, and adds explicit `.git` write authority. Runtime inspection proved:

```text
inherit permission ceiling   ads-direct-git
trusted root                 C:\Projects_Data\autonomous-data-science-system
.git writable root           present
readOnly downscope           :read-only
config overrides             2
```

The caller cannot select an arbitrary stronger profile remotely.

### 3. A Windows ACL state-transition defect was diagnosed and repaired

With the custom profile active, `git fetch origin` initially failed at:

```text
.git/FETCH_HEAD: Permission denied
```

Host inspection proved that `.git` still carried explicit deny-write ACEs for the persistent Codex workspace capability SID from earlier `:workspace` execution, while the new `.git` capability SID had Modify access.

The project owner removed only the two stale explicit deny ACEs from the ADS repository `.git` directory. The inherited deny on `.git/FETCH_HEAD` disappeared, while the `.git`-specific writable capability and unrelated ACLs remained.

A subsequent direct fetch no longer failed at filesystem access. It progressed to network connection and failed because the inherit profile still had `networkAccess=false`. The removed workspace-SID deny ACEs were not recreated.

### 4. Network authority was then enabled only for the inherit profile

The same bounded profile was changed only by enabling network access. After the host-side Codexless restart, model-free context reported:

```text
inherit profile       ads-direct-git
networkAccess         true
.git writable         true
trusted ADS root      unchanged
```

A separate `access=readOnly` network probe still resolved to `:read-only` and could not reach GitHub. The network widening therefore did not leak into the read-only downscope.

### 5. The final `git fetch origin` did not reach Codex at all

After filesystem and inherit-network authority were both correct, ChatGPT attempted:

```text
git fetch origin
access=inherit
```

through generic model-free `codex.command_exec`.

The ChatGPT/OpenAI outer tool-safety layer blocked the tool invocation before local execution with the user-visible message:

```text
Deze toolaanroep is geblokkeerd door de veiligheidscontroles van OpenAI.
Controleer nogmaals wat je verzendt.
```

A subsequent generic `icacls .git` invocation was also blocked by the same outer layer. No local command was dispatched in either case.

The local repository therefore remained clean and unsynchronized, with local HEAD behind the public branch.

### 6. The current public Codexless command surface is generic

At the evaluated Codexless revision, the public model-free tool exposes an argv vector and local working-directory context through generic `codex.command_exec`, with `access` constrained to `inherit` or `readOnly`. The MCP declaration presents the operation as a general command-execution capability rather than a Git-specific semantic action.

Do not assume from this fact that a narrower tool would or would not be allowed. That is one of the questions to research.

## Minimum governing ADS read set

From the exact frozen target, inspect at least:

```text
Research 105's Codexless controlled-local-execution record
local-execution validation records 012 through 015
docs/model_collaboration/README.md
docs/DEVELOPMENT_METHOD.md
docs/CURRENT_STATE.md
docs/current_routing.json
```

Locate the Research 105 and validation 012-015 files by their numbered identities at the frozen target rather than guessing a filename or searching later branches.

Also inspect the exact upstream implementations needed to test claims, including the evaluated Codexless revision and the locally relevant OpenAI Codex release source where available. Do not rely only on repository summaries when upstream code is inspectable.

## Independent external research requirements

Use current primary sources and concrete implementation evidence where possible. Research broadly enough to avoid assuming that Codexless is the only relevant design.

Investigate at least:

```text
OpenAI Developer Mode / custom MCP documentation
OpenAI-described confirmation and blocking behavior for MCP write/modify tools
Model Context Protocol tool annotations and safety semantics
OpenAI Codex App Server command/process primitives relevant to local execution
Codexless public and internal/workbench execution architecture
reference or mature Git-focused MCP servers
other local-development MCP bridges used from ChatGPT or comparable MCP clients
concrete GitHub issues/discussions showing successful or blocked local Git operations
```

For community evidence, distinguish reproducible implementation facts from anecdotal reports.

## Architecture questions to answer independently

1. **Feasibility classification.** Is there credible evidence that ChatGPT Chat can dispatch bounded local Git operations through a custom MCP bridge? Is there credible evidence of a categorical platform prohibition? What is documented versus inferred?
2. **Outer safety-layer diagnosis.** What properties of an MCP tool can influence whether ChatGPT dispatches, confirms, or blocks it? Consider tool name, title, description, input schema, annotations, open-world behavior, command payload, user wording, app permission state, conversation context, and operation semantics. Which factors can be tested independently?
3. **Generic shell versus semantic operations.** Compare a generic argv/shell command tool with narrow purpose-built Git actions. Does a semantic tool materially reduce ambiguity or risk to the client safety layer? What evidence supports that conclusion?
4. **Correct MCP annotations.** How should fetch-like, status/read, strict fast-forward update, commit, and push operations be classified under `readOnlyHint`, `destructiveHint`, `idempotentHint`, and `openWorldHint`? Do not call an operation read-only merely because it leaves the checked-out working tree unchanged if it still mutates Git metadata.
5. **Execution primitive.** If a bounded Git façade is feasible, should it internally use Codex App Server `command/exec`, an App Server host-process primitive, a dedicated host-side Git implementation, or another mechanism? Compare permission fidelity, credential availability, network behavior, auditability, portability, failure modes, and attack surface.
6. **Authority bounding.** How should a tool be restricted to an already trusted repository? Should remote, branch/refspec, protocol, destination, and operation be fixed or locally allowlisted rather than caller-selected? How should strict fast-forward semantics be guaranteed mechanically? Which operations should remain unavailable by design?
7. **Credentials and network.** What is the smallest safe way for a local Git action to reuse legitimate host credentials/network access without exposing credentials to the remote caller? Does the recommended primitive alter the answer?
8. **Tool-contract versus immutable-platform test.** Design a minimal controlled experiment that can distinguish a generic-command-tool block, a categorical Git-specific block, confirmation-gated behavior, conversation/context-sensitive blocking, and a local executor failure after successful dispatch.
9. **Comparable implementations.** Find concrete projects/issues where ChatGPT or another MCP client successfully performs local Git fetch/pull/commit/push. Inspect their tool schemas/descriptions and execution mechanism where available. Identify whether the comparison is genuinely relevant to ChatGPT Web rather than only Claude Desktop or an IDE client.
10. **Security and trust.** Identify prompt-injection, repository-content, remote-URL, credential, refspec, submodule, hook, config, symlink/path, and command-injection risks relevant to a Git façade. Keep controls proportional to the user's trusted local ADS checkout, but do not assume repository contents are always benign.
11. **Strongest alternative.** What is the strongest architecture that avoids adding new MCP Git tools? Compare retaining generic `command_exec`, using the formal Codex lane, exposing a bounded existing process primitive, manual host Git, or another option.
12. **Abandonment criteria.** What empirical result would establish that the direct ChatGPT route is not worth further engineering and should defer Git mutations/synchronization to the formal Codex lane or another governed fallback?

## Required first-phase output

Write one durable independent research proposal at:

```text
docs/model_collaboration/threads/MC-0009/messages/001_claude_independent_chatgpt_local_git_mcp_feasibility_research.md
```

Preserve the normal collaboration provenance fields and include:

```text
exact ADS SHA reviewed
independence statement and known exposures
sources inspected, grouped as primary documentation / source code / community evidence
independent feasibility conclusion
strongest evidence for feasibility
strongest evidence against feasibility
outer safety-layer diagnosis
recommended architecture
recommended execution primitive and why
exact first MCP tool shape(s) to test, including names/descriptions/input schemas/annotations
minimal controlled experiment and success/failure criteria
authority and security boundaries
strongest alternative
abandonment criteria
what evidence would change the recommendation
explicit FACT / SOURCE_FINDING / COMMUNITY_OBSERVATION / INFERENCE distinction where material
```

Do not optimize for agreement with ChatGPT. No ChatGPT candidate implementation has been provided for this phase.

## Comparative second phase

After Claude's independent position is durably frozen, ChatGPT will independently disposition the findings and may freeze a concrete candidate architecture. Only then may MC-0009 enter a comparative phase in which Claude sees the ChatGPT candidate and challenges it.

The first Claude message must remain unchanged as the independent record.

## Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0009/messages/**
```

Do not modify Codexless, local-execution configuration, ACLs, Source Universe state, canonical ADS documentation, validators, workflows, current routing, the collaboration contract, or any other repository target state during the independent phase.

## Blocking semantics

MC-0009 blocks implementation of a new direct-Git MCP architecture until Claude's independent first-phase research is preserved and dispositioned by the ChatGPT task owner.

It does not reopen Research 105's already accepted bounded-local-execution result. It also does not itself authorize or resume Source Vault ingestion. The existing direct-lane authority audit remains the live project boundary while this focused collaboration is pending.