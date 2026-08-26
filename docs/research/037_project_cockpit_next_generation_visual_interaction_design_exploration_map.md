# Research 037: Project Cockpit Next-Generation Visual and Interaction Design Exploration Map

**Date:** 2026-08-26  
**Status:** Active product-design research and hypothesis map, not an accepted visual specification  
**Scope:** Broad next-generation Project Cockpit visual, spatial, motion, conversation, information-density, scalability, and rendering exploration before mockup selection or implementation  
**Authority:** Research only. Specification 008 remains the accepted V1 interaction architecture unless later evidence and normal promotion governance revise it.  
**Primary interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-06  
**Companion collaboration thread:** MC-0004  
**Independent Claude Phase-A base:** `bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88`

---

## 1. Purpose

The Project Cockpit has already passed an important architectural threshold. Specification 008 established that ADS can use one immersive spatial Project Cockpit as the primary active-work environment while preserving deep analytical work, project context, navigation, accessibility and bounded rendering.

That success should not be confused with visual completion.

The project owner has now deliberately reopened the Cockpit as a **broad design problem**, not merely another styling pass. The goal is to spend time making the Cockpit materially better, more advanced, more visually refined, more expressive, more dynamic where dynamism carries meaning, and more distinctive as a serious professional analytical product.

The exploration is intentionally allowed to challenge current implementation choices. Elements may be redesigned, simplified, removed, reorganized or replaced where the accepted interaction architecture does not require their current form.

Examples explicitly invited by the project owner include:

```text
richer grid/world treatment
small interaction and visual details
more meaningful connections between work units
dynamic connection behavior
light or signal movement where it communicates real state
clear differences between unresolved, active and completed work
better transitions
possible depth / 2.5D / 3D treatments
large redesigns rather than only incremental polish
```

The project owner also added an important requirement that must be elevated in this exploration:

> A compact native Cockpit composer must coexist with a serious long-form conversation experience. ADS users need to hold extended project conversations, revisit previous messages and continue discussions. The transcript cannot simply disappear after each short interaction.

This research therefore studies the Cockpit as a combined:

```text
spatial project operating environment
+
analytical workbench
+
methodological reasoning/control surface
+
long-form conversational workspace
```

without reducing the product to any one of those metaphors.

---

# 2. Governing boundary: what is already accepted versus what is open

## 2.1 Accepted interaction architecture

Specification 008 currently promotes the following V1 product model:

```text
Project Cockpit as primary immersive active-work environment
living project-process projection
meaningful work-unit semantics
spatial focus into real reusable specialist workspaces
reachability != simultaneous mounting
finite navigable world distinct from semantic project plane
2D project navigation and recovery
bounded geometric zoom and native pinch capability
viewport-aware semantic stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

These properties have real implementation and repeated human-review evidence. A visual redesign should therefore begin by **preserving the problem solved**, even if it replaces the current concrete visual treatment.

For example:

```text
accepted
    collision-safe floating interaction

not frozen
    exact right-side rail, popover shape or visual material
```

and:

```text
accepted
    stage orientation remains recoverable while navigating

not frozen
    current stage names, widths, typography or ruler treatment
```

and:

```text
accepted
    compact native system interaction belongs in the Cockpit

not frozen
    exact composer geometry or where the full transcript lives
```

## 2.2 Explicitly unfrozen space

Specification 008 deliberately leaves open:

```text
final Cockpit visual identity
final graph/canvas library
final gesture library
project auto-layout
semantic zoom / grouping
minimap
finite-world extent details
stage taxonomy and widths
stage-ruler material/treatment
permanent vertical tool-rail design
production project search
final URL contract
pan/zoom/HUD persistence details
canonical screenshot baseline
```

The new exploration therefore has legitimate room to be ambitious.

## 2.3 Foundation 021 remains binding

The visual target remains a modern premium professional analytical product that is:

```text
compact enough for serious work
+
clear enough for complex project state
+
polished enough to feel premium
```

The product should not become:

```text
a generic admin dashboard
a marketing page full of oversized cards
a decorative sci-fi visualization with poor analytical utility
a dense legacy enterprise interface with weak hierarchy
a giant chatbot with project state hidden in prose
```

Visual excellence and analytical correctness are separate requirements. Neither excuses weakness in the other.

---

# 3. Current implementation diagnosis

The existing Cockpit is valuable because it made the interaction architecture executable. It should now be treated as a **prototype substrate and evidence source**, not as the final visual template.

## 3.1 Current strengths

The implementation already demonstrates:

```text
large 2D navigable project world
continuous grid reserve
world-owned ambient depth
geometric zoom
native trackpad pinch candidate
viewport-aware stage ruler
meaningful work units
project connectors
Jump/search
fold-away chrome
floating composer
focus into Data / EDA / Missingness workspaces
browser Back and URL restoration
fullscreen
reduced-motion behavior
cross-platform browser gates
```

This gives the next design phase something concrete to critique rather than forcing design from prose only.

## 3.2 Current limitations that are especially relevant now

### Fixed representative geometry

`CockpitProjectMap.tsx` currently uses a fixed-size representative semantic canvas and explicit absolute node positions. This was appropriate for interaction validation but is not an adequate long-term scale strategy.

### Fixed connector paths

The representative map contains a short list of manually authored SVG paths. Most connectors share one visual treatment and only a deferred path currently receives a simple alternate class.

This means the current connector layer carries far less project meaning than it potentially could.

### Mostly shared card grammar

Current map work units are largely variations of one rounded rectangular card composition. Status changes border, background, icon treatment and opacity, but object meaning is still primarily text and icon based.

This is weaker than Foundation 021's longer-term requirement that project objects and meaningful work types should not all collapse into generic cards.

### Geometric zoom without a full semantic-scale system

The current project plane geometrically scales. Stage orientation is partly compensated in screen space, but the map does not yet provide a deliberate multi-level information architecture where different classes of information appear, aggregate or simplify by scale.

### Evolved stylesheet layers

The frontend currently imports the base Cockpit stylesheet followed by several review-specific override stylesheets. That history is useful evidence of iterative validation, but it is also a sign that the next coherent visual direction should eventually be consolidated into a design system rather than extended indefinitely through review-number overrides.

### Minimal conversation depth

The composer proves native Cockpit system interaction, but the current product does not yet provide the serious searchable long-form transcript/workspace that the project owner now requires.

This is not actually a contradiction with earlier design work. Research 002 already recorded an unresolved question:

```text
Where does the conversational transcript live when the composer is minimal?
```

The current exploration should now answer that question at product-design level.

---

# 4. External research method

The goal of external research is not to find one application to imitate. ADS combines concerns that normally appear in separate product categories:

```text
spatial design tools
workflow / lineage graphs
data orchestration control planes
professional developer tools
agent/chat workspaces
analytical environments
large graph visualizations
motion systems
map-style level-of-detail systems
```

References were therefore selected because each solves part of the problem well.

For every reference, the useful question is:

```text
What product problem is this pattern solving?
Does ADS have the same problem?
Which principle transfers?
Which implementation or visual convention should not be copied blindly?
```

---

# 5. External reference findings

## 5.1 React Flow: rich spatial interaction is now a credible implementation comparator

Current React Flow documentation is materially relevant to the new exploration.

### Animated edges

React Flow demonstrates custom edge implementations in which SVG elements can move directly along an arbitrary edge path with `<animateMotion>`. Its examples also show ordinary DOM/React nodes moving along paths through the Web Animations API.

This validates the technical plausibility of the project owner's idea of a light, signal packet or other compact indicator moving along a relation.

The important ADS implication is not "animate all edges". It is:

> Relationship animation can be implemented as a state-bearing visual channel when project semantics justify it.

### Contextual zoom

React Flow also demonstrates nodes changing the content they render according to current zoom.

That directly supports a serious ADS semantic-scale hypothesis:

```text
low scale
    topology / stage / state

