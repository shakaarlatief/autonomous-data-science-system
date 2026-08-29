# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            259
active branch         v1-cockpit-design-exploration
active PR             none
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      presentation-state integrity human confirmation, then Adaptive Conversation Dock review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

## Current Cockpit status

The source-faithful integrated Cockpit is the protected whole-product design substrate.

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Normal current substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Adaptive Conversation Dock review route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Checkpoint 259 interrupts the Adaptive Conversation Dock review only long enough to confirm recovery of two intermittent presentation failures reported by the project owner.

### Conversation Boxes integrity

The accepted spacing remains:

```text
16px list row gap
6px top + bottom structural WorkUnit-row padding
canonical WorkUnit footprint unchanged
```

Research 098 found selector drift between the current Conversation renderer (`data-thread-scope="work"`) and the historical `.is-workunit-thread` selector used by the structural padding correction. Accepted spacing also depended unnecessarily on a late-mounted rail-study stylesheet.

The recovery moves the accepted spacing contract into a statically loaded presentation-integrity layer and corrects the current selector binding. The spacing is now verified through full-focus, Boxes/Text switching, co-present mode and the Adaptive Dock Threads drawer.

### Current-process Focus integrity

The accepted M09 focus semantics remain unchanged.

Research 098 found an asymmetric lifecycle: WorkUnit focus membership was initialized once, while relation focus classes were continuously resynchronized. A WorkUnit DOM remount could therefore produce the reported state in which relation lines recessed but WorkUnit boxes did not.

The recovery now keeps one authoritative membership set, repairs membership on WorkUnit remounts, resynchronizes relations after repair, statically loads the Focus stylesheet and protects the accepted recession values from later study-style precedence.

Latest complete Cockpit fidelity workflow:

```text
implementation target  0374d624ec0e88d65060fb2424ce18291ca40792
workflow run           33240152004
job                    99067985262
browser tests          73 / 73 passing
```

The previous 71 tests remain green. Two new lifecycle regressions explicitly cover the intermittent failure families.

The Adaptive Conversation Dock remains an opt-in candidate. Its product-design judgment resumes immediately after the project owner confirms the repaired spacing and Focus behavior remain stable in normal use.

Production `/cockpit` remains untouched.

## Critical integration history

The first holistic integrated Cockpit browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is **not an accepted Cockpit baseline**.

Human review exposed major fidelity failures against previously accepted Phase-C designs. The repository had preserved exact accepted target SHAs and executable artifacts, but integration manually reimplemented them from textual summaries instead of faithfully reusing or porting those exact artifacts.

The failed browser remains diagnostic evidence only and is excluded from the replacement source graph.

## Implementation-provenance recovery

The Cockpit provenance layer remains authoritative:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

Manifest coverage:

```text
23 total entries
19 MUST_PORT / MUST_PRESERVE
4 deliberately non-promotable entries
```

First exact-history proof:

```text
workflow run 33156357834
commit       2127563c0ed980f7bf6fad36e36b11e76500c59b
result       PASS
```

The rule remains:

```text
accepted implementation exists
    -> reuse or port exact implementation
    -> preserve accepted geometry / behavior / hierarchy
    -> adapt only inside the recorded boundary
    -> verify against exact source evidence
```

## Held Phase-C decisions remain intact

The held mechanism set still includes G4, H4, scientific WorkUnit grammar, E5, D0-D3, P7, current-process focus, runtime/T7, BLOCKED/FAIL, A3, SEL2, X5, Z7, Quiet Graphite, Boxes/Text, A6 and Conversation access across Grid and Deep Dive.

L0 remains provisional. Semantic zoom remains deferred with S0 as the geometric working default.

Checkpoint 259 repairs implementation integrity only. It does not reopen Conversation spacing values, M09 Focus semantics, Quiet Graphite, Boxes/Text, A6, conversation scope/access, source-state preservation or the Adaptive Conversation Dock composition question.

`docs/cockpit/PHASE_C_DECISION_LEDGER.md` remains the exhaustive disposition ledger for Research 037-088. Later source-recovery and whole-product studies are routed through Research 089 onward, checkpoints and current-state records.

## Repository preservation model

```text
semantic/product authority
    + design disposition
    + exact implementation provenance
    + deterministic historical-source verification
    + integrated implementation-fidelity verification
    + explicit current routing
    + human product-design gates
```

## Start here

```text
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

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json

# collaboration state
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```
