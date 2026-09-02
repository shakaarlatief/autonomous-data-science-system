# Current State

**Checkpoint:** 274
**Date:** 2026-09-02  
**Active development branch:** `v1-source-vault-bootstrap-resume`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Latest specification:** Specification 027  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-15
Conversation title       15 - Codex Desktop Thread Handoff and Source Vault Continuation
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: Codex Desktop handoff integration closed; reviewed Source Vault ingestion active

Checkpoint 274 closes the remaining cooperative Desktop release question for the tested scope and returns the active project boundary to reviewed Source Vault ingestion of the frozen 20-entry first corpus.

The completed integration architecture separates four layers:

```text
Codex thread persistence
Codex writer/process ownership
Codex Desktop sidebar/catalog reconciliation
durable cross-client thread identity and runtime-agent rehydration
```

H6 remains live: completed ADS Codex tasks expose the exact persisted `threadId` plus `codex://threads/<threadId>`, and the Rich Task Card's `Open in Codex Desktop` handoff was verified against a real same-thread Desktop continuation.

The durable identity is `threadId`; Codexless `agentRef` values are ephemeral runtime handles. Model-free `codex.agent_bind` remains verified, including re-binding after a complete Codexless restart.

The final cooperative handoff used disposable ADS-root thread `01a060d7-7249-78b2-b4a0-61cc4376da4f`. It was continued in Codex Desktop and archived through the supported Desktop UI while Desktop remained running. Newly published model-free `codex.thread_unarchive`, implemented through official `thread/read` plus `thread/unarchive`, successfully unarchived it. Model-free bind then returned fresh `agentRef` `agent_7d5d070f-24c0-470b-9164-2ca7db2623a4`. After normal metered user approval, turn `01a0628f-8415-77d3-9a8d-2ab29f204c53` resumed the same persisted thread and completed exact result `ARCHIVE_UNARCHIVE_REACQUIRE_COMPLETE`.

The accepted operational classifications are `UNARCHIVE_PATH=PASS`, `POST_UNARCHIVE_BIND=PASS`, and `ARCHIVE_RELEASES_DESKTOP_WRITER=PASS`. The last classification is scoped to the observed successful sequence; no claim is made about an unobserved internal instant at which the writer lease was released.

After restart, live Codexless health reported `toolCount 46` and tunnel ready HTTP 200. No private Codex DB/session/catalog write, forced process termination, Desktop quit, permission widening, cross-client forced unsubscribe, or safety workaround was used. The Codex handoff integration is closed for current scope.

The earlier direct synchronization result remains accepted for the exact frozen contracts:

```text
codex.git_fetch_origin
    VERIFIED
    fixed git fetch origin

codex.git_pull_ff_only
    VERIFIED
    fixed trusted ADS branch/upstream
    strict fast-forward only
    clean-tree fail-closed preconditions
    no caller-controlled Git arguments
```

The successful strict-fast-forward pull was also followed by another successful routine bounded synchronization using the same accepted contract.

Research 105 remains:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

Codexless remains a replaceable bounded local-execution transport. It is not project authority, a mandatory core dependency, a permission source, or an unrestricted host-control path.

The direct synchronization feasibility question that paused Source Vault work is closed for its exact accepted scope.

---

## What the investigation established

The investigation distinguished multiple execution layers rather than treating every failed attempt as the same failure:

```text
ChatGPT / OpenAI outer safety and dispatch
MCP action contract
Codexless routing and public surface
Codex authority/profile resolution
network authority
Codex command/exec sandbox
Windows filesystem ACLs / capability identities
Git semantics
repository branch/upstream/cleanliness state
postcondition verification
```

Key evidence sequence:

```text
generic codex.command_exec carrying Git
    BLOCKED BEFORE LOCAL EXECUTION

bounded codex.git_fetch_origin
    DISCOVERED
    DISPATCHED
    EXECUTED THROUGH MODEL-FREE CODEX command/exec
    EXIT 0

bounded codex.git_pull_ff_only first dispatch
    DISCOVERED
    DISPATCHED
    REACHED LOCAL EXECUTION
    FAILED AT .git/FETCH_HEAD WITH PERMISSION DENIED
    REPOSITORY UNCHANGED

read-only host diagnosis
    RECURRENT WINDOWS WORKSPACE-CAPABILITY DENY CONFIRMED ON .git
    INHERITED DENY CONFIRMED ON .git/FETCH_HEAD
    DEDICATED .git WRITABLE CAPABILITY STILL HAD MODIFY

guarded host ACL repair
    BACKUP CREATED
    EXACT TWO MATCHING EXPLICIT DENY RULES REQUIRED
    TWO -> ZERO IN-MEMORY GUARD PASSED
    ACL WRITTEN ONLY AFTER GUARDS PASSED
    POST-REPAIR DENY ABSENT
    EXPECTED MODIFY ALLOWANCES PRESENT

second separately authorized semantic pull dispatch
    DISPATCHED EXACTLY ONCE
    EXIT 0
    STRICT FAST-FORWARD VERIFIED
    CLEAN POSTFLIGHT VERIFIED
    OLD-HEAD ANCESTRY VERIFIED

later routine bounded synchronization
    EXIT 0
    STRICT FAST-FORWARD VERIFIED AGAIN
```

The first failed semantic pull was useful evidence because it localized the first failing layer after proving earlier layers had succeeded.

---

## Accepted Git boundary remains deliberately narrow

Accepted:

```text
fixed semantic fetch from origin
fixed trusted-branch strict-fast-forward pull
bounded network + Git-metadata authority
clean-tree and repository-state fail-closed checks
readOnly downscope to :read-only
postflight equality / cleanliness / ancestry verification
```

Not accepted merely because pull succeeded:

```text
arbitrary Git commands
commit
push
force push
reset
checkout
rebase
merge commits
arbitrary branch / remote / refspec selection
public codex.process
unrestricted host access
automatic ACL repair
permission widening to bypass a guard
```

Exact accepted capability is governed by:

```text
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
```

---

## Durable operational and investigation knowledge

Repository-owned operational procedures:

```text
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
```

The authority bootstrap is part of reproducible ADS operation. A healthy Codexless process or ready tunnel is not sufficient evidence that the ADS-specific `ads-direct-git` authority is active.

The Windows Git-metadata ACL condition is lifecycle-sensitive. The problematic workspace-capability DENY was observed to recur after later lifecycle activity even while the logical profile still reported `.git` as writable. The exact recreating lifecycle event was not isolated, so no stronger causal claim is made.

After relevant Codex/Codexless/sandbox lifecycle changes:

```text
restore and verify the ADS authority bootstrap
-> run the read-only ACL integrity gate before direct Git mutation
-> stop if a DENY is detected
```

ACL repair is never automatic merely to make a Git operation pass.

Broader reusable lessons are preserved in:

```text
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
```

The central methodological rule is disciplined claim scope:

```text
a failed route is not automatically an impossible capability
```

when multiple contracts or layers can still explain the result.

Future cross-layer investigations should localize the failure, research relevant contracts when ambiguity remains, design the smallest safe discriminating experiment, keep it fail-closed, preserve negative evidence by layer, change only the implicated layer, and keep successful claims bounded to the exact verified contract.

---

## Current Source Vault state

The Source Universe remained untouched throughout the direct Git investigation.

Current permanent Source Vault boundary:

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

The original source root and other machine/storage coordinates remain `RESOLVED_PRIVATE`. Their exact values must be retrieved from the accepted private/local continuity layer only when concrete execution requires them.

No Source Universe, Source Vault, original corpus, credential, backup payload, or recovery state was changed by the Codexless/direct-Git work.

---

## Exact next Source Vault action