medium scale
    work-unit identity and status

high scale
    richer evidence / metrics / rationale

focus
    full analytical workspace
```

### Viewport behavior

React Flow exposes pan/zoom configurations similar to design tools, including scroll/pinch behavior and design-tool-style controls. This overlaps with capabilities ADS already had to implement manually.

### Performance warnings

React Flow's own performance guidance is equally important. It explicitly warns about:

```text
unnecessary node/edge subscriptions and rerenders
large expanded node trees
complex node/edge styles
heavy animation, shadow and gradient use at scale
```

It recommends memoization, selective state, collapsing large trees and simplifying styles if necessary. It also provides an `onlyRenderVisibleElements` optimization for large graphs.

### ADS interpretation

React Flow now deserves a serious prototype comparison because the new requirements are closer to the problems it solves:

```text
richer edge behavior
semantic-scale node content
grouping / collapse
large project navigation
future layout integration
built-in spatial interaction primitives
```

This is still not a technology decision. The current DOM/CSS/SVG implementation has lower dependency complexity and full control. A comparative prototype should establish whether React Flow's capabilities actually reduce complexity and improve product quality for ADS.

References:

- https://reactflow.dev/examples/edges/animating-edges
- https://reactflow.dev/examples/interaction/contextual-zoom
- https://reactflow.dev/learn/advanced-use/performance
- https://reactflow.dev/api-reference/react-flow
- https://reactflow.dev/learn/concepts/the-viewport

---

## 5.2 Dagster: flexible information density and graph scalability

Dagster provides two especially transferable lessons.

### Facets

Dagster+'s newer lineage interface uses **facets** so users can selectively reveal metadata on graph objects. A user may want a clean lineage graph in one moment and rich information such as owners, automation conditions, latest materializations and health at another.

This is strongly applicable to ADS because a serious project map contains too many potentially useful dimensions to show all at once.

A future ADS equivalent could expose view lenses such as:

```text
Minimal
    topology + status

Methodology
    recommendations + blockers + unresolved questions

Evidence
    findings + evidence/provenance emphasis

Execution
    active runs + waiting states + failures

Review
    approvals + decisions + unresolved human questions
```

Those names are hypotheses only. The transferable principle is **user-controlled contextual information density**.

### Large graph scaling

Dagster's detailed account of scaling asset graphs to thousands of nodes is a useful warning. Rendering every edge remained expensive even after node virtualization, and excessive edges were also visually unhelpful. Dagster chose to suppress edges whose relevant endpoints were not visible under certain high-density conditions, preserve manually highlighted relationships, add navigational support and use collapsible groups.

The broader ADS lesson is:

> A renderer that can technically draw thousands of relationships does not make a thousand-relationship project view understandable.

ADS should continue to project the relevant project-process view rather than expose its complete object graph.

References:

- https://dagster.io/blog/introducing-the-new-dagster-plus-ui
- https://dagster.io/blog/scaling-dag-visualization

---

## 5.3 Linear: contextual commands, hierarchy and small interaction quality

Linear remains a useful reference for professional information density rather than spatial graph rendering.

### Contextual command architecture

Linear's command system groups and prioritizes actions according to what the user is currently focused on. It also allows command interactions to appear close to the UI object that invoked them while remaining searchable and keyboard controllable.

ADS currently has Jump/search plus several explicit controls. The next design should ask whether future control growth is better handled through one **context-aware command surface** rather than permanently adding buttons.

Possible ADS command groups might respond to:

```text
map focus
selected work unit
focused analytical workspace
conversation selection
active run
approval waiting state
```

### Hierarchy and density

Linear's design writing repeatedly emphasizes reducing noise while increasing useful hierarchy and information density. The useful transfer is the discipline of making many small details feel deliberate rather than adding visual spectacle for its own sake.

References:

- https://linear.app/changelog/2019-10-07-contextual-command-menu
- https://linear.app/changelog/2019-12-18-new-command-menu

---

## 5.4 VS Code: the strongest reference for compact interaction plus deep conversation history

The project owner's long-form conversation requirement has a very strong current analogue in VS Code's agent surfaces.

VS Code separates the idea of a **session/conversation** from the surface used to display it.

Its Chat view exposes:

```text
sessions list
conversation history
chat input
compact or side-by-side layouts
optional separate window
```

Current agent-session management goes further:

```text
multiple sessions
multiple chats within a session in some environments
chat tabs
side-by-side or stacked chat groups
restored conversation history
restored split sizes
forking from conversation history
archiving without deletion
export
searchable/queryable session history
```

The most important ADS lesson is architectural:

> Persistent conversation state does not have to be represented as a permanent giant chat column.

The same underlying conversation can be available through several presentation states.

For ADS, the minimal composer can remain native to the project map while a full conversation surface can expand, dock, split or focus without becoming a different conceptual conversation.

A second important lesson is **conversation lifecycle**. Long-running professional use requires users to find, reopen, branch, archive and understand prior discussions. ADS does not need to copy VS Code's exact session model, but a transcript that is merely hidden DOM above the composer is insufficient.

References:

- https://code.visualstudio.com/docs/agents/run/chat-view
- https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions
- https://code.visualstudio.com/docs/agents/concepts/sessions
- https://code.visualstudio.com/docs/agents/run/sessions/session-history

---

## 5.5 LangSmith Studio: graph and conversation can be different views over persistent thread state

LangSmith Studio is useful because it explicitly supports both graph-oriented and chat-oriented views over agent execution.

Its current Studio documentation distinguishes:

```text
Graph mode
    detailed execution/state visibility

