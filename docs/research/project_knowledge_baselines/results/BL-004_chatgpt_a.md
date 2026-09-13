# BL-004 Result: Holistic Cockpit Integration Planning

## Result receipt

| Field | Value |
|---|---|
| Scenario ID | BL-004 |
| Environment / model | ChatGPT, GPT-5.6 Sol; repository access through Codexless Runtime Bridge |
| Frozen snapshot SHA | `2d425c76c385961cdd7f986c17ed83437a3d3806` |
| Snapshot access method | Exact snapshot-bounded local Git object/tree reads through Codexless read-only command execution, using `git ls-tree`, `git show`, and `git grep` against the frozen SHA. The BL-004 request itself was read from the exact user-specified request path before snapshot evidence access. |
| Result path | `docs/research/project_knowledge_baselines/results/BL-004_chatgpt_a.md` |
| Read/access failures | No substantive access failure. A broad `git ls-tree` output and one combined production-source `git show` were truncated by the tool response limit; critical evidence was then read through narrower snapshot-bounded calls. No descendant/current project content was used as substantive evidence. |
| Approximate tool/read effort | About 16 snapshot-bounded Git read commands, plus one workspace-authority lookup and one read of the BL-004 request. |

## Sources materially consulted

The governing and materially consulted snapshot evidence was: `docs/specifications/008_v1_project_cockpit_interaction_architecture.md`; `docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md`; `docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md`; `docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md`; Research 037, 043, 045, 050, 051, 058, 061, 063, 067, 070, 071, 073, 074, 077, 078, 085, and 086; targeted status/selection reads across Research 039, 040, 055, 056, 072, 079, 081, 082, 083, and 084; Checkpoint 248; the frozen `frontend/design-lab` tree; and the production Cockpit implementation in `frontend/src/components/CockpitProjectMap.tsx`, `frontend/src/pages/CockpitPage.tsx`, `frontend/src/cockpit.css`, and `frontend/src/cockpit-review-6.css` as available in the frozen snapshot.

## Final answer

### 1. What I would treat as governing

I would use a strict authority stack rather than treating all Phase-C files as peers.

**First, Specification 008 is the interaction-architecture floor.** It is the promoted V1 Cockpit contract. The holistic integration must preserve the immersive Project Cockpit as the primary active-work environment; the distinction between the finite navigable world and semantic project plane; two-dimensional navigation and recovery; bounded geometric zoom and native pinch; viewport-aware stage orientation; scalable Jump/search; compact and fold-away chrome; collision-safe floating surfaces; true fullscreen with graceful fallback; URL-addressable deep-work state; keyboard accessibility; reduced-motion behavior; world-owned restrained ambient depth; and reuse of real specialist workspaces rather than mounting every deep workspace inside every node. Phase-C visual work may refine how these capabilities look, but it should not accidentally reopen or remove capabilities already promoted by Specification 008.

**Second, Foundation 021 governs product character and interface quality.** The Cockpit is a reasoning and control surface, not a decorative graph. It should remain compact, information-dense, premium, accessible, and analytically legible. Chat is integrated but not the sole durable representation of project state. This also means the first holistic integration should establish a real design system instead of extending the existing stack of review-number stylesheet overrides.

**Third, Foundations 023 and 024 govern the semantic versus presentation boundary.** Work-unit meaning, relation meaning, directionality, project state, runtime state, priority, evidence, and constraints are system-owned semantics. Approved visual appearance choices may vary only inside those semantic boundaries. Connector treatment and hover behavior are presentation choices, while whether a relation is directed and which endpoint is source or target are semantic invariants.

**Fourth, I would treat the latest explicit human-selected Phase-C decision for each visual or interaction channel as the current design decision.** Earlier variants remain historical evidence unless the later record explicitly keeps them open. The latest record wins where a later research memo or checkpoint corrects an earlier framing. A concrete example is conversation: Checkpoint 248 and Research 086 supersede the narrower Checkpoint 247 framing. They preserve its transition experiments only as possible full-focus motion evidence, while making conversation orthogonal to the underlying work context.

**Fifth, the isolated design-lab implementations are fidelity oracles for accepted mechanisms, not independent product architecture.** Where a research record names an exact accepted browser target or file, I would port geometry, timing, layer ordering, proportions, and interaction behavior from that implementation rather than recreating the effect from memory or prose. I would not inherit prototype-only persistence, fixture ontologies, or experiment controls merely because they exist in the same page.

**Finally, the existing production Cockpit is the integration substrate, not the visual authority.** It already contains valuable promoted mechanics such as pan/zoom, pinch coalescing, stage-ruler geometry synchronization, Jump safe-area behavior, fullscreen, keyboard navigation, focus routing, and specialist-workspace reuse. Those should be refactored and preserved. Its current fixed node geometry, manually authored connector paths, single-axis `NodeStatus`, and layered review CSS should not be mistaken for the target Phase-C design system.

