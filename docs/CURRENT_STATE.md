# Current State

**Checkpoint:** 270  
**Date:** 2026-09-01  
**Active development branch:** `v1-source-vault-bootstrap-resume`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Latest specification:** Specification 027 extends Specifications 025/026 with governed historical-intermediate checkpoint integrity and discoverability.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-14
Conversation title       14 - Codexless Write Validation and Source Vault Resume
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: semantic Git fetch verified, strict fast-forward pull contract frozen

Research 105 remains accepted as:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

Codexless remains accepted only as a **replaceable bounded local execution transport**. It is not a project authority, mandatory core dependency, permission source, or unrestricted host-control path.

The post-acceptance direct-lane audit has now established two distinct boundaries:

```text
generic codex.command_exec carrying git fetch origin
    BLOCKED BY CHATGPT/OPENAI BEFORE LOCAL EXECUTION

bounded codex.git_fetch_origin
    DISCOVERED BY CHATGPT
    DISPATCHED THROUGH THE NORMAL HOST SAFETY LAYER
    EXECUTED THROUGH THE EXISTING CODEX AUTHORITY BACKEND
    git fetch origin EXIT 0
```

The fetch-specific evidence is preserved in:

```text
docs/local_execution/validation/013_direct_lane_git_metadata_permission_profile_source_audit.md
docs/local_execution/validation/014_direct_git_profile_runtime_application_partial.md
docs/local_execution/validation/015_direct_git_profile_active_metadata_write_denied_windows_acl_investigation.md
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
```

Validation 018 is the fetch-specific result owner.

The next checked-out-branch synchronization experiment is now frozen separately in:

```text
docs/local_execution/validation/019_bounded_semantic_git_pull_ff_only_contract_frozen.md
```

Validation 019 authorizes only the bounded local implementation and controlled dispatch experiment defined there. It does not yet prove or accept semantic pull.

---

## Direct-lane authority result to date

The custom direct profile remains:

```text
profile                  ads-direct-git
extends                  :workspace
trusted ADS root         C:\Projects_Data\autonomous-data-science-system
explicit writable root   .git
inherit networkAccess    true
readOnly downscope       :read-only
authority source         host-profile-override
```

The earlier `.git/FETCH_HEAD` denial was caused by a stale Windows workspace-capability DENY ACE persisting alongside the narrower `.git` writable capability. The exact stale workspace-SID deny rules on `.git` were removed. After that repair, the remaining network boundary was widened only for the inherit profile with `network={enabled=true}`.

`access=readOnly` continues to downscope to `:read-only` and does not inherit the broader execution profile.

With filesystem and inherit-network authority ready, generic `codex.command_exec` carrying `git fetch origin` was still blocked by ChatGPT/OpenAI before local dispatch. No wrapper, alternate command, `codex.process`, Codex agent, or disguised fallback was used to route around that block.

---

## Verified semantic Git fetch boundary

Validation 017 froze `codex.git_fetch_origin` as a strict empty-schema semantic action. The caller cannot choose command, cwd, remote, URL, refspec, branch, credentials, or permission profile.

Its fixed backend is:

```text
git fetch origin
```

through the same existing `CodexAuthorityExecutor.exec()` and official Codex App Server `command/exec` path with:

```text
access      inherit
timeout     30 seconds
profile     ads-direct-git
```

The truthful annotation contract remains:

```text
readOnlyHint     false
destructiveHint  true
idempotentHint   false
openWorldHint    true
```

The first local patch exposed a live-factory registration defect: the allowlist contained the new tool but the running HTTP factory had not registered it, causing MCP initialize to fail. The tool was moved into the actual `mcp-server-factory.mjs` public-preview path and the focused live-factory contract test passed.

The refreshed live surface became:

```text
Codexless version              0.1.1-preview.5
total MCP actions              43
private app-only actions        3
publicly callable actions      40
```

The Secure MCP Tunnel recovered to:

```text
/healthz   200 live
/readyz    200 ready
```

