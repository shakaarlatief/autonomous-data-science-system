# Current State

**Checkpoint:** 271  
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
Interaction session      chatgpt-14
Conversation title       14 - Codexless Write Validation and Source Vault Resume
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: direct bounded Git investigation closed, Source Vault reviewed ingestion next

Checkpoint 271 closes the bounded post-Checkpoint-270 investigation into whether the direct model-free ChatGPT -> bounded MCP -> Codex command/exec route can safely perform the ADS synchronization needed before Source Vault work resumes.

The answer is accepted for the exact frozen contracts:

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

Canonical numbered Checkpoint 271 is now the current meaningful project boundary. It closes the direct Git feasibility investigation and returns the project to Source Vault continuation.

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
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
docs/local_execution/validation/019_bounded_semantic_git_pull_ff_only_contract_frozen.md
docs/local_execution/validation/020_semantic_git_pull_ff_only_dispatched_local_fetch_head_denied.md
docs/local_execution/validation/021_semantic_git_pull_ff_only_verified_after_acl_repair.md
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/current_routing.json
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

---

## Conversation-rotation boundary

This is a natural planned-rotation point for `chatgpt-14`.

The durable project boundary is already Source Vault ingestion next. Planned rotation must still follow `docs/CONTINUITY.md` and evaluate the actual transition evidence rather than assuming readiness from prose.

Required transition checks are external to the durable checkpoint itself:

```text
exact-head public Repository Integrity PASS
required private continuity anchor reconciled and verified
local checkout fast-forwarded if it is behind the public authority
no other open transition obligation
CHAT_ROTATION_PREFLIGHT evaluated as PASS / HOLD / FAIL from actual evidence
```

A final local synchronization after this checkpoint is expected because public preservation advances the branch. That operational catch-up does not create another project checkpoint and should not be copied into live state as a permanently volatile exact local-HEAD fact.

If rotation passes, the new persistent conversation must use the standard continuation procedure in `docs/CONTINUITY.md`, allocate a fresh provider-local session/title, reconstruct public authority first, and then retrieve relevant private complement where available.

---

## Minimum reading for continuation

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/validation/021_semantic_git_pull_ff_only_verified_after_acl_repair.md
docs/DEVELOPMENT_METHOD.md
```
