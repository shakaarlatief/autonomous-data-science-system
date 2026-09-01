# MC-0009 Thread: ChatGPT Local Git Through MCP Feasibility and Safety Architecture

**Status:** WAITING FOR CLAUDE INDEPENDENT RESEARCH  
**Mode:** INDEPENDENT_THEN_COMPARATIVE  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Independent review target:** `cb48c1ac539592e63b13cbc8e4e2413cb0b196a0`  
**Task owner:** ChatGPT / `chatgpt-14`  
**Independent reviewer:** Claude / `claude-03`  
**Project owner:** Human  
**Target-state write owner:** none during independent phase

## Objective

Determine whether ordinary ChatGPT Chat, through a trusted local MCP bridge, can practically dispatch bounded local Git operations without a Codex model-agent turn, and determine the smallest safe architecture and controlled experiment that can distinguish a tool-contract/safety-classification problem from an immutable platform prohibition.

The detailed neutral research contract is in `BRIEF.md`.

## Why this thread is independent first

The project has reached a real architecture boundary after proving local execution, a bounded Codex permission profile, explicit `.git` authority, Windows ACL repair, and inherit-only network access. The remaining generic `git fetch origin` attempt was blocked by the outer ChatGPT/OpenAI tool-safety layer before local dispatch.

ChatGPT has researched plausible next directions but has not frozen a candidate implementation in the repository. Claude should therefore form and durably preserve an independent position before seeing a ChatGPT candidate.

The independent phase is classified:

```text
BLIND_TO_CANDIDATE
```

Claude may use the problem facts and diagnostic evidence in `BRIEF.md`, the exact frozen repository target, upstream source, primary documentation, and external implementation/community evidence. Claude must not search later coordination-branch artifacts for a ChatGPT candidate before Message 001 is frozen.

## Post-freeze canonical preservation

The later diagnostic sequence already summarized neutrally in `BRIEF.md` has now also been preserved as the first-class local-execution validation record:

```text
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
```

That record was created after the frozen independent target. It is the canonical durable repository record for the post-015 ACL-confirmation/repair, inherit-network, and outer-tool-safety evidence, but it does **not** change the MC-0009 independent review target and is **not** part of Claude's substantive ADS evidence base for the `BLIND_TO_CANDIDATE` phase.

Before Message 001 is durably frozen, Claude should rely on the neutral facts already supplied in `BRIEF.md` and should not inspect validation 016. The reciprocal reference exists only so the collaboration state points to the canonical preservation location without silently moving the frozen review boundary.

## Phase 1: independent research

Claude reads the coordination branch only to locate this thread, then uses the exact frozen target for substantive ADS repository evidence.

Required output:

```text
docs/model_collaboration/threads/MC-0009/messages/001_claude_independent_chatgpt_local_git_mcp_feasibility_research.md
```

Claude must preserve its own evidence classification, feasibility judgment, architecture recommendation, exact first tool shapes/annotations to test, controlled experiment, security boundaries, strongest alternative, and abandonment criteria.

### Claude write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0009/messages/**
```

Claude must not modify target-state code/docs, Codexless configuration, ACLs, Source Universe state, current routing, this collaboration contract, or any unrelated repository path.

## Phase 1 gate

Implementation of a new direct-Git MCP architecture is blocked until:

```text
Claude Message 001 is durably preserved
+
ChatGPT verifies exact target/write-scope discipline
+
ChatGPT dispositions the independent findings
```

This gate does not reopen Research 105's accepted bounded-local-execution result and does not authorize Source Vault ingestion.

## Phase 2: comparative review

Only after the independent position is frozen may ChatGPT preserve a concrete candidate architecture for comparison. If the task owner then opens the comparative phase, Claude may inspect that candidate and challenge it.

Message 001 must remain unchanged as the independent record.

A comparative review should explicitly identify, whether supporting or disagreeing:

```text
strongest plausible failure mode
strongest alternative
material disagreement class, if any
what evidence would change the judgment
which parts remain provisional
```

## Resolution semantics

MC-0009 resolves only after the task owner has dispositioned the independent findings and any opened comparative phase has been completed or explicitly declined with a reason.

Resolution of MC-0009 can inform the direct-lane authority audit but does not itself:

```text
promote a new execution architecture
modify Codexless
change local permission profiles or ACLs
resume Source Vault ingestion
change scientific experiment state
```

Normal ADS research/specification/implementation governance remains required for any accepted architecture change.