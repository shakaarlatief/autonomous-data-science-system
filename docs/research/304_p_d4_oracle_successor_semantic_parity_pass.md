# Research 304: P-D4 Oracle-Successor Semantic Parity PASS

**Date:** 2026-09-24
**Status:** P-D4 PASS / SEMANTIC ORACLE-SUCCESSOR PARITY DEMONSTRATED / NO TARGET AMENDMENT REQUIRED / CURRENT ORACLE NOT YET RETIRED
**Parent protocol:** Research 277
**Corpus freeze:** Research 299
**Old-oracle baseline:** Research 300 / PASS 11 OF 11
**Successor contract:** Research 302 / V0.2
**Harness freeze:** Research 303 / `7f0f035f38118d0f9671050ac6fb5fc3b938cc37`
**Probe:** P-D4
**Evidence:** `experiments/r8c_assurance_probe_v01/evidence/p_d4_run_001.json`
**Evidence SHA-256:** `5af23915934a5c752206044aff41c9131841f0037a089e6674bf9cc57964ecd7`
**Scope:** Reconcile the frozen P-D4 successor execution against the preregistered semantic parity and representation-translation discriminator.
**Authority:** Empirical probe result only. It does not itself retire the current oracle or authorize physical migration/cutover.

## 1. Result

The exact Research 303 harness returns:

```text
P_D4=PASS
old_oracle_matches=11/11
successor_matches=11/11
criteria=7/7 PASS
```

No corpus label, successor claim, threshold, control or input binding changed after execution.

## 2. Frozen corpus parity

The successor reproduces every pre-frozen GOOD/BAD disposition:

```text
PD4-C01 real historical routing defect           BAD  -> BAD
PD4-C02 canonical reconciliation                 GOOD -> GOOD
PD4-C03 accepted W1 authority boundary           GOOD -> GOOD
PD4-C04 accepted P-D2 state                      GOOD -> GOOD
PD4-C05 stale-but-agreeing active checkpoint     BAD  -> BAD
PD4-C06 missing routed checkpoint                BAD  -> BAD
PD4-C07 orientation/canonical disagreement       BAD  -> BAD
PD4-C08 volatile semantic boundary               BAD  -> BAD
PD4-C09 malformed integration revision           BAD  -> BAD
PD4-C10 malformed routing payload                BAD  -> BAD
PD4-C11 unrelated-branch freshness specificity   GOOD -> GOOD
```

The real Research-107-era defect is rejected by both branch-scoped freshness and stable-boundary claims.

## 3. Claim-local failure evidence

The successor does not merely return a generic failure. The frozen bad cases map to structured semantic claim violations:

```text
C05 -> PD4-SR3 branch-scoped freshness
C06 -> PD4-SR2 route target exists
C07 -> PD4-SR4 orientation semantic parity
C08 -> PD4-SR5 stable semantic boundary
C09 -> PD4-SR6 integration revision identity
C10 -> PD4-SR1 translatable structured facts
```

This is intentionally different from preserving the current checker stdout and return-code taxonomy.

## 4. Representation translation succeeds

The direct `ROUTING_ASSURANCE_SUBJECT_V1` good subject passes without reading:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
checkpoint filenames
scripts/check_current_routing.py
```

The paired direct stale subject fails exactly `PD4-SR3-BRANCH-SCOPED-FRESHNESS`.

This establishes the core P-D4 point: the semantic invariant can survive a representation change without retaining the current carrier mechanism.

## 5. Successor semantic-completeness controls

All four Research 302 controls fail their preregistered claim:

```text
active_pr = 0                         -> PD4-SR7
invalid work-line identity            -> PD4-SR7
latest_specification = '28'           -> PD4-SR8
empty latest_experiment_outcome       -> PD4-SR8
```

The successor classifier also passes its static independence check against direct references to the old checker, legacy routing/current-state paths, Git access and subprocess execution.

## 6. Oracle-retirement interpretation

The evidence supports:

```text
semantic parity is feasible
legacy carrier/output shape is not uniquely required
translated representation preserves the frozen invariants
WARRANT-F V0.2 amendment required by P-D4 = false
```

It does not support immediate deletion of `scripts/check_current_routing.py` or the live compatibility surfaces.

Research 263's migration-oracle obligation still applies: the current verifier remains a migration oracle until the eventual successor is productionized, cutover-qualified and explicitly released. The P-D4 harness is temporary evidence machinery, not production successor implementation.

## 7. Limits

The corpus is deliberately bounded. It establishes semantic parity across one real defect, three accepted historical states, six mutation/malformed negatives and one branch-specificity case, plus four successor-only type/identity controls.

It does not prove universal equivalence for every possible future routing state. Production realization still requires the normal target implementation, migration, cutover and ratchet processes.

## 8. Program state

P-D4 becomes the seventh decision-relevant probe with a valid/scoped result.

```text
P_H=INCONCLUSIVE / scoped provider evidence
P_D6=PASS
P_D3=PASS
P_D5=PASS
P_D1=PASS
P_D2=PASS
P_D4=PASS

COMPLETED_VALID_SCOPED_PROBES=7_OF_8
REMAINING=P_S

OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
FILE_LEVEL_MIGRATION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false
AUTHORITY_SWITCH_ALLOWED=false

NEXT=P_S_STOCHASTIC_CAMPAIGN_POWER_DESK_STUDY
```