### 2. Current Phase-C decisions that should survive integration

| Channel | Current held or selected direction | Important boundary |
|---|---|---|
| World/grid | G4 Adaptive Hybrid, dark-first baseline. Currents may traverse the 20 px lattice; rare glints belong only to 100 px major-grid intersections and retain quiet independent cadence even when currents are Lively. | Light-mode redesign is deferred. Do not make glints accelerate with current intensity. |
| Work-unit lighting | H4 Integrated Response with immediate crisp hover entry, pointer hotspot, fuller node-colored hover halo, grid/world illumination, connector emphasis, one restrained perimeter sweep, slight depth lift, and slower release. Use Reduced in-box resting illumination as the held baseline while preserving H4 outward/world response. | Broad circular resting halo was rejected. Motion cannot carry semantics alone. |
| Category grammar | Stable scientific-marker mapping: Question/Blocker circle; Investigation square; Validation/Analysis triangle; Model Work diamond; Evaluation plus. | Category semantics are not an appearance preference. |
| Appearance configuration | Approved dimensions can compose, currently including normal versus subtle box shapes and none versus micro-material versus micro-light treatments, with curated presets. | Prototype `localStorage` is not a production persistence decision. Accessibility and semantic safety override preference. |
| Connector composition | Relation semantics are separate from treatment and hover. One terminal treatment at a time. Direction arrows exactly follow semantic direction. | Do not stack arrow + dot + socket without a new semantic reason. |
| Relation class | E5 Hue + Tag is the selected carrier. Direction arrows remain separate. Stroke rhythm is deliberately reserved for a future semantic dimension. | Final relation taxonomy and exact production hues remain open. |
| Project disposition | P7 Neutral Tag + Tone. Category color dominates at rest; disposition tag remains neutral at rest and reveals disposition color on hover; selective tonal recession may distinguish completed/deferred/future work. | Do not reintroduce a second persistent disposition color system around every node. Final ontology remains open. |
| Current-process lens | Current-focus membership is a separate axis from work-unit existence and project disposition. Users may add/remove nodes from the focus set. Context is strongly suppressed in focus mode but made operable while editing the set. | Prototype persistence and automatic membership logic remain open. |
| Operational status | Exactly one carrier at a time for live operational state: Dot + dynamic ring or animated soft-shade status tag. Global switching changes all live boxes and clears local overrides; local switching may change one box. No current runtime means no runtime carrier. | Carrier preference does not change runtime semantics. Reduced motion keeps static state identity. |
| Blocked versus failed | BLOCKED shares the operational-status presentation slot without becoming a runtime-state synonym. BLOCKED compact form uses the sharper non-circular red constraint ring; FAIL uses the smoother circular red ring. Tag mode says `BLOCKED` or `FAIL` explicitly. A blocker cause and `BLOCKS` relation remain separately represented. | Shared visual slot does not merge ontology. |
| Attention priority | A3 Signal Bars, three ascending micro-bars near the upper-right frame, spatially separated from disposition and operational status. | No final binary/ordinal/scored priority model is frozen. |
| Persistent selection | SEL2, four compact neutral-cool corner brackets outside the rendered frame, persistent after pointer exit. | Selection is distinct from hover and from keyboard `:focus-visible`. |
| Contextual expansion | X5 balanced two-axis expansion, 390 x 210 px in the accepted experiment, one integrated object, surrounding map remains at normal salience, no X5-specific context recession. | Internal semantic payload is not frozen. L0 Flat Fields is only the provisional working default. |
| Deep focus | Z7 Pull-Back Then Dive from the actual rendered source position into a fullscreen specialist workspace. At the deepest state the project grid and surrounding boxes disappear; a compact topology compass remains. | Exact timing/easing, return choreography, compass semantics, mounting mechanics and URL details remain open. Reduced motion reaches the same end state essentially instantly. |
| Zoom information | S0 geometric-control working default. Keep information behavior stable across zoom for now. | Semantic zoom is deferred, not rejected. Do not add it to the first holistic integration. |
| Conversation visual baseline | Quiet Graphite; Boxes/Text user-switchable thread rail; canonical Cockpit work-unit rendering in Boxes mode; A6 work-unit context expansion; no redundant floating A6 work-unit card. | Conversation persistence schema and final A6 internal content remain open. |
| Conversation architecture | Conversation is orthogonal to work depth. It must be reachable from Grid neutral, selected, and X5 states, and from Deep Dive. It may take full focus or coexist with work. Opening/closing conversation must preserve underlying work context. Invocation origin and conversation scope are separate. | No final right-dock/split/context-rail winner is selected at this snapshot. P3 in the latest browser is only the initial default. |

