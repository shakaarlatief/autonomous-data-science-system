# Current State

**Checkpoint:** 187  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolve the principal design choices for the first project-state-to-methodological-horizon coverage diagnostic. Specification 022 is not frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the Checkpoint 187 design boundary, then prospectively freeze the exact Specification 022 treatment universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and advancement gates before implementation.

## Active ChatGPT development context

```text
Design session: 05
ChatGPT project: Autonomous Data Science System
Session title: 05 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. `main` hosts the narrow governed live-launch control plane. Specification 020 one-shot authorization and temporary live/observer/preservation/reconciliation helpers have been retired from `main`, while their GitHub audit history remains preserved.

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
    -> dependency-backed recommendation experiment 021        [FAIL, PRESERVATION ONLY]
```

Specification 014 showed equal frozen reasoning quality for SELECTIVE and FULL_HORIZON while SELECTIVE used 66.56% fewer provider input tokens.

Specification 016 supported the bounded construct that DEFER-like sequencing needs a concrete represented activating dependency if deterministic separation from NOT_NOW is expected.

Specification 019 completed the matched recommendation-value rerun after system-owned provenance repaired the instrumentation defect, but the frozen result remained `FAIL`.

Specification 020 prospectively isolated the recommendation/blocking construct and completed successfully. Its cleaned exact PR head passed the Specification 020 Ubuntu/Windows diagnostic plus accepted reasoning-context, disposition-semantics, launcher, and checkpoint-metadata regressions before PR #44 merged into `v1-frontend-spike` at `a856983172f6436b73e3f7d0e609d208b55a443b`.

---

## Specification 020 complete result

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
```

Frozen gate result:

```text
BC-G01 structured validity                    PASS
BC-G02 aggregate exact accuracy               1.000000  PASS
BC-G03 every variant majority-correct         12 / 12 at 3 / 3  PASS
BC-G04 every pair both sides majority-correct 6 / 6, both sides 3 / 3  PASS
BC-G05 exact joint blocking pointers          1.000000  PASS
BC-G06 RECOMMENDED null pointers              1.000000  PASS

outcome                                      BLOCKING_BOUNDARY_SUPPORTED
```

Supported conclusion:

```text
exact unresolved requirement
    + exact active defended downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action resolves requirement

can make BLOCKING_REQUIRED operationally separable from RECOMMENDED
for the frozen deliberately unambiguous microstates with the fixed reasoner.
```

This does not promote production `BLOCKING_REQUIRED`/`RECOMMENDED` enums or establish selective methodological-context recommendation value.

Specification 019 remains immutable `FAIL` evidence and is not rescored.

Raw and interpreted evidence:

```text
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
```

---

## Preservation and continuity hardening

Checkpoint 172 records the green bounded hardening:

```text
docs/current_routing.json
    routing metadata only

scripts/check_current_routing.py
    validates the manifest contract
    verifies the current checkpoint exists
    verifies README / CURRENT_STATE / KNOWLEDGE_MAP do not contradict key pointers

.github/workflows/current-routing-consistency.yml
    runs the validator on Ubuntu and Windows for routing-sensitive changes
```

Pre-checkpoint implementation evidence:

```text
head                               5f5dfb81a97f089afc91f20d4632683714a43f60
Current routing consistency        32714760241  success
V1 blocking calibration diagnostic 32714760194  success
V1 autonomous launcher CI          32714760205  success
V1 reasoning context value         32714760211  success
V1 disposition semantics           32714760225  success
```

Final exact PR #54 promotion evidence:

```text
head                                      44d92d73029ad56925bd2c49bb373be5bdef44ce
Checkpoint metadata                       32718585355  success
Current routing consistency               32718585226  success
  ubuntu-latest                           success
  windows-latest                          success
V1 blocking calibration diagnostic        32718585224  success
V1 autonomous live experiment launcher CI 32718585218  success
V1 reasoning context value                32718585213  success
V1 disposition semantics diagnostic       32718585232  success
merge                                     a639cfc570290a2169425f43078bbb242fa398e9
```

Checkpoint 172 provenance belongs to Design session 05, `05 - Selective Context Promotion & Reasoning Vertical Slice`.

Markdown remains the substantive knowledge source. The manifest does not replace foundations, specifications, checkpoints, results, decisions, or explanatory current-state material. Development Method remains v0.4 because that version already authorizes narrow partial automation once repetitive or inconsistent current-routing maintenance is observed.

---

## Current non-selections

Still deliberately open:

```text
final recommendation/action taxonomy and ranking policy
production REQUIRED/BLOCKING semantics
whether and how methodological navigation / coverage reduces the human burden of surfacing important analytical paths across realistic evolving projects
natural-language/project-state -> reasoning-function derivation
open-world proposal/action discovery
mapping accepted recommendations to authoritative project objects/events
automatic project execution and human approval/escalation policy
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist architecture
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

---

## Exact continuation

```text
1. validate the exact Checkpoint 187 / PR #68 reconciled design head
2. prospectively author and freeze Specification 022 with exact universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and gates
3. only after that frozen contract is green, implement provider-free experiment machinery and integrity tests
4. do not authorize a provider-backed run until a later exact live-capable source is separately frozen and authorized through Specification 018
5. do not rerun the supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```

## Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/187_project_state_methodological_coverage_design_choices_resolved.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/checkpoints/186_methodological_navigation_coverage_review_completed.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

## Specification 021 complete result and interpretation boundary

Specification 021 completed after the first live attempt was preserved as `INCOMPLETE` instrumentation evidence and the usage-serialization defect was repaired without changing the frozen scientific contract.

The complete replacement design produced:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           1.000000       1.000000        1.000000
semantic score           0.958333       0.950000        0.950000
blocking false positives 0              0               0
pointer errors            0              0               0
```

Frozen outcome:

```text
DBRA-G08 SELECTIVE DBRA-01 semantic  0.800000 < 0.850000
positive SELECTIVE value signals     0
advancement outcome                  FAIL
```

The failed recommendation implementation is not promoted. PR #66 preserves the contract, fixture, raw evidence, stable result, research, and checkpoints only.

Research 030 / Checkpoint 183 additionally clarify that this supplied-action disposition experiment is not a test of the broader methodological-navigation and coverage capability. Question A remains largely untested end-to-end.

## Question A architecture/evaluation review

Research 031 establishes the next evaluation decomposition:

```text
UNIVERSE COVERAGE
    -> NAVIGATION / PATH COVERAGE
    -> APPLICABILITY / MISSING CONTEXT
    -> CONCRETE OPTION GENERATION
    -> PRIORITIZATION / DISPOSITION
    -> MODEL-FACING CONTEXT VALUE
```

The first successor experiment class should move upstream and begin from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Research 032 / Checkpoint 187 now resolve the leading diagnostic design as four evolving episode families, a controlled 28-asset benchmark universe, separate hidden oracle and evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, explicit catalog-gap accounting, blinded semantic matching, and reliability/noise metrics. The exact Specification 022 payloads, thresholds, runtime settings, seed, and gates remain to be frozen prospectively.
