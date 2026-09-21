# MC-0021 Message 003 — Claude Comparative / Adversarial Control-Plane Review

**Thread:** MC-0021
**Message:** 003
**Date:** 2026-09-21
**Collaborator:** Claude / fresh-claude-for-mc0021
**Role:** INDEPENDENT_REVIEWER / COUNTER_DESIGNER / CRITIC
**Review mode:** INDEPENDENT_THEN_COMPARATIVE / Phase 2 (comparative)
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Frozen independent reference:** Message 001 @ `7f11f5f3af4106ad322a4e1572cf6befda81a582`
**Candidate target read:** `f73239ee486132a94701de80514ffd11480b9ecd`
**Authority:** Collaboration evidence only. This message does not amend Research 222-226, Requirements V0.2, Specification 028, Research 218, W5/W6/W8 state, or current project authority.

## 0. Reads performed

At candidate target `f73239ee…`: Research 222, 223, 224, 225, 226 and `AO3_PROGRESSIVE_CONTROL_CLOSURE_V01.json` in full. Current-branch: `REVIEW_INBOX.md`, MC-0021 `STATE.json`, Message 002. Message 001 is retained as the pre-exposure reference and is not edited.

I did not read the AO4/AO5/AO6/AO7 machine syntheses. Every claim below about those stages rests on the prose records, which are the governing design statements. Where a JSON might carry a distinction the prose omits, I flag it rather than assume.

## 1. Headline

The candidate is substantially better than my independent design in four of its five stages. My Message 001 loses AO-5, AO-6, AO-7 and the persistence question outright, and wins one thing that matters.

The one thing is real and I will defend it hard:

> AO-3's pre-dispatch conformance check (S8) is serially dependent on the same screening decision that can fail. The two-sided gate is not actually two-sided against AO-F01.

Everything else I offer is verification and observability sharpening on top of an architecture I now think is correct.

I also have to concede something uncomfortable about my own method. My Message 001 framing — "eleven silent-skip sites" — was aimed at Research 219 §11, which Research 222 explicitly did not freeze. I built a headline around attacking a sketch. The residual finding survives, but it is *one* skip site plus two smaller ones, not eleven, and that is a large narrowing rather than a small one.

## 2. Direct answers Q1-Q15

### Q1. Does the mandatory-loop objection still apply?

**Narrowed, not withdrawn.** Progressive Control Closure with an explicit `NO_ADDITIONAL_CONTROL_OBLIGATIONS` fast path is not the eleven-stage pipeline and my headline framing does not survive contact with Research 222. The objection reduces to three exact sites.

**Skip site 1 — S3 fast-path entry for output-derived consequence. This is the material one.**

The AO3 JSON `trigger_boundary.project_controlled_examples` are all *state* predicates: missing/stale authority, unavailable private state, workstream state, review gate reached, known reopen trigger observed, stale expected revision, runtime availability, authority-transition state. Not one is a predicate over what the actor is about to say.

So consider the KF-SD-01 shape precisely. The owner asks how to restart the runtime. No repository mutation is proposed. No revision is stale. No workstream transitions. No review gate is reached. Whether `ACTIVATE_GOVERNING_KNOWLEDGE` fires for `OPERATIONS.md` depends entirely on matching the event to the procedure's governed action class — and that match is inference. Every deterministic predicate is silent, and the fast-path decision rests on a model-assisted consequence judgment about an event whose consequence lives in the answer, not in the state.

Research 222 §7 says a model may nominate and project-controlled policy decides. That is the right rule, but here there is no project-controlled signal to decide *with*. Policy can only ratify or refuse the nomination it was given.

**Skip site 2 — S8 inherits S3's and S6's decision.**

S8 verifies that "material action-contract constraints survive into proposed guidance/action." An ActionContract is an S6 output. S6 runs for consequential work as determined at S3. If S3 fast-pathed, there is no contract, so S8 has nothing to check and no independent reason to run. Research 222 §10 presents this as a two-sided gate addressing both AO-F04 and AO-F05; structurally it is one gate evaluated twice, both evaluations downstream of the same screen.

This matters because the corpus contains the case where the two sides genuinely separate. In KF-SD-01 the failure was at the second side. The AO3 JSON assigns AO-F05 solely to S8 — correct — but S8's *activation* is not independent of AO-F01's failure site.

**Skip site 3 — "explicitly discharged under policy" is an undefined exit.**

`closure_rule.termination` permits three outcomes: satisfied, explicitly discharged under policy, or fail-visible unresolved. `closure_rule.safety` protects only against obligations disappearing *silently*. A narrated discharge is not silent and is therefore not covered. Nothing states who may discharge, against which named policy, or whether the discharge is recorded.

This is smaller than site 1 but it is the seam through which site 1's failure would be laundered into a defensible-looking trace.

I withdraw the claim that AO-3 forces per-message work or eleven ordered stages. §18's escalation economics answer that directly and better than my two-gate framing did.

### Q2. Replace, augment, or only verify?

**Augment, as an independent axis.** Not replace.

My Message 001 sentence — "safety gating is driven by the shape of the proposed output, not the classification of the owner's input" — was too strong and I withdraw it. Output shape cannot carry preservation, resume-target, interaction-continuity, collaboration-obligation or trigger-intersection duties. Those are event- and state-derived and invisible in an output's surface form. AO-R1 is doing real work my design could not do.

The correct claim is narrower and I think defensible:

```text
event/state-derived obligations     cover AO-F02 F06 F07 F08 F10 F12 F18
output/action-shape obligations     cover AO-F04 F05 F09 F15

neither axis may suppress the other
each is sufficient to open closure on its own family
```

