# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-28  
**Current checkpoint:** 248  
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
docs/VISION.md
docs/PRINCIPLES.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

Current route:

```text
checkpoint                        248
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  Conversation access + coexistence architecture review
source-vault deployment           PAUSED, Course 2 gate unchanged
```

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
micro-checkpointing rule      HARDENED
checkpoint validation gate    HARDENED
routing push validation       HARDENED
Claude branch routing         EXPLICIT
new knowledge subsystem       NOT JUSTIFIED
```

---

# Held Cockpit visual and semantic controls

```text
G4 Adaptive Hybrid world
Dark mode baseline
H4 hover/outward response
Reduced in-box resting light
scientific category-marker grammar
E5 Hue + Tag relation-class carrier
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
switchable runtime carrier with T7 Soft Shade
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working default
Z7 Pull-Back Then Dive specialist-workspace entry
fullscreen specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite Conversation Workspace baseline
Boxes/Text user-switchable conversation rail
A6 Adaptive Anchor opened-box composition
A6 resting state without redundant floating box
```

Important targets:

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
```

---

# Specialist deep focus

Primary evidence:

```text
docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
docs/research/077_fullscreen_specialist_workspace_and_spatial_zoom_transition_experiment.md
frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
```

Result:

```text
Z7 Pull-Back Then Dive selected
fullscreen specialist workspace selected current end-state direction
project grid / surrounding boxes absent in deep focus
compact topology compass retained
```

---

# Semantic zoom

```text
docs/checkpoints/244_z7_deep_focus_accepted_semantic_zoom_review_opened.md
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

semantic zoom
    DEFERRED
```

---

# Conversation Workspace visual and scope decisions

Independent visual evidence:

```text
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
frontend/design-lab/conversation-workspace-claude-independent.html
frontend/design-lab/conversation-workspace-chatgpt-independent.html
```

Held result:

```text
Quiet Graphite
    selected current visual baseline

previous rendered ChatGPT / Claude alternatives
    rejected as currently rendered systems
```

Scope/anchor evidence:

```text
docs/checkpoints/246_quiet_graphite_baseline_conversation_scope_anchor_review_opened.md
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
frontend/design-lab/conversation-workspace-work-unit-anchor.html
```

Held scope model:

```text
PROJECT-GENERAL CONVERSATION
    no work-unit home

WORK-UNIT-SCOPED CONVERSATION
    explicit work-unit home

PER-TURN CONTEXT
    separate temporary context

Conversation rail
    Boxes / Text user switch

A6 Adaptive Anchor
    selected opened-box composition
    no redundant floating work-unit box at rest
```

---

# Earlier Conversation Workspace composition evidence recovered

Research 079 remains important:

```text
docs/research/079_conversation_workspace_presentation_architecture_experiment.md
frontend/design-lab/conversation-workspace-architecture.html
```

The earlier candidates are now interpreted as presentation/co-presence mechanisms rather than mutually exclusive product architectures:

```text
CV0 Focus Workspace        -> full chat focus baseline
CV1 Right Dock             -> work-primary co-present candidate
CV2 Split Workbench        -> balanced co-present candidate
CV5 Focus + Context Rail   -> chat-dominant co-present candidate
CV6 Conversation + Inspector -> focused-context evidence
```

---

# Current Slice: Conversation access + coexistence

Checkpoint:

```text
docs/checkpoints/248_conversation_access_and_coexistence_architecture_review_opened.md
```

Research/browser:

```text
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
frontend/design-lab/conversation-workspace-access-coexistence.html
frontend/design-lab/conversation-workspace-access-coexistence.css
frontend/design-lab/conversation-workspace-access-coexistence.js
```

Local URL:

```text
http://localhost:5173/design-lab/conversation-workspace-access-coexistence.html
```

Current product model:

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

Browser presentation candidates:

```text
P0 Work only / compact chat
P1 Full chat focus
P2 Right dock
P3 Balanced split
P4 Chat dominant + work context
```

P3 is only the initial browser default. No co-present mode is frozen.

Checkpoint 247's E0-E4 entry transitions remain preserved as possible full-focus transition motion evidence. No winner was selected.

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

Claude Message 010 is complete. Current next actor is the human project owner reviewing the conversation access/coexistence architecture.

---

# Promoted Cockpit architecture

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Specification 008 remains accepted and is not replaced by current browser experiments.

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
