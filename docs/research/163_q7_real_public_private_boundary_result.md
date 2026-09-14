# Research 163: Q7 Real Public / Private Boundary Result

**Date:** 2026-09-14
**Status:** REAL Q7 CROSS-REPOSITORY SUBSYSTEM SUPPORT PASSED / ZERO PRIVATE-VALUE LEAKAGE / Q7 NOT FINALLY QUALIFIED / Q9 MIGRATION-ROLLBACK SHADOW NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q7 public/private boundary / degraded mode
**Fixture freeze commit:** `fc62ef4722763cb73eee239c512d8ea4b95a5366`
**Scope:** Execute the exact Research 162 public/private fixture against frozen public authority and hash-bound real private companion evidence, preserve independent private-freshness failure, prove bounded-dependency/degraded behavior and non-leakage, and record the next architecture-level uncertainty.
**Authority:** Shadow subsystem evidence only. Public ADS remains sole project-development authority. No private companion mutation or freshness repair is performed by this result.
**Declared references:** `research:162`, `research:161`, `research:159`, `research:144`, `specification:025`, `specification:026`, `checkpoint:507`

## 1. Exact execution provenance

```text
PRIVATE_EVIDENCE_RECEIPT_V01.json
    SHA-256  d9c5648e0a62cb2b6fa6b96c4615e1513cff8d48fc5ff3179c8f5aa4abdf0a66

FIRST_RUN_RESULTS_V01.json
    SHA-256  de41c83b5181ef96bffe359a96e165430b0b350f17ed286c114cf9fc0010823b

FIRST_RUN_COMPARISON_V01.json
    SHA-256  f4e610203933c340bc9b7ee1c2e89584670cc558d41764d10d9fa6dcd0de03e7
    7 / 7 aggregate oracle checks passed

RESULTS_V01.json
    SHA-256  de41c83b5181ef96bffe359a96e165430b0b350f17ed286c114cf9fc0010823b

FINAL_COMPARISON_V01.json
    SHA-256  d7d65ff9265e381c981538f1124a1e1ece2c4d8f17346456809cee5e368fd2c5
    8 / 8 aggregate checks passed

first run == final result          yes
implementation repairs             0
focused Q7 tests                  10 passed
exhaustive partitioned unit suite 259 / 259 passed
Python in-memory compile           PASS
```

One monolithic full-unit invocation exceeded the Runtime Bridge command's 30-second execution ceiling. The suite was then run exhaustively in three non-overlapping file partitions: 147 + 80 + 32 = 259 tests, all passing. This is an execution-surface partition, not a reduced test set.

The implementation does not read the separate oracle.

## 2. Real private evidence boundary

The private companion was read directly through its already-qualified private workspace. Inside that private authority boundary, a model-free extraction bound the exact private repository head and exact private file hashes, parsed only the explicitly public-safe synchronization anchor, and scanned sensitive private strings before creating a public-safe receipt.

The public repository receives only:

```text
cryptographic evidence bindings
public-safe continuity checkpoint/commit
selected already-public-safe numeric/boolean Source Vault state
non-leakage counts
```

It does not receive the private workspace root, exact local storage coordinates, account identifiers, remote destination identifiers or URLs, or other private-only values.

```text
private strings examined in private boundary  19
private exact values leaked                    0
private paths serialized                       0
```

## 3. Real stale-anchor result is preserved, not repaired away

The frozen private companion anchor is older than the public Checkpoint 506 target. The existing public continuity checker was also exercised against a temporary **public-safe anchor projection** carrying only those two allowed anchor fields. It returned exactly:

```text
PRIVATE_CONTINUITY_INTEGRITY=FAIL
```

for checkpoint and commit mismatch.

That failure is valuable evidence. It is not repository corruption and it does not invalidate already resolved private facts. The experiment deliberately does **not** update the private anchor merely to make Q7 green.

The architecture must represent these truths simultaneously:

```text
public repository integrity                 independent claim
public RESOLVED_PRIVATE fact                still resolved
private companion currently accessible      yes in this experiment
private freshness against target             FAIL
private-required transition                  blocked
ordinary public continuation                 still usable
```

## 4. Scenario results

### Q7-S01: public-only continuation, private unavailable

PASS.

