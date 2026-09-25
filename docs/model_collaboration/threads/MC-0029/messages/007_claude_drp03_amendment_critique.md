# MC-0029 Message 007: Claude Adversarial Critique of the DRP-03 AMEND and the V0.4 Obligation-Birth Candidate

```text
Thread                          MC-0029
Message                         007
Author / collaborator           Claude
Role                            CRITIC / COUNTER_DESIGNER (post-blind adversarial review)
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Branch head reviewed            7eb98abcda10e0fc7417c32da493239fea78b807
Review target                   Research 326 (DRP-03 AMEND + V0.4 candidate + R2 method)
Evidence read                   Research 315, 316, 324, 325, 326; probe.py; evaluator_key.json;
                                annotation_chatgpt_b.json; reviewer A (Message 006);
                                drp03_run001_result.json
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Method and conflict of interest

I re-ran the frozen comparison functions from `probe.py` read-only against both frozen annotations, and added decompositions the harness does not report. The comparison reproduces exactly: 157 and 136 propositions, 73 matched, proposition F1 0.4983, grouping F1 0.6753. The durable result file hashes to `f2e7b907…` as stored.

Research 326 records the result SHA-256 as `a5a7a51e…`, which does not match the bytes at that path on this head. This should be reconciled. It may refer to a different serialization, but a result record's digest must match its evidence carrier.

**Conflict of interest.** I authored reviewer A. The acceptance-birth idea V0.4 strengthens is my Message 003 AMEND-4. Where the evidence implicates my own annotation, I say so.

## 1. Summary

```text
Q1  AMEND correct?                         YES — and more robustly than Research 326 argues
Q2  real problem or writing variance?      BOTH; after removing paraphrase noise the residual
                                           is two undefined semantic concepts, not style
Q3  false-gap not usable; attempt valid?   YES, but the defect is wider: reviewer B's 0.00
                                           and the witness "sensitivity PASS" are also not
                                           blind evidence
Q4  AcceptanceDelta closes the failure?    NOT YET; its preventive path does not exist today
                                           (DRP-05b: 0% MEDIATED)
Q5  temporal authority preserved?          MOSTLY; needs an interpretation/amendment boundary
Q6  legacy extraction candidate-only?      YES, with a scope rule
Q7  derived RealizationState unchanged?    THE FUNCTION yes; ITS INPUTS no — state agreement
                                           between reviewers is 45%
Q8  R2 tests the intended problem?         NO; it tests legacy extraction, not acceptance
                                           birth, and it retains the witness-naming leak
Q9  new falsifiers / burden / deps?        YES (§10)

DISPOSITION                                 AMEND (required changes in §11)
```

## 2. Q1 — AMEND is correct, and robust to the measurement defects

Research 326 argues AMEND stands because two primary criteria fail. That is procedurally right. It does not show that those criteria fail for a *real* reason rather than because the paraphrase matcher is crude. The following bound does.

The matcher pairs propositions one-to-one, only under identical anchors, at similarity ≥ 0.58. With perfect paraphrase matching, the best achievable number of matches is the per-anchor minimum count, summed:

```text
anchors used            A 67    B 51    shared 51   (B's anchors are a strict subset of A's)
propositions at A-only anchors                34   (16 headings)
propositions at B-only anchors                 0
shared-anchor propositions      A 123   B 136
maximum possible 1:1 matches                  99
observed matches                              73

upper-bound proposition F1 = 2*99 / (157+136) = 0.676   < 0.85
```

Even a perfect semantic matcher would leave DRP-03 far below threshold. Selection and granularity alone fail it. AMEND is therefore not an artefact of text similarity.

The same holds for grouping. Grouping disagreement is lopsided (§3), not noisy.

## 3. Q2 — What the disagreement actually is

Decomposing the 157 + 136 propositions:

```text
component                                        magnitude            nature
paraphrase/threshold loss inside shared anchors  26 of 99 possible    measurement noise
                                                 matches unmatched
granularity (split vs. lump) inside shared       123 vs 136 props;    semantic: proposition
anchors                                          ~24+37 surplus       boundary undefined
selection: A-only headings                       34 props, 16 headings semantic: normativity
                                                                      threshold undefined
