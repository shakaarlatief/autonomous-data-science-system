# MC-0016 Message 001: Claude Adversarial Review of Candidate 01

```text
Thread                          MC-0016
Message                         001
Author / collaborator           Claude
Role                            ADVERSARIAL REVIEWER
Interaction environment         Claude
Project / workspace             Autonomous Data Science System
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Repository head reviewed        dc083fa46ebad8c5b83cbc59f5ccaa21bcdb26f6 (routing only)
Exact review target             69aed186a0d63b3c395a133cd920099d5fa8e000
Candidate                       PKA-CANDIDATE-01
Purpose                         Adversarial review of the first whole-architecture candidate and its
                                 claimed 50 KA-R / 17 KA-I design-coverage, per the MC-0016 brief
```

I read Requirements V0.2, Research 143, Research 144 (the candidate), Research 145 (the coverage/qualification plan) and `QUALIFICATION_MATRIX_V01.json` in full at the exact target commit. I checked the JSON against the markdown table (they match) and treated the 50/50 + 17/17 coverage claim as something to independently re-derive, not accept.

## A. Candidate architecture coherence

Mostly coherent -- the identity/authority-mode axes from Research 143 are applied consistently throughout, and the nine responsibilities genuinely compose rather than competing for the same territory. But three specific seams don't fully interlock, and I want to name them precisely rather than gesture at "some rough edges":

**Prose-procedure edits and the structured action contract can drift with no detector.** Section 7 puts a structured action contract "within the same source" as its governing prose. Section 23's local checks include "procedure contract syntax/order uniqueness" -- syntax, not semantic agreement with the prose next to it. If someone edits the prose to add a mandatory step without updating the structured contract, nothing in the validation architecture catches it. This is the same disagreement Question B below asks about, just showing up as a missing mechanism rather than a missing rule.

**Capture has a stated failure mode in only one direction.** Section 31 lists "capture is too burdensome and important reasoning remains trapped in conversations" as a falsification condition. It does not list the opposite and, given Research 129's own C_capture/C_consolidate cost model, equally plausible failure: capture accumulates because nothing forces consolidation, and the low-friction intake surface becomes exactly the second knowledge swamp the candidate was built to avoid. Section 25's consolidation triggers (routing-payload growth, stale summaries, workstream closure) don't include "capture backlog age or size" as a trigger.

**Joint-authority declarations have no stated creation governance.** Section 12 specifies what a joint-authority declaration *contains*. Nothing specifies who decides *to create one*, or what review a new joint-authority declaration gets before it's accepted as an exception rather than a convenience. This connects directly to Question D below, where I think it's the sharper version of the same gap.

## B. Rich source versus structured declaration drift

Section 7 states the structured action contract is "an authoritative projection within the same source, not an LLM-generated shadow copy" -- but this states the *intent* that both stay consistent, not what happens *if they don't*. For the single mechanism most directly motivated by BL-001, I don't see an explicit precedence rule for when the prose and the structured contract inside the same document disagree.

I'd recommend the candidate adopt one directly: **the structured contract is the sole authoritative encoding of material constraints; prose is explanatory and non-normative wherever the structured contract also speaks, and any detected prose/contract disagreement is itself a document defect to be fixed, not a case to arbitrate at read time.** That is a real one-home-per-fact rule, stated plainly, rather than left implicit in "authoritative projection." Absent this, "what exactly is authoritative if prose and structure disagree" -- the brief's own question -- has no answer in the current text.

## C. Selective durable identity and tombstones

Bounded in the sense that matters for KA-R31/KA-I12: allowing the *total count* of identity-transition records to grow with history is fine, since those requirements are about required reconstruction cost, not storage volume. What I don't see specified is whether **looking up one identity's current state requires an indexed, bounded-cost lookup or a scan of the whole tombstone history.** Section 10 says a generated identity index maps ID to current carrier, but doesn't say whether that index is built incrementally (only reprocessing new transitions) or by rescanning everything on every regeneration. This is not a hypothetical concern -- it is exactly the caveat Research 136 attached to the V0.1 probe results and which Research 144/145 don't restate: full-rebuild scan counts grew linearly with history in that probe even though the *active view* stayed bounded. "Boundedness" for identity resolution needs the same caveat made explicit, or the claim is aspirational rather than mechanically guaranteed.

