# MC-0004 Message 001: Claude Independent Cockpit Design Proposal (Phase A)

**Thread:** MC-0004
**Message:** 001
**Author / collaborator:** Claude
**Role:** INDEPENDENT_REVIEWER / COUNTER_DESIGNER — Phase A
**Interaction environment:** Claude (claude.ai, chat interface with GitHub MCP connector)
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `claude-01`
**Conversation title:** `01 - ADS Development Review & Collaboration`
**Model / configuration:** Claude Sonnet 5
**Exact review base:** `bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88`, per `MC-0004/BRIEF.md` and `MC-0004/THREAD.md`
**Independence status:** `BLIND_TO_CANDIDATE`. I did not read Research 037, any later ChatGPT MC-0004 message, or any comparative synthesis. Every file cited below was fetched at the exact review-base SHA, not the branch head, including `THREAD.md`/`STATE.json` which I fetched at branch head only for procedural fields (task owner, write scope, phase) — I checked their content first and confirmed neither contains design material before relying on them.
**Read set:** `README.md`, `frontend/README.md`, Foundation 021, Specification 008, Research 002, Research 003, Research 009, Research 012, `frontend/src/components/CockpitProjectMap.tsx`, `frontend/src/cockpit.css` — all at the review-base SHA.
**Purpose:** Independent Phase-A design exploration for the next-generation Project Cockpit, per `MC-0004/BRIEF.md`.

---

## 0. What the current implementation actually tells me

Before proposing anything, I want to be concrete about what I found reading the real code, not just the research prose, because the code disagrees with the research in one important way.

Research 002 §11 explicitly warned against the existing frontend's "recognizable design grammar" (Inter-style sans, white panels, slate text, blue/indigo accent, rounded cards, soft borders, subtle shadows, small uppercase eyebrow labels) becoming an unexamined default, and said the Cockpit "deserves a deliberate visual exploration from first principles." Foundation 021 §2 independently warns against "oversized cards, excessive whitespace, decorative gradients, and low information density that make analytical software feel like a marketing page."

Reading `cockpit.css` directly, the current implementation is exactly the pattern both documents warned against: 9–15px card radii, `color-mix`-muted borders, soft `rgba(15,23,42,...)` shadows, `backdrop-filter: blur()` glassmorphism, 8.5–13px font sizes throughout, status conveyed via `color-mix` badge tinting. It is competent, restrained, professional — and it is the generic modern SaaS-dashboard language the project's own foundational documents said not to default to. That gap, between what was warned against and what was actually built, is the clearest and most evidence-backed starting point for this exploration, so I'm treating it as the primary thing to fix rather than a secondary polish note.

Three more things the code shows that the research prose doesn't fully anticipate:

- **The ten work-unit nodes are visually identical.** Every node (`.cockpit-node`) uses the same card shape regardless of whether it represents a completed objective, a blocking question, an investigation, or a modeling run. Foundation 021 §6 explicitly asks for first-class visual representations per object type, "not all... generic cards with different headings." The current implementation is exactly that generic-card pattern.
- **Connectors are hand-drawn SVG paths with no semantic data behind them.** `CONNECTOR_PATHS` is a hardcoded array of ten path strings; one gets a `deferred` dashed style purely by array index, not by any actual relationship property. There's no arrowhead, no directionality, no distinction between "data flows into this" and "this blocks that." Whatever connectors are supposed to mean today, the code doesn't encode it.
- **There's no semantic zoom.** Zoom is a literal CSS `zoom` property scaling the same fixed-detail cards uniformly. Nothing collapses, clusters, or simplifies at lower zoom levels.
- **Node positions are hardcoded pixel coordinates** (`.node-objective { left: 60px; top: 155px; }`, etc.), which is fine for a ten-node fixture but has no path to scaling, and sits in tension with Research 002 §5's own explicit statement that projects branch, loop, and reopen non-linearly.

I'm citing these because I think a design proposal grounded in what the code actually does is stronger than one grounded only in the research memos' aspirations.

---

## 1. What the Cockpit should feel like

**At rest:** calm, spatial, unmistakably a serious analytical tool rather than a landing page — closer to a precision instrument panel than a dashboard. Static areas should recede visually; nothing should move without a reason.

**While work is active:** legible tension, not clutter. The single biggest gap in the current implementation is that "active" and "static" look almost the same — a status-colored icon is the only signal. I want active work to be physically distinguishable at a glance, through restrained, purposeful motion (Section 14), not just color.

