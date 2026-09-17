# Research 186: W0 Current-State-Core G010 Result

**Date:** 2026-09-17
**Status:** PKA-G010 ACCEPTED / CURRENT-STATE-CORE PRODUCTION CONTRACT VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179 prospectively refined by Research 185
**Prior accepted boundary:** Checkpoint 534 / Research 185 / `e1d8fa96fff0a2558ba41e185c0855748fad6ded`
**Scope:** Record the accepted G010 production current-state-core generator, the Research 185 schema refinements, the frozen 23-item qualification crosswalk, two independent semantic defects found after Codex self-verification, their bounded repairs, and the final complete verification evidence.
**Authority:** Implementation evidence subordinate to Specification 028, Research 179 and Research 185. This record accepts PKA-G010 only. It does not accept PKA-G011+, publish successor views, start W1 migration, overwrite live compatibility paths, or switch operational authority.

## 1. Accepted G010 boundary

G010 implements the production `current_state_core` derived view through the accepted G009 framework. There is no separate current-state generation architecture.

The implementation extends the strict W0 input contracts exactly as frozen by Research 185:

```text
workstream.v1
    execution_anchor
        checkpoint
        development_branch
        pull_request
        current_boundary
    stage
        stage_id
        stage_state
    optional governing_procedure semantic identity
    optional orientation_milestones[] lifecycle controls
    current_anchor and execution_anchor mutually exclusive

project_boundary.v1
    promoted_branch + promoted_commit pair
    both required for PROJECT_INTEGRATION_BOUNDARY

semantic_source.v1
    outcome semantic identity
    required only for EXPERIMENT_RESULT
```

All refined objects remain closed under `additionalProperties=false`. No generic facts/value/payload registry, carrier-path identity, path-order selection rule, or compatibility-surface input was introduced.

## 2. Production current-state-core V1

The frozen production output contains:

```text
schema_version
active_workstream
    semantic_id
    state
    objective
    execution_anchor
    stage
integration_boundary
    semantic_id
    promoted_branch
    promoted_commit
current_specification
    semantic_id
current_experiment
    semantic_id
    outcome
paused_workstreams[]
    semantic_id
    state
    resume_target
    governing_procedure          when naturally owned
    orientation_milestones[]     when naturally owned
```

Required singular owners are selected by explicit profile/kind/state semantics. Zero or multiple candidates fail visibly. No path, filename number, input order, timestamp, lexical semantic-ID order or first-match rule selects authority.

Paused resumable workstreams are plural. Their output ordering by semantic identity is presentation-only and does not imply priority or authority.

## 3. G009 integration

`current_state_core_specification()` is one ordinary G009 `ViewSpecification` using:

```text
view_id               current_state_core
compute identity      current_state_core.v1
serializer            canonical_json.v1
rebuildability        DETERMINISTIC_BYTE_REBUILD
selector              complete canonical corpus
implementation basis  exact GIT_BLOB_BYTES_AT_COMMIT
implementation closure same audited 25-file G009 generation closure
```

The restricted compute unit and all helpers are loaded from exact committed source bytes without executing the containing module body. Full and selected generation use the same complete-input builder. The manifest binds exact source content, implementation closure, selection contract and compute/serializer execution identities.

Generated artifacts remain derived and non-authoritative. `WORKTREE_SNAPSHOT` cannot claim durable freshness.

## 4. Qualified fixture and 23-item crosswalk

Research 157/158 remain immutable historical behavioral evidence. G010 adds a separate strict production-schema-valid synthetic corpus plus a qualification-only semantic crosswalk.

The production fixture proves:

```text
15 / 15 compact-core must-preserve semantics represented
8 / 8 deeper must-preserve semantics remain exact-source recoverable
23 / 23 historical must-preserve items explicitly crosswalked
canonical expected current-state-core bytes  1,421
qualified size budget                       <= 2,048 bytes
historical Research 157 fixture hash         unchanged
historical Research 157 oracle hash          unchanged
```

The eight non-core Source Vault semantics remain drill-down knowledge owned by the existing Source Vault source/evidence set. They are not copied into the compact current-state core and no generic production field was added to carry them.

The production runtime does not read the historical oracle, import the Research 157 script, parse specification numbers from filenames, or use `docs/CURRENT_STATE.md`, `docs/current_routing.json`, `docs/CONTINUITY.md` or `docs/KNOWLEDGE_MAP.md` as generation inputs.

## 5. Independent defect 1: paused-workstream overconstraint

Codex's first complete implementation passed its 993-test self-verification, but independent ChatGPT review found a contract violation.

The initial `core_paused` projection required every paused resumable workstream to contain both:

```text
governing_procedure
orientation_milestones
```