## D. SINGLE_SOURCE default and JOINT_AUTHORITY exception

This is where I want to be most direct, because I think the candidate has reintroduced a defect I already found and named once, without closing it.

Section 11's admission test for JOINT_AUTHORITY ("does the authoritative content genuinely require multiple sources together?") is, in structure, the same test as V0.2's relation-admission rule that I found near-circular in MC-0014: a plain-language criterion with no stated way to derive the answer from observable, lower-level signals, applied by whoever is deciding whether to create the exception. Research 143 itself notes that Corpus V0.1 produced zero real cases needing `JOINT_AUTHORITY`, which means this specific criterion has never been exercised against anything harder than a synthetic fixture -- the same evidentiary position V0.2's admission rule was in before MC-0014's review found it circular.

To be fair to what *does* work here: ordinary base+supplement cases correctly stay out of this exception. Section 13's `SUPPLEMENT` transition mode, plus V0.1's already-validated directional-declaration-plus-derived-closure pattern, handles the common case cleanly and directionally, exactly as the brief hoped. The problem is narrower than "the whole mechanism is broken" -- it's that the boundary of the *exception itself* rests on the same kind of unoperationalized judgment call that has already caused one real defect in this program, and nothing in Candidate 01 shows the lesson was applied here.

## E. Derived current state and current routing

`CURRENT_STATE.md` today contains genuinely editorial, hand-synthesized narrative -- not just structured facts, but judgment calls about what currently matters most and why. Section 16 correctly admits this can't simply be mechanically regenerated: "any unique accepted insight discovered during generation must be promoted into a canonical source before the view can rely on it as project truth."

That's the right principle, and it correctly *locates* the hard problem. It doesn't yet *solve* it. The sharp question is: who or what does the discovering? If a human, that's a real recurring editorial cost that undercuts the "cheap regeneration" promise elsewhere in the candidate. If a model, then the summarization step inherits exactly the BL-001-style fidelity risk -- an LLM-generated narrative can read smoothly while silently dropping something load-bearing, which is precisely what Research 129's F1-F9 consolidation-fidelity vector exists to catch. Section 15 states the summary "cannot silently contain unique accepted truth," but nothing in Section 23's validation layers actually tests for that on the hardest instance (a full narrative view, not a structured field). This is a real gap, not a solved problem restated with new vocabulary.

## F. Workstream object versus canonical source

The design matches what V0.1 already validated (source-local workstream state, generated active-route projection) and what RC-005/RC-006 confirmed against real data. What isn't addressed: this project's own history shows workstreams that pause and stay paused for a long time without being rejected, deleted, or completed (Cockpit since Checkpoint 267 is the concrete real example already in the corpus). Section 6 lists `paused` as a distinct, semantically-live state, but nothing specifies when or whether a long-paused workstream drops out of the "must consider" set for ordinary bootstrap, versus staying in the generated active view indefinitely. Given this project's demonstrated tendency to accumulate exactly this kind of long-paused-but-not-closed thread, I'd flag this as a concrete, not hypothetical, risk to KA-R32/KA-R34's boundedness and observability claims.

## G. Authority resolver and action-contract fidelity