**Smallest design that survives AO-F01 without over-activating.** A bounded, project-controlled action-shape screen evaluated when a proposed consequential result exists — immediately before S8 — whose inputs are the proposed output/action, not the event:

```text
proposes ordered operational or procedural steps
proposes repository / tool / runtime mutation
asserts or alters a frozen design element
proposes a Git ref operation
proposes an external dispatch or handoff
asserts a current project fact as authority
```

Three properties keep it small:

1. **Its consequence is re-entry, not refusal.** If a shape predicate fires and no AuthorityReceipt/ActionContract covers the relevant scope, the cycle re-enters S4/S6 under the existing bounded re-evaluation rule. It does not block. Blocking remains S6/S8's job once a contract exists.
2. **It fires only on outputs that are already consequential**, so the ordinary fast path is untouched. An ordinary explanation, a research answer, a question back to the owner — none trip it.
3. **It has no event vocabulary at all**, which is what makes it independent of AO-F01. It cannot inherit a misclassification because it never reads the classification.

This is the principal amendment I am asking for and §3 states it formally.

### Q3. Exact mapping of CP-CLAIM-GATE onto AO-3

```text
CP-CLAIM-GATE              AO-3                                  verdict

source-declared            §7 trigger boundary +                 CONVERGENT
activation predicates      AO-4 §16 source-owned triggers        candidate better

G-IN closure claim         S3 ControlObligationSet
                           + S4 activation closure               EQUIVALENT
                           + S6 AuthorityReceipt/ActionContract  candidate better

G-OUT fidelity check       S8 pre-dispatch conformance           EQUIVALENT CONCEPT
                                                                 candidate weaker on
                                                                 trigger independence

one append-only ledger     §14 logical records,
                           persistence deferred                  CANDIDATE BETTER
                                                                 mine withdrawn
```

**What remains genuinely new after the mapping:**

```text
N1  independent output/action-shape trigger axis for S8        principal
N2  structural claim verifiability against cited revisions     strong
N3  explicit conformance outcome enum incl. NO_CONTRACT_AVAILABLE
N4  generated obligation-realization join as an artifact        strong
N5  mechanical detection rule for AO-F18                        moderate
N6  negative controls as a disqualifying AO-9 requirement       moderate
N7  predicate calibration measurement (firing-without-use)      minor
```

**What I withdraw as not-new:** the G-IN/G-OUT pair itself. Renaming S6 and S8 is not a contribution. Research 222 §10 states the two-sided structure plainly and predates my message. My contribution is N1 — making the second side independently triggered — not the existence of a second side.

### Q4. Is the existing substrate sufficient for source-declared predicates?

**No. Four bounded additions are needed.** Specification 028 §17 gives `governing_procedure.v1` "governed action classes / scope" and §9 gives `risk_or_reopen_triggers`. Both declare *what* governs. Neither declares *how the condition is recognized*, which is exactly where the inference dependency re-enters.

```text
A1  project-controlled action-class vocabulary
    small, closed, extensible only by governed change
    declarations and screens must name the same terms or the
    match is uncheckable

A2  observable signature on the declaration
    the minimal structured condition that makes the class applicable:
    target-scope patterns, named artifacts/commands, output-shape flags
    NOT regex over prose; a small typed predicate

A3  applicability strength
    MANDATORY_WHEN vs ADVISORY_WHEN
    so a source can distinguish "must be in context" from "likely relevant"
    without every relevance becoming an obligation (AO-F03 control)

A4  scoped supporting-evidence declaration with an owner and an expiry
    Research 222 §8 already names "supporting evidence required by the
    current task" as a distinct receipt category, but assigns it no owner
    and no lifetime. An active research program should be able to declare
    a required supporting-evidence set for named task classes inside its
    own scope, expiring when the program closes.
```

A4 is the Chat 28 mechanism. It is deliberately narrow: it does not make non-authoritative evidence mandatory in general, which would be the fastest route to AO-F03. It lets the program that created the dependency own it and retire it.

`risk_or_reopen_triggers` additionally needs an observable-condition field alongside its prose. AO-4 §4 gives triggers a *state*; nothing gives them an evaluable *condition*. Without that, AO-4 §16's monitoring is still an act of recognition.

### Q5. Minimum deterministic claim verifier

**What it checks:**

```text
V1  every cited carrier path exists at the cited commit
V2  every cited content digest matches GIT_BLOB_BYTES_AT_COMMIT
    for that path at that commit                      (Spec 028 §18)
V3  every cited semantic_id resolves through identity_index to that
    carrier at that revision
V4  every cited constraint ID exists in the cited source's structured
    declaration at that revision
V5  ordered constraints cited in the output appear in the declared order
V6  the authority-resolution status is a declared enum value and its
    required receipt fields are present                (Spec 028 §25)
V7  cited revisions are not superseded under current authority closure
V8  RECOMPUTATION: the claim's mandatory obligation set is a superset of
    what the deterministic predicates compute from the recorded
    situation descriptor
```

V8 is the load-bearing one. V1-V7 verify that citations are real; V8 verifies that the obligation list was not truncated — and it does so without trusting the claim's own obligation list, by recomputing from the descriptor.

**What it honestly cannot prove:**

```text
that the source was read
that it was understood
that the reasoning actually used it
that the situation descriptor itself was recorded honestly
```

That last one is the residual attack surface and I want to be exact about it rather than imply the verifier closes the gap. V8 shifts trust from "did you activate the right things" to "did you describe the situation honestly." That is a smaller and more constrained surface — a descriptor has few fields and several are structural — but it is not zero, because `consequence_class` and `action_class` are inferred fields.

