# Research 087: Holistic Integrated Cockpit Baseline and Accepted-Invariants Audit

**Date:** 2026-08-28  
**Status:** Active Phase-C integration evidence  
**Scope:** Pauses isolated component-by-component browser exploration and reconstructs the accepted/held Project Cockpit decisions from the beginning of the current Cockpit design phase into one coherent executable Cockpit baseline.  
**Authority:** Research and integration evidence only. This memo does not promote provisional shell geometry, final header/chrome composition, grid/world dimensions, specialist-workspace internals, co-present conversation proportions, final conversation transition choreography, or production implementation architecture.  

## 1. Trigger

The project owner explicitly changed the design process boundary.

The current design phase had accumulated substantial evidence through separate bounded browsers. That was useful for discovering and selecting individual mechanisms, but continuing to add isolated component browsers now risks losing the product-level interaction between those decisions.

The requested process change is:

```text
PAUSE new isolated design questions

collect the accepted / held results
    from the beginning of the current Cockpit design phase

reconstruct them in one actual Cockpit

review the whole product surface

then continue refinement from that integrated Cockpit
    instead of treating every later question as a separate universe
```

This is an integration boundary, not a request to freeze every unresolved detail.

## 2. Why this is the right point to integrate

The project now has enough held evidence that interaction between mechanisms matters more than discovering another standalone visual treatment.

Examples:

```text
SEL2 selection
    now matters together with
X5 contextual expansion
    together with
Z7 deep dive
    together with
Conversation Workspace access

runtime / BLOCKED carriers
    now matter together with
category grammar
    disposition
    attention
    relation class
    current-process focus

Conversation Workspace
    now matters together with
Grid state preservation
    Deep Dive state preservation
    project-general vs work-unit scope
    Boxes/Text navigation
    A6 context expansion
```

The integrated browser is therefore intended to expose inconsistencies that individual design-lab slices cannot reveal.

## 3. New integrated browser

Local route:

```text
http://localhost:5173/design-lab/cockpit-integrated-baseline.html
```

Files:

```text
frontend/design-lab/cockpit-integrated-baseline.html
frontend/design-lab/cockpit-integrated-baseline.css
frontend/design-lab/cockpit-integrated-baseline.js
```

Exact initial holistic frontend target:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

Production `/cockpit` remains untouched.

## 4. Accepted-invariants reconstruction audit

The integrated browser must be judged against the accepted/held decisions below rather than by copying the latest single fixture wholesale.

### 4.1 Project world

Held:

```text
G4 Adaptive Hybrid world
    dark baseline
    visible 20px grid
    stronger 100px major-grid structure
    travelling currents
    restrained major-grid glints
    slow ambient world depth
    no authored fixed ambient focal coordinates
```

Integrated browser:

```text
20px + 100px grid layers
travelling horizontal and vertical currents
major-grid glints
restrained dark technical world
```

Exact original accepted target remains preserved in prior research history.

### 4.2 Work-unit rest and hover

Held H4 model:

```text
REST
    localized asymmetric in-box category-colored illumination
    narrow soft outward spill
    reduced resting light

HOVER
    stronger full halo
    pointer-following hotspot
    local world emphasis
    connector emphasis conceptually available
    restrained perimeter sweep
    2px lift
    fast entry / smoother release
```

Integrated browser reconstructs the reduced resting light, pointer-following hotspot, outward spill, 2px lift and restrained perimeter sweep.

### 4.3 Category grammar

Held:

```text
Question / Blocker        circle / yellow
Investigation             square / green
Validation / Analysis     triangle / blue
Model Work                diamond / red
Evaluation                plus / purple
```

The integrated browser uses this grammar directly.

### 4.4 Appearance controls

Foundation 023 remains held:

```text
ADS owns semantic meaning
+
user controls approved non-semantic appearance dimensions
```

Integrated appearance controls:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light

Connector terminal
    Clean
    Micro dots
    Frame sockets
    Direction arrows

Runtime carrier
    Dot + dynamic ring
    T7 Soft Shade tag
```

These are appearance controls only. They do not change semantic state.

### 4.5 Connectors, relation class and directionality

Held:

```text
E5 Hue + Tag relation class
D0-D3 semantic directionality model
one active terminal treatment
hover/focus orthogonal to terminal treatment
```

Exact accepted targets remain:

```text
directionality
    07d573b6569b9f09a3b7e00936f3eadecee721b3

relation class E5
    497e81f06ba1f9901511449237d1bb9f96b2d108
```

The integration uses relation-hue + tag connectors and direction arrows as the initial user appearance setting, while preserving the terminal-treatment switch.

### 4.6 Project disposition

Held P7:

```text
Neutral Tag + Tone