Chat mode
    simpler conversation-oriented interaction
```

It also treats a thread as a persistent conversation container whose state survives multiple runs. Threads can be selected, inspected and forked from prior checkpoints.

ADS should not inherit LangGraph/LangSmith persistence semantics merely because this UX pattern is useful. ADS already has an ADS-owned project model and a separate runtime architecture.

The transferable design principle is:

> One durable interaction context can have multiple views optimized for different user jobs.

For ADS those views may be:

```text
Cockpit map
Conversation Workspace
focused analytical workbench
history / provenance inspection
```

rather than forcing all four concerns into one visual panel.

References:

- https://docs.langchain.com/langsmith/studio
- https://docs.langchain.com/langsmith/use-studio
- https://docs.langchain.com/langsmith/use-threads

---

## 5.6 Motion for React: a stronger candidate for interruptible product transitions

The current Cockpit has already explored the browser View Transition API. The broader design phase should compare that with a dedicated motion layer rather than assuming one mechanism must serve every transition.

Motion for React currently supports:

```text
layout animation
shared-element transitions through layoutId
gestures
presence transitions
scroll-linked animation
reduced-motion configuration
```

Its layout engine animates real elements with transforms and explicitly emphasizes interruptibility and non-blocking interaction. That is attractive for Cockpit interactions where users can act quickly and should not wait for a decorative transition to finish.

Potential ADS uses include:

```text
work unit -> focused workspace handoff
composer -> expanded Conversation Workspace
inspector docking / undocking
stage / lens changes
compact status indicator -> detailed run surface
```

The accessibility documentation is equally important. Motion can disable transform/layout animation for users requesting reduced motion while preserving less physically disruptive changes such as opacity/background transitions.

This fits ADS's existing accessibility boundary.

References:

- https://motion.dev/docs/react
- https://motion.dev/docs/react-layout-animations
- https://motion.dev/docs/react-accessibility

---

## 5.7 Microsoft Semantic Zoom and Mapbox: zoom should alter information density, not merely magnification

Microsoft's Semantic Zoom documentation makes a useful conceptual distinction:

```text
optical/geometric zoom
    magnifies the same representation

semantic zoom
    switches between different views of the same underlying content
```

It also recommends preserving predictable layout/panning relationships between scales.

Mapbox provides another useful implementation analogy. Mapbox camera expressions can change visual properties according to zoom level, allowing information density, marker size, labels and other representations to vary continuously with scale.

ADS does not need to implement one binary zoom-out/zoom-in switch. A stronger project map can use several controlled representation bands.

The key constraint is semantic continuity:

> Zooming should reveal more or less detail about the same project state, not silently change the project's scope or meaning.

References:

- https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/semantic-zoom
- https://docs.mapbox.com/mapbox-gl-js/guides/styles/style-layers/

---

## 5.8 Cytoscape.js and Sigma.js: large graph renderers reinforce that visual complexity is the real limit

Cytoscape.js explicitly notes that large graphs become slower as element count and style complexity increase, and that edges are especially expensive.

Sigma.js takes a different route. Its current rendering architecture is WebGL oriented and designed for graphs with tens of thousands of nodes and edges. It also adjusts item sizes with zoom so graph elements remain readable instead of scaling naively.

The contrast is useful for ADS technology selection:

```text
React-rich semantic work units
    likely favor DOM/React-oriented canvas abstractions

very large mostly graphical networks
    may favor WebGL-oriented renderers such as Sigma
```

ADS's primary Cockpit is currently much closer to the first case. Work units contain meaningful controls, statuses and potential accessibility semantics rather than only circles and labels.

Sigma remains valuable as a comparator if future project projections become dramatically larger or if ADS introduces a separate large-scale graph view.

References:

- https://js.cytoscape.org/
- https://www.sigmajs.org/docs/advanced/sizes/
- https://v4.sigmajs.org/concepts/rendering/
- https://v4.sigmajs.org/how-to/technical/performance/

---

## 5.9 PixiJS: a possible hybrid ambient/world rendering layer

PixiJS is a GPU-oriented 2D rendering option that may be more relevant to the user's desired visual sophistication than a full 3D engine.

It provides:

```text
high-throughput 2D scene rendering
culling
render groups
custom GPU-oriented visual effects
filters and blend behavior
```

Its documentation also warns that filters, masks, blend changes and unnecessary scene complexity carry real costs.

This suggests a potentially useful **hybrid architecture hypothesis**:

```text
DOM / React
    semantic work units
    text
    controls
    accessibility

SVG / graph layer
    semantic connections where DOM/SVG is sufficient

optional Pixi world layer
    ambient grid
    local activity fields
    lightweight signal particles
    high-volume decorative/non-semantic spatial effects
