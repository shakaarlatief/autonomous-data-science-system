# MC-0003 Message 002: Claude Deferred Catch-Up Review

**Thread:** MC-0003
**Message:** 002
**Author / collaborator:** Claude
**Role:** REVIEWER
**In reply to:** THREAD.md review request, Research 036, `docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md`
**Interaction environment:** Claude (claude.ai, chat interface with GitHub MCP connector)
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `claude-01`
**Conversation title:** `01 - ADS Development Review & Collaboration`
**Model / configuration:** Claude Sonnet 5
**Exact target reviewed:** `74fbf8f5dbf7b57bb5f3038b41122f20e09a4b53` — I fetched Research 036 and the protocol doc at that exact SHA, not the current branch head, specifically to honor the rule this design itself states (a review of an ancestor commit is not automatically a review of a descendant). This message is itself a first data point for finding 4 below.
**Purpose:** Deferred direct review of the candidate deferred-review/catch-up architecture, processed second in this session after MC-0002, per `REVIEW_INBOX.md`'s stated ordering.

---

## Answers to the ten review-focus questions

**1. Is requirement-vs-gate-boundary separation sufficient?**
The two-axis model (REQUIRED/OPTIONAL × BEFORE_TARGET_MUTATION/BEFORE_THREAD_RESOLUTION/BEFORE_PROMOTION/NONE) is the right shape — see finding F1 for one gap in it.

**2. Are the candidate gate boundaries the right ones?**
Broadly yes for this project's current structure, though the ordering between `BEFORE_THREAD_RESOLUTION` and `BEFORE_PROMOTION` is assumed rather than stated as a strict total order. MC-0002 happened to nest them correctly (review before resolution, resolution before promotion audit), but that's one data point, not a rule the design states explicitly. Worth naming as an assumption, not a defect.

**3. Does the review inbox create dangerous duplicate authority?**
Not currently, and the design is genuinely careful about this — the "important limitation" section and the explicit resolution rule ("thread and repository evidence control") are exactly right. But see F2: the safeguard is entirely textual right now, with no mechanical check that the inbox and the corresponding `STATE.json` actually agree.

**4. Is exact review-target freezing strong enough for delayed review?**
Yes. I can confirm this worked correctly in practice, not just on paper — I deliberately fetched both governing documents at the frozen SHA rather than the branch head for this review, and separately confirmed `STATE.json`'s current `last_transition.repository_head` matches that same SHA exactly. No gap found here.

**5. Is downstream reliance / impact-sweep handling sufficient?**
This is the weakest part of the design — see F3, the strongest finding in this review.

**6. Are one-by-one and batch catch-up rules proportionate?**
Yes, and this session is direct evidence: I'm processing MC-0002 and MC-0003 together for efficiency, exactly as Research 036 §8 anticipates, while keeping their target heads, findings, and dispositions fully separate, per its own stated constraint. The rule works as intended.

**7. Are prospective/blind review protections strong enough?**
The principle (§10: don't retroactively convert a prospective gate into a post-hoc one) is correct, but like F2 and F3, it's currently enforced only by everyone remembering to follow it — no mechanism would catch a violation.

**8. Should any mechanical extension be smaller or larger than proposed?**
Smaller, and later. I'd hold off on a Specification 025 until real use produces more than one deferred thread's worth of evidence — but when it does get written, F1–F3 below should be its priority list, not a fresh brainstorm.

**9. Can several pending threads coexist safely without global collaborator locking?**
Yes — confirmed directly: right now MC-0002 and MC-0003 are both `WAITING` on Claude simultaneously, using independent per-thread `target_write_owner` scoping, with no global lock anywhere. This is exactly what §12 claims and it's true.

**10. What is the strongest failure mode still missing?**
F3 (downstream dependency tracking has no mechanical support at all) — see below.

---

## Findings

### F1 — requirement × gate-boundary coherence isn't validated (minor)

A `REQUIRED` review paired with gate `NONE` ("advisory/optional... creates no acceptance gate") reads as internally contradictory — something can't be both required and gated by nothing. The document doesn't say this combination is disallowed, and nothing would catch it if someone recorded it. Minor, cheap to fix: either state explicitly that `NONE` is only valid when requirement is `OPTIONAL`, or explain the legitimate case where `REQUIRED` + `NONE` makes sense (I couldn't construct one).

### F2 — inbox/state consistency is unguarded (moderate)

`REVIEW_INBOX.md` is explicitly documented as non-authoritative, which is the right call — but this project already has a documented failure mode that looks exactly like this: `KNOWLEDGE_MAP.md` drifting out of sync with the actual document tree, which is precisely why Checkpoint 172's routing-consistency guard exists. `REVIEW_INBOX.md` is the same pattern (a human-readable convenience index shadowing machine-authoritative state) applied to a new surface, and right now nothing checks that its `target head` fields actually match the referenced thread's `STATE.json.last_transition.repository_head`. I did this cross-check by hand for MC-0002 and MC-0003 in this session; nothing would force the next reviewer to.

**Recommendation:** don't build this now — the same "earn complexity through evidence" principle that correctly kept Specification 024 narrow applies here too, and there's only one inbox with two entries so far. But this is the first concrete, well-scoped candidate for a future CI check, not a hypothetical one: a script that reads `REVIEW_INBOX.md`'s stated target heads and asserts they match each referenced thread's `STATE.json`, on the same model as the existing `current_routing.json` guard.

### F3 — downstream dependency tracking is described but has zero mechanical support (the strongest finding)

Research 036 §6.3 gives a good qualitative checklist for what a downstream impact sweep should ask ("which later tasks relied on the corrected claim," "which tests must be rerun," etc.) — but there is no field anywhere, in this design or in Specification 024's already-implemented `STATE.json` schema, that records *which threads depend on which other threads*. When a late review produces a required correction, the described response ("inspect downstream tasks that relied on the corrected result") is entirely a matter of someone remembering or manually searching, not something the system can answer.

This is the same category of gap MC-0001 found in the original collaboration architecture — real safety property, described correctly in prose, with no machine-checkable seam — and it was accepted there as the single must-fix item before routine use. I'd give this the same weight here. It's not an argument against the current design (the qualitative description is correct and worth keeping), but it's the one place I'd flag as "don't let this stay purely aspirational once there are enough threads for a real dependency chain to exist."

**What would resolve it:** a `depends_on: [thread_id, ...]` field added to `STATE.json` in whatever specification eventually extends it — cheap to add, and it would let a future backlog-discovery script actually answer "what does a correction to MC-000X put at risk" instead of relying on memory.

---

## Overall assessment

The design is sound as protocol, and unusually well-grounded for something written before real pressure existed — the project deliberately created its own pressure test (this exact multi-item backlog) rather than designing in the abstract, and the core claims held up when I checked them against actual behavior in this session, not just against the document's own logic. I don't think this needs a correction before continuing to operate as protocol.

I'd recommend against writing a Specification 025 yet. When one is warranted, F1–F3 are the concrete, evidence-backed list to start from, in priority order: F3 first (real safety gap, currently invisible), F2 second (known failure pattern this project has already lived through once), F1 last (cheap clarification, low consequence either way).

I'm not reopening MC-0001 or Specification 024. This review stayed inside the frozen MC-0003 target.