This is the strongest-specified part of the whole candidate, and I want to say that plainly before naming its one real gap. Sections 19-20 give an actual testable shape -- a receipt with source IDs, revisions, activated constraints, and a concrete list of properties qualification must demonstrate (constraints survive, stay ordered, prohibitions aren't dropped, preconditions checked, missing/contradictory cases fail visibly). This reads like something that could become a test suite tomorrow, which is more than I can say for most of the rest of the document.

The one real gap: Section 20 correctly requires that "one model pass is not accepted as sole proof for high-consequence promotion/execution," but doesn't say what *is* required instead -- a second independent model, a human, some specific N-pass agreement rule. Every other "concrete open implementation choice" in Section 30 is fine to leave open (storage syntax, directory layout, search backend). This one isn't in the same category -- it's the verification method for the single mechanism directly motivated by the sharpest empirical finding in the whole evidence program, and I don't think it should be left as open as everything else on that list.

## H. Capture/promotion and consolidation economics

Capture's minimalism (Section 14: ID, time, provenance pointer, status, optional rough link) is well-judged and matches the ICM low-friction-intake lesson I evaluated favorably in MC-0012. Where this connects back to E and A: "promotion records...sufficient provenance and rejected rationale" is, again, a statement of intent rather than a checkable mechanism. I'd rather name this once, clearly, than list it three separate times: **E, H, and Section 25's general consolidation all share one unaddressed gap -- a concrete fidelity-verification mechanism for what a compression/summarization/promotion step is and isn't allowed to drop.** Fixing it once (for instance, actually operationalizing Research 129's F1-F9 dimensions as a checklist rather than citing them as a design principle) would close all three instances at once.

## I. Scale and maintenance economics

Section 26's central claim -- local changes touch a few canonical sources plus their generated dependency neighborhood, not a growing set of global files -- is the right claim and matches what V0.1's `active_view_bytes` result (138 bytes flat across 1x/5x/10x, for both H1 and H2, which I verified directly against the raw JSON in MC-0014) actually supports. But that same probe's `full_rebuild_source_scan_count` grew linearly with history for both candidates, and Research 136 was explicit that this is only acceptable if full rebuilds are periodic/global while *required* reconstruction uses bounded materialized views -- a caveat Candidate 01 doesn't restate. Section 26 doesn't commit to incremental generation (only reprocessing what changed) as opposed to full-rescan generation for its derived views generally, which is the same underspecification I flagged narrowly for identity in Question C, generalized to every generated view. Without that commitment, the scaling claim is supported for the *result* being small, not for *producing* that result staying cheap as history grows.

## J. Public/private and migration

The forward migration path (M0-M6) is genuinely thorough and well-sequenced, and the abstract private-dependency declaration (Section 22) is a reasonable, minimal mechanism consistent with KA-R37-39. What's missing is the other direction: M7 requires "rollback proof," and Section 31 lists a big-bang switch as a falsification condition, but nothing in Sections 16, 22, or 27 specifies what rollback actually *is* mechanically. Can the old compatibility files be regenerated losslessly from the new architecture's state at any point after a switch, so reverting never loses legitimate post-switch work? Section 16 only frames shadow-generated compatibility views as a pre-switch comparison tool, not as a standing post-switch rollback capability. This needs its own explicit design before M7 can be more than an aspiration.

## K. 50 + 17 design-coverage audit

I looked at this independently rather than checking Research 145's table for internal consistency (which it has -- the JSON and markdown agree). Based on Sections A-J above, I'd downgrade seven items from `DESIGN_COVERED` to a more honest `PARTIALLY_COVERED`:

```text
KA-R09  consequential-action authority activation and contract fidelity
    the resolver/receipt shape is real (Section G), but the missing prose/structure
    precedence rule (B) and the underspecified multi-pass verification requirement (G)
    mean the single most safety-critical requirement isn't fully designed yet

KA-R14  supersession, supplementation and conflict visibility
    REPLACE/SUPPLEMENT/SPECIALIZE/CORRECT covers the ordinary directional cases well;
    the JOINT_AUTHORITY boundary this requirement also depends on is under-specified (D)

KA-R17  view-contract consolidation fidelity
    the boundary/intent (capture doesn't imply authority) is genuinely well covered
    elsewhere (KA-I16 stays fully covered); the fidelity-verification mechanism this
    requirement specifically asks for is not designed (E, H)

KA-R31  non-linear-history reconstruction cost
KA-I12  required reconstruction cost not structurally proportional to history
    both rely on an incremental-generation commitment the candidate doesn't make (I)

KA-R43  migration preservation and identity reconciliation
    the forward path is solid; rollback, part of what safe migration requires, is
    unmechanized (J)

KA-R46  representation-independent continuity of identity
    the semantic design (tombstones, transitions) is sound; the lookup-boundedness
    guarantee that makes it acceptable at scale isn't specified (C)
```

Nothing I found should be called `NOT_COVERED` outright -- every gap I found is a real mechanism with a real, nameable missing piece, not an ignored requirement. And several items deserve explicit credit for being genuinely well covered under scrutiny, not just asserted: KA-R24 (probabilistic retrieval subordinate to explicit resolution) matches the XACML/OPA precedent this program validated extensively; KA-R29 (concurrent-collaborator safety via expected-revision preconditions) is directly supported by V0.2's actually-passing stale-revision-rejection test, which I verified against raw code in MC-0014, not just prose; KA-I01/KA-I02 (repository authority, one explicit authority) are foundational and applied consistently everywhere I checked.

## L. Alternative-family reopening

Not yet, and I want to give a sharper reason than "the trigger conditions aren't met." Candidate 01 now names seven distinct structured-declaration profile types (workstream, governing-procedure/action-contract, decision/requirement, evidence/source, identity-transition, joint-authority, capture) plus their generated indexes -- real breadth, more than either H1 or H2 individually proposed. That's worth tracking as a trend, not dismissing: if implementation adds an eighth, ninth, or tenth profile type while chasing edge cases from the failure corpus, that growth curve is itself the signal Research 145's own reopening rule is watching for, and I'd recommend adding profile-type count as an explicit tracked metric in Section 24 rather than leaving the "does it feel like too much" judgment unmeasured.

But testing whether object-primary would actually *fix* my strongest findings, I don't think it would. Object-primary still needs a rule for when to create a new relationship object versus reuse an existing one (the same circularity risk as D, not specific to which family is "primary"), and it still needs a human-readable projection that could drift from the underlying objects (the same risk as B, just relocated). My findings are about missing precedence and governance rules, which any family still has to answer. That's real evidence against reopening now, not just an absence of the stated trigger.

## Required conclusion

**1. Strongest design defect.** Not a single mechanism -- a recurring pattern. This is the third time in this program the same shape of gap has appeared: an admission/precedence judgment stated in plain language with no way to derive the answer from observable signals (V0.2's relation-admission rule, MC-0015's four-way taxonomy conflation, and now Candidate 01's `JOINT_AUTHORITY` boundary, Question D). Finding the pattern is more valuable than any one instance of it, and I don't think it's closed yet.

**2. Strongest property that survives attack.** The authority-resolver/action-contract mechanism (Question G) -- concretely specified, directly and explicitly answering BL-001, and closer to test-ready than anything else in the document.

**3. Corrected coverage.** 43 of 50 KA-R and 16 of 17 KA-I remain honestly `DESIGN_COVERED`. Seven items (KA-R09, KA-R14, KA-R17, KA-R31, KA-R43, KA-R46, KA-I12) should move to `PARTIALLY_COVERED`, each for the specific reason given in Question K. Zero items are `NOT_COVERED`.

**4. Coherent enough for a shadow prototype?** Yes, with one condition: Phase P0/P1 should resolve the prose/structure precedence rule (B) and state an explicit incremental-generation commitment (I/C) as part of building the substrate, not as follow-up work discovered later -- both are cheap design decisions now and expensive retrofits once generators exist.

**5. Smallest falsification-first prototype slice, in priority order:**

```text
1. Write down the prose/structure precedence rule explicitly (B) -- a decision, not code
2. Construct one deliberately joint-authority-shaped real-ish case and test whether the
   admission criterion can be applied non-circularly (D) -- directly retests the pattern
   from finding 1
3. Replay BL-001 against the resolver/action-contract mechanism, per Research 145's own
   top priority (G)
4. Decide and state incremental-vs-full-rescan generation, then time a synthetic 10x
   history run against it (I, C)
5. Design the rollback mechanism concretely before any real migration step (J) -- not
   needed to validate core semantics, so lowest priority for a first slice
```

**6. Conditions that would reopen H3 or another family.** Profile-type count growing past roughly ten during implementation; `JOINT_AUTHORITY` declarations proliferating beyond a small number of genuinely distinct cases; or concrete evidence (not yet in hand) that an object-primary representation would actually resolve the precedence/governance gaps in B and D, which I currently doubt but haven't disproven.

**7. Is another Claude round needed?** One short round, narrowly on findings B and D -- if ChatGPT's disposition states a concrete prose/structure precedence rule and a concrete, non-circular joint-authority test, I don't think a further round is needed before prototyping begins. Everything else in this review (C, E, F, H, I, J) can be carried forward as prototype-phase work items rather than requiring another design round first.