```

The important word is optional. Adding a GPU renderer merely to make a few gradients look nicer would be unjustified complexity.

References:

- https://pixijs.com/8.x/guides/concepts/performance-tips
- https://pixijs.com/8.x/guides/concepts/render-groups
- https://pixijs.com/8.x/guides/components/application/culler-plugin

---

## 5.10 React Three Fiber: 3D is possible, but should have to prove analytical value

React Three Fiber makes sophisticated React-integrated WebGL feasible, but its own performance guidance reinforces an important product restraint. Continuous WebGL rendering consumes resources; on-demand rendering is recommended where scenes can rest.

This strongly supports testing **2.5D depth cues** before committing to a permanent full 3D world.

Examples of bounded depth that may be useful:

```text
selected work unit lifts slightly from the world
active relationship rises one visual layer
project world subtly recedes during focus
floating control surfaces occupy clearly separated depth planes
a short perspective cue helps establish transition direction
```

These can provide spatial richness while keeping analytical text front-facing and readable.

A permanent perspective scene full of rotated information cards should be treated skeptically unless prototype evidence shows it improves comprehension.

References:

- https://r3f.docs.pmnd.rs/advanced/scaling-performance
- https://r3f.docs.pmnd.rs/advanced/pitfalls

---

## 5.11 Airflow and Prefect: process topology and execution state should remain distinguishable

Airflow's current UI deliberately provides separate but related views such as:

```text
Grid View
Graph View
Runs
Tasks
Events
Code
Details
```

Graph View can overlay a particular run's task states on dependency structure, while Grid View is optimized for seeing execution state over many runs.

Prefect similarly distinguishes a workflow definition from the state of a particular run. States such as running, retrying, completed, failed, cancelled or late describe execution instances.

The ADS lesson is important:

> Project-process state, methodological status and runtime execution state should not be collapsed into one overloaded color/status variable.

A work unit might simultaneously be:

```text
methodologically REQUIRED
project disposition ACTIVE
current run WAITING_FOR_TOOL
human approval NOT_REQUIRED
```

The Cockpit needs a controlled visual grammar that reveals the right dimension for the current user task rather than pretending there is one universal status.

References:

- https://airflow.apache.org/docs/apache-airflow/stable/ui.html
- https://docs.prefect.io/v3/concepts/states

---

# 6. Cockpit Design Exploration Map

The next visual program should explore the following areas as connected but separable design problems.

```text
A. Spatial world / canvas
B. Grid and ambient world
C. Work-unit visual grammar
D. Relation / connector semantics
E. Semantic zoom and level of detail
F. Stage / project orientation
G. Focus transitions and workspace handoff
H. Runtime / execution visualization
I. Blocked / unresolved / approval / completed / deferred state
J. Navigation, search and command surfaces
K. Conversation system and full transcript workspace
L. Inspectors / context / evidence surfaces
M. Information density and view lenses
N. Depth / 2.5D / bounded 3D
O. Motion language
P. Large-project scalability
Q. Light/dark visual identity
R. Accessibility and reduced motion
S. Rendering / interaction technology
T. Product-state loading, empty, error and recovery behavior
```

No single mockup should be considered sufficient if it only makes the resting project map attractive. The product must be tested while actually changing state, opening conversation, focusing analytical work, running tasks, resolving blockers and navigating large project structures.

---

# 7. Conversation architecture: from composer to serious project dialogue

This is a first-class design problem, not an accessory to the grid.

## 7.1 The required distinction

ADS should distinguish at least four concepts at product level:

```text
Composer
    lightweight entry point for speaking to the system from current context

Conversational response
    user-visible system answer, potentially concise when structured UI is more useful

Conversation history
    durable visible multi-turn dialogue the user can revisit

Conversation Workspace
    full surface for reading, searching and continuing long discussions
```

These terms do **not** yet define database entities.

## 7.2 Progressive conversation depth

A strong candidate interaction model is progressive depth:

```text
RESTING COCKPIT
    compact native composer

SEND / RECEIVE
    concise nearby response or response indicator
    project state can change visibly

EXPAND RECENT CONTEXT
    lightweight recent-turn surface when only a little history is needed

OPEN CONVERSATION WORKSPACE
    full searchable transcript
    long-form discussion
    project references
    conversation navigation
    continuing input
```

This preserves the existing principle that chat should not permanently dominate the Cockpit while solving the owner's requirement that the conversation remains available.

## 7.3 Candidate presentation modes

These should be prototyped rather than selected in prose.

### A. Docked Conversation Lens

```text
project map             conversation
or focused work         transcript
```

The conversation opens as a resizable side region. The Cockpit viewport responds to the occupied safe area instead of being hidden under it.

Advantages:

```text
simultaneous project + discussion
excellent for discussing visible work
familiar professional pattern
```

Risks:

```text
can drift back toward permanent giant sidebar
reduced horizontal project space
requires strong resize/collision behavior
```

### B. Conversation Focus Workspace

The composer expands spatially into a near-full/full conversation workbench, analogous to entering Data or EDA focus.

Advantages:

```text
full reading width
strong continuity with Cockpit focus metaphor
simple long-form transcript
```

Risks:

```text
less simultaneous map visibility
must preserve easy return and project context
```

### C. Split Workbench

Conversation and selected analytical surface occupy configurable panes. The project map may remain as a compact orientation layer or be temporarily replaced.

Advantages:

```text
best for deep analytical discussion
can compare chart/table/evidence directly with conversation
```

Risks:

```text
more layout complexity
split-state persistence decisions
can feel IDE-like if overdone
```

### D. Canvas-Anchored Conversation Surface

A conversation surface grows from the composer but remains visually part of the spatial Cockpit, perhaps with the project world visible/receded behind it.

Advantages:

```text
strongest visual continuity
potentially distinctive
```

Risks:

```text
harder to make long transcripts ergonomically excellent
higher motion/collision complexity
risk of decorative glass treatment
```

### E. Dedicated direct Conversation view plus Cockpit entry

A specialist Conversation route can coexist with any of the above, just as Data/EDA direct routes coexist with Cockpit focus.

This may be valuable for users who know they want to resume a long conversation directly.

## 7.4 Conversation and project state should be bidirectionally linked

Conversation should not become a parallel universe disconnected from structured project state.

Potential interactions:

```text
message references "Production missingness"
    -> hover/click highlights or opens the project work unit

project work unit
    -> "Discuss" opens conversation at related turns or starts scoped discussion

system response creates a Proposal / Question / Investigation
    -> transcript visibly records that structured project change

Decision accepted in Cockpit
    -> conversation can reference the resulting Decision object rather than only prose
```

This produces a stronger product than a generic chat log because the transcript becomes a navigational and explanatory surface over real project work.

## 7.5 Conversation is not the canonical home of consequential truth

Foundation 021 remains important:

```text
conversation
    useful discussion and interaction history

structured project state
    durable operational representation of consequential outcomes
```

If the user and system agree to defer a model benchmark, that decision should not remain true only because message 147 says so. It should be represented in project state and the transcript should link to or summarize that change.

## 7.6 Conversation should not expose hidden reasoning traces as product explanation

The full Conversation Workspace means the full **user-visible conversation**, not unrestricted internal chain-of-thought or raw orchestration traces.

Technical activity can be represented through inspectable user-facing summaries, run events, tool activity and provenance where useful.

## 7.7 Conversation lifecycle remains open

Product research should evaluate:

```text
one principal conversation per project
multiple named project conversations
contextual sub-conversations attached to work units
forks / branches for alternatives
archive / resume
search across project conversation history
conversation compaction and summary UX
whether recent context and complete history are represented differently
```

Do not freeze the persistence model simply by copying VS Code or LangSmith terminology.

---

# 8. Relation and connector semantics

The project owner's moving-light idea becomes much more valuable when treated as a semantic system.

## 8.1 Candidate relation vocabulary

A first visual hypothesis:

```text
SETTLED / SATISFIED RELATION
    stable low-contrast solid line
    no continuous animation

