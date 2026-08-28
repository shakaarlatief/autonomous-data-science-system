# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-28  
**Current checkpoint:** 249  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/249_holistic_integrated_cockpit_baseline_review_opened.md
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
frontend/design-lab/cockpit-integrated-baseline.html
```

Current route:

```text
checkpoint                        249
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  holistic integrated Cockpit baseline review
source-vault deployment           PAUSED, Course 2 gate unchanged
```

---

# Current primary product-review surface

```text
http://localhost:5173/design-lab/cockpit-integrated-baseline.html
```

Exact initial holistic frontend target:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

The current working method is:

```text
Integrated Cockpit
    primary review surface

Bounded design-lab browsers
    supporting evidence
    reopened only when a specific question benefits from factorization
```

---

# Accepted-invariants audit

Primary audit:

```text
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
```

It reconstructs the whole browser from accepted/held decisions rather than copying the latest fixture wholesale.

Held controls represented in the integrated baseline:

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
Jump/search, zoom/recovery and fullscreen
```

Important exact targets:

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
A6 no-floating-box refinement 606e027f281b35c2dfc93d059a1681df23bc2b73
integrated Cockpit baseline   8e554d847bb3b6318db432abcb5dff742f0fa523
```

---

# Current holistic architecture

```text
PROJECT GRID
    neutral
    selected work unit
    X5 expanded work unit

        -> Z7

SPECIALIST DEEP DIVE
    full-stage specialist workspace
    compact topology compass

x

CONVERSATION PRESENTATION
    compact project composer
    full-focus Conversation Workspace
    co-present work + Conversation

x

CONVERSATION SCOPE
    project-general
    work-unit scoped
```

The integrated browser demonstrates global and work-unit conversation access from both Grid and Deep Dive while preserving the underlying work state.

---

# Provisional whole-Cockpit shell

The following are integration glue only, deliberately visible but not frozen:

```text
HUD height                       54px
finite world                     2400 x 1500 fixture
project plane                    2200 x 1320 fixture
HUD composition                  provisional
map-tool rail                    provisional
compact composer geometry        provisional
specialist internal modules      schematic
co-present chat width            46% provisional
co-present thread rail behavior  provisional collapse
```

These should now be judged from the integrated Cockpit rather than through detached speculation.

---

# Specialist deep-focus evidence

```text
docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
docs/research/077_fullscreen_specialist_workspace_and_spatial_zoom_transition_experiment.md
frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
```

Result:

```text
Z7 Pull-Back Then Dive selected
full-stage specialist workspace held
project grid absent during Deep Dive
compact topology compass retained
```

---

# Semantic zoom

```text
docs/research/078_project_world_semantic_zoom_level_of_detail_experiment.md
frontend/design-lab/work-unit-semantic-zoom.html
```

Disposition:

```text
S0 Geometric Control
    provisional working default

S1-S8
    preserved for later
    not rejected
```

---

# Conversation Workspace evidence

Visual baseline:

```text
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
```

Held result:

```text
Quiet Graphite
    current visual baseline
```

Scope and work-unit anchor:

```text
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
frontend/design-lab/conversation-workspace-work-unit-anchor.html
```

Held:

```text
PROJECT-GENERAL CONVERSATION
WORK-UNIT-SCOPED CONVERSATION
PER-TURN CONTEXT separate from home
Boxes / Text user switch
A6 work-unit context expansion
no redundant floating work-unit identity
```

Access/coexistence correction:

```text
docs/checkpoints/248_conversation_access_and_coexistence_architecture_review_opened.md
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
frontend/design-lab/conversation-workspace-access-coexistence.html
```

Research 079's earlier split/dock ideas remain preserved as co-presence evidence rather than discarded whole-product alternatives.

---

# Promoted Cockpit architecture

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Specification 008 remains accepted and is not replaced by the design-lab integration baseline.

---

# Repository preservation / development-method route

```text
docs/checkpoints/README.md
scripts/check_checkpoint_metadata.py
.github/workflows/checkpoint-metadata.yml
scripts/check_current_routing.py
.github/workflows/current-routing-consistency.yml
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/080_explicit_coordination_branch_claude_trigger_hardening.md
```

Current audit result:

```text
architecture                  SOUND
metadata/provenance repair    PRESERVED
checkpoint hygiene            HARDENED
routing validation            HARDENED
Claude branch routing         EXPLICIT
new knowledge subsystem       NOT JUSTIFIED
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

No Claude obligation is currently pending. The human project owner is the next actor reviewing the integrated Cockpit.

---

# Source Universe route

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

Current interpretation:

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```