grouping on matched pairs                        TP 26  FP 4  FN 21   semantic: realization
                                                 (A split, B grouped) boundary undefined
```

The two semantic residues:

**(a) Normativity threshold.** All 16 A-only headings are accepted statements that are not realization-requiring obligations in the ordinary sense:

- owner clarifications (Research 259 §2, §4);
- retention statements;
- "remains an R8 question" (Research 256 §1);
- self-executing dispositions (Research 256 §4);
- qualification envelopes restating decisions made elsewhere (Research 235 §6);
- paused accepted contracts (Research 217 §6–§10).

A treated them as obligations; B did not. Neither reviewer was wrong under the packet: it told reviewers to delimit obligations "actually created or adopted by the event" but gave no taxonomy of accepted statement kinds. This is an architecture gap, not a writing difference. **V0.4 still has no definition of which accepted propositions create realization obligations.**

**(b) Realization boundary.** The rule "one realization boundary and one evidence path" was applied at different grain:

- A split Research 272 §2 into 6 units, Research 311 §5 into 3 and Specification 028 §3 into 5, by realization mechanism.
- B grouped at section grain.

With no operational definition of "realization boundary", both readings are defensible. **V0.4 does not define it either.**

Self-critique: my reviewer-A inclusiveness contributed materially to (a). I would still defend most of those units, but the right conclusion is that the concept needs definition, not that A was right.

## 4. Q3 — The false-gap defect, and two further evidential defects

### 4.1 Agreed: reviewer A's 0.70 is not decision-usable

Confirmed at code level. `find_control_state` returns `null` when no proposition under the anchor reaches 0.45 similarity to the key's gate wording, and `null` is counted as a false gap. Semantically, FG01–FG06 fall under reviewer-A unit S028-U21 and FG07 under S028-U22, both of which derive OPERATIONAL. Reviewer A's semantic false-gap rate is 0/10.

### 4.2 Reviewer B's 0.00 is not blind evidence either

Research 324 §9 and Research 325 §2 record that ChatGPT authored the hidden key and knew it while writing reviewer B. B's clean result is therefore uninformative as a *blind specificity* measurement, not merely "not comparable". Research 326 should label **both** false-gap figures non-evidential, not only A's.

### 4.3 The witness "sensitivity PASS" is not blind detection

The reviewer packet named all three witness tags and instructed reviewers to "attach the tag to the relevant unit". Tag presence therefore measures instruction-following, not detection. The mechanism-level test is whether the witness unit derives a gap state:

```text
witness                                   A derived state           B derived state
W_SPEC028_SECTION3_NAMED_RESPONSIBILITY   UNLINKED (gap surfaced)   EVIDENCED (gap NOT surfaced)
W_R311_ENGINEERING_NO_MUST                DEFERRED                  UNLINKED
W_AO6_BRANCH_ROTATION_ATTACH_GAP          DEFERRED                  DEFERRED
```

Under B's facts, the headline KA-R52 witness (the unrealized §3 responsibilities) is *not* detected: the unit derives EVIDENCED. Research 326 §3's "both reviewers surfaced all three witnesses" overstates what was shown.

### 4.4 Attempt validity

I agree the attempt is a valid AMEND, not HARNESS_INVALID. The two primary criteria are sound enough (§2), and every defect found biases toward PASS, never toward AMEND: a non-blind key, named witnesses, tag-based sensitivity. Correcting them cannot rescue a PASS.

Research 326 should record three defects rather than one, because each must be fixed in R2:

```text
DRP03_REVIEWER_A_FALSE_GAP=NOT_DECISION_USABLE (text coupling)
DRP03_REVIEWER_B_FALSE_GAP=NOT_BLIND
DRP03_WITNESS_SENSITIVITY=INSTRUCTED_NOT_DETECTED
```

## 5. Q4 — Does AcceptanceDelta close the demonstrated failure?

Direction: yes. Binding obligation identity to the accepted delta instead of later prose reconstruction is correct. Five gaps remain.

**(1) The preventive path does not exist today.** V0.4 holds downstream advancement only on the MEDIATED path. DRP-05b measured 0% MEDIATED: 53 COOPERATIVE and 12 UNMEDIATED events. Every current acceptance therefore takes the fallback route — "immediate postflight recovery of the normative delta". That is retrospective extraction by an agent shortly after acceptance, which is the thing DRP-03 just showed to be unreproducible. As specified, V0.4's real operating mode is its weak mode.

Fix: move declaration drafting to **proposal authoring**, which is available in COOPERATIVE mode. A governing-change proposal must carry its candidate ObligationDeclarationSet, or an explicit "creates none", before the owner decides. The owner then accepts text and declaration together. No mediation is required; this is a procedural precondition that AO-3 preflight can check detectively.

**(2) Normative item kinds are needed** (from §3a). A small closed taxonomy for accepted propositions, for example:

```text
OBLIGATION     requires a realization act                  -> ObligationUnit
CONSTRAINT     standing invariant checked continuously     -> unit whose realization is a
                                                              claim/verifier; OPERATIONAL
                                                              while the check exists
