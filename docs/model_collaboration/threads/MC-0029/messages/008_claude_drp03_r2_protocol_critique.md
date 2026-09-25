# MC-0029 Message 008: Claude Adversarial Protocol Critique of the DRP-03 R2 Preregistration Candidate

```text
Thread                          MC-0029
Message                         008
Author / collaborator           Claude
Role                            PROTOCOL CRITIC (not an R2 reviewer)
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Branch head reviewed            35f874bb30a15d8450a4ef39e681758475e25374
Review target                   Research 328 (DRP-03 R2 exact preregistration candidate)
Reviewed against                Research 327 (V0.5), Message 007, Research 316, accepted R5-R8C
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Scope and method

This is a protocol critique. No hidden R2 key or harness exists; I created none and inferred none. I produced no R2 annotation.

I verified Research 328's mechanical claims against repository history, using a blobless clone of the coordination branch for commit metadata only:

```text
split rule SHA256(event_id)[0:4] mod 2     reproduces exactly:
                                           E256, E311 DEVELOPMENT; E235, E248, E259, E272 HELD_OUT
each "pre-acceptance snapshot"             is the direct parent of its acceptance commit
```

Two claims do **not** survive history (§1, §2).

Research 327's reconciliation of Message 007 is faithful. The critique below concerns only whether Research 328 measures V0.5 fairly.

## 1. Q1 — The event universe is not mechanically bounded

Research 328 describes the six events as "mechanically bounded to six explicit owner/governance acceptance records used in the R7-R8/AO transition program for which a pre-acceptance proposal snapshot exists". The branch history between the AO-9 closure and R8-C contains more owner-acceptance commits than the six selected:

```text
33af354  Accept G-DUAL and preserve from-scratch lower levels     (Research 246)  EXCLUDED
8c85be8  Accept G-DUAL amendment and unblock R6                   (Research 248)  E248
39a5f8f  Accept R6 bounded-context architecture                   (Research 251)  EXCLUDED
1d91d0d  Accept amended R7 architecture and unblock R8            (Research 256)  E256
1819914  Accept amended R8-A and freeze representation freedom    (Research 259)  E259
46bc4ee  Accept MC-0027 audit and freeze corrected probe          (probe contract) EXCLUDED
6e627e5  Accept WMR-H V0.3 and close MC-0027                      (Research 272)  E272
0a68787  Accept WARRANT-F V0.2 and close R8-C                     (Research 311)  E311
1435b02  Apply AO9 P7 D01 amendment                               (AO-3 §24)      folded into E235
02847e6  Accept AO9 P7 D02 requirement                            (KA-R51)        folded into E235
6c1a51c  Accept AO9 P7 D03 and close AO9                          (Research 235)  E235
```

The G-DUAL amendment (E248) is included while G-DUAL itself (Research 246) and R6 (Research 251) are not. No stated rule produces that set. Selection by the protocol author, who also authored every proposal and acceptance record, is exactly where home-field advantage enters (Q10).

Representativeness is also narrow:

- **One event kind.** All six are large OWNER_DECISION_ACCEPTANCE events for architecture stages. None is a REQUIREMENT, POLICY/PROFILE or AUTHORITY/CUTOVER acceptance of the kinds V0.5 §8 enumerates, although KA-R51 and KA-R52 inside E235 are requirement acceptances in substance.
- **No negative birth event.** Every event creates realization units. CREATES_NO_REALIZATION_UNITS is never exercised, so over-declaration on a null event is untested.
- **Four held-out events.** Every rate threshold is decided by a few dozen items.

Required change: define the universe by a written, replayable selection rule over commit history — for example, every commit that adds or modifies an owner-decision record between two frozen boundary commits. Then classify each candidate by event kind. Include at least one pure-DISPOSITION or PRINCIPLE acceptance as a negative birth control, and at least one requirement-kind acceptance. Record exclusions with reasons before any key authoring.

## 2. Q2 — E235's snapshot leaks accepted outcomes

E235's "pre-acceptance snapshot" `02847e6` is itself the acceptance commit for P7-D02. Its parent `1435b02` applied P7-D01. At the snapshot:

- Research 222 §24 (the accepted D01 amendment) is present;
- Requirements V0.2 already contains accepted KA-R51;
- the AO-9 reconciliation JSON is updated.

The packet exposes "exact pre-acceptance snapshot commit", so a reviewer would see two of the three accepted deltas the event asks them to declare. Research 328's assurance that "no acceptance record itself is reviewer-visible" is true of Research 235 but not of the accepted text.

Required change: split E235 into E235-D01 (snapshot `b908fe0`), E235-D02 (snapshot `1435b02`) and E235-D03 (snapshot `02847e6`). Alternatively, treat it as one event with snapshot `b908fe0`. Add a mechanical temporal-fairness check for every event: no packet file may contain text that first appears in or after the acceptance event's first commit.

A broader fairness issue follows. "Exact pre-acceptance snapshot" means the reviewer gets the whole repository at that commit. It must be stated whether the reviewer sees only the bounded packet or the full snapshot. The full snapshot contains CURRENT_STATE, routing and checkpoints, which often pre-announce the expected decision.

## 3. Q3 — E259 does not test what it claims

E259 is meant to test incorporation of an owner-added decision-time delta. The only repository carrier of that owner clarification is Research 259 §2 itself. That is the acceptance record, written after the decision by the protocol author, in the protocol author's words.

A packet that supplies "explicit owner decision-time text" must therefore excerpt the acceptance record. Two consequences:

- The input is the key author's rendering, which trivially aligns with the key.
- "Incorporation = 100%" then measures transcription of text handed to the reviewer, not the real risk: failing to capture an owner addition that exists only in conversation.

Required change: E259's decision-time input must be the owner's verbatim decision message, with provenance (a chat export or the owner's own statement). If no verbatim record exists, E259 cannot score owner-added-delta capture and must be excluded from that metric, or moved to development.

Operationally this exposes a missing V0.5 rule: every acceptance event should persist the owner's verbatim decision text as evidence, so owner-added deltas are never known only through an agent's paraphrase.

## 4. Q4 — The hidden key would be one more opinion

For R2-BIRTH the ground truth is "what the owner accepted". Research 328 has that truth authored by ChatGPT, who wrote every proposal and every acceptance record. The key then encodes author intent, which is not the same as owner acceptance. It is also the same construct error R1 had: one reviewer's reading treated as truth.

Required change:

- Author the held-out key independently twice: the protocol author plus one further key author who is not a decision reviewer.
- Report inter-key-author agreement (binary normativity kappa and kind kappa) **as a construct-validity gate before reviewers run**. If key authors cannot agree above the reviewer thresholds, the taxonomy is underdetermined (F-O4). Scoring reviewers against a contested key would be meaningless.
- Resolve key-author disagreements on material items by owner adjudication. Record residual disagreement as a frozen, capped allowed-ambiguity set (for example, at most 10% of held-out items), reported with the result so it cannot silently absorb failures.

## 5. Q5 — Grouping key: score constraints, not canonical groupings

For future obligations, the V0.5 four-part test ("same evidence event", "same qualification decision") is a prediction about realization that has not happened yet. Enumerating "canonical or allowed-equivalent groupings" would force the key author to pick among defensible alternatives: the R1 problem again.

Required change: express the grouping key as pairwise constraints.

- **MUST_JOIN:** item pairs that the four-part test clearly unites, such as clauses of one gate or one realization artifact.
- **MUST_SPLIT:** pairs with different owners, different realization artifacts or independent failure.
- All other pairs are unconstrained.

Score grouping F1 only on constrained pairs, and report the unconstrained fraction. This makes the key checkable against the rule instead of against the key author's taste.

## 6. Mechanical segmentation still encodes weight and boundaries

The segmentation rule is mechanical in principle, with three leaks:

1. **Inconsistent granularity.** A multi-sentence list item is one item, while the same text as a paragraph is several. The author's formatting choices, made while knowing the answer, set how many items a statement produces.
2. **Code-block fragmentation.** ADS acceptance records put much normative content in indented blocks: state lists, arrow flows, gate lists. "One item per non-empty semantic line/row" splits a single arrow-flow statement into many items, and "semantically addressable" is a judgment, not a rule. Item-weighted precision and recall then weight a statement by its line count.
3. **Heading selection.** "Allowed headings ... selected only to capture the explicit decision package" is chosen by the key author, who knows the accepted delta. Restricting the packet to relevant sections pre-solves selection and inflates precision.

Required changes:

- One segmentation rule for all block types, with no "semantic" qualifier. For example: a contiguous non-blank block of structured lines is one item; prose and list items split by the same sentence rule.
- Report item-weighted and statement-weighted metrics, with statement-weighted metrics deciding.
- Scope each proposal carrier as a whole document, or by a mechanical rule such as "sections referenced by the decision input". It must never be curated.

## 7. Q6 — BIRTH thresholds

The direction is right: authority adjacency justifies BIRTH thresholds stricter than LEGACY, and zero material omissions is the correct hard floor. Four corrections:

- **REVIEW flags must count as capture.** A material item the reviewer flags as ambiguous (REVIEW_REQUIRED naming that item) is captured-with-review, not an omission. The mechanism escalates exactly that case.
- **Sample-size floor.** State the minimum held-out realization-requiring item count, statement-weighted. Below it the result is INCONCLUSIVE, not PASS. Report confidence intervals: with around 40 items, 0.90 is decided by one or two errors.
- **Avoidable REVIEW rate needs a definition.** "Avoidable" must be defined mechanically as a REVIEW flag on an item outside the frozen allowed-ambiguity set. Otherwise the key author decides what was avoidable.
- **Contamination.** Kappa "between reviewers" must be computed only between blind reviewers (§10).

## 8. Q7 — LEGACY thresholds

Weaker thresholds are appropriate because the output is candidate-only. But the asymmetry is wrong. For migration-safety evidence a missed gap is costly and a spurious candidate is cheap, because it goes to review. Recall should be at least the BIRTH level (≥ 0.90), with precision relaxed (for example ≥ 0.75).

The LEGACY held-out corpus as listed (Specification 028 obligation and gate sections, Research 311 Engineering, Research 225 §16) is the R1 corpus. R1's `evaluator_key.json` is public in the repository and names the three witnesses and ten false-gap controls. Any reviewer with repository access can read them.

Required change: LEGACY hidden witnesses and false-gap controls must be new identities not present in any R1 artifact, or the blind reviewer must have no repository access (§10). Witness detection of 100% on three items is fine as a floor but needs more than three witnesses to mean much. Six or more is suggested.

## 9. Q8 — STATE: mostly right, three gaps

The fixture list covers the R1 failure well: generic hold, missing reactivation or evidence path, stale, contradictory, wrong subject. Its framing of real attribution as validating source-owned facts matches V0.5's natural-owner direction. Three gaps:

1. **Precedence is under-specified.** "Invalid / stale / contradictory required facts → REVIEW_REQUIRED" precedes DEFERRED, but "required" is undefined. Add fixtures for:
   - a valid deferral plus a stale irrelevant evidence fact;
   - a deferral whose reactivation condition has already occurred (a stale deferral);
   - a scoped-selector deferral whose resolved set excludes the obligation;
   - a SUPERSEDED governing parent, to prove the governing and realization lifecycles stay separate.
2. **Real distractors.** Held-out candidate facts must include verbatim real holds from the repository (the "Still held" / "not authorized" blocks), not only synthetic ones. Those are what caused the R1 split.
3. **Reference implementation versus reviewer.** Fixture accuracy of 100% should be run against a reference implementation of the V0.5 validity and derivation rules; a failure there is a specification or harness defect. Reviewer attribution agreement is a separate measurement. Mixing them turns rule-comprehension errors into architecture AMENDs.

The "real/candidate source-fact mappings" corpus for the 0.90 agreement threshold is not specified. It must be frozen with the harness.

## 10. Q9 — Reviewer independence and concealment are not yet sufficient

**Contamination of Claude-04.** R1's primary sources were the acceptance records of events 217, 235, 256, 259, 272 and 311. Claude-04 annotated the accepted obligations of **three of the four held-out BIRTH events** (E235, E259, E272) and both development events. Its R2 annotation cannot count toward any inter-reviewer threshold. Research 328 §8 and §11 currently compute binary kappa, kind kappa and cross-reviewer grouping F1 "between reviewers", which would include it.

Required: inter-reviewer thresholds use two fresh blind reviewers. Claude-04 output is descriptive only.

**Operational definition of "fresh".** In this environment a new Claude interaction inside the same Claude Project inherits project memory and can search past conversations. ChatGPT memory can carry the same contamination. "Fresh" must mean all of the following:

- no project or account memory;
- no past-chat search;
- no Git-host connector, or a connector restricted to the published packet;
- packet files supplied directly;
- an attestation plus a tool-call log retained as evidence.

**Key concealment.** In R1 the hidden key was committed to the repository and blindness relied on honor. For R2, freeze the key by hash commitment: publish the SHA-256 at freeze and keep the key out of every reviewer-accessible location until all annotations are frozen, then publish it. The same applies to held-out labels for development-versus-held-out integrity.

**Two blind reviewers from different providers** are preferable, so that shared model priors do not masquerade as agreement.

## 11. Q12 — Result semantics

PASS / AMEND / HARNESS_INVALID is too coarse:

- **Component results.** Report BIRTH, LEGACY and STATE separately, and map their consequences. BIRTH PASS with LEGACY AMEND should not block V0.5's birth mechanism, but must block DRP-07's use of legacy extraction.
- **Add INCONCLUSIVE** for below-floor sample size or confidence intervals straddling a threshold.
- **Add CONSTRUCT_UNDERDETERMINED** for failure of the inter-key-author gate (§4). That is F-O4 evidence, not a harness defect.
- **COST_CARRY units.** Freeze its units now: items, units, tokens or minutes per event, REVIEW count, owner-intervention count. Mark it explicitly as *extraction-from-proposal* cost, which is not the cost of authoring declarations during proposal writing. DRP-08 must not reuse it unadjusted.

## 12. Downstream holds

The four holds are correct, with two refinements:

- **DRP-07** can be split. Clause-level Specification 028 lineage (section → disposition → successor) does not depend on obligation units and can proceed. Only obligation-unit lineage waits for R2.
- **DRP-08** must treat R2 cost as a lower- or upper-bound proxy (§11), not the target mechanism's cost.

DRP-04 and DRP-06 holds are right as stated.

## 13. Q11 and Q12 — Missing whole-system failure modes

```text
M-1  OWNER RUBBER-STAMP / AUTHORITY LAUNDERING
     V0.5 makes an agent-drafted declaration part of what the owner accepts
     (T-1: "accepted structured interpretation"). If the owner approves a
     12-unit set without scrutiny, agent errors acquire accepted status.
     V0.5 needs: agent-drafted provenance on every declaration item, a
     material-items-first summary for owner review, and a light T-2 correction
     path for agent-drafting errors. R2 should include at least one
     seeded-error proposal declaration and record whether review catches it,
     or state honestly that owner-review efficacy is untested.