ACTIVE DEPENDENCY / CURRENT FLOW
    slightly stronger line
    sparse directional signal or travelling highlight
    animation stops when activity stops

UNRESOLVED DEPENDENCY
    segmented / incomplete line grammar
    restrained periodic cue only if attention is needed

BLOCKING DEPENDENCY
    visibly interrupted or gated relation
    blocker marker near meaningful boundary
    no successful-flow animation through the block

CANDIDATE / ALTERNATIVE PATH
    thin ghosted relation
    visually secondary until selected

DEFERRED PATH
    muted dashed treatment
    no active flow

EXECUTION IN PROGRESS
    transient signal packet / light travel
    visually tied to actual event state

FAILED EXECUTION
    brief failure transition
    settles into an inspectable failed state rather than flashing forever
```

Exact styling is deliberately unfrozen.

## 8.2 Motion should correspond to temporal truth

A useful rule:

> If a relation is moving, the user should be able to explain what is currently moving in the project.

This prevents a constant sci-fi circuit-board effect that looks advanced but conveys nothing.

## 8.3 Relationship direction must remain understandable without animation

Reduced-motion mode and static screenshots must still communicate direction/status through:

```text
path geometry
markers
line pattern
labels where needed
node state
```

Motion is an additional channel, never the only carrier of meaning.

## 8.4 Edge overload must be actively controlled

Potential scale techniques:

```text
render only project-process relations relevant to current projection
aggregate relationships at low semantic zoom
show local neighborhoods on selection
fade or omit low-value relations by lens
bundle/route common paths if understandable
preserve highlighted relations while suppressing irrelevant offscreen complexity
```

Dagster and Cytoscape both reinforce that edges are a major performance and comprehension cost.

---

# 9. Grid and spatial world

The current grid established spatial continuity. The next exploration can make it substantially richer without making it louder.

## 9.1 Multi-layer substrate hypothesis

```text
minor grid
    very low contrast
    useful at normal/high scale

major grid
    larger interval
    slightly stronger orientation cue

semantic regions
    stage / project structure
    clearly not identical to world grid

ambient world field
    restrained tonal/depth variation

local activity field
    appears only around meaningful current activity
```

## 9.2 Scale-aware grid behavior

At low zoom the minor grid may fade while larger spatial divisions remain. At high zoom the minor grid can become more useful for orientation and precision.

This follows the same logic as map/cartographic level of detail.

## 9.3 Dynamic local effects should be event-driven

Possible examples:

```text
current investigation
    faint local halo or density field

active run
    subtle localized activity shimmer

selection
    nearby grid intersections respond briefly

completion
    activity subsides into a calm settled region
```

These are hypotheses only. The resting world should remain calm.

## 9.4 World boundary

Specification 008 still permits a finite world. The next design should test whether the finite boundary can feel intentional rather than like an arbitrary large DIV.

Possible cues:

```text
very subtle grid attenuation
world-coordinate edge marker
soft depth falloff
no dramatic vignette
```

---

# 10. Semantic zoom and level of detail

Semantic zoom is one of the highest-value unresolved capabilities.

## 10.1 Candidate representation bands

These bands are exploratory, not frozen thresholds.

```text
PROJECT SCALE
    stage structure
    major branches
    compact work-unit glyphs
    active route
    major blockers / approvals
    little or no description prose

WORK SCALE
    title
    work-unit type
    status
    compact metrics / counts
    primary relations

INSPECTION SCALE
    concise description
    evidence / question counts
    current action
    richer relation labels

FOCUS
    normal full-resolution analytical workspace
```

## 10.2 Stable semantic identity

Across levels, a work unit should remain recognizably the same object/projection. The user should not feel that zooming changed the project's meaning.

Potential continuity mechanisms:

```text
consistent anchor position
stable icon / core mark
animated detail reveal rather than replacement jump
shared highlight language
```

## 10.3 Aggregation at low scale

Large projects may need grouped forms:

```text
stage cluster
investigation cluster
model-family cluster
completed-work summary
collapsed historical branch
```

Aggregation should be based on useful project semantics, not merely geometric proximity.

---

# 11. Work-unit visual grammar

A sophisticated Cockpit should not become a zoo of arbitrary shapes, but it should convey more than status-colored generic cards.

## 11.1 Separate identity dimensions

Visual design should distinguish at least:

```text
WHAT IS THIS?
    investigation / question / decision / model work / evaluation / finding-like milestone / run-related unit

WHAT IS ITS PROJECT DISPOSITION?
    active / recommended / deferred / completed / blocked / future

WHAT IS HAPPENING NOW?
    idle / running / waiting / failed / waiting for human

HOW IMPORTANT IS IT NOW?
    required / recommended / relevant / low-priority
```

These dimensions should not all fight for the same border color.

## 11.2 Candidate visual channels

Possible channels include:

```text
silhouette / edge geometry
small semantic glyph
surface material
left/top signature band
status marker
relation port treatment
background density
motion
z-depth
text hierarchy
```

The system should use the minimum set that remains learnable.

## 11.3 Completed work should settle

A useful product metaphor is that project regions become quieter as they become settled.

Completed units may:

```text
compact slightly at low zoom
lose transient animation
retain clear provenance/status
remain inspectable
recede behind current work without becoming invisible
```

This helps the project map feel alive while work is changing and calm where work is resolved.

---

# 12. Stage and project orientation

The current horizontal semantic stage ruler has good interaction evidence but its final visual treatment and taxonomy remain open.

Design alternatives should include:

```text
A. refined horizontal semantic ruler
B. soft stage fields/regions with persistent compact top orientation
C. stage clusters that collapse at project scale
D. more topology-driven orientation where stages are secondary metadata rather than dominant lanes
```

The project is nonlinear, so stages must never imply a mandatory waterfall pipeline.

A work unit may branch backward, reopen an earlier concern or span multiple methodological responsibilities.

Stage visuals should therefore communicate **orientation**, not false process certainty.

---

# 13. Motion language

Motion should become a coherent design system rather than a collection of CSS transitions.

## 13.1 Proposed motion categories

```text
NAVIGATION MOTION
    where did I go?

