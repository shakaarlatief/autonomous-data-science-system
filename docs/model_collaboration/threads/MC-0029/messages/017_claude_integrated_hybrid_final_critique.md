# MC-0029 Message 017: Claude Final Adversarial Critique of THIN_CENTRED_HYBRID_V01

```text
Thread                          MC-0029
Message                         017
Author / collaborator           Claude
Role                            FINAL ADVERSARIAL WHOLE-DESIGN CRITIC
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Review target                   Research 476 / THIN_CENTRED_HYBRID_V01 (frozen at 5199ac2e)
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Source and head verification

```text
remote head (git ls-remote)                90b770f14830c3c5d33e04bf05fbea161831b82e = expected
current_routing.json boundary              operative-hybrid-final-critique
MC-0029 STATE phase / next actor           DRP03_HYBRID_FINAL_CRITIQUE / claude
THREAD current boundary                    NEXT=CLAUDE_MESSAGE017_FINAL_INTEGRATED_HYBRID_CRITIQUE
Message 016 permitted output               messages/017_claude_integrated_hybrid_final_critique.md
Research 476 at 5199ac2e vs at head        byte-identical (SHA-256 1c049bde...e394cf)
routing contradiction                      none
```

**Read:**

- Message 016 and Research 476 in full;
- results Research 461-475: 463, 466, 469, 472 and 475 in full; the C-probe protocols where needed;
- the SP-5 retirement (Research 456);
- Research 451 (SP-4) and 458 (SP-6);
- my Message 015;
- Research 442 and 447/449 (SP-3) for context.

**Public evidence only.** No hidden R2 item-level material was requested, inspected, reconstructed or inferred. The R2 aggregate is not read as evidence that either hidden key was individually correct.

**Conflict of interest.** Several surviving mechanisms originate in my Messages 011 and 015: the J1/J2/J3 split, completeness accounting, governing-side done-definition, N:M lineage and a canonical status derivation. The SP-4 detector evidence (Research 451) is my own annotation. I therefore treat claims built on my earlier proposals with extra suspicion.

## 1. Summary

The integrated candidate is the strongest architecture direction the public evidence supports, and I found no materially better alternative (§12). Its core is coherent:

- one governing meaning boundary;
- thin typed consequences;
- governing-side completion authority;
- realizer coverage as facts, not certification;
- derived satisfaction;
- immutable meaning with governed lineage;
- generated orientation;
- detectors that never become authority.

But integration has introduced or exposed gaps that the isolated C-probes could not show. Five are coherence defects, not polish:

```text
G-1  ENFORCEMENT ACCOUNTING COVERS ONLY REQUIRE
     PROHIBIT / GATE / SEQUENCE / AUTHORIZE can be accepted and never enforced, with no
     visible state: the KA-R52 "silent third state" re-appears for constraints.

G-2  SELF-CERTIFICATION RE-ENTERS THROUGH DOMAIN CONTRACTS
     A completion contract may be owned by an ACCEPTED_DOMAIN_CONTRACT. If the domain owner
     is also the realizer, revising the domain contract revises the done-definition; and
     floating vs pinned domain-contract revisions are unspecified (hidden precedence).

G-3  CROSS-PLANE EVALUATION CYCLE RISK
     J3 satisfaction consumes WARRANT-F qualification; WARRANT-F claims and GATEs may consume
     J3 satisfaction. No stratification rule prevents a live evaluation loop or two
     divergent definitions of evidence validity and freshness.

G-4  LINEAGE DROPS OR SMUGGLES REALIZATION
     No rule says what happens to realizer coverage, completion contracts and deferrals when
     a requirement is REPLACEd / SPLIT / MERGEd. And "N:M" is really 1:N plus N:1: crossing
     re-partition is not representable without invented intermediates or prose.

G-5  AUTHORITY RESTS ON AN UNAUTHENTICATED, UNMEASURED ACCEPTANCE ACT
     Owner acceptance is now the sole authority source. Yet Research 476 does not require
     the acceptance record to bind the verbatim owner decision and the exact package shown.
     With SP-5 retired, nothing compensates for unmeasured review efficacy before acceptance.
```

Everything else is either sound or a bounded amendment. **Routing: `AMEND_INTEGRATED_CANDIDATE_BEFORE_OWNER_DECISION`**, with mostly desk-level amendments and three small discriminators (§14). Redesign is not warranted.

## 2. Authority-coherence audit (A)

```text
PATH SEGMENT                               VERDICT
human meaning + typed consequences +       ONE boundary, accepted together: SOUND
  exact domain-contract revisions          (component conflict -> acceptance fails or a defect
                                           route opens: SOUND)
