# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            256
active branch         v1-cockpit-design-exploration
active PR             none
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      structural Conversation spacing + flat rail control-set human review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

## Current Cockpit status

The source-faithful integrated Cockpit is the protected whole-product design substrate.

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Current human-review route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=angled
```

The `edge=angled` query is historical implementation plumbing. The current right-side rail is normal flat 2D.

Current review targets are:

```text
Conversation Boxes rail
    16px list row gap
    6px top + bottom structural WorkUnit-row padding
    actual rendered surfaces must read as distinct objects

Project Grid right rail
    compact flat 2D surface
    Fullscreen restored
    Expand selected WorkUnit removed from current rail candidate
    Hide project HUD removed from current rail candidate
    clarity-only label expansion retained

Current-process Focus
    explicitly unchanged
    project owner confirmed it is working correctly

Deep Dive project-position compass
    live Checkpoint 255 implementation carried forward unchanged
```

Latest complete Cockpit fidelity workflow:

```text
implementation target  e2768a807b2a80f438248a25f7d41e53be561d51
workflow run           33211613408
job                    98985900484
browser tests          68 / 68 passing
```

The current gate measures actual rendered Conversation WorkUnit separation at both desktop and narrow widths, rather than relying only on CSS gap values.

Production `/cockpit` remains untouched.

## Critical integration history

The first holistic integrated Cockpit browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is **not an accepted Cockpit baseline**.

Human review exposed major fidelity failures against previously accepted Phase-C designs. Source-level audit found that the repository preserved exact accepted target SHAs and executable artifacts, but that integration manually reimplemented the design from textual summaries instead of faithfully reusing or porting those exact artifacts.

The failed browser remains only as diagnostic evidence and is explicitly excluded from the replacement implementation source graph.

## Implementation-provenance recovery: complete

The repository has a dedicated Cockpit provenance layer:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

The manifest contains:

```text
23 total entries
19 MUST_PORT / MUST_PRESERVE
4 deliberately non-promotable entries
```

A full-history GitHub Actions gate verified every declared exact source binding:

```text
workflow run 33156357834
commit 2127563c0ed980f7bf6fad36e36b11e76500c59b

Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

## Accepted Phase-C decisions remain intact

The held mechanism set still includes G4, H4, scientific WorkUnit grammar, E5, D0-D3, P7, current-process focus, runtime/T7, BLOCKED/FAIL, A3, SEL2, X5, Z7, S0, Quiet Graphite, Boxes/Text, A6 and Conversation access across Grid and Deep Dive.

Checkpoint 256 changes Conversation row geometry and the current flat-rail control composition only. It does not revoke those held semantics.

The complete disposition history is in `docs/cockpit/PHASE_C_DECISION_LEDGER.md`. The exact implementation source graph is in `docs/cockpit/accepted_implementation_manifest.json`.

## Repository preservation model

The repository-memory architecture combines:

```text
semantic decision record
    + complete disposition history
    + exact implementation provenance
    + deterministic historical-source verification
    + integrated implementation-fidelity verification
    + explicit current routing
```

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/256_structural_conversation_spacing_and_project_tool_rail_controls_review_opened.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md

docs/checkpoints/255_flat_project_rail_conversation_spacing_and_live_compass_review_opened.md
docs/research/095_conversation_spacing_flat_project_rail_and_live_topology_compass.md

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json

# failed integration evidence only
docs/checkpoints/249_holistic_integrated_cockpit_baseline_review_opened.md
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
frontend/design-lab/cockpit-integrated-baseline.html

# collaboration state
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```
