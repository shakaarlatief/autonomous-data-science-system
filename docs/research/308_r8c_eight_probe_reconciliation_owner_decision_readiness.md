# Research 308: R8-C Eight-Probe Reconciliation and Owner-Decision Readiness

**Date:** 2026-09-24
**Status:** WARRANT-F V0.2 OWNER-DECISION-READY / RECOMMEND ACCEPT / OWNER DECISION NOT YET RECORDED / NO PHYSICAL MIGRATION
**Parent candidate:** Research 276 WARRANT-F V0.2
**Probe protocol:** Research 277
**Final probe result:** Research 307
**Scope:** Reconcile all eight decision-relevant probes against Research 277's owner-decision rule, preserve all scoped limitations and migration obligations, and state the evidence-based owner recommendation without making the owner's decision.
**Authority:** Decision-readiness synthesis only. Only the project owner may choose ACCEPT / AMEND / REOPEN.

## 1. Decision-readiness test

Research 277 requires WARRANT-F V0.2 to satisfy all of:

```text
all eight probes reconciled
no unresolved AMEND result
no active HARNESS_INVALID result
every INCONCLUSIVE result explicitly scoped
current-debt-only findings translated into downstream obligations rather than target restrictions
```

Observed:

```text
all eight probes reconciled                  PASS
unresolved AMEND results                    0
active HARNESS_INVALID results              0
scoped INCONCLUSIVE results                 1 / P-H
unscoped INCONCLUSIVE results               0
current-state findings converted to target restrictions improperly  0
```

Historical harness-invalid attempts remain preserved in the record, especially P-D3 Attempts 001-003 and P-D2 Attempt 001, but each was prospectively repaired before the valid result. They are not active unresolved probe outcomes.

Therefore:

```text
OWNER_DECISION_READY=true
```

## 2. Complete probe disposition

| Probe | Final disposition | Architecture effect |
|---|---|---|
| P-H current host capability | INCONCLUSIVE, scoped | Current active host-settings read capability remains unknown; target provider/workflow remains open and must be qualified before dependent cutover. No target amendment. |
| P-D6 executor capability/trust separation | PASS | Assurance semantics remain executor-neutral and capability/trust aware. Actor/model/surface labels do not own trust semantics. |
| P-D3 boundary independence | PASS | Product can remain independent of Project runtime correctness; JW1 can remain independent of Engineering runtime correctness for representative target-shaped behavior. |
| P-D5 adapter fidelity | PASS | Product/JW1 may retain native result semantics; consumer-side Engineering adapters map them to neutral evidence without reverse dependency. |
| P-D1 warrant proportionality | PASS | Selective first-class claims and scoped warrants are viable without one claim per test; partial warrant status remains explicit. |
| P-D2 base-revision ratchet | PASS | Material weakening is distinguishable from strengthening/neutral lineage evolution; self-weakening and stale batch binding are rejected. |
| P-D4 oracle successor | PASS | Current routing invariants can survive representation change; legacy carrier/output shape is not a target requirement. Current oracle remains a migration oracle until explicit qualified release. |
| P-S stochastic campaign power | PASS | A future paired, item-clustered, preregistered campaign is feasible; current two-item evidence remains OBSERVE_ONLY for decision-grade stochastic BLOCK. |

Seven probes therefore return PASS and one returns explicitly scoped INCONCLUSIVE.

No probe returns AMEND.

## 3. Why P-H does not block semantic architecture acceptance

P-H did not establish whether today's GitHub installation can realize the eventual target trust/enforcement properties because the active read surface could not inspect current host settings.

Research 277 explicitly permits an INCONCLUSIVE result when its limits are scoped and it is not used as positive support for an unavailable decision-grade claim.

P-H is scoped exactly that way:

```text
CURRENT_GITHUB_T2_CAPABILITY=UNKNOWN
TARGET_PROVIDER_SELECTED=false
TARGET_PROVIDER_REQUIREMENTS_UNCHANGED=true
HOST_OR_PROVIDER_QUALIFICATION_REQUIRED_BEFORE_DEPENDENT_CUTOVER=true
```

Accepting WARRANT-F V0.2 therefore does not accept GitHub, GitHub Actions, the current Git identity model or any current workflow as the target.

## 4. What the empirical program changed

The probe program did not require a semantic amendment to WARRANT-F V0.2.

It did sharpen several implementation and migration obligations:

```text
host/provider realization
    must later demonstrate the required capability, isolation, subject binding, producer authenticity and policy provenance

current routing oracle
    remains active migration evidence until a production successor is implemented, shadow-qualified and explicitly released

stochastic BLOCK evidence
    cannot reuse the historical Prototype V0 two-item corpus as decision-grade generalization evidence
    must use preregistered item-level power/sample-size design and private confirmatory items

warrant claims
    remain scoped; broad claims with narrower witness evidence remain PARTIALLY_WARRANTED

consumer-native result formats
    may change; Engineering owns neutral adaptation rather than imposing one result format upstream

execution planning
    must select by explicit capability/trust properties rather than model/tool name
```

These are realization constraints and migration obligations, not reasons to preserve the current repository mechanism.

## 5. What remains intentionally unselected

Owner acceptance of WARRANT-F V0.2 would still not select:

```text
branch model
PR model
merge queue
direct-push policy
GitHub Actions
CI provider
runner provider
host-protection mechanism
identity provider
status/check publisher
exact Python test framework
exact evidence store
deployment provider
release topology
current current_routing/CURRENT_STATE carrier design
current repository-integrity aggregate implementation
```

This preserves the owner's all-level from-scratch design freedom.

## 6. What ACCEPT would accept

An owner `ACCEPT` would accept WARRANT-F V0.2 as the semantic assurance architecture direction, including Research 276's reconciled WF-A1 through WF-A36 rules and the R8A Engineering-environment amendment candidate.

That Engineering amendment is:

```text
project/engineering/
    independent Python project
    independent lock

no Product+JW1 co-installation into Engineering
JW1 invoked through CLI/result contract rather than path dependency
small assurance-kernel runtime dependency budget
one Engineering-owned bootstrap entry prepares required environments
remove any root Python project unless an independent repository-wide runtime justification exists
```

Acceptance still does not authorize moving files or changing operational authority immediately.

## 7. What ACCEPT would unblock

After owner acceptance, the next work is concrete realization and governed migration planning.

That includes:

```text
reconcile/amend Specification 028 where the accepted R8-C architecture changes its implementation contract
unhold and design AO-10 under the accepted assurance/control-evidence semantics
derive the concrete Engineering/verification/delivery realization from the accepted semantic architecture
qualify provider/host realization rather than inheriting today's setup
design evidence publication/storage satisfying non-self-mutation and public/private rules
implement and qualify gate evaluator, affected-scope fallback, exact-result promotion and adapters
retain current migration oracles until explicit successor release criteria are satisfied
only then progress toward file-level/physical migration and authority-switch gates
```

Realization-stage probes remain downstream as Research 276 already specified.

## 8. Recommendation

The evidence supports `ACCEPT` rather than `AMEND` or `REOPEN`.

Reason:

```text
the candidate survived every decision-relevant semantic discriminator
no probe exposed a target-architecture defect
the only inconclusive result concerns current provider observability, which the architecture already treats as an open realization question
the stochastic probe supports the proposed campaign discipline without overstating the existing evidence
the oracle probe shows that semantic invariants can be preserved without retaining current mechanisms
the ratchet, boundary, adapter, warrant and executor probes each support their corresponding architectural seams
```

`AMEND` would currently require introducing a change not demanded by the frozen empirical program.

`REOPEN` would require evidence that the fundamental assurance model or prior architectural boundary is unsound; no such evidence was observed.

Therefore the recommendation is:

```text
RECOMMEND_OWNER_DECISION=ACCEPT
```

## 9. Decision boundary

This research does not record owner acceptance.

The owner may still choose:

```text
ACCEPT
AMEND
REOPEN
```

Until that explicit choice:

```text
WARRANT_F_V0_2=OWNER_DECISION_READY
OWNER_ASSURANCE_DECISION=PENDING
SPECIFICATION028=UNCHANGED
AO10=HELD
FILE_LEVEL_MIGRATION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false
AUTHORITY_SWITCH_ALLOWED=false
```

## 10. Current state

```text
R8C_DECISION_RELEVANT_PROBES=8_OF_8_RECONCILED
R8C_UNRESOLVED_AMEND=0
R8C_ACTIVE_HARNESS_INVALID=0
R8C_SCOPED_INCONCLUSIVE=P_H_ONLY

WARRANT_F_V0_2=OWNER_DECISION_READY
RECOMMEND_OWNER_DECISION=ACCEPT
OWNER_ASSURANCE_DECISION=PENDING

NEXT=OWNER_ACCEPT_AMEND_OR_REOPEN_WARRANT_F_V0_2
```
