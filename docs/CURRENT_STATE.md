# Current State

**Checkpoint:** 260  
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
docs/checkpoints/260_conversation_boxes_row_owned_spacing_human_recheck_opened.md
docs/research/099_conversation_boxes_visible_separation_human_retest_and_row_owned_geometry_recovery.md
```

Checkpoint 259's human confirmation produced a split result:

```text
current-process Focus
    working as far as tested

Conversation Boxes
    still visibly missing the original spacing
```

The project owner's screenshots show the canonical Conversation WorkUnit artifacts still stacking as visually joined objects. That direct visual evidence overrides the previous assumption that a green 73/73 browser gate had closed the Conversation spacing defect.

The active gate is now narrow: verify the new row-owned Conversation spacing locally. Adaptive Conversation Dock product judgment remains paused only until this underlying rail presentation is trustworthy again.

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
    current Boxes spacing human recheck surface

?conversation=adaptive-dock
    opt-in professional co-present Conversation candidate
    Boxes spacing must also remain correct here
    product-design review resumes after Checkpoint 260 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Checkpoint 260 Conversation Boxes recovery

## Human evidence

After pulling the Checkpoint 259 recovery, the project owner reported:

```text
Focus is working as far as tested.
Boxes still do not have the spaces we originally had between them.
```

The screenshots visibly corroborate the Boxes finding.

This means the Conversation branch of Checkpoint 259 failed its human confirmation, while the Focus branch currently passes human retest.

## Correction to the Research 098 Conversation diagnosis

Research 098's stale-selector finding was real but incomplete.

The current renderer emits:

```text
data-thread-scope="work"
```

and some older styles referenced:

```text
.is-workunit-thread
```

but the integrated Phase-C completion adapter also restores `.is-workunit-thread` for canonical WorkUnit rows. Therefore selector identity alone cannot explain the continued visual failure.

The stronger implementation weakness was that accepted visible separation still depended on surrounding layout state:

```text
parent grid row-gap
exact data-conversation-rail="boxes" selector
transformed canonical WorkUnit children
late whole-product style composition
```

The current Conversation UI resolves every non-Text state as Boxes/artifact. Historical persistence also used `artifact`. The user's screenshot does not prove that exact legacy state was active, so Research 099 does not overclaim it as the sole root cause. It is nevertheless a concrete state that the current UI resolves as Boxes and that the previous CSS contract did not explicitly protect.

## Row-owned geometry

The intended visual target remains the Checkpoint 256 spacing. The canonical WorkUnit footprint is unchanged.

Spacing is now owned by actual conversation rows:

```text
parent list row-gap             0px
project-general bottom margin  16px
WorkUnit top padding             6px
WorkUnit bottom padding          6px
WorkUnit bottom margin          16px
last WorkUnit bottom margin      0px
```

The presentation selector is now:

```text
html:not([data-conversation-rail="text"])
```

so both current `boxes` and historical/compatible `artifact` states receive the same structural separation.

Implementation artifacts:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

## Deterministic test correction

The previous tests explicitly expected parent `row-gap` to carry the separation. That encoded the old implementation rather than the user-visible contract.

The updated gates instead assert:

```text
parent row-gap is not the spacing carrier
project row owns >=16px following space
WorkUnit rows own >=16px following space
WorkUnit rows keep >=6px top/bottom structural padding
actual rendered project-to-WorkUnit separation remains visible
actual rendered WorkUnit-to-WorkUnit separation remains visible
```

A new regression uses:

```text
viewport                       1536 x 864
forced legacy rail state       artifact
current Boxes UI               still selected
visible row-owned separation   required
```

---

# Current-process Focus

No Focus code was changed for Checkpoint 260.

Research 098's recovery remains current:

```text
one authoritative focusMembership set
node scope reapplied from that set
WorkUnit remount/replacement observer
membership controls restored on replacement carriers
relations resynchronized after node repair
Focus stylesheet statically loaded
accepted opacity/filter contract protected from later style precedence
```

Current human evidence is positive: Focus is working as far as tested.

Do not reopen Focus without another concrete reproduction.

---

# Deterministic fidelity status

Implementation target:

```text
29419f7a1ccbd3cbcdc98f333e1b594c01d63fb1
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33241369935
job           99071179670
result        SUCCESS
browser tests 74 / 74 passing
```

The 74-test gate includes all previous source-faithful Cockpit coverage plus the new user-like-viewport legacy-artifact spacing regression.

A green gate still does not substitute for the current human recheck because the previous green gate did not prevent the locally visible defect.

---

# Adaptive Conversation Dock remains open, not promoted

Checkpoint 258 and Research 097 remain the product-design evidence for Conversation/Cockpit co-presence.

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

Checkpoint 260 does not accept, reject or retune this candidate. It repairs and revalidates the Boxes rail substrate needed to judge it reliably.

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
Human pulls the latest v1-cockpit-design-exploration branch and hard-refreshes.

Inspect Boxes on:
    normal cockpit-reintegration.html route
    ?conversation=adaptive-dock route

Required visible result:
    project-general artifact separated from first WorkUnit
    every WorkUnit separated from the next WorkUnit
    canonical WorkUnit footprint unchanged
    Focus continues working

If correct:
    close Checkpoint 260
    resume Checkpoint 258 Adaptive Conversation Dock visual review immediately

If still wrong:
    preserve the screenshot and exact route/state
    keep Adaptive Dock product judgment paused
    continue only Conversation rail presentation-integrity debugging
```
