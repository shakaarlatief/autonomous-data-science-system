# Research 563: R0-P03 reviewer-boundary feasibility and bounded source access

**Date:** 2026-10-13
**Status:** SOURCE_ACCESS_API_MECHANICS_QUALIFIED / FRESH_REVIEWER_EXECUTION_NOT_QUALIFIED
**Scope:** Inspect actual execution options, implement a small source-only access candidate, and examine reference custody and historical-event provenance without launching a reviewer or producing tasks/answers.
**Parent:** Research 513, 559-562; published Checkpoint 898; Validation 252; accepted public/private repository contracts.
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `35eb45064006c8fbfd2acce59d10ce32948146bf`.
**Interaction:** Existing exposed Codex/codex-01; ChatGPT/chatgpt-38 retains task ownership and independent acceptance.
**Authority:** Bounded engineering evidence. No fresh-reviewer attestation, OS/network isolation certification, private-store allocation, experiment freeze, new checkpoint or scoring authority.

## Actual execution evidence

Starting HEAD matched the owner's published basis, with an empty index and clean working tree. The existing capsule exporter, intake brief, method candidate and tests were read alongside the governing research and repository roles. The existing four-module suite passed **46/46** before this implementation.

The live Runtime Bridge `codex.project_context` call at the public repository returned CLI **0.162.0-alpha.17.2**, a `workspaceWrite` projection, `networkAccess=false`, and a public-repository workspace root. This is a model-free ephemeral bootstrap, not an inference or reviewer turn. Its implicit skill inventory returned **unavailable**, with `IMPLICIT_SKILLS_STRUCTURE_MISMATCH`; the reported zero count cannot be interpreted as proof that no skills/context exist. The same metadata call at the existing capsule scratch directory failed with **EPERM**. No authority or permission policy was changed to bypass it.

A live model-free `codex.command_exec` probe under its resolved **`:read-only`** profile read these three files successfully, returning only paths and byte counts:

| Outside the intended source world | Bytes read |
|---|---:|
| Original W5 `corpus_annotations_v02.json` | 15,486 |
| Current Research 562 | 11,217 |
| `.git/HEAD` | 49 |

Thus read-only execution protects against writes but does not exclude old gold, current designs or Git reads in this registered workspace. The public agent-start tool does not let callers choose a narrower permission profile, filesystem roots or network authority. Prompt wording and a new conversation cannot repair that observed access boundary. The current chat also has shell, web/browser and connector capabilities; a spawned command's network restriction is not evidence that every model-facing tool lacks external access. Official [OpenAI sandboxing documentation](https://learn.chatgpt.com/docs/sandboxing) likewise treats spawned-command enforcement and client/environment policy separately.

Local command discovery found Codex, Claude Code, Docker and WSL. PATH Codex reported **0.154.0**, distinct from the bridge's bootstrap executable; the two cannot be silently treated as the same tested runtime. Docker inspection failed on configuration access and a missing engine pipe. WSL enumeration returned `E_ACCESSDENIED`. These results establish **unavailable to this sandbox**, not global absence, an empty image inventory, or proof that no usable owner-controlled environment exists. No daemon was started, runtime installed, trust changed or elevation attempted.

