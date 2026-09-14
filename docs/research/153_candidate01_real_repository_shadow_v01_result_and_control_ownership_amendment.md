# Research 153: Candidate 01 Real-Repository Shadow V0.1 Result and Control-Ownership Amendment

**Date:** 2026-09-14
**Status:** REAL-REPOSITORY SHADOW V0.1 PASS ON FIRST RUN / MIGRATION-SEED BURDEN EXPOSED / CONTROL OWNERSHIP AMENDED / ZERO-SEED SHADOW MIGRATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Execute the exact Research 152 real-repository shadow, preserve first-run evidence, distinguish genuine source-derived parity from explicit migration seeding, and amend Candidate 01's ownership model for live routing/control facts before any authority migration.
**Authority:** Real-repository shadow evidence and candidate-design amendment only. Current continuity remains operational authority. Requirements V0.2 remain frozen.
**Declared references:** `research:152`, `research:151`, `research:144`, `research:145`, `checkpoint:497`, `path:docs/CONTINUITY.md`, `path:docs/current_routing.json`, `path:docs/CURRENT_STATE.md`, `path:docs/KNOWLEDGE_MAP.md`

## 1. Exact execution provenance

Fixture/oracle were committed and pushed before implementation at:

```text
freeze commit         bca1210e3e2a9b97fab0b4e2c574f6192d9bb50a
source base commit    e10fd108330f2cf8d260a621ea59053aebd28291
fixture SHA-256       9e8cd2ce0be7ced69eabc246414bd9aa0f21b305e03efeffd81db86c222d42bc
```

The first executable run passed all 24 frozen comparison checks before any repair:

```text
FIRST_RUN_RESULTS_V01.json
    SHA-256  54e666aa5d42bb83b97e0ff2a8124bd6024dfd22ab71f2740bb87638ee0f50a3

FIRST_RUN_COMPARISON_V01.json
    SHA-256  2f31903e0de921c9b2df764eb617aad5425b5125e71b1eadc2c033c0c1d693dd
    24 / 24 pass

RESULTS_V01.json
    SHA-256  54e666aa5d42bb83b97e0ff2a8124bd6024dfd22ab71f2740bb87638ee0f50a3

first run == final result   yes
repair after first run      none
```

The final implementation reads zero comparison targets during generation. Comparison targets are opened only after the candidate projection exists.

## 2. Real source integrity and bounded generation

All 11 source-manifest blobs exactly match their frozen bytes and SHA-256 at `e10fd108330f2cf8d260a621ea59053aebd28291`.

Candidate generation reads seven non-target real sources:

```text
Research 144
Checkpoint 192
Checkpoint 496
CONTINUITY.md
Research 124
Research 151
Specification 027
```

Generation comparison-target reads:

```text
0
```

Only the later scoring phase reads:

```text
current_routing.json
CURRENT_STATE.md
KNOWLEDGE_MAP.md
```

This makes the parity evidence materially stronger than reading a target and reproducing it.

## 3. Real workstream reconstruction

The shadow route reconstructs:

```text
WS-R124 -> WS-C01 -> WS-REAL-SHADOW
```

`WS-OPS-V02` is correctly treated as a completed dependency rather than an active route node.

Three workstream units have obvious existing source homes, but the current `WS-REAL-SHADOW` unit required an explicit successor-style migration seed. This is the first real evidence that Candidate 01's workstream model fits the project semantically **but the current repository does not yet encode every live workstream as a machine-resolvable canonical workstream source.**

The result therefore supports the semantic model while exposing actual migration work.

## 4. Exact current-routing parity and what it does not prove

The generated shadow routing object exactly equals the real frozen `current_routing.json` at the base commit:

```text
schema_version               1
current_checkpoint           496
active_development_branch    v1-source-vault-bootstrap-resume
active_pr                    null
promoted_integration_branch  v1-frontend-spike
promoted_integration_sha     2480109fadeee1e480ef03b82e335aacdf9adf91
latest_specification         027
latest_experiment_outcome    INCOMPLETE
current_boundary             project-knowledge-real-repository-shadow-next
```

But exact parity must be decomposed by source origin. It is not evidence that all fields are already independently source-local.

### Independently recovered from real non-target evidence

