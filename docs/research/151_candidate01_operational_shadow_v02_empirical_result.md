# Research 151: Candidate 01 Operational Shadow V0.2 Empirical Result

**Date:** 2026-09-14
**Status:** BROADER OPERATIONAL SHADOW PASS AFTER PRESERVED FIRST-RUN DEFECTS / REAL-REPOSITORY SHADOW QUALIFICATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Implement the exact Research 150 operational fixture after its public freeze, preserve and diagnose first-run defects before repair, verify the repaired implementation against the untouched oracle, and determine what synthetic operational behavior is now supported.
**Authority:** Broader synthetic integration evidence only. No current authority surface is replaced and no frozen requirement is declared finally qualified.
**Declared references:** `research:149`, `research:150`, `research:145`, `path:docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_FIXTURE_V02.json`, `path:docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_ORACLE_V02.json`, `checkpoint:495`

## 1. Freeze and first-run provenance

The operational fixture/oracle were committed and pushed before implementation at:

```text
freeze commit        7231fcb0d6423787f58ed561a9064841e5f9a724
fixture SHA-256      6daefddd448ead145281d56da8325925cb82c71fc57418283ef21c65418ec486
oracle SHA-256       a1af441f356fbd0e7cac65ba1f6c45589f96941139e669d99de4276acf8440b6
```

The first executable output was preserved before oracle-driven repair:

```text
FIRST_RUN_RESULTS_V02.json
SHA-256  b570c078908adb9ce64680b9a2c820fd44d35838a23ba4077c278be444de5e18
```

A separate comparison record captures the first-run result against the frozen oracle:

```text
FIRST_RUN_COMPARISON_V02.json
SHA-256  ed48a1bf88bef1b5e1207d2a11f406fb24ce3cfcdc775b5d2d5e4ae67dea1ee3
38 checks
35 pass
3 fail
```

The final repaired result is:

```text
RESULTS_V02.json
SHA-256  6a7e2f1b9846cb2e7c3e349c75a512c30540ccdab0ae485a3154d398236a7de6
```

Fixture and oracle bytes remained unchanged throughout.

## 2. First-run defects were preserved, not hidden

The first run failed exactly three checks.

### D1: paused-workstream ordering mismatch

The semantic membership was correct, but `paused_visible` was alphabetically sorted rather than preserving the source/control ordering frozen by the view contract.

```text
first run   WS-MIGRATION, WS-PRIVATE
oracle      WS-PRIVATE, WS-MIGRATION
```

This was a deterministic view-order contract defect, not a workstream-state error. The implementation was corrected to preserve declared source order.

### D2: current-state workstream ordering mismatch

The current-state core contained the correct active/paused/blocked sets but alphabetically sorted them. The frozen view contract expected project/control order. The implementation now preserves workstream-source order.

Again, the defect was representational/order fidelity rather than missing or false semantic state.

### D3: natural authority precedence was reversed

This was the substantive first-run defect. The resolver interpreted `SUPPLEMENT owner -> target` backwards and emitted the supplement before its base:

```text
first run   AUTH-SAFE-SUPPLEMENT, AUTH-SAFE-BASE
required    AUTH-SAFE-BASE, AUTH-SAFE-SUPPLEMENT
```

The repair replaced the incorrect base-selection heuristic with a small deterministic topological walk in which relation targets are prerequisites of the relation owner. This preserves the natural directional semantics already established in MC-0016.

No fixture/oracle weakening was used to make these failures pass.

## 3. O1 workstream continuity result

Baseline mandatory route:

```text
WS-PKA -> WS-C01 -> WS-OPS
```

Long-lived paused work remains visible without permanently occupying the mandatory route:

```text
WS-PRIVATE
WS-MIGRATION
```

The fixture contains two genuine multi-dependency nodes:

```text
WS-INTEGRATION <- WS-OPS + WS-PRIVATE
WS-MIGRATION   <- WS-INTEGRATION + WS-AUDIT
```

