# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            251
active branch         v1-cockpit-design-exploration
active PR             none
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      source-faithful holistic Cockpit reintegration
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

## Critical Cockpit integration state

The first holistic integrated Cockpit browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is **not an accepted Cockpit baseline**.

Human review exposed major fidelity failures against previously accepted Phase-C designs. Source-level audit found that the repository preserved exact accepted target SHAs and executable artifacts, but that integration manually reimplemented the design from textual summaries instead of faithfully reusing/porting those exact artifacts.

Concrete mismatches included:

```text
canonical WorkUnit geometry and surface grammar changed
H4 rest/hover layers were simplified/reinterpreted
G4 ambient behavior was reauthored with fixed authored positions
Quiet Graphite was approximated with a new global palette/font system
```

The failed browser remains only as diagnostic evidence and is explicitly excluded from the replacement implementation source graph. Production `/cockpit` remains untouched.

## Implementation-provenance recovery: complete

The repository now has a dedicated Cockpit provenance layer:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

The manifest currently contains:

```text
23 total entries
19 MUST_PORT / MUST_PRESERVE
4 deliberately non-promotable entries
```

A full-history GitHub Actions gate has verified every declared exact source binding:

```text
workflow run 33156357834
commit 2127563c0ed980f7bf6fad36e36b11e76500c59b

Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

This closes the provenance gate. It does not yet mean a replacement holistic browser has passed implementation fidelity.

## Current reintegration protocol

The next holistic Cockpit is a controlled composition task, not a fresh design exercise.

```text
MUST_PORT / MUST_PRESERVE
    reuse or port the exact accepted source implementation
    preserve declared geometry, behavior and visual hierarchy
    adapt only inside the manifest boundary

PROVISIONAL_ONLY
    carry only where necessary
    keep explicitly provisional

DEFERRED / REJECTED / EVIDENCE-ONLY
    preserve history
    do not select through implementation accident

UNRESOLVED WHOLE-PRODUCT GLUE
    introduce the minimum required glue
    label and record it as provisional
```

After composition, the replacement browser must pass the integrated fidelity gate against the exact accepted targets before holistic human product review resumes.

## Accepted Phase-C decisions remain intact

The failed integration does not revoke the previously held decisions, including G4, H4, scientific WorkUnit grammar, E5, D0-D3, P7, current-process focus, runtime/T7, BLOCKED/FAIL, A3, SEL2, X5, Z7, S0, Quiet Graphite, Boxes/Text, A6 and Conversation access across Grid/Deep Dive.

The complete disposition history is in `docs/cockpit/PHASE_C_DECISION_LEDGER.md`. The exact implementation source graph is in `docs/cockpit/accepted_implementation_manifest.json`.

## Repository preservation conclusion

The repository-memory architecture preserved the semantic decisions and historical executable artifacts. The failure exposed a missing implementation-consumption safeguard, which is now addressed through:

```text
semantic decision record
    + complete disposition history
    + exact implementation provenance
    + deterministic historical-source verification
    + integrated implementation-fidelity verification
```

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md

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
