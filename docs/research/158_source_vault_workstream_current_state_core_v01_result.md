# Research 158: Source Vault Workstream + Current-State Core Shadow V0.1 Result

**Date:** 2026-09-14
**Status:** CURRENT-STATE-CORE SHADOW PASS ON FIRST RUN / SOURCE-VAULT A-CATEGORY GAP CLOSED IN SHADOW / WHOLE-ARCHITECTURE EVIDENCE RECONCILIATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Execute the exact Research 157 fixture after public freeze, preserve first-run evidence, verify the successor Source Vault workstream against real evidence, prove all must-preserve semantics remain recoverable, and test whether a compact current-state core can be generated without reading the current global state/routing targets.
**Authority:** Shadow subsystem evidence only. Current continuity remains operational authority.
**Declared references:** `research:157`, `research:156`, `research:155`, `research:144`, `checkpoint:502`

## 1. Exact execution provenance

```text
fixture freeze commit       cedaa770fbb7d45139ddcb39a3438b7578a7ae44
real comparison base        57df6561f506cba2c26222693d1403585fad23d2

FIRST_RUN_RESULTS_V01.json
    SHA-256  56c26acb345e164feeddf7a92101f3e332f62d34ece2eaf25a3a4bd6ba81cc64

FIRST_RUN_COMPARISON_V01.json
    SHA-256  da4425240a0df4a7b3b4e5212c4bed22262cb2aa44dcf7bf0a95136a299bfcf7
    12 / 12 pass

RESULTS_V01.json
    SHA-256  56c26acb345e164feeddf7a92101f3e332f62d34ece2eaf25a3a4bd6ba81cc64

first run == final result   yes
repair after first run      none
```

The implementation does not read the separate oracle.

## 2. Source Vault workstream result

The new shadow Source Vault workstream aligns with the real permanent-bootstrap runbook, Validation 003, Validation 004 and Checkpoint 274 across all frozen evidence checks:

```text
registry migrated / verified               PASS
Alembic head 0003_source_universe           PASS
SQLite table count 33                       PASS
20 / 20 prospective MATCH                  PASS
no compare mismatches                       PASS
ingestion NOT_STARTED                       PASS
resume target                               PASS
governing procedure                         PASS
working audit PENDING                       PASS
independent backup proof PENDING            PASS
clean restore/restored audit PENDING        PASS
Course 2 BLOCKED                            PASS
private dependency = RESOLVED_PRIVATE       PASS
```

The workstream is `PAUSED`, not completed or superseded. Its return condition is explicit project routing rather than the stale old statement that tied resume to Research 113 closing.

This closes the main A-category ownership gap identified by Research 156 **inside the successor shadow model**. It does not yet promote the shadow workstream source into current authority.

## 3. Must-preserve fidelity result

The fixture contains 23 semantic must-preserve items.

```text
required directly in compact core    15
source-owned drill-down only           8
recoverable after generation          23 / 23
missing                                0
```

The important result is that preservation does not require copying every detailed Source Vault fact into a global current-state object.

For example:

```text
core
    Source Vault = PAUSED
    resume target
    governing procedure
    ingestion status
    Course 2 gate

Source Vault workstream drill-down
    registry state
    Alembic head
    table count
    exact compare counts
    audit / backup / restore state
    private dependency classification
    full resume sequence
```

This is direct executable support for one-home-per-fact plus compact derived orientation.

## 4. Compact CURRENT_STATE_CORE result

The generated core contains:

```text
checkpoint 501
active branch / PR
promoted integration branch + exact SHA
latest specification 027
latest experiment outcome INCOMPLETE
active Research 124 stage
target architecture NOT SELECTED
current semantic boundary
paused Source Vault summary
```

Canonical serialized core size:

```text
871 bytes
```

The frozen real `CURRENT_STATE.md` comparison target is:

```text
283,023 bytes
```

Ratio:

```text
0.003077
≈ 0.31%
```

This number must **not** be interpreted as “99.69% of project knowledge can be deleted.” The comparison demonstrates that genuinely live global orientation can be tiny when history, procedures, evidence and detailed workstream state remain in their natural sources.

## 5. Real target parity

Generation reads zero current global targets and receives zero facts from them. After the core exists, comparison opens:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
```

Results:

```text
routing subset exact parity                 PASS
checkpoint marker                           PASS
Research 124 active-stage marker            PASS
target-not-selected marker                  PASS
Source Vault current-state marker           PASS
Source Vault resume target                   PASS
Course 2 blocked marker                      PASS
```

The old Research-113 Source Vault return-condition sentence is also detected as stale at the exact frozen base rather than being propagated into the successor source. Because the live current-state file remains operational authority, that stale wording was corrected at Checkpoint 502.

## 6. Verification

```text
first-run oracle checks                    12 / 12
first run == final                         yes
implementation repair                      none
focused tests                              11 passed
full unit suite                            238 passed in 20.99s
Python in-memory compile                   PASS
forbidden generation reads                 0
global-target generation facts             0
Source Vault evidence alignment            PASS
must-preserve recoverability               23 / 23
routing subset parity                      PASS
```

## 7. Architectural interpretation

The combined evidence from Research 153-158 now shows a coherent pattern on real ADS surfaces:

```text
current_routing
    can be a derived compatibility projection

current global state
    contains extensive history/navigation/copies that need not be global truth

paused Source Vault continuation
    fits a durable workstream semantic owner

compact live orientation
    can be generated from natural owners without losing the frozen must-preserve set
```

This is stronger than merely redesigning today's files. It supports a responsibility split in which the old files may eventually disappear or change form entirely. The experiment does not prescribe their survival.

## 8. Why the next step is not another legacy-file conversion

At this point, immediately moving to `CONTINUITY.md`, then `KNOWLEDGE_MAP.md`, then another existing file would risk turning architecture research into file-by-file refactoring. That would overfit Candidate 01 to the current implementation.

The next step should therefore return to the **whole architecture**. The evidence accumulated since Research 144 should be reconciled across the ten qualification clusters:

```text
Q1  bootstrap / reconstruction / discovery
Q2  authority resolution / action-contract fidelity
Q3  identity / relationship / temporal semantics
Q4  workstream continuation / concurrency
Q5  capture / promotion / consolidation fidelity
Q6  derived views / freshness / multi-axis projection
Q7  public-private boundary / degraded mode
Q8  scaling / maintenance economics
Q9  migration / authority switch / self-hosting evolution
Q10 qualification methodology / budgets
```

For each cluster, the project should distinguish:

```text
design-only support
synthetic evidence
real-repository seeded evidence
real-repository zero-seed evidence
remaining selection-blocking uncertainty
```

Only the highest-value unresolved **architectural** uncertainties should trigger further experiments, regardless of which current file happens to contain relevant evidence.

```text
RESEARCH158=CURRENT_STATE_CORE_SHADOW_PASS
FIRST_RUN=12_OF_12
MUST_PRESERVE=23_OF_23
CORE_BYTES=871
REAL_CURRENT_STATE_TARGET_BYTES=283023
GLOBAL_TARGET_GENERATION_FACTS=0
SOURCE_VAULT_A_GAP=CLOSED_IN_SHADOW
CURRENT_STATE_AUTHORITY_SWITCH=NOT_AUTHORIZED
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_AND_SELECTION_BLOCKER_AUDIT
```