FOCUS MOTION
    what project object became my current workspace?

STATE-CHANGE MOTION
    what changed?

EXECUTION MOTION
    what is happening now?

ATTENTION MOTION
    what newly requires me?

COMPLETION MOTION
    what just resolved?

AMBIENT MOTION
    minimal life/depth without carrying critical information
```

## 13.2 Calm resting state

The Cockpit should not continuously advertise that it is dynamic.

A stronger principle is:

```text
project changing
    visibly alive

project settled
    visibly calm
```

Persistent animation should require persistent underlying activity.

## 13.3 Motion budget

The design system should eventually define:

```text
duration families
easing/spring families
maximum concurrent attention animations
which layers can move continuously
when animations cancel or retarget
reduced-motion substitutions
```

## 13.4 Interruptibility

Users should not become trapped waiting for transitions. A professional workbench should permit quick consecutive actions.

This is one reason Motion for React deserves comparison against whole-screen View Transition behavior for some Cockpit transitions.

---

# 14. Depth, 2.5D and 3D

## 14.1 Preferred exploration order

```text
1. strong 2D hierarchy
2. subtle depth/elevation
3. bounded 2.5D transition/depth experiments
4. full 3D only if earlier prototypes reveal a real problem it solves
```

## 14.2 Promising 2.5D uses

```text
selection lifts from grid
active path occupies a slightly nearer layer
focused workspace emerges from selected work unit
background project topology recedes during focus
conversation workspace docks on a distinct depth plane
approval surface clearly sits above ordinary inspection surfaces
```

## 14.3 Full 3D risk

A permanent 3D canvas can create:

```text
text readability problems
perspective distortion
harder keyboard/screen-reader mapping
higher GPU/battery cost
more difficult automated visual testing
interaction novelty that competes with analytical work
```

A full 3D prototype should therefore have to demonstrate measurable orientation/comprehension value, not only visual novelty.

---

# 15. Execution and temporal activity

Project structure and runtime activity should cooperate without becoming the same thing.

## 15.1 Candidate transient run layer

When a work unit is executing, a compact live layer might expose:

```text
queued
preparing
reasoning
executing
waiting for tool
waiting for approval
paused
completed
failed
cancelled
```

where those states are authoritative and meaningful.

The visual layer might include:

```text
small live marker on work unit
edge signal showing current downstream/upstream relation
compact duration/progress cue when meaningful
one-click expansion to richer run surface
```

## 15.2 History is not continuous animation

Once a run ends, its animation should stop. Historical execution remains inspectable through state/history views rather than leaving the world permanently animated to memorialize past activity.

---

# 16. Information-density lenses

Dagster's facets suggest a powerful ADS-specific design direction.

Instead of asking one work-unit card to expose every useful field, the Cockpit can support **view lenses**.

Exploratory examples:

```text
PROJECT LENS
    project topology and current status

METHODOLOGY LENS
    required/recommended/relevant guidance
    blockers and unresolved questions

EVIDENCE LENS
    findings/evidence/provenance emphasis

EXECUTION LENS
    runs, waiting states, failures, current activity

REVIEW LENS
    approvals, decisions, contested/unresolved work
```

The final design might use fewer or differently named lenses.

A lens should not change underlying truth. It changes **which dimensions are visually foregrounded**.

This can also be combined with semantic zoom:

```text
zoom
    controls detail by spatial scale

lens
    controls detail by user intent
```

Those are orthogonal mechanisms and should remain conceptually separate.

---

# 17. Navigation and command architecture

The current Jump/search surface solved immediate scale problems. Future Cockpit growth may require a more general command architecture.

## 17.1 Candidate hierarchy

```text
always-visible direct controls
    only frequent spatial essentials

contextual controls
    actions for current selection/focus

command/search surface
    rare or broad actions
    project search
    navigation
    view/lens switching
    run/approval actions where appropriate
```

## 17.2 Command surface should respect project context

Examples:

```text
no selection
    jump to active blocker
    find work
    open conversation
    fit project

selected Investigation
    discuss
    open evidence
    run next step
    defer

focused Data workspace
    find column
    ask about current view
    open related Question
```

This can reduce permanent tool-rail growth while remaining discoverable.

---

# 18. Large-project scalability

The project should explicitly design for a future map far larger than the current ten-unit fixture.

## 18.1 Scalability is both computational and cognitive

```text
renderer can draw it
    !=
user can understand it
```

Both gates matter.

## 18.2 Candidate controls

```text
project-process projection remains bounded
semantic zoom
stage/semantic grouping
collapse/expand
relevant-neighborhood emphasis
viewport virtualization / culling
edge suppression/aggregation
search/jump
lens-specific filtering
layout caching where warranted
lazy detail loading
```

## 18.3 Stress fixtures required

Future prototypes should not only use the current churn fixture.

At minimum create synthetic/representative project maps around:

```text
small       10-20 visible work units
medium      50-100 projected work units
large       250+ projected work units with clustering
branchy     many competing investigations / reopened work
run-heavy   many simultaneous or recently completed runs
```

The goal is not to claim every project should show 250 full cards. It is to test whether semantic grouping prevents that failure mode.

---

# 19. Accessibility and reduced motion

Accessibility remains part of professional quality and should influence the visual architecture from the start.

## 19.1 Required static redundancy

No meaning may rely only on:

```text
color
motion
spatial position
depth
hover
```

Status and relationships need semantic text/ARIA equivalents and recoverable keyboard behavior.

## 19.2 Reduced motion

For reduced-motion users:

```text
large scale/translation transitions
    -> fade or near-instant state change

continuous ambient movement
    -> disabled or greatly reduced

execution motion
    -> static live-state indicator

moving edge signal
    -> static directional/state treatment