### 3. The most important integration refactor

Before carrying visual CSS into production, I would separate the semantic axes that the current production map compresses together.

The frozen `CockpitProjectMap.tsx` currently uses one `NodeStatus` union containing values such as `complete`, `blocked`, `attention`, `ready`, `selected`, `deferred`, and `future`. Phase-C evidence demonstrates that these are not one mutually exclusive dimension. A single work unit may simultaneously be:

```text
category             Investigation
project disposition  Current
operational status   BLOCKED
attention priority   elevated
selection            selected
focus membership     in current process
appearance profile   subtle shape + micro material
conversation scope   has a work-unit-scoped thread
```

If the integration keeps a single status field, the accepted visual grammar will fight itself and semantic combinations will become impossible or misleading. The first architectural step should therefore be a factorized presentation model with independent fields for category, disposition, operational status/progress constraint, attention, selection, focus membership, relation semantics, and presentation preference. The exact final backend ontology can remain open; the frontend composition model only needs to stop conflating channels that Phase C has already proven independent.

### 4. How I would construct the holistic integration

I would build one shared production visual system around semantic primitives rather than copy each design-lab page into `/cockpit`.

The central primitive should be a single canonical work-unit renderer with explicit visual slots: category marker, category-owned accent, disposition tag/tone, operational-status carrier, attention signal, external selection brackets, configurable shape/micro-surface layer, hover/world-lighting layer, and content region. That same renderer should be reused in the Project Grid and in Conversation Workspace Boxes mode, matching the Phase-C decision that conversation should not invent a second mini-card grammar.

Relations should likewise use a single relation renderer driven by an explicit semantic relation object. The renderer can choose a validated presentation treatment, but direction, source/target identity, relation class, and cause/effect semantics must come from the relation model. Hue + Tag should carry relation class; arrow endpoints should carry direction; stroke rhythm should remain unused until a separate semantic dimension earns it.

The world layer should be independent from the work-unit layer. G4 grid/current/glint effects belong to the navigable world so they do not expose the semantic project plane as an accidental rectangle. Work-unit rest/hover spill may illuminate that world locally, but the ambient world should remain restrained and should not become a runtime-state visualization.

The integration should preserve the promoted map mechanics already present in production. I would keep the existing proven pan, zoom, pinch, fit/reset, Jump/search safe area, stage-ruler synchronization, fullscreen, keyboard and reduced-motion behavior while replacing the current generic node/status styling with the factorized Phase-C grammar. This is safer than rebuilding navigation and visual design simultaneously.

### 5. Integration sequence

I would integrate in this order so each layer can be validated before the next one can obscure it:

```text
1. Preserve Specification 008 mechanics and establish shared design tokens.
2. Integrate G4 world substrate and dark-first baseline.
3. Replace generic production cards with the canonical Phase-C work-unit primitive.
4. Add scientific category markers, Reduced rest light, H4 hover/world response, and appearance-profile composition.
5. Replace manual semantic styling of relations with the shared relation renderer, then add directionality and E5 Hue + Tag.
6. Add project disposition P7.
7. Add conditional operational status, BLOCKED/FAIL mapping, and explicit blocker relationships.
8. Add A3 attention priority.
9. Add SEL2 persistent selection.
10. Add the editable current-process focus lens.
11. Add X5 contextual expansion with L0 as the provisional internal-layout control.
12. Connect X5 to the existing real specialist workspaces through Z7, preserving full-stage deep focus and the compact topology compass.
13. Add the full Conversation Workspace using Quiet Graphite, Boxes/Text, canonical work-unit reuse, and A6 context expansion.
14. Make conversation orthogonal to Grid/Deep Dive and prove full-focus plus co-present modes without selecting an unfrozen final split geometry prematurely.
15. Only after semantic composition is stable, do integrated spacing, collision, performance, and motion polish.
```

This ordering keeps the difficult semantic overlays visible as independent problems. It also prevents the conversation layer from forcing a premature redesign of the map or specialist-workspace state model.

### 6. Fidelity strategy

For accepted mechanisms, I would transfer measured values and behavior from the frozen design-lab implementation rather than recreate them by eye. Examples include the G4 lattice relationships, H4 entry/release behavior, relation-tag proportions, X5 accepted geometry, SEL2 bracket placement, BLOCKED/FAIL ring geometry, runtime perimeter-trace motion, and Z7 source-relative origin handling.

