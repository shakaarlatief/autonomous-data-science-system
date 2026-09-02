# Checkpoint 271: Bounded Direct Git Synchronization Verified, Source Vault Resume Ready

**Date:** 2026-09-02  
**Status:** Verified infrastructure-closure checkpoint  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Direct bounded Git synchronization investigation closed; permanent Source Vault reviewed ingestion ready to resume  
**Scope:** Records the completed post-Checkpoint-270 investigation into safe direct model-free ADS Git synchronization, the verified bounded semantic fetch and strict-fast-forward pull contracts, the Windows ACL diagnosis and guarded repair boundary, repeated successful synchronization, durable operational procedures, reusable investigation lessons, and the return to Source Vault continuation.  
**Authority:** Historical verification and continuity provenance. Exact accepted Git capability is governed by `docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md`; current continuation is governed by `docs/CURRENT_STATE.md`, `docs/current_routing.json`, and `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-14`  
**Conversation title:** `14 - Codexless Write Validation and Source Vault Resume`  
**Primary collaborator:** ChatGPT  
**Branch:** `v1-source-vault-bootstrap-resume`

## Why this checkpoint exists

Checkpoint 270 accepted Codexless as a replaceable bounded local-execution transport after controlled write/read/delete proof, but it deliberately left one follow-up question open before Source Vault ingestion resumed:

```text
Can routine ADS synchronization be performed safely through the direct
ChatGPT -> bounded MCP -> Codex command/exec lane without requiring a
model-bearing Codex agent for every Git mutation?
```

That question has now been answered for an exact bounded contract.

The investigation produced both a verified capability and broader reusable ADS knowledge. It therefore constitutes a meaningful closure boundary rather than another micro-iteration inside Checkpoint 270.

## What changed after Checkpoint 270

The post-270 sequence established:

```text
permission/profile architecture reconstructed
    ->
custom ads-direct-git authority selected and verified
    ->
Windows .git capability/ACL interaction diagnosed
    ->
bounded semantic git fetch contract frozen and verified
    ->
bounded semantic strict-fast-forward pull contract frozen
    ->
first semantic pull dispatched and localized to .git/FETCH_HEAD denial
    ->
recurrent workspace-capability DENY confirmed by read-only host diagnosis
    ->
exact guarded ACL repair performed after backup and rule-count guards
    ->
semantic strict-fast-forward pull dispatched again exactly once
    ->
strict fast-forward succeeded with clean postflight and ancestry proof
    ->
routine bounded synchronization succeeded again
    ->
operational/bootstrap/ACL procedures and investigation lessons preserved
```

The detailed chronology is owned by Validations 013 through 021 and the accepted semantic-pull record.

## Layered failure localization

The investigation demonstrated that superficially similar failures occurred at different layers and therefore required different interpretations.

The relevant stack included:

```text
ChatGPT / OpenAI outer safety and dispatch
MCP action contract
Codexless routing and public surface
Codex authority/profile resolution
network authority
Codex command/exec sandbox
Windows filesystem ACLs and capability identities
Git semantics
repository branch/upstream/cleanliness preconditions
postcondition verification
```

The generic `codex.command_exec` Git attempt was blocked before local execution. A later bounded semantic fetch reached and succeeded through the same underlying model-free Codex command execution path. Therefore the generic-command failure was not evidence that Git synchronization was categorically impossible through every bounded direct contract.

The first semantic pull then reached local execution but failed at `.git/FETCH_HEAD`. That negative result positively established that discovery, outer dispatch, Codexless routing, authority selection, network-enabled execution and local command execution had already succeeded. The remaining failure was localized to effective Git-metadata filesystem authority.

## Windows ACL diagnosis and guarded repair

Read-only host inspection confirmed that the workspace capability SID again had two explicit DENY entries on `.git`, inherited by `.git/FETCH_HEAD`, while the dedicated `.git` writable capability still had Modify authority.

The repair remained narrowly bounded:

```text
backup current .git ACL
require exactly two matching explicit DENY rules
remove only those exact rules in memory
require exactly zero matching explicit DENY rules before write
write repaired ACL
verify workspace DENY absent
verify expected Modify allowances remain
```

The exact lifecycle event that recreated the DENY was not isolated. ADS therefore does not claim a stronger causal mechanism than the evidence supports.

Instead, the lifecycle-sensitive condition is now governed operationally by:

```text
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
```

A detected DENY remains a stop condition. ACL repair is never automatic merely to make a Git operation succeed.

## Verified semantic strict-fast-forward pull