```

The final destination and project meaning must be identical.

## 19.3 Conversation accessibility

A long transcript introduces additional requirements:

```text
logical message reading order
keyboard movement between transcript and composer
search result navigation
focus restoration when closing/docking
screen-reader announcement of new responses without reading entire history again
accessible links from messages to project objects
```

---

# 20. Technology exploration matrix

No technology is selected by this research.

| Candidate | Strongest ADS fit | Main risk / limitation | Prototype trigger |
|---|---|---|---|
| Current React + DOM/CSS/SVG | Maximum control, accessibility, already proven | Manual spatial/layout/edge complexity grows | Keep as control baseline |
| React Flow | React-rich nodes, pan/zoom, edges, grouping, semantic node content, visibility options | Dependency/model constraints and rerender/style cost at scale | Prototype richer semantic edges + grouping + zoom |
| React Flow + Dagre/ELK-style layout | Automatic directed/project layout | Layout may fight desired project semantics or become unstable | Medium/large fixture prototype |
| Motion for React | Shared-element/focus/docking transitions, interruptibility, reduced motion | Adds motion abstraction and bundle/runtime surface | Prototype node -> focus and composer -> conversation |
| Sigma.js | Very large WebGL graph rendering | Less natural for rich DOM work units and forms | Only if scale evidence demands mostly graphical rendering |
| PixiJS hybrid layer | Rich 2D ambient world/signals with GPU acceleration | Extra renderer synchronization/complexity | Only if CSS/SVG cannot meet visual/performance target |
| React Three Fiber | True depth/3D experiments | GPU cost, interaction/accessibility complexity, novelty risk | Bounded experimental 2.5D prototype only |
| Pure browser View Transition API | Native capability, low dependency | Whole-screen snapshots/interruption limits for some interactions | Retain as baseline for appropriate transitions |

The strongest current hypothesis is **layered specialization**, not one universal renderer:

```text
semantic controls/text/workspaces
    DOM/React

project topology / spatial interaction
    current DOM/SVG or React Flow candidate

advanced ambient effects
    CSS/SVG first
    optional GPU layer only if earned

full analytical focus
    ordinary full-resolution DOM workspaces
```

---

# 21. Candidate design directions for mockup exploration

These directions are intentionally distinct enough to reveal trade-offs.

## Direction A: Precision Instrument

Character:

```text
quiet
premium
high information hierarchy
extremely restrained motion
fine technical grid
clean semantic connectors
very strong typography
subtle depth
```

Key hypothesis:

> ADS can feel advanced primarily through precision, hierarchy, semantic detail and extremely high-quality microinteraction rather than visible spectacle.

Potential strengths:

```text
professional trust
long-session comfort
high information density
lower motion risk
```

Potential failure:

```text
may feel too conventional or insufficiently alive
```

## Direction B: Living Analytical Field

Character:

```text
calm world at rest
project activity becomes visible spatially
semantic signals move through active relations
local activity fields
strong semantic zoom
completed regions settle
```

Key hypothesis:

> The Cockpit can make analytical progress perceptible as a living system without turning into decorative science fiction.

Potential strengths:

```text
distinctive ADS identity
excellent live-state communication
strong project-at-a-glance understanding
```

Potential failure:

```text
motion/effects may become distracting or expensive if not tightly governed
```

## Direction C: Spatial Control Room

Character:

```text
more operational
project map + compact live status
information lenses/facets
contextual command system
strong execution/review visibility
```

Key hypothesis:

> Advanced ADS users may benefit more from controllable information density and operational awareness than from a highly expressive world.

Potential strengths:

```text
power-user clarity
execution observability
scales to many project dimensions
```

Potential failure:

```text
could become enterprise-dense or dashboard-like
```

## Direction D: Depth-Aware Workbench

Character:

```text
2.5D spatial layering
selected work physically lifts
project recedes into depth on focus
conversation and analytical surfaces dock on clear depth planes
bounded perspective cues
```

Key hypothesis:

> Depth can strengthen spatial orientation and continuity if used only at transitions and hierarchy boundaries.

Potential strengths:

```text
advanced visual identity
excellent focus continuity
```

Potential failure:

```text
novelty may outrun usability
performance/accessibility complexity
```

The likely final direction may combine selected elements from several candidates. They should still be prototyped independently first so the comparison remains meaningful.

---

# 22. Prototype and evaluation program

Implementation should not begin as one large redesign commit.

## 22.1 First prototype artifacts

Before product code changes, produce realistic visual compositions for the same project state across candidate directions.

At minimum each direction should show:

```text
1. resting project overview
2. active Investigation with live relation activity
3. hard blocker affecting downstream work
4. completed branch next to unresolved branch
5. selected work unit
6. semantic zoomed-out project state
7. expanded long-form Conversation Workspace
8. conversation + analytical work side-by-side or alternative chosen mode
9. running work / waiting-for-human state
10. dark and light appearance sample
```

## 22.2 Representative scenario

Continue using a controlled scenario so visual differences are comparable:

```text
Customer Churn Prediction
prediction moment unresolved
production missingness investigation active
chronological validation selected
baseline model completed
Random Forest benchmark deferred
evaluation downstream
```

Add enough transcript history to make the Conversation Workspace genuinely long rather than a three-message mock.

## 22.3 Evaluation questions

### Product comprehension

```text
Can the user identify what is active within five seconds?
Can the user identify what is blocking downstream validity?
Can the user tell which work is settled versus merely inactive?
Are relationship meanings understandable without a legend after reasonable learning?
```

### Spatial orientation

```text
Does zoom preserve identity and position?
Does semantic zoom reduce clutter rather than create popping confusion?
Can the user recover current stage/branch?
```

### Conversation

```text
Can the user open old discussion quickly?
Can the user search/revisit earlier messages?
Can the user discuss a visible project object without losing project context?
Does expanding chat feel like the same ADS workspace rather than opening a generic chatbot?
Can structured project changes be seen from the transcript?
```

### Motion

```text
Does movement communicate real project state?
Is the resting state calm?
Can the user interrupt transitions?
Does reduced-motion mode preserve meaning?
```

### Professional quality

```text
Would the surface support hours of analytical work?
Does it feel distinctive without becoming theatrical?
Are typography, spacing and density excellent?
Does dark mode preserve hierarchy rather than merely invert colors?
```

### Scale

```text
Does medium/large project state remain understandable?
What is grouped or suppressed?
Do edges become noise?
What happens when many runs are active?
```

## 22.4 Technical proof spikes only after visual selection

Once one or two directions are preferred, create bounded technical spikes for the uncertain mechanisms, for example:

```text
React Flow semantic edge + contextual zoom proof
Motion focus/conversation transition proof
medium/large project auto-layout proof
optional Pixi ambient-world proof
optional bounded 2.5D depth proof
```

Do not adopt all candidate technologies in one branch.

---

# 23. Independent Claude exploration under MC-0004

Because visual/product design is high-impact and susceptible to anchoring, this exploration uses the accepted `INDEPENDENT_THEN_COMPARATIVE` collaboration mode.

The neutral brief was frozen before this Research 037 candidate at:

```text
bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
```

Claude Phase A should therefore produce its own design from the accepted baseline and neutral user requirements without seeing this document.

After Claude's independent proposal is durably preserved:

```text
Research 037
+
Claude independent proposal
    -> comparative synthesis
    -> explicit convergence/disagreement
    -> strongest alternatives
    -> human visual/product preference where normative