When the frozen `PRIVATE_FIXTURE_READY=True` signal arrives, `WS-PRIVATE` becomes an activated route leaf while `WS-OPS` remains active. This demonstrates that pause/return semantics can change route salience without erasing durable paused-work metadata.

Interrupted transition recovery uses durable receipts:

```text
completed  T1, T2
pending    T3, T4
blind replay required  false
```

The stale workstream update expecting revision 3 against actual revision 4 fails with zero mutation. The fresh update expecting revision 4 succeeds and produces revision 5.

### Interpretation

The candidate can represent the workstream as a durable first-class semantic unit while keeping state single-source and generating aggregate route projections. This directly exercises the corrected Research 143 construct.

## 4. O2 capture, consolidation and promotion result

`SYN-BAD` omits must-preserve negative-evidence unit `U4` and fails fidelity even though its promotion review is `ACCEPTED`:

```text
SYN-BAD       FIDELITY_FAIL / missing U4
PROMOTE-BAD   PROMOTION_BLOCKED_FIDELITY
```

`SYN-GOOD` preserves all required units, including U4 as intentionally latent with a recoverable source, and may promote:

```text
SYN-GOOD       FIDELITY_PASS
PROMOTE-GOOD   PROMOTED -> KN-OPS-FOUNDATION
provenance     CAP-1
latent drilldown U4 -> CAP-1:U4
```

`CAP-2` remains candidate material. Storage and repeated inclusion in the capture set do not make it authority.

The generated narrative's unsupported novel claim `NC2` is routed back to candidate capture rather than entering the deterministic current-state core.

### Interpretation

This is executable support for the distinction:

```text
capture != accepted authority
review acceptance != sufficient promotion when fidelity fails
generated narrative != authority source
unique accepted synthesis crosses explicit promotion
```

## 5. O3 derived current views result

The three derived surfaces rebuild deterministically after deletion:

```text
ROUTING_CURRENT        rebuild equal
CURRENT_STATE_CORE     rebuild equal
NAVIGATION_INDEX       rebuild equal
```

Current-state core after the valid promotion:

```text
active     WS-PKA, WS-C01, WS-OPS
paused     WS-PRIVATE, WS-MIGRATION
blocked    WS-INTEGRATION
accepted   KN-BASE, KN-OPS-FOUNDATION
```

Navigation is generated from declarations and permits the same source to participate in several axes without truth duplication, for example `WS-PRIVATE` appears under project-knowledge, qualification and privacy.

### Interpretation

The experiment supports derived global routing/current/navigation surfaces with one-home-per-fact source semantics. It does not yet prove parity with the current real ADS `CURRENT_STATE.md`, `current_routing.json` or `KNOWLEDGE_MAP.md`.

## 6. O4 public/private degraded-mode result

All four frozen cases behave distinctly:

```text
PUBLIC-ONLY
    PASS_PUBLIC_ONLY
    private loaded = false

PRIVATE-REQUIRED-AVAILABLE
    PASS_PRIVATE_VERIFIED
    verification = VERIFIED

PRIVATE-REQUIRED-UNAVAILABLE
    FAIL_VISIBLE_REQUIRED_PRIVATE_UNAVAILABLE

RESOLVED-PRIVATE-NOT-VERIFIED
    public state remains RESOLVED_PRIVATE
    private verification = NOT_VERIFIED
```

The public result contains zero occurrences of the three private-only sentinel values.

### Interpretation

This directly exercises the owner policy that private unavailability must not invent contradiction with a publicly resolved-private conclusion, while genuinely private-required work must still fail visibly when verification is unavailable.

## 7. O5 authority uncertainty result

The candidate distinguishes four materially different cases:

```text
AUTH-COMPLETE
    RESOLVED
    AUTH-SAFE-BASE -> AUTH-SAFE-SUPPLEMENT

AUTH-MISSING-REQUIRED
    FAIL_VISIBLE_MISSING_REQUIRED_AUTHORITY
    missing AUTH-SAFE-SUPPLEMENT

AUTH-CONFLICT
    UNRESOLVED_AUTHORITY_CONFLICT
    AUTH-CONFLICT-A versus AUTH-CONFLICT-B

OPTIONAL-RETRIEVAL-DOWN
    DEGRADED_OPTIONAL_RETRIEVAL
    low-risk exploration may proceed
    uncertainty remains visible
```

This is important because "unavailable" is not one universal state. Consequence and source role determine whether the system must stop or may degrade.

## 8. Verification

```text
frozen fixture hash guard                 PASS
fixture/oracle unchanged after freeze      PASS
first-run result preserved                 PASS
first-run comparison preserved             PASS
first-run defects                          3
repair changed implementation only         PASS
focused V0.2 tests                         11 passed
all unit tests                             208 passed in 2.20s
Python in-memory compile                   PASS
final oracle comparison                    PASS
private sentinel leak count                0
```

## 9. Requirement-evidence interpretation

V0.2 adds broader synthetic support for mechanisms associated with:

```text
KA-R11 uncertainty visibility
KA-R13 action-shaped authority resolution
KA-R14 supplementation and unresolved conflict
KA-R17 consolidation fidelity
KA-R18 synthesis provenance
KA-R20 explicit authority class
KA-R21 rebuildability
KA-R22 explicit promotion
KA-R23 derived-view source/freshness contract shape
KA-R24 optional retrieval not sole authority
KA-R25 explicit workstream identity/state
KA-R26 pause/return semantics
KA-R27 multiple dependencies
KA-R28 interruption recovery
KA-R29 stale collaborator update safety
KA-R37 public/private authority boundary
KA-R38 non-leakage
KA-R39 bounded private dependency
KA-R42 consequence-sensitive degraded mode
KA-R47 multi-axis organization without copied truth
KA-R48 capture/consolidation/promotion separation
KA-I03 derived state has no unique accepted truth
KA-I06 missing/conflicting authority surfaces
KA-I07 must-preserve/provenance survives consolidation
KA-I09 paused-work semantics
KA-I10 public/private separation
KA-I13 local generated maintenance pattern
KA-I14 optional retrieval failure cannot bypass authority
KA-I15 live route/state/view health is reconstructable
KA-I16 capture does not imply authority
```

This remains synthetic support and receives no final qualification credit.

## 10. What is now still missing before target narrowing

Two frozen synthetic slices now cover foundational semantic mechanics and broader operational behavior. Continuing with increasingly elaborate synthetic fixtures would have diminishing value.

The next high-value evidence should move onto the **real repository in shadow mode**, without changing current authority. The candidate should be tested against a bounded real active slice for:

```text
real workstream/source declarations and route reconstruction
shadow-generated current_routing parity
shadow-generated deterministic current-state core versus real CURRENT_STATE content
shadow navigation/Knowledge Map projections
real governing-source activation on one consequential project procedure
real capture/promotion from an actual new reasoning increment
actual dependency-local maintenance touch count
```

The objective is not yet migration. It is to find where synthetic assumptions fail when confronted with today's repository structures, prose, exceptions and artifact families.

If the real-repository shadow slice requires broad hand-authored translation tables, duplicates unique current truth, or cannot reproduce the operational route without reading the existing global views as authority, Candidate 01 should be reconsidered before migration work.

```text
RESEARCH151=OPERATIONAL_SHADOW_V02_PASS_AFTER_REPAIR
FIRST_RUN_CHECKS=35_OF_38_PASS
FIRST_RUN_DEFECTS=3
SUBSTANTIVE_FIRST_RUN_DEFECTS=1_AUTHORITY_ORDERING
FINAL_FROZEN_ORACLE=PASS
H3_REOPEN=NO
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REAL_REPOSITORY_SHADOW_PARITY_AND_BEHAVIOR_SLICE
```