The core principle I'd state for this exploration: **motion and visual weight should track where the project's actual attention currently is, not decorate the whole canvas uniformly.** This is my answer to the brief's "dynamic without being distracting" requirement — the mechanism for avoiding distraction is scarcity, not subtlety alone.

---

## 2. Two materially different candidate directions

### Direction 1 — Living Process Canvas (preferred)

Keep the promoted spatial map/pan/zoom/focus-transition model from Specification 008 — it has seven rounds of real human-review evidence behind it, and I don't think that evidence should be discarded without a specific reason to. Push its visual and semantic execution much further than the current baseline:

- Replace hardcoded pixel node positions with an auto-layout algorithm operating within stage lanes (force-directed or constraint-based, still bounded by the accepted stage taxonomy where one exists).
- Give each object *category* (not each individual node) a distinct silhouette family — Questions/Blockers share one visual family, Findings/Evidence another, Decisions their own, Runs/Investigations their own — so the map communicates type at a glance without becoming, in the brief's words, a "chaotic shape zoo."
- Make connectors data-driven and meaningful (Section 4).
- Introduce restrained depth: stage zones sit on a very slightly receded backdrop plane; selected/active nodes lift with a real sense of elevation rather than a soft box-shadow alone.
- Introduce semantic zoom (Section 5).

### Direction 2 — Analytical Command Deck

A more control-room-inspired alternative, closer to Research 002's Direction B. Instead of literal spatial position on an ever-wider canvas, work items live in a small number of adaptive lanes — Now / Next / Blocked / History — that reflow based on actual project state. This trades some of the spatial-memory benefit of a living map for stronger information density and faster orientation as projects grow large and nonlinear (the brief's Q6), since growth doesn't require an ever-wider canvas or reliance on semantic zoom to stay legible.

### Preferred direction and why

**Direction 1.** It's the smaller, better-evidenced delta from something already validated through seven real-browser human review cycles, and it directly targets the two clearest gaps I found in the actual code (generic visual grammar, no connector semantics) without discarding a spatial-navigation model users have already responded well to. Direction 2 is not weaker on its merits — see Section 12 — but adopting it would mean re-earning the orientation/legibility evidence Specification 008 already has for the current spatial model, and I don't think the brief's evidence justifies that reset yet.

---

## 3. Spatial world/grid design

Preserve the `FiniteNavigableGridWorld` / `SemanticProjectPlane` distinction from Specification 008 §6 — it's sound and already validated. Within Direction 1, I'd change:

- Auto-layout within lanes rather than hand-placed coordinates (Section 2), so the grid can actually accommodate branching and reopened work without manual redesign each time the fixture changes.
- The stage-zone backdrop should carry more visual identity than the current faint dashed-border rectangles — enough that a glance at low zoom communicates "five stages" without reading labels, while remaining subordinate to the work units themselves.

---

## 4. Visual grammar and connector semantics

**Work-unit grammar:** category-level silhouette families as described in Section 2, layered with the existing status-color system (blocked/attention/ready/complete/deferred), which already works reasonably well and doesn't need replacing — only supplementing.

**Connectors** should encode three independent things, none of which the current implementation encodes at all:

1. **Relationship type** — data/evidence flow, blocking dependency, or supporting-evidence link — via distinct line treatments (weight, dash pattern), not just color.
2. **Directionality** — actual arrowheads or a flow-direction cue. The current SVG paths have none.
3. **Liveness** — animation reserved *only* for connectors leading to or from whatever is currently receiving attention (an active run, a just-produced Finding), not applied uniformly. This is the direct mechanism for "movement where it has real meaning" without becoming visual noise, and it should be capped — see Section 13.

---

## 5. Semantic zoom / level-of-detail

Currently absent entirely. I'd propose: past a zoom threshold, individual work-unit cards progressively collapse into simpler glyphs grouped by stage — status color and count surviving, detail text and icons dropping — similar to marker clustering in mapping applications. This directly serves both the "alive without chaotic" requirement and large-project scalability (Section 6), since it's the mechanism that keeps a 50-node project legible at low zoom without redesigning the layout algorithm separately.

---

## 6. Stages and orientation at scale