```

Agreement will not automatically promote a design. Disagreement will not automatically favor the more conservative design.

---

# 24. Current research conclusions

The research supports several **high-value hypotheses** that deserve mockup/prototype testing:

1. **Semantic zoom is probably one of the largest remaining quality/scalability opportunities.** The project should not rely on geometric shrink alone.
2. **Connections can become a true project-state language.** Sparse directional motion should correspond to real temporal activity, not decoration.
3. **The world/grid can become richer while remaining calm.** Multi-scale grid layers and local event-driven effects are promising.
4. **Completed work should visually settle.** Dynamic activity should reduce as project state becomes resolved.
5. **Information lenses/facets may solve the conflict between comprehensiveness and visual calm.**
6. **A context-aware command surface can prevent permanent control proliferation.**
7. **The compact composer must expand into a first-class Conversation Workspace.** Long transcript history, search/re-entry and links to project state are now part of the design problem.
8. **Conversation presentation and conversation persistence should be separated conceptually.** A persistent dialogue can appear as compact composer, dock, split, focus workspace or direct view without becoming several unrelated conversations.
9. **2.5D depth is more promising than default full 3D.** Depth should serve orientation and focus before spectacle.
10. **Motion should become a governed design language.** The resting Cockpit should be calm; activity should make it alive only when something is actually happening.
11. **React Flow now deserves a real comparator spike.** The new semantic-edge, grouping, contextual-zoom and scale requirements are closer to capabilities that may justify the dependency.
12. **The final renderer may be layered.** DOM/React remains strongest for semantic work and accessibility; GPU rendering should be introduced only for problems CSS/SVG cannot solve adequately.
13. **Large-project design must be tested explicitly.** Ten attractive fixed cards are not evidence of a scalable Cockpit.
14. **The current implementation should remain the control baseline.** Redesign should be compared against it rather than erasing working evidence prematurely.

These are research conclusions and prototype priorities, not promoted product decisions.

---

# 25. Explicit non-decisions

Research 037 does **not** select or freeze:

```text
final Cockpit visual identity
final grid appearance
final color palette
final work-unit shapes
final connector grammar
whether active edges use travelling light
final semantic-zoom thresholds
final information lenses
final Conversation Workspace mode
conversation persistence/thread data model
number of conversations per project
final motion library
React Flow
Dagre / ELK / another layout engine
PixiJS
Sigma.js
React Three Fiber
full 3D
2.5D production use
final stage taxonomy
final command system
final minimap
final runtime-status visual vocabulary
final implementation branch/specification
```

No production frontend code should be changed merely because this map lists a promising idea.

---

# 26. Next legitimate step

The immediate design sequence is:

```text
1. preserve this research and the deliberate active-boundary switch
2. obtain Claude's blind Phase-A MC-0004 design from neutral brief commit
3. preserve Claude's independent proposal
4. compare the two explorations explicitly
5. identify 2-4 strongest visual directions/mechanisms
6. produce realistic static/interactive mockups before changing production Cockpit architecture
7. perform human product review
8. open a bounded prototype specification only after the preferred direction is clear enough
```

The permanent source-vault bootstrap remains deliberately paused, not rejected or superseded. Its Course 2 gate remains unchanged.

---

# 27. External sources consulted

Accessed 2026-08-26 unless stated otherwise.

## Spatial graph / interaction

- React Flow, Animating Edges: https://reactflow.dev/examples/edges/animating-edges
- React Flow, Contextual Zoom: https://reactflow.dev/examples/interaction/contextual-zoom
- React Flow, Performance: https://reactflow.dev/learn/advanced-use/performance
- React Flow, ReactFlow API: https://reactflow.dev/api-reference/react-flow
- React Flow, Panning and Zooming: https://reactflow.dev/learn/concepts/the-viewport
- Cytoscape.js, performance documentation: https://js.cytoscape.org/
- Sigma.js, node and edge sizes: https://www.sigmajs.org/docs/advanced/sizes/
- Sigma.js v4 rendering: https://v4.sigmajs.org/concepts/rendering/
- Sigma.js v4 performance: https://v4.sigmajs.org/how-to/technical/performance/

## Data/workflow product UI

- Dagster, new Dagster+ UI and lineage facets: https://dagster.io/blog/introducing-the-new-dagster-plus-ui
- Dagster, scaling DAG visualization: https://dagster.io/blog/scaling-dag-visualization
- Apache Airflow 3 UI overview: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
- Prefect 3 states: https://docs.prefect.io/v3/concepts/states

## Command / professional interaction patterns

- Linear, contextual command menu: https://linear.app/changelog/2019-10-07-contextual-command-menu
- Linear, new command menu: https://linear.app/changelog/2019-12-18-new-command-menu

## Conversation / agent workspace patterns

- VS Code, Chat view: https://code.visualstudio.com/docs/agents/run/chat-view
- VS Code, manage agent sessions: https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions
- VS Code, sessions and handoff: https://code.visualstudio.com/docs/agents/concepts/sessions
- VS Code, session history: https://code.visualstudio.com/docs/agents/run/sessions/session-history
- LangSmith Studio: https://docs.langchain.com/langsmith/studio
- LangSmith, use Studio: https://docs.langchain.com/langsmith/use-studio
- LangSmith, use threads: https://docs.langchain.com/langsmith/use-threads

## Motion / scale / rendering

- Motion for React: https://motion.dev/docs/react
- Motion layout animations: https://motion.dev/docs/react-layout-animations
- Motion accessibility: https://motion.dev/docs/react-accessibility
- Microsoft Semantic Zoom: https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/semantic-zoom
- Mapbox GL JS style expressions: https://docs.mapbox.com/mapbox-gl-js/guides/styles/style-layers/
- PixiJS performance tips: https://pixijs.com/8.x/guides/concepts/performance-tips
- PixiJS render groups: https://pixijs.com/8.x/guides/concepts/render-groups
- PixiJS culling: https://pixijs.com/8.x/guides/components/application/culler-plugin
- React Three Fiber scaling performance: https://r3f.docs.pmnd.rs/advanced/scaling-performance
- React Three Fiber performance pitfalls: https://r3f.docs.pmnd.rs/advanced/pitfalls
