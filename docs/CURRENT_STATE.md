# Current State

**Checkpoint:** 251  
**Date:** 2026-08-28  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C source-faithful holistic reintegration. The implementation-provenance recovery opened by Checkpoint 250 is complete: the full Phase-C decision ledger exists, the 23-entry implementation manifest is structurally valid, and every declared historical source path resolves at its exact integration target under a full-history CI gate. The replacement holistic Cockpit may now be built only by exact source reuse/porting plus explicitly provisional whole-product glue.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-09
Conversation title       09 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

```text
docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
```

Current task:

```text
build replacement holistic Cockpit by source-faithful composition/porting
preserve every MUST_PORT / MUST_PRESERVE manifest item
carry provisional items only as provisional
keep deferred/rejected/evidence-only candidates unselected
introduce only minimum unresolved whole-product glue and label it provisional
run deterministic provenance validation continuously
add integrated fidelity checks against exact accepted targets
only then resume holistic human product review
```

Production `/cockpit` remains untouched.

---

# Implementation-provenance recovery status

Durable recovery architecture:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

Current manifest coverage:

```text
23 total entries
19 required
    MUST_PORT / MUST_PRESERVE

4 non-promotable
    PROVISIONAL_ONLY
    DO_NOT_SELECT_DURING_INTEGRATION
    EXCLUDED_SOURCE
```

First full-history provenance run:

```text
workflow run  33156357834
commit        2127563c0ed980f7bf6fad36e36b11e76500c59b

Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

This closes the provenance gate. It does **not** yet close the integrated fidelity gate.

---

# Two-gate integration model

```text
PROVENANCE GATE
    exact decision/source recovery
    exact historical source resolution
    PASS

INTEGRATED FIDELITY GATE
    replacement browser preserves declared geometry/behavior/visual hierarchy
    replacement browser preserves semantic-channel separation
    provisional glue remains identified
    failed/deferred/rejected sources remain unselected
    OPEN / NOT YET PASSED
```

A replacement browser may not be called the accepted holistic baseline merely because it renders or because the provenance validator passes.

---

# Failed integration disposition

The first holistic browser:

```text
frontend/design-lab/cockpit-integrated-baseline.html
exact target 8e554d847bb3b6318db432abcb5dff742f0fa523
```

remains classified as:

```text
FAILED INTEGRATION ATTEMPT
NOT an accepted baseline
NOT a production target
NOT a basis for new visual decisions
EXCLUDED from the implementation source graph
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
Conversation coexistence      db31970d6885ce785609f9c3300f22123130d821
```

The complete exact source graph is in `docs/cockpit/accepted_implementation_manifest.json`; the short list above is navigation only.

---

# Repository-preservation diagnosis

Current evidence:

```text
semantic decisions              preserved
complete Phase-C disposition    preserved
exact target SHAs               preserved
executable historical artifacts preserved
implementation source bindings  preserved
exact-history CI verification   active
holistic integrated fidelity    not yet proven
```

The durable integration model is now:

```text
semantic decision
    + complete disposition history
    + exact implementation target
    + exact source files
    + allowed adaptation boundary
    + known fixture caveats
    + deterministic provenance gate
    + integrated fidelity gate
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