The current implementation's fixed five-column, hardcoded-pixel-width stage strip cannot survive real growth — it's explicitly a ten-node fixture. Within Direction 1, stage zones should size themselves to their actual content rather than fixed pixel widths, and semantic zoom (Section 5) should be the primary mechanism for staying legible as work-unit count grows, rather than requiring the canvas to grow proportionally to project size. I'd treat this as the strongest single piece of evidence in favor of Direction 2 if Direction 1's semantic zoom doesn't hold up under real large-project testing — see Section 12.

---

## 7. Selection and focus transitions

Keep the validated pattern from Research 003 exactly as designed: spatial handoff into a full-resolution `CockpitFocusHost`-mounted workspace, not literal CSS-transform magnification of the node itself. This is good architecture already, confirmed by reading `CockpitProjectMap.tsx` — focus transitions are handled at the routing/component level, not by scaling DOM nodes. Nothing here needs to change; I'd only extend the same mechanism to host the Conversation Workspace (Section 10).

---

## 8. Visualizing running work, blockers, and history

The current status vocabulary (blocked/attention/ready/selected/deferred/future/complete) is a reasonable foundation and shouldn't be discarded. What's missing is a *live* state — something actively running right now — which the current type system doesn't distinguish from "ready." I'd add a distinct `active` status with its own restrained motion treatment (Section 14), separate from the static "ready" state it currently gets collapsed into.

---

## 9. Navigation, search, and controls at scale

The existing Jump/search pattern (quick semantic destinations + searchable results, collision-aware against the composer) is genuinely good — Research 009 and Research 012's human-review evidence both confirm it working well after iteration, and I don't see a reason to redesign it. I'd only extend its result list to reflect semantic-zoom clusters once those exist, so searching a large project surfaces clusters as well as individual work units.

---

## 10. From minimal composer to full Conversation Workspace

This is the area the brief weights most heavily, so I want to be concrete about the architecture, not just gesture at requirements.

**Proposed model:** the composer stays exactly where it is today — bottom-floating, collision-safe, good as-is — for lightweight in-context steering. Sending a message, or explicitly choosing to expand, transitions into a **Conversation Workspace** using the *same* spatial-focus-transition mechanism already validated for Data/EDA/Missingness (Section 7) — reusing Research 003 §4's dual-access pattern rather than inventing a new interaction style. Conversation becomes just another focusable specialist workspace, not a bolted-on sidebar or a separate product surface.

Inside the Conversation Workspace: a full scrollable, searchable transcript. Critically, per Foundation 021 §7's explicit requirement, messages that produced consequential project changes — a new Finding, a Decision, a state change — should render inline as linked project-object cards within the transcript, not as plain prose, so the conversation reads as a legible history of actual project evolution rather than a disconnected log sitting next to the "real" project state.

**Threading (Q11):** one primary project-level thread by default, with explicit contextual sub-conversations only when a user deliberately branches a focused discussion from inside a specific work-unit's focus view. I'm proposing this as a product-UX preference, not asserting anything about the underlying persistence model — that's explicitly out of scope for what I can responsibly claim here.

**Linking (Q12):** every message that changes project state should carry a durable link to the object it changed, consistent with the transcript-as-history idea above, and the reverse should also hold — a Finding or Decision's detail view should be able to show which conversation produced it.

**Re-entry:** search within the transcript, plus reuse of Specification 008 §14's URL-addressable-focus pattern so a specific point in conversation history is deep-linkable the same way a data focus state already is.

---

## 11. 2.5D/3D depth

I'd recommend CSS-only layered depth — subtle `transform`/parallax, a receded backdrop plane for stage zones, real elevation on active/selected nodes — rather than a true 3D engine. This satisfies Foundation 021's "subtle depth and elevation where useful" without the accessibility, performance, and maintainability cost of a 3D rendering stack, which seems disproportionate for a desktop analytical tool that isn't trying to be an immersive showcase product.

---

## 12. Strongest alternative considered

Direction 2 (Analytical Command Deck) is a genuinely close call, not a token alternative. Lane-based reflow may scale better than any spatial-canvas approach once a project has many branching, non-linear work streams — exactly the scenario Research 002 §5 says the system must support. Direction 1's semantic zoom is my answer to that scaling problem, but it's untested; if it doesn't hold up in practice, Direction 2's reflow model doesn't have the same dependency on zoom-level clustering to stay legible. I'm recommending Direction 1 primarily because it's the smaller change from already-validated interaction architecture, not because I'm confident it's the better long-run answer to large-project scale.

---

## 13. Strongest failure mode in my preferred design

