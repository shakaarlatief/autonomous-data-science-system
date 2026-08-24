# Current State

**Checkpoint:** 178  
**Date:** 2026-08-24  
**Active development branch:** `v1-dependency-backed-recommendation-value`  
**Active PR:** #55 draft, Specification 021 first governed live execution incomplete; instrumentation repair next  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological-knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, dependency-backed blocking construct validity, and machine-checkable current-routing consistency seams. Specification 021 remains prospectively frozen; its first governed live execution is preserved as incomplete because attempt-metadata serialization prevented every reasoner output from becoming a scored observation.  
**Latest experiment status:** Specification 021 `INCOMPLETE`  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** keep the first live run immutable as incomplete evidence, repair only the mappingproxy-backed usage-metadata serialization defect for reasoner and judge attempt records, prove the repair provider-free cross-platform, and only then freeze any replacement live-source boundary.

## Active ChatGPT development context

```text
Design session: 05
ChatGPT project: Autonomous Data Science System
Session title: 05 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` hosts the narrow governed live-launch control plane. The consumed Specification 021 authorization and temporary default-branch live exposure have been retired after preservation of the first raw run; no replacement Specification 021 provider call is currently authorized.

---

## Durable architecture and accepted evidence

Prototype V0 established the scaling rule:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Foundation 018 separates Objects, Relations, Events, and Views. Foundation 019 establishes:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Foundation 020 separates reusable methodological knowledge from project state, execution implementation, and presentation.

Accepted technical/runtime boundaries remain D-028 through D-032. Specification 008 remains the promoted Project Cockpit interaction architecture. Specifications 012-014 remain the bounded accepted Horizon/selective-context/real-reasoning chain. Specification 018 remains the accepted governed live-experiment launcher.

Research 028 preserves the broader forward architecture:

```text
SYSTEM-OWNED PROJECT STATE
    What is true about this project?

METHODOLOGICAL NAVIGATION
    Given what is true, what matters now?

LLM REASONING
    Given what matters, how should we reason about it?
```

---

## Current evidence chain

```text
reusable methodological knowledge
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> real reasoning evidence                              [SUPPORTED]
    -> recommendation/action experiment 015                 [FAIL, PRESERVED]
    -> dependency-backed disposition diagnostic 016         [SUPPORTED]
    -> relation-backed recommendation experiment 017        [INCOMPLETE, PRESERVED]
    -> governed live-experiment launcher 018                 [SUPPORTED, PROMOTED]
    -> system-owned-provenance recommendation experiment 019 [FAIL, PRESERVED]
    -> recommendation/blocking calibration diagnostic 020   [SUPPORTED, PROMOTED]
    -> dependency-backed recommendation-value experiment 021 [INCOMPLETE; RAW EVIDENCE PRESERVED]
```

Specification 014 showed equal frozen reasoning quality for SELECTIVE and FULL_HORIZON while SELECTIVE used 66.56% fewer provider input tokens.

Specification 016 supported the bounded construct that DEFER-like sequencing needs an exact represented activating dependency when deterministic separation from NOT_NOW is expected.

Specification 019 completed the matched recommendation-value rerun after system-owned provenance repaired the instrumentation defect, but the frozen result remained `FAIL`. SELECTIVE exact disposition accuracy was `0.916667` versus `0.944444` for GENERIC and FULL_HORIZON, with repeated blocking false positives in the nonlinear model-family case.

Specification 020 prospectively isolated the recommendation/blocking construct and returned `BLOCKING_BOUNDARY_SUPPORTED` with 36/36 exact observations and exact requirement/scope pointers. The supported bounded construction is:

```text
exact unresolved requirement
    + exact active defended downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action RESOLVES requirement
```

Specification 019 remains immutable `FAIL` evidence and is not rescored.

---

## Specification 020 preserved result

Frozen live source:

```text
82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
```

Governed live execution:

```text
launch issue          45
launcher run          32701990350
live run              32701999678
live job              97355284139
artifact               9510887324
artifact SHA-256       35ed6b472eac22090e563bbafee30aab1b666c00453ebcfd8cd0a832b79be678
reasoner outputs       36 / 36
provider attempts      36 / 45
failed attempts        0
retries                0
execution integrity    true
outcome                BLOCKING_BOUNDARY_SUPPORTED
```

Primary evidence:

```text
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
```

---

## Level-2 routing-consistency hardening closed

Checkpoint 173 closes the first narrow machine-checkable current-routing hardening.

Accepted mechanism:

```text
docs/current_routing.json
    routing metadata only

scripts/check_current_routing.py
    validates manifest shape, referenced checkpoint existence,
    and key current routing fragments

.github/workflows/current-routing-consistency.yml
    cross-platform validation on routing-sensitive changes
```

Final closure evidence:

```text
PR #54 final head                       44d92d73029ad56925bd2c49bb373be5bdef44ce
PR #54 merge                            a639cfc570290a2169425f43078bbb242fa398e9
final routing-sensitive integration     09670d5127c14cf3cece727b31823d5de4572211
Current routing consistency push run    32719182489  success
ubuntu-latest                           success
windows-latest                          success
```

Markdown remains the substantive knowledge source. The manifest is not a second repository for rationale, specifications, experiment interpretation, or historical evidence.

---

## Specification 021 incomplete first live execution

Frozen design artifacts remain:

```text
docs/research/029_dependency_backed_recommendation_value_design.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
docs/checkpoints/174_specification_021_dependency_backed_recommendation_value_contract_frozen.md
```

Frozen scientific question:

> Given matched project microstates with explicit requirement/scope/resolver relations, explicit defer-trigger relations, fixed reasoner/runtime treatment, and system-owned methodological provenance, does the accepted SELECTIVE exact-revision methodological-context path improve recommendation/action quality relative to a strong GENERIC reasoner while remaining no more expansion-prone than FULL_HORIZON?

Exactly four new cases are frozen:

```text
DBRA-01  future validity and model sequencing
DBRA-02  compact nonlinear model shortlist
DBRA-03  distribution evidence before transformation
DBRA-04  missingness / class-imbalance decision framework
```

Exactly three conditions are frozen:

```text
GENERIC
SELECTIVE
FULL_HORIZON
```

The system owns exact methodological provenance and supplied project relation identities. The model owns recommendation content and may select only among supplied IDs.

Action-local pointer semantics are frozen:

```text
BLOCKING_REQUIRED
    exact blocking requirement + exact blocked scope + null defer pointer

RECOMMENDED
    all pointers null

DEFER
    null blocking pointers + exact supplied defer trigger

NOT_NOW
    all pointers null
```

The complete plan is:

```text
4 cases x 3 conditions x 3 repetitions
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
90 maximum attempts
randomization seed 2026082402
```

Frozen complete outcomes:

```text
PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
incomplete / integrity failed -> no advancement classification
```

`SAFE_BUT_NOT_DIFFERENTIATED` is a legitimate scientific outcome. The contract must not be changed merely because a strong generic reasoner remains competitive.

Provider-free implementation evidence at Checkpoint 175:

```text
validated implementation head             8e199c29e3f082b353f92f27868aedca0ebbbf74
Specification 021 provider-free run        32722934829  success
ubuntu job                                 97418007046  success
windows job                                97418007218  success
```

Checkpoint 176 froze the fully reconciled pre-live source:

```text
aa830eda4fe80bc349afcb4f3bd0ab53f37bfcc7
```

Checkpoint 177 freezes the exact live-capable source and historical source ref:

```text
validated live source                      b589bad975880b2d3cccc3596fc82539b1b96577
live-source ref                            v1-spec021-dependency-backed-recommendation-value-live-source
Specification 021 provider-free run        32724242554  success
windows job                                97421896915  success
ubuntu job                                 97421897042  success
Current routing consistency                32724242550  success
Checkpoint metadata                        32724242502  success
V1 reasoning context value                 32724242572  success
V1 disposition semantics diagnostic        32724242509  success
V1 blocking calibration diagnostic         32724242515  success
V1 autonomous live experiment launcher CI 32724242570  success
```

The live source contains only separated provider execution plumbing around the frozen experiment. The first live-plumbing validation exposed one lifecycle mismatch: the implementation-stage `DBRA-INV-24_no_live_surface` invariant correctly became incompatible with Checkpoint 176's permission to add the live wrapper/workflow. It was replaced by `DBRA-INV-24_pre_authorization_boundary`, which requires the one-shot repository authorization to remain absent until the live source is frozen. Frozen scientific authority did not change.

The first governed live execution is now preserved:

```text
launch issue             56
launcher run             32727227189
live run                 32727241852
live job                 97431195730
artifact                 9520249437
artifact SHA-256         b936fab44a17dc22fb9fe31dacdb6f09104a765fcb2223df8ef517338403fe77
preservation commit      247314916fa028e2d27ea282ee030a26a30a84cc
successful reasoners     0 / 36
successful judges        0 / 36
reasoner failed attempts 72
provider attempts        72 / 90
complete scored design   false
execution integrity      false
advancement outcome      null
classification           INCOMPLETE
```

All 72 reasoner attempts failed uniformly while recording live-shaped usage metadata with `cannot pickle 'mappingproxy' object`. No condition-specific recommendation conclusion is justified. Checkpoint 178 strongly isolates the defect to attempt-metadata serialization and freezes the run as incomplete evidence, not scientific `FAIL`.

The consumed launch authorization, temporary default-branch target workflow, observer, and preservation helper have been retired after raw evidence preservation. Issue #56 is closed as completed. No replacement live execution is authorized at this boundary.

---

## Current non-selections

Still deliberately open:

```text
whether explicit methodological knowledge adds recommendation/action value beyond a strong generic reasoner
final recommendation/action taxonomy and ranking policy
production REQUIRED/BLOCKING semantics
whether blocking should ultimately be deterministic from project relations
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
accepted recommendation -> authoritative project object/event mapping
automatic project execution and human approval/escalation policy
admissibility/risk-sensitive assurance policy
large-scale governed knowledge-universe construction
final provider/model and reasoning-effort policy
multi-agent/specialist architecture
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

---

## Exact continuation

```text
1. keep run 32727241852 immutable as INCOMPLETE evidence
2. replace only unsafe usage attempt-metadata serialization with explicit JSON-safe serialization
3. cover both reasoner and judge attempt recording with non-null live-shaped raw_provider_usage regression tests
4. validate the repair on Ubuntu and Windows with no provider credential
5. run inherited accepted-seam checks on the exact repaired head
6. freeze a new exact live-source boundary only after all required checks pass
7. use a new Specification 018 launch ID for any replacement live run
8. preserve any replacement artifact before interpretation
9. do not modify or rescore Specification 021 science or Specifications 015-020
```

## Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/173_routing_consistency_hardening_promoted_and_closed.md
docs/checkpoints/174_specification_021_dependency_backed_recommendation_value_contract_frozen.md
docs/checkpoints/175_specification_021_provider_free_implementation_gate_cross_platform_passed.md
docs/checkpoints/176_specification_021_pre_live_boundary_frozen.md
docs/checkpoints/177_specification_021_live_source_frozen.md
docs/checkpoints/178_specification_021_live_execution_incomplete_usage_serialization.md
docs/research/029_dependency_backed_recommendation_value_design.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```
