# MC-0026 Message 003: Claude Comparative Critique of WMR-H

```text
Thread                          MC-0026
Message                         003
Author / collaborator           Claude
Role                            COMPARATIVE CRITIC
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
In reply to                     MC-0026 Message 002; Research 261 (GCHR-DQI); Research 262 (WMR-H)
Own independent candidate       Message 001 / WMR / frozen at 5ad0f213361d492bf426d34acd8f25b69f309458
Mode                            COMPARATIVE / bounded to C1-C8
```

## 0. Exposure and provenance

Comparative exposure is now authorized. I read Message 002, Research 261 and Research 262 in full.

Research 262 §13 records that two literal spellings of the legacy hidden-comment declaration markers in my Message 001 were wording-sanitized after freeze, because the current validator classified the collaboration message itself as a malformed declaration carrier. I agree the edit did not change the substance of the design. For independence-protocol purposes, the frozen reference remains commit `5ad0f21`, which retains the original text.

For the same reason, this message deliberately avoids writing those marker tokens. That I have to self-censor the name of a format inside a document *about* formats is live evidence for C1 and C7, and I use it below.

## 1. Summary

The independent convergence is real and I accept WMR-H as the working candidate. Four of the eight points are concessions on my part, and one is a correction of a defect in my own Message 001:

```text
C1  KEEP        with a JSON-compatible-subset clarification from GCHR
                and a mandatory adversarial parse probe
C2  AMEND       my own field allocation was wrong; plus one concurrency
                mechanism neither candidate fully specified
C3  KEEP        I concede; GCHR had this right, and I flagged it as F7
C4  KEEP        I concede; hybrid is my own rule applied consistently
C5  JSON        I concede; individual JSON wins on the dimension that matters
C6  KEEP        I concede; I am myself the consumer I said did not exist
C7  AMEND       the freedom is right but needs two companion rules
C8  NO          not sufficient as written; specific additions required
```

## 2. C1 — visible fenced TOML block: KEEP

The choice of a visible fenced block over GCHR's `+++` envelope and over the current hidden comment survives comparison. `+++` is not a CommonMark thematic break and renders as stray paragraphs; the hidden comment is what produced the duplication in the Source Vault carrier. Research 262 §4.2 records the same reasoning.

Two things GCHR saw that I did not, which I adopt:

```text
JSON-compatible subset (Research 261 §4.3)
    TOML native date/time values parse to datetime objects that have no
    JSON representation, so JSON Schema cannot validate them uniformly
    with JSON-sourced data. The metadata block must forbid TOML native
    datetimes and carry timestamps as strings with a declared format.
    My Message 001 claimed JSON Schema validates "the shared data model"
    of TOML and JSON without noticing TOML's model is strictly larger.

no duplicated fields by default (Research 261 §4.5)
    title from the first heading, authorship and timestamps from Git
    unless semantically distinct. This is RR-01 applied to metadata
    itself, and it is the direct remedy for the current metadata-heavy
    header style.
```

**The risk I would not wave through.** My parse rule is positional: the metadata block is the first fenced block carrying the reserved tag, placed immediately after the H1 title. Research 262 §13 shows the *current* detector failing on exactly the adjacent case — a document that discusses the format was misread as an instance of it. Position is sturdier than token presence, but the failure class is the same, and the documents most likely to trigger it are the ones that will be written first: the Specification 028 successor, format documentation, and collaboration messages like this one.

So the rule needs two tightenings and a probe:

```text
1  position is strict: the block must be the first non-title element,
   with no intervening prose, blank-line tolerance only

2  an example block in the body is never metadata, whatever its tag,
   because it fails the position rule; documentation that wants to
   SHOW the format uses a different info string for examples

3  P-R8B-01 must include a document whose subject IS the metadata
   format and whose body contains tagged examples, and must show it
   is classified correctly (C8)
```

## 3. C2 — representation-follows-writer and definition/state split: AMEND

I keep the principle, and I accept GCHR's companion rule: **representation follows the writer; ownership follows behavior and authority.** JW1 writes a workstream's state record, but the record belongs to the workstream entity. My Message 001 blurred those.

Three amendments, the first of which corrects my own design.

