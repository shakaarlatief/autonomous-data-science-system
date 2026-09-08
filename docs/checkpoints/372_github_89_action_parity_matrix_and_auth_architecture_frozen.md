# Checkpoint 372: GitHub 89-Action Parity Matrix and Authentication Architecture Frozen

**Date:** 2026-09-08
**Status:** PASS / 89 ACTIONS MAPPED / PREIMPLEMENTATION SCHEMA CAPTURE NEXT
**Checkpoint class:** RESEARCH + ARCHITECTURE DESIGN BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve the complete exact-name mapping of the historical 89-action native GitHub connector baseline, the selected GitHub App/device-flow authentication and REST/GraphQL architecture, the parity safety/error/pagination/mutation contracts, and the final evidence gate before implementation.
**Authority:** Research 123 and `docs/research/GITHUB_CONNECTOR_PARITY_MATRIX.md` own the design; Validation 128 owns the native qualification evidence; `github_connector_89_action_inventory.json` owns the machine-readable action inventory.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Exact baseline is now mapped

The public repository previously preserved the exact native action count and capability families but not every action name. Research 123 now owns a durable 89-entry inventory reconstructed from the two 2026-09-08 GitHub-only qualification transcripts and cross-checked against Validation 128.

Mechanical result:

```text
repository / installation / branch / commit / file / raw Git   29
issues                                                           17
Actions / CI                                                       9
pull requests / reviews                                           33
repository permission                                              1
TOTAL                                                              89
unique native actions                                              89
unique target actions                                              89
negative-challenge new actions                                      0
```

`python scripts/check_github_connector_parity_inventory.py` returns:

```text
GITHUB_CONNECTOR_89_ACTION_INVENTORY=PASS
```

Every native `GitHub.<action>` has a one-for-one preferred target `github.<action>` plus read/write classification, current parity state, reuse basis and target REST/GraphQL transport.

## 2. Current parity is explicitly zero, not partially claimed

Inspection of the current Runtime Bridge implementation finds no remote GitHub API layer. The existing generalized semantic Git tools are local-repository capabilities and therefore do not count as remote connector parity.

```text
exact remote Runtime Bridge parity now   0 / 89
mapped missing actions                   89 / 89
reusable local architecture              YES
```

This avoids falsely calling local `git_fetch`, `git_commit_paths` or `git_push_ff_only` equivalents of GitHub repository/PR/issue/Actions objects.

## 3. Authentication architecture selected

The preferred production architecture is a dedicated **GitHub App** with user authorization through GitHub's device flow.

This is not merely a security preference. Installation-aware baseline actions require GitHub App user-token semantics. The architecture is:

```text
ChatGPT
    -> Runtime Bridge github.* semantic tools
        -> GitHubAuthority
            -> dedicated GitHub App
            -> device-flow user authorization
            -> expiring user access token + refresh lifecycle
            -> server-owned protected secret storage
        -> internal GitHubApiTransport
            -> REST
            -> GraphQL where required
```

Repository scope follows GitHub App installation selection and the authenticated user's permissions. Runtime Bridge does not impose a weaker second repository whitelist merely for convenience.

Tokens/secrets are never MCP arguments/results and never ordinary Git. The Windows secret-store implementation remains a focused implementation qualification, with OS-protected DPAPI/Credential Manager mechanisms preferred over plaintext state.

## 4. API and behavior contracts selected

The design now preserves:

```text
internal server-owned REST/GraphQL transport
no arbitrary caller HTTP / URL / method / token / header
server-owned GitHub API version
installation-derived repository scope
structured HTTP + GraphQL error evidence
valid-empty distinct from API failure
action-specific pagination rather than one global policy
search total/incomplete metadata where returned
stale-SHA and expected-head concurrency failures
non-force raw-ref behavior where observed
no blind retry after uncertain mutations
resource/file handoff for workflow artifact ZIPs
merge methods + optional expected_head_sha
exact issue/review/comment/thread identity
```

Raw Git maps to GitHub's Git Database REST API. Pull-request draft/auto-merge/review-thread state uses GraphQL where it best preserves the native object model. Actions rerun remains limited to the two observed rerun families for first parity closure.

## 5. Public tool-surface direction

The preferred public shape remains explicit one-action-per-tool parity:

```text
GitHub.get_user_login -> github.get_user_login
...
GitHub.get_repo_collaborator_permission -> github.get_repo_collaborator_permission
```

The current 63-tool Runtime Bridge plus 89 GitHub tools would total 152 tools. This is treated as an empirical host-projection question under AB-008, not as a reason to weaken capability in advance. Implementation will expand in coherent slices and fresh-chat qualify projection/schema fidelity after each surface change.

## 6. Local reconnaissance

The machine has GitHub CLI 2.97.0, but its configured GitHub API token currently fails `gh auth status` as invalid. Existing semantic Git pushes remain healthy through the separate Git credential path.

This is useful architecture evidence:

```text
Git transport authentication != GitHub API authentication
```

Production therefore will not depend on the current GitHub CLI credential as the parity authority. It will use the dedicated GitHub App contract.

No credential was changed in this checkpoint.

## 7. Final preimplementation evidence gap

Validation 128 preserved the 89-action count and live capability evidence but not the complete native schemas. Implementing from guessed schemas would undermine the parity objective.

A discovery-only procedure is now preserved at:

```text
docs/research/GITHUB_CONNECTOR_SCHEMA_CAPTURE.md
```

One fresh GitHub-only conversation should first freeze its actual projected action count, then capture the 89 baseline schemas in six manageable follow-up batches. No GitHub action needs to be invoked and no mutation is permitted.

If the future projection differs from 89, preserve the new projection separately rather than rewriting the historical baseline.

## 8. Exact continuation

```text
1. run the fresh GitHub-only read-only schema capture;
2. reconcile captured schemas into the 89-action inventory/matrix;
3. mechanically derive the exact GitHub App permission manifest from official endpoint requirements;
4. implement G0 auth/secret/API kernel in the private local-runtime repository;
5. qualify G1 read-only identity/installation/repository discovery;
6. continue G2-G7 incrementally through all 89 actions;
7. separately implement/qualify the live connector display-name rename;
8. close Research 123 only after practical parity is evidence-backed.
```

Research 113 remains paused, not closed. Source Vault remains paused. The owner's separately planned next stage remains deferred behind explicit Research 123 closure or redirect.

```text
CHECKPOINT372=GITHUB_89_ACTION_PARITY_MATRIX_FROZEN
GITHUB_ACTION_NAMES_MAPPED=89_OF_89
GITHUB_INVENTORY_VALIDATOR=PASS
EXACT_REMOTE_PARITY_NOW=0_OF_89
AUTH_ARCHITECTURE=GITHUB_APP_USER_TOKEN_DEVICE_FLOW
TARGET_PUBLIC_ACTIONS=89_EXPLICIT_GITHUB_TOOLS
NATIVE_SCHEMA_CAPTURE=PENDING
IMPLEMENTATION=NOT_STARTED
RESEARCH123=ACTIVE
NEXT=FRESH_READ_ONLY_89_ACTION_SCHEMA_CAPTURE
```
