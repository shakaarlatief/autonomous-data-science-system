# MC-0004: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Status:** ACTIVE / PHASE C SOURCE-FAITHFUL HOLISTIC REINTEGRATION  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Task owner:** ChatGPT  
**Target-state write owner:** ChatGPT  
**Claude role:** independent reviewer / counter-designer / researcher  
**Human project owner:** final arbiter of product-intent choices  
**Opened:** 2026-08-26  
**Current ChatGPT interaction session:** `chatgpt-09`  
**Current ChatGPT conversation title:** `09 - Project Cockpit Design Exploration`

## Collaboration history

```text
Phase A
    Claude independent proposal
    cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    BLIND_TO_CANDIDATE

Phase B
    Claude comparative review
    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    COMPARATIVE_ONLY

Phase C divergent work-unit ideation
    ChatGPT Message 003
    Claude Message 004

Phase C divergent deep-focus ideation
    ChatGPT Message 005
    Claude Message 006
    204664ae1e732dd504174bbc62545e9a93adc85f

Phase C Conversation Workspace independent dual design
    ChatGPT Message 007 blind request
    frozen base c190420c6d77d3191ca9efb9ffc1e401bbb7fda8
    ChatGPT isolated browser frozen at c66f72a74e681f89fd52ba591a1387ea50f0e959
    Claude Message 008 completed at cab2e464d81b48edadd1b6ae51bb7dd620d7e892
    blind gate COMPLETE

Phase C Conversation Scope + Work-Unit Anchor
    Quiet Graphite selected current baseline
    Checkpoint 246
    Research 082
    ChatGPT Message 009
    Research 083
    ChatGPT Message 009A human refinement addendum
    Claude Message 010 completed at 8c2c95aec8bf9d53e17500f4a38f9311d19a1e8b
    Research 084 synthesis browser opened
    project owner reaffirmed prior design and rejected B1-B4 as irrelevant to chosen look
    redundant A6 floating work-unit card removed

Phase C Conversation Workspace entry / return transition
    Checkpoint 247
    Research 085
    transition browser target 43ee0ae0ffc63eba6e99a42e9157568c53cc8806
    no transition selected
    later determined too narrow as a primary architecture frame

Phase C Conversation access + coexistence
    Checkpoint 248
    Research 086
    factorized access/coexistence browser target db31970d6885ce785609f9c3300f22123130d821

Phase C holistic integrated Cockpit attempt
    Checkpoint 249
    Research 087
    integrated frontend target 8e554d847bb3b6318db432abcb5dff742f0fa523
    FAILED FIDELITY REVIEW

Phase C implementation-provenance recovery
    Research 088
    Checkpoint 250
    source-level failure diagnosis
    project owner review completed in chatgpt-09
    exhaustive decision/source recovery explicitly authorized

Phase C provenance recovery completion
    Phase-C Decision Ledger frozen
    23-entry accepted implementation manifest frozen
    deterministic validator added
    full-history CI gate added
    workflow run 33156357834 PASS
    exact historical source verification PASS
    Research 089
    Checkpoint 251
    source-faithful holistic reintegration opened
```

## Failed holistic integration disposition

The browser frozen at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is classified as:

```text
FAILED INTEGRATION ATTEMPT
NOT an accepted Cockpit baseline
NOT a production target
NOT a basis for new visual decisions
EXCLUDED from the replacement implementation source graph
PRESERVED only as diagnostic evidence
```

The failure mode is established at source level:

```text
accepted browser-rendered implementation existed
    -> semantic summary was read
    -> a new visually similar implementation was manually authored
    -> implementation fidelity was not mechanically or visually gated
```

That process is prohibited for the replacement integration.

## Preserved accepted / working Phase-C results

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific marker category grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation class
D0-D3 directionality
single active connector terminal treatment
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
one switchable runtime carrier
T7 Soft Shade runtime tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for elevated attention
SEL2 four outside corner brackets
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working default
Z7 Pull-Back Then Dive specialist-workspace entry
full-stage specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite current Conversation Workspace visual baseline
project-general + work-unit-scoped conversation distinction
A6 Adaptive Anchor work-unit context expansion
canonical WorkUnit box / Text user-switchable conversation rail
A6 resting state without redundant floating home-object card
conversation available from Grid and Deep Dive
full-focus + co-present conversation capability
source work-state preservation across conversation open/close
compact native Cockpit composer
Specification 008 Jump/search, map recovery and fullscreen capability
```

Important status distinctions remain binding:

```text
L0 Flat Fields
    PROVISIONAL WORKING DEFAULT
    not a final accepted internal-layout design

S0 Geometric Control
    PROVISIONAL WORKING DEFAULT
    semantic zoom remains deferred

S1-S8 semantic zoom candidates
    DEFERRED / PRESERVED
    not rejected