REST
    category remains dominant
    neutral disposition tag
    Completed / Deferred / Future recede tonally

HOVER
    state-specific disposition color may reveal
```

Exact accepted target:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The integrated browser keeps category dominant and uses tonal recession for Deferred, Future and Completed.

### 4.7 Current-process focus

Held:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

The integrated browser currently exposes the first two as the primary holistic interaction. The richer editable-set tooling remains preserved from its accepted browser and is not reimplemented as a new shell decision here.

Exact accepted editable-focus target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

### 4.8 Runtime and operational status

Held conditional runtime semantics:

```text
NONE
QUEUE
RUN
WAIT
HUMAN
FAIL
```

with:

```text
No runtime
    !=
Idle runtime
```

Held operational presentation:

```text
one carrier per live runtime or BLOCKED status
user-switchable globally between
    Dot + dynamic ring
    T7 Soft Shade tag
```

Held BLOCKED / FAIL distinction:

```text
BLOCKED
    red center dot
    sharper non-circular ring

FAIL
    red center dot
    smoother circular ring
```

Exact targets:

```text
T7 Soft Shade
    08534f94c2f272f969159087de2797a23e36b330

switchable runtime carrier
    fb847bd65ff6e5e4203a89ee2d4f74b7187c8359

BLOCKED/status carrier
    88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

The integrated fixture includes RUN and BLOCKED examples and the global carrier switch.

### 4.9 BLOCKER / BLOCKS / BLOCKED

Held conceptual model:

```text
BLOCKER
    unresolved cause

BLOCKS
    relationship from cause to affected work

BLOCKED
    resulting condition on affected work

FAIL
    failed current execution attempt
```

The integrated project map contains a `BLOCKS` relation and a BLOCKED investigation rather than treating blocked as a free-floating red state with no cause concept.

### 4.10 Attention priority

Held:

```text
A3 Signal Bars
    three ascending micro-bars
    structural upper-right signal
```

Exact accepted target:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

The Model selection work unit uses A3.

### 4.11 Persistent selection

Held:

```text
SEL2 Corner Brackets
    four compact neutral-cool brackets
    outside the rendered work-unit frame
```

Exact accepted target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

The integrated browser uses four outside brackets and does not repeat the historical two-corner fixture defect.

### 4.12 X5 contextual expansion

Held:

```text
X5 balanced two-axis expansion
    approximately 390 x 210
    one integrated expanded work-unit object
    expands width + height
    surrounding project world remains normal salience
    no X5-specific context recession
```

Exact accepted target:

```text
94bc1100b7388cc56497cafc03051ce326424a80
```

The integration uses X5 with the L0 working internal layout.

### 4.13 Expanded internal layout

Held only as working default:

```text
L0 Flat Fields
    provisional
    sufficient to continue
    not final semantic schema
```

The integrated X5 therefore shows Purpose, Constraint, Evidence and Next Action without promoting those fields as the final work-unit persistence schema.

### 4.14 Specialist Deep Dive

Held ladder:

```text
compact work unit
    -> SEL2
    -> X5
    -> Z7 Pull-Back Then Dive
    -> fullscreen specialist workspace
```

Held end state:

```text
specialist workspace owns active Cockpit stage
project grid absent
surrounding project boxes absent
compact topology compass retained
```

Exact selected target:

```text
04616a52df5cceff6c59223bbd6f07448d027510
```

The integrated browser reconstructs the Z7 spatial feeling and a full-stage specialist workspace with a clean compact compass.

Specialist internals remain schematic and must not be promoted from this fixture.

### 4.15 Semantic zoom

Held current behavior:

```text
S0 Geometric Control
    provisional working default

S1-S8
    preserved for later
    not rejected
```

The integrated map changes geometry with zoom but does not change information content by zoom level.

### 4.16 Conversation Workspace visual baseline

Held:

```text
Quiet Graphite
    current baseline
```

Previously rendered alternatives remain rejected as currently rendered systems. New palette exploration may happen later only through genuinely new candidates.

The integrated full Conversation Workspace uses Quiet Graphite.

### 4.17 Conversation scope and navigation

Held:

```text
PROJECT-GENERAL CONVERSATION
    belongs to project broadly
    no work-unit home

WORK-UNIT-SCOPED CONVERSATION
    belongs to one work unit

PER-TURN CONTEXT
    separate from conversation home
```

Held conversation rail:

```text
Boxes / Text
    user-switchable

Boxes
    same canonical WorkUnit identity grammar
    scaled for navigation
```

The integrated browser persists the Boxes/Text preference locally.

