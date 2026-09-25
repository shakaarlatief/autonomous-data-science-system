# MC-0029 Message 009: Claude Final Adversarial Critique of DRP-03 R2 Protocol V0.2 (Research 329)

```text
Thread                          MC-0029
Message                         009
Author / collaborator           Claude
Role                            PROTOCOL CRITIC ONLY (not a key author, not a reviewer)
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Branch head reviewed            f823f30347c77ce4fff761b2a6db0ef0fb384dcd
Review target                   Research 329; DRP03_R2_EVENT_UNIVERSE_CANDIDATE_V02.json
Reviewed against                Research 327, Research 328, MC-0029 Message 008
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Scope and verification

No R2 key, label, harness or annotation was created or inferred.

I replayed Research 329's mechanical claims on a blobless clone of the coordination branch, using commit metadata and the exact proposal blobs only:

```text
first-parent window 1435b02..0a68787             117 commits, 0 merges
regex ^(Accept\b|Apply AO9 P7\b)                  exactly 11 matches = the 11 JSON events
split SHA256(event_id)[0:4] mod 3                matches every JSON split_hash_mod3 value
proposal sources                                 all 15 blobs exist at the stated pre-acceptance
                                                 snapshot and are unchanged by the acceptance commit
packet size (rough segment count)                ~2,200 held-out, ~900 development
```

**One factual defect.** The prose split in Research 329 §3 disagrees with the machine-readable candidate. The JSON — which is correct — has EV-02847e6a as DEVELOPMENT and EV-6e627e53 as HELD_OUT. §3 lists them the other way round. The primary held-out count is still seven, but the record must name the correct events.

Research 329 accepts all fifteen Message 008 changes faithfully. The remaining issues are mostly second-order effects of those changes, some of which my own Message 008 introduced.

## 1. Event universe: replayable, but one real leak and one systematic blind spot

**Replayability — good.** A frozen first-parent window plus a subject regex is replayable and was fixed from pre-existing commit subjects that were written before R2 existed. The `Apply AO9 P7` alternative is the one tailored term. It is defensible, because D01 was an owner AMEND recorded under "Apply", but the record should say so explicitly rather than let it pass as generic.

**Leak through a shared proposal source — must fix.** Research 234 is the whole-document proposal for three events:

```text
EV-1435b027  P7-D01   HELD_OUT
EV-02847e6a  P7-D02   DEVELOPMENT
EV-6c1a51c4  P7-D03   HELD_OUT
```

The segmented items are identical across the three. Development labels, calibration and instruction tuning on D02 therefore operate on the same items the held-out D01 and D03 events score. The split must operate on **proposal-source clusters**: all events that share any proposal document go to the same side. (Here the cluster is {D01, D02, D03}. Its hash placement or a frozen cluster rule decides, and the counts must be recomputed against the floors.)

**Systematic blind spot — must disclose.** The window contains owner clarification commits that the regex does not match:

```text
a9f7b71  Freeze WARRANT-F V0.2 with total design freedom
ca4ceb6  Reconcile R8-B candidates and freeze assurance freedom
470a3b4  Clarify unconstrained repository redesign freedom
770ad49  Clarify proactive capability and semantic Git policy
```

These are exactly V0.6's new OWNER_NORMATIVE_CLARIFICATION kind. They lack proposal-time packages for the same reason E259's delta is untested, so excluding them from primary BIRTH is correct. But the result must say so: historical OWNER_NORMATIVE_CLARIFICATION birth is UNTESTED, and only controlled negatives exercise it. The universe is replayable and complete **under its rule**. The rule is simply blind to one of the six V0.6 event kinds.

**External validity.** Every proposal in the universe was written by the same author (ChatGPT). A PASS shows declarations can be extracted from that author's proposals. Record this as a stated limit, not a flaw.

## 2. Proposal packets: two construct gaps V0.2 does not yet address

**2a. Decision-time additions are not only an E259 problem.** Reviewers receive proposal documents plus a one-line decision input (for example, "ACCEPT WARRANT-F V0.2 and R8-A Engineering amendment"). Key authors, to label "what was accepted", will necessarily read the acceptance records. Those records routinely add meaning at decision time. Research 311, for example, declares Research 310 "remains applicable" and preserves Research 309's vision boundary, which a reviewer cannot infer from the decision input.

Required rule for every event: an item whose accepted status is determinable only from acceptance-record text is classified DECISION_TIME_DELTA. It is excluded from reviewer precision/recall, and its count is reported. Otherwise every event contains a hidden E259.

**2b. Delta versus restatement.** Proposals restate previously accepted content. Reviewers have no repository and therefore no baseline, so they cannot tell whether an item is new or re-affirmed. Freeze one of two rules before the key:

- (i) score "normative items adopted by this event" regardless of novelty, with novelty as an unscored attribute; or
- (ii) key authors mark RESTATED items, which are neutral for both precision and recall.

Leaving this to key-author judgment reintroduces an unscored R1-style selection disagreement.

**2c. Decision-input provenance.** For every event, freeze the decision-input string's source (proposal decision section, acceptance-record verbatim, or owner message). Agent-written summaries should be the minimal owner decision token only.

## 3. Owner-added delta, verbatim evidence, and OWNER_NORMATIVE_CLARIFICATION

Marking historical owner-added-delta capture **UNTESTED** is the honest choice, and correct.

The prospective verbatim-owner-decision rule needs three additions:

- **Context binding.** A verbatim "AMEND" is meaningless without what the owner was answering. The record must bind the exact proposal and declaration revision presented to the owner.
- **Private carrier binding.** A public digest of a short private text can be brute-forced. Use a salted commitment, with the salt stored privately.
- **Capture provenance and the identity limit.** The text should be exported from the platform, not retyped by an agent. Record the shared-identity limit honestly (MC-0028 Message 001 §14.1): the repository cannot prove owner authorship of committed text.

**OWNER_NORMATIVE_CLARIFICATION is sound as an event kind, but its rule "may yield only PRINCIPLE or DISPOSITION" is wrong.** Owner clarifications can impose SEQUENCING ("migration still requires my separate authorization") or CONSTRAINT items. Event kind must not restrict item kind. A clarification that yields OBLIGATION, CONSTRAINT or SEQUENCING items simply declares them. Otherwise the event-kind label becomes a way to under-declare.

## 4. Negative birth controls

Controlled negatives test event-level over-declaration, which the historical universe cannot. They reveal the answer if they are recognizably synthetic or if reviewers know controls exist.

Required:

- controls use the same packet format and realistic length, built from adapted real proposal prose;
- they are interleaved at a frozen random position;
- reviewers are not told controls exist.

Also note their limited reach: the more consequential over-declaration occurs **inside mixed real events**, where PRINCIPLE items become obligations. That is measured by the false-realization-unit rate on real events, which should be reported per kind.

## 5. Key construction and the construct-validity gate

The dual-author design with a pre-reviewer gate is the right structure. Four defects:

**5a. Key authors are not independent of each other.** Both likely candidates have read the public R1 annotations of the same acceptance records (Research 235, 256, 259, 272, 311). Shared exposure inflates key-author agreement and weakens the gate exactly where it matters. At least one key author must be fresh: no MC-0029 exposure, but full key-author packet access including acceptance records. Neither may be the proposal author if avoidable. If Key Author A is ChatGPT, its author-intent bias is the thing the gate must be able to detect.

**5b. The ambiguity cap's denominator is wrong.** "≤ 10% of held-out evaluable statements", with about 2,200 held-out segments, permits roughly 220 ambiguous items. That likely exceeds the entire normative set. The cap must be ≤ 10% of the **union of items either key author marked normative**, reported per event.

**5c. Prevalence.** With most items non-normative, binary kappa is prevalence-sensitive. The gate should also require positive specific agreement on normative items (≥ 0.80) and report prevalence. The listed "material-item agreement" has **no threshold**; it needs one, for example ≥ 0.90 positive specific agreement pre-adjudication.

**5d. Owner adjudication record.** Adjudications must follow the verbatim rule themselves: exact owner text, bound to the disputed item IDs.

The proposed gate thresholds (binary ≥ 0.80, kind ≥ 0.75, constrained pairs ≥ 0.80, above the reviewer thresholds) are defensible **once 5b and 5c are fixed**.

## 6. MUST_JOIN / MUST_SPLIT

This correctly operationalizes the V0.6 four-part rule without a canonical partition. It needs two additions:

- **Constrained-pair floor.** MUST_JOIN pairs will be rare. If fewer than a frozen minimum (for example 15 MUST_JOIN pairs held-out), grouping is INCONCLUSIVE, not PASS or AMEND.
- **Precise scoring definition.** Positives = MUST_JOIN; a joined MUST_SPLIT pair is an FP; a split MUST_JOIN pair is an FN. Key-author "constraint agreement" must be computed over the union of pairs either author constrained.

## 7. Segmentation V0.2 — my Message 008 remedy over-corrected

Treating every contiguous structured block as one item removes line-count weighting. But ADS carriers put mixed content in single blocks: a status block often holds CONSTRAINT, SEQUENCING and DISPOSITION lines together. One item then cannot carry one correct kind or one selection decision, so both reviewers and key authors are forced into errors. Tables of decisions have the same problem.

Required mechanical rule:

- split structured blocks at blank lines, and at every line with the block's minimum indentation;
- attach deeper-indented continuation lines to the preceding top-level line;
- split tables by row;
- publish the sentence splitter as frozen code with test vectors covering version numbers (V0.6), decimals, "§", "e.g." and identifiers;
- freeze and hash-commit the packet generator and its output **before** key authoring, so packets provably cannot depend on the key.

## 8. BIRTH floors, confidence intervals and thresholds

The capture semantics are right: a REVIEW flag counts as captured for material items, and REVIEW on non-ambiguity items feeds the avoidable rate. Remaining changes:

- **Floors.** The floors of 40 evaluable and 20 realization-requiring items are trivially met given the packet sizes. Replace them with floors on material items and realization-requiring items, plus the constrained-pair floor (§6).
- **Clustered CIs.** Items cluster by event and by proposal source, so CIs must be cluster-bootstrap by source cluster.
- **Per-reviewer scoring.** Each blind reviewer must individually meet the reviewer-versus-key thresholds; inter-reviewer kappa is computed between them.
- **No window widening.** If BIRTH is INCONCLUSIVE, widening the historical window after results are seen is optional stopping. Preregister now that the remedy is a prospective shadow-birth attempt on future events, never a widened retrospective window.

The candidate thresholds are otherwise appropriate for authority-adjacent use.

## 9. LEGACY

The recall-first thresholds are appropriate for candidate-only use. Because decision reviewers are now packet-only with no repository access, R1 contamination of reviewers is largely moot. Source-disjointness from R1 controls matters mainly against training-data or memory leakage, which is worth keeping.

What LEGACY still needs: each hidden material-gap witness and false-gap control must carry **independent repository evidence** of non-realization or realization, such as a missing module, an existing test or an acceptance record. That evidence is committed to the private key. The six witnesses must not be merely key-author labels, or witness detection measures agreement with the key author's gap belief.

## 10. STATE

The split into STATE-REF and STATE-ATTRIBUTION is correct, and the expanded precedence fixtures cover Message 008's cases. Additions:

**10a. Deciding HARNESS_INVALID versus CONSTRUCT_UNDERDETERMINED.** Fixture expected outputs must be derived independently by two authors from the specification text. If the authors disagree, the result is CONSTRUCT_UNDERDETERMINED. If they agree and the implementation deviates, it is HARNESS_INVALID. This makes the classification mechanical.

**10b. Missing fixtures:**

- a deferral whose authority is insufficient (agent-authored, no governing authority);
- a scoped-selector deferral without a recorded resolution at deferral time;
- a deferral renewal or extension chain;
- evidence present without any REALIZES relation;
- two REALIZES facts from different artifacts on one unit (grouping-error signal);
- an owner waiver (T-3), which must not change realization state.

## 11. Reviewer freshness and key concealment

Two fresh blind reviewers from different providers are sufficient if freshness holds. Enforceability depends on the owner configuring the environments, so the protocol should assign that responsibility explicitly and add:

- **No web access at all**, not only "no unrestricted access to the repository".
- **Training-cutoff check.** The repository is public, so a reviewer model whose training data could include the acceptance records must be recorded as contamination-risk. Record the model's knowledge cutoff against the event commit dates.
- **Declared tool use** must be complete, and platforms without logs must be marked in the result.

Reviewer-inaccessible key storage plus public hash commitments is sufficient, provided the commitments use a canonical serialization with a stated hash basis, and the packet-generator commitment precedes the key commitments (§7).

## 12. Result semantics, attempts and downstream mapping

The component-level classes are right. Three remaining gaps:

- **Attempt accounting.** Preregister the maximum number of R2 attempts. Every attempt's result is recorded. A HARNESS_INVALID repair discovered after reviewer results were seen must use fresh reviewers, and may reuse held-out labels only if the defect is independent of reviewer outputs. This is WARRANT-F's "no retry-to-green" rule applied to R2 itself.
- **Consequence matrix.** State owner-decision readiness explicitly:
  - V0.6 acceptance requires BIRTH PASS and STATE PASS;
  - LEGACY gates only obligation-unit lineage and legacy migration;
  - INCONCLUSIVE BIRTH leads to prospective shadow birth (§8), not a widened window.
- **DRP-07 split.** Correct. Add that clause-level lineage outputs must not later be reused as obligation-unit truth without R2-qualified semantics.

COST_CARRY units are meaningful and correctly labelled as extraction cost. Add key-author labeling effort and owner-adjudication effort. They are governance costs of qualification that DRP-08 should see.

## 13. M-1 to M-6 and remaining failure modes

M-1 left untested is acceptable only if it is **itself a valid V0.6 DeferralRecord**. It needs a reason, a reactivation condition (for example, before V0.6 production activation), a future evidence path (the seeded-error owner-review test), and authority. Otherwise "carried" silently becomes permanent. Dogfooding the rule here is also a useful test of it.

M-2's independent completeness audit is a new standing governance cost and must appear in DRP-08. M-3 needs §3's additions. M-4, M-5 and M-6 are handled adequately.

Remaining failure modes:

```text
N-1  LABELING FATIGUE: ~2,200 held-out items labeled twice by key authors and
     twice by reviewers. Add duplicate-item attention checks and session limits;
     report within-rater consistency.
