# Current State

**Checkpoint:** 250  
**Date:** 2026-08-28  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C integration fidelity recovery. The first holistic Cockpit reconstruction failed human fidelity review because accepted browser-rendered components were reimplemented from textual summaries rather than faithfully reused/ported from their exact source targets. No further visual design or holistic rebuild should proceed until exact implementation provenance is bound to the held decisions.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-08
Conversation title       08 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

```text
docs/checkpoints/250_integrated_cockpit_fidelity_failure_recovery_audit_opened.md
docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
```

Current task:

```text
construct accepted-implementation manifest
bind exact target SHA -> exact source artifacts
record invariant vs allowed adaptation boundary
record known fixture caveats
define fidelity verification gate
only then rebuild holistic Cockpit by reuse/porting
```

Production `/cockpit` remains untouched.

---

# Failed integration disposition

The first holistic browser:

```text
frontend/design-lab/cockpit-integrated-baseline.html
exact target 8e554d847bb3b6318db432abcb5dff742f0fa523
```

is classified as:

```text
FAILED INTEGRATION ATTEMPT
NOT an accepted baseline
NOT a production target
NOT a basis for new visual decisions
PRESERVED as diagnostic evidence
```

Source-level audit found concrete divergence from accepted source artifacts, including WorkUnit geometry, H4 lighting implementation, G4 ambient behavior and Quiet Graphite visual tokens.

---

# Accepted / held Phase-C decisions remain intact

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
full-stage specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite Conversation Workspace baseline
project-general + work-unit-scoped conversation distinction
Boxes/Text user-switchable conversation rail
A6 Adaptive Anchor work-unit context expansion
A6 resting state without redundant floating home-object card
conversation available from Grid and Deep Dive
full-focus + co-present conversation capability
source work-state preservation across conversation open/close
compact native Cockpit composer
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

Important accepted targets:

```text
directionality                07d573b6569b9f09a3b7e00936f3eadecee721b3
relation class E5             497e81f06ba1f9901511449237d1bb9f96b2d108
P7 disposition                fac1db37af4225927d6c799e37418a3ad9c42c13
editable focus                da115b74de526fca05ed6f468bef39bdb801355c
T7 Soft Shade                 08534f94c2f272f969159087de2797a23e36b330
switchable runtime            fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
BLOCKED/status carrier        88fd3c3cfe7a1eff4664afde06341b7b654c97f4
A3 attention priority         767c66f76974d3c0a851de0dfa17c502817a4b12
SEL2 selection                e7304fe834d86166d843fda7e1df0f4ddb1f793a
X5 contextual expansion       94bc1100b7388cc56497cafc03051ce326424a80
Z7 specialist deep focus      04616a52df5cceff6c59223bbd6f07448d027510
semantic zoom browser         65ac02326a75b1c9f056676819d2d1b7b23b74c5
Quiet Graphite source         c66f72a74e681f89fd52ba591a1387ea50f0e959
A6 no-floating-box refinement 606e027f281b35c2dfc93d059a1681df23bc2b73
```

---

# Repository-preservation diagnosis

Current evidence:

```text
semantic decisions              preserved
exact target SHAs               preserved
executable historical artifacts preserved
holistic integration protocol   insufficient
```

The missing safeguard is explicit implementation provenance and fidelity validation. A future integrator must not be able to read labels such as `G4`, `H4`, `SEL2` or `Quiet Graphite` and then recreate them approximately.

Required durable model:

```text
semantic decision
    + exact implementation target
    + exact source files
    + allowed adaptation boundary
    + known fixture caveats
    + fidelity verification
```

---

# Semantic zoom disposition

```text
S0 Geometric Control
    provisional working default

S1-S8
    preserved for later
    not rejected

semantic zoom
    DEFERRED
```

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
```

Course 2 remains gated.
