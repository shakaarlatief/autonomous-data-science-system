# Research 227: AO-8 Independent Architecture Review Reconciliation

**Date:** 2026-09-21
**Status:** AO-8 COMPLETE / REVIEW RECONCILED / AO-9 NEXT
**Program:** Research 219
**Review thread:** MC-0021
**Independent review:** Message 001 @ 7f11f5f3af4106ad322a4e1572cf6befda81a582
**Comparative review:** Message 003 @ 4eb17b185bf939e0767e72121a61081a5638fda0
**ChatGPT reconciliation:** MC-0021 Message 004
**Integrated candidate target reviewed:** f73239ee486132a94701de80514ffd11480b9ecd
**Machine synthesis:** docs/research/project_knowledge_activation_orchestration/AO8_REVIEW_RECONCILIATION_V01.json
**Scope:** Reconcile MC-0021 independent/comparative review against the frozen AO-3 through AO-7 candidate, preserve accepted baseline semantics, identify disposition-pending amendment and requirements candidates, and carry bounded AO-9/AO-10 qualification/realization obligations forward without silently mutating frozen architecture.
**Authority:** Architecture-review reconciliation. This closes AO-8 but does not silently amend frozen AO-3 through AO-7 architecture, Requirements V0.2, Specification 028, Research 218, or project authority.

## 1. Result

AO-8 produced a genuinely independent counter-design and then a direct comparative review.

The independent design initially preferred:

~~~text
source-declared activation predicates
two mandatory claim/conformance gates
one append-only control ledger
smaller interaction continuity
veto-only successor bridge
~~~

After candidate exposure, the reviewer withdrew or substantially narrowed the competing claims that would have replaced AO-4 through AO-7.

The integrated architecture therefore survives independent review.

No stage is superseded or reopened.

## 2. Candidate status after review

~~~text
AO-3 Progressive Control Closure
    retained as accepted baseline
    one material amendment candidate opened for AO-9 evidence

AO-4 Governed Evolution Cases
    KEEP

AO-5 Anchored Interaction Continuity and Independent Recovery
    KEEP

AO-6 Purpose-Bound Git Lifecycle
    KEEP
    realization obligation strengthened

AO-7 Authority-Preserving Successor Bridge
    KEEP as architecture baseline
    qualification refinements carried forward
~~~

AO-8 does not perform an AMEND because Research 223 requires explicit owner decision for material architecture amendment and the principal proposed amendment has a clean empirical falsifier.

## 3. Material AO-3 amendment candidate

The surviving independent criticism is:

AO-3's pre-dispatch conformance path is not independent of the earlier obligation screen. If S3 incorrectly fast-paths a consequential guidance event, S6 may never create an ActionContract and S8 has no independent reason to run.

The candidate repair is a bounded project-controlled output/action-shape screen immediately before final dispatch/conformance.

Its purpose is not to classify owner intent and not to replace event/state activation.

It asks whether the proposed result itself contains a shape that independently warrants authority/contract closure, for example:

~~~text
ordered operational/procedural steps
repository/tool/runtime mutation
frozen-design assertion/change
Git ref action
external dispatch/handoff
authoritative current-project assertion
~~~

If it fires without sufficient closure, the cycle re-enters reconstruction/authority resolution.

Status:

~~~text
EVOLUTION_CASE=AO8-E01
AFFECTED_CONTRACT=Research 222 / AO-3
CANDIDATE_CLASSIFICATION=AMEND
DISPOSITION=DISPOSITION_PENDING
REQUIRED_NEXT_EVIDENCE=AO-9 C-versus-D regression
OWNER_DECISION=DEFERRED_UNTIL_EVIDENCE
~~~

## 4. Clarification and qualification candidates

AO-8 carries the following into AO-9/AO-10 without silently editing Research 222:

~~~text
AO8-C01
    define exactly how a mandatory control obligation may be
    explicitly discharged under policy

AO8-C02
    distinguish CONFORMANT from NO_CONTRACT_AVAILABLE

AO8-Q01
    evaluate deterministic structural verification of receipts/claims

AO8-Q02
    include negative controls and activation-overreach measures

AO8-Q03
    measure predicate/trigger calibration and retirement pressure

AO8-Q04
    evaluate whether supporting-evidence requirements need explicit
    scoped owner + expiry semantics

AO8-Q05
    evaluate generated consolidated control-evidence view only if
    bounded records otherwise leave self-observation fragmented