After diagnosis and guarded repair, one separately authorized second semantic pull dispatch succeeded.

The contract remained fixed and caller-nonparameterized:

```text
git pull --ff-only --no-rebase --no-tags --no-recurse-submodules origin v1-source-vault-bootstrap-resume
```

The successful verification established:

```text
semantic action discovery       PASS
outer dispatch                  PASS
Codexless routing               PASS
ads-direct-git authority        PASS
network authority               PASS
local Codex command/exec        PASS
strict fast-forward             PASS
branch/upstream preservation    PASS
working-tree cleanliness        PASS
local/tracking equality         PASS
old-HEAD ancestry               PASS
```

The experimental success was then followed by another routine bounded synchronization using the same accepted contract. That second success reduced the possibility that the accepted run depended on an unexplained one-off state.

## Accepted capability boundary

The direct model-free route is accepted for the exact semantic contracts documented in the local-execution acceptance record:

```text
fixed semantic git fetch origin
fixed trusted-branch strict-fast-forward pull
clean-tree and repository-state fail-closed preconditions
bounded network + Git-metadata authority
readOnly still downscopes to :read-only
clean postflight and ancestry verification
```

This checkpoint does not authorize neighboring Git capability merely because pull succeeded.

Still unaccepted:

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
permission widening to bypass a failed guard
```

The accepted direct route remains model-free and bounded. The formal Codex agent remains a separate model-bearing route rather than the definition of direct-lane feasibility.

## Operational reproducibility preserved

The investigation also exposed that process liveness is not equivalent to correct ADS authority.

Starting the Codexless launcher in a fresh shell without the required ADS-specific `CODEXLESS_*` parent environment caused authority to fall back to the ordinary workspace profile. This bootstrap knowledge is now durable rather than chat-dependent.

Current public-safe operational owners are:

```text
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
```

## Reusable investigation lessons

The broader Level-2 lessons are preserved in:

```text
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
```

The most important methodological conclusion is:

```text
a failed path
    is not automatically
an impossible capability
```

when multiple contracts or system layers can still explain the observed result.

The reusable investigation pattern is:

```text
observe the exact failure
-> identify the last proven layer and first suspected failing layer
-> separate the target feasibility question from available fallback routes
-> research the relevant contracts / implementation
-> formulate competing explanations
-> design the smallest safe discriminating experiment
-> keep the experiment fail-closed
-> preserve positive and negative evidence by layer
-> change only the layer implicated by evidence
-> retest the same bounded contract
-> reverify lifecycle-sensitive state
-> preserve reproducible operational knowledge durably
```

This is disciplined persistence, not indefinite trial and error.

## Source Vault boundary remained unchanged

No Source Universe, original-source corpus, Source Registry content, Source Vault payload, credential, backup payload or recovery state was modified during this investigation.

The permanent Source Vault boundary remains:

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

Machine-specific source and storage coordinates remain `RESOLVED_PRIVATE`.

## Current project transition

The direct Git synchronization feasibility investigation is closed for its exact accepted scope.

Therefore the active project route returns to:

```text
reviewed ingestion of the frozen 20-entry first corpus
-> working-store integrity audit
-> deterministic encrypted backup staging
-> independent remote replication
-> remote retrieval + encrypted-object digest reproduction
-> decryption
-> clean restore
-> restored integrity audit
-> Course 2 unblock only after recovery proof succeeds
```

The Source Vault sequence remains governed by `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`.

## Verification and rotation boundary

This checkpoint is accepted only with the repository-integrity gate green on the exact public commit that introduces it and reconciles the live routing state.

The public/private continuity anchor must then be reconciled to that exact public boundary when the private companion is required for planned chat rotation.

A final machine-local fast-forward may still be needed after public preservation because creating this checkpoint necessarily advances the public branch beyond the previously synchronized local checkout. That synchronization is an operational transition check, not a reason to create another checkpoint.

## Exact continuation

After this checkpoint and its exact-target integrity verification:

```text
1. reconcile the private continuity anchor to this public checkpoint boundary
2. fast-forward the local ADS checkout through the accepted bounded pull if it is behind
3. evaluate CHAT_ROTATION_PREFLIGHT without overclaiming PASS before all required evidence exists
4. start the next persistent ADS conversation using docs/CONTINUITY.md
5. allocate a fresh provider-local interaction session/title
6. reconstruct public state first and private complement only when relevant
7. resume reviewed Source Vault ingestion from repository authority
```

Do not reopen the direct Git investigation merely because Source Vault work resumes. Reopen only if a new observed failure or materially broader capability question justifies it.