```text
current_checkpoint
    parsed from real Checkpoint 496

latest_specification
    parsed from real Specification 027

latest_experiment_outcome
    parsed from Checkpoint 192's governed INCOMPLETE result

current_boundary
    reconstructed from Checkpoint 496's explicit NEXT boundary
```

### Experiment-context value requiring a future canonical owner

```text
active_development_branch
    supplied by the frozen experiment/base-branch context
    not yet recovered from a Candidate-01 canonical workstream declaration
```

### Explicit migration seed copied from today's global live-state authority

```text
active_pr
promoted_integration_branch
promoted_integration_sha
```

Therefore:

> **Routing parity passes, but zero-seed successor reconstruction has not yet been demonstrated.**

That distinction is central to honest migration qualification.

## 5. Ownership disposition for the migration-seeded control facts

The evidence does **not** justify a broad `PROJECT_CONTROL` registry/profile. The migration facts decompose naturally into two semantic homes.

### 5.1 Active branch and active PR belong to the primary active workstream anchor

Candidate 01 already gives workstreams a `current_anchor`. Real evidence now sharpens that profile. For the primary continuation route, the workstream's canonical state should be able to own:

```text
active_development_branch
active_pr or explicit no-active-PR state
current semantic boundary / resume anchor
relevant checkpoint/ref when needed
```

The compatibility `current_routing.active_development_branch` and `active_pr` fields can then be **derived projections** from the primary active route rather than independent project-wide authority.

This also scales better to future concurrency. The successor representation may preserve several workstream-local PR anchors even if the old compatibility view exposes only the primary route's single `active_pr`.

### 5.2 Promoted branch + SHA form one project-wide semantic unit

`promoted_integration_branch` and `promoted_integration_sha` are not naturally properties of the current Research 124 workstream. Together they state one durable project-wide fact:

```text
PROMOTED_INTEGRATION_BOUNDARY
    branch
    exact promoted commit
    promotion provenance/evidence
    current/superseded state
```

Candidate 01 is therefore amended with a narrow **Project Integration Boundary** profile/semantic unit. This is not a general project-control store. It owns only the promoted integration boundary because that fact has project-wide continuity and no more natural workstream owner.

Routing and current-state views derive branch/SHA from this single canonical source.

## 6. Why the broad PROJECT_CONTROL profile is rejected for now

A broad global project-control source would be easy to create, but it would recreate the exact architectural gravity Candidate 01 is trying to avoid. The current real evidence can be decomposed without it:

```text
active branch / PR / route anchor
    -> primary active workstream

promoted integration branch + SHA
    -> Project Integration Boundary semantic source

latest specification
    -> derived from specification identity/index

latest scientific outcome
    -> derived from governed experiment result state

current checkpoint
    -> current route/checkpoint evidence

current boundary
    -> active workstream continuation semantics
```

A broad `PROJECT_CONTROL` profile should reopen only if later real cases reveal several unrelated project-wide control facts with no honest narrower semantic owner and repeated coordination cost makes the narrower decomposition worse.

## 7. Real governing action-contract result

The shadow contract B01..B10 aligns with the actual ordered `Required new-session reconstruction` section in `CONTINUITY.md`. All ten source tokens are present in source order.

The good bootstrap plan passes.

The deliberately bad plan:

```text
omits B03 = direct CONTINUITY read
emits B05 before B04
```

fails visibly with exactly those defects.

This is the first Candidate 01 action-contract result over an actual current ADS governing procedure rather than a synthetic procedure.

### Limitation

The structured B01..B10 contract was authored as a migration shadow and checked against the existing prose. Candidate 01 still needs a real migration path that places the structured contract into the canonical governed source without creating duplicate normative truth.

## 8. Current-state semantic parity

Without using `CURRENT_STATE.md` during generation, the later comparison confirms all five frozen markers:

```text
checkpoint 496
active development branch
Research 124 active stage
next bounded real-repository shadow boundary
target architecture remains unselected
```

This is useful but intentionally not full-document equivalence. Today's `CURRENT_STATE.md` contains extensive historical/editorial material and unique live synthesis accumulated under the existing architecture. Candidate 01 has not yet demonstrated that the whole document can become a derived current-state core safely.

That is now the largest remaining global-surface decomposition problem.

## 9. Knowledge Map / navigation result

The candidate generates a small multi-axis navigation projection over three real artifacts. The later comparison confirms all three are discoverable in the real `KNOWLEDGE_MAP.md`.

