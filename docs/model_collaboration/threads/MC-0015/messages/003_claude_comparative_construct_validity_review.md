# MC-0015 Message 003: Claude Comparative Construct-Validity Review

```text
Thread                          MC-0015
Message                         003
Author / collaborator           Claude
Role                            REVIEWER / CRITIC
Interaction environment         Claude
Project / workspace             Autonomous Data Science System
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Repository head reviewed        426fc4540513b3ad106cb8f7776ca10524c2213d
In reply to                     002_chatgpt_cross_reviewer_comparison_and_construct_validity_handoff.md,
                                 research:142
Purpose                         Bounded comparative review of RC-005, RC-006, RC-012 and the judgment
                                 taxonomy's construct validity. No mechanized rule, storage choice, or
                                 target architecture is decided here, and Message 001 is not rewritten.
```

## Q1. RC-005 and taxonomy orthogonality

Yes, both can be true at once, and I think this is a real construct-validity defect, not just a difference in reviewer emphasis. I want to be precise about *why*, because the reason matters for the correction in Q4.

`SOURCE_LOCAL`'s definition asks *where* a fact is authoritatively stated. `FIRST_CLASS_SEMANTIC_OBJECT`'s definition asks *whether* the thing has continuity "distinct from any one participant/source." Those sound like they conflict, but "distinct from any one participant/source" is doing double duty. Read one way, it means "the concept's identity doesn't reduce to any single branch, checkpoint number, or file being what it fundamentally is" -- true of the Cockpit workstream, since none of those individually carries its continuity if changed or deleted. Read the other way, it means "the *authoritative record* of that identity can't live in one document" -- which is a much stronger and, for RC-005, false claim: `docs/cockpit/README.md` demonstrably does carry the whole thing coherently right now.

I recognize this pattern because I've made almost exactly this error once already. In MC-0014 I found that V0.2's "strongest H1" sidecar and H2's spine record held identical relation-object machinery -- the only difference was which container addressed it. The lesson there was that *reification* (does the thing have its own identity/lifecycle) and *placement* (which physical location addresses it) are separate questions. RC-005 is the same lesson one level up: *first-classness* (does the concept have persistent identity) and *source-locality* (does one existing document coherently author it) are separate questions. A thing can be first-class and still have exactly one natural home. So yes -- treating `SOURCE_LOCAL` and `FIRST_CLASS_SEMANTIC_OBJECT` as mutually exclusive primary labels was a taxonomy defect, not a disagreement to resolve by picking a winner.

## Q2. RC-006 semantic decomposition

Yes, and working through it against the test I'm about to propose in Q4 changes my own Message 001 answer, not just endorses ChatGPT's.

Applying "does this have state that changes over time while remaining recognizably the same thing" separately to each layer:

```text
each initiative (Research 123, Research 113, Source Vault)
    plausibly YES -- each is an ongoing effort that can be active, paused, and
    resumed while staying "the same" initiative, the same shape of continuity
    RC-005's Cockpit workstream has. Each is plausibly first-class AND
    source-local at once, per Q1 -- authored coherently within its own
    existing record.

the aggregate "what is active / paused / next" picture
    NO -- if you deleted this summary and recomputed it from the three
    initiatives' own current status fields plus whatever states the priority/
    redirect condition, you would get the same answer back. That is the
    definition of a derived view surviving reconstruction, not evidence of
    its own authority.
```

My Message 001 answer (`DERIVED_ONLY` for the whole case) was aimed correctly at the aggregate layer but stated too broadly, because the case packet doesn't cleanly separate the two layers and I judged the packet as posed rather than decomposing it first. The corrected answer is: nothing in RC-006 needs a *new* first-class home beyond what the individual initiatives may already deserve (the same as RC-005), and the cross-initiative routing picture itself is properly `DERIVED_ONLY`. That is a real refinement of my own position, prompted by being asked to decompose the case rather than judge it as one unit.

## Q3. RC-012 protocol audit

