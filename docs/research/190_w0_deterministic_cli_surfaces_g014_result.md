# Research 190: W0 Deterministic CLI Surfaces G014 Result

**Date:** 2026-09-18
**Status:** PKA-G014 ACCEPTED / DETERMINISTIC CLI SURFACES QUALIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179, with Research 185 retaining its G010 field-level refinement
**Prior accepted gate:** Checkpoint 538 / Research 189
**Initial G014 implementation commit:** `05dca1d6d3f71dfa19c0c166be83dc08ae6e9237`
**Accepted implementation base:** `eae343ac1f5c242b19d69f5c5c888cfe9b7bf0bd`
**Scope:** Accept the deterministic W0 command-line validation, rebuild, incremental refresh and freshness surfaces after adversarial review, generated-artifact write hardening, completion of all eight persistent W0 structural views, and complete post-repair regression qualification.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G014 only. It does not accept PKA-G015+, start W1, publish successor views as authority, overwrite compatibility authority, or switch operational authority.

## 1. Accepted G014 boundary

The accepted command surface is:

```text
python -m tools.project_knowledge validate
python -m tools.project_knowledge rebuild
python -m tools.project_knowledge refresh --changed-since <commit>
python -m tools.project_knowledge check-freshness
```

Specification 028 requires deterministic validation, rebuild and freshness surfaces with non-zero failure on hard defects. The additional `refresh` command is a thin CLI exposure of the already accepted G013 incremental-selection path and does not introduce a second refresh architecture.

The CLI remains an L4 transport/rendering boundary. Application semantics live below it in `services/cli_ops.py`; generation remains owned by the accepted G009/G013 machinery.

## 2. Deterministic command semantics

### validate

`validate` requires an explicit snapshot mode:

```text
COMMIT_SNAPSHOT
    requires --ref

WORKTREE_SNAPSHOT
    forbids --ref
```

Its result is deterministic JSON with:

```text
validation_scope = QUERY_INDEPENDENT
snapshot mode/status
exact source commit when committed
discovery counts
governed/noncanonical counts
ordered diagnostics
explicit deferred query-dependent checks
```

Hard validation defects return command failure and process exit code `1`. CLI argument-contract failures remain distinct argparse failures with exit code `2`.

The new semantic validation layer composes only checks that can be made without inventing an authority query, retrieval context, or current wall-clock instant. It reuses existing G006 identity and G008 workstream semantics where those semantics are query-independent, and preserves explicit deferment where temporal/query context is genuinely required.

For committed validation, schema interpretation is bound to the selected commit's exact project-knowledge schema closure. Checkout schema drift cannot silently redefine an older commit.

### rebuild

`rebuild` opens one exact committed snapshot, requires query-independent semantic validity, and rebuilds the complete persistent W0 view set through the accepted G009 generation path.

By default it is non-mutating:

```text
complete committed sources
-> build all persistent views
-> materialize in a temporary staging root
-> verify staged bytes
-> compare expected bytes with existing worktree artifacts
-> return deterministic diff/digest state
```

Repository output is written only with explicit `--write`.

### refresh

`refresh --changed-since <commit>` reuses the accepted G013 plan:

```text
previous exact commit
+ current exact commit
-> deterministic affected-view plan
-> rebuild affected views from complete current inputs
-> temporary staging/diff
-> optional explicit --write
```

No changed-file delta enters view compute and no persisted generated state is patched.

### check-freshness

`check-freshness` compares worktree materializations against a complete deterministic rebuild from one exact committed source state.

Each persistent view reports a deterministic status such as:

```text
FRESH
STALE
INVALID
MISSING
```

A command-level success requires every persistent view to be fresh.

## 3. Complete persistent W0 view contract

Independent acceptance review found that the first committed G014 implementation exposed only the accepted G009 demonstration inventory plus the G010 current-state core:

```text
source_inventory
current_state_core
```

That was insufficient for Specification 028. Research 179 and the physical architecture require eight persistent W0 structural artifacts.

The accepted repair registers exactly:

```text
docs/project_knowledge/generated/source_catalog.json
docs/project_knowledge/generated/identity_index.json
docs/project_knowledge/generated/authority_index.json
docs/project_knowledge/generated/workstream_graph.json
docs/project_knowledge/generated/subject_index.json
docs/project_knowledge/generated/risk_obligation_index.json
docs/project_knowledge/generated/current_state_core.json
docs/project_knowledge/generated/CURRENT_STATE_CORE.md
```

The original `source_inventory` remains a qualified G009 structural/test view but is not misrepresented as one of the eight production persistent W0 artifacts.

The repair adds deterministic restricted pure units for the missing structural views while retaining the same exact-Git implementation closure, isolated worker, deterministic serializer and manifest architecture established by G009.

## 4. Persistent-view semantics

The eight persistent views have deliberately bounded roles:

```text
source_catalog
    governed current canonical semantic sources and source/profile metadata

identity_index
    authored identity/history lookup and static transition closure
    over canonical plus accepted historical governed sources
    temporal cases remain explicitly deferred rather than guessed

authority_index
    deterministic authority candidate and relation inputs
    not a precomputed answer to an unspecified authority query

workstream_graph
    current canonical workstream nodes, dependencies, readiness and route projection
    static semantics cross-checked against the accepted G008 engine

subject_index
    deterministic navigation memberships from authored profile/kind/scope metadata

risk_obligation_index
    source-owned risk/reopen triggers and currently active procedural/resume obligations

current_state_core.json
    accepted compact G010 machine projection

CURRENT_STATE_CORE.md
    deterministic human-readable representation of the same G010 semantic core
```

The new `ViewInputSelector.authority_classes` contract defaults to canonical-only, preserving earlier G009/G010 behavior. Views that require accepted history opt in explicitly. The authority-class selector is bound into the deterministic manifest boundary and therefore also participates in G013 impact analysis.

Focused qualification proves a matching historical input selects the declaring view, while a nonmatching historical source does not create false impact.

## 5. Generated-artifact write boundary

Generated outputs remain non-authoritative and all repository writes are confined to:

```text
docs/project_knowledge/generated/
```

The generated I/O adapter rejects:

```text
canonical/out-of-root target paths
symlink targets
junction targets
non-file targets
unsafe parent components
```

Adversarial review found an additional hard-link hazard before acceptance. An existing generated-path hard link could make an in-place overwrite mutate another file through the shared inode.

The accepted writer therefore uses:

```text
same-directory temporary file
-> flush
-> fsync
-> os.replace(target)
```

This replaces the generated directory entry instead of mutating the pre-existing linked inode. The permanent regression proves the canonical hard-link target remains byte-identical.

Explicit `--write` also checks that every locally influential governed source class used by the production view set matches the selected commit before materialization and again after the generated writes. This currently includes canonical inputs and accepted historical inputs required by `identity_index`. Source drift fails with `MATERIALIZATION_SOURCE_DRIFT` rather than reporting a false successful publication.

## 6. Query-independent semantic validation

G014 adds an application-level validation composition above the base discovery/schema validator. Its purpose is to make hard repository defects visible through the CLI without pretending that every authority/time question can be decided globally.

Qualified checks include, among others:

```text
exact committed schema-closure availability
duplicate current semantic identity
identity-transition static structure and multiplicity
overlapping temporal identity claims
invalid temporal intervals
dangling authored relation targets
duplicate governing-procedure constraint identity
overlapping duplicate joint-authority sets where scope/action/time intersect
workstream dependency/context/resume-target structural defects
durable-evidence rejection for non-committed snapshots
public/private validation inherited from the accepted substrate
```

Temporal workstream or identity questions that genuinely require an evaluation instant are not silently resolved from the wall clock. Structural defects remain errors, while truly context-dependent evaluation is exposed as deferred information.

## 7. Independent adversarial review and repairs

The first G014 implementation was not accepted merely because its CLI tests passed.

Two important acceptance findings were repaired.

### 7.1 Generated hard-link alias hazard

A generated path could already be a hard link to another regular file. In-place replacement semantics would risk mutating the other path.

Accepted repair:

```text
temporary sibling + fsync + os.replace
```

Permanent qualification:

```text
direct hard-link attack
normal explicit materialization
canonical-path rejection
3 / 3 PASS
```

### 7.2 Incomplete production persistent-view registry

After the initial G014 commit, contract review compared the CLI production registry against Specification 028 and Research 179 and found that only two views were wired.

This was a contract-level defect even though the focused CLI behavior itself passed.

Accepted repair commit:

```text
eae343ac1f5c242b19d69f5c5c888cfe9b7bf0bd
Repair G014 persistent W0 view coverage
```

The repair:

```text
adds the seven missing persistent structural views around the already accepted current_state_core
keeps source_inventory as a non-production demonstration view
adds exact schemas/shape qualification for persistent outputs
cross-checks identity semantics against G006
cross-checks workstream semantics against G008
extends G009 input selection with explicit authority classes
extends G013 impact qualification for the authority-class selector
extends materialization source-drift protection to every influential governed input class
```

The first post-repair G013 run exposed two test issues, not new production defects: one historical test source did not satisfy the view's profile/path selector, and one implementation-drift probe assumed a byte fragment remained globally unique. Both tests were corrected to exercise their intended contracts. The exact repaired regressions then passed.

## 8. Collaboration provenance

The G014 implementation and acceptance work was carried out in interaction session `chatgpt-26` through the registered Runtime Bridge workspace.

ChatGPT performed the acceptance inspection, contract reconciliation, adversarial hard-link review, all-eight-view repair, cross-gate regression design, final qualification, repository reconciliation and gate disposition.

This record does not assert secondary-agent participation that is not durably evidenced by the G014 commit history.

## 9. Final verification

Implementation commits:

```text
05dca1d6d3f71dfa19c0c166be83dc08ae6e9237
Implement PKA-G014 deterministic CLI surfaces

eae343ac1f5c242b19d69f5c5c888cfe9b7bf0bd
Repair G014 persistent W0 view coverage
```

Focused qualification:

```text
G014 CLI                                      26 / 26 PASS
persistent W0 views                            5 / 5 PASS
architecture guards                           23 / 23 PASS
combined G014/persistent/architecture         54 / 54 PASS

G009 view framework                           53 / 53 PASS
G009 isolated execution                       76 / 76 PASS
G013 full/incremental refresh                  40 / 40 PASS
combined G009/G013 regression                169 / 169 PASS
```

Complete unit inventory:

```text
1,130 / 1,130 PASS
1130 passed in 958.43s
```

Additional gates:

```text
compileall                                  PASS
pre-documentation WORKTREE validation      PASS / 1,418 candidates / zero diagnostics / NON_COMMITTED
acceptance-document WORKTREE validation    PASS / 1,420 candidates / zero diagnostics / NON_COMMITTED
implementation COMMIT validation           PASS / 1,418 candidates / zero diagnostics / COMMITTED
implementation commit                      eae343ac1f5c242b19d69f5c5c888cfe9b7bf0bd
PUBLIC_REPOSITORY_INTEGRITY                PASS
git diff --check                           PASS
```

The default Windows user temporary directory is not reliably available inside the Runtime Bridge sandbox. Qualification therefore uses explicit repository-local pytest temporary roots. A read-only collect-only probe that omitted that controlled temp root failed before test collection with the known environment condition; no repository test executed in that probe.

All controlled qualification scratch directories were removed after their runs.

## 10. Gate disposition

```text
PKA-G001..PKA-G014   PASS
PKA-G015..PKA-G017   PENDING
W0                    IN PROGRESS
W1                    NOT STARTED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
SPECIFICATION_028=UNCHANGED
```

## 11. Next W0 work

The next bounded gate is PKA-G015:

```text
professional architecture documentation skeleton
+ version-controlled whole-architecture diagram source
```

G015 should document the architecture that is now implemented and qualified. It must not be used as a reason to start W1 early, publish successor views as authority, or switch the current continuity architecture.

```text
RESEARCH190=PKA_G014_ACCEPTED
PKA_G001_G014=PASS
PKA_G015_G017=PENDING
NEXT=PKA_G015_ARCHITECTURE_DOCUMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