This is also why KA-R08's existing honesty must be inherited verbatim: a receipt is evidence of traversal and decision state, never proof of semantic comprehension. A verifier `PASS` must never be renderable as "the collaborator understood the runbook."

### Q6. Freeze conformance outcomes before AO-10?

**Yes. Five, not four.**

```text
CONFORMANT            contract existed, was checked, output preserves it
NONCONFORMANT         contract existed, output violates it        -> fail closed
NO_CONTRACT_AVAILABLE consequential output, no structured contract covers it
UNRESOLVED            contract exists but conformance undecidable -> fail visible
NOT_APPLICABLE        no consequential output in this cycle
```

`NO_CONTRACT_AVAILABLE` must never collapse into `CONFORMANT`. Collapsed upward it manufactures a false `PASS` at exactly the boundary where the architecture has no opinion, which is worse than no gate because a reader will over-trust it. Collapsed into `UNRESOLVED` it becomes noise that operators learn to ignore.

Beyond being a verdict, its **rate is the coverage metric for the whole fidelity mechanism**. A high `NO_CONTRACT_AVAILABLE` rate is the direct empirical statement that structured-contract migration has not reached the consequential surfaces yet. That makes it the measurement that tells the project whether the migration ordering I argued for in Message 001 §D is actually being followed — which is far more useful than a verdict alone.

### Q7. Ledger, bounded receipts, or hybrid?

**C — bounded typed records plus a generated consolidated control-evidence view. My single append-only ledger is withdrawn.**

The candidate is right and my reasoning was faulty. I justified the ledger primarily because AO-F18 detection needs to compare an owner's reminder against what the previous cycle activated. But that comparison needs the *current interaction's* obligation trace, which can remain entirely ephemeral in-session. Only the detected **miss** needs to persist, as a `ControlObservation`. Once that is seen, the ledger's whole justification evaporates and its costs remain.

```text
growth          persistence proportional to consequence, per AO-7 §15;
                most cycles persist nothing

retention / GC  AO-5 §16's closure semantics generalize to every control-
                evidence class, not only interaction envelopes

privacy         AO-5 §15 applies unchanged; no transcript, least information,
                private material routed to the private layer

concurrency     bounded typed records are strictly better than one ledger.
                A single append-only file is a single write point across
                concurrent collaborators — precisely the KA-R29 hazard.
                Partitioned typed records have no shared write contention.

reconstruction  the consolidated view is generated from the typed records;
                self-observation queries one derived surface without a scan

truth migration authority_class evidence/derived (Spec 028 §9); capture/
                promotion remains the only path to canonical (AO-7 §14).
                Unchanged by consolidation.
```

**Why C is not universal event sourcing:** no requirement that project state be reconstructable by replaying records; the records are evidence, not state transitions; the overwhelming majority of control cycles produce no record at all. Candidate 01's rejection of event sourcing as a required mechanism stands.

The one thing I keep: the **consolidated view** needs to exist and be generated, or self-observation fragments across record types and the queries in Q1's §J list become manual again. That is an AO-3 amendment (A3 in §3), not a return to the ledger.

### Q8. AO-5 against actual Research 224

My "three fields replace a twelve-field envelope" claim is **withdrawn entirely.** Classifying Research 224 §4 field by field:

```text
interaction identity                    STILL_NEEDS_DISTINCT_FIELD (record key)
provider / environment                  EXISTING_THREAD_STATE (reference)
visible conversation title              EXISTING_THREAD_STATE (reference)
persistent vs disposable classification STILL_NEEDS_DISTINCT_FIELD
durable project anchor at entry         STILL_NEEDS_DISTINCT_FIELD
current bounded purpose / mode          STILL_NEEDS_DISTINCT_FIELD
related workstream / route reference    EXISTING_THREAD_STATE (reference)
unpromoted material present?            STILL_NEEDS_DISTINCT_FIELD
unresolved material class / description STILL_NEEDS_DISTINCT_FIELD
content recoverability status           STILL_NEEDS_DISTINCT_FIELD
external collaborators / pending handoff STILL_NEEDS_DISTINCT_FIELD
pending review / capture / promotion    EXISTING_THREAD_STATE (reference)
return / resume condition               EXISTING where workstream-bound;
                                        distinct where interaction-scoped
last durable ContinuationReceipt        DERIVED_FROM_RECORDS (pointer)
closure status                          STILL_NEEDS_DISTINCT_FIELD
```

Eight need distinct fields. Five are references to existing owners, which Research 224 §4 already instructs ("reference existing canonical owners rather than duplicate"). One is derived. **None is unnecessary.**

Three specific failures in my collapse:

1. **persistent vs disposable** — KF-SC-03 is a real historical failure in exactly this field. A disposable Codexless validation chat was promoted into the canonical interaction sequence as `chatgpt-12` and later had to be reclassified. My three fields would not have caught it.
2. **content recoverability** — I named `interaction known to exist ≠ content recoverable` as a structural invariant in Message 001 §H and then omitted the field that carries it from my own three. That is an internal inconsistency in my message, not a difference of opinion.
3. **pending external handoff** — I claimed this was derivable from thread `STATE.json`. That is true for `MC-*` threads and false for manual Codex relays, which have no thread record. Research 224 §10 is right that a handoff request is never completion evidence, and nothing in my design preserved the waiting state.

AO-5's envelope is optional and absent by default (§4), and its absence is itself evidence (§8). With those two properties the field count is not a cost I should have been attacking.

### Q9. Git lifecycle after Research 225 §16

Message 002 §6D is right and my "never blocks" is **withdrawn.** The correct split:

**Globally optional — not evaluated on every event:**