I would create an integrated Phase-C reference fixture containing representative combinations that deliberately stress channel coexistence. The fixture should include at least a Question/Blocker, Investigation, Validation, Model Work, and Evaluation node; multiple dispositions; no-runtime and live-runtime cases; BLOCKED and FAIL; elevated attention; selection; focus/non-focus membership; multiple relation classes and directions; X5 expansion; and a work-unit-scoped conversation. The objective is not to demonstrate every backend state. It is to prove that the accepted visual channels remain legible when combined.

Visual-regression snapshots should be added only after comparing the integrated renderer against the isolated accepted design-lab references and receiving human review. The first integrated screenshot should not silently become the new canonical truth merely because it is the first one produced.

Static screenshots are insufficient for the most important Phase-C interaction evidence. Manual/browser review or deterministic interaction capture is needed for H4 entry and release, ambient cadence, runtime ring/tag motion, X5 expansion, Z7, and conversation open/close/state restoration. Reduced-motion variants should be tested separately to ensure the same semantics survive without motion.

Representative viewport validation should preserve Specification 008's desktop/laptop boundary, including 1440, 1280, 1024 widths and the 1024 x 768 height case. Collision testing should explicitly include the composer, Jump/search, context surfaces, X5 expansion, and co-present Conversation Workspace.

### 7. State ownership during integration

I would keep three state layers distinct.

```text
semantic project state
    work-unit and relation meaning
    disposition
    runtime/progress constraint
    priority
    evidence/provenance

presentation profile
    approved box shape
    micro design
    operational carrier preference where retained
    connector presentation preference where retained
    future safe appearance choices

session/navigation state
    pan/zoom
    selected node
    X5 open state
    current work surface
    conversation presentation mode
    temporary rail/pane state
```

The exact production persistence destination for the second and third layers is intentionally not decided by this plan, because Phase-C explicitly left those contracts open. The component/state architecture should make later persistence choices possible without pretending that prototype `localStorage` or current query parameters are already the product contract.

### 8. What I would explicitly avoid

I would not keep extending `cockpit-review-N.css` as the production architecture. The historical cascade is valuable evidence, but the holistic integration is the point at which accepted tokens, layers, and component states should be consolidated.

I would not copy every positive design-lab mechanism into one visually stacked card. Phase C repeatedly selected orthogonality and one-carrier-at-a-time rules because visual channels compete. Configurability should compose only approved dimensions that remain semantically safe.

I would not treat design-lab fixture names as a final backend ontology. Several research records explicitly say the category, disposition, runtime, relation, priority, and persistence models remain open.

I would not promote semantic zoom now. S0 is the working behavior and semantic zoom is deliberately deferred.

I would not turn the Conversation Workspace into a destructive replacement route. The latest checkpoint requires conversation to preserve Grid/X5/Deep Dive state and to support both full focus and co-presence.

I would not introduce React Flow, Pixi, a gesture framework, or another rendering dependency merely because Phase-C research considered them. Specification 008 leaves technology open and requires a specialized dependency to earn its complexity through measured scale, layout, accessibility, interaction, or maintainability need.

### 9. Definition of a faithful first holistic integration

I would consider the integration faithful when one coherent Cockpit can render realistic mixed states without semantic collisions; appearance changes never alter project meaning; the world still pans, zooms, pinches, orients, jumps, recovers, and respects accessibility exactly as the promoted interaction architecture requires; accepted Phase-C visual mechanisms match their isolated reference behavior closely enough to survive side-by-side human review; selection can become X5 and then Z7 deep focus without losing context; conversation can be opened from every required work depth and closed without resetting that work state; and all still-open Phase-C questions remain visibly open rather than being accidentally frozen by implementation convenience.

The first implementation milestone should therefore be an **integration proof**, not a final visual promotion. After it passes deterministic behavior/accessibility checks and side-by-side fidelity review against the accepted design-lab evidence, a human integrated-browser review should decide what new adjustments are genuinely caused by composition. Only those integrated findings should be allowed to revise the accepted isolated decisions.

## Uncertainty / areas not checked

I did not read every Phase-C research file or every design-lab source file line-by-line. I concentrated on the promoted interaction specification, durable design foundations, the latest explicit human-selected records for each major channel, the current Checkpoint 248 boundary, the frozen design-lab inventory, and the existing production Cockpit integration substrate. Where an isolated research memo named an exact accepted browser target, I treated that target as the fidelity oracle even when I did not exhaustively inspect every CSS/JS declaration in that artifact.

The latest conversation co-presence composition is intentionally unresolved at this snapshot. Likewise, light-mode redesign, semantic zoom, final internal X5 information architecture, final runtime/priority/disposition ontologies, preference persistence, exact Z7 timing/return behavior, final compass semantics, URL/session contracts, and production graph/canvas technology remain open. The integration should preserve those uncertainties rather than resolving them implicitly.
