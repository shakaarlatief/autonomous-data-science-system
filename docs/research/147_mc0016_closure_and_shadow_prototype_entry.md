# Research 147: MC-0016 Closure and Falsification-First Shadow Prototype Entry

**Date:** 2026-09-14
**Status:** MC-0016 RESOLVED / CANDIDATE 01 PROTOTYPE-READY AT DESIGN LEVEL / FINAL QUALIFICATION PENDING / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Close the adversarial whole-candidate review, preserve the final cross-model disposition, freeze the remaining prototype work items and route Research 124 from design critique into falsification-first shadow implementation.
**Authority:** Research/prototype-routing evidence only. Requirements V0.2 remain frozen acceptance authority. The current continuity architecture remains operational authority.
**Declared references:** `research:144`, `research:145`, `research:146`, `path:docs/model_collaboration/threads/MC-0016/messages/001_claude_adversarial_candidate_01_review.md`, `path:docs/model_collaboration/threads/MC-0016/messages/002_chatgpt_adversarial_review_disposition_and_narrow_followup.md`, `path:docs/model_collaboration/threads/MC-0016/messages/003_claude_narrow_candidate_amendment_review.md`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`

## 1. Cross-model closure

MC-0016 performed the intended adversarial function. Claude did not identify a reason to abandon Candidate 01 or reopen H3 before empirical implementation. It did identify multiple places where a reasonable semantic intention had not yet been converted into a governed mechanism. Those findings are now incorporated.

The final narrow review concludes:

```text
B_PRECEDENCE=CLOSED
D_JOINT_AUTHORITY=CORRECTED_BY_FINAL_J2_J3_TIGHTENING
H3_REOPEN_BEFORE_PROTOTYPE=NO
ANOTHER_CLAUDE_ROUND_BEFORE_PROTOTYPE=NO
MC0016=CLOSE
```

The remaining uncertainties are empirical rather than architecture-dialogue blockers.

## 2. Candidate 01 design rules frozen for the first prototype

The first prototype must treat these as fixed candidate semantics unless a falsification result forces explicit amendment:

```text
1. rich repository-native semantic sources remain primary authority
2. semantic identity is selective, not universal
3. ordinary authoritative facts have one canonical semantic source
4. directional relations use one natural semantic owner plus generated reverse/closure views
5. joint authority is default-deny and requires J1-J6, including the natural-owner versus
   arbitrary-symmetry discriminator
6. exact action-contract constraints have one normative structured home with stable constraint IDs
7. governed-procedure prose/contract edits trigger semantic drift review; drift never becomes a
   second authority source
8. consequential execution uses deterministic contract checks and a structured execution plan
9. high-consequence free-form transformation receives independent verification when deterministic
   equivalence cannot establish conformance
10. capture remains non-authoritative until explicit promotion
11. consequential consolidation uses a must-preserve manifest
12. current state separates deterministic core from optional narrative synthesis
13. normal reconstruction uses bounded materialized/current views; ordinary refresh is dependency-local
14. periodic corpus-wide rebuild remains legitimate for repair/qualification/migration
15. normal identity lookup uses a generated current-target index over complete transition history
16. paused work remains durable without remaining permanently mandatory in bootstrap
17. derived stores contain no unique accepted truth
18. rollback is exporter/parity/reverse-switch based and never dual-authority
19. current architecture remains authoritative until explicit qualified switch
```

## 3. First prototype purpose

The next phase is not implementation polish and not migration. It is an attempt to **falsify the candidate cheaply**.

The smallest useful shadow prototype should answer whether the candidate's strongest claims can survive executable pressure:

```text
A. can one exact-fidelity procedure maintain one normative constraint home and detect likely prose/contract drift?
B. can ordinary base/supplement authority remain source-owned while a truly symmetric irreducible case
   is admitted under J1-J6 without self-confirming flags?