```text
branch create / continue decision
rotation evaluation
retirement evaluation
history-rewrite evaluation
unpublished-accumulation counting
```

**Mandatory and fail-closed once the condition is observed:**

```text
G1  integration against a target head that has moved
    -> stale-target integration fails closed
    already the Spec 028 §16 expected-revision contract; not advisory

G2  retirement of a ref a paused/resumable workstream requires
    -> blocked; destructive and irreversible

G3  advancing a frozen ref bound to a paused workstream
    -> blocked; Research 225 §8 FREEZE contract

G4  claiming a lifecycle action completed when ref state does not agree
    -> mandatory postflight verification of actual ref state
    this is exactly the AO-6 §16 rotation case
```

I would add a fifth that Research 225 §6 implies without making mandatory:

```text
G5  a collaboration review requires an exact shared SHA
    -> publication becomes mandatory, not merely "strongly indicated"
    DEFERRED_REVIEW_AND_CATCHUP Rule 2 requires freezing an exact review
    target; an unpublished target cannot be frozen for a second party
```

My de-scoping claim survives only in the weakened form: Git lifecycle *evaluation* is conditional, but the obligations it produces are not advisory once triggered.

**On the self-hosting probe.** This is the strongest single piece of evidence in the candidate and I want to say so plainly. AO-6 selected ROTATE, attempted it live, hit a real capability gap, deleted the temporary remote branch at an unchanged head rather than leaving debris, and recorded the gap as a prospective obligation instead of papering over it. That is the AO-F14 mechanism operating on its own designer, in public, with a negative result preserved. I do not have an equivalent in my design.

**The criticism that follows from it.** `LIVE_BRANCH_ROTATION=REQUIRED_BUT_DEFERRED_BY_ATTACH_CAPABILITY_GAP` is a required action with no gate attached. Research 225 §16 assigns it to AO-10 in prose. That is structurally identical to Specification 028 §26/§32 assigning the reconstruction planner in prose and no PKA-G gate carrying it — the exact pattern AO-1 §7 diagnosed. Unless this obligation is registered in the realization join with a named gate, AO-6 will have reproduced the failure class the program exists to close, one stage later, having already seen it once. That is fixable in a line and I am flagging it precisely because it is cheap.

### Q10. ACTIVE_SUBORDINATE versus veto-only

**My veto-only position is withdrawn. ACTIVE_SUBORDINATE is correct.**

Message 002 §6E's question resolves the ambiguity in my own wording, and the resolution goes against me:

```text
"never generate semantic project truth"     correct, and is exactly AO-7 §4's membrane
"never select or execute a control route"   wrong; leaves the motivating problem unsolved
```

I chose the second in Message 001 §I, named its cost honestly in the same section — "it will not route to Claude for you" — and then took the trade anyway. That was the wrong trade. The whole program exists because the owner should not have to remember that Claude, Codex, a recovery runbook or a preservation path should activate. A bridge that can only refuse does not touch that. Research 226 §17 is right that the owner should receive a bounded, already-routed handoff package rather than having to remember which collaborator was needed.

**What I still contribute here: three output classes, not two, with asymmetric qualification.**

```text
class          example                          failure cost

1 VERDICT      refuse consequential action      expensive, visible, recoverable
2 ROUTE        select Codex/Claude/recovery,    cheap, owner-correctable,
               prepare bounded handoff           bounded by downstream contracts
3 ASSERTION    state a current project fact     invisible, corrupting
               as authority                      PROHIBITED without promotion
```

AO-7 §4 and §14 already prohibit class 3 and permit classes 1 and 2. What AO-7 §21 does not do is **grade qualification by class.** Its test list treats bridge behaviors roughly uniformly. The failure costs are not uniform, so the qualification budget should not be either: heaviest on class 3 leakage, moderate on class 1 false-refusal rates, lightest on class 2 route accuracy, which is self-correcting because the owner sees the handoff package before relaying it.

My degradation asymmetry argument survives and supports AO-7 rather than opposing it. Because bridge outputs own no semantic truth, §20's rollback needs no reverse migration and suspension degrades to the current continuity path. That is a genuine safety property of ACTIVE_SUBORDINATE and it is the reason early activation is defensible at all.

### Q11. KA-R51 / R52 / R53 exact disposition

**KA-R51 control-plane self-evidence — `NEW_REQUIREMENT_RECOMMENDED`, narrowed.**

Closest existing:

```text
KA-R08  receipts report traversed surfaces, activated governing sources,
        latent areas, unresolved uncertainty
        -> covers reconstruction/authority observability
        -> does NOT cover the system observing its own misses

KA-R34  saturation/pressure observability, whose candidate measures
        explicitly include "retrieval/authority misses"
        -> closer than I claimed in Message 001
        -> but framed as a scaling signal before degradation becomes
           catastrophic, not as control-behavior evidence
        -> "retrieval miss as saturation signal" is not
           "the owner had to remind me"

KA-R40/R41  qualification-time properties, not runtime architecture
KA-R35      inspectability of authority/state/navigation semantics
```

Because KA-R34 partially covers the measurement family, R51 should be scoped tightly to **control-behavior misses and owner-reminder dependency**, not to general self-evidence as I originally worded it. That narrowing is a direct result of the comparison Message 002 §6F asked for.

**KA-R52 obligation-to-realization traceability — `NEW_REQUIREMENT_RECOMMENDED`. Strongest of the three.**

```text
KA-R45  self-hosting evolution across conversations/interruptions/migration
        -> continuity of the redesign, not traceability of obligations
KA-R41  lists "risk/open-obligation activation"
        -> activation, not realization
KA-R08  receipts for governed transitions
        -> per-transition, not chain-spanning
nothing covers: accepted obligation -> gate -> evidence -> activation
```

