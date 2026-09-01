# Checkpoint 270: Codexless Controlled Write Verified, Local Execution Accepted

**Date:** 2026-09-01  
**Status:** Verified local-execution acceptance boundary  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Codexless local-execution evaluation closed after governed write/read/delete proof, before permanent Source Vault ingestion resumes  
**Scope:** Records the successful permission-aware local fast-forward, exact disposable write/read/delete validation, explicit Research 105 acceptance classification, and the resulting next continuation boundary.  
**Authority:** Historical verification provenance. `docs/research/105_codexless_local_execution_bridge_evaluation.md`, `docs/CURRENT_STATE.md`, and `docs/current_routing.json` govern current interpretation and continuation.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-14`  
**Conversation title:** `14 - Codexless Write Validation and Source Vault Resume`  
**Primary collaborator:** ChatGPT  
**Branch:** `v1-source-vault-bootstrap-resume`

## Why this checkpoint exists

Research 105 had remained deliberately open after the full fresh-chat read-only path was proven because ADS still lacked evidence that the same bridge architecture could perform a bounded local write safely, verify it exactly, remove it, and return the repository to a clean state.

That transition has now been proven against the real local ADS checkout.

The execution interaction used for the final test was a disposable diagnostic ChatGPT conversation. It did not consume a persistent ADS interaction-session number. The persistent coordination and durable preservation for this boundary belong to `chatgpt-14`.

## Synchronization and permission boundary

Before the controlled write, the clean local branch was one commit behind origin:

```text
local HEAD   284c99e094a44750404fa197da127bfaf6d9b93a
origin HEAD  063fdc99c76d7821efc58bb83823bcad33c068c5
```

The direct bridge command lane reached the local repository but could not write `.git/FETCH_HEAD` under the current `:workspace` / `workspaceWrite` sandbox. The failed `git pull --ff-only` made no mutation.

The formal Codex agent lane then requested approval for exactly:

```text
git pull --ff-only origin v1-source-vault-bootstrap-resume
```

The project owner granted a one-time approval only. No broader or persistent permission was granted as part of the test.

The strict fast-forward succeeded:

```text
284c99e094a44750404fa197da127bfaf6d9b93a
    ->
063fdc99c76d7821efc58bb83823bcad33c068c5
```

No merge, rebase, reset, commit, push, or GitHub write occurred in the local diagnostic.

## Controlled write/read/delete result

Exactly one disposable artifact was created:

```text
tests/research105_disposable_probe_20260901_7f3c9a2e.txt
```

Exact UTF-8 contents:

```text
Research 105 disposable controlled-write proof.
Nonce: 20260901-7f3c9a2e
```

Verification proved:

```text
text-exact match   True
byte-exact match   True
byte count         73
SHA-256            2489c0a51e8c8f003043b8bd59f75fbf46590301a243d316645b4e2f990be564
```

The artifact was then deleted and its final existence check returned `False`.

Final local repository state at the end of the diagnostic:

```text
local HEAD                                    063fdc99c76d7821efc58bb83823bcad33c068c5
origin/v1-source-vault-bootstrap-resume       063fdc99c76d7821efc58bb83823bcad33c068c5
working tree                                  clean
staged changes                                none
unstaged changes                              none
protected Source Universe mutation            none
```

The detailed evidence is preserved in:

```text
docs/local_execution/validation/012_controlled_write_read_delete_local_operation_verified.md
```

## Research 105 decision

Research 105 is now explicitly classified:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

This means Codexless is accepted as a **replaceable bounded local execution transport** for ADS work. It is not promoted into a core architectural authority or made a mandatory ADS product dependency.

The acceptance is deliberately nuanced:

```text
direct read / inspection path                proven
direct command execution                     proven within current sandbox authority
formal permission-aware write path           proven
controlled disposable write/read/delete      proven
visible sandbox denial                       proven
protected-state cleanup                      proven
browser integration                          deferred
```

The current direct command lane still cannot perform at least the Git metadata write required by `.git/FETCH_HEAD` under its present sandbox projection. That limitation is not hidden by the acceptance decision.

## Important observability finding

During the formal agent test, the visible Call Codex card continued to show `Codex running` while the underlying agent was actually paused in `awaitingApproval` for the exact Git command. The bounded agent-state query exposed the pending approval immediately.

Therefore future ADS supervision must distinguish the Rich Card presentation from authoritative agent state when progress appears stalled.

The persistent `chatgpt-14` conversation also experienced intermittent ChatGPT host rejection of Developer MCP invocation after earlier successful bridge calls. Fresh diagnostic conversations remained usable. This remains a host/runtime integration limitation to investigate rather than a reason to erase the successful local proof.

## Source Vault boundary

The Source Universe was not mutated by this validation.

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

Research 105 no longer blocks ingestion on local-execution acceptance grounds.

## Exact continuation after this checkpoint

Before resuming ingestion, the project owner selected one additional bounded engineering investigation: reconstruct the bridge/tunnel/Codex permission architecture from repository evidence and determine whether routine local writes and normal Git operations can be enabled safely through the direct ChatGPT -> bridge execution lane without requiring a formal Codex agent for every mutation.

That follow-up should distinguish:

```text
ChatGPT plug-in permission
Secure MCP Tunnel authority
Codexless transport policy
Codex project trust / permission profile
command/exec sandbox projection
.git metadata treatment
formal Codex agent approval routing
```

The goal is not unrestricted host access. The goal is the smallest safe authority model that permits routine ADS-local execution while keeping sensitive/private locations and unrelated host state outside the required boundary.

After that bounded authority audit is resolved or deliberately deferred, resume the permanent Source Vault bootstrap from the still-clean pre-ingestion boundary.

Any public repository commit preserving this checkpoint necessarily advances origin beyond the local validation target `063fdc99...`; therefore the local checkout must be fast-forwarded again before the next machine-local ADS mutation.

## Public preservation recovery note

During final public preservation, several sequential GitHub connector contents writes advanced the branch before the intended coherent multi-file tree was attached. The resulting bounded partial commits are `6f26aaf4edafd81292362074af8cf864fcd16c05`, `a2f215fe66c881049e0456e7ecc28df4ae54aad7`, `8c602f79d0137ac0b0155ed67f8d74246324b07a`, and `4aa981756378611f31668b28ccace178227840dd`. They contained only already-intended routing/checkpoint content or a no-content-change routing write. No force update, reset, deletion, or history rewrite was used. The final reconciliation commit is a normal descendant of those partial writes and must pass the same exact-target repository-integrity gates before the transition is considered accepted. This was bounded preservation-tooling residue only and did not alter the Research 105 local-execution evidence or Source Universe state.