Research 085 E0-E4 Conversation transition candidates
    EVIDENCE ONLY
    no winner selected

Research 084 B1-B4 Conversation synthesis candidates
    HISTORICAL / NOT ADOPTED
    must not replace the selected Quiet Graphite + A6 direction
```

## Completed recovery contract

The repository now contains the durable recovery substrate required before another holistic integration:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
    exhaustive Research 037-088 disposition ledger

docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    human-readable exact source/invariant/adaptation contract

docs/cockpit/accepted_implementation_manifest.json
    machine-readable 23-entry manifest

scripts/check_cockpit_implementation_manifest.py
    deterministic structural + exact-history validator

.github/workflows/cockpit-implementation-provenance.yml
    full-history CI gate
```

For every mechanism that belongs in the integrated product, the manifest binds:

```text
semantic decision
status / maturity
origin evidence
exact implementation target SHA
exact source file(s)
visual / behavioral invariants
allowed integration adaptations
known fixture caveats
fidelity verification method
```

The manifest also records decisions that intentionally do **not** authorize implementation, including provisional defaults, unselected candidates and the failed integrated browser.

## Provenance gate result

First full-history run:

```text
workflow run 33156357834
commit 2127563c0ed980f7bf6fad36e36b11e76500c59b

Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

The implementation-provenance recovery is therefore closed.

This does not mean the replacement integrated browser has passed visual/interaction fidelity. That is the next gate.

## Integration rule after recovery

```text
accepted implementation exists
    -> reuse or port that exact implementation
    -> preserve its verified geometry, behavior and visual grammar
    -> adapt only inside the explicitly recorded integration boundary

accepted interaction exists
    -> reuse or port the exact behavior
    -> do not substitute a similar animation or approximate visual treatment

provisional working default exists
    -> carry it only as provisional
    -> do not promote it through integration by accident

deferred / rejected / evidence-only candidate exists
    -> preserve its history
    -> do not implement it as accepted product behavior

whole-product answer genuinely does not exist
    -> introduce the minimum integration glue
    -> label it provisional
    -> keep it visually subordinate to held source implementations
```

## Conversation Workspace visual disposition

The independent dual-design round is complete and preserved in Research 081.

The project owner selected:

```text
Quiet Graphite
    current baseline
```

Currently rendered alternatives remain rejected:

```text
Deep Navy
Warm Slate
Monochrome Signal
Violet Ink
Editorial Dark
Claude Technical Manuscript
Claude Studio Console
Claude Hybrid
```

Future visual exploration may introduce genuinely new candidates. Rejected systems must not be silently revived as active options.

## Conversation Scope + Work-Unit Anchor result

Held product model:

```text
PROJECT-GENERAL CONVERSATION
    legitimate project-level conversation
    no single box owns it

WORK-UNIT-SCOPED CONVERSATION
    belongs to one work unit
    remains immediately recognizable as belonging to that box

PER-TURN CONTEXT
    separate temporary project context
```

Held presentation:

```text
conversation rail
    user-switchable Boxes / Text

Boxes mode
    canonical work-unit visual identity

opened-box composition
    A6 Adaptive Anchor

A6 rest-state identity
    active box in sidebar
    title + WORK UNIT scope in header
    Expand box action
    no extra floating box in transcript
```

Conversation ownership does not imply project-map selection, so SEL2 is not added merely because a chat belongs to a work unit.

Exact A6 floating-box removal:

```text
606e027f281b35c2dfc93d059a1681df23bc2b73
```

## Conversation access / coexistence result

Research 086 established the factorization:

```text
WORK CONTEXT
    Grid neutral
    Grid selected
    Grid X5 expanded
    Deep Dive

x

CONVERSATION PRESENTATION
    compact / work only
    full chat focus
    co-present work + chat

x

CONVERSATION SCOPE
    project-general
    work-unit-scoped
```

Exact factorized browser target:

```text
db31970d6885ce785609f9c3300f22123130d821
```

Conversation open/close must preserve and restore the source work state.

## Current collaboration gate

```text
next actor: ChatGPT
mode: source-faithful holistic reintegration
pending Claude obligation: none
human fidelity-failure diagnosis review: COMPLETE
implementation provenance gate: PASS
integrated fidelity gate: OPEN
holistic human review: WAITING FOR INTEGRATED FIDELITY PASS
```

## Production boundary

Production `/cockpit` remains untouched.

Still unfrozen includes final Cockpit shell geometry, HUD structure, finite-world dimensions, stage taxonomy, map-tool rail treatment, compact-composer geometry, specialist-workspace internal composition, topology-compass semantics/details, Conversation co-present layout and split resizing, full-chat transition choreography, conversation persistence/session model, conversation URL state, historical-state semantics, pinned context, non-work-unit conversation homes, semantic zoom, large-project virtualization and final production frontend component architecture.
