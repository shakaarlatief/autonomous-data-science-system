# MC-0016 Message 003: Claude Narrow Candidate Amendment Review

```text
Thread                          MC-0016
Message                         003
Author / collaborator           Claude
Role                            ADVERSARIAL REVIEWER
Interaction environment         Claude
Project / workspace             Autonomous Data Science System
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Repository head reviewed        57f84b28f5c0cef9bd48b291387541baba32769d (routing only)
Exact amended candidate target   64d04fcc6ba2bcf6b66d4abbcccea714ca11870b
Purpose                         Narrow review of exactly two amendments (Research 144 Section 33.1-33.2
                                 and 33.3 / Research 146 Sections 2-4), per the MC-0016 Message 002 handoff
```

I read the amended Research 144 (Section 33 in full, plus Sections 7, 11, 12, 23 for context) and Research 146 in full at the exact amended target. This response addresses only the two authorized questions.

## Question B follow-up: normative precedence

The rule closes the ambiguity it was written to close. Making the structured contract the sole normative home, requiring a new mandatory constraint to enter the contract before the procedure stays qualified, and treating disagreement as a document defect rather than a runtime choice -- together these remove the "which wins" question BL-001-style dispatch would otherwise have to answer on the fly. I don't think there's a residual contradiction in the rule's own logic.

There is one adjacent gap the rule doesn't cover, and I want to name it precisely rather than let it pass as though it were part of the same question: **the rule specifies which side wins once a disagreement is known, but nothing specifies how a disagreement gets noticed in the first place.** Section 23's validation layers still list "procedure contract syntax/order uniqueness" as a local check -- syntax, not semantic agreement between the prose and the structured contract next to it. If someone edits the prose to describe a new mandatory step and simply doesn't touch the structured contract, nothing flags it. Under the new rule that isn't a normative failure -- the structured contract is authoritative by definition, so its silent incompleteness is technically "correct" -- but it does mean a procedure can drift into being quietly wrong relative to what any human reading the prose would reasonably expect, with no mechanism to surface that drift.

This is a real but categorically different risk than BL-001's own failure mode. BL-001 was a *dispatch* failure: a complete, correct source existed and its constraints were dropped on the way to guidance. What I'm describing is a *source-integrity* failure: the source itself silently stops being complete. The assurance ladder in Section 3 (deterministic check, then structured plan, then independent verification for high-consequence free-form transformation) defends against the first shape regardless of whether prose and contract are in sync, which is why I don't think this residual gap should reopen the precedence question itself.

**Smallest correction:** add one impact-aware check (fits the existing Section 23 tier, not a new tier) that runs whenever either the prose or the structured contract of a governed procedure changes, and does a basic semantic-diff-style comparison -- flag for review rather than auto-resolve. This is additive, not a redesign.

`B_PRECEDENCE = CLOSED` for the question as posed. The drift-detection gap is real but adjacent and small enough that I'd carry it into Phase P0 as a work item rather than treat it as blocking.

## Question D follow-up: JOINT_AUTHORITY admission

The reframing matters and genuinely changes my assessment. My MC-0014 finding was about a *mechanized* rule reading boolean flags that had already been hand-set by whoever built the fixture -- circular because the classifier and the label-setter were the same act. J1-J6 is explicitly a governed *human* promotion decision with an evidenced review receipt (J5), not a claim that a classifier can derive the answer automatically. That specific circularity does not recur here, and J5 directly closes the "no creation governance" gap I raised in my own Message 001 Section A.

Testing J2 and J3 specifically, as asked, I found a real residual precision gap in both, and I can give the concrete counterexample the brief asks for.

**The counterexample.** Take an ordinary base+supplement pair, exactly like V0.1's validated P1/P2 case: P2 declares `supplements: [{target: P1, precedence_after: P1}]`. Under J3's own example list -- "set-level ordering/precedence" -- a reviewer could plausibly read this as qualifying: after all, "which comes first" is a fact *about the set*, and nothing in J3's wording as written excludes it. But this is exactly the case V0.1 already proved stays cleanly source-local: the precedence fact is owned by P2's own directional declaration, not by anything that needs its own identity. If J3 is applied literally, a reviewer following its example list correctly could promote a joint-authority object for a case this program has already shown doesn't need one -- which is precisely the "exception proliferates into a de facto spine" failure Section 31 warns against, just moved from a mechanized rule into a human one.