M-2  PROPOSAL-AUTHOR INCENTIVE
     In operation the proposal author drafts its own declaration and could
     under-declare to reduce apparent burden. V0.5 needs an independent
     completeness audit in operation (at least sampled), not only in R2.

M-3  CHAT-ONLY OWNER DELTAS
     Owner decisions arrive in conversation and are transcribed by an agent.
     Without a verbatim-decision persistence rule (§3), owner-added deltas are
     unrecoverable except through paraphrase.

M-4  BOOTSTRAP
     V0.5's own acceptance will be the first event needing a declaration set,
     and there is no accepted mechanism yet. The first declaration must be
     explicitly marked bootstrap, independently audited and re-validated once
     the mechanism is accepted.

M-5  HOLD-TO-DEFERRAL MIGRATION BURDEN
     Under V0.5 validity rules most current program-level holds are not valid
     DeferralRecords. Adoption would turn many currently "held" obligations
     into REVIEW_REQUIRED or UNLINKED at once. DRP-08 must include the
     conversion cost, and the transition plan must stage it.

M-6  ASSURANCE REUSE
     R2's hidden witnesses and false-gap controls should become the WARRANT-F
     sensitivity and specificity witnesses of the G2 "no untracked third
     state" claim, with the same concealment discipline. Otherwise the warrant
     is instruction-tested again.
