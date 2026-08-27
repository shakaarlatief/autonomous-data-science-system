# Model Collaboration Review Inbox

**Date:** 2026-08-27  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs and resolution records remain authoritative.  
**Repository:** `shakaarlatief/autonomous-data-science-system`  
**Coordination branch:** `v1-cockpit-design-exploration`

## Routing discipline

The repository and coordination branch above must also be named explicitly in the human-to-Claude trigger prompt.

```text
coordination branch
    where Claude reads current routing, this inbox, thread state and request files

exact target ref / SHA
    immutable evidence or artifact a specific request may direct Claude to inspect
```

Claude should not infer or switch the coordination branch from default-branch contents, newest commits, missing files or unrelated branch discovery. If the trigger names a different branch than this authoritative current routing state, Claude should stop and report the mismatch rather than choose a branch heuristically.

## Pending model obligation

```text
MC-0004 Message 008
Claude blind Conversation Workspace + chat visual-design response
```

Request:

```text
docs/model_collaboration/threads/MC-0004/messages/007_chatgpt_conversation_workspace_blind_design_request.md
```

Frozen blind request base:

```text
c190420c6d77d3191ca9efb9ffc1e401bbb7fda8
```

## Next actor

```text
Claude
```

Current checkpoint remains:

```text
245
```

## Independence rule

Claude must design independently from the product requirements in Message 007.

Claude must not inspect:

```text
frontend/design-lab/conversation-workspace-architecture.*
docs/research/079_conversation_workspace_presentation_architecture_experiment.md
later ChatGPT Conversation Workspace redesign artifacts
unrelated branches
```

ChatGPT is independently redesigning the same problem on:

```text
chatgpt-conversation-workspace-independent-design
```

Claude must not inspect that branch. The two outputs are compared only after both independent designs exist.

## Scope of Claude response

The request is deliberately broader than split/dock/fullscreen architecture. Claude should independently design the entire Conversation Workspace visual and interaction system, including:

```text
workspace composition
chat visual identity
colors / surfaces
typography
user and ADS message geometry
project-object references
structured project-change moments
tool / provenance summaries
composer
navigation / search
conversation lifecycle ideas
motion / micro-interactions
density
accessibility
browser-test plan
```

Production `/cockpit` remains untouched. S0 Geometric Control remains the provisional zoom working default; semantic zoom remains deferred.
