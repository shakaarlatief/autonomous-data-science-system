# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-29  
**Current checkpoint:** 258  
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
checkpoint                258
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
current boundary          Adaptive Conversation Dock whole-product human review
```

---

# Current whole-product browser

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Accepted current substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Current opt-in review candidate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Route roles:

```text
plain route
    accepted Checkpoint 256 / 257 continuation substrate
    adaptive Conversation study absent

?conversation=adaptive-dock
    current professional co-present Conversation candidate
    human review open

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Checkpoint 258 boundary

The project owner accepted the previous Conversation spacing and current flat-rail control-set corrections for continuation.

Accepted continuation values/state:

```text
Conversation list gap                         16px
Conversation WorkUnit row padding             6px top + bottom
Fullscreen current flat rail                  present
Expand selected WorkUnit current flat rail    absent
Hide project HUD current flat rail            absent
current-process Focus                          unchanged / working
live Deep Dive topology compass               carried forward
```

The newly opened question is only the professional composition of the already-held Conversation Workspace with active Cockpit work.

---

# Adaptive Conversation Dock study

Research 097 diagnoses the previous co-present failure as a hierarchy problem:

```text
wide Conversation surface
    + permanently visible Conversation thread rail
    + long-form transcript
    -> visually resembles a second full application beside the Cockpit
```

The current review candidate retains the source-faithful full-focus Workspace but changes co-present presentation to:

```text
compact right secondary dock
resizable left edge
Cockpit retains majority of visible width
Threads invokes the same Boxes/Text rail as a drawer
A6 becomes invoked inspector sheet in compact co-presence
project-aware composer retained
```

Current implementation:

```text
frontend/design-lab/cockpit-conversation-integration-study.css
frontend/design-lab/cockpit-conversation-integration-study.js
frontend/design-lab/cockpit-spatial-rail-study-gen2-anchor.js
frontend/e2e/cockpit-reintegration-conversation-integration-study.spec.ts
```

The ordinary route intentionally remains unchanged until human acceptance.

---

# Current deterministic evidence

Implementation target:

```text
00957b684cbc57dad11561f7ed262faf1bba4383
```

Complete Cockpit fidelity workflow:

```text
workflow run  33238181528
job           99062775945
result        SUCCESS
browser tests 71 / 71 passing
```

The three new tests cover adaptive-study isolation, compact-dock/thread-drawer behavior and source-state-safe resize/full-focus restoration. All previous 68 source-faithful Cockpit tests remain green.

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
    PASS, 71/71 at current implementation target

HUMAN PRODUCT-DESIGN GATE
    OPEN at Checkpoint 258 for Adaptive Conversation Dock
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

Checkpoint 258 does not reopen those decisions. Research 086 remains the key semantic architecture for Conversation/work-context orthogonality.

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

remains:

```text
FAILED INTEGRATION ATTEMPT
NOT an accepted baseline
NOT a production target
NOT a visual source of truth
PRESERVED only as diagnostic evidence
```

Research 088 is the source-level diagnosis. The implementation manifest is the exact source-reuse contract.

---

# Historical whole-product studies

```text
Research 092
    direct-manipulation spatial rail studies

Research 093
    architectural 3D edge studies

Research 094
    resting angled rail, rejected for current rail direction

Research 095
    flat rail + initial Conversation spacing + live compass

Research 096
    structural Conversation spacing + current flat rail control set

Research 097
    current Adaptive Conversation Dock co-presence candidate
```

Do not revive historical alternatives as current product behavior without explicit new evidence and human direction.

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
Review the Adaptive Conversation Dock on the opt-in route.

If professionally coherent:
    preserve acceptance and tune only identified details
    consider making it the default co-present presentation

If not:
    challenge the adaptive-dock composition family
    preserve the accepted Conversation semantic architecture
    leave the normal no-query Cockpit unchanged
```