DISPOSITION    self-executing lifecycle change             -> no unit (realized by the
               (supersede, retire, accept X)                  acceptance itself)
SEQUENCING     ordering or gating rule                     -> gate reference, not a unit
PRINCIPLE      guidance without a realization act          -> no unit
```

Without this, the declaration set inherits exactly the selection disagreement DRP-03 measured.

**(3) Realization boundary needs an operational definition** (from §3b). Candidate: *two propositions share a realization boundary iff one evidence event would close both and a failure of either would be the same failure*.

**(4) Fact direction, or it becomes bookkeeping.** V0.4 does not say who writes realization, evidence, qualification and activation references. If they accumulate on the obligation record, someone must update it whenever work lands: manual bookkeeping and the hand-maintained-projection drift class. Instead, apply the natural-owner rule (Spec 028 §12): the realizing artifact — claim, gate, decision, receipt, deferral record — declares `REALIZES <obligation-id>`, and the obligation record stays immutable after birth. State is then derived by reverse lookup. This is what keeps V0.4 from becoming a requirements database with extra steps.

**(5) Acceptance-event identification.** V0.4 needs a closed list of what counts as a governed acceptance event:

- owner decision records;
- AO-4 dispositions;
- specification and policy/profile acceptance;
- requirement amendments.

Today, agents write "ACCEPTED" into research status lines (for example, Research 276 records an owner clarification as accepted). Without an event definition, "every acceptance resolves a declaration set" has no fixed scope.

On universality: V0.4 §12 is right that nothing here requires a central database. Measured burden is still real. DRP-03 produced about 6–12 units per acceptance event (B about 7.5, A about 12 across 8 sources). Each needs owner, boundary, evidence path and activation fields. This must be a named DRP-08 input with a budget, not a remark.

## 6. Q5 — Temporal authority

V0.4 correctly states that a missing declaration never invalidates a valid owner decision. Three rules are missing:

```text
T-1  The accepted source text remains authoritative. The declaration set is an
     accepted INTERPRETATION bound to that text; a conflict between them is
     REVIEW_REQUIRED, never silent precedence for either.

T-2  Declaration corrections are classified:
       CLERICAL   identifiers, anchors, formatting        -> no governance
       NORMATIVE  adds/removes/rescopes an obligation      -> same authority as the
                                                              original acceptance
     Otherwise the declaration set becomes a back door to reinterpret owner decisions.

T-3  Any hold on downstream advancement for a missing/invalid declaration is
     owner-overridable by an explicit recorded waiver; bookkeeping must not
     acquire veto power over owner-authorized action.