The existing ChatGPT developer MCP app was refreshed. Fresh ChatGPT discovery then reported 40 publicly callable tools and exposed `codex.git_fetch_origin`.

Validation 018 then invoked the semantic fetch exactly once:

```text
exit status             0
stdout                  empty
stderr                  empty
requested access        inherit
effective profile       ads-direct-git
permission ceiling      ads-direct-git
authority source        host-profile-override
```

Before and after the fetch:

```text
branch
    v1-source-vault-bootstrap-resume

local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume
    ca42678c9873d350ab5dd9d2b577f36eecdc5854

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 12]

working tree
    clean
```

`.git/FETCH_HEAD` was demonstrably refreshed while its contents remained unchanged:

```text
before timestamp  2026-09-01T16:45:08.3729850Z
after timestamp   2026-09-01T17:25:19.4063452Z
length             8711 bytes before and after
SHA-256            f1e35235bc0b4679e1577222d36fc8e6ce3bd3007a8104eefe340feafb91592d before and after
```

No pull, merge, checkout, reset, rebase, commit, push, agent, process tool, wrapper, or alternate fetch mechanism was used.

The strongest supported conclusion remains:

```text
ChatGPT -> bounded semantic MCP action -> Codex command/exec -> Git fetch
    VERIFIED for codex.git_fetch_origin on the trusted ADS repository
```

This does not prove that semantic naming alone controls ChatGPT safety decisions or that Git operations in general are accepted.

---

## Frozen semantic strict-fast-forward pull contract

Validation 019 now freezes the next experiment before any local implementation.

The action is:

```text
codex.git_pull_ff_only
```

with a strict empty caller schema. The first experiment fixes:

```text
trusted repository  host-configured ADS root
branch              v1-source-vault-bootstrap-resume
upstream            origin/v1-source-vault-bootstrap-resume
remote              origin
```

The caller cannot choose command, cwd, remote, URL, refspec, branch, credentials, permission profile, merge strategy, or rebase mode.

The tool must fail closed unless the exact branch/upstream are active and the index/working tree are clean with no untracked files or ambiguous in-progress Git operation state.

The fixed mutation is:

```text
git pull --ff-only --no-rebase --no-tags --no-recurse-submodules origin v1-source-vault-bootstrap-resume
```

through the same Codex authority backend with `access=inherit` and the existing `ads-direct-git` ceiling.

The explicit flags are part of the safety contract:

```text
--ff-only                 refuse non-fast-forward history changes
--no-rebase               prevent pull.rebase configuration from rebasing
--no-tags                 avoid unnecessary tag expansion
--no-recurse-submodules   avoid recursive submodule activity in the first test
```

The implementation must preserve read-only preflight/postflight through `:read-only`, must not auto-retry an uncertain mutation, and must not roll back with reset/checkout/rebase or any other compensating write.

A successful postflight must establish at least:

```text
branch unchanged
working tree clean
index clean
local HEAD after
origin-tracking HEAD after
local HEAD == origin-tracking HEAD
pre-operation HEAD is ancestor of post-operation HEAD when HEAD changes
```

The annotation contract remains conservatively truthful:

```text
readOnlyHint     false
destructiveHint  true
idempotentHint   false
openWorldHint    true
```

Validation 019 also records the residual trusted-Git-environment boundary: normal repository/host Git behavior such as configured hooks or checkout filters is not new caller authority, but the implementation must not add or widen such mechanisms. If inspection finds active behavior that materially broadens the expected effect, stop before dispatch and preserve that fact.

Expected local experimental surface after implementation:

```text
total MCP actions          44
private app-only actions    3
publicly callable actions  41
```

Implementation is authorized by Validation 019 but has not yet been performed. ChatGPT dispatch of the stronger semantic action is therefore still untested.

---

## Stronger Git operations remain unaccepted

The following remain untested and unaccepted unless explicitly covered by the strict fast-forward experiment above:

```text
merge commits
checkout
reset
rebase
commit
push
force behavior
arbitrary Git subcommands
arbitrary host process execution
```