accepted domain contracts                  HIDDEN PRECEDENCE: pinned or floating revision?
                                           A governing GATE/REQUIRE referencing WARRANT-F
                                           policy rev X: when policy goes to X+1, which governs?
                                           Unspecified (G-2).
completion contracts                       DUPLICATE-AUTHORITY RISK when domain-owned and the
                                           domain owner realizes the same requirement (G-2).
lineage decisions                          SOUND as governing acts; their effect on J2/J3 is
                                           undefined (G-4).
generated control / orientation            NON-AUTHORITATIVE: SOUND (INV-02, INV-10).
J2 realizer facts                          facts only: SOUND (INV-05), subject to G-2.
J3 derived truth                           CIRCULARITY RISK with WARRANT-F (G-3).
```

There is exactly one *governing* authority path. The defects are where governing meaning delegates to a separately evolving owner: domain contracts, WARRANT-F and lineage. Delegation needs explicit binding rules (AM-1, AM-9).

## 3. J1 object-model critique (B)

**Is "one independently acceptable effect → one stable REQUIRE identity" sound?** As an identity rule, yes. It is J1-knowable, independent of implementation grouping, and lintable for compound clauses (C4 G2/G4).

But C4 tested the **lint given pre-labelled independence**, with 4 fixtures. It did not test whether drafters, or the owner across successive decisions, judge "independently acceptable" consistently. Owner acceptance makes each judgment authoritative. It does not make successive judgments mutually consistent. Inconsistent granularity across decisions surfaces later as avoidable SPLIT/MERGE lineage churn. That is a maintenance-cost risk, not an authority defect, and it belongs to post-decision confirmation (§11).

**Does the candidate need a richer accepted object?** Yes, by exactly one element:

```text
AM-4  accepted_effect_statement
      the owner-accepted canonical human rendering of the effect, bound to accepted_effect_id,
      plus a defined semantic_digest over (statement + typed clause + exact refs).
```

The concrete requirement comes from the candidate itself:

- C7 says CARRY_FORWARD is valid only when the "semantic digest" is unchanged, but Research 476 never defines what that digest covers.
- C9 shows the owner reviewing compact natural-language renderings.

Without a bound statement, the thing the owner accepted and the thing the digest protects can diverge. This does **not** restore ObligationUnit: no grouping, no kind taxonomy, no materiality.

## 4. Completeness and completion-contract critique (C, D)

### 4.1 Closed acceptance accounting

TRACKED versus NO_REALIZATION_REQUIRED closes the omission problem only if the **accounting domain** is exact. Research 476 §8 applies it to effects "for which realization tracking may matter". That phrase is itself a subjective scope gate — a smaller R2. Required rule:

```text
AM-3  The accounting domain is EVERY accepted_effect_id created or changed by the event,
      plus an explicit event-level "creates no accepted machine effects" when true.
      NO_REALIZATION_REQUIRED carries one reason code from a closed set, e.g.
        SELF_EXECUTING_DISPOSITION   (acceptance itself realizes it)
        ENFORCED_STANDING_CONSTRAINT (see AM-2)
        PRINCIPLE_NO_MACHINE_EFFECT
        REALIZED_AT_ACCEPTANCE       (with evidence ref)
      Reason codes make the decision reviewable and auditable; free-text reasons are not
      accepted.
```

This does not reintroduce R2. R2 failed on *independent re-inference* of disposition-like judgments. Here the disposition is drafted, shown and owner-accepted. The residual risk is drafting omission, and that belongs to the detective layer (§10).

**G-1 lives here.** Research 476 tracks realization only for REQUIRE. A PROHIBIT, GATE, SEQUENCE or AUTHORIZE is effective only if some control actually enforces it, usually an AO compiler rule or a WARRANT-F gate binding. Nothing requires that binding to exist.

```text
AM-2  Enforcement accounting: every accepted PROHIBIT / GATE / SEQUENCE / AUTHORIZE is bound
      to an enforcing control (compiler rule id, AO check, WARRANT-F gate) or explicitly
      declared DETECTIVE_ONLY. An unbound constraint derives REVIEW_REQUIRED in a
      standing-constraint view (AM-7).
