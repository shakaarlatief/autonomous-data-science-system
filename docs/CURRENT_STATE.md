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

## Current active stage: semantic direct Git fetch verified, stronger synchronization contract next

Research 105 remains accepted as:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

Codexless remains accepted only as a **replaceable bounded local execution transport**. It is not a project authority, mandatory core dependency, permission source, or unrestricted host-control path.

The post-acceptance direct-lane authority audit has now established an important additional capability boundary:

```text
generic codex.command_exec carrying git fetch origin
    BLOCKED BY CHATGPT/OPENAI BEFORE LOCAL EXECUTION

bounded codex.git_fetch_origin
    DISCOVERED BY CHATGPT
    DISPATCHED THROUGH THE NORMAL HOST SAFETY LAYER
    EXECUTED THROUGH THE EXISTING CODEX AUTHORITY BACKEND
    git fetch origin EXIT 0
```

The completed fetch-specific evidence is preserved in:

```text
docs/local_execution/validation/013_direct_lane_git_metadata_permission_profile_source_audit.md
docs/local_execution/validation/014_direct_git_profile_runtime_application_partial.md
docs/local_execution/validation/015_direct_git_profile_active_metadata_write_denied_windows_acl_investigation.md
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
```

Validation 018 is the current fetch-specific result owner.

---

## Direct-lane audit result to date

The audit separated several distinct layers rather than treating local Git as one permission switch.

### Codex profile and Windows filesystem boundary

The custom direct profile is:

```text
profile                  ads-direct-git
extends                  :workspace
trusted ADS root         C:\Projects_Data\autonomous-data-science-system
explicit writable root   .git
inherit networkAccess    true
readOnly downscope       :read-only
authority source         host-profile-override
```

The earlier `.git/FETCH_HEAD` denial was not caused by profile-selection failure. Host inspection confirmed a stale Windows workspace-capability DENY ACE persisted alongside the newer `.git` writable capability. Exactly the stale workspace-SID deny rules on `.git` were removed, leaving the narrower `.git` capability intact.

After that ACL repair, the filesystem boundary was crossed successfully and the next inner failure was network-disabled execution. The inherit profile was then widened only with `network={enabled=true}`. `access=readOnly` continued to downscope to `:read-only` and did not inherit that network widening.

### Outer ChatGPT tool-safety boundary

With filesystem and inherit-network authority ready, a final generic `codex.command_exec` request containing `git fetch origin` was blocked by ChatGPT/OpenAI before local dispatch.

No wrapper, alternate command, `codex.process`, Codex agent, or disguised fallback was used to route around that block.

This established the A-side observation for the later semantic-tool experiment.

---

## Semantic Git fetch experiment

Validation 017 froze a dedicated action:

```text
codex.git_fetch_origin
```

The caller schema is a strict empty object. The caller cannot choose:

```text
command
cwd
remote
URL
refspec
branch
credentials
permission profile
```

Internally the action is fixed to:

```text
git fetch origin
```

through the same existing Codex authority executor and official Codex App Server `command/exec` path with:

```text
access      inherit
timeout     30 seconds
profile     ads-direct-git
```

The conservative MCP annotations remain:

```text
readOnlyHint     false
destructiveHint  true
idempotentHint   false
openWorldHint    true
```

The experiment did not mislabel fetch as read-only or additive-only merely to influence host safety behavior.

---

## Codexless live-factory correction and public surface

The first local experimental patch added the new allowlist entry correctly but registered the action in a factory that the running public HTTP path did not use. That produced a real MCP initialize failure because the live allowlist contained a tool that the actual server configuration had not registered.

The implementation was corrected so the semantic action is registered in the live `mcp-server-factory.mjs` path, only for `publicPreview`, while preserving the same authority backend and narrow caller contract.

Focused syntax/contract checks passed.

The live surface then became:

```text
Codexless version              0.1.1-preview.5
total MCP actions              43
private app-only actions        3
publicly callable actions      40
```

The three private app-only actions remain:

```text
codex.agent_card_state
codex.agent_commit
codex.agent_decline
```

The Secure MCP Tunnel recovered to:

```text
/healthz   200 live
/readyz    200 ready
```

The existing ChatGPT developer MCP app was refreshed through its `Vernieuwen` action. Fresh ChatGPT discovery then reported 40 publicly callable tools and exposed `codex.git_fetch_origin`.

---

## Validation 018 execution result

Immediately before the single semantic fetch call:

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

`codex.git_fetch_origin` was invoked exactly once and returned:

```text
exit status             0
stdout                  empty
stderr                  empty
requested access        inherit
effective profile       ads-direct-git
permission ceiling      ads-direct-git
authority source        host-profile-override
```

Read-only post-inspection showed local `HEAD`, upstream commit, status and working tree unchanged.

`.git/FETCH_HEAD` was demonstrably refreshed:

```text
before timestamp  2026-09-01T16:45:08.3729850Z
after timestamp   2026-09-01T17:25:19.4063452Z
length             8711 bytes before and after
SHA-256            f1e35235bc0b4679e1577222d36fc8e6ce3bd3007a8104eefe340feafb91592d before and after
```

The timestamp change proves the fetch executed and refreshed Git metadata. The unchanged digest shows the fetched reference content available at that moment had not changed.

No pull, merge, checkout, reset, rebase, commit, push, agent, process tool, wrapper, or alternate fetch mechanism was used.

---

## Current interpretation

The strongest supported conclusion is:

```text
ChatGPT -> bounded semantic MCP action -> Codex command/exec -> Git fetch
    VERIFIED for codex.git_fetch_origin on the trusted ADS repository
```

The A/B result supports that the MCP action contract materially affected dispatchability for this exact operation. It does **not** prove that semantic naming alone controls ChatGPT safety decisions, that every bounded semantic action will be dispatched, or that Git operations in general are accepted.

The direct lane is therefore more capable than the earlier generic-command observation suggested, while remaining intentionally bounded.

The following stronger operations are still untested and unaccepted:

```text
pull
merge
checkout
reset
rebase
commit
push
arbitrary Git subcommands
arbitrary host process execution
```

---

## Next direct-lane engineering boundary

The next useful question is checked-out-branch synchronization, not another fetch test.

A possible future action is conceptually:

```text
codex.git_pull_ff_only
```

but **no implementation is authorized yet by Validation 018**.

A separate contract must be frozen first because fast-forward pull can change local `HEAD` and working-tree files. That contract should specify at least:

```text
fixed trusted repository
fixed current configured upstream/origin behavior
strict fast-forward-only semantics
clean-tree and branch preconditions
no merge commit
no rebase
no reset
no checkout
no force behavior
no arbitrary caller command/remote/refspec
exact authority profile
postcondition/status verification
failure and uncertainty handling
outer ChatGPT dispatch as a separately observed result
```

If a direct semantic pull route is not worth the additional complexity or is blocked, the already-proven formal Codex permission-aware synchronization path remains available.

---

## Source Vault remains paused and unchanged

No Source Universe or permanent Source Vault state was touched during the direct-lane Git audit or semantic fetch experiment.

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

Canonical numbered Checkpoint 270 remains the latest numbered checkpoint. Validation 018 is a meaningful fetch-specific experimental result inside the still-open direct-lane synchronization investigation, so no new numbered checkpoint is created by this preservation step.

Any new public branch mutation must pass the Repository Integrity workflow on its exact new HEAD before a new exact-target `PUBLIC_REPOSITORY_INTEGRITY=PASS` claim is made.

The public repository remains the sole project-development authority.

---

## Model collaboration state

MC-0009 remains `DEFERRED / NON-BLOCKING`.

Claude's originally planned independent feasibility research was not required to proceed with the bounded experiment. A later counter-design or independent review may still be useful, but it is not an acceptance gate for the verified fetch result.

No Claude Message 001 is assumed to exist unless it is later preserved in the governed collaboration thread.

---

## Current canonical route

The governing route for the current boundary is:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
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

From the verified semantic-fetch boundary:

```text
1. preserve Validation 018 and refresh CURRENT_STATE/current_routing coherently
2. require Repository Integrity to pass on the exact preservation HEAD
3. before the next machine-local ADS mutation, recognize that the local checkout is still behind the public branch and must be synchronized through an accepted route
4. if continuing the direct-lane investigation, freeze a separate strict fast-forward pull contract before implementing or dispatching any semantic pull tool
5. otherwise deliberately defer that stronger experiment and use the already-proven formal Codex synchronization route
6. once the direct-lane synchronization boundary is resolved or deliberately deferred, resume reviewed ingestion of the frozen 20-entry first corpus
7. run the working-store integrity audit before accepting any backup
8. continue deterministic encrypted backup, remote retrieval, decryption, clean restore and restored integrity proof
```

Do not weaken Git safety, repository-integrity validators, Source Universe controls, or private/public separation merely to simplify local execution.

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
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/DEVELOPMENT_METHOD.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

When relevant and accessible, retrieve the private companion only after the public reconstruction.