Installed Claude Code **2.1.283** help provides a concrete prospective alternative. It describes `--restricted` removing command/code tools and confining built-in file tools, `--tools` selecting built-ins, `--strict-mcp-config` limiting configured MCPs, and `--safe-mode` suppressing customizations while leaving managed policy relevant. `--bare` suppresses inherited context but changes authentication and still needs explicit tool controls. These distinctions are corroborated by the [official CLI reference](https://code.claude.com/docs/en/cli-reference). No Claude session or model call was launched, no effective tool inventory or managed-policy audit was obtained, and no read-denial/network test ran inside that host. Help text establishes an available **configuration candidate**, not a qualified reviewer.

## Route comparison and observed qualification receipt

| Route | Fresh exposure | Filesystem/Git and model tools | External access | Submission/verifier evidence | Disposition |
|---|---|---|---|---|---|
| New ordinary Codex/bridge chat in the ADS checkout | New session could be fresh; existing codex-01 is exposed | Observed read-only route admits old W5/design/Git reads; no caller-selected source-only profile | Command network flag does not remove browser/search/connectors | Bootstrap and read-probe evidence exist; no restricted reference output flow | Does not meet the source-only boundary as tested. |
| Existing Claude Code restricted configuration | Must be a new, unresumed session with prior exposure declared | Useful installed flags; actual effective tool list, managed settings, source-root and link denials untested | Browser/web/MCP/hooks and transport still require concrete verification | Version/help evidence only; transcripts/stdout and output custody unqualified | Simplest existing host candidate for a subsequent non-semantic preflight. |
| Separately confined OS/container workspace | Must receive no prior conversation, gold or design context | Can separate mounts/accounts in principle; Docker/WSL unavailable here | Egress and host mounts require real inspection | No confined instance or receipt exists | Not technically qualified in this environment. |
| Exclusive function/MCP host using the new source API | Fresh request/session and full tool inventory remain host obligations | API admits only fixed corpus content; broader process/tool access is outside its control | API itself has no network operation; host transport/connectors unqualified | Exact source identities, commitments and negative tests are available; no reference submission tool | API mechanics qualified; end-to-end reviewer route unqualified. |

Observed receipt: **source-access mechanics PASS; fresh session/exposure NOT ATTESTED; exclusive model tool inventory NOT VERIFIED; reviewer OS/network boundary NOT VERIFIED; restricted complete-output flow NOT QUALIFIED; overall reviewer execution NOT QUALIFIED**. This is an engineering receipt about what ran, not a fabricated future-reviewer declaration. ChatGPT, Claude/claude-04 and Codex/codex-01 remain exposed and ineligible for fresh reference adjudication.

## Small useful source-access candidate

`source_only_access_candidate.py` adds a standard-library, importable `SourceOnlyAccess` object. A trusted coordinator supplies the capsule; the model-facing entry point is only `request(list/read/search)`. It starts no model, MCP service or permanent runtime, and has no write, Git, shell, URL-fetch, packet-submission or arbitrary-path operation. No generic Runtime Bridge implementation changed.

At initialization it checks the capsule roster and real regular files/directories, rejects symlinks and Windows junctions inside the capsule, requires exactly the original 65 source paths, verifies the pinned path@blob manifest and each Git-compatible blob identity, and independently verifies **1,725,920 bytes** and content digest `baf2b893435c1951b52814a3de897f7684890b1449bb437b46948cc868d304d3`. Trust comes from the pinned manifest/content commitments, not editable capsule receipt text. The original historical revision remains `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`; the original nine hints remain unchanged.

After initialization, requests use immutable memory only. Exact allowlisted names exclude traversal/absolute/drive-relative paths, original annotation/answer fixtures, current P03 material, Git metadata and the two capsule metadata files. Extra parameters and unknown operations fail with stable codes without host-path diagnostics. Lists/searches cap at 20 results, queries are literal and at most 128 characters, and reads cap at 100 lines/16,384 text characters. Results retain historical path, Git blob ID and SHA-256; line-preserving paged reads reconstruct every original source byte. Post-initialization disk changes cannot alter or expand the API snapshot.

Validation 252 records **44 new API tests plus 46 existing P03 tests = 90 PASS**, including a real Windows junction, corpus corruption/extension, manifest replacement, forbidden requests, bounded outputs and exact immutable-Git reconstruction. These tests qualify this API surface only. An importing Python process still has its ambient privileges, and a host exposing shell or other tools could bypass the API. The candidate is not yet registered as any model's exclusive tool surface and provides no authority-bearing answer storage.

## Complete-reference custody dependency

The public repository remains sole ADS development authority. The companion is a **knowledge-preservation complement only**; the private local-runtime repository preserves runtime/materialization evidence. Neither charter grants experimental gold custody. Existing historical Key Author execution records demonstrate a previous pattern of private artifacts outside Git and public commitment blocks, but their accepted experiment-specific permissions and paths are not reusable authority for P03. No private semantic payload was inspected or stored here.

The proportionate next custody option is an **owner-designated experiment-output location**, with a separately restricted reviewer/custodian identity and no premature arm-author access. Preserve each complete packet and source/version manifest as a retained immutable version, verify recovery/readback, and publish only its content commitment and permitted provenance before arm authoring. A mere private filename, same-account ACL assumption, or digest without retained bytes is insufficient. A dedicated new private Git repository is not necessary if an existing owner-controlled versioned retention mechanism can satisfy those conditions. No such destination or responsibility was allocated here; transcript logs, stdout and returned assistant text must also be covered so a hidden packet is not pasted into an arm author's chat.

## Historical owner-event route: source evidence beyond 36 headings

The inspected `docs/DECISIONS.md` at starting HEAD has Git blob `2369141f8134f01941f2c1b635780a5ec8fb7b2b`. Its 36 numbered records include 20 simply marked Accepted, six Accepted for V1, three explicitly superseded/partially superseded records, two selected-successor/non-operational records, and five other scoped acceptance statuses. These are decision summaries with dates, not a uniform archive of verbatim owner queries or independently sampled tasks.

Concrete provenance/closure checks establish limitations rather than selecting tasks:

- D-003 expressly says its exact visibility-change decision/date is not preserved. A mechanical heading selector cannot invent that missing event.
- D-011/D-015 have scoped supersession; D-035 remains an accepted historical selection while D-036 selects a later logical target and Specification 028 remains operational. A status/header-only rule cannot determine contemporary authority.
- D-026/D-027 concern Prototype V0 execution, while D-028 through D-033 concern different V1 technology/substrate choices. Counting these as equivalent whole-Project information needs would ignore domain and time scope.
- D-031/D-032 point beyond the ledger to schemas, specifications, executable/runtime evidence and results. Genuine cross-plane or impact closure requires exact referenced content and further dependency examination, not just the decision paragraph.
- D-036 has stronger event provenance: Research 502 identifies owner-artifact commit `7f31572466605c82f60a90034e1b2b05c7b865a1`. Direct Git-object inspection verifies the 1,007-byte `owner_decision.json` at SHA-256 `28ecf862a546c7aff2554877b061b661763571dae64b25ff5e63c361ceb4ab06`, bound to an exact candidate and packet. This verifies one event chain, not twelve independent tasks or four-category coverage.

No rule establishing three eligible events in each required category, independent question extraction, exact source/authority closure or a closure union fitting the future build world has been qualified. Therefore the mechanical route remains permitted but **not recommended as ready**. A fresh non-arm author also remains permitted; neither route was selected and no questions, labels or references were authored.

## Smallest next action and stopping boundary

No complete fresh-reviewer execution route was positively qualified. The exact missing capability is an **accessible, inspectable host that enforces the exclusive permitted source/tool/context surface and delivers output to an authorized restricted retained version**. The source API now supplies useful, tested access mechanics; adding speculative servers or changing generic trust cannot substitute for that host evidence.

The smallest next action is an owner-operated **non-semantic preflight** of the installed restricted Claude route, or another already available exclusive-tool host, with a source-only handoff destination and separately designated output custodian. Record the actual fresh/unresumed context, effective tools/managed policy, permitted-source reads, denials for old gold/design/Git and link escapes, external-tool/egress constraints, and synthetic-output retention/visibility. Return only a sanitized qualification receipt. This is a concrete environment/access action, not permission to adjudicate references. If the chosen host cannot prove those boundaries, use an owner-controlled confined account/container rather than widening the ADS workspace profile.

No additional checkpoint or routing transition is warranted: retain Checkpoint 898 and `p-three-reviewer-execution-authority-qualification`. Option A remains approved but unexecuted; original W5/Research 513, nine legacy cases >=8/9, twelve primary cases >=10/12 and zero false-authority tolerance remain unchanged. No evaluator, reference packet, selected task, held-out cohort, scoring, physical architecture selection or migration occurred. This unit remains uncommitted for independent ChatGPT inspection.