The next substantive ADS action is:

```text
reviewed ingestion of the frozen 20-entry first corpus
```

Then:

```text
working-store integrity audit
-> deterministic backup staging
-> client-side encryption
-> independent remote replication
-> remote retrieval
-> encrypted-object digest reproduction
-> decryption
-> clean restore
-> restored integrity audit
-> Course 2 unblock only after the accepted recovery proof succeeds
```

The governing Source Vault procedure is:

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

---

## Repository integrity and development method

Research 103-108 and Specifications 024-027 continue to govern repository integrity and continuity.

Development Method v0.9 remains current.

Canonical numbered Checkpoint 274 is now the current meaningful project boundary. It preserves the completed Archive -> Unarchive -> Bind -> Resume sequence, closes the Codex Desktop handoff integration for current scope, and returns the active route to reviewed ingestion of the frozen 20-entry first corpus.

The public repository remains the sole project-development authority.

Any public branch mutation must pass Repository Integrity on its exact resulting HEAD before an exact-target `PUBLIC_REPOSITORY_INTEGRITY=PASS` claim is made.

Private continuity remains an orthogonal claim and must be reconciled to the exact public boundary when required for planned conversation rotation.

---

## Model collaboration state

MC-0009 remains `DEFERRED / NON-BLOCKING`.

The direct semantic fetch/pull experiments resolved the immediate feasibility question without requiring Claude Message 001. No Claude response is assumed to exist unless later preserved through the governed collaboration thread.

---

## Current canonical route

```text
docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md
docs/research/111_archive_unarchive_reacquire_closes_codex_desktop_handoff.md
docs/local_execution/validation/031_desktop_archive_unarchive_rebind_resume_verified.md
docs/checkpoints/273_durable_bidirectional_codex_thread_handoff_verified_cooperative_release_next.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/local_execution/validation/027_codex_desktop_deeplink_handoff_live_verified.md
docs/local_execution/validation/028_codex_desktop_catalog_writer_ownership_followup.md
docs/local_execution/validation/029_durable_thread_bind_restart_reacquisition_verified.md
docs/local_execution/validation/030_bound_active_writer_combined_live_test_blocked_by_platform_safety.md
docs/checkpoints/272_codex_desktop_thread_handoff_verified_deeplink_candidate_preflighted.md
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/current_routing.json
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

---

## Conversation-rotation boundary

Substantial Codex integration work continued in `chatgpt-15` beyond Checkpoint 273 and is now preserved as Checkpoint 274.

The repository is now sufficient to reconstruct the completed cooperative archive/unarchive handoff and the restored Source Vault boundary without relying on this chat. A deliberate rotation is valid after the current uncommitted preservation changes are reviewed, committed/pushed through the accepted route, and the required continuity/integrity gates are evaluated.

When rotation is chosen, follow `docs/CONTINUITY.md` and evaluate the actual transition evidence:

```text
exact-head public Repository Integrity PASS
required private continuity anchor reconciled and verified when applicable
local checkout synchronized with the public authority when required
no unrecorded archive/unarchive handoff state
CHAT_ROTATION_PREFLIGHT evaluated as PASS / HOLD / FAIL from actual evidence
```

A new persistent conversation must allocate a fresh provider-local session/title, reconstruct public authority first, recover any relevant private complement, and continue from the `source-vault-reviewed-first-corpus-ingestion` boundary unless the repository has advanced further.

---

## Minimum reading for continuation

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md
docs/research/111_archive_unarchive_reacquire_closes_codex_desktop_handoff.md
docs/local_execution/validation/031_desktop_archive_unarchive_rebind_resume_verified.md
docs/checkpoints/273_durable_bidirectional_codex_thread_handoff_verified_cooperative_release_next.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/checkpoints/272_codex_desktop_thread_handoff_verified_deeplink_candidate_preflighted.md
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/DEVELOPMENT_METHOD.md
```
