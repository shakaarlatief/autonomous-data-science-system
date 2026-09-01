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

## Current active stage: Codexless local execution accepted, direct-lane authority audit before Source Vault resume

Research 105 has crossed the controlled-write boundary and is now closed as:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

The accepted result is deliberately scoped. Codexless is accepted as a **replaceable bounded local execution transport**, not as a new project authority, mandatory core dependency, or permission source.

The final controlled local validation proved the full sequence against the real ADS checkout:

```text
clean local checkout synchronized by strict fast-forward
local HEAD == origin-tracking HEAD
one exact disposable artifact created
text-exact readback PASS
byte-exact readback PASS
disposable artifact deleted
working tree returned clean
protected Source Universe state unchanged
```

Detailed evidence is preserved in:

```text
docs/local_execution/validation/012_controlled_write_read_delete_local_operation_verified.md
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
```

---

## Research 105 acceptance evidence

Before synchronization, the local checkout was clean at:

```text
284c99e094a44750404fa197da127bfaf6d9b93a
```

while the matching origin-tracking branch was at:

```text
063fdc99c76d7821efc58bb83823bcad33c068c5
```

The direct bridge command lane reached the real local repository but the current `:workspace` / `workspaceWrite` command-execution sandbox denied the `.git/FETCH_HEAD` write required by `git pull --ff-only`.

The formal Codex agent lane then entered the normal exact-command approval path. The project owner granted a one-time approval for only:

```text
git pull --ff-only origin v1-source-vault-bootstrap-resume
```

The strict fast-forward succeeded without merge, rebase, reset, commit, push, or GitHub write.

The disposable proof used:

```text
tests/research105_disposable_probe_20260901_7f3c9a2e.txt
```

with exact UTF-8 content:

```text
Research 105 disposable controlled-write proof.
Nonce: 20260901-7f3c9a2e
```

and verified:

```text
text-exact match   True
byte-exact match   True
byte count         73
SHA-256            2489c0a51e8c8f003043b8bd59f75fbf46590301a243d316645b4e2f990be564
```

The artifact was deleted, final existence was `False`, and the final local status was clean with local HEAD and origin both at `063fdc99c76d7821efc58bb83823bcad33c068c5`.

A public preservation commit created after that local proof necessarily advances origin beyond the validation target. Before the next machine-local ADS mutation, the local checkout must therefore be fast-forwarded again to the then-current public HEAD.

---

## Direct-lane permission and supervision follow-up

Research 105 acceptance does not hide the observed execution asymmetry:

```text
direct read / inspection                 PASS
direct command execution                 PASS within current sandbox authority
direct Git metadata write                BLOCKED at .git/FETCH_HEAD under current command/exec sandbox
formal permission-aware Git operation    PASS after exact one-time approval
controlled disposable local write        PASS
```

The project owner selected a bounded post-acceptance audit before permanent Source Vault ingestion resumes.

The audit must reconstruct the actual implementation and prior setup from repository authority rather than guess from current UI behavior. It should distinguish at least:

```text
ChatGPT plug-in permission
Developer MCP host capability
Secure MCP Tunnel authority
OpenAI tunnel-client/runtime-key authority
Codexless transport configuration
Codex project trust / permission profile
command/exec sandbox projection
workspace writable roots
.git metadata treatment
formal Codex agent approval routing
```

The goal is **not** unrestricted host access. The goal is to determine whether routine ADS-local writes and ordinary Git operations can be enabled safely through the direct ChatGPT -> bridge lane, using the smallest authority required, while unrelated host state, sensitive locations, credentials, private source material and browser authority remain outside the required boundary.

If that refinement is not safely configurable or is not worth the complexity, Research 105 remains accepted through the already-proven formal permission-aware path.

---

## Known current Codexless integration limitations

The following observations remain material:

1. The current direct `command_exec` sandbox can deny Git metadata mutation even when the repository working tree is otherwise inside the workspace authority ceiling.
2. During the formal Codex test, the visible Call Codex card remained in `Codex running` while the underlying agent was actually `awaitingApproval`. The bounded agent-state query exposed the exact pending command. Future supervision should not equate the Rich Card presentation with authoritative agent state when progress appears stalled.
3. The persistent `chatgpt-14` conversation experienced intermittent ChatGPT host rejection of Developer MCP invocation after earlier successful bridge calls. Fresh disposable diagnostic conversations remained usable. This is a host/runtime integration limitation, not evidence that the local transport proof failed.
4. The formal Call Codex card reported a high token-usage figure for the bounded task. The accounting semantics and cause are not yet audited, so no cost/efficiency conclusion is frozen from that observation alone.
5. Browser integration remains deferred.