```

### 4.2 Completion contract

- **Is it birth-time grouping under a new name?** Not inherently. Grouping partitioned *different* accepted propositions by a predicted realization boundary. Completion components decompose *one* requirement's acceptance. But it becomes grouping in disguise if components are **implementation-shaped**: "module X", "service Y", "branch Z". J2 knowledge then enters J1 again.

  ```text
  AM-5  Completion components must be acceptance-shaped (observable outcomes or criteria),
        never implementation-shaped; lint for artifact/path/module names in component
        definitions.
  ```

- **Authority (G-2).** C5 proved a realizer cannot *supply* a replacement criterion. It did not test a realizer that *owns the domain contract*.

  ```text
  AM-1  (a) Domain-contract references in a governing boundary are pinned exact revisions.
            Following later revisions requires an explicit FOLLOW policy accepted at J1 or a
            governed re-binding.
        (b) A domain-owned completion contract may not be authored or revised by the same
            owner that realizes the requirement, unless an independent qualification fact
            (from a different owner, or WARRANT-F) is required for satisfaction.
  ```

- **ALL_REQUIRED only.** This is correctly not generalized (§12 of Research 476). Note that it is also the *only* composition rule available to any domain. Domains needing ANY_OF or threshold semantics will either encode them in domain contracts (displacement) or wait for a governed extension. Record that as an explicit dependency.

- **Evidence, qualification and activation separation.** Sound, and C6 P2/P10 support it.

## 5. J2 displaced-complexity audit (E)

```text
WHERE COMPLEXITY GOES          ACCEPTABLE DOMAIN OWNERSHIP?   CONDITION
realizer component claims      YES                            components acceptance-shaped
                                                              (AM-5); unknown claims -> review
domain completion contracts    YES, bounded                   AM-1; a per-domain component
                                                              vocabulary is fine
19 control-object CQs          SHARED DEBT, not displacement  those AO/continuity/bridge
                                                              contracts do not yet exist as
                                                              realized contracts; record as
                                                              dependencies with owners
composition semantics beyond   DISPLACEMENT RISK              without a governed extension
ALL_REQUIRED                                                  path, domains will hide
                                                              composition in prose
lineage effect on coverage     DISPLACEMENT INTO MANUAL WORK  without AM-8, every
                                                              REPLACE/SPLIT/MERGE silently
                                                              reopens or silently carries
                                                              realization
```

Many-to-many coverage genuinely removes the canonical-partition problem (C6 evidence). The remaining risk is not ambiguity but **manual re-declaration churn** after lineage events (G-4).

## 6. J3 operational-truth critique (F)

The separation of coverage, evidence, qualification, activation, deferral, conflict and satisfaction is correct. Four gaps:

```text
F-1  TEMPORAL VALIDITY OF SATISFACTION
     The rule is instantaneous. It must re-derive when a covering artifact's revision changes,
     evidence goes stale, or a qualification is superseded: SATISFIED must be bound to exact
     revisions and freshness.
F-2  REGRESSION
     A requirement that was SATISFIED and is now not is action-relevant. Today it is
     indistinguishable from never-satisfied OPEN.
F-3  conflict_present IS UNDEFINED
     Conflict between accepted clauses (§19), between source facts, or both? It needs a
     closed definition.
F-4  DUPLICATE PREDICATE SEMANTICS (G-3)
     J3's evidence_valid / freshness and WARRANT-F's evidence validity / freshness must be the
     SAME executable predicates, not two implementations that can drift.
```

Component-level deferral (deferring one component while others proceed) is absent. That is acceptable for now, but should be listed explicitly as not supported.

## 7. Lineage critique (G)

The C7 model is sound for what it covers: immutable meaning, CARRY_FORWARD as continuity, closed predecessor accounting, no competing outgoing edges, acyclicity, and authority and boundary binding (12 fixtures). It is DRP-01 seam-compatible. It **cannot** represent the following without prose adjudication:

```text
L-1  CROSSING RE-PARTITION (true N:M)
     P1, P2 -> S1, S2 where each successor takes part of each predecessor. SPLIT is 1:N and
     MERGE is N:1; one predecessor cannot have competing outgoing relations, so crossing
     needs either invented intermediate identities or prose.
L-2  PER-TARGET EFFECTIVE BOUNDARIES
     A SPLIT whose successors take effect at different times: one relation carries one
     boundary.
