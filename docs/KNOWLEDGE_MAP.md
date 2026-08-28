# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-28  
**Current checkpoint:** 254  
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

docs/checkpoints/254_resting_angled_cockpit_rail_human_review_opened.md
docs/research/094_resting_angled_rail_spatial_identity_and_clarity_only_expansion.md

docs/checkpoints/253_architectural_cockpit_edge_gen2_human_review_opened.md
docs/research/093_architectural_cockpit_edge_instrument_surface_depth_study.md

docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md
docs/research/092_spatial_edge_rail_depth_direct_manipulation_and_docking_study.md

docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
docs/research/091_source_faithful_reintegration_interaction_integrity_gate.md

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

Current route:

```text
checkpoint                254
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
current boundary          resting angled right-side rail human review
```

---

# Current whole-product design route

The source-faithful integrated Cockpit is the active whole-product design substrate.

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Product Surface Study A currently explores provisional shell presentation including:

```text
continuous viewport-owned grid
compact project identity HUD
right-side spatial tool surface
invoked Jump/search
normal Conversation typography
compact full Conversation composer
```

Primary study modules:

```text
frontend/design-lab/cockpit-product-surface-study.css
frontend/design-lab/cockpit-product-surface-study-readability.css
frontend/design-lab/cockpit-product-surface-study.js
```

## Current rail study

The project owner's latest clarification separates spatial identity from readability expansion.

```text
3D / spatial identity
    belongs to the compact rail itself at rest

clarity expansion
    may widen the same rail and reveal labels
    does not create or intensify its 3D identity

direct manipulation
    is not required for the current visual goal
```

Current live route:

```text
Resting Angled Rail
    ?edge=angled
```

Current implementation:

```text
frontend/design-lab/cockpit-spatial-rail-study-angle.css
frontend/design-lab/cockpit-spatial-rail-study-angle.js
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

Current authored study geometry is provisional:

```text
compact width              72px
clarity width              220px
perspective                 1050px
Y orientation               -24deg
X orientation               0.8deg
screen-plane rotation       -0.8deg
front-face Z translation    20px
rear construction offset    +10px x / +7px y / -28px z
```

The important current hypothesis is not those exact numbers. It is that a compact right-edge rail can feel like a physical Cockpit instrument surface through permanent angle, perspective, thickness and attachment.

No drag grip, slider role or intermediate deployment states exist in the current candidate.

Latest complete deterministic browser evidence:

```text
implementation target  67c3105ff26601a2f259e44007b23ce638b23838
workflow run           33202773778
job                    98956116141
result                 SUCCESS
browser tests          64 / 64 passing
```

The four newest checks prove that:

```text
compact resting rail already has perspective and rear depth
no drag grip or slider exists
clarity expansion leaves the rail transform and project state unchanged
real controls remain functional
Conversation and Deep Dive retain stage ownership
```

No rail visual treatment is selected yet.

## Historical rail studies

Research 092 and Research 093 remain preserved as design history and interaction evidence:

```text
Research 092
    A · Extruded Blade
    B · Layered Deck
    C · Dock and Float

Research 093
    A · Hinged Instrument Panel
    B · Telescoping Layer Stack
    C · Spatial Command Console
```

These drag/deployment variants are now **historical / inactive for the current rail design axis**. Human review does not need to compare them before proceeding with the resting-angle question.

Direct manipulation is not globally rejected. It may be revisited later if a separate functional requirement justifies it.

---

# Provenance and integration gate status

Implementation-provenance recovery is complete at the source-binding layer.

Durable provenance gate:

```text
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

First full-history verification:

```text
workflow run  33156357834
commit        2127563c0ed980f7bf6fad36e36b11e76500c59b

Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

Current gate model:

```text
PROVENANCE GATE
    PASS

DETERMINISTIC INTEGRATION GATE
    PASS for current covered implementation

HUMAN PRODUCT-DESIGN GATE
    OPEN
```

A green browser suite protects accepted mechanisms and cross-mechanism behavior. It does not promote provisional whole-product design candidates.

The holistic fidelity workflow watches:

```text
frontend/design-lab/cockpit-reintegration*
frontend/design-lab/cockpit-product-surface-study*
frontend/design-lab/cockpit-spatial-rail-study*
frontend/e2e/cockpit-reintegration*.spec.ts
```

---

# Failed integration remains excluded

The holistic browser frozen at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

failed fidelity review and is **not an accepted Cockpit baseline**.

Research 088 found that the repository preserved exact target SHAs and executable accepted artifacts, but the failed integration manually reimplemented the design from semantic summaries.

Observed divergences included:

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

Do not use that browser as a visual source of truth or as the parent implementation of the replacement browser.

---

# Cockpit source-of-truth architecture

Use three layers together:

```text
SEMANTIC / PRODUCT AUTHORITY
    accepted specifications
    foundations
    explicit human-reviewed research selections

DESIGN DISPOSITION
    docs/cockpit/PHASE_C_DECISION_LEDGER.md
    selected / provisional / deferred / rejected / diagnostic

IMPLEMENTATION PROVENANCE
    docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    docs/cockpit/accepted_implementation_manifest.json
    exact integration SHA + source files + invariants + adaptation boundary
```

A future integrator must not infer implementation details from labels such as G4, H4, SEL2, X5, Quiet Graphite or A6.

---

# Accepted implementation provenance

The complete exact target/source graph is machine-readable in:

```text
docs/cockpit/accepted_implementation_manifest.json
```

High-value navigation targets include:

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
Conversation coexistence      db31970d6885ce785609f9c3300f22123130d821
```

The short list is navigation only. The manifest is authoritative for exact source paths and maturity.

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
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

None of these are revoked by current shell experimentation.

---

# Current integration / design protocol

```text
accepted implementation exists
    reuse or port exact source implementation
    preserve declared invariants
    adapt only inside the manifest boundary

provisional working default exists
    carry only as provisional

candidate is deferred/rejected/evidence-only
    preserve history
    do not select through implementation accident

whole-product presentation is open
    test it on the integrated Cockpit
    preserve each candidate and disposition
    do not promote until explicit human evidence
```

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

No Claude obligation is currently pending. The current next actor is the human reviewer for the single resting angled rail candidate.

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