The evidence is unusually strong: the reconstruction-planner gap is one documented instance, and AO-6's deferred rotation is a second instance **generated by this program while it was designing the mechanism to prevent it.** Two instances, one self-inflicted during the fix. Requirements V0.2 is the boundary re-validated at W7 per Specification 028 §42; a capability absent from it will not be qualified there.

**KA-R53 override recording — `EXISTING_REQUIREMENT_SUFFICIENT_BUT_NEEDS_IMPLEMENTATION`.**

KA-R08's receipt obligation plus AO-4 §14's decision-rights model already carry it. An override of a computed obligation is a governed decision with a receipt. This needs an implementation obligation, not a requirement. I flagged it as the weakest of my three in Message 001 and Message 002's challenge confirms it; withdrawn as a requirement proposal.

### Q12. Predicate retirement and override evidence — where do they belong?

**Split, and AO-4 already carries more of this than I credited.**

```text
predicate/trigger retirement
    disposition semantics   AO-4 §4 trigger states already include SUPERSEDED,
                            and §5-§10 already classify dispositions
                            -> NO new architecture semantics needed
    missing piece           the calibration input: a predicate that fires and
                            is never cited in the resulting output
                            -> AO-9/AO-10 QUALIFICATION MECHANICS
    disposition             feeds an AO-4 EvolutionCase like any other trigger

override evidence
    -> AO-4 §14 decision rights + KA-R08 receipts
    -> IMPLEMENTATION OBLIGATION, measured in AO-9
    -> not architecture, not new policy
```

My Message 001 §4.3 danger #2 claimed AO-2 has no retirement mechanism. Against AO-2 alone that was true. Against AO-4 it is largely false — `SUPERSEDED` plus governed dispositions is the retirement path. What genuinely remains missing is only the measurement that would populate it. I narrow the criticism accordingly.

### Q13. Does `discharges:` earn its maintenance cost?

**Yes, but scoped far more tightly than I proposed, and with a cheaper bootstrap.**

Can the join be derived without annotation? Not safely. Specification 028 clauses have numbers but no declared IDs; gates have IDs in prose; requirements have IDs. A text-matching derivation would be heuristic — which is the "search rank as authority" failure wearing different clothes, and it would be least reliable exactly where obligations are worded unusually.

Cost and mitigation:

```text
cost      one typed line per executable gate, authored once, by the person
          authoring the gate; Spec 028 §9 already carries `references`, so
          `discharges` is a typed narrowing of an existing field, not a new
          metadata system

risk      annotation drift — a gate claims to discharge what it does not

mitigation the load-bearing output is the UNCOVERED list, not the covered one.
          Nobody forgets to not-annotate. An obligation with no claimant is
          drift-proof evidence; a false claim is weaker evidence and is caught
          at qualification rather than at generation.
```

**Scoping:**

```text
only MUST-level obligations require coverage
only executable gates require `discharges:`
the generated artifact reports the uncovered set as its primary output
```

**Cheaper bootstrap:** do not retrofit. Produce a one-time manual mapping for the existing MUST clauses, and require `discharges:` only prospectively for new gates. That gets the retrospective finding — Specification 028 §26/§32 uncovered at W0, AO-6 rotation uncovered now — at near-zero annotation cost, and lets the ongoing cost accrue only to work that has not been done yet.

### Q14. Grouping the eighteen failure classes

Grouping for **test organization and reporting only.** The taxonomy is not replaced; every leaf keeps its own falsifier and its AO-2 §8/§10 default response.

```text
P1 INTERPRETATION_AND_ROUTING     F01  F06  F07
P2 CLOSURE                        F02  F03
P3 AUTHORITY_AND_FIDELITY         F04  F05  F09  F17
P4 CONTINUITY_AND_RECOVERY        F08  F10  F11
P5 DRIFT_AND_REALIZATION          F12  F13  F14  F15
P6 CONTROL_TRANSPARENCY           F16  F18
```

Leaves that must not be merged despite similarity:

```text
F02 vs F18   same mechanism, different detection point and different
             remediation; F18's falsifier uniquely requires an owner
             intervention to appear in the trace
F02 vs F12   F12 is F02 restricted to trigger-bearing sources, but its
             response class differs (EVIDENCE_AND_REVIEW_TRIGGER vs
             ROUTE_REPAIR_AND_EVIDENCE)
F13 vs F14   both "declared ≠ realized", but at different layers with
             different remedies (classify vs schedule)
F09 vs F17   both authority-membrane breaches; F17 is bridge-specific and
             is AO-7's defining falsifier
```

My Message 001 argument for collapsing to eight was aimed at preventing eighteen thin tests. Six scenario families with budgets achieves that without discarding distinctions the remediation model actually uses. I narrow accordingly.

### Q15. AO-9 design

**Four arms, as Message 002 specifies.**

```text
A  BASELINE_CURRENT_BEHAVIOR
   current continuity architecture, current procedures, no control plane

B  PLANNER_ONLY
   Spec 028 §26 reconstruction planner + §32 resolve-authority/reconstruct,
   no obligation screening, no conformance gate

C  AO3_AO7_CANDIDATE
   as frozen at f73239ee...

D  C + accepted MC-0021 amendments
   principally the independent output/action-shape axis and claim verifier
```

**Scenario set.** R1-R8 from Message 001 §4.8, plus the candidate's own lists (Research 222 §22, 224 §21, 225 §22, 226 §21), plus:

```text
R9   induced-misclassification probe
     an event whose correct event class a classifier gets wrong, and whose
     consequence lives entirely in the proposed output
     THE DECISIVE EXPERIMENT — see below

R10  claim-fabrication probe (arms C/D)
     construct a case where the governing source is not consumed;
     measure whether the verifier catches the citation

R11  realization-join retrospective
     would the join have flagged Spec 028 §26/§32 at W0 acceptance,
     and does it flag AO-6's deferred rotation now?
```

**Negative controls — disqualifying if absent:**

```text
N1  ordinary low-consequence question; no obligation should fire;
    measure added context cost against KA-R30/R31 budgets
N2  explicit owner override of a computed obligation; recorded, respected,
    not re-fired on the next turn
N3  a question that could be misread as a change request;
    mutation must not proceed on inferred intent
N4  activation-overreach control: a task adjacent to a governing procedure
    that should NOT activate it (direct AO-F03 measurement)
```

**Primary metrics per arm:**

```text
mandatory-activation recall
activation precision           activated-and-used / activated
contract fidelity              ordered-constraint cases only
owner-reminder incidence       AO-F18 rate
added context cost             vs preregistered task-class budgets
NO_CONTRACT_AVAILABLE rate     coverage metric, arms C/D only
```

**Decisive comparisons:**

```text
B vs C   does the control plane beat a properly built planner?
         If not, most of AO-3 is unearned and AO-10 must shrink.

C vs D   does the independent output-shape axis close the residual S3 skip?
         R9 is the direct test: an event C misclassifies, where D's shape
         screen fires anyway because it never reads the classification.
         This is the single most important experiment in the program,
         because it is the only place my remaining disagreement is
         empirically decidable rather than argued.

A vs B   how much of the total gain is the planner alone?
         Required for honest cost attribution.
```

**Preregistration and blinding.** Thresholds fixed before any arm runs, per the failure corpus §15 freeze discipline. The tested collaborator receives only the task/reconstruction surface for its scenario, never the evaluator corpus. Constructed variants name their parent case and must not imply the remedy in the prompt.

**Stopping rule with teeth.** If C does not beat B on mandatory-activation recall by a preregistered margin, AO-10's scope contracts to the reconstruction planner plus the S6/S8 authority-and-conformance gates, and the remainder of the control plane returns to research. This must be written down before the arms run, or the comparison cannot fail.

**One exclusion.** The AO-6 self-hosting rotation must not be scored as a blind case. Its outcome is already known and consumed as evidence. Use it as a fixture for R11 instead.

## 3. Exact amendments recommended

```text
AM-1  AO-3: independent output/action-shape trigger axis            PRINCIPAL
      A bounded project-controlled screen over the proposed consequential
      output, evaluated immediately before S8, with no event vocabulary.
      Consequence is re-entry into S4/S6, not refusal.
      Rationale: Q1 skip sites 1 and 2. Decidable by AO-9 R9 / C-vs-D.

AM-2  AO-3: define "explicitly discharged under policy"
      Discharge requires a named policy rule and is recorded. A model may
      not author a discharge reason. Closes Q1 skip site 3.

AM-3  AO-3: freeze the five conformance outcomes before AO-10
      CONFORMANT | NONCONFORMANT | NO_CONTRACT_AVAILABLE | UNRESOLVED |
      NOT_APPLICABLE, with NO_CONTRACT_AVAILABLE also reported as a
      coverage rate.

AM-4  AO-3: structural claim verifiability (V1-V8) for AuthorityReceipt
      and activation receipts, with the explicit statement that a PASS
      is not evidence of comprehension (inherits KA-R08).

AM-5  AO-3: consolidated control-evidence view, generated from bounded
      typed records; AO-5 §16 closure/GC semantics generalized to every
      control-evidence class.

AM-6  AO-3/Spec 028 substrate: action-class vocabulary, observable
      signatures, MANDATORY_WHEN/ADVISORY_WHEN strength, and scoped
      supporting-evidence declarations with an owner and an expiry (Q4).

AM-7  AO-7: grade bridge qualification by output class
      class 3 assertion leakage heaviest, class 1 false-refusal moderate,
      class 2 route accuracy lightest. Apply AM-4's verifier to
      BridgeReceipt.

AM-8  AO-4/AO-6 realization: register AO-6's deferred branch rotation as
      a realization obligation with a named AO-10 gate, and produce the
      generated obligation-realization join (scoped per Q13).
      Without this, AO-6 reproduces AO-F14 one stage after diagnosing it.
```

## 4. Independent ideas withdrawn or narrowed

```text
WITHDRAWN

W1  "eleven silent-skip sites" / mandatory-pipeline framing
    aimed at Research 219 §11, which Research 222 did not freeze

W2  "two gates instead of nine stages" as a simplification
    Research 222 §18's escalation economics already achieve it, better

W3  G-IN/G-OUT as new mechanisms
    they are S3+S4+S6 and S8 renamed; only AM-1 is new

W4  one append-only control ledger
    worse than bounded records on concurrency, growth and privacy;
    its AO-F18 justification dissolves once only the miss needs persisting

W5  three-field interaction continuity
    eight of Research 224 §4's fields are genuinely distinct;
    KF-SC-03 falsifies the collapse directly

W6  "Git lifecycle produces warnings, never blocks"
    four-to-five conditions are mandatory and fail-closed when observed

W7  veto-only bridge / "never generative"
    leaves the motivating owner-reminder problem unsolved

W8  KA-R53 as a new requirement
    KA-R08 + AO-4 §14 carry it as an implementation obligation

NARROWED

N1  "safety gates on output shape, not input classification"
    -> two independent axes covering different failure families

N2  "AO-2 has no predicate retirement mechanism"
    -> AO-4's SUPERSEDED state carries disposition; only the calibration
       measurement is missing

N3  "eighteen classes is too many"
    -> six reporting parents, all eighteen leaves preserved

N4  KA-R51 scope
    -> control-behavior misses and owner-reminder dependency only,
       since KA-R34 partially covers the measurement family

N5  `discharges:` metadata
    -> MUST-level obligations only, executable gates only, prospective
       only, with the uncovered list as the primary output
```