---

## Repository integrity hardening remains accepted

The v0.8/v0.9 repository-integrity architecture remains the governing continuity and public-integrity framework. The reconciled public target at `284c99e094a44750404fa197da127bfaf6d9b93a` passed the full Repository Integrity workflow on Ubuntu and Windows, and the later historical-intermediate extension at `063fdc99c76d7821efc58bb83823bcad33c068c5` also passed the exact public workflows before the Research 105 local synchronization.

The integrity architecture continues to distinguish numbered checkpoints from governed historical intermediate milestones. Canonical numbered Checkpoint 252 remains:

```text
docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md
```

The useful earlier source-faithful reintegration milestone remains preserved as:

```text
docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md
```

No renumbering of later checkpoints occurs.

Any new public branch mutation must pass the Repository Integrity workflow on its own exact HEAD before a new `PUBLIC_REPOSITORY_INTEGRITY=PASS` claim is made for that target.

---

## Current canonical route

The governing route for the current boundary is:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/local_execution/validation/011_fresh_chat_read_only_local_operation_verified.md
docs/local_execution/validation/012_controlled_write_read_delete_local_operation_verified.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/CONTINUITY.md
docs/DEVELOPMENT_METHOD.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

Repository-integrity background remains governed by Research 103-108 and Specifications 024-027.

Development Method v0.9 remains the current operational method.

---

## Source Vault remains paused and unchanged

The local-execution proof did not authorize or perform source ingestion.

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

The original source root and other machine-specific operational coordinates remain `RESOLVED_PRIVATE`. Their exact values do not belong in public Git.

The next-generation Project Cockpit frontend exploration remains paused at its previously frozen state.

Research 105 itself no longer blocks Source Vault ingestion. The current pause exists because the project owner selected the bounded direct-lane authority audit as the next engineering step before ingestion resumes.

---

## Interaction-provenance naming clarification

The canonical naming guide has been clarified for this session boundary.

The abstract pattern:

```text
NN - Main Topic / Stage
```

uses `/` as explanatory notation meaning "main topic or stage". A literal slash is **not required punctuation**. Natural human wording is preferred, including conjunctions such as `and` when a title combines related concepts.

Therefore this session correctly uses:

```text
14 - Codexless Write Validation and Source Vault Resume
```

Historical titles that accurately record the title actually used are not retroactively rewritten merely for cosmetic conformity.

The canonical rule lives in:

```text
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
```

---

## Public/private/preflight claims remain separate

The integrity architecture distinguishes:

```text
PUBLIC_REPOSITORY_INTEGRITY
    PASS | FAIL

PRIVATE_CONTINUITY_INTEGRITY
    PASS | FAIL | NOT_VERIFIED

CHAT_ROTATION_PREFLIGHT
    PASS | HOLD | FAIL
```

A public PASS never proves private freshness. After the public commit preserving Checkpoint 270 and Research 105 closure, the private companion's public-safe synchronization anchor must be reconciled separately before a new private PASS is claimed for that boundary.

No deliberate chat rotation is currently required. A future rotation claim must evaluate the exact public target, required private continuity and any then-open transition obligations rather than inheriting an older PASS/HOLD state.

---

## Exact continuation order

From the Research 105 acceptance boundary:

```text
1. preserve Research 105 closure and Checkpoint 270 coherently
2. require the complete Repository Integrity workflow to pass on the exact new public HEAD
3. reconcile the private companion public-safe anchor to that exact public commit and verify private continuity separately
4. before further local work, fast-forward the local checkout from the validation target to the new public HEAD
5. reconstruct and audit the direct-lane permission architecture from durable repository evidence
6. determine whether a smaller safe direct-write/Git authority configuration exists or keep the proven formal approval lane
7. resume reviewed ingestion of the frozen 20-entry first corpus into the permanent Source Registry and Source Vault
8. run the working-store integrity audit before accepting any backup
9. continue deterministic encrypted backup, remote retrieval, decryption, clean restore and restored integrity proof
```

Do not weaken repository-integrity validators or Source Universe safety boundaries merely to simplify the local execution path.

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

Then read the governing current boundary:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/local_execution/validation/012_controlled_write_read_delete_local_operation_verified.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/DEVELOPMENT_METHOD.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

Read Research 106-108 and Specifications 025-027 when repository-integrity details are relevant to the next mutation.

When relevant and accessible, retrieve the private companion only after the public reconstruction.

The public repository remains the sole project-development authority.