The already-proven formal Codex permission-aware synchronization route remains available if the semantic pull experiment is blocked, fails closed, or is deliberately abandoned.

---

## Source Vault remains paused and unchanged

No Source Universe or permanent Source Vault state was touched during the direct-lane Git audit, semantic fetch experiment, or pull-contract preservation.

The permanent Source Universe remains frozen at:

```text
permanent Source Registry           MIGRATED / VERIFIED
Alembic head                        0003_source_universe
SQLite tables                       33
first permanent corpus compare      20 / 20 MATCH
DIFFERENT_ARTIFACT                  0
MISSING_LOCAL_SOURCE                0
ADDITIONAL_LOCAL_SOURCE             0
source ingestion                    NOT STARTED
working-store integrity audit       PENDING
independent encrypted backup proof  PENDING
clean restore + restored audit      PENDING
Course 2                            BLOCKED
```

The original source root and other machine-specific operational coordinates remain `RESOLVED_PRIVATE` and do not belong in public Git.

Source Vault ingestion remains paused because the project owner chose to finish or deliberately bound the direct-lane synchronization investigation before resuming ingestion.

---

## Repository integrity and development method

Research 103-108 and Specifications 024-027 continue to govern repository integrity and continuity.

Development Method v0.9 remains current.

Canonical numbered Checkpoint 270 remains the latest numbered checkpoint. Validation 019 freezes the next experiment inside the still-open direct-lane synchronization investigation, so no new numbered checkpoint is created by this contract-preservation step.

Any new public branch mutation must pass the Repository Integrity workflow on its exact new HEAD before a new exact-target `PUBLIC_REPOSITORY_INTEGRITY=PASS` claim is made.

The public repository remains the sole project-development authority.

---

## Model collaboration state

MC-0009 remains `DEFERRED / NON-BLOCKING`.

Claude's originally planned independent feasibility research was not required for the bounded fetch experiment and does not block the pull experiment. A later counter-design or independent review may still be useful.

No Claude Message 001 is assumed to exist unless it is later preserved in the governed collaboration thread.

---

## Current canonical route

The governing route for the current boundary is:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
docs/local_execution/validation/019_bounded_semantic_git_pull_ff_only_contract_frozen.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/model_collaboration/threads/MC-0009/STATE.json
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

Repository-integrity background remains governed by Research 103-108 and Specifications 024-027.

---

## Exact continuation order

From the frozen strict-fast-forward pull contract:

```text
1. preserve Validation 019 and refresh CURRENT_STATE/current_routing coherently
2. require Repository Integrity to pass on the exact contract-preservation HEAD
3. reconstruct the local Codexless implementation baseline from the verified 43-action fetch-patched runtime
4. implement only codex.git_pull_ff_only according to Validation 019, with focused syntax/contract tests and no authority widening
5. restart/refresh the local MCP runtime and existing ChatGPT app, expecting 44 total actions and 41 publicly callable actions
6. perform read-only discovery/authority verification and stop before mutation if any contract invariant differs
7. dispatch codex.git_pull_ff_only exactly once under the frozen experiment, with no command_exec/process/agent/wrapper fallback
8. perform only the frozen read-only postcondition checks and preserve the exact result
9. if direct synchronization is verified or deliberately deferred/abandoned, close this bounded authority investigation coherently
10. resume reviewed ingestion of the frozen 20-entry first corpus only after that boundary is resolved
11. run the working-store integrity audit before accepting any backup
12. continue deterministic encrypted backup, remote retrieval, decryption, clean restore and restored integrity proof
```

Do not weaken Git safety, repository-integrity validators, Source Universe controls, private/public separation, or ChatGPT/OpenAI platform safety merely to make the experiment pass.

---

## Minimum reading for continuation

Bootstrap-critical first reads:

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

Then read the current direct-lane boundary:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
docs/local_execution/validation/019_bounded_semantic_git_pull_ff_only_contract_frozen.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/DEVELOPMENT_METHOD.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

When relevant and accessible, retrieve the private companion only after the public reconstruction.