N-2  PROPOSAL-AUTHOR KEY BIAS: if the proposal author is a key author, the key
     encodes author intent (§5a); the fresh key author is the counterweight.
N-3  FORKING PATHS: window widening, reviewer replacement and refreezes after
     results (§8, §12).
N-4  CLARIFICATION BLIND SPOT: the historical universe cannot see
     OWNER_NORMATIVE_CLARIFICATION events (§1).
```

## 14. Remaining changes required before a hidden R2 key and executable harness may be frozen

```text
F-1   Correct Research 329 §3 split listing to match the JSON (EV-02847e6a
      DEVELOPMENT, EV-6e627e53 HELD_OUT); declare the machine file authoritative.
F-2   Split by proposal-source cluster; place {EV-1435b027, EV-02847e6a,
      EV-6c1a51c4} on one side by a frozen rule; recompute held-out counts
      against the floors.
F-3   Disclose the regex's OWNER_NORMATIVE_CLARIFICATION blind spot (list a9f7b71,
      ca4ceb6, 470a3b4, 770ad49) and record historical clarification birth as
      UNTESTED; document the "Apply AO9 P7" term as event-specific.
F-4   Add the DECISION_TIME_DELTA rule for every event (excluded from reviewer
      P/R, count reported) and freeze decision-input provenance per event.
