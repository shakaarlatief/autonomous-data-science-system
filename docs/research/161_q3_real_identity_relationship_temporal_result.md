# Research 161: Q3 Real Identity / Relationship / Temporal Result

**Date:** 2026-09-14
**Status:** REAL Q3 SHADOW SUPPORT ESTABLISHED / H3 REOPEN TRIGGERS NOT FIRED / Q3 NOT FINALLY QUALIFIED / Q7 REAL PUBLIC-PRIVATE BOUNDARY NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q3 identity / relationship / temporal semantics
**Fixture freeze commit:** `5b53e906f64ee96457af5a14ff1fbe24368178b8`
**Exact real base:** `d8690d215e9701fc25d378a7d104aa6dbab10b2d`
**Scope:** Execute the exact Research 160 fixture, preserve the failed first implementation run and repair, verify all five real ADS semantic cases, measure architecture complexity, and apply the prospectively frozen H3/Object-Primary reopening rule.
**Authority:** Shadow subsystem evidence only. No current project authority changed and no final KA-R/KA-I pass is granted by this result.
**Declared references:** `research:160`, `research:159`, `research:144`, `research:143`, `checkpoint:505`

## 1. Exact execution provenance

```text
FIRST_RUN_RESULTS_V01.json
    SHA-256  34b37939ce34422bc924cee96a4a2d0c043dc746be025ee45a1b9440a2a1c93d

FIRST_RUN_COMPARISON_V01.json
    SHA-256  66139a91440d3435bc22f34f8dc298331bca7207eefe7ba0895f18bf219afae8
    1 / 4 aggregate oracle checks passed

RESULTS_V01.json
    SHA-256  3f722f778637bd67c86ce297ca559e93c8e2a6ef51ab9ff0d366d1eb6876b73e

FINAL_COMPARISON_V01.json
    SHA-256  ef074346b827c49f7d7f54a4e95f7ace00e9e5cf7bb44ba15e22a914e472d15c
    4 / 4 aggregate oracle checks passed

implementation repairs after first run  1
focused tests                           11 passed
full unit suite                         249 passed
```

The implementation does not read the separate oracle.

## 2. First-run failure and why it does not count as an H3 result

The first run failed Q3-R03 and therefore prospectively fired the `real_semantic_query_unresolvable` H3 reopening trigger. The failure was preserved rather than overwritten.

The defect was in the probe implementation, not in Candidate 01's semantic representation:

```text
incorrect first-run assumption
    the historical-intermediate Markdown source itself must contain
    Git rename commit b79d6ae...

actual frozen evidence contract
    the source carries original/current identity semantics
    Git history carries the rename commit provenance
```

The implementation already had a separate Git-history verification step. The single repair removed the invalid requirement that the Markdown body duplicate the Git commit hash. The fixture, shadow sources, real base and oracle were unchanged.

This distinction matters architecturally: Candidate 01 explicitly avoids copying carrier/history facts into every semantic source when Git can own that evidence honestly. Treating the missing duplicate as a semantic failure would reward exactly the duplication the architecture is trying to avoid.

## 3. Final real-case results

### Q3-R01: D-015 scoped supersession

PASS. One source-owned `REPLACE` relation resolves the external-source architecture uncertainty to D-033 while retaining the public-Git source-binary exclusion outcome. The recording and scoped-supersession dates remain selective rather than universal.

### Q3-R02: D-011 six-successor partial supersession

PASS. Six scoped source-owned relations resolve six implementation scopes while D-011 retains residual applicability elsewhere. The representation deliberately does not invent per-successor effective dates from the three aggregate dates preserved in the prose.

### Q3-R03: historical-intermediate carrier/identity repair

PASS after the implementation repair described above. The semantic milestone remains resolvable under a project-owned semantic ID; its current carrier is the historical-intermediate path; `Checkpoint 252` is retained only as original identity provenance; the canonical numeric Checkpoint 252 remains the spatial-rail checkpoint; and actual Git history proves the rename at `b79d6ae...`. No identity collision exists.

### Q3-R04: durable paused Cockpit workstream

PASS. The Cockpit remains one durable semantic workstream while `PAUSED`, with its exact future branch/head resume anchor preserved. Pausing does not require a separate central workstream object store.

### Q3-R05: MC-0013 epistemic-role transition

PASS. Message 001 remains `INDEPENDENT_CANDIDATE_DESIGN` at the exact substantive base while the thread's current state is `COMPARATIVE_ONLY` and Message 003 onward is `COMPARATIVE_REVIEW` after the explicit exposure trigger. Selective epistemic structure is sufficient; no universal event ledger is needed.

## 4. Complexity result

The final probe reports:

```text
shadow sources                                5
source-local relations                        7
selective temporal fields                     5
standalone relation sources                   0
standalone identity-transition sources        0
joint-authority sources                       0
general authoritative registries              0
duplicated authoritative relations            0
universally objectized participants           0
real semantic query failures                  0
```

All five frozen H3 reopening triggers are false.

```text
H3_REOPEN=false
```

This is meaningful because the fixture was deliberately selected to include dense scoped supersession, real carrier repair, durable workstream identity and epistemic transition. Candidate 01 handled them without creating standalone relation/transition objects or a general semantic registry.

## 5. What this says about Candidate 01 versus H3

The result strengthens the repository-native selective-profile hypothesis. It shows that several real ADS cases that look object-like can remain naturally represented as:

```text
rich semantic source
+ small source-adjacent structured declaration
+ Git/source evidence where that evidence naturally lives
+ derived lookup/resolution later
```

This is evidence against reopening H3 **for these observed cases**. It is not evidence that Object-Primary is impossible or permanently rejected.

The most important unresolved real transition classes are still:

```text
MERGE
SPLIT
TOMBSTONE
```

The repository sample does not currently provide equivalent real Candidate 01 implementation evidence for those transition classes. Synthetic lifecycle evidence remains weaker than a real case.

## 6. Q3 qualification disposition

All five Q3 KA-R mechanisms now have real Candidate 01 support at subsystem level:

```text
KA-R12  explicit epistemic role
KA-R15  relationship semantics
KA-R16  current state, history and selective temporal semantics
KA-R46  representation-independent continuity of identity
KA-R49  selective temporal and supersession semantics
```

The probe also materially supports KA-I04 and KA-I17, but it does not grant a final integrated pass to any item. Q3 still lacks complete real coverage of merge/split/tombstone and integrated authority-resolution behavior over those transitions.

Therefore:

```text
Q3_REAL_SUBSYSTEM_SUPPORT=PASS
Q3_FINAL_QUALIFICATION=PENDING
H3_REOPEN=NO
```

## 7. Next architecture uncertainty

Research 159's priority order remains useful after Q3. The next P0 architectural uncertainty is Q7 public/private authority boundary and degraded mode. All six Q7 items are currently synthetic-only.

The next test should therefore use the real layered public/private continuity boundary while avoiding any private-content leakage. It should test delegation, availability/unavailability semantics, ordinary public reconstruction, consequence-sensitive failure and public-view non-leakage. It must remain a shadow qualification and must not turn private data into public fixture content.

```text
RESEARCH161=Q3_REAL_SUBSYSTEM_SUPPORT_PASS
FIRST_RUN_DEFECT=PRESERVED_AND_REPAIRED_ONCE
FINAL_ORACLE=4_OF_4
REAL_CASES=5_OF_5
H3_REOPEN=false
Q3_FINAL_QUALIFICATION=PENDING
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=Q7_REAL_PUBLIC_PRIVATE_BOUNDARY_QUALIFICATION
```
