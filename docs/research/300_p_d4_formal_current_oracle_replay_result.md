# Research 300: P-D4 Formal Current-Oracle Replay Result

**Date:** 2026-09-24
**Status:** P-D4 OLD-ORACLE REPLAY PASS / 11 OF 11 SEMANTIC LABELS MATCH / SUCCESSOR DESIGN NEXT / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Corpus freeze:** Research 299 / `d1f9418b4315010b0b4e77cc5943921a5b0e76d0`
**Oracle family:** Current routing integrity
**Frozen oracle source:** `3da817c7d9af9492d071801bec4e649baa0f48f4:scripts/check_current_routing.py`
**Evidence:** `experiments/r8c_assurance_probe_v01/evidence/p_d4_old_oracle_replay_001.json`
**Evidence SHA-256:** `e46e42feec2edd4393697d88aa5c6f67436c0416b6926e9eddd961767b6bfaa0`
**Scope:** Run the frozen current oracle against the corpus committed before successor design and preserve its baseline sensitivity/specificity behavior.
**Authority:** Baseline oracle evidence only. No successor implementation or retirement decision exists yet.

## 1. Formal replay

The frozen current-routing checker was materialized from its exact Git blob at `3da817c7...` and executed against all eleven cases from the committed Research 299 corpus.

Result:

```text
FORMAL_OLD_ORACLE_REPLAY=PASS
cases=11
matched_semantic_labels=11
mismatches=0
```

Every GOOD case returned zero. Every BAD case returned non-zero.

## 2. Case outcomes

```text
C01 real Research-107 historical defect          BAD  -> nonzero
C02 canonical reconciliation                    GOOD -> zero
C03 W1 authority boundary                       GOOD -> zero
C04 P-D2 accepted state                         GOOD -> zero
C05 stale-but-agreeing active checkpoint        BAD  -> nonzero
C06 missing routed checkpoint                   BAD  -> nonzero
C07 human/machine disagreement                  BAD  -> nonzero
C08 volatile boundary                           BAD  -> nonzero
C09 malformed integration revision              BAD  -> nonzero
C10 malformed routing payload                   BAD  -> nonzero
C11 unrelated-branch freshness specificity      GOOD -> zero
```

This confirms that the frozen corpus is not merely semantically labelled; it is also a valid sensitivity/specificity baseline for the existing oracle.

## 3. Failure-mode diversity

The BAD corpus reaches multiple current-oracle failure paths:

```text
manifest-level hard rejection / return 2
cross-surface consistency violation / return 1
active-branch freshness violation / return 1
target-existence violation / return 1
```

The GOOD corpus includes three real accepted historical states plus the branch-scoping specificity case.

## 4. Successor still not designed during replay

The replay code only:

```text
materialized exact frozen Git artifacts
applied already-frozen deterministic mutations
executed the frozen current oracle
recorded outputs
```

No successor claims, schema, representation, translated carrier or replacement implementation existed during this replay.

Therefore the next stage can use the now-frozen semantic corpus and current-oracle baseline without allowing the successor to redefine the test set.

## 5. Next design obligation

The successor must now be derived from the semantic invariants, not from output-string cloning or source-code preservation.

It must make explicit which current-oracle requirements are:

```text
semantic invariants to preserve
compatibility-bound representation checks
transitional duplicate-surface synchronization obligations
or mechanism-specific behavior that may disappear after translation
```

Any intentional semantic difference must be preregistered before successor execution.

## 6. Current state

```text
P_D4_CORPUS=FROZEN
P_D4_OLD_ORACLE_REPLAY=PASS_11_OF_11
P_D4_SUCCESSOR=NOT_DESIGNED
P_D4_RESULT=NOT_AVAILABLE

COMPLETED_VALID_SCOPED_PROBES=6_OF_8
OWNER_ASSURANCE_DECISION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=P_D4_SUCCESSOR_CLAIMS_WARRANTS_AND_HARNESS_FREEZE
```