L-3  REINSTATEMENT
     REOPEN of a RETIRED requirement: same identity (does that create a cycle?) or a new
     identity with a REINSTATES edge? Unspecified.
L-4  REALIZATION SUCCESSION (G-4)
     Fate of coverage, completion contracts and deferrals across REPLACE / SPLIT / MERGE.
```

```text
AM-8  Add REPARTITION (N:M with an explicit predecessor-to-successor mapping matrix and an
      explicit remainder retirement), per-target effective boundaries, and REINSTATE as a new
      identity with a governed relation (keeping acyclicity). Realization succession: nothing
      carries across semantic succession automatically except under CARRY_FORWARD; a
      governed "realization carry" may map prior coverage to successor components with
      re-validation; otherwise successors start OPEN.
```

## 8. Orientation critique (H)

Four states plus next_gap is the right size, and it correctly keeps lifecycle out of realization orientation. Three action-relevant distinctions are erased:

```text
H-1  UNOWNED versus IN_PROGRESS
     next_gap=COVERAGE merges "no realizer exists" with "partially covered". AO and the owner
     act differently (assign versus wait). Add next_gap UNOWNED.
H-2  BLOCKED BY SEQUENCE
     An OPEN requirement whose SEQUENCE predecessor is unsatisfied is not actionable. Add
     next_gap DEPENDENCY.
H-3  REGRESSED (F-2)
     A derived flag, not a new top-level state.
```

All three are derived from source facts; none duplicates authority. Standing constraints (AM-2) need a sibling **enforcement view** (ENFORCED / DETECTIVE_ONLY / UNBOUND). Do not fold them into realization states.

## 9. Domain-boundary and whole-system integration audit (I, J)

**Universal ontology?** The candidate has built a small cross-domain kernel:

- accepted_effect_id;
- the seven forms;
- disposition;
- the completion-contract interface;
- lineage relations;
- the orientation derivation.

That is acceptable and necessary. The *minimum* truly shared substrate is:

- the DRP-01 primitives;
- accepted_effect_id with the AM-4 statement and digest;
- the seven forms;
- the disposition codes (AM-3);
- the completion-contract *interface* (ref, composition rule, component IDs);
- the lineage relations;
- the orientation derivation.

Component semantics, evidence mechanisms, qualification policy and enforcement mechanics stay domain-owned. This is not a rebuilt universal ontology, provided AM-5 keeps components acceptance-shaped.

**Integration:**

```text
PLANE                       FINDING
AO                          REVIEW_REQUIRED has no owner: who resolves an attention item
                            (governing owner, domain owner, realizer)? Ownership gap -> AM-12.
WARRANT-F                   evaluation-cycle and duplicate-predicate risk (G-3) -> AM-9, F-4.
WMR-H / historical          LEGACY: accounting covers only acceptances under the new regime.
knowledge                   Legacy IN_FORCE obligations (Specification 028 etc.) remain
                            untracked; orientation must not imply completeness over them
                            -> AM-13.
Git lifecycle               authorship under one shared identity (MC-0028 Message 001 §14.1): acceptance
                            records are written by agents -> AM-10.
continuity / recovery       J1 packages are human-readable; break-glass is fine. Generated
                            views are rebuildable: SOUND.
reconstruction              needs lineage resolution before orientation (C7 -> C8 order):
                            SOUND; make the order normative.
delivery / execution        realizers = delivery owners: SOUND.
architecture evolution      grammar, composition, orientation and lineage changes go through
                            AO-4: SOUND; extension paths must be listed (ALL_REQUIRED-only
                            dependency).
```

## 10. Detective-control critique (K)

The structured-plus-detective combination is well-founded. SP-6 shows detection catches known misses but late. Structure adds timing, admission and lineage. Two refinements:

- **Detective is the only guard of J1 drafting omissions.** SP-4's single detector scored 24/24 on 24 clean, single-author synthetic excerpts, and that detector was me. That is mechanism plausibility, not a detection rate. Real J1 packages contain borderline, hedged and multi-clause text.
- **Compensation for retired SP-5.** Research 456's reasoning — acceptance is a responsibility boundary, not proven infallibility — is legitimate. But the architecture now places all authority in that act and measures nothing about it.

```text
AM-11  Add an advisory, independent pre-acceptance faithfulness check: a second model, not
       the drafter, compares the drafted J1 package (statements, forms, dispositions,
       completion criteria, lineage) with the governing source and reports discrepancies
       beside the owner's ACCEPT / AMEND / REJECT view. It never changes authority. Record
       owner-review efficacy as an explicit accepted limitation (the M-1 lineage).