```

## 14. Required changes before the hidden R2 key and executable harness may be frozen

```text
R2P-1   Replace the six-event selection with a written, replayable selection rule
        over commit history; enumerate all candidates (including Research 246, 251
        and the AO-9 P7 D01/D02 commits) with inclusion/exclusion reasons; classify
        by V0.5 event kind; add at least one negative birth event
        (DISPOSITION/PRINCIPLE only) and one requirement-kind event.
R2P-2   Fix E235 temporal leakage: split into D01/D02/D03 events with their true
        parent snapshots, or use b908fe0 as the single snapshot; add a mechanical
        check that no packet text first appears at or after the acceptance event.
R2P-3   State whether reviewers see only the bounded packet or the full snapshot;
        if the full snapshot, exclude or neutralize live-state carriers that
        pre-announce decisions.
R2P-4   E259: use the owner's verbatim decision message with provenance, or remove
        E259 from the owner-added-delta metric. Add a V0.5 rule to persist verbatim
        owner decision text at every acceptance event.
R2P-5   Two independent held-out key authors; an inter-key-author agreement gate
        before reviewers run; owner adjudication of material disagreements; a
        capped, frozen, reported allowed-ambiguity set.
R2P-6   Grouping key as MUST_JOIN / MUST_SPLIT pair constraints scored only on
        constrained pairs, with the unconstrained fraction reported.
