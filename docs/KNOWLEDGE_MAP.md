# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-28  
**Current checkpoint:** 250  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/250_integrated_cockpit_fidelity_failure_recovery_audit_opened.md
docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
```

Current route:

```text
checkpoint                250
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
current boundary          integrated Cockpit fidelity recovery audit
```

---

# Critical recovery finding

The holistic browser frozen at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

failed fidelity review and is **not an accepted Cockpit baseline**.

Research 088 found that the repository still preserves exact target SHAs and executable accepted artifacts, but the failed integration manually reimplemented the design from semantic summaries.

Observed divergences include:

```text
canonical WorkUnit geometry/surface grammar
H4 layered rest/hover lighting
G4 ambient current/glint behavior
Quiet Graphite palette/typography implementation
```

Failed integration evidence remains preserved at:

```text
docs/checkpoints/249_holistic_integrated_cockpit_baseline_review_opened.md
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
frontend/design-lab/cockpit-integrated-baseline.html
```

Do not use that browser as a visual source of truth.

---

# Accepted implementation provenance that must be recovered exactly

Current exact targets include:

```text
directionality                07d573b6569b9f09a3b7e00936f3eadecee721b3
relation class E5             497e81f06ba1f9901511449237d1bb9f96b2d108
P7 disposition                fac1db37af4225927d6c799e37418a3ad9c42c13
editable current focus        da115b74de526fca05ed6f468bef39bdb801355c
T7 Soft Shade                 08534f94c2f272f969159087de2797a23e36b330
switchable runtime            fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
BLOCKED/status carrier        88fd3c3cfe7a1eff4664afde06341b7b654c97f4
A3 attention priority         767c66f76974d3c0a851de0dfa17c502817a4b12
SEL2 persistent selection     e7304fe834d86166d843fda7e1df0f4ddb1f793a
X5 contextual expansion       94bc1100b7388cc56497cafc03051ce326424a80
Z7 specialist deep focus      04616a52df5cceff6c59223bbd6f07448d027510
semantic zoom browser         65ac02326a75b1c9f056676819d2d1b7b23b74c5
Quiet Graphite source         c66f72a74e681f89fd52ba591a1387ea50f0e959
A6 no-floating-box refinement 606e027f281b35c2dfc93d059a1681df23bc2b73
```

These targets are not merely historical references. The recovery task must bind them to exact source files and allowed integration adaptations before any new holistic build.

---

# Held Phase-C semantics / product direction

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
Dot + ring / T7 Soft Shade carrier switch
BLOCKER -> BLOCKS -> BLOCKED
BLOCKED sharper ring / FAIL smoother ring
A3 Signal Bars
SEL2 four outside corner brackets
X5 balanced two-axis expansion
L0 provisional Flat Fields
Z7 Pull-Back Then Dive
full-stage specialist workspace
compact topology compass
S0 Geometric Control
Quiet Graphite Conversation Workspace
project-general + work-unit conversations
Boxes / Text conversation rail
A6 work-unit context expansion
no redundant A6 floating work-unit box
conversation access from Grid + Deep Dive
full-focus + co-present Conversation capability
source work-state preservation
compact native Cockpit composer
```

None of these are revoked by the failed integration.

---

# Recovery protocol

Before another integrated Cockpit:

```text
accepted implementation manifest
    semantic decision
    exact target SHA
    exact HTML/CSS/JS source files
    invariant visual/behavioral properties
    allowed integration adaptations
    known fixture caveats
    fidelity verification method

then

holistic rebuild
    reuse/port exact accepted implementations
    invent only genuinely unresolved shell glue
    label that glue provisional

then

fidelity gate
    compare integrated result against exact accepted targets
```

Only after this gate should holistic human product review resume.

---

# Key historical evidence routes

Work-unit/world grammar:

```text
frontend/design-lab/work-unit-grammar.*
frontend/design-lab/work-unit-selection-state.*
```

Deep focus:

```text
docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
docs/research/077_fullscreen_specialist_workspace_and_spatial_zoom_transition_experiment.md
frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
```

Conversation:

```text
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
frontend/design-lab/conversation-workspace-chatgpt-independent.html
frontend/design-lab/conversation-workspace-work-unit-anchor.html
```

Promoted architecture:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

No Claude obligation is currently pending. Human review of the failure diagnosis is the current gate.

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