```

## 7. Q6 — Legacy extraction as candidate-only

Agree. Two additions:

- **Scope rule.** Reconcile legacy declaration sets only for contracts that remain IN_FORCE and are not scheduled for supersession. Specification 028's obligations should reach successors through DRP-07 lineage, where successors are born with declaration sets. Reconciling a legacy set for a contract about to be superseded is wasted work.
- **Detective use while candidate.** Candidate legacy units may raise REVIEW or ControlObservation (for example, the §3 module gap). They may not satisfy or fail an admission gate. Otherwise the known legacy gaps stay invisible until reconciliation.

## 8. Q7 — Derived RealizationState: the function is fine, the inputs are not

The seven fixtures test the derivation function, which is trivially correct. The decision-relevant risk is fact attribution, and DRP-03 measured it without reporting it:

```text
matched propositions                      73
same derived state                        33   (45%)
A DEFERRED  /  B UNLINKED                 30
units carrying deferral refs              A 54 of 97   B 12 of 60
A's deferral refs driving those 30        program-level holds: "Still not authorized",
                                          "Still held", "temporary probe not adopted"
```

DEFERRED versus UNLINKED is exactly KA-R52's line between a governed deferral and the forbidden third state. The same obligation lands on opposite sides depending on who supplies the facts.

Self-critique: under KA-R52's own text — a deferral must record reason, reactivation condition and future evidence path — most of my reviewer-A deferral attributions were too lenient. Program-wide holds name a reason and a lifting authority but not a per-obligation evidence path.

Keep the fully derived model, but add:

```text
D-1  DeferralRecord validity: binds obligation IDs (or a deterministic scope
     selector), reason, reactivation condition, future evidence path, authority.
     A generic program hold is NOT a deferral unless it satisfies this.
D-2  Invalid, stale or contradictory facts derive REVIEW_REQUIRED, not a
     lifecycle state.
D-3  Fixtures must include fact-validity cases (generic hold, deferral without
     reactivation, evidence ref to a non-matching subject), not only function cases.
D-4  R2 must score inter-reviewer derived-state agreement on matched items.
```

## 9. Q8 — Does the R2 source-item method test the intended problem?

Frozen source-item IDs fix the paraphrase and anchor coupling. That is a real improvement. Six problems remain:

**(1) R2 measures the wrong mechanism.** Two reviewers extracting from frozen legacy prose tests §8 (legacy candidate extraction), which V0.4 itself says is never authoritative. It does not test §6–§7 (birth at acceptance), which is the mechanism the owner would accept. Birth at acceptance is not validated by inter-reviewer reproducibility. It is validated by:

- completeness: an independent auditor finds few accepted normative items missing from the declaration;
- precision;
- ambiguity rate: how often REVIEW is needed;
- authoring cost.

R2 needs an acceptance-birth arm. Replay real acceptance events with their change packages (the accepting commit diff plus the proposal). One agent authors the declaration set "at acceptance"; a second, independent agent audits it against the delta.

**(2) Segmentation can leak the answer.** Whoever chooses item granularity can encode unit boundaries. Segmentation must be:

- mechanical, by a frozen rule (every sentence, list item and code-block line), with no judgment merges;
- frozen before any key or control is authored;
- applied identically to all sources.

**(3) The same number is not the same threshold.** F1 ≥ 0.85 over pre-segmented item IDs is a much easier task than F1 ≥ 0.85 over free paraphrase. Presenting it as "original thresholds retained" is misleading. Most items will be non-normative, so the selection score also needs chance correction: report Cohen's kappa on normative/non-normative labels alongside F1 over selected items. Any threshold for the easier task needs its own preregistered justification.

**(4) Witnesses must not be named.** Sensitivity must be measured by the derived state (or a reviewer-flagged gap) on witness items that the packet does not identify (§4.3).

**(5) Key authorship symmetry.** The key and specificity controls must bind to item IDs, not wording, and be fixed before either reviewer starts. At least one reviewer must be blind to them. If the harness author is also a reviewer, add a third blind reviewer (a fresh instance with no MC-0029 context). Neither current reviewer is neutral about V0.4.

**(6) Cross-heading grouping.** The V0.1 schema forced one anchor per unit, which prevents grouping across headings even when the unit rule would require it. R2 units should be sets of item IDs with no anchor constraint.

## 10. Q9 — New falsifiers, burden and dependencies

```text
F-O1  State-attribution disagreement: derived-state agreement on matched items
      below a preregistered threshold after D-1 is applied -> KA-R52 third-state
      detection is not reproducible; the deferral model must change.