The same problem shows up in J2's phrasing: "cannot represent the complete governing-set semantics" is ambiguous between two readings. Read strictly, ordinary directional relations can represent almost anything -- V0.2's own strongest-H1 result showed that even a genuinely symmetric, no-natural-owner relation could still be forced into a directional sidecar via a lexicographic tie-break. So "cannot represent" in the *impossible* sense is almost never true. What actually distinguishes the cases that deserve joint authority from the cases that don't -- and this is the single most important empirical finding from the whole V0.1/V0.2 program -- is not representability, it's whether the only available directional representation requires an **arbitrary, semantically unmotivated** choice among otherwise symmetric participants. J2 doesn't say that. As worded, it's satisfiable by "this feels awkward to express directionally," which is a much weaker and more subjective bar than the one this program actually validated.

**Smallest stronger rule.** Tighten J2 and J3 to explicitly invoke the arbitrary-versus-natural-owner distinction rather than leaving "cannot represent" and "not derivable" open to the wider reading:

```text
J2 (tightened)
    ordinary source-owned relations plus deterministic closure cannot represent the
    governing-set semantics WITHOUT introducing an arbitrary, non-semantically-motivated
    directional choice among sources that are otherwise symmetric with respect to the
    governed action/scope/time

J3 (tightened)
    a set-level fact exists that is not derivable from any member source's own natural
    directional relation -- including ordinary base/supplement, replace, specialize or
    correct ordering, which already carries an inherent direction and does not qualify
    merely because the fact "isn't currently encoded" somewhere
```

With this tightening, the base+supplement counterexample above cleanly fails J2/J3 (there is a natural, non-arbitrary direction -- the supplement names its own base), and a genuinely symmetric case like V0.2's ternary relation cleanly passes (no participant is more natural than another, so any directional encoding is a tie-break). That is the actual discriminator this program already earned through two rounds of empirical probing, and I think J1-J6 should say so explicitly rather than leave it to each reviewer's individual judgment to rediscover.

`D_JOINT_AUTHORITY = STILL_OPEN`, narrowly -- not because the governance framing is wrong (J5 in particular is a real, correct fix), but because J2/J3's current wording doesn't yet encode the one distinguishing test this program has actually validated, and a careful reviewer applying the literal text could reasonably promote a case that ordinary source-local declaration already handles cleanly.

## Optional scope correction

Nothing I'd call materially necessary. I reviewed Research 146 Section 13's recalibration of my original seven-item downgrade and I think it's fair, not just diplomatically accepted: KA-R31/KA-I12's actual text is about *required* reconstruction cost, which KA-R33's periodic-rebuild carve-out already legitimately covers, so my original framing of that as a KA-R31/KA-I12 gap was imprecise even though the missing mechanism (an explicit incremental-refresh commitment, Section 33.6) was real and is now present. Same acknowledgment for the KA-R43/KA-R44 rollback reassignment and the KA-R46 identity-lookup reassignment -- the underlying mechanisms I flagged as missing are now specified (Sections 33.7, 33.10); I just had the wrong requirement numbers attached to a couple of them. I'd note only in passing, not as a formal correction, that KA-R14's "kept as fully covered" status is very slightly ahead of D's narrow residual above -- but the gap is small enough, and the fix specific enough, that I don't think it's worth reopening the count over.

## Required conclusion

1. `B_PRECEDENCE = CLOSED` -- the normative-truth question is genuinely resolved; the adjacent drift-detection gap is real but categorically smaller and doesn't reopen it.
2. `D_JOINT_AUTHORITY = STILL_OPEN` -- the governance reframing correctly defuses the original mechanized-circularity concern, but J2/J3's wording needs the arbitrary-versus-natural-owner tightening above before the admission test reliably excludes cases this program has already shown should stay source-local.
3. Neither issue blocks the falsification-first shadow prototype. Both corrections are small, additive, and cheap to fold into Phase P0's initial substrate design (the drift-detection check as one more impact-aware validator; the J2/J3 wording fix as a text change to the same section) rather than requiring implementation to pause for another design round.
4. H3 or another family should not reopen before the prototype. Nothing in this narrow review changes my Message 001 assessment, and J5's review-governance addition further reduces the joint-authority proliferation risk that was one of the two conditions that would have justified reopening.
5. MC-0016 can close after this response. Both findings I asked to see concrete answers for got them -- one fully, one requiring a small, precisely-specified wording correction rather than further dialogue. I'd carry the J2/J3 tightening and the drift-detection check into the prototype phase as named work items rather than as reasons for a further Claude round.