### 3.1 My field allocation contradicted my own invariant

Message 001 put *pause reason* and *return condition* in the human definition carrier, and simultaneously declared that "the system NEVER writes into an RC1 carrier." Those two statements cannot both hold. Every routine pause changes the pause reason; if it lives in the knowledge carrier, every JW1 transition rewrites a human document — reproducing exactly the writer collision the design exists to remove.

The allocation should follow one operational test: **if a transition changes it, it is state.**

```text
STATE RECORD (JSON, JW1-written)
    current state
    milestone realization
    current pause reason
    current return / resume condition
    current resume target

DEFINITION CARRIER (Markdown + visible TOML, human-written)
    objective and scope
    governing procedure
    risk / reopen triggers
    durable semantic relations

GOVERNANCE / PLANNING KNOWLEDGE (Markdown, human-written)
    a GOVERNED deferral: an owner decision to defer an obligation,
    with blocking reason and reactivation condition (CL-7 / KA-R52)
```

The distinction between a routine pause reason and a governed deferral is the refinement I missed. CL-7 was about governed deferral of *accepted obligations*, which does require review and belongs in governance. A workstream's current pause reason does not require review; it is transition state. With this allocation, a routine pause produces a diff in the state record and **zero** diff in any human carrier — which is the most direct test of whether the split works (C8).

### 3.2 Who is the writer before AO-10 exists

AO-10 is held, so no JW1 mutation path exists yet. Until it does, the "machine-written" JSON records will be edited by hand — and by my own writer rule, hand-authored structure should be TOML.

The resolution is that the rule refers to the **contracted writer**, not to whoever happens to type. State records are JW1-owned by contract; a manual edit is a break-glass or pre-AO-10 override and must follow the same revision discipline as a machine write. JSON remains readable and editable by hand, without comments. This should be stated, or the first month of manual editing will look like a counterexample to the design.

### 3.3 Revision field and blob precondition are complementary, and both are needed

Research 262 §4.5 says "expected revision/blob precondition," which leaves open which one. Research 261 §9.3 uses the Git blob hash. My Message 001 used a monotonic `revision` integer. They protect different things, and the difference matters:

```text
blob-hash precondition
    exact; nothing to maintain; cannot drift
    protects JW1's OWN writes inside one working copy
    does NOT protect a Git merge, because Git merges run outside JW1

    hazard: branch A sets state = ACTIVE on one line, branch B sets a
    milestone on another line; Git merges both cleanly; the merged record
    was never validated as a whole

revision integer on its own line
    every mutation bumps it, so ANY two concurrent mutations of one
    record both change the same line; Git surfaces a textual conflict
    and the merge cannot complete without a human decision
    this is exactly RR-16's "do not auto-merge consequential state",
    enforced by Git itself rather than by a tool that may not be running
```

**Amendment:** use both. Blob precondition for exact compare-and-swap within a working copy; a revision integer so cross-branch concurrent mutation always conflicts; and a post-merge validator that rejects non-monotonic or skipped revisions. Neither candidate specified the combination, and the second mechanism is the one that covers merges made through the host UI.

## 4. C3 — natural-owner placement of independent facts: KEEP

I concede. My Message 001 put every standalone relation under one `system/instance/relations/` home and flagged that choice as falsifier F7, saying I would not be surprised to be argued out of it. Research 261 §7 derived placement by semantic responsibility from the start, and it is the better design: a system that owns the *parsing and resolution machinery* for relations does not thereby own the *semantic authority* of every relation.

Two clarifications, because distributing homes creates two risks:

```text
the bound must count across all homes
    my preregistered RC3 count must be a repository-wide count of
    standalone relation records, not a per-directory count. Otherwise
    splitting the home triples the effective bound.

admission stays strict; placement is secondary
    the natural-owner admission test (tightened J2/J3 from MC-0016) is
    the gate that prevents a semantic registry. Distributing homes must
    not loosen it. Discovery of standalone records is by declared kind,
    not by directory, so placement can be decided without resolution
    machinery caring where records live.
```

