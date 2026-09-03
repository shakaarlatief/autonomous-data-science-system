# Checkpoint 279: Generic Workspace Document Read and Architecture Backlog Qualified

**Date:** 2026-09-03
**Status:** ACCEPTED INFRASTRUCTURE / CONTINUITY BOUNDARY
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Codex/Codexless upstream research with generic ordinary-folder read authority and first-class PDF semantic reading live-qualified
**Scope:** Preserves the `workspace-standard` ordinary non-Git authority extension, live `codex.document_read` qualification, hardened isolated PDF parser boundary, private runtime evidence synchronization, and the new durable open-architecture backlog.
**Authority:** Historical infrastructure/continuity checkpoint. Research 113 remains the broader active upstream-research program; this checkpoint accepts the exact local authority/document-reading boundary verified by Validation 039.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-16`
**Conversation title:** `16 - Codex Live Task Viewer Publication and Source Vault Continuation`
**Primary collaborator:** ChatGPT
**Branch:** `v1-source-vault-bootstrap-resume`

## Accepted live surface

Codexless is now live at:

```text
version          0.1.1-preview.9
surface          codexless-public-preview-v2
public tools     52
```

The live MCP server itself exposes `codex.document_read`. A fresh disposable ChatGPT conversation then invoked that action successfully against a real PDF in a registered ordinary read-only workspace.

## Generic workspace extension

`workspace-standard` is accepted for ordinary non-Git filesystem/project authority. The first live use registered `big-data-statistics` with only `read`. The registry is now revision 3 with exact content hash:

```text
a1b430bc29bb29aa9736db3d63c92746be698d445043d12a1fedf7a61aa37319
```

This extends the already-accepted Research 116 architecture without reopening its core multi-repository decision. It proves that a normal personal/non-Git project folder can be admitted under the same stable workspace authority surface without adding another MCP action.

## Document-read boundary

`codex.document_read` is accepted for bounded embedded-text extraction from PDFs under existing workspace `read` authority. It owns/pins `pdfjs-dist@5.4.624`, returns source/parser/page provenance, and intentionally does not perform OCR or rendering.

Before publication, the parser was hardened into an isolated Node child process with a hard timeout and memory ceiling. File reads are byte-bounded and revalidated for identity/size after the read. The 11-test focused regression proves timeout termination/recovery and growth-bound behavior in addition to ordinary authority/media/path tests.

The decisive real-file qualification returned:

```text
workspaceId       big-data-statistics
file              BDS-exam-24-25-solutions.pdf
sha256            acaf11f8512a4b61f8887e3710a6c717676d6a9b8d9c418cbe8fa08cc9d3e9de
size              160885 bytes
pageCount         5
returnedPages     [1]
parser            pdfjs-dist@5.4.624
OCR               false
truncated         false
```

Validation 039 is the canonical exact evidence.

## Durable architecture backlog

`docs/OPEN_ARCHITECTURE_BACKLOG.md` is introduced as a compact durable index for explicit future architecture ideas, deferred investigations, known gaps, and continuation obligations that should not disappear merely because they arose as side tracks. It does not replace current state, open questions, research, or accepted specifications.

Important still-open areas include device-independent mobile tunnel access, host/runtime-maintenance authority, autonomous Codex supervision/wakeup, active-turn writer transfer, Rich Card actionability, cross-client spectator synchronization, v17 semantic task presentation, App Server steer/queue/reviewer investigation, and broader host-capability taxonomy.

The accepted `document_read` baseline is no longer an open backlog item; future document work is narrowed to visual rendering, explicit OCR, additional formats, and possibly stronger OS-level parser isolation.

## Private runtime preservation

The reviewed non-secret runtime implementation was synchronized to the private local-runtime repository and committed as:

```text
799390a5d0347b46e0be6caaf70a912ca83bac64
Preserve generic workspace and document reader runtime
```

The private push passed `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`, used one non-force push with `retried=false`, and ended with exact local/remote equality and `postflightOk=true`. A final provenance-only follow-up may advance `RUNTIME_STATE.json` to the public Checkpoint 279 commit after this public checkpoint is committed.

## Exact continuation

```text
1. commit and push this Checkpoint 279 public preservation with Repository Integrity PASS
2. advance private RUNTIME_STATE.json to the exact public Checkpoint 279 commit and push that provenance-only follow-up
3. verify a fresh Claude environment can access both public ADS and the private local-runtime repository for MC-0010
4. run the deliberate chat-rotation preflight
5. rotate to chatgpt-17 with the stable 52-tool surface
6. resume broader Research 113
7. keep the explicit architecture backlog open
8. resume Source Vault only after deliberate closure of the broader Level-2 research route
```
