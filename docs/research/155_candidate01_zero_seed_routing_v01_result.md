# Research 155: Candidate 01 Zero-Seed Successor-Native Routing V0.1 Result

**Date:** 2026-09-14
**Status:** ZERO-SEED SUCCESSOR-NATIVE ROUTING PARITY PASSED ON FIRST RUN / CURRENT-STATE DECOMPOSITION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Execute the exact Research 154 zero-seed routing fixture after its public freeze, preserve first-run evidence, verify exact compatibility parity without global live-state generation inputs, and decide whether current routing is ready to move from semantic-design uncertainty into later migration qualification.
**Authority:** Shadow subsystem evidence only. Current continuity remains operational authority. No current routing/state file changes authority role in this research record.
**Declared references:** `research:153`, `research:154`, `research:144`, `research:145`, `checkpoint:499`, `path:docs/current_routing.json`

## 1. Exact execution provenance

```text
fixture freeze commit    e327d2a2f4843b99f1440c977b7ce6e5a108759f
real compatibility base  4da4cfecc052b2f339e14dba0e91525662c144b2

FIRST_RUN_RESULTS_V01.json
    SHA-256  cf0d4f9505ad8fdab0c54bf293e9022448239318516f9f2f88dcdab12a7dd5eb

FIRST_RUN_COMPARISON_V01.json
    SHA-256  986f2f82d8248fa038f24f02bdfc6428a06346bc59e1a5634bfe848d607cc414
    8 / 8 pass

RESULTS_V01.json
    SHA-256  cf0d4f9505ad8fdab0c54bf293e9022448239318516f9f2f88dcdab12a7dd5eb

first run == final result   yes
repair after first run      none
```

The implementation reads the frozen fixture but not the oracle.

## 2. Zero-seed generation result

Generation reads exactly four sources:

```text
SHADOW_WORKSTREAM_SOURCE.md
SHADOW_PROJECT_INTEGRATION_BOUNDARY.md
Specification 027 at the frozen real base
Checkpoint 192 at the frozen real base
```

Before generation completes it reads none of:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

Measured generation state:

```text
global live-state generation facts  0
forbidden target reads               0
manual successor source touches      2
broad project-control sources        0
```

Only after the complete routing object exists does the comparison phase open the frozen `current_routing.json` target.

## 3. Exact compatibility parity

The successor-native projection is byte-semantically equal as a JSON object to the frozen compatibility target:

```text
schema_version               1
current_checkpoint           498
active_development_branch    v1-source-vault-bootstrap-resume
active_pr                    null
promoted_integration_branch  v1-frontend-spike
promoted_integration_sha     2480109fadeee1e480ef03b82e335aacdf9adf91
latest_specification         027
latest_experiment_outcome    INCOMPLETE
current_boundary             project-knowledge-zero-seed-routing-shadow-next
```

```text
ROUTING_EXACT_PARITY=PASS
```

## 4. Ownership result

Every compatibility field now has one explicit successor semantic owner or deterministic source:

```text
active_development_branch
active_pr
current_checkpoint
current_boundary
    -> active workstream execution anchor

promoted_integration_branch
promoted_integration_sha
    -> Project Integration Boundary

latest_specification
    -> computed from Specification 027

latest_experiment_outcome
    -> computed from Checkpoint 192 governed result
```

The experiment therefore removes the three global-state migration facts and the branch experiment-context dependency that remained in Research 153's generation path.

## 5. What was manually migrated

Zero-seed **generation** does not mean zero migration effort. Two successor shadow sources had to be authored before the run:

```text
1  primary active workstream execution-anchor source
2  Project Integration Boundary source
```

Those sources were frozen before implementation and hash-checked by the generator. This is the correct migration accounting: the facts move once into natural successor owners, after which the derived routing surface no longer needs hand-maintained copies.

The prototype therefore supports this scaling relation:

```text
canonical fact changes
    -> edit its one natural owner
    -> regenerate routing

not

canonical fact changes
    -> separately edit workstream state + current routing + current state summaries
```

## 6. Broad project-control registry remains unnecessary in this slice

Exact parity is achieved with two narrow semantic profiles and two computed controls. No broad `PROJECT_CONTROL` object or central control registry is needed.

This is stronger evidence for the selective-source architecture than Research 153's seed-assisted parity. It is still a bounded slice, so the rejection remains provisional rather than universal.

## 7. Routing subsystem disposition

The routing problem is now materially different from the state before Research 153:

```text
semantic ownership                  explicit
current global live-state seed      eliminated from generation
compatibility view reconstruction   exact
first-run repair                    none
source-touch burden                 2 successor canonical sources
project-control registry            not needed
```

This is enough to treat **zero-seed routing derivation as supported at shadow-subsystem level**. It is not enough to switch authority because the shadow sources are not yet production canonical sources and rollback/migration qualification has not run.

## 8. Verification

```text
frozen fixture/oracle hashes          PASS
shadow source hashes                   PASS
real source/target hashes              PASS
first-run oracle comparison            8 / 8
first run == final                     yes
focused tests                          8 passed
full unit suite                        227 passed in 12.66s
Python in-memory compile               PASS
forbidden generation reads             0
global live-state generation facts     0
routing exact parity                   PASS
```

## 9. Requirement-evidence interpretation

This result materially strengthens evidence for:

```text
KA-R06 explicit active-route reconstruction
KA-R21 derived state rebuildability
KA-R23 source-bound persistent derived views
KA-R25 durable workstream identity/state
KA-R31 bounded current reconstruction
KA-R33 dependency-local maintenance architecture
KA-R47 orthogonal derived views without copied truth
KA-I02 one project authority without competing derived truth
KA-I03 derived state contains no unique accepted truth in this routing slice
KA-I13 routine fact changes can be localized to natural owners
KA-I15 live routing/currentness is reconstructable
```

The machine qualification matrix records this as `REAL_REPOSITORY_ZERO_SEED_SUBSYSTEM_SUPPORT`, not final architecture-wide qualification.

## 10. Next major unresolved global surface

Routing is no longer the highest-value uncertainty. The next problem is `CURRENT_STATE.md`. Today's file intentionally mixes several roles accumulated by the current continuity architecture:

```text
current canonical/live facts
active route/orientation
accepted synthesis and rationale
recent checkpoint narrative
historical development detail
compatibility pointers
```

Candidate 01 cannot simply declare the whole file derived without first proving that no unique accepted truth disappears. The next stage must therefore decompose the real current-state surface into:

```text
A  canonical source-owned facts that need a natural home
B  deterministic current-state core fields
C  optional non-authoritative orientation narrative
D  historical/latent material that need not remain on mandatory bootstrap
E  unresolved items whose future role is not yet safe to assign
```

The decomposition should be machine-auditable and source-traceable before any generated replacement is attempted.

```text
RESEARCH155=ZERO_SEED_ROUTING_PASS
FIRST_RUN=8_OF_8
ZERO_SEED_ROUTING_PARITY=PASS
ROUTING_SUBSYSTEM_SHADOW_SUPPORT=YES
GLOBAL_LIVE_STATE_GENERATION_FACTS=0
BROAD_PROJECT_CONTROL_PROFILE=NOT_NEEDED_IN_SLICE
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REAL_CURRENT_STATE_DECOMPOSITION_AND_SOURCE_OWNERSHIP_AUDIT
```
