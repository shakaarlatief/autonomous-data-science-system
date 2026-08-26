# MC-0004 Neutral Brief: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Purpose:** Neutral problem statement for an independent first-pass Cockpit visual/product design exploration  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Important:** Phase A must be completed from this brief plus the accepted pre-proposal repository state. The reviewer must **not** read Research 037, later Cockpit exploration proposals, comparative syntheses, or other proposer-specific candidate material until the independent proposal has been durably recorded.

## Problem

The Autonomous Data Science System already has a promoted V1 Project Cockpit interaction architecture. The project owner now wants to deliberately reopen **visual and interaction design exploration** without assuming the current appearance is close to final.

This is not a request for incremental CSS polish only. The design may be substantially reconsidered where the accepted interaction architecture does not constrain it. Existing elements may be redesigned, replaced, simplified, removed, or reorganized if a better professional product results.

The target is a Project Cockpit that feels substantially more advanced, coherent, visually refined, alive, information-bearing, and distinctive while remaining a serious analytical work environment rather than a decorative concept demo.

## Accepted baseline that should not be casually discarded

The governing interaction baseline is Specification 008. Among other things, it has already earned evidence for:

```text
Project Cockpit as the primary immersive active-work environment
living project-process projection
meaningful user-facing work units rather than every persisted object
spatial navigation and focus into real reusable specialist workspaces
finite navigable grid world distinct from the semantic project plane
2D navigation, zoom, fit/reset, Jump/search and recovery
compact/fold-away chrome
collision-safe floating surfaces
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
reachability != simultaneous mounting
```

These are current accepted interaction requirements, not proof that the present visual implementation is optimal. Specification 008 explicitly leaves the final Cockpit visual identity, graph/canvas technology, semantic zoom/grouping, minimap, auto-layout, stage taxonomy, ruler treatment, tool-rail design, and several other choices unfrozen.

## Product owner design intent

The owner wants broad exploration before implementation. Areas explicitly invited for reconsideration include, without requiring any particular solution:

```text
grid/world appearance
small visual details and microinteractions
more meaningful connector/relationship treatment
dynamic versus settled visual states
movement or light along lines where it has real meaning
transitions between project work and focused workspaces
richer depth or possible 2.5D/3D treatments
how unfinished, active, blocked, completed and deferred work differ
how the product can feel more dynamic without becoming distracting
major redesigns if they are stronger than the current composition
```

The owner wants inspiration from high-quality existing products and interaction systems, but ADS must not become a copy of any one reference.

## Important conversation requirement

A minimal native composer at the bottom of the Cockpit is not enough by itself.

ADS is a data-science working environment in which the user must be able to hold long, substantive conversations with the system, revisit prior messages, continue earlier discussions, and reason collaboratively over a project just as they would in a serious LLM-assisted data-science workflow.

Therefore the design exploration must address both:

```text
lightweight in-context interaction
    composer / concise response / immediate steering

and

full conversation depth
    durable visible transcript
    prior messages
    continued multi-turn discussion
    practical navigation/search/re-entry into conversation history
```

The expanded conversation experience should feel integrated with the Cockpit rather than forcing a permanently dominant generic chat sidebar. It may use docking, focus transitions, split views, overlays, a dedicated conversation workspace, or another stronger design. The reviewer should propose the best architecture rather than assume one of these.

The conversation surface must coexist with the project-state principle that consequential outcomes should become structured project state rather than remaining authoritative only inside prose history.

## Existing implementation context

The current frontend is a React/TypeScript/Vite evaluation track using ordinary DOM/CSS/SVG/browser geometry for the Cockpit. It already demonstrates the promoted interaction model but is not final production architecture.

The current implementation should be treated as evidence and a baseline to critique, not as a visual template that must be preserved.

Do not assume a dedicated graph/canvas library is required. Do not assume it is unnecessary either. Technology should follow concrete product requirements and measured trade-offs.

## Phase-A reading boundary

Use the accepted repository state rooted at the pre-proposal integration boundary plus this neutral brief.

Recommended governing read set:

```text
README.md
frontend/README.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md
frontend/src/components/CockpitProjectMap.tsx
frontend/src/cockpit.css
```

Phase A must **exclude**:

```text
docs/research/037_*
any later MC-0004 proposer message containing ChatGPT's candidate design
any later comparative synthesis or recommendation
candidate implementation created after this brief
```

If candidate content is encountered accidentally, disclose the exposure and classify the independence limitation rather than pretending the review remained blind.

## Questions the independent proposal should answer

Develop your strongest independent design direction for the next-generation Cockpit. Address at least:

1. What should the Cockpit feel like visually and behaviorally at rest and while work is active?
2. How should the spatial world/grid be designed?
3. What visual grammar should distinguish different meaningful work units without creating a chaotic shape zoo?
4. What should connectors mean, and when should they be animated or static?
5. How should semantic zoom or other level-of-detail behavior work?
6. How should stages/orientation work as projects become large and nonlinear?
7. How should selection and focus transitions into full analytical workspaces behave?
8. How should running work, blockers, unresolved questions, approvals, completion, deferral and historical state be visualized?
9. How should navigation, search, commands and controls scale without clutter?
10. How should the minimal composer expand into a serious long-form Conversation Workspace with searchable/revisitable history while retaining Cockpit/project context?
11. Should conversation be one persistent thread, multiple threads, contextual sub-conversations, or some other product model? Distinguish product UX from unproven persistence implementation details.
12. How should chat messages link to project work, evidence, decisions and state changes?
13. What role, if any, should 2.5D or 3D depth play?
14. What motion language should ADS use, including reduced-motion behavior?
15. How should information density be controlled for novice scanning versus expert inspection?
16. What rendering/interaction technology would you investigate, and what evidence would justify replacing the current DOM/CSS/SVG implementation?
17. What are the largest scalability, accessibility, performance and maintainability risks in your design?
18. What concrete mockups/prototypes and evaluation scenarios should be built before implementation architecture is frozen?

## Desired Phase-A output

Produce an independent design exploration rather than a single unqualified answer. Include:

```text
core design principles
at least two materially different candidate directions
preferred direction and why
conversation/transcript architecture
motion and connector semantics
semantic-zoom / information-density strategy
large-project scalability strategy
technology hypotheses with trade-offs
what you would explicitly avoid
prototype/evaluation plan
strongest failure mode in your preferred design
strongest alternative considered
what evidence would make you change your recommendation
remaining provisional decisions
```

Do not optimize for agreement with ChatGPT. Do not optimize for disagreement either. The goal is the strongest independent design judgment from the accepted ADS requirements and the owner's stated product intent.