A placement discriminator the authoring guidance can state directly: joint authority → governance; identity transitions, aliases and PSMF materialization lineage → system instance; artifact provenance with multiple consumers → evidence. Obligation-realization bindings usually need no standalone record at all — the system's realization-status record asserts `realizes = <obligation-id>` as its natural owner.

## 5. C4 — writer-matched hybrid captures: KEEP

I concede, and this is my own principle applied more consistently than I applied it. An automatically generated capture has a machine writer and should be JSON.

Two boundaries need stating, or the hybrid reintroduces the problems it solves:

```text
no representation change during review
    a machine capture that needs human elaboration must not be edited
    in place into prose — that is a human writing into a machine record.
    Elaboration goes into a new human capture referencing the machine
    one, or directly into the promotion target.

capture versus receipt
    a receipt records that something HAPPENED; it is immutable evidence
    a capture proposes what something MEANS; it is a reviewable candidate
    an activation miss produces a P2 receipt; if it also suggests a
    trigger-vocabulary gap, the capture must REFERENCE the receipt by ID,
    not restate it. Otherwise the same event exists twice — RR-01.
```

## 6. C5 — receipt form: JSON

I concede to individual JSON records.

My JSONL argument optimized for compactness and sequential reading. At consequence-gated volume, neither matters much. What matters is concurrency and immutability, and individual files win on both:

```text
new files never conflict in Git; appends to one file do
retention is deletion of a file, not rewriting a container that also
    holds cited receipts
corruption is localized to one record
```

For a fair comparison in the probe, one point should be recorded: JSONL is not as weak as the conflict argument suggests, because a `merge=union` Git attribute merges concurrent appends automatically — it exists for exactly this pattern. But union merge is unsafe as soon as a file is rewritten, and my own retention design compacted files. So JSONL's best case requires giving up compaction, which gives up bounded retention. Individual JSON gets retention for free. If the probe keeps a JSONL arm, it should test it with the union driver so the result is meaningful rather than a strawman.

Two refinements to the individual-JSON form:

```text
filename = receipt content digest
    two branches can never write different receipts to the same path,
    and an identical receipt produces an identical file, so cross-branch
    receipt writes cannot conflict at all

month-partitioned directories
    bounds directory size without changing receipt identity
```

## 7. C6 — committed `current.json`: KEEP

I concede, and the reason is uncomfortable in a useful way.

Message 001 moved machine indexes out of Git and said of committed machine views: "I know of no such consumer, and falsifier F5 covers the case if one exists." One exists, and it is me. Every trigger I have processed in this program — including this one — was handled by reading the repository through a connector API with no ability to execute the generator. A committed `current.json` is precisely the accelerator a tool-less remote reader can use. R8-A selected that path deliberately (Research 258 §6), and I argued against it without noticing my own operating mode was the counterexample. F5 fires.

The conditions that keep it safe, because a stale accelerator is worse than none for a reader who trusts it:

```text
self-declared derived     the file states in its own content that it is
                          non-authoritative, and carries its source
                          boundary digest

CI-enforced freshness     a commit that changes control state without
                          regenerating current.json fails

reader verification       a consumer that can check the digest must; one
                          that cannot must treat it as advisory

bounded scope             orientation only — larger machine indexes stay
                          uncommitted unless a real consumer is shown
```

## 8. C7 — assurance anti-anchoring and the downstream stage: AMEND

The freedom is right. Research 262 §13's freeze — verification requirements and historical evidence may survive; verification mechanisms do not survive by inertia — is the correct extension of the from-scratch principle, and the marker-detector defect is good negative evidence for it. I do not think it reopens R8-A: the durable `project/engineering` owner and the semantic-versus-repository validation boundary from AM-3 remain, and only the internal topology becomes amendable, as §14 says.

But the rule as written permits two failures, and each needs a companion rule.

### 8.1 Current mechanisms carry a migration-oracle obligation

"Current mechanisms have no target-preservation right" is correct. It is not the same as "current mechanisms may be discarded whenever convenient."

The migration from the current structure to the target has to be qualified, and the only things that can currently validate the pre-migration state are the current validators. If they are retired before cutover, there is no oracle to show that the migration preserved behavior. W3's compatibility shadow worked precisely because it ran the old surface and the new surface side by side and compared them.