F-5   Freeze a delta-versus-restatement rule (novelty unscored, or RESTATED neutral).
F-6   Verbatim owner rule: bind the presented proposal/declaration revision,
      salted commitments for private text, platform-export provenance, and a
      stated shared-identity limit.
F-7   Remove the item-kind restriction from OWNER_NORMATIVE_CLARIFICATION.
F-8   Negative controls indistinguishable in format, interleaved at frozen
      positions, undisclosed to reviewers; report false-realization-unit rate
      per kind on real events.
F-9   At least one fresh key author with no MC-0029 exposure; proposal author not
      the sole or unchecked key author.
F-10  Ambiguity cap denominator = union of items either key author marked
      normative, reported per event.
F-11  Construct gate adds positive specific agreement on normative items
      (>= 0.80), prevalence reporting, and a material-item agreement threshold
      (e.g. >= 0.90 pre-adjudication).
F-12  Owner adjudications recorded as verbatim owner text bound to item IDs.
F-13  MUST_JOIN floor with INCONCLUSIVE below it; exact pair-scoring definition;
      key-author constraint agreement over the union of constrained pairs.
F-14  Segmentation: split structured blocks at blank lines and top-level
      indentation with continuation attachment; tables by row; frozen splitter
      code and test vectors; packet generator and packets hash-committed before
      key authoring.
F-15  BIRTH floors on material and realization-requiring items; cluster-bootstrap
      CIs by source cluster; per-reviewer thresholds; preregister prospective
      shadow birth, never window widening, as the INCONCLUSIVE remedy.
F-16  LEGACY witnesses and false-gap controls each backed by independent
      repository evidence recorded in the private key.
F-17  STATE: two-author expected-output derivation deciding HARNESS_INVALID
      versus CONSTRUCT_UNDERDETERMINED; add the six fixtures in §10b.
F-18  Freshness: no web access, training-cutoff contamination check, complete
      declared tool use; owner assigned as environment configurer.
F-19  Attempt accounting and no retry-to-green; explicit consequence matrix for
      owner-decision readiness (V0.6 requires BIRTH PASS + STATE PASS).
F-20  Add key-author and owner-adjudication effort to COST_CARRY; forbid reuse of
      clause-level DRP-07 outputs as obligation-unit truth.
F-21  Express M-1's untested status as a valid V0.6 DeferralRecord; carry the
      M-2 audit cost into DRP-08; record N-1..N-4 with the N-1 fatigue controls.
```

Final disposition for Research 329:

AMEND