This supports the derived-navigation model, but the subject declarations were authored in the shadow fixture rather than extracted from existing source metadata. Therefore this experiment demonstrates **projection feasibility**, not zero-touch Knowledge Map migration.

A later migration must place subject declarations at natural source homes or derive them from an accepted structured source contract.

## 10. Real capture boundary

`REAL-CAP-01` remains `candidate` throughout the run. Merely discovering a real migration insight in the experiment does not make the captured text authoritative.

This Research 153 reconciliation is the explicit promotion boundary for the accepted conclusions from that capture: the accepted design conclusion is not the raw sentence itself, but the narrower ownership amendment in Sections 5-6.

## 11. Migration burden measured by this slice

The real slice exposes several different kinds of migration work that should not be conflated:

```text
semantic-unit migration seed
    1 active workstream unit currently lacks a dedicated Candidate-01-style source

current global control facts explicitly copied for parity
    3 facts in the frozen fixture

additional ownership refinement exposed by self-review
    active development branch must move into the primary workstream anchor too

new narrow canonical semantic unit
    1 Project Integration Boundary source for promoted branch + SHA

structured governing-contract migration
    1 real procedure, 10 constraints, currently shadow-authored and prose-aligned

subject/navigation declarations
    3 source declarations in the bounded navigation slice
```

These counts are not repository-wide estimates. They are direct migration work observed in one bounded real slice.

## 12. Verification

```text
fixture hash guard                       PASS
all 11 exact base-source hashes          PASS
generation target reads                  0
first-run oracle checks                  24 / 24
first run == final result                yes
first-run repair                         none
focused real-shadow tests                11 passed
full unit suite                          219 passed in 10.89s
Python in-memory compile                 PASS
routing exact parity                     PASS
CONTINUITY B01..B10 alignment            PASS
comparison targets opened only afterward PASS
```

## 13. Evidence interpretation

This is stronger than the synthetic slices because it binds Candidate 01 mechanisms to actual repository artifacts and an actual governing procedure. It adds real-shadow support for mechanisms associated with:

```text
KA-R02 stable project-controlled bootstrap
KA-R05 progressive source descent
KA-R06 active route reconstruction
KA-R08 reconstruction/authority receipts
KA-R09 consequential contract fidelity
KA-R18 provenance/source basis
KA-R20 authority classes for derived/candidate surfaces
KA-R23 source revision/freshness binding
KA-R25 explicit workstream identity/state
KA-R35 human/model inspectability
KA-R47 multi-axis navigation without copied truth
KA-R48 capture does not imply promotion
KA-I02 one explicit authority / derived targets remain comparisons
KA-I03 generated views contain no unique accepted truth in this slice
KA-I05 real governing contract survives into plan checking
KA-I11 reconstruction does not rely on prior chat
KA-I15 live route/currentness can be projected from durable evidence plus explicit migration seeds
KA-I16 capture does not imply authority
```

No item receives final qualification credit yet. Most importantly, the experiment proves parity only **with explicitly measured migration seeds**, not after those seeds have been relocated into successor canonical sources.

## 14. Next empirical step

The next step should not be another broad architecture dialogue and should not yet be target selection. It should close the exact real gap this experiment found:

> **Create shadow successor-native canonical sources for the primary active workstream anchor and Project Integration Boundary, move the frozen migration-seeded facts into those sources, and prove exact current-routing reconstruction with zero global live-state migration facts in the generation path.**

The same slice should keep the real `CONTINUITY` contract and navigation declarations, then quantify manual/source touch burden.

After zero-seed routing parity, the next major problem is full `CURRENT_STATE.md` decomposition into:

```text
canonical source-owned facts
deterministic current-state core
optional non-authoritative orientation narrative
historical material that should leave the mandatory active surface
```

```text
RESEARCH153=REAL_SHADOW_V01_PASS
FIRST_RUN=24_OF_24
ROUTING_EXACT_PARITY=PASS_WITH_MEASURED_MIGRATION_SEEDS
BROAD_PROJECT_CONTROL_PROFILE=REJECTED_FOR_NOW
WORKSTREAM_ANCHOR_OWNS_ACTIVE_BRANCH_PR=AMENDED
PROJECT_INTEGRATION_BOUNDARY_PROFILE=ADDED
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=ZERO_SEED_SUCCESSOR_NATIVE_ROUTING_SHADOW
```
