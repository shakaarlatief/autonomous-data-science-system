# Research 165: Q9 Migration / Authority-Switch / Rollback Result

**Date:** 2026-09-14
**Status:** Q9 REAL-BASE SHADOW SUBSYSTEM SUPPORT PASSED / ROLLBACK EXPORT PROVED / AUTHORITY SWITCH CORRECTLY BLOCKED / WHOLE-ARCHITECTURE EVIDENCE RECONCILIATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q9 migration / authority switch / self-hosting evolution
**Fixture freeze commit:** `9305692b5c474ba3b637e83366916622c5bf675e`
**Exact real base:** `fe40740e62dabc41e538b2b604e84f5e9167e92d`
**Scope:** Execute the frozen Q9 migration/rollback fixture, prove real-base semantic parity and path-independent identity, preserve reverse-reference compatibility, produce a legacy-compatible rollback export without touching live authority, keep the authority switch fail-closed, and prove Candidate 01 can preserve its own migration state.
**Authority:** Shadow subsystem evidence only. The existing continuity architecture remains operational authority. No production migration, reverse authority switch, or target selection occurs.
**Declared references:** `research:164`, `research:163`, `research:159`, `research:146`, `research:144`, `checkpoint:509`

## 1. Exact execution provenance

```text
FIRST_RUN_RESULTS_V01.json
    SHA-256  12a9ba9ea1e71c6a9886f3792e11c0bdb86669f9eb0fd74a1925eda8e5f43b75

FIRST_RUN_COMPARISON_V01.json
    SHA-256  9b4ac6b1e6ea6976e9d15f6b68c515574720a5eef00819090b1d67c6600e72c5
    10 / 10 frozen oracle checks passed

RESULTS_V01.json
    SHA-256  12a9ba9ea1e71c6a9886f3792e11c0bdb86669f9eb0fd74a1925eda8e5f43b75

FINAL_COMPARISON_V01.json
    SHA-256  2fbe04ac83f85816e967e0e660f248ff9d7bc59eaeea085ded08a1f58690840e
    11 / 11 checks passed

first run == final result          yes
implementation repairs             0
focused Q9 tests                  12 passed
exhaustive partitioned unit suite 271 / 271 passed
Python in-memory compile           PASS
```

The implementation never reads the oracle.

An initial focused-test invocation exceeded the Runtime Bridge 30-second execution ceiling because the test harness recomputed the complete probe in every test. The test harness was then made result-cached without changing probe behavior. A later oversized candidate-test partition also exceeded the command ceiling and was split into non-overlapping partitions. The exhaustive passing total is:

```text
147 + 12 + 53 + 27 + 32 = 271 / 271
```

These are execution-surface partitioning adjustments, not architecture or probe repairs.

## 2. Migration semantic parity

All ten frozen migration units pass exact legacy-to-successor parity:

```text
MU01 current checkpoint                  PASS
MU02 active development branch           PASS
MU03 active PR                           PASS
MU04 current semantic boundary           PASS
MU05 promoted integration branch         PASS
MU06 promoted integration commit         PASS
MU07 latest specification                PASS
MU08 latest experiment outcome           PASS
MU09 target architecture unselected      PASS
MU10 final qualified pass count          PASS
```

The result matters because these values are not read from a replacement global current-state registry. They resolve from the two natural successor semantic owners plus deterministic controls and the migration workstream.

## 3. Identity and migration provenance

The three shadow successor semantic IDs remain:

```text
WS-PKA-CURRENT
PROJECT-INTEGRATION-BOUNDARY
PKA-C01-MIGRATION
```

No semantic identity is a file path. All three sources remain `shadow_only=true` with candidate authority, and migration provenance is bound to exact real base `fe40740e62dabc41e538b2b604e84f5e9167e92d`.

This provides real-base migration evidence for the distinction between semantic identity and carrier identity without promoting a central semantic registry.

## 4. Reverse-reference compatibility

The exact-base reverse-reference measurements reproduce the frozen baseline:

```text
docs/current_routing.json   115 reference lines
docs/CURRENT_STATE.md       121 reference lines
docs/CONTINUITY.md           98 reference lines
```

Candidate 01 does not require those paths to disappear at migration time. The first two remain compatibility export targets; `CONTINUITY.md` remains an authored compatibility surface.

```text
broken reverse-reference targets = 0
```

This supports the migration principle that semantic ownership may move while established compatibility paths remain available during transition.

