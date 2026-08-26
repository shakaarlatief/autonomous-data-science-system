# MC-0004: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Status:** ACTIVE / PHASE B COMPARATIVE REVIEW  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Task owner:** ChatGPT  
**Target-state write owner:** ChatGPT  
**Independent reviewer / counter-designer:** Claude  
**Human project owner:** final arbiter of product-intent choices  
**Opened:** 2026-08-26

## Purpose

Run a deliberately broad next-generation Project Cockpit design exploration while preserving the promoted Specification 008 interaction architecture unless new evidence justifies revising it.

The task is research and design synthesis first. It does not authorize production frontend implementation or silently freeze a new visual identity.

## Independent Phase A

The neutral problem statement is:

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
```

The exact immutable neutral-brief commit for Phase A is:

```text
bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
```

Claude reasoned from that exact ref and the accepted pre-proposal repository material named by the brief. Phase A did not read Research 037 or later ChatGPT candidate-design material before Claude's independent proposal was durably recorded.

Claude's frozen Phase-A proposal is:

```text
docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
```

The preserved Phase-A classification is:

```text
BLIND_TO_CANDIDATE
known candidate exposures: none
```

The earlier manual catch-up attempt that landed on an older repository branch exposed only stale collaboration/routing state, not Research 037 or other candidate design content, so the independent design evidence remains valid.

## Comparative Phase B

The independent gate is now satisfied.

Claude may now read:

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
```

and compare it directly with its frozen Phase-A proposal.

The Phase-B comparative review should preserve under `messages/`:

```text
strongest convergence
material disagreements
ideas from Research 037 that improve Claude's original proposal
ideas from Claude Phase A that Research 037 underweights or misses
strongest alternative design direction after seeing both
which mechanisms deserve realistic mockups first
what should remain deliberately unresolved
what evidence would change the comparative recommendation
```

Phase B is intentionally comparative. It must not retrospectively describe Phase A as influenced by Research 037.

## Target-state scope

ChatGPT owns mutation of the bounded research/routing surfaces for this exploration:

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/checkpoints/206_source_vault_paused_cockpit_design_exploration_opened.md
docs/checkpoints/207_mc0004_phase_a_frozen_comparative_design_opened.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
README.md
this thread contract/state
```

Claude may write only the declared secondary collaboration surface:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

No frontend implementation file is part of the current target-state write scope.

## Collaboration phases

```text
PHASE A  COMPLETE
    ChatGPT external/product research proceeded independently
    Claude produced independent design proposal from neutral brief

PHASE B  ACTIVE
    both independent positions are frozen
    candidate exposure is allowed
    Claude performs direct comparative review
    ChatGPT then performs synthesis from both preserved positions

PHASE C
    human + collaborators choose which design directions deserve mockups/prototypes

PHASE D
    separate bounded implementation/prototype specification only after design evidence warrants it
```

## Independence rule

The preserved Phase-A independence classification applies only to the already-frozen message 001.

Phase B is `COMPARATIVE_ONLY` by design because Claude may now inspect Research 037 and later comparative material. Candidate exposure in Phase B is not contamination of the historical Phase-A result.

## Authority rule

```text
accepted repository specifications / decisions
    >
this collaboration thread
    >
raw model proposals
```

MC-0004 does not promote any visual concept merely because both models prefer it. Promotion still requires normal ADS evaluation and preservation.

## Human arbitration

The human project owner should decide genuine product-intent questions such as desired visual character, acceptable level of visual dynamism, and preference among otherwise technically defensible design directions.

Routine implementation details, source gathering, technical comparison and evidence synthesis should not be escalated merely because two models could make different stylistic choices.

## Closure condition

MC-0004 can close when:

```text
Claude independent design is preserved
ChatGPT research/design exploration is preserved
comparative synthesis is completed
material disagreement is explicit
human product direction is recorded where needed
next prototype/mockup boundary is clear
```

Closure does not require the final production Cockpit visual system to be frozen.