AO8-Q06
    grade bridge qualification by VERDICT / ROUTE / ASSERTION class
~~~

## 5. Realization obligations

AO-8 makes two prospective obligations explicit.

### AO10-O01: branch attach/switch and selected rotation

Research 225 already selected ROTATE for the live branch but the accepted mutation surface cannot attach/switch the local checkout.

Before AO-10 closes:

~~~text
governed local branch attach/switch is qualified or implemented
selected rotation is retried from an exact published head
local branch + upstream + remote ref + project routing are reconciled
result is preserved
~~~

AO-10 must attach this to an executable qualification gate or explicit governed deferral.

### AO10-O02: Specification 028 representation reconciliation

Before AO-10 performs production mutations for the bridge/control-evidence design:

~~~text
prove the chosen representation fits Specification 028 as written
OR
obtain explicit owner-approved prospective specification amendment
~~~

This includes bridge activation state, new persistent control-evidence surfaces, any new derived control-evidence view, and typed realization metadata when not already covered.

No Specification 028 amendment is performed by AO-8.

## 6. Requirements findings

AO-8 identifies two prospective Requirements V0.2 amendment candidates.

### AO8-R51 candidate

Control-behavior misses and owner-reminder dependency should be observable enough to become qualification/evolution evidence without relying on the owner to notice the pattern.

Closest current requirements: KA-R08, KA-R34, KA-R35, KA-R40, KA-R41.

Status: credible gap, owner decision deferred until AO-9 evidence.

### AO8-R52 candidate

Accepted MUST-level obligations should be traceable to implementation/migration gate, evidence, qualification and operational activation, or explicit governed deferral.

Evidence:

~~~text
Spec 028 reconstruction/CLI obligation scheduling gap
AO-6 selected branch rotation without an executable realization gate yet
~~~

Status: strong credible gap, owner decision deferred until AO-9 evidence.

### R53

A new override-recording requirement is not recommended. Existing KA-R08 plus AO-4 decision-rights semantics are sufficient if implementation makes overrides inspectable.

## 7. Control evidence persistence

AO-8 rejects a universal append-only control ledger.

Preferred direction remains:

~~~text
ephemeral control state for ordinary cycles
bounded typed evidence/receipts when persistence is justified
optional generated consolidation if qualification proves it useful
~~~

This is not event sourcing and does not make evidence authoritative.

## 8. Failure taxonomy

All eighteen AO-F leaves remain.

For reporting only, AO-9 may group them into:

~~~text
INTERPRETATION_AND_ROUTING
CLOSURE
AUTHORITY_AND_FIDELITY
CONTINUITY_AND_RECOVERY
DRIFT_AND_REALIZATION
CONTROL_TRANSPARENCY
~~~

No leaf distinction is removed.

## 9. AO-9 minimum comparative design

AO-9 must compare:

~~~text
A BASELINE_CURRENT_BEHAVIOR
B PLANNER_ONLY
C AO3_AO7_CANDIDATE
D AO3_AO7_PLUS_REVIEW_AMENDMENT_VARIANT
~~~

Positive pressure must include the real historical failures and self-hosting evidence.

Negative controls are mandatory.

The decisive material comparison is:

~~~text
R9
    classifier/event interpretation is wrong or insufficient
    proposed output contains consequential operational structure
    compare C versus D
~~~

If C already closes R9, AO8-E01 should not amend AO-3.

If D closes R9 and C does not at acceptable precision/context cost, AO8-E01 has evidence for an owner AMEND decision.

AO-9 must freeze thresholds and stopping rules before scored runs and must not tune the tested candidate after held-out outcomes are observed.

## 10. Stage boundary

~~~text
AO_8=COMPLETE
MC0021=RESOLVED
INDEPENDENT_REVIEW_INTEGRITY=PASS
AO3_BASELINE=RETAINED_PENDING_AO9
AO8_E01_OUTPUT_SHAPE_AMENDMENT=DISPOSITION_PENDING
AO4=KEEP
AO5=KEEP
AO6=KEEP
AO7_BASELINE=KEEP
AO10_O01=REQUIRED
AO10_O02=REQUIRED
AO8_R51_REQUIREMENT_CANDIDATE=DISPOSITION_PENDING
AO8_R52_REQUIREMENT_CANDIDATE=DISPOSITION_PENDING
AO8_R53_NEW_REQUIREMENT=REJECTED
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_9_EMPIRICAL_HISTORICAL_REGRESSION_PROGRAM
~~~