## 5. Rollback exporter proof

The implementation generated a temporary isolated legacy-compatible tree from successor state. It did not overwrite live authority files.

The generated routing manifest was exactly equal to the frozen Checkpoint 508 routing authority. The generated compact `CURRENT_STATE.md` contained the exact fragments required by the existing legacy routing contract. Checkpoint 508 was materialized into the temporary export tree from the frozen real base.

The existing unmodified validator then returned:

```text
Current routing consistency: PASS
checkpoint=508
checked_branch=v1-source-vault-bootstrap-resume
active_branch=v1-source-vault-bootstrap-resume
active_pr=none
promoted=v1-frontend-spike@2480109fadeee1e480ef03b82e335aacdf9adf91
latest_specification=027
latest_outcome=INCOMPLETE
current_boundary=project-knowledge-migration-rollback-shadow-next
```

Live `docs/current_routing.json` and `docs/CURRENT_STATE.md` were hash-checked before and after the export.

```text
routing exact parity                 PASS
legacy validator                     PASS
live authority mutation detected     false
rollback compatibility path count    2
```

This is materially stronger than relying on Git revert alone. It shows that the successor representation can regenerate a legacy representation understood by the existing continuity validator for the tested migration-critical slice.

## 6. Authority switch remains correctly closed

Even with rollback proof and public repository integrity passing inside the probe, the switch gate returns:

```text
allowed                       false
current operational authority CURRENT_CONTINUITY_ARCHITECTURE
successor authority state     SHADOW_ONLY
authority switch requested    false
```

The explicit blockers are:

```text
FINAL_QUALIFICATION_INCOMPLETE
TARGET_NOT_SELECTED
OWNER_TARGET_ACCEPTANCE_ABSENT
```

The experimental protocol independently forbids switching authority. Therefore neither a successful migration shadow nor a successful exporter can accidentally promote Candidate 01.

## 7. Self-hosting evolution

Candidate 01 successfully preserves its own migration as a semantic workstream. From the shadow sources alone, the probe reconstructs:

```text
migration phase              M6_SHADOW_RECONCILIATION
parent                       WS-PKA-CURRENT
current authority            CURRENT_CONTINUITY_ARCHITECTURE
successor state              SHADOW_ONLY
authority switch requested   false
next action                  prove parity, reverse-reference safety, lossless export,
                             switch blocking and self-hosted continuation
```

The migration workstream is also linked as an active child of the Research 124 workstream. This gives bounded real-base support for KA-R45 without claiming the successor is already operational authority.

## 8. Q9 qualification disposition

The result materially supports all six Q9 items:

```text
KA-R19  one explicit project-development authority
KA-R43  migration preservation and identity reconciliation
KA-R44  old authority remains until successor qualification
KA-R45  self-hosting evolution
KA-I08  old continuity remains operational until explicit qualified switch
KA-I17  semantic continuity is not forced to equal carrier continuity
```

Q9 is **not finally qualified**. This probe demonstrates a bounded shadow migration slice, not a complete production migration of all accepted project knowledge and not an actual reversible authority transition. Final switch evidence cannot exist before target selection, full qualification and owner acceptance.

The descriptive Candidate 01 evidence coverage now becomes:

```text
items with synthetic-or-better evidence   58 / 67
items with some real-repository evidence  49 / 67
final qualified passes                     0 / 67
```

## 9. What should happen next

Research 159's original P0 sequence has now executed three major architecture-level falsification targets after its audit:

```text
Q3 real identity/relationship/temporal       executed
Q7 real public/private boundary              executed
Q9 migration/rollback shadow                 executed
Q10 integrated qualification program         still pending
```

Before starting another isolated subsystem probe, the project should **reconcile the whole evidence field again**. Q3, Q7 and Q9 changed the maturity distribution substantially. The next experiment should be chosen from the remaining selection blockers using the updated evidence, not automatically inherited from Research 159.

```text
RESEARCH165=Q9_SHADOW_SUBSYSTEM_SUPPORT_PASS
FIRST_RUN=10_OF_10
FINAL_COMPARISON=11_OF_11
MIGRATION_UNITS=10_OF_10
ROLLBACK_EXPORT=PASS
LEGACY_VALIDATOR=PASS
LIVE_AUTHORITY_MUTATION=false
AUTHORITY_SWITCH_ALLOWED=false
SELF_HOSTING=PASS
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_V02
```
