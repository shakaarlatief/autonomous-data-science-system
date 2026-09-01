# MC-0009 Thread: ChatGPT Local Git Through MCP Feasibility and Safety Architecture

**Status:** CLAUDE INDEPENDENT RESEARCH DEFERRED / NON-BLOCKING  
**Mode:** INDEPENDENT_THEN_COMPARATIVE  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Independent review target:** `cb48c1ac539592e63b13cbc8e4e2413cb0b196a0`  
**Task owner:** ChatGPT / `chatgpt-14`  
**Independent reviewer:** Claude / `claude-03`  
**Project owner:** Human  
**Target-state write owner:** none while the collaboration review is deferred

## Objective

Determine whether ordinary ChatGPT Chat, through a trusted local MCP bridge, can practically dispatch bounded local Git operations without a Codex model-agent turn, and determine the smallest safe architecture and controlled experiment that can distinguish a tool-contract/safety-classification problem from an immutable platform prohibition.

The detailed neutral research contract is in `BRIEF.md`.

## Why this thread was independent first

The project reached a real architecture boundary after proving local execution, a bounded Codex permission profile, explicit `.git` authority, Windows ACL repair, and inherit-only network access. The remaining generic `git fetch origin` attempt was blocked by the outer ChatGPT/OpenAI tool-safety layer before local dispatch.

ChatGPT researched plausible next directions but did not freeze a candidate implementation before MC-0009 opened. Claude was therefore initially asked to form and durably preserve an independent position before seeing a ChatGPT candidate.

The intended first phase remains classified:

```text
BLIND_TO_CANDIDATE
```

if it is later resumed from the frozen target without exposure to descendant candidate material.

## Post-freeze canonical preservation

The later diagnostic sequence already summarized neutrally in `BRIEF.md` has also been preserved as the first-class local-execution validation record:

```text
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
```

That record was created after the frozen independent target. It is the canonical durable repository record for the post-015 ACL-confirmation/repair, inherit-network, and outer-tool-safety evidence, but it does not change the MC-0009 independent review target.

## Human routing decision: proceed without waiting for Claude

On 2026-09-01 the project owner explicitly chose to continue the direct-Git investigation without waiting for Claude's Message 001.

This changes the collaboration gate, not the value of the deferred research:

```text
Claude independent research          DEFERRED
blocking prerequisite for experiment REMOVED BY HUMAN ROUTING DECISION
frozen Claude review target          PRESERVED
ChatGPT task ownership               PRESERVED
new direct-Git architecture          NOT YET ACCEPTED
small bounded experiment             AUTHORIZED TO PROCEED
```

The accepted collaboration method explicitly allows collaborator unavailability or deferral not to globally block ADS unless a current accepted gate requires it. The project owner has now removed the MC-0009 Claude-first gate for this experimental boundary.

The deferred Claude obligation remains useful. If Claude later performs the original independent pass, it must still use the exact frozen target and avoid descendant candidate/implementation artifacts. If Claude has already seen later candidate material, the independence status must be reclassified rather than pretending the pass remained blind.

## Current ChatGPT experiment boundary

ChatGPT may now proceed with the smallest controlled experiment capable of testing the outer tool-contract hypothesis. The first experiment is governed in:

```text
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
```

The experiment must not widen the existing Codex permission profile, expose `codex.process`, change Secure MCP Tunnel authority, alter ACLs, or touch Source Universe state merely to make the test pass.

## Deferred Phase 1: independent research

If resumed while still legitimately blind to descendant candidate content, Claude's originally requested output remains:

```text
docs/model_collaboration/threads/MC-0009/messages/001_claude_independent_chatgpt_local_git_mcp_feasibility_research.md
```

Claude's write scope remains:

```text
docs/model_collaboration/threads/MC-0009/messages/**
```

Claude must not modify target-state code/docs, Codexless configuration, ACLs, Source Universe state, current routing, this collaboration contract, or any unrelated repository path.

## Deferred-review semantics

There is currently no Claude action that blocks the bounded semantic Git-fetch experiment.

If Claude later returns:

```text
1. preserve the exact review target and actual exposure status;
2. freeze Claude's findings as a numbered message;
3. compare the findings against whatever experimental evidence exists then;
4. do not retroactively claim that implementation waited for Claude;
5. inspect downstream reliance if Claude identifies a material defect.
```

## Comparative review

A comparative review remains optional after Claude's independent position is actually frozen. If the independent phase is no longer genuinely blind because Claude has seen descendant candidate content, use an honest comparative/adversarial classification instead.

A comparative review should explicitly identify, whether supporting or disagreeing:

```text
strongest plausible failure mode
strongest alternative
material disagreement class, if any
what evidence would change the judgment
which parts remain provisional
```

## Resolution semantics

MC-0009 is now a deferred, non-blocking collaboration thread. It may later be resumed, reclassified, or closed with an explicit reason.

The direct-lane engineering investigation proceeds under normal ADS research/validation governance independently of Claude's current availability.

MC-0009 itself still does not:

```text
promote a new execution architecture
modify Codexless
change local permission profiles or ACLs
resume Source Vault ingestion
change scientific experiment state
```

Normal ADS research/specification/implementation governance remains required for any accepted architecture change.