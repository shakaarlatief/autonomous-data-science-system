# Current State

**Checkpoint:** 259  
**Date:** 2026-08-29  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-09
Conversation title       09 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
Collaboration thread     MC-0004
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

```text
docs/checkpoints/259_cockpit_presentation_state_integrity_recovery.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md
```

The project owner paused Checkpoint 258 Adaptive Conversation Dock review after reporting two intermittent failures in already-held surfaces:

```text
Conversation Boxes rail
    accepted visible WorkUnit spacing sometimes disappeared

current-process Focus
    sometimes context WorkUnits did not recess correctly
    sometimes relation lines recessed while WorkUnit boxes did not
```

Both failure families have now been investigated, repaired and deterministically verified. The immediate gate is human confirmation that the intermittent behavior no longer reproduces under normal use. After that confirmation, return directly to the Adaptive Conversation Dock visual review.

Production `/cockpit` remains untouched.

---

# Whole-product browser and routes

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Normal current substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Adaptive Conversation Dock candidate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Route roles remain:

```text
plain route
    current source-faithful whole-product substrate

?conversation=adaptive-dock
    opt-in professional co-present Conversation candidate
    product-design review resumes after stability confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Presentation-state integrity recovery

## Conversation Boxes spacing

Accepted values remain unchanged:

```text
list row-gap                16px
WorkUnit structural padding 6px top + bottom
canonical WorkUnit footprint unchanged
```

Root cause:

```text
current Conversation renderer
    data-thread-scope="work"

Checkpoint 256 structural selector
    .is-workunit-thread
```

The historical class is not emitted by the current renderer. The 16px list gap could still make some deterministic geometry checks pass, while the intended structural row padding was not bound to the current DOM.

The correction is now owned by a statically loaded cross-surface integrity layer:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
```

It uses the current data attribute as the primary selector and retains `.is-workunit-thread` only as a historical compatibility fallback. The Checkpoint 256 stylesheet was corrected to match the same current identity.

This also removes unnecessary dependence on a late-mounted rail-study stylesheet for an already-accepted Conversation layout guarantee.

## Current-process Focus

M09 semantics and the accepted q/i/v example membership remain unchanged.

Root cause was lifecycle asymmetry:

```text
WorkUnit data-process-scope
    assigned only during initial setup

relation is-context-edge / is-current-edge
    continuously resynchronized through a MutationObserver
```

If a WorkUnit DOM carrier was replaced while project semantics remained the same, relation recession could be repaired while node recession was not. That matches the human-reported state in which lines faded but boxes did not.

Recovery:

```text
one authoritative focusMembership set
node scope reapplied from that set
WorkUnit remount/replacement observer
membership controls restored on replacement carriers
relations resynchronized after node repair
Focus stylesheet statically loaded
accepted opacity/filter contract protected from later study-style precedence
```

Accepted presentation values remain:

```text
focused context WorkUnit opacity  0.27
focused current WorkUnit opacity  1.00
context-edge opacity              0.16
current-edge opacity              1.00
```

Accepted hover and edit-mode lift behavior remains intact.

---

# Deterministic fidelity status

Implementation target:

```text
0374d624ec0e88d65060fb2424ce18291ca40792
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33240152004
job           99067985262
result        SUCCESS
browser tests 73 / 73 passing
```

The previous 71 tests all remain green. Two new lifecycle tests verify:

```text
Conversation spacing on ?conversation=adaptive-dock&focus=work&work=i&depth=x5
full-focus spacing
Boxes -> Text -> Boxes switching
co-present Threads-drawer spacing
return to full-focus spacing
static Focus stylesheet readiness
repeated process-focus switching
node/relation recession agreement
WorkUnit DOM replacement and automatic focus-membership repair
```

A green gate does not substitute for the human confirmation requested here because the original failures were intermittent and discovered through normal use.

---

# Adaptive Conversation Dock remains open, not promoted

Checkpoint 258 and Research 097 remain the current product-design evidence for Conversation/Cockpit co-presence.

The candidate still tests:

```text
full-focus
    source-faithful Quiet Graphite Workspace
    persistent Boxes/Text rail

co-present
    compact resizable right-side secondary dock
    Cockpit remains majority visible
    Threads invokes the same Boxes/Text rail as a drawer
    A6 available as invoked inspector sheet
```

Checkpoint 259 does not accept, reject or retune this candidate. It repairs the substrate on which that human review depends.

---

# Held Conversation semantics remain intact

```text
Quiet Graphite baseline
project-general + WorkUnit-scoped conversation
Boxes / Text user-switchable thread navigation
A6 Adaptive Anchor
no redundant A6 floating home card
Conversation access from Grid neutral / selected / X5 / Deep Dive
full-focus + co-present capability
source work-state preservation
Conversation ownership separate from SEL2 selection
compact native Cockpit composer
```

---

# Other held Phase-C decisions remain intact

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation-class carrier
D0-D3 semantic directionality
single active connector terminal treatment
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
one switchable operational carrier
T7 Soft Shade runtime tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 four outside corner brackets
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working internal-layout default
Z7 Pull-Back Then Dive specialist-workspace entry
full-stage specialist workspace
compact topology compass retained
S0 Geometric Control provisional zoom working default
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

L0 remains provisional. Semantic zoom remains deferred.

Implementation provenance remains governed by:

```text
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only.

---

# Deferred / paused work remains unchanged

```text
semantic zoom
    DEFERRED
    S0 geometric control remains the provisional working default

source-vault bootstrap
    PAUSED
    not cancelled or rejected

Course 2 source-universe gate
    unchanged
```

---

# Exact next step

```text
Human pulls the latest v1-cockpit-design-exploration branch.

First confirm stability:
    repeatedly exercise Current process focus on the normal route
    repeatedly open Conversation Boxes mode
    switch Boxes / Text
    switch full-focus / co-present on the adaptive route
    confirm spacing no longer collapses
    confirm WorkUnit boxes and relation lines remain synchronized under Focus

If stable:
    close the Checkpoint 259 confirmation gate
    resume Checkpoint 258 Adaptive Conversation Dock visual review immediately

If either failure reproduces:
    capture the exact sequence and visible state
    keep Adaptive Dock product judgment paused
    reopen presentation-integrity debugging only
```