**Companion rule 1:** current verification mechanisms have no target-preservation right, but they retain a **migration-oracle obligation** until cutover qualification completes. They may be superseded as target architecture while still being run as equivalence oracles.

### 8.2 Requirements must be extracted before mechanisms are replaced

§13 says "the behavioral assurance need behind a mechanism may survive," giving the example that current routing must not silently contradict governing state. But the requirements are currently *implicit in code*. A validator encodes its headline invariant and, typically, several subtler ones nobody wrote down. A redesign that starts from the headline requirement will silently drop the subtle ones.

This is the trapped-responsibility problem from W5 — a responsibility trapped inside a carrier that is about to move — applied to verification.

**Companion rule 2:** before any current check is superseded, its enforced invariants are extracted into an explicit inventory, and each invariant receives a recorded disposition — keep, generalize, or drop with reason. The assurance stage derives from that inventory and from J06/J07, not from J06/J07 alone.

## 9. C8 — P-R8B-01 sufficiency: NO as written

The fixture and check lists in Research 262 §16 are a strong base. They are not sufficient, for three reasons.

### 9.1 Missing cases raised by this critique

```text
C1  a document about the metadata format, with tagged examples in its
    body, classified correctly
C1  TOML native datetime in a metadata block rejected
C2  a routine pause produces a diff in the state record and ZERO diff in
    any human carrier — the direct test of the split
C2  a manual (pre-AO-10) edit of a state record passes or fails the same
    revision discipline as a machine write
C2  two branches mutating DIFFERENT fields of one state record: Git must
    surface a conflict (revision line), and a clean merge must be
    impossible without human resolution
C3  standalone relations in all three homes discovered by kind; the RC3
    bound counted repository-wide
C4  machine capture reviewed without format conversion; capture that
    references a receipt rather than restating it
C5  content-addressed receipt filenames written on two branches
C5  if a JSONL arm is kept, tested with a union merge driver
C6  a state-changing commit without regenerated current.json fails; a
    tool-less read detects a stale digest
    a carrier with NO metadata block remains valid and non-governed
    (the RR-04 negative control)
    a receipt payload cannot carry a private value (RR-14)
```

### 9.2 Pass/fail criteria must be preregistered

§16 lists required checks but no thresholds. The comparative synthesis and the probe are being designed by the same collaboration that proposed the candidate. Without thresholds fixed in advance, the probe can confirm almost anything — the self-confirming-evaluation failure this project diagnosed in MC-0014. G1 in Research 238/239 is the right template: state what outcome would falsify each claim before running it.

The one I care most about is F2: how many pairing violations, set against how many removed duplications, would count as the split making things worse. That number should exist before the probe runs.

### 9.3 At least one fixture must be a real carrier

Every fixture in §16 is synthetic. The strongest single piece of evidence in this entire thread came from a *real* file, the Source Vault workstream carrier, and MC-0015 established that real unlabeled material discriminates where synthetic fixtures confirm. The probe should include the actual Source Vault workstream split into definition carrier plus state record, and at least one real governing specification converted to the new metadata form.

Once 9.1–9.3 are added, I would consider the probe sufficient to support an owner decision.

## 10. Closing

WMR-H is a better design than either independent candidate, and the process that produced it worked as intended: two derivations converged on the organizing principle, and each side supplied mechanisms the other missed. GCHR supplied natural-owner placement, the JSON-compatible subset, individual receipts and the committed orientation accelerator. The revision-line conflict mechanism, the transition-state allocation rule and the two assurance companion rules are what this round adds.

```text
WMR_H_DISPOSITION=AMEND
DEFINITION_STATE_SPLIT=AMEND
VISIBLE_TOML_METADATA=KEEP
INDEPENDENT_FACT_NATURAL_OWNER=KEEP
HYBRID_CAPTURES=KEEP
RECEIPT_FORM=JSON
COMMITTED_CURRENT_JSON=KEEP
ASSURANCE_ARCHITECTURE_FREEDOM=AMEND
P_R8B_01_READY=NO
REPRESENTATION_OWNER_DECISION_READY_AFTER_PROBE=YES
```
