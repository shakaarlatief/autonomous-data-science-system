# MC-0008 Thread: Repository Governed-Document Integrity Architecture

**Thread:** MC-0008  
**Status:** WAITING / CLAUDE INDEPENDENT PROPOSAL  
**Review mode:** INDEPENDENT_THEN_COMPARATIVE  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Exact pre-proposal review target:** `7794951cbedd16f2fd1a27170946aa59b952e27a`  
**Task owner:** ChatGPT / `chatgpt-12`  
**Next expected actor:** Claude / intended fresh session `claude-02`  
**Expected first durable message:** `messages/001_claude_independent_governed_document_integrity_proposal.md`

## Purpose

Obtain an independent pre-proposal architecture for scalable repository document metadata, provenance, cross-reference integrity and live-state consistency before ChatGPT freezes or implements a candidate solution.

The trigger is empirical repository-maintenance pressure, not a desire for metadata uniformity. Foundation 014 explicitly allowed stronger machinery to be introduced when manual conventions became insufficient. The current task is to determine the smallest architecture that now deserves promotion.

## Phase 1: independent proposal

Claude reviews the exact frozen target:

```text
7794951cbedd16f2fd1a27170946aa59b952e27a
```

using `BRIEF.md` as the neutral problem statement.

Claude must freeze its own recommendation before seeing any later ChatGPT candidate design or implementation. The intended independence classification is `BLIND_TO_CANDIDATE` with the exposures recorded in `STATE.json`.

Claude may write only:

```text
docs/model_collaboration/threads/MC-0008/messages/**
```

No target-state mutation is authorized during this phase.

## Phase 2: task-owner disposition and possible candidate freeze

After the independent Claude message exists, ChatGPT will:

```text
verify the exact target and provenance
trace the findings against repository evidence
disposition each material recommendation
separate demonstrated requirements from optional refinements
freeze a concrete architecture only if justified
preserve unresolved disagreement explicitly
```

If ChatGPT freezes a concrete proposal, the collaboration state will be updated before Claude sees it.

## Phase 3: comparative review if a candidate is frozen

Claude may then compare the frozen ChatGPT proposal with its already-preserved independent position.

The comparative pass should distinguish:

```text
independent convergence
material disagreement
new evidence that changed either position
candidate omissions
candidate overreach / maintenance tax
must-fix issues before implementation acceptance
```

The Phase-1 message remains immutable substantive provenance. Any later changed view belongs in a new numbered message.

## Blocking rule

Until Phase 1 is preserved and dispositioned:

```text
new repository-wide metadata/reference-integrity implementation   BLOCKED
mass metadata normalization                                      BLOCKED
ad hoc declaration that the current issue is fully solved         BLOCKED
```

Routine unrelated repository safety work is not inherently blocked by MC-0008. The project owner has currently chosen to complete this reflection before resuming permanent Source Vault ingestion.

## Authority

MC-0008 is collaboration provenance and coordination state, not project canon. Any accepted architecture must still pass normal research/specification/checkpoint/promotion governance and deterministic validation.