The connector-liveness mechanism (Section 4) is the riskiest part of this proposal. If "active" ends up loosely defined, or if a real project has several genuinely active things at once, animated connectors could stack up and produce exactly the visual noise the brief warns against — the opposite of the intended effect. Mitigation: cap simultaneous animated connectors (for example, only the one to three most currently relevant paths animate at any moment; everything else stays static but still color/dash-coded by type). This cap is a guess, not a validated number, and belongs in the prototype/evaluation plan below rather than being treated as settled.

---

## 14. Motion language

- **Idle/ambient:** near-static. No decorative looping motion on inactive nodes.
- **Active state:** a slow, subtle luminance or elevation signal on genuinely active nodes only — not a generic pulse applied everywhere.
- **Event-triggered:** a brief "traveling" highlight along a connector only when something has actually just happened (a Finding produced, a run completed) — event-driven, not ambient.
- **Focus transitions:** keep the existing spatial handoff exactly as validated.
- **Reduced motion:** extend the existing, already well-implemented `prefers-reduced-motion` discipline in `cockpit.css` to every new motion element — traveling-connector highlights should default to a static emphasized state, not disappear entirely, preserving Research 003 §17's rule that the final state must be identical whether or not animation runs.

---

## 15. Information density

Progressive disclosure via semantic zoom (Section 5) for the map itself; inside focus workspaces, keep the existing pattern of a compact hero/summary layer with expandable detail panels, which the current Missingness workspace already does reasonably well based on what I read in the CSS.

---

## 16. Technology hypotheses

I'm not recommending a wholesale technology change. The existing DOM/CSS/SVG approach has earned seven rounds of positive human review for the core interaction, and Specification 008 §18 is explicit that a specialized dependency should be introduced only when measured requirements justify it — I don't have that evidence yet, so I won't manufacture a recommendation to replace it.

What I would flag as worth *measuring*, not adopting outright: connector animation (Section 4) and semantic-zoom clustering (Section 5) at higher node counts than the current ten-node fixture could become a real SVG/DOM performance question. A bounded canvas or WebGL layer for just the connector-rendering surface is a reasonable hypothesis to prototype and measure against a realistic node count before deciding either way.

---

## 17. What I would explicitly avoid

```text
a full 3D/WebGL scene rebuild — disproportionate for a desktop analytical tool
ambient idle motion applied to every node uniformly
a permanent full-height chat sidebar — Specification 008 section 11 already
    rejected this, and the brief repeats the warning
discarding the validated pan/zoom/focus-transition architecture without
    new evidence that it's actually failing
a distinct visual shape per individual node rather than per object category
    (the "chaotic shape zoo" the brief warns against)
```

---

## 18. Prototype and evaluation plan

Mirror the project's own established Cockpit review methodology rather than inventing a new one:

1. Two to three static high-fidelity mockups of the same representative Churn project scenario used throughout the existing Cockpit research, showing Direction 1 and Direction 2 treatments side by side.
2. An isolated working prototype of just the connector-liveness and semantic-zoom mechanisms, since they're the highest-uncertainty, most novel pieces of this proposal — not the full Cockpit.
3. Extend the existing Playwright/accessibility gate pattern to cover the Conversation Workspace focus transition before any wider implementation, following the same cross-platform discipline already used for Specification 008.
4. A real-browser human review round, matching the format that already worked well for Research 009 and Research 012, rather than treating automated gates alone as sufficient — this project's own history shows the automated gate and human judgment have caught different problems.

---

## 19. Remaining provisional decisions

```text
exact shape-family taxonomy per object category — needs its own dedicated pass
exact simultaneous-animated-connector cap — needs prototyping, not guessable
    from first principles
whether Direction 1 or Direction 2 is ultimately preferred — this is exactly
    the kind of genuine product-intent/visual-dynamism-level choice MC-0004's
    own THREAD.md reserves for human arbitration, not something I should
    resolve unilaterally here
```

---

## 20. What evidence would change this recommendation

```text
if a future spike shows users losing spatial orientation once node count
    exceeds roughly 25-30 even with semantic zoom, I'd shift toward Direction
    2's lane-based reflow instead
if real human review finds the connector-liveness treatment distracting
    rather than orienting, I'd drop it in favor of static, type-coded
    connectors with no animation at all
if the existing DOM/SVG approach measurably struggles at realistic node
    counts, that would justify actually adopting a canvas/WebGL layer rather
    than just prototyping one
```
