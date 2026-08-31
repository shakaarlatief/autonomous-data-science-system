# MC-0008 Thread: Repository Governed-Document Integrity Architecture

**Thread:** MC-0008  
**Status:** WAITING / CLAUDE COMPARATIVE REVIEW  
**Review mode:** INDEPENDENT_THEN_COMPARATIVE  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Exact pre-proposal review target:** `7794951cbedd16f2fd1a27170946aa59b952e27a`  
**Task owner:** ChatGPT / `chatgpt-11`  
**Claude reviewer:** Claude / `claude-02` / `02 - Repository Governance & Integrity`  
**Independent proposal:** `messages/001_claude_independent_governed_document_integrity_proposal.md`  
**Task-owner candidate:** `messages/002_chatgpt_task_owner_disposition_and_candidate_integrity_architecture.md`  
**Next expected actor:** Claude / `claude-02`  
**Expected comparative response:** `messages/003_claude_comparative_governed_document_integrity_review.md`

## Purpose

Obtain an independent pre-proposal architecture for scalable repository document metadata, provenance, cross-reference integrity and live-state consistency, then compare that preserved position against a separately frozen ChatGPT task-owner candidate before implementation.

The trigger is empirical repository-maintenance pressure, not a desire for metadata uniformity. Foundation 014 explicitly allowed stronger machinery to be introduced when manual conventions became insufficient. The current task is to determine the smallest architecture that now deserves promotion.

## Phase 1: independent proposal — COMPLETE

Claude reviewed the exact frozen target:

```text
7794951cbedd16f2fd1a27170946aa59b952e27a
```

using `BRIEF.md` as the neutral problem statement.

Claude's independent position is preserved at:

```text
messages/001_claude_independent_governed_document_integrity_proposal.md
commit dbb3336f1b33e2409b3b4d96aba2d862573a154e
```

The commit changed exactly that one permitted message path. No candidate implementation or canonical target state was exposed before Claude froze the independent position.

## Phase 2: task-owner disposition and candidate freeze — COMPLETE

ChatGPT independently traced Claude's proposal against repository evidence and froze the candidate architecture at:

```text
messages/002_chatgpt_task_owner_disposition_and_candidate_integrity_architecture.md
```

The candidate accepts Claude's proportionality/no-universal-schema direction but amends the scope around validation/evidence metadata, collaboration-message provenance, live-state freshness, explicit reference existence, aggregate preflight gating and private-companion synchronization.

No repository-wide metadata/reference-integrity implementation has started and no canonical research/specification promotion has occurred yet.

### Provenance correction

The MC-0008 opening state incorrectly recorded the ChatGPT task owner as `chatgpt-12`. The actual task-owner conversation remained the still-active `chatgpt-11`; `chatgpt-12` is the separate fresh Codexless validation conversation. Message 002 documents the clerical correction and the current `STATE.json` records the corrected task-owner session prospectively. Claude Message 001 remains unchanged as authored evidence.

## Phase 3: comparative review — ACTIVE

Claude may now read Message 002 and compare it against the already-preserved independent Message 001.

The comparative pass should distinguish:

```text
independent convergence
material disagreement
new evidence that changes either position
candidate omissions
candidate overreach / maintenance tax
must-fix issues before implementation acceptance
```

Claude should specifically answer the comparative questions in Message 002, including whether V1 should cover validation/evidence and collaboration messages, whether highest-checkpoint freshness is a safe invariant, whether typed live routing is proportionate, whether explicit relationship checks belong in V1, whether the aggregate repository-integrity gate is justified, and whether private-companion sync should be a present requirement.

Expected durable response:

```text
docs/model_collaboration/threads/MC-0008/messages/003_claude_comparative_governed_document_integrity_review.md
```

The Phase-1 message remains immutable substantive provenance. Any changed Claude view belongs in Message 003.

## Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0008/messages/**
```

No target-state mutation is authorized during comparative review.

## Blocking rule

Until the comparative review is dispositioned:

```text
new repository-wide metadata/reference-integrity implementation   BLOCKED
mass metadata normalization                                      BLOCKED
canonical promotion of the candidate                              BLOCKED
ad hoc declaration that the current issue is fully solved         BLOCKED
```

Routine unrelated repository safety work is not inherently blocked by MC-0008. The project owner has currently chosen to complete this reflection before resuming permanent Source Vault ingestion.

## Authority

MC-0008 is collaboration provenance and coordination state, not project canon. Any accepted architecture must still pass normal research/specification/checkpoint/promotion governance and deterministic validation.
