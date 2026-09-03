# ChatGPT tool projection refresh and connector coexistence observations

**Date:** 2026-09-03
**Status:** `PASS / HOST-BEHAVIOR OBSERVATION PRESERVED`
**Scope:** Preserve two ChatGPT-host observations relevant to Codexless architecture: stale MCP action projection in an existing conversation after a tool-surface refresh, and repeated failure of the native GitHub connector when a developer MCP is active.
**Authority:** Host/integration observation only. This record does not define OpenAI product guarantees. Official documentation and current product behavior may change independently.
**Declared references:** `research:113`, `research:116`, `path:docs/local_execution/validation/033_semantic_git_commit_push_surface_publication_and_public_ads_push_verified.md`, `path:docs/local_execution/OPERATIONS.md`

## 1. Existing conversation retained an older action projection

After semantic Git commit/push tools were published, the live Codexless MCP server exposed 50 tools and a fresh disposable ChatGPT conversation successfully discovered:

```text
codex.git_commit_paths
codex.git_push_ff_only
```

The long-running canonical `chatgpt-16` conversation continued to expose its earlier callable tool projection and could not call those two new tool names directly.

The same backend still accepted calls to already-known actions such as `codex.command_exec`, `codex.read_many`, and `codex.precise_edit`.

Bounded conclusion:

```text
new MCP action name/schema
    may require a refreshed/fresh conversation to become callable

backend/policy change behind an already-known stable action
    can remain usable from the existing conversation
```

This is an important architectural reason to keep future action schemas stable and move repository/project variability into server-owned configuration/authority state.

## 2. Fresh-chat discovery showed two different counts

The fresh disposable validation observed:

```text
live Codexless MCP tools/list count      50
ChatGPT connector resource projection    46
```

The two newly published semantic Git tools were present in the ChatGPT projection and callable despite the count difference.

Therefore:

```text
toolCount reported by live MCP
!= automatically
number of callable connector resources projected by ChatGPT
```

The difference must not automatically be diagnosed as stale discovery without comparing visibility/app-only/private resources.

## 3. Native GitHub connector coexistence problem

The project owner repeatedly opened fresh ChatGPT conversations and attempted to use both:

```text
@ADS Codexless Local Bridge
@GitHub
```

Observed recurring behavior:

```text
ADS developer MCP works
GitHub may still appear in available tool definitions
GitHub invocation fails with:
FORBIDDEN: This conversation is restricted to developer MCPs
```

The problem was reproduced across roughly ten fresh conversations according to the project owner.

This is not merely a discovery-list issue because the GitHub connector can appear in available tool definitions while execution is rejected later.

## 4. External evidence

Current OpenAI Developer Mode documentation describes selecting one or more apps in a conversation and does not document a rule that activating one developer MCP must categorically disable all ordinary connectors.

Official reference:

```text
https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta
```

A separate OpenAI Developer Community report describes the same exact runtime error while combining a custom/developer MCP with ordinary connected apps:

```text
FORBIDDEN: This conversation is restricted to developer MCPs
```

Community reference:

```text
https://community.openai.com/t/openai-s-own-developer-mode-documentation-says-multiple-apps-can-be-combined-but-actual-custom-mcp-openai-apps-behavior-does-not-match/1383485
```

Evidence classification under Research 113:

```text
official documentation     A / OFFICIAL_DOCUMENTATION
ADS repeated reproduction  G / ADS_EXPERIMENT
community reproduction     F / COMMUNITY_OBSERVATION
```

## 5. Current classification

The evidence supports:

```text
likely ChatGPT host/runtime limitation or product bug
not currently localized to Codexless
no supported workaround established inside this project
```

The evidence does not yet support a stronger claim about the exact internal cause of the `restricted to developer MCPs` state.

Until upstream behavior changes, ADS should not design a critical workflow that requires the native GitHub connector and the Codexless developer MCP to be executable in the same ChatGPT conversation.

## 6. Architectural response

Research 116 deliberately reduces reliance on same-conversation native GitHub access by making Codexless capable of operating on multiple authorized local Git clones.

Desired workflow:

```text
ChatGPT + Codexless
    -> local authorized clones
    -> bounded semantic Git synchronization
    -> GitHub remote
```

The native GitHub connector remains useful for remote-only metadata/review tasks when available, but it should not be a required dependency for ordinary ADS local development continuity.

## 7. Conversation rotation consequence

A new persistent `chatgpt-17` conversation is desirable once the next flexible multi-repository action surface is finalized and refreshed.

Opening it immediately after the 50-tool publication would be inefficient because another schema-level change is expected during Research 116. The current plan is to rotate once after that stable surface is qualified, then avoid future rotations for ordinary workspace/branch additions by using mutable server-owned authority state behind stable tools.