Research 185 defines those declaration controls as optional. Specification 028's generic paused-workstream contract requires pause/return/resume continuity, not Source-Vault-specific orientation fields.

A valid Cockpit-like paused resumable workstream containing only its normal pause contract and semantic resume target therefore failed G010 with:

```text
CURRENT_STATE_MISSING_CONTROL
paused resumable workstream requires governing_procedure
```

This was an acceptance blocker because G010 projects all paused resumable workstreams, not only the Source Vault fixture workstream.

Repair:

```text
every paused resumable projection always emits
    semantic_id
    state
    resume_target

optional governing_procedure is projected only when authored
optional orientation_milestones are projected only when authored
```

The frozen output schema was corrected to make those two projected members optional while preserving their strict shapes when present. A permanent Cockpit-like regression now proves the generic Research 185 / Specification 028 contract remains valid.

## 6. Independent defect 2: governing-procedure type confusion

Independent review then replaced the canonical `governing_procedure.v1` owner with an ordinary canonical `semantic_source.v1` NOTE carrying the same semantic identifier.

The initial implementation still generated the core successfully because reference resolution checked only semantic-ID uniqueness, not the required semantic source profile.

That allowed a non-procedure source to satisfy a field explicitly typed as a governing-procedure identity.

Repair:

```text
when governing_procedure is present:
    referenced semantic identity must exist exactly once
    resolved source must have profile governing_procedure.v1
    otherwise fail CURRENT_STATE_REFERENCE_TYPE
```

A permanent adversarial regression now proves the wrong-profile substitution fails both generation and freshness visibly.

These repairs do not broaden G010 authority or change the Research 185 field contract.

## 7. Determinism and fail-visible behavior

G010 qualification covers:

```text
strict production fixture admission
frozen historical fixture/oracle hashes
exact 23-item crosswalk
15 core semantics + 8 source-owned semantics
repeated deterministic generation
full/selected equivalence
input permutation independence
semantic carrier movement
unrelated canonical input behavior
meaningful-input freshness changes
missing/duplicate/noncanonical singular role owners
missing/ambiguous semantic references
malformed execution anchors and stages
legacy current_anchor compatibility
current_anchor + execution_anchor rejection
duplicate/illegal milestones
integration-boundary promoted-pair rules
experiment outcome rules
minimal generic paused resumable workstream
wrong-profile governing-procedure substitution
poisoned compatibility surfaces
poisoned historical oracle
generated-view non-authority
WORKTREE non-durability
```

No compatibility path is overwritten and no persistent successor view is published by G010 acceptance.

## 8. Final verification evidence

After the independent repairs, the complete non-overlapping unit inventory was requalified:

```text
G010 current-state core                  76 / 76 PASS
G009 view framework                      53 / 53 PASS
G009 execution/adversarial               76 / 76 PASS
G006 identity                            63 / 63 PASS
G007 authority                          103 / 103 PASS
G008 workstreams                         89 / 89 PASS
substrate schemas                        86 / 86 PASS
substrate declarations                   70 / 70 PASS
substrate snapshots                      49 / 49 PASS
architecture guards                      19 / 19 PASS
inherited unit inventory                309 / 309 PASS
---------------------------------------------------
complete unit inventory                 993 / 993 PASS
```

Additional gates:

```text
compileall                              PASS
WORKTREE validation                    PASS / 1,409 candidates / zero diagnostics / NON_COMMITTED
accepted-HEAD COMMIT validation        PASS / 1,404 candidates / zero diagnostics / COMMITTED
accepted implementation base           e1d8fa96fff0a2558ba41e185c0855748fad6ded
PUBLIC_REPOSITORY_INTEGRITY            PASS
git diff --check                       PASS
```

The first WORKTREE validation during final review saw additional test-temporary files. All task-created G009/G010 review temporary directories were removed and validation was rerun to the expected 1,409-candidate boundary. The pre-existing access-restricted historical `.tmp/pytest-checkpoint-275/` and `.tmp/pytest-publication-276/` directories were intentionally left untouched.

## 9. Gate disposition

```text
PKA-G001..PKA-G010   PASS
PKA-G011..PKA-G017   PENDING
W0                    IN PROGRESS
W1                    NOT STARTED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
SPECIFICATION_028=UNCHANGED
RESEARCH_179=REFINED_BY_RESEARCH_185
```

## 10. Next W0 work

The next bounded gate is PKA-G011:

```text
capture validation enforces non-authority before explicit promotion
```

G011 must build on the accepted substrate without changing operational authority or starting W1.

```text
RESEARCH186=PKA_G010_ACCEPTED
PKA_G001_G010=PASS
PKA_G011_G017=PENDING
NEXT=PKA_G011_CAPTURE_VALIDATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