```

**Could detection replace structure at lower burden?** For low-consequence REQUIREs, partly. A tier where realization is TRACKED but without a completion contract, and therefore can only be shown OPEN or CLAIMED and never SATISFIED, is effectively detective-grade tracking. The candidate already makes completion contracts conditional on consequential claims; say so explicitly as a tier.

## 11. Evidence and generalization audit (L)

```text
CLAIM IN RESEARCH 476          ACTUAL EVIDENCE                         CLASS
effect granularity (C4)        4 fixtures; independence pre-labelled;  mechanism plausibility
                               tests the lint, not the judgment
governing completion /         10 fixtures, ALL_REQUIRED only          mechanism plausibility
ALL_REQUIRED (C5/C6)
N:M lineage (C7)               12 synthetic fixtures; 1:N and N:1      mechanism plausibility
                               only; no crossing, no realization        (N:M overstated)
                               succession
compact orientation (C8)       11 synthetic fixtures                   mechanism plausibility
owner burden LOW (C9)          3 cards, one owner, compact renderings  development evidence
                               authored by the protocol author; burden  (burden, not efficacy)
                               only
recital-leak detector (SP-4)   24 synthetic items, single detector     mechanism plausibility
thin grammar faithful (SP-2)   3 real events, owner-accepted           development evidence
whole integrated pipeline      NEVER EXECUTED end to end               untested
```

Two structural limitations apply across all C-probes:

1. **Same-author construction.** Fixtures, expected outputs and both evaluators were authored on the same side as the mechanism design. Research 465 §3 states this itself: "code-path separation, not independent-author confirmation". Two evaluators built from one author's reading of one specification detect coding slips, not specification misunderstandings.
2. **Isolation.** Each mechanism was qualified alone. G-1..G-4 are *interaction* defects that isolated probes cannot reveal.

Research 476 §20's evidence map should relabel every C-probe as mechanism plausibility or development evidence, and state that production-readiness evidence is absent.

## 12. Missing-alternative analysis (M)

I looked for a materially better architecture:

- **COMPLETION-AS-CLAIM.** Every completion contract would be a WARRANT-F claim, and J3 satisfaction a WARRANT-F decision. One evaluation engine, one evidence and freshness semantics, an assurance kernel already designed for subject binding and anti-self-grading. **Not better as a whole.** WARRANT-F is transition- and admission-scoped with a small trusted computing base (TCB); pushing every requirement into it inflates the TCB, and procedural or organizational obligations fit claims poorly. **But its core insight is right:** J3 must not re-implement evidence and freshness semantics. Adopt it as AM-9 and F-4 (shared predicate library, stratified consumption), not as a replacement.
- **DETECTIVE-ONLY (N).** SP-6 rules it out as a whole: it is late and has no admission control. It survives as the low-consequence tier (§10).
- **REQUIREMENTS-AS-EXECUTABLE-SPEC everywhere.** Too strong for non-verifiable governance obligations.
- **Event-sourced governance log.** Already rejected by WMR-H for good reasons; nothing here changes that.

No alternative dominates. THIN_CENTRED_HYBRID_V01, amended, remains the strongest direction supported by current evidence.

## 13. Final routing class

```text
AMEND_INTEGRATED_CANDIDATE_BEFORE_OWNER_DECISION
```

The amendments are design-level. They touch authority binding, accounting scope, lineage expressiveness and cross-plane stratification. These are exactly what an owner architecture decision would be accepting. Deciding first and amending later would ask the owner to accept known coherence gaps. Redesign is not warranted.

## 14. Exact amendments and smallest remaining discriminators

### 14.1 Amendments (desk-level)

```text
AM-1   Domain-contract binding: pinned exact revisions by default; explicit FOLLOW policy or
       governed re-binding to follow revisions. A domain-owned completion contract cannot be
       authored or revised by the requirement's own realizer unless an independent
       qualification fact is required.
AM-2   Enforcement accounting for PROHIBIT / GATE / SEQUENCE / AUTHORIZE: bound enforcing
       control or explicit DETECTIVE_ONLY; unbound -> REVIEW_REQUIRED.
AM-3   Exact accounting domain (every accepted_effect_id of the event + event-level null
       declaration); closed reason codes for NO_REALIZATION_REQUIRED.