### 4.18 A6 Conversation Workspace work-unit context

Held:

```text
A6 Adaptive Anchor

resting conversation identity
    active canonical box in sidebar
    title + WORK UNIT scope in header
    Expand box action
    no redundant floating mini-box in transcript
```

Exact floating-box removal:

```text
606e027f281b35c2dfc93d059a1681df23bc2b73
```

The integrated browser follows this directly.

### 4.19 Conversation access is orthogonal to work depth

Checkpoint 248 clarification remains the governing interaction model:

```text
WORK CONTEXT
    Grid neutral
    Grid selected
    Grid X5
    Specialist Deep Dive

x

CONVERSATION PRESENTATION
    compact composer
    full-focus Conversation Workspace
    co-present Conversation Workspace

x

CONVERSATION SCOPE
    project-general
    work-unit scoped
```

The integrated browser demonstrates:

```text
Global Conversations from Grid
Chat from selected work unit
Open conversation from X5
Global Conversations from Deep Dive
Chat about this work unit from Deep Dive
full-focus chat
co-present chat
return to preserved source work state
```

The exact co-present layout/proportion remains provisional.

## 5. New holistic shell choices that are intentionally provisional

The project owner explicitly noted that several whole-Cockpit questions had not yet been designed because earlier work concentrated on isolated components.

The integrated browser therefore requires initial concrete answers so that the product can be reviewed as a whole, but they are NOT frozen by this integration.

Current provisional shell values include:

```text
Cockpit HUD height
    54px

finite world fixture
    2400 x 1500

semantic project plane fixture
    2200 x 1320

initial viewport position
    representative centered work region

map tools
    compact right-side vertical rail

compact composer
    bottom-center floating Cockpit surface

header composition
    project identity
    current surface breadcrumb
    project synchronization status
    Focus current
    Jump
    Conversations
    appearance settings
    fullscreen

specialist internal modules
    schematic only

co-present conversation mode
    provisional 46% right-side stage share
    rail collapses in co-present mode for usable transcript width
```

These are now visible precisely so later iteration can happen against a real whole product instead of abstract speculation.

## 6. State-preservation behavior in the baseline

The integrated prototype keeps source work state when conversation opens.

Conceptually:

```text
Grid selected / X5 expanded
    -> Full Conversation
    -> return
    -> Grid selection / X5 remain

Deep Dive
    -> Full Conversation
    -> return
    -> Deep Dive restored

Grid or Deep Dive
    -> Co-present Conversation
    -> close
    -> same underlying work surface remains
```

This is a product-level requirement. The exact persistence/URL/session implementation remains unfrozen.

## 7. Interaction controls available in the integrated browser

The first holistic fixture supports:

```text
select a work unit
expand to X5
collapse X5
enter Deep Dive
return to project
open project-general conversation globally
open work-unit conversation from selected/X5/Deep Dive
switch Boxes/Text conversation navigation
expand A6 work-unit context in full chat
switch full-focus/co-present conversation
return to preserved work state
zoom in/out/reset/fit
native Ctrl-wheel geometric zoom candidate
Focus current / Context visible
Jump/search work units
appearance controls
fullscreen with standards-based API fallback
keyboard Escape recovery
```

This is intentionally broader than the earlier bounded browsers because the purpose has changed from isolated mechanism selection to holistic integration review.

## 8. What the human should review now

Do not start by asking which new micro-component to invent.

Review the integrated product for:

```text
Does it finally feel like one Cockpit?

Are the accepted mechanisms mutually coherent?

Is the Grid/world proportion right?

Does the HUD consume the right amount of space?

Are the map tools and composer placed well?

Does selection -> X5 -> Deep Dive feel like one hierarchy?

Can conversation be reached naturally from every relevant work state?

Does full chat feel connected to the same project rather than another app?

Does co-present chat feel plausible when working in Deep Dive?

Which shell-level details now look wrong only because we can finally see everything together?
```

The next design work should emerge from that holistic review.

## 9. Process disposition

```text
isolated component exploration
    PAUSED as the default workflow

accepted historical browser evidence
    PRESERVED

holistic integrated Cockpit
    CURRENT PRIMARY REVIEW SURFACE

new isolated experiment
    only when the integrated Cockpit exposes a question that genuinely benefits from factorized comparison
```

This does not forbid future bounded experiments. It changes their role: the integrated Cockpit becomes the product baseline and bounded browsers become supporting experiments when needed.

## 10. Production boundary

Production `/cockpit` remains untouched.

The integrated browser is still a design-lab artifact. Production integration should happen only after the holistic baseline is sufficiently coherent and an explicit production-integration audit is performed.