R2P-7   Segmentation: one rule for all block types with no "semantic" judgment;
        contiguous structured blocks as single items; statement-weighted metrics
        decide; proposal scope whole-document or mechanically derived, never curated.
R2P-8   BIRTH: count REVIEW-flagged material items as captured; freeze a minimum
        held-out sample size with INCONCLUSIVE below it; report CIs; define
        "avoidable REVIEW" mechanically against the allowed-ambiguity set.
R2P-9   LEGACY: recall >= 0.90 with relaxed precision (e.g. >= 0.75); new hidden
        witnesses and false-gap controls not present in any R1 artifact (or no
        repository access); at least six witnesses.
R2P-10  STATE: add the precedence and temporal fixtures in §9; include verbatim real
        repository holds as distractors; run fixtures against a reference
        implementation separately from reviewer attribution; freeze the real
        fact-mapping corpus.
R2P-11  Independence: inter-reviewer thresholds only between two fresh blind
        reviewers (preferably different providers); Claude-04 descriptive only;
        operational freshness definition (no memory, no past-chat search, no
        repository access beyond the packet, retained tool-call logs).
R2P-12  Key concealment by hash commitment; the key and held-out labels are
        published only after all annotations are frozen.
R2P-13  Result semantics: per-component results with mapped downstream
        consequences; add INCONCLUSIVE and CONSTRUCT_UNDERDETERMINED; freeze
        COST_CARRY units and label them extraction-from-proposal cost.
R2P-14  Downstream: split DRP-07 into clause lineage (may proceed) and
        obligation-unit lineage (held); DRP-08 treats R2 cost as a bounded proxy.
R2P-15  Record M-1..M-6 in V0.5 as open failure modes, with at least the seeded-error
        owner-review check (M-1) either included in R2 or explicitly declared untested.
```

Final disposition for Research 328:

AMEND