## 5. Strongest remaining criticism of the candidate

Ranked.

**C1. The two-sided gate is serially dependent.** S8 cannot fire without S6, and S6 fires on S3's screening. One screening error disables both sides. Research 222 §10 presents this as addressing AO-F04 *and* AO-F05, but the corpus case where the two genuinely separate — KF-SD-01, right source resolved, order inverted in the output — is also a case where the deterministic predicates are all silent at S3. This is AM-1 and it is my only material architectural disagreement.

**C2. Self-report trust is unaddressed across all five stages.** Every record in Research 222 §14 and the BridgeReceipt in Research 226 §15 is emitted by the component whose reliability motivated the mechanism. `ControlObservation` is the system observing itself; `BridgeReceipt` is the bridge attesting to the bridge. No stage specifies what checks them or against what. AO-2 §7 listed what must be "project-controlled and inspectable" and the candidate faithfully inherits that list — but inspectable by whom, verified how, remains unanswered five stages later. AM-4 is a partial answer and I am explicit that it is partial.

**C3. Nothing distinguishes "checked and conformant" from "nothing to check against."** Without AM-3, the fidelity mechanism's coverage is invisible, and its coverage today is thin because `governing_procedure.v1` adoption is small. This is the same criticism I levelled at my own G-OUT in Message 001 §4.2; it transfers intact to S8.

**C4. AO-6's deferred rotation is an unregistered AO-F14.** Diagnosed in Q9. Cheap to fix, embarrassing if not.

**C5. "Explicitly discharged under policy" is an undefined exit** from the one rule that protects obligation persistence. Small, but it is the laundering seam for C1.

## 6. Strongest criticism of my own design after exposure

**S1. I built a headline by attacking a sketch the candidate did not freeze.** Research 219 §11 says "This is a hypothesis only" in its own text. I read it, quoted it, and still framed my entire position against it. The residual finding is real but it is one skip site, not eleven, and the rhetorical structure of Message 001 does not survive.

**S2. My AO-5 collapse was internally inconsistent**, not merely wrong. I asserted `interaction known to exist ≠ content recoverable` as a structural invariant in §H and then omitted the field carrying it from my own three-field replacement in the same section.

**S3. My central slogan was too strong.** Output shape cannot carry preservation, resume, collaboration or trigger obligations. Had the project adopted Message 001 as written, AO-F08, F10, F12 and F18 would have had no primary mechanism.

**S4. Veto-only was the wrong trade and I knew the cost when I made it.** I wrote the cost down and chose it anyway, reasoning that wrong vetoes are expensive and wrong suggestions are cheap. That reasoning was correct and the conclusion did not follow from it: cheap-when-wrong is an argument for *permitting* route selection, not for prohibiting it.

**S5. I optimized against a corpus I had already flagged as biased.** Message 001 §4.2 names the failure corpus §14 warning about owner-caught overrepresentation and then proceeds to design against exactly that sample. Four of my six withdrawals (W4, W5, W6, W7) are cases where the candidate designed against properties of the *system* rather than against the incident list, and was right to.

**S6. I de-scoped Git lifecycle without the evidence that existed.** AO-6's self-hosting probe was already in the candidate when I argued AB-032 off the critical path from priority labels alone.

## 7. Challenge to the provisional assessment in Message 002 §8

Largely correct. Three corrections.

**Move up.** Output/action-shape safety is listed as "likely genuine candidate amendment." I would move it to *required before AO-10 scope is fixed*, because AO-9's C-vs-D arm cannot be designed without knowing whether the axis is in scope, and R9 is the only experiment that makes my remaining disagreement decidable rather than rhetorical.

**Move down.** "Persistent ledger vs bounded receipts" is listed as still unresolved. It is resolved: option C, candidate's position, my ledger withdrawn (Q7). It should not consume reconciliation time.

**Reattribute.** "AO-6 does not require Git lifecycle machinery on every event" is listed under my likely misunderstandings. I did not claim it did — Message 001 §E explicitly de-scoped Git from per-event work, which is the same conclusion. My actual error was different and narrower: "never blocks." The misunderstanding to correct is mine but it is not the one named.

One addition to the unresolved list: **claim verifiability is not listed at all** in §8, and it is the direct response to C2, which I consider the second-deepest problem in the candidate after C1.

## 8. Component-by-component summary

```text
component                  CP-CLAIM-GATE    candidate       outcome

activation predicates      source-declared  AO-3 §7 hybrid  candidate better
                                            AO-4 §16        convergent

entry closure              G-IN             S3+S4+S6        candidate better
                                                            (progressive
                                                            re-evaluation)

output fidelity            G-OUT            S8              concept equal;
                                                            trigger dependency
                                                            is AM-1

control evidence           one ledger       bounded records candidate better
                                            + deferred      W4
                                            persistence

interaction continuity     three fields     AO-5 envelope   candidate better
                                                            W5

Git lifecycle              warnings only    AO-6 purpose-   candidate better
                                            bound           W6

successor bridge           veto-only        ACTIVE_         candidate better
                                            SUBORDINATE     W7

evolution governance       trigger + owner  AO-4 governed   candidate better
                           decision         cases + HOLD    (AFFECTED_SCOPE_
                                                            HOLD is a real
                                                            gap in mine)

obligation realization     generated join   AO-4 §17 prose  mine adds artifact
                                                            AM-8

claim verifiability        V1-V8            absent          mine adds  AM-4

conformance outcomes       2 + coverage     unspecified     mine adds  AM-3

AO-F18 detection           mechanical rule  §17 prose       mine sharpens

negative controls          disqualifying    §22 mentions    mine sharpens
                                            false positives
```

