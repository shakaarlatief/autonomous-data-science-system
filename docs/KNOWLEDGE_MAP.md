# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-29  
**Current checkpoint:** 259  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/259_cockpit_presentation_state_integrity_recovery.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md

docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md

docs/checkpoints/257_canonical_cockpit_review_route_normalized.md
docs/checkpoints/256_structural_conversation_spacing_and_project_tool_rail_controls_review_opened.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md

docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
docs/research/085_conversation_workspace_a6_refinement_and_entry_transition.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
docs/research/079_conversation_workspace_presentation_architecture_experiment.md

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

Current route:

```text
checkpoint                259
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
current boundary          presentation-state integrity human confirmation, then Adaptive Conversation Dock review
```

---

# Current whole-product browser

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

Route roles:

```text
plain route
    current source-faithful whole-product substrate

?conversation=adaptive-dock
    current professional co-present Conversation candidate
    review resumes after Checkpoint 259 stability confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Checkpoint 259 presentation-integrity recovery

Human review found two intermittent failures in already-held surfaces before Adaptive Dock judgment continued.

## Conversation Boxes

Accepted values remain:

```text
16px list row gap
6px top/bottom structural WorkUnit-row padding
```

Research 098 identified selector drift:

```text
current renderer           data-thread-scope="work"
stale structural selector  .is-workunit-thread
```

and an avoidable dependency on a late-mounted rail-study stylesheet.

Current recovery artifacts:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
frontend/design-lab/cockpit-reintegration.html
```

The accepted spacing guarantee is now statically present and targets the actual current WorkUnit-row identity. Historical `.is-workunit-thread` remains only as a compatibility fallback.

## Current-process Focus

Research 098 identified lifecycle asymmetry:

```text
node membership      initialized once
relation recession   continuously resynchronized
```

Current recovery artifacts:

```text
frontend/design-lab/cockpit-reintegration-process-focus.js
frontend/design-lab/cockpit-reintegration-process-focus.css
frontend/design-lab/cockpit-reintegration.html
```

Focus now owns membership independently of DOM instances, repairs replacement WorkUnit carriers, restores membership controls, resynchronizes relation classes, statically loads Focus styling and protects the accepted recession contract against later study-style precedence.

M09 semantics are unchanged.

---

# Current deterministic evidence

Implementation target:

```text
0374d624ec0e88d65060fb2424ce18291ca40792
```

Complete Cockpit fidelity workflow:

```text
workflow run  33240152004
job           99067985262
result        SUCCESS
browser tests 73 / 73 passing
```

New regression surface:

```text
frontend/e2e/cockpit-reintegration-presentation-integrity.spec.ts
```

It verifies:

```text
Adaptive full-focus / co-present / Threads-drawer Conversation spacing
Boxes -> Text -> Boxes spacing stability
static Focus stylesheet readiness
repeated process-focus switching
node/relation recession synchronization
WorkUnit carrier replacement and automatic focus-membership recovery
```

All previous 71 tests remain green.

---

# Adaptive Conversation Dock study remains open

Research 097 diagnoses the old co-present composition as a hierarchy problem:

```text
wide Conversation surface
    + permanently visible Conversation thread rail
    + long-form transcript
    -> resembles a second full application beside the Cockpit
```

The opt-in candidate remains:

```text
full focus
    source-faithful Quiet Graphite Workspace
    persistent Boxes/Text rail

co-present
    compact right secondary dock
    resizable left edge
    Cockpit retains majority visible width
    Threads invokes the same Boxes/Text rail as a drawer
    A6 becomes an invoked inspector sheet
```

Checkpoint 259 neither accepts nor rejects that product-design direction. It repairs the substrate required to judge it reliably.

---

# Source-of-truth architecture

Use these layers together:

```text
SEMANTIC / PRODUCT AUTHORITY
    accepted specifications
    foundations
    explicit human-reviewed selections

DESIGN DISPOSITION
    docs/cockpit/PHASE_C_DECISION_LEDGER.md
    exhaustive for its declared Research 037-088 scope

POST-RECOVERY WHOLE-PRODUCT EVIDENCE
    Research 089 onward
    recent checkpoints

IMPLEMENTATION PROVENANCE
    docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    docs/cockpit/accepted_implementation_manifest.json

CURRENT ROUTING
    docs/CURRENT_STATE.md
    docs/KNOWLEDGE_MAP.md
    docs/current_routing.json
    latest checkpoint + research record
```

A future integrator must never infer accepted implementation details from shorthand labels alone.

---

# Provenance and fidelity gates

Implementation-provenance recovery remains complete:

```text
manifest entries   23
required           19
non-promotable      4
first history gate 33156357834 PASS
```

Current gate model:

```text
PROVENANCE GATE
    PASS

DETERMINISTIC INTEGRATION GATE
    PASS, 73/73 at current implementation target

HUMAN STABILITY CONFIRMATION
    OPEN at Checkpoint 259

HUMAN PRODUCT-DESIGN GATE
    Adaptive Conversation Dock review resumes immediately after stability confirmation
```

---

# Held Conversation architecture

```text
Quiet Graphite baseline
project-general + WorkUnit-scoped conversations
Boxes / Text thread navigation
A6 Adaptive Anchor
no redundant floating A6 WorkUnit box
Conversation access from Grid neutral / selected / X5 / Deep Dive
full-focus + co-present presentation capability
source work-state preservation
Conversation ownership independent from SEL2 selection
compact native Cockpit composer
```

Checkpoint 259 changes none of those decisions.

---

# Other held Phase-C product direction

```text
G4 Adaptive Hybrid world
H4 hover/outward response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation-class carrier
D0-D3 directionality
single terminal-treatment appearance choice
P7 Neutral Tag + Tone disposition
current-process focus lens
conditional runtime semantics
R1 / T7 switchable operational carrier family
BLOCKER -> BLOCKS -> BLOCKED
BLOCKED sharper ring / FAIL smoother ring
A3 Signal Bars
SEL2 four outside corner brackets
X5 balanced two-axis expansion
L0 provisional Flat Fields
Z7 Pull-Back Then Dive
full-stage specialist workspace
compact topology compass
S0 Geometric Control provisional working default
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

Semantic zoom remains deferred. L0 remains provisional.

---

# Failed holistic integration remains excluded

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

remains diagnostic evidence only, not an accepted baseline, production target or visual source of truth.

---

# Historical whole-product studies

```text
Research 092  direct-manipulation spatial rail studies
Research 093  architectural 3D edge studies
Research 094  resting angled rail, rejected for current rail direction
Research 095  flat rail + initial Conversation spacing + live compass
Research 096  structural Conversation spacing + current flat rail control set
Research 097  Adaptive Conversation Dock co-presence candidate
Research 098  intermittent Conversation spacing + Focus integrity recovery
```

---

# Source Universe route

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
Course 2 gate unchanged
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

No Claude obligation is pending. The next expected actor is the human reviewer.

---

# Exact next step

```text
Pull the latest branch and try to reproduce the two intermittent failures.

If Conversation spacing and Focus remain stable:
    close Checkpoint 259 human confirmation
    resume Adaptive Conversation Dock review

If either still fails:
    preserve the exact reproduction sequence
    keep product-design review paused
    reopen only presentation-integrity debugging
```