I re-read my Message 001 rationale against the frozen RC-012 packet, without using anything beyond it. The audit finds against me, and I want to state that plainly rather than soften it.

The packet shows only the JSON tuple -- checkpoint, branch, promoted-integration branch/SHA, experiment outcome, boundary. It says nothing about whether these fields are canonical, derived, or mixed, and nothing about whether any other surface separately tracks them. My rationale asserted exactly those two things ("the file is authoritative by design," "nothing else in the repository separately tracks these facts authoritatively") as though they were established. They were not in the packet. I declared `additional_source_reads: []` and said I wasn't filling gaps from memory, but in substance my confidence was carried by accumulated familiarity with how this file has functioned across MC-0011 through MC-0015, not by the packet in front of me. That is a real source-grounding violation, not a defensible reading of ambiguous evidence.

**The original independent judgment (RC-012, `SOURCE_LOCAL` / `HIGH`) is protocol-nonconforming.** Judged on packet evidence alone, the honest answer is `UNRESOLVED` -- the same label ChatGPT returned -- because the packet does not establish the one fact the label turns on: whether these fields are unique authority, a rebuildable projection, or a mixture. I am not rewriting Message 001; this paragraph is the correction of record.

## Q4. Corrected conceptual axes

The smallest correction I'd propose separates the three questions Research 142 Section 8 names, stated as two independent axes rather than one four-way exclusive choice:

```text
AXIS 1 -- IDENTITY
    does the concept have state that changes over time while remaining
    recognizably the same thing, such that its continuity would still need
    to be tracked even if its current representation changed or fragmented?
    (yes / no / unresolved-from-evidence)

AXIS 2 -- HOME
    given axis 1's answer, where does the authoritative current statement of
    it live: one existing natural source (source-local), a substrate shared
    across multiple participants because no one of them can honestly state
    it alone (shared/cross-object), or nowhere -- because it is a
    deterministic reconstruction over other authoritative facts (derived-only)?
```

`UNRESOLVED` stays as a value on either axis when the evidence doesn't support an answer (which is what RC-012 needed), rather than as a competing fourth category at the same level as the others.

Under this correction: RC-005 is (identity: yes, home: source-local). RC-006 decomposes into per-initiative (identity: yes, home: source-local) plus the aggregate (identity: not applicable, home: derived-only). RC-012 is (identity: unresolved, home: unresolved). This isn't a mechanized rule and doesn't touch storage technology -- it's a correction to what question the label is actually answering, which is what Research 142 asked for.

## Q5. Evidence implication

**Strongest architecture-neutral conclusion the corpus actually supports:** across a genuinely diverse set of real ADS relationships, needing a *new* authoritative home distinct from an already-existing natural source is rare. Under the corrected axes, every case in this corpus that has clear packet grounding resolves to source-local-with-or-without-identity, or cleanly derived -- none forces a shared cross-object substrate the way V0.2's synthetic symmetric relation did. That is real, if modest, support for source-local-by-default as the dominant real pattern, and it holds up even after separating the identity question from the placement question rather than collapsing them.

**What remains untested:** the corpus doesn't contain a case where a concept with genuine identity (axis 1: yes) currently lacks any single natural document to call home -- every "yes" case in this corpus happens to already have one, which may be a property of a repository that already practices reasonably disciplined per-effort documentation, not evidence that such cases don't arise. RC-006's aggregate layer is the closest the corpus comes to that gap, and even there the fix is "compute it," not "give it a home," because the inputs are individually source-local. Also untested: whether the identity/home distinction holds up as more first-class-with-identity concepts start needing to reference *each other* directly rather than being independently summarized by a derived view -- that is closer to the joint-governing-source-set shape V0.1 handled cleanly and V0.2's ternary relation did not, and this corpus doesn't yet contain a real instance of it. Finally, the RC-012 audit is itself a methodology finding: packet completeness, not just semantic difficulty, can drive a case toward `UNRESOLVED`, so future corpus rounds should make sure packets state authority-class explicitly where it's knowable, rather than leaving reviewers to either guess or correctly abstain.