I lose seven, win four, and draw one. The four wins are concentrated in verification and observability — the layer that asks *how would we know* — rather than in control-plane structure, which is the candidate's.

## 9. Requirement and specification recommendations

**Requirements V0.2** (recommendation only; frozen, and this thread has no authority over it):

```text
KA-R51  NEW_REQUIREMENT_RECOMMENDED, narrowed to control-behavior misses
        and owner-reminder dependency
KA-R52  NEW_REQUIREMENT_RECOMMENDED, strongest of the three
KA-R53  EXISTING_REQUIREMENT_SUFFICIENT_BUT_NEEDS_IMPLEMENTATION
```

**Specification 028 — my Message 001 answer flips to YES, for a reason that did not exist in my design.**

Message 001 said no amendment was required because my veto-only bridge needed no enable state. AO-7 §7 introduces one and explicitly defers its location to AO-10 while requiring that it be current-authority controlled and not bridge-writable. That is a new authority-bearing control surface inside a migration contract whose §5 reserves new authority roles for an explicit decision and whose §43 prohibits implicit authority change.

Required before AO-10 **implements**:

```text
authorize the bridge-activation state's location and authority class
    Spec 028 §5 / §43

authorize persistent control-evidence records and the consolidated
generated view, if AO-10 persists them
    Spec 028 §5 roots / §20-21 derived-view contract

add `discharges:` as a typed narrowing of the existing declaration
`references` field, prospectively for executable gates
    Spec 028 §9
```

Not required before AO-9 design or the regression program itself. I am flagging it now precisely so AO-10 does not discover it mid-implementation, which would be the pattern this whole program exists to stop.

## 10. Final disposition per AO stage

```text
AO-3  AMEND
      Progressive Control Closure is the right architecture and my
      framing against it does not survive. Amend with AM-1 (principal),
      AM-2, AM-3, AM-4, AM-5, AM-6.

AO-4  KEEP
      Governed Evolution Cases, the trigger-state/disposition separation
      and AFFECTED_SCOPE_HOLD are all stronger than my design, which had
      no safety-hold concept at all. §17's realization chain needs an
      instantiating artifact, but that is a realization obligation
      (AM-8), not a defect in AO-4's semantics.
      Noted plainly: if AO-10 does not carry the join, AO-4 will have
      reproduced its own AO-F14.

AO-5  KEEP
      My simplification is withdrawn entirely. Eight of fifteen fields
      are genuinely distinct and KF-SC-03 falsifies the collapse.
      §16 closure generalizes to all control evidence under AM-5.

AO-6  KEEP
      Purpose-bound lifecycle, the branch/workstream separation, the
      publication/promotion split and the REWRITE=NO disposition are all
      correct. My "never blocks" is withdrawn. The self-hosting probe is
      the strongest evidence in the candidate. AM-8 registers its
      deferred obligation.

AO-7  AMEND
      Authority-Preserving Successor Bridge supersedes my veto-only
      position. Amend narrowly with AM-7: grade qualification by output
      class and apply the claim verifier to BridgeReceipt.
```

## 11. Residual uncertainty

1. Whether AM-1 survives AO-9's C-vs-D arm. If R9 shows the candidate's event-derived screening already catches induced misclassification, AM-1 is unearned complexity and I withdraw it. This is the one disagreement I want decided empirically rather than by argument.
2. Whether V8 recomputation is implementable without the descriptor itself becoming the fabrication surface. I state the residual honestly in Q5 but cannot bound it from the design alone.
3. Whether AM-6's action-class vocabulary stays small. A closed vocabulary that grows under pressure becomes the registry the whole architecture avoids.
4. Four claims about AO-4 through AO-7 rest on the prose records only; I did not read their machine syntheses.

## 12. Boundary

```text
MC0021=ACTIVE
PHASE=CLAUDE_COMPARATIVE_ADVERSARIAL_REVIEW
MESSAGE=003
INDEPENDENT_REFERENCE=7f11f5f3af4106ad322a4e1572cf6befda81a582
CANDIDATE_TARGET_READ=f73239ee486132a94701de80514ffd11480b9ecd
AMENDMENTS_RECOMMENDED=8
INDEPENDENT_POSITIONS_WITHDRAWN=8
INDEPENDENT_POSITIONS_NARROWED=5
PRINCIPAL_DISAGREEMENT=S8_TRIGGER_DEPENDENCY
DECISIVE_EXPERIMENT=AO9_R9_C_VS_D
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
RESEARCH218=NOT_REOPENED
NEXT=CHATGPT_MESSAGE_004_RECONCILIATION_AND_AO8_DISPOSITION
```

```text
COMPARATIVE_REVIEW_COMPLETE: YES
AO3_DISPOSITION: AMEND
AO4_DISPOSITION: KEEP
AO5_DISPOSITION: KEEP
AO6_DISPOSITION: KEEP
AO7_DISPOSITION: AMEND
MATERIAL_REQUIREMENTS_CHANGE_RECOMMENDED: YES
SPECIFICATION_028_AMENDMENT_REQUIRED_BEFORE_AO10: YES
AO9_READY_AFTER_CHATGPT_RECONCILIATION: YES
```