```text
private continuity   NOT_VERIFIED
public resolved fact preserved
task disposition     ALLOW_PUBLIC_CONTINUATION_WITH_PRIVATE_NOT_VERIFIED
```

This demonstrates the distinction between **private value resolution** and **current private verification**.

### Q7-S02: private-required transition, private unavailable

PASS.

```text
private continuity   NOT_VERIFIED
task disposition     BLOCK_REQUIRED_PRIVATE_UNVERIFIED
```

A required private dependency fails visibly rather than being guessed or silently bypassed.

### Q7-S03: private-required transition, accessible but stale real private anchor

PASS.

```text
private continuity   FAIL
task disposition     BLOCK_PRIVATE_CONTINUITY_FAIL
```

The public project-development authority remains unchanged and the public resolved-private classification remains intact.

### Q7-S04: public-safe projection over a real sensitive private payload

PASS. The private-side extraction used the hash-bound real payload internally while the public result contains only a whitelisted safe projection.

```text
private exact-value leaks   0
private path serialization  0
```

The stale continuity anchor remains `FAIL`; projection safety does not magically make the private repository current.

### Q7-S05: optional retrieval unavailable during low-risk public exploration

PASS.

```text
task disposition                    DEGRADED_OPTIONAL_NO_AUTHORITY_BYPASS
optional retrieval authority bypass false
```

Optional capability loss degrades discovery without weakening governing-authority safety.

## 5. Architectural conclusion

Candidate 01 can represent the real ADS public/private boundary with a small explicit policy plus an independent private-evidence/freshness receipt. The important semantic split is:

```text
RESOLVED_PRIVATE
    project knows the private fact exists/is resolved

PASS / FAIL / NOT_VERIFIED
    current verification status of the delegated private continuity surface
```

Those dimensions must not be collapsed.

The successful result also supports a professional cross-boundary pattern:

```text
private authority boundary
    inspect exact private state
    validate / redact locally
    emit only public-safe receipt

public architecture
    consume receipt
    preserve sole development authority
    make consequence-sensitive decision
```

This avoids both extremes: copying private state publicly and making public reconstruction depend on unrestricted private access.

## 6. Q7 qualification disposition

The real probe materially supports all six Q7 items:

```text
KA-R37  explicit public/private authority boundary
KA-R38  private-data non-leakage
KA-R39  bounded private dependency
KA-R42  consequence-sensitive degraded mode
KA-I10  public/private separation + non-leakage
KA-I14  optional retrieval failure cannot bypass authority safety
```

All six now have real Candidate 01 subsystem evidence. Q7 is **not** finally qualified because final integrated migration/continuation behavior has not yet been exercised under the successor as operational authority, and no authority switch has occurred.

Current descriptive Candidate 01 evidence coverage after Q3 + Q7 is:

```text
items with synthetic-or-better evidence   54 / 67
items with some real-repository evidence  45 / 67
final qualified passes                     0 / 67
```

## 7. Next architecture uncertainty

The next P0 selection blocker from Research 159 is Q9 migration / authority switch / self-hosting evolution. This is now more valuable than another subsystem-local semantic probe because Candidate 01 has accumulated substantial real evidence while still relying on the old continuity architecture as operational authority.

The next experiment should remain **shadow-only** and prove migration/rollback mechanics without switching authority. It should test at least:

```text
semantic parity from current authority into successor shadow
identity/provenance preservation
reverse-reference reconciliation
explicit old-authority retention during shadow migration
lossless rollback/export back to current representation
single-authority transition preconditions
self-hosting evolution state sufficient to coordinate its own later switch
```

A failed rollback or semantic-parity result must block selection rather than being patched around by prematurely changing authority.

```text
RESEARCH163=Q7_REAL_SUBSYSTEM_SUPPORT_PASS
FIRST_RUN=7_OF_7
FINAL_COMPARISON=8_OF_8
PRIVATE_VALUE_LEAKS=0
PRIVATE_PATH_SERIALIZATION=0
REAL_PRIVATE_FRESHNESS=FAIL_AS_EXPECTED_AND_PRESERVED
Q7_FINAL_QUALIFICATION=PENDING
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=Q9_MIGRATION_AUTHORITY_SWITCH_ROLLBACK_SHADOW
```
