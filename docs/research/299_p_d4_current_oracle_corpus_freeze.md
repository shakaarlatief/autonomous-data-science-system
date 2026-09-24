# Research 299: P-D4 Current-Oracle Corpus Freeze Before Successor Design

**Date:** 2026-09-24
**Status:** P-D4 CORPUS FROZEN / SUCCESSOR NOT YET DESIGNED / FORMAL OLD-ORACLE REPLAY NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-D4
**Oracle family:** Current routing integrity
**Oracle source commit:** `3da817c7d9af9492d071801bec4e649baa0f48f4`
**Corpus:** `experiments/r8c_assurance_probe_v01/p_d4_oracle_corpus.json`
**Corpus working-tree SHA-256:** `889e86bed3a84ed39f7ace337b8e955aa852a0cd657e26f2041b7f4c6229436b`
**Scope:** Freeze the known-good, known-bad and mutation-generated corpus before any P-D4 successor oracle design or implementation.
**Authority:** Fixture freeze only. It does not select a successor mechanism, retire the current oracle, or authorize physical migration.

## 1. Why current routing is the selected oracle family

P-D4 asks whether a real current validation family with material accepted history can be retired through semantic parity rather than implementation/output preservation.

The current-routing family is suitable because it has all of the required properties:

- it protects live project routing and continuity rather than a toy surface;
- Research 106 explicitly states its semantic invariants;
- Research 107 preserves a real historical routing defect;
- later accepted states provide multiple real known-good snapshots;
- its current representation is intentionally transitional and already expected to become a compatibility surface rather than permanent target authority;
- a future successor therefore must preserve the invariants without inheriting the exact `docs/current_routing.json` + `CURRENT_STATE.md` mechanism.

The current oracle is frozen at `3da817c7...` and its Git-blob content SHA-256 is `0bdcb46c6d7d7971139e2f6eba39f89decb0303fa3a98d96fa8bcfcd0ec8cb0f`.

## 2. Independent corpus semantics

The corpus contains 11 cases: 4 semantically GOOD and 7 semantically BAD.

Historical cases:

```text
PD4-C01  real Research-107-era defect at 851ff497...       BAD
PD4-C02  canonical repository-integrity reconciliation      GOOD
PD4-C03  accepted W1 authority boundary                     GOOD
PD4-C04  accepted P-D2 result state                         GOOD
```

Mutation/malformed cases:

```text
PD4-C05  stale-but-agreeing active checkpoint               BAD
PD4-C06  routed checkpoint does not exist                   BAD
PD4-C07  machine/human live-state disagreement              BAD
PD4-C08  volatile checkpoint-number boundary label          BAD
PD4-C09  malformed promoted integration revision            BAD
PD4-C10  syntactically malformed routing payload            BAD
PD4-C11  unrelated-branch freshness specificity             GOOD
```

The semantic labels are not derived from a successor. They come from the accepted Research 106/107 contracts and the meaning of the mutations themselves.

## 3. Real historical defect

`851ff497...` is not an invented negative.

Research 107 independently records that state as containing:

```text
CURRENT_STATE/current_routing checkpoint 268 while checkpoint 269 exists
over-specific volatile current_boundary
```

The fixture binds the exact historical routing blob, CURRENT_STATE blob and complete checkpoint-path inventory for that commit.

## 4. Frozen semantic invariant pressure

The cases exercise these invariant families without deciding the successor representation:

```text
ROUTING_FACTS_PARSEABLE
ROUTE_TARGET_EXISTS
ACTIVE_CHECKPOINT_FRESH
BRANCH_SCOPED_FRESHNESS
ORIENTATION_AGREES
SEMANTIC_BOUNDARY_STABLE
INTEGRATION_REVISION_WELL_FORMED
```

These names are corpus semantics, not a successor schema.

## 5. Exact binding

Every historical/base snapshot stores:

```text
immutable Git commit
SHA-256 of docs/current_routing.json Git content
SHA-256 of docs/CURRENT_STATE.md Git content
ordered checkpoint-path inventory
checkpoint inventory SHA-256
```

Mutation cases then apply deterministic, explicit operations to one frozen good base rather than embedding a second uncontrolled copy of the fixture.

Structural validation recomputed every source blob and checkpoint inventory and returned:

```text
P-D4 corpus structural freeze validation PASS
cases 11
fixture_sha256 889e86bed3a84ed39f7ace337b8e955aa852a0cd657e26f2041b7f4c6229436b
```

## 6. Methodological boundary

Some exploratory materializability checks of selected historical commits occurred before this freeze to confirm the current oracle could be executed against reconstructed snapshots. They are not the formal P-D4 replay and did not involve any successor design.

The important anti-overfitting boundary is intact:

```text
CORPUS_FROZEN_BEFORE_SUCCESSOR_DESIGN=true
SUCCESSOR_DESIGNED=false
FORMAL_OLD_ORACLE_REPLAY_OBSERVED=false
```

The successor claims/warrants, translated representation and implementation must be authored only after this corpus is committed and frozen.

## 7. Required next sequence

```text
commit/push corpus freeze
-> formally replay frozen current oracle on all 11 cases
-> derive successor semantic claims/warrants from the frozen invariants
-> preregister any intentional semantic differences before successor execution
-> implement only enough successor behavior for the probe
-> include a translated-representation case
-> freeze harness before result observation
-> execute P-D4
```

## 8. Current state

```text
P_D4_CORPUS=FROZEN
P_D4_SUCCESSOR=NOT_DESIGNED
P_D4_FORMAL_REPLAY=NOT_RUN

COMPLETED_VALID_SCOPED_PROBES=6_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=P_D4_OLD_ORACLE_REPLAY_AND_SUCCESSOR_DESIGN
```