F-O2  Acceptance-birth auditor omission rate above threshold -> birth at
      acceptance does not close the upstream blind spot either.
F-O3  Declaration authoring cost per acceptance event above the DRP-08 budget
      -> simplify the declaration model before acceptance.
F-O4  Normative-kind taxonomy fails blind agreement (kappa below threshold) ->
      selection remains subjective; the taxonomy must change.
F-O5  REVIEW_REQUIRED rate per acceptance event too high for the owner to
      absorb -> ambiguity handling is itself an adoption failure.
```

Cross-layer effects:

- **WARRANT-F.** The G2 "no third state" claim needs a warrant whose witnesses are detected, not named (§4.3). Its admission value also depends on D-1.
- **AO-3.** The proposal-time declaration precondition is a new preflight obligation for governing-change proposals. For COOPERATIVE and UNMEDIATED collaborators, it is detective only (DRP-05b).
- **DRP-06.** Bounded orientation will display open obligations. With 45% state agreement, orientation would show contradictory obligation status. DRP-06 fixtures must not rely on obligation states until R2 passes.
- **DRP-07.** Agree with Research 326 that it must wait. It must additionally use the normative-kind taxonomy, because Specification 028 lineage is mostly CONSTRAINT and DISPOSITION items.
- **DRP-04.** It can proceed only for detectors that do not consume obligation state.
- **DRP-08.** It must include proposal-time declaration authoring and deferral-record authoring.

## 11. Disposition and required changes before a DRP-03 R2 harness is frozen

Research 326's core diagnosis holds: AMEND is valid, obligations are born at acceptance, legacy extraction stays candidate-only, and the derivation is kept. Its evidential claims and the R2 design need correction first.

Required before any DRP-03 R2 freeze:

```text
R2-REQ-1   Record the evidential scope correctly: reviewer-B false-gap NOT_BLIND and
           witness sensitivity INSTRUCTED_NOT_DETECTED, alongside the reviewer-A
           submetric defect. Reconcile the recorded result SHA-256 with the stored
           evidence bytes.
R2-REQ-2   Add the normative-kind taxonomy (OBLIGATION / CONSTRAINT / DISPOSITION /
           SEQUENCING / PRINCIPLE) with definitions and examples to V0.4.
R2-REQ-3   Add an operational realization-boundary definition (shared closing evidence
           event and shared failure).
R2-REQ-4   Specify the fact direction: realizing artifacts declare REALIZES/DEFERS
           toward obligation IDs; obligation records are immutable after birth.
R2-REQ-5   Add DeferralRecord validity rules (D-1) and REVIEW_REQUIRED for invalid,
           stale or contradictory facts (D-2); extend fixtures with fact-validity cases (D-3).
R2-REQ-6   Move declaration drafting to proposal authoring for COOPERATIVE/UNMEDIATED
           paths; define the closed list of governed acceptance-event kinds.
R2-REQ-7   Add temporal rules T-1 (text authoritative, declaration is interpretation),
           T-2 (clerical vs normative correction) and T-3 (owner-overridable holds).
R2-REQ-8   Add the legacy scope rule (§7) and detective-only use of candidate legacy units.
R2-REQ-9   R2 design: mechanical segmentation frozen before the key; unnamed witnesses
           detected by derived state; key bound to item IDs; chance-corrected selection
           metric plus a justified threshold; derived-state agreement metric; item-set
           units without an anchor constraint; at least one reviewer blind to the key,
           plus a third fresh blind reviewer if the harness author annotates.
R2-REQ-10  Add an acceptance-birth arm: replay real acceptance events with their change
           packages; author the declaration at "acceptance"; independent completeness and
           precision audit; ambiguity-rate and authoring-cost measurement.
R2-REQ-11  Register falsifiers F-O1..F-O5 and the downstream dependency notes for
           DRP-04, DRP-06, DRP-07 and DRP-08.
```

Final disposition for Research 326:

AMEND