C. can a BL-001-style source-read-but-contract-dropped case be prevented by the resolver + action contract?
D. can normal generated-view refresh be dependency-local while a full rebuild remains independently reproducible?
E. can identity transition history grow while normal lookup stays bounded through the current-target index?
```

These are intentionally smaller than implementing all ten qualification clusters at once. If these foundations fail, broader prototype work should stop and the architecture should be reconsidered before more machinery is built.

## 4. Prototype substrate boundary

The prototype should be isolated from current authority. It may use synthetic or shadow copies of repository facts, but must not turn Candidate 01 declarations into live project authority.

The first slice should contain only the minimum profile/schema surface required for the five questions above:

```text
GOVERNING_PROCEDURE
    semantic identity, scope/applicability, authority state, source-owned relations, structured
    action contract with stable local constraint IDs

JOINT_AUTHORITY_DECLARATION
    only for the positive J1-J6 test case

IDENTITY_TRANSITION
    only enough to exercise rename/merge/split/current-target lookup

DERIVED_VIEW_MANIFEST
    source binding, generator/version, freshness and rebuildability
```

Do not implement workstream, capture, private-boundary, full current-state narrative or migration machinery in the first slice unless one of the first five tests genuinely requires it.

## 5. Fixture discipline

The first prototype should use one immutable machine-readable fixture version. It must include at least:

```text
P1 base procedure
P2 ordinary supplement with natural direction P2 -> P1
JX symmetric/irreducible joint-authority-shaped case
JN near-miss case that must remain source-owned / derived-only
BL1 five-plus ordered action constraints including precondition + prohibition
BL1_BAD_OUTPUT deliberately omits/reorders at least one activated constraint
ID rename/move + merge + reversal + split history
H1X passive-history multiplier for refresh/rebuild measurement
```

The fixture must not contain a hand-set `should_be_joint_authority` or equivalent answer flag. Expected behavior belongs in separate test oracles so the admission logic cannot read its own label.

## 6. Falsification order

Run the first slice in this order:

```text
1. source-contract normative-home + drift-detection test
2. J1-J6 ordinary directional near-miss versus irreducible symmetric positive case
3. BL-001-style authority resolver + action-contract conformance failure
4. dependency-local incremental refresh versus clean full rebuild
5. identity history/current-target lookup under passive growth
```

Any semantic failure should be recorded before repair. Do not silently strengthen the fixture or implementation and report only the repaired result.

## 7. Evidence discipline

Record raw machine-readable results plus a separate interpretation record. Do not compress the first run into a scalar score. At minimum report:

```text
semantic result per case
fail-visible state
authoritative source locations touched
generated locations refreshed
full rebuild source count
incremental refresh source count
current-view size
identity lookup steps
joint-authority objects created
validator findings
constraint IDs activated / preserved / omitted
implementation/profile surface added
```

## 8. Stop / reopen conditions

Stop the prototype and reconsider Candidate 01 if the first slice shows any of:

```text
ordinary base/supplement requires joint-authority reification
J1-J6 still depends on hidden expected labels or arbitrary reviewer intuition to decide the fixture
structured action contracts create duplicate normative truth or cannot catch source-integrity drift proportionately
BL-001-style omission can pass despite activated deterministic constraint IDs
normal reconstruction/lookup requires whole-history scan
ordinary local change routinely requires global manual edits or full rebuild
profile/special-object machinery expands materially beyond what the five tests require
```

H3 remains a reference pole and should reopen only if the selective profile model begins behaving like a general object substrate and object-primary representation offers a demonstrably cleaner solution to the same failures.

## 9. Current disposition

```text
MC0016=RESOLVED
CANDIDATE=PKA-CANDIDATE-01
DESIGN_COVERAGE=50_KA_R__17_KA_I_AFTER_AMENDMENT
FINAL_QUALIFIED_PASSES=0
CURRENT_ARCHITECTURE=STILL_OPERATIONAL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_SMALLEST_FALSIFICATION_FIRST_SHADOW_PROTOTYPE
```