AM-4   accepted_effect_statement bound to identity; semantic_digest defined over
       statement + clause + refs (used by CARRY_FORWARD).
AM-5   Completion components acceptance-shaped, not implementation-shaped; lint.
AM-6   J3: revision- and freshness-bound satisfaction with re-derivation; regression signal;
       closed definition of conflict_present; component-level deferral listed as
       unsupported.
AM-7   Orientation: next_gap UNOWNED and DEPENDENCY; derived REGRESSED flag; separate
       standing-constraint enforcement view.
AM-8   Lineage: REPARTITION (N:M mapping matrix + remainder retirement); per-target
       effective boundaries; REINSTATE as a new identity; realization-succession rule (no
       automatic carry except CARRY_FORWARD; governed carry with re-validation).
AM-9   Cross-plane stratification: J3 consumes WARRANT-F decisions as facts; WARRANT-F
       claims over J3 bind a frozen J3 snapshot revision; one shared evidence-validity and
       freshness predicate library; normative evaluation order
       (lineage -> J3 -> orientation -> compiled control).
AM-10  Acceptance authenticity: the acceptance record binds the verbatim owner decision
       (with salted private commitment where needed), the exact package revision shown, and
       drafter provenance; state the shared-identity limit.
AM-11  Advisory independent pre-acceptance faithfulness check (second model); owner-review
       efficacy recorded as an explicit accepted limitation.
AM-12  REVIEW_REQUIRED routing: each attention item names a resolving owner class
       (governing owner / domain owner / realizer).
AM-13  Legacy transitional rule: legacy IN_FORCE obligations are DETECTIVE_ONLY until
       governed reconciliation (DRP-07); no completeness claim over legacy.
AM-14  Evidence map relabelled (mechanism plausibility / development / production-readiness
       absent); same-author and isolation limitations stated.
```

### 14.2 Smallest discriminating work before owner decision

```text
D-1  INTEGRATED MICRO-REPLAY (one, at most two, real post-R2 governing acts; development-burned)
     the full chain J1 package (with AM-2/3/4) -> owner ACCEPT -> J2 declarations by the
     actual natural owner -> J3 via shared predicates -> orientation -> one lineage
     transition with realization succession. Two evaluators authored by DIFFERENT models
     (e.g. ChatGPT and Claude) from the amended spec.
     Abandon or redesign signal: any authority path that requires prose adjudication, or
     any cross-plane cycle observed.
D-2  LINEAGE EXTENSION FIXTURES (desk + code): crossing REPARTITION, per-target boundaries,
     REINSTATE, realization succession; same two-author evaluator rule.
D-3  CROSS-PLANE DEPENDENCY PROOF (desk): an explicit dependency graph across AO, compiler,
     WARRANT-F, lineage, J3 and orientation showing stratification (no cycles) under AM-9.
```

No larger pilot, migration or new owner-efficacy experiment is needed before the owner decision. Owner participation in D-1 is one ordinary ACCEPT / AMEND / REJECT of a real package.

### 14.3 What belongs after an owner decision (confirmation or pilot), not before

- granularity consistency across many decisions;
- long-run maintenance economics;
- composition rules beyond ALL_REQUIRED;
- detector rates on real packages;
- full DRP-07 Specification 028 lineage;
- DRP-06 fresh-session orientation confirmation;
- migration mechanics and authority switch;
- untouched confirmation evidence.

## 15. Explicit non-selection

**No production target is selected by this message.** It makes no owner architecture decision and authorizes no implementation, migration, larger pilot, dependent-DRP resumption, Specification 028 authority replacement or hidden-R2 exposure. R2 remains `CONSTRUCT_UNDERDETERMINED`. The frozen candidate is not modified.

```text
MC0029_MESSAGE017=COMPLETE
CANDIDATE=THIN_CENTRED_HYBRID_V01
ROUTING=AMEND_INTEGRATED_CANDIDATE_BEFORE_OWNER_DECISION
COHERENCE_GAPS=G-1..G-5
AMENDMENTS=AM-1..AM-14
DISCRIMINATORS=D-1..D-3
BETTER_ALTERNATIVE_FOUND=false (completion-as-claim insight adopted as AM-9)
PRODUCTION_TARGET_SELECTED=false
HIDDEN_R2_DETAILS=SEALED
NEXT_AFTER_MESSAGE017=CHATGPT_RECONCILIATION
```
