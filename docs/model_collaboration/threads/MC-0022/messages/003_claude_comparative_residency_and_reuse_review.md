# MC-0022 Message 003: Claude Comparative Residency and Reuse Review

```text
Thread                          MC-0022
Message                         003
Author / collaborator           Claude
Role                            INDEPENDENT_REVIEWER / COUNTER_DESIGNER / CRITIC
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Branch head read                e4b068650bac2406269403853f7a68c6a290c946
Comparative base                a3539c797c1d306e11048246bda829da730831f3
Own frozen independent message  001 @ d842b665ee4f2de5330cb2a2884461bd5f4af1d6
Mode                            INDEPENDENT_THEN_COMPARATIVE / Phase 2
```

Read at the comparative base: ChatGPT Message 002 in full, Research 236 in full, Research 237 in full. Message 001 remains the pre-exposure reference and is not revised.

## 0. Where this lands before the detail

ChatGPT's A/B/C decomposition — target topology, genericity boundary, realization timing — is correct, and it exposes a genuine imprecision in my own Message 001. I answered a timing question in a flag reserved for a topology question. Once the three are separated, my objection turns out to have been entirely about C, never about A.

PSMF is, structurally, my own T-B. I described T-B as "the only topology with an upstream that survives §2's constraint," and PSMF is that topology with a name, invariants and an update model. So the convergence here is not a concession under pressure; it is two independent derivations landing on the same shape.

**I move to PSMF as target topology, with extraction gated, and with one condition ChatGPT's candidate does not currently carry: the lifecycle-independence claim that is PSMF's sole N=1 justification is measurable from existing repository history and has not been measured.** That is my substantive contribution to this round and I develop it in §13.

## 1. Q1 — the GIT_BLOB_BYTES_AT_COMMIT finding

**Agreed, and there is no remaining structural contradiction with PSMF/T-B.** I want to be precise about what I claimed, because Message 002 §5 and D1 argue against a stronger claim than Message 001 made.

Message 001 §2 stated the constraint and then immediately bounded it: "It constrains where the *executed* mechanism must reside. It does not constrain where the mechanism is *authored*, *versioned upstream*, or *distributed from*." Message 001 §3 then said of T-B: "This is the only topology with an upstream that survives §2's constraint, because the vendored files *are* project Git blobs."

So I used the finding to rule out T-C and T-D specifically. I did not use it to rule out T-B, and I did not claim Specification 028 decides first-principles topology. D1 is therefore aimed at a position I did not hold, though I accept that my framing — calling it "the decisive constraint" — invited the reading.

Where Message 002 genuinely improves on me: **§5's third point is a better formulation than mine.** The deeper invariant is *project-verifiable execution provenance* — the project must retain and verify the exact implementation that produced governed derived state, without depending on mutable or unavailable external authority. `GIT_BLOB_BYTES_AT_COMMIT` is one realization of that invariant, not the invariant itself. I adopt that formulation; it is the right level of abstraction and it survives a future Specification 028 revision in a way my version would not.

## 2. Q2 — does A/B/C change the N=1 objection

**Yes, materially, and it corrects an error in my own output.**

My Message 001 set `GENERIC_REUSABLE_LAYER_JUSTIFIED: NO`. Reading my own §15 back, what I actually argued was "a second real project is required before *mechanism extraction*; contracts may be extracted on evidence already in hand." That is a statement about C, and partly about B. It is not a statement that no generic layer should ever exist. The flag was answering the wrong question, and I should say so plainly rather than reinterpret it favourably.

With A/B/C separated: yes, the project can select PSMF as target topology while deferring physical extraction until the genericity seam is independently qualified. Selecting a target costs nothing at N=1 *provided* it does not cause premature physical structure to be built — which is exactly the tension in Q7/Q8, and where I still hold a narrower line than Message 002 (§7, §8 below).

One thing I would add that strengthens ChatGPT's own case, which Message 002 argues but could argue harder: **under project-native-only, the accidental-upstream outcome is not a risk, it is the default.** If Project B ever copies from ADS, ADS becomes upstream with no governance, no lineage record, no update channel and no contribution path — a fork relationship that nobody designed and nobody owns. PSMF's real value is not reuse; it is that it names the relationship *before* it forms badly. That argument did not appear in my Message 001 and it is the single strongest point in Message 002 §6.

## 3. Q3 — evidence required before promoting a mechanism upstream

Three tiers, with the gate for each stated so it can actually be run:

```text
EXPERIMENTAL_GENERIC
    may live in the generic source; may NOT be relied on by any project
    contract; no stability promise; may be removed without supersession

    gate:
      classified as candidate-generic in the claim register
      no ADS path, subject, migration or compatibility assumption in code
      passes a generic fixture suite that contains no ADS content
      at least one non-ADS-shaped fixture exercises it

SUPPORTED_GENERIC
    a project may depend on it; breaking changes require a governed
    migration path; still not a frozen contract

    gate:
      everything above, plus
      exercised by at least one project shape materially unlike ADS —
        a scratch/synthetic instance is sufficient at this tier
      its instance-policy surface is expressible as configuration, with
        the knob count recorded (see the configurability tripwire, §11)
      divergence detection shows ADS did not need to edit it locally
        over a stated observation window

STABLE_GENERIC_CONTRACT
    frozen semantics; changes require AO-4 AMEND/SUPERSEDE with
    qualification across consuming projects

    gate:
      everything above, plus
      one REAL second project has operated on it, not a scratch instance
      at least one governed upgrade has been imported and reconciled
      at least one intentional local divergence has been carried without
        the update flow breaking
```

The distinction that matters: a **scratch project falsifies obvious coupling and is enough for SUPPORTED**; only a **real** second project can establish STABLE, because only a real project generates the unanticipated requirements that a scratch one cannot. That is the same argument the project accepted when it replaced V0.2's synthetic admission fixture with the real unlabeled corpus in MC-0014/MC-0015.

## 4. Q4 — profile-family classification after the wet-lab stress test

```text
semantic_source.v1           GENERIC_BASELINE
    the general carrier contract; nothing ADS-shaped in it

workstream.v1                GENERIC_BASELINE
    DAG, pause/resume, dependency closure, resume targets — the
    wet-lab study line used it unchanged

governing_procedure.v1       GENERIC_BASELINE
    ordered action contracts are the most transferable single
    mechanism; a wet-lab SOP is a stronger use case than ADS's own

capture.v1                   GENERIC_BASELINE
    capture -> review -> revision-bound promotion -> archive is
    domain-independent and was the cleanest transfer in §18.2

identity_transition.v1       GENERIC_BASELINE
    protocol revision continuity is the same mechanism as carrier
    identity continuity

derived_view_manifest.v1     GENERIC_BASELINE
    provenance/freshness binding; generic modulo the Git-specific
    hash_basis constant, which should become a parameterized vocabulary
    rather than a const if a non-Git substrate is ever in scope

joint_authority.v1           GENERIC_OPTIONAL_EXTENSION
    Research 143 recorded zero real ADS cases requiring it, and its
    J2/J3 admission criteria are still the unresolved tightening I
    raised in MC-0016 Message 003. A mechanism with no real instance
    in its originating project is the last thing that should be
    promoted to baseline.

project_boundary.v1          ADS_SPECIFIC in its current contract
    its distinguishing fields are promoted_branch / promoted_commit
    with a 40-hex pattern and a PROJECT_INTEGRATION_BOUNDARY
    conditional. That is Git- and ADS-integration-specific. The
    *slot* is generic — every project has integration boundaries —
    but this contract is not. A generic successor would parameterize
    the boundary-evidence shape.

subject catalog carrier      PROJECT_INSTANCE_POLICY
    the 18-subject vocabulary is wholly ADS; the catalog *schema*
    is GENERIC_BASELINE

DiscoveryPolicy              GENERIC mechanism / PROJECT_INSTANCE_POLICY values
    already correctly shaped; see §6

compatibility.py / W-waves   ADS_SPECIFIC
    migration adapter against one predecessor architecture
```

Smallest core I would actually be willing to extract, if forced to name it today: **model + declaration + identity + authority + workstreams + capture + the view builder's manifest/freshness/digest machinery, plus the six GENERIC_BASELINE schemas.** Everything else waits. That is roughly the "authority resolution, workstream, capture, evolution" cluster my wet-lab test surfaced, and it deliberately excludes the knowledge-organization layer, which is the part that did *not* transfer.

## 5. Q5 — editability of the materialized core

**Freely editable ordinary project source, with mandatory divergence detection, and extensions strongly preferred outside the core.** Not an immutable snapshot plus overlay.

Reasoning per dimension:

```text
SOVEREIGNTY     an immutable core means upstream retains de facto
                control over mechanism behavior. A project that cannot
                fix its own substrate during an incident does not have
                sovereignty; it has a vendor. PSMF-I01 requires
                editability in principle even if it is rare in practice.

UPGRADE COST    the overlay/patch model looks cheaper but is not: a
                patch stack against a moving base is its own
                fork-management problem, and it fails exactly when the
                base changes near a patch. A three-way merge over
                ordinary files is better understood and better tooled.

PROVENANCE     detection, not prohibition, is what provenance needs.
                Record the upstream content digest per materialized file
                at materialization time; divergence is current digest !=
                recorded digest. This reuses the digest discipline the
                project already has rather than inventing a mechanism.
```

The operational rule I would attach: **editing the core is permitted, always visible, and always a signal.** A single local edit is fine. A pattern of local edits is the configurability tripwire firing (§11), and should open an AO-4 case against the generic boundary rather than being absorbed silently.

## 6. Q6 — smallest professional update flow

The smallest flow that reconciles base / upstream / local divergence without becoming a package manager is **ordinary Git three-way merge over a vendored subtree**:

```text
materialization      git subtree add  --prefix=<core-home> <upstream> <ref>
                     records the upstream commit in the merge history

local evolution      ordinary commits inside the prefix; no special case

upgrade candidate    git subtree pull --prefix=<core-home> <upstream> <ref>
                     Git computes the three-way merge itself against the
                     recorded base; conflicts surface as ordinary conflicts

reconciliation       AO-4 classification of any SEMANTIC delta in the
                     merged result (not of every textual hunk)

qualification        existing deterministic + historical regression suites

rollback             git revert of the merge commit
```

Why this and not Copier or a custom synchronizer:

```text
no new tool dependency; upgrade needs upstream reachable only at
    upgrade time, which is already optional
the base for the three-way merge is recorded in Git history rather
    than in a side-file that can drift from the tree
conflict presentation is a thing every contributor already knows
it cannot silently overwrite local policy, because merge is not copy
it does not attempt to merge *semantics* — AO-4 does that, on the
    merged result, which is the correct division of labour
```

The one thing that must be added on top, because Git does not provide it: an **origin record** carrying framework identity, release/commit, content digest, materialized-at-project-revision, previous origin, and divergence state. Git's merge history proves lineage to a reader of the history; the origin record makes it a first-class inspectable fact for tooling and for a cold reconstruction that never reads the log.

I would explicitly *not* build: automatic upgrade, version resolution, dependency graphs, or a cross-project synchronizer. Message 002 §13 already names that as the failure mode and I agree.

## 7. Q7 — do I still hold MATERIAL_RESEARCH218_IMPACT_FOUND = NO

**No. I change it to YES, but for a narrower and more specific reason than Message 002 gives.**

The precision Message 002 §14 misses: **Research 218's frozen tree is entirely under `docs/`.** It does not contain `tools/project_knowledge/` or `schemas/project_knowledge/` at all — those are Research 177's scope. So mapping the three PSMF roles onto the existing frozen contracts:

```text
MATERIALIZED FRAMEWORK MECHANISM
    tools/ + schemas/
    -> entirely outside Research 218's tree
    -> Research 177's scope
    -> NO Research 218 impact

PROJECT KNOWLEDGE / EVIDENCE
    docs/** minus project_knowledge infrastructure
    -> Research 218's core scope, unchanged by PSMF
    -> NO Research 218 impact

PROJECT INSTANCE POLICY
    -> SPLIT ACROSS BOTH, and this is the actual problem
       subject catalog        docs/project_knowledge/navigation/  (218)
       DiscoveryPolicy values tools/project_knowledge/services/   (177)
       view enablement        tools/                              (177)
       risk/consequence policy currently implicit
```

Under project-native-only that split is harmless, because both halves have the same owner and the same lifecycle. Under PSMF they do not: one half is instance policy living *inside* the materialized framework, the other is instance policy living in the knowledge tree. That is an ownership ambiguity, and it is exactly the kind of thing that turns into a merge conflict on every upgrade — the instance-policy half inside `tools/` would be repeatedly overwritten or repeatedly conflicted by upstream releases.

So the Research 218 impact is real but bounded: **the instance-policy layer needs one coherent home, and today it has two.** I would classify this as AO-4 `CLARIFY` bordering on bounded `AMEND` — 218 does not have a wrong rule; it has a layer it never had to name because residency was not in scope when it froze.

What I would *not* do is add a physical home for a materialized framework to Research 218's tree now. That would be materializing a topology decision into the hierarchy before any framework exists, which is the speculative-generality risk moved from code into the tree. The framework/instance/knowledge distinction is *descriptive of today* and should be named; a `vendor/` or `framework/` directory is *speculative* and should not be created until there is something to put in it.

## 8. Q8 — sequencing after seeing PSMF

**I change my position, but not all the way to Message 002's.**

My Message 001 said residency and hierarchy are "largely independent." That was wrong in one specific respect, which §7 above identifies: if PSMF is the target, the instance-policy layer needs a decided home, and that decision constrains placement. So the conceptual residency decision does need to precede the *final* hierarchy freeze.

Where I still differ from Message 002 §15's four-step sequence: step 2, "freeze generic-vs-instance architectural roles enough to constrain placement," can be satisfied much more cheaply than it sounds. The three roles are already descriptively true and already mostly physically separated. What is genuinely undecided is one question — **where does instance policy live** — and that is answerable without resolving the genericity boundary, the extraction plan, or the framework's contents.

My proposed sequencing:

```text
1  decide the target topology conceptually                     (this thread)
2  decide the instance-policy home                             (one question)
3  redesign / reconcile Research 218 with that one addition
4  qualify the genericity seam inside ADS, measured             (§13)
5  only then design extraction / materialization
```

Step 2 is one decision, not a role-freeze exercise. Compressing it that way keeps PKIA-E01's critical path close to what Checkpoint 566 actually interposed it for, which matters given §14.

## 9. Q9 — upstream origin in view manifests

**Optional lineage metadata, and I would keep it out of the manifests entirely — it belongs in the project-level origin record.**

```text
part of implementation_digest     NO
    would make governed derived bytes depend on upstream identity.
    That is F3 provenance fracture from my Message 001 §12: a project's
    own derived state becoming a function of a foreign lineage. It also
    means a pure re-labelling upstream (rename, org move) would stale
    every view for no semantic reason.

mandatory manifest field          NO
    breaks any project that never had an upstream. A project-native
    origin is a legitimate permanent state under PSMF, not a
    transitional one.

optional manifest field           workable but wasteful
    duplicates one project-level fact across eight manifests. The
    project already holds "one home per fact" as a principle; this
    would violate it for no gain.

project-level origin record       PREFERRED
    one carrier, one fact, resolvable at reconstruction time, and it
    is where the divergence state and upgrade history already need
    to live anyway
```

Local `GIT_BLOB_BYTES_AT_COMMIT` binding is preserved unchanged under PSMF. That is the whole point of materialization.

## 10. Q10 — contracts-as-data as the first PSMF wave

**Yes, fully compatible, and this is a better synthesis than my Message 001 framing.** I presented T-E as a competing alternative topology; it is more accurately the *first materialization wave* of PSMF. No incompatibility exists:

```text
schemas are already data, already versioned, already vendored by default
they satisfy project-verifiable execution provenance trivially — they
    are inputs, not generators
they can be materialized with an origin record before any mechanism is
    extracted
a second project implementing independently against the same contracts
    is the strongest available N=2 evidence for the mechanism claim
```

The one thing wave one must get right, which Research 237 §5.5 flags and neither candidate resolves: **schema `$id` namespace ownership.** All nine schemas are under `https://schemas.ads.local/project-knowledge/`, which identifies an ADS-local realization. If schemas become the first generic artifact, that namespace must be decided — framework-owned, project-parameterized, or dual. I would put this in wave one's scope explicitly, because it is cheap now and a migration later.

## 11. Q11 — falsifiers for PSMF itself

```text
PSMF-F1  CONFIGURABILITY EXPLOSION
    Express ADS plus one materially different project shape purely
    through instance policy. Record the knob count and the number of
    conditional branches inside generic mechanisms that exist only to
    serve one of the two. If generic code needs meaningful
    project-conditional behavior, the boundary is wrong and
    project-native-only wins.

PSMF-F2  CORE EDIT PRESSURE
    With divergence detection live, observe whether ordinary ADS work
    requires editing the materialized core. Message 002 §13 already
    names this; I would add that the threshold should be set *before*
    observation, not after, so it cannot be rationalized.

PSMF-F3  UPGRADE RECONCILIATION COST
    Import one real upstream release across one real local divergence.
    If the AO-4 semantic reconciliation load per upgrade approaches the
    cost of simply re-deriving the change locally, the upstream is not
    paying for itself.

PSMF-F4  LIFECYCLE COUPLING (the decisive one)
    PSMF's entire N=1 justification is that mechanism and project have
    independent lifecycle pressures. If, over a measured window, ADS's
    own changes routinely span both layers, that claim is false and
    the separation has no basis. See §13 — this is measurable now,
    from history the repository already has.
```

## 12. Strongest remaining criticism of PSMF

Not synchronization complexity — Message 002 §13 already names that and the §6 subtree flow bounds it adequately.

**The strongest remaining criticism is that PSMF's justification and PSMF's evidence gate are pointed at different things.**

The justification (Message 002 §6, D2, D3) is *lifecycle independence and ownership*: mechanism and project change for different reasons, so they should have different canonical homes, and ADS should not become accidental upstream.

The evidence gate (Message 002 §7, §12) is *transferability*: a second project tests whether mechanisms work elsewhere.

Those are not the same claim. A mechanism can be perfectly transferable and still have a lifecycle entirely welded to ADS's, in which case a separate upstream buys nothing but coordination cost. Conversely a mechanism could have genuinely independent lifecycle pressure and still be non-transferable, in which case the separation is justified but the *reuse* framing is wrong.

Message 002 gates on transferability and then claims the benefit of lifecycle independence. The gate does not test the claim. That is the gap, and §13 is my proposed fix.

## 13. The measurement neither of us proposed

PSMF's central N=1 argument is empirically checkable from evidence the repository already holds, before any extraction and at low cost.

```text
sample a bounded window of recent substantive changes — the AO program
and W0-W5 waves give several hundred commits and ~570 checkpoints

classify each change by which layer it touched:
    MECHANISM_ONLY        tools/ + schemas/ generic modules
    INSTANCE_POLICY_ONLY  discovery values, subjects, view enablement
    KNOWLEDGE_ONLY        docs/** substantive content
    SPANS_LAYERS          any combination

then read the distribution:

    if MECHANISM_ONLY is a substantial, recurring share
        -> lifecycle independence is real
        -> PSMF's justification holds on ADS's own evidence, at N=1

    if SPANS_LAYERS dominates
        -> mechanism and project co-evolve
        -> a separate upstream would have been conflicted on most
           changes, and PSMF's core argument is falsified before
           any extraction cost is paid
```

This is cheap, uses no hypothetical second project, and tests the *actual* claim rather than a proxy for it. I would make it a required gate before step 5 of §8's sequencing, and I would want the threshold stated before the measurement is run.

I should be explicit about my own uncertainty: **I do not know which way this comes out.** My intuition from reading the W0–W5 history is that SPANS_LAYERS is common — the C1 implementation-closure work, the subject-catalog work and the compatibility shadow all touched mechanism and policy together — but intuition from reading is exactly what this project has repeatedly shown to be unreliable, and it is why the measurement is worth running rather than arguing about.

## 14. Strongest criticism of my own T-A preference, after seeing PSMF

Three, in descending force.

**My flag answered the wrong question.** `GENERIC_REUSABLE_LAYER_JUSTIFIED: NO` conflated target with timing. A reader taking my Message 001 flags at face value would have concluded I opposed a generic layer in principle, which my own §15 contradicts. That is an output defect, not a difference of judgment.

**I underweighted the accidental-upstream failure.** My Message 001 treated the cost of deferral as "reversibility premium grows over time." The sharper cost is that deferral does not preserve a neutral state — it makes ADS the default upstream the moment a second project exists, with no governance. Message 002 §6 is right about this and I did not see it.

**My §17 "largely independent" claim was too strong.** §7 above shows the instance-policy layer genuinely splits across Research 177 and Research 218 scope, which is a real coupling between residency and hierarchy that I missed because I was reasoning about carrier placement rather than layer ownership.

What I would still defend from Message 001: the §2 constraint (Message 002 accepts it), the N=1 caution about mechanism extraction (Message 002 accepts it), the three-layer genericity split (Message 002 largely adopts it), and the wet-lab finding that authority/evolution mechanics transfer better than knowledge organization (Message 002 §12 explicitly agrees and draws the right conclusion — a narrower generic core).

## 15. Convergence and remaining disagreement

Convergence is now nearly total. Both designs independently arrived at: complete local materialization, zero runtime dependency, project-local authority, explicit and optional upgrades, permitted divergence, no hidden global authority, ADS-specific migration adapters, a half-built mechanism/policy seam, knowledge organization being more ADS-shaped than authority mechanics, and contracts being extractable earlier than mechanisms.

On Message 002's six stated disagreements:

```text
D1  PARTLY ACCEPT — my claim was already scoped to T-C/T-D; but
    ChatGPT's "project-verifiable execution provenance" formulation
    is better than mine and I adopt it

D2  ACCEPT — this was my A/C conflation; corrected in §2

D3  ACCEPT — and §2 above strengthens it beyond what Message 002 argues

D4  ACCEPT, NARROWED — §7; the impact is the instance-policy home,
    not the whole hierarchy, because 218's tree is docs-only

D5  ACCEPT, COMPRESSED — §8; conceptual residency first, but step 2
    is one question rather than a role-freeze exercise

D6  ACCEPT — §10; contracts-as-data is wave one, not a competitor
```

Remaining disagreement, now small:

```text
R1  The evidence gate does not test the justification (§12), and the
    lifecycle-independence claim should be measured from existing
    history before extraction is designed (§13).

R2  No physical home for a materialized framework should enter the
    Research 218 tree until a framework exists (§7).

R3  Sequencing step 2 should be scoped to the instance-policy home
    rather than a general role freeze (§8).
```

None of these blocks reconciliation. All three are conditions on how PSMF is realized, not objections to selecting it.

## 16. On the stacked-transition point

Message 002 §16 is right that W5-F0 and AO-10 are held rather than running, and that this is serialization rather than three concurrent migrations. I accept the correction.

I would note one thing that is not a disagreement but should be on the record: PKIA-E01 was interposed to unblock AO-10 and W5-F0, and Message 002 §15's sequencing makes its resolution require residency → role freeze → hierarchy redesign → extraction design. That is a materially longer critical path than "reconsider the hierarchy," which is what Checkpoint 566 interposed. The §8 compression is my attempt to keep that path honest. Scope growth in an interposed correction is worth naming even when each step is individually justified.

## 17. Impact summary

```text
RESEARCH 177    MATERIAL CHANGE RECOMMENDED — prospective CLARIFY.
                177 already stated that later extraction into a
                standalone package remained possible if another project
                needed the tooling. PSMF does not contradict it; it
                names the relationship 177 left open. The clarification
                is that repository-local *materialization* is permanent
                while canonical *authorship* may move.

RESEARCH 218    MATERIAL CHANGE RECOMMENDED — narrow. One addition:
                a decided home for the instance-policy layer, which
                today splits across 218's navigation area and 177's
                tools area (§7). No framework directory. No change to
                placement precedence, naming, granularity, item
                carriers or subject contracts.

SPEC 028        NO MATERIAL CHANGE RECOMMENDED NOW. PSMF satisfies
                §19 unchanged, as Message 002 §5 correctly argues.
                Later additions for origin/lineage, materialization and
                upgrade import are likely, but they are additive
                contracts for a later realization, not corrections to
                the current one. I would reconsider only if the
                hash_basis const needs to become a parameterized
                vocabulary for a non-Git substrate, which is not in
                scope.
```

## 18. Evidence and qualification gates before extraction

```text
G1  lifecycle-independence measurement passes a pre-stated threshold
    (§13) — this is the gate PSMF's own justification requires and
    currently lacks

G2  instance-policy home decided and Research 218 reconciled (§7)

G3  generic core defined at the §4 boundary, with every ADS path,
    subject, fixture and compatibility assumption removed from it

G4  generic fixture suite exists containing no ADS content

G5  configurability tripwire threshold stated in advance, then
    measured against one non-ADS project shape (PSMF-F1)

G6  divergence detection implemented and observed on ADS before any
    upstream exists — it is useful on its own and it is the
    instrument PSMF-F2 needs

G7  schema namespace ownership decided (§10)

G8  one rehearsed materialization back into ADS producing byte-identical
    governed views — the Message 002 §17 equivalence step
```

G1, G3 and G8 are the load-bearing ones. G1 because it tests the justification; G3 because it is the actual work; G8 because it proves materialization preserves provenance before anything depends on it.

## 19. Answers to Q12 and final position

Target topology: **PROJECT_SOVEREIGN_MATERIALIZED_FRAMEWORK.**

Externalization timing: **after a genericity qualification prototype** — specifically after G1–G8, with G1 having the power to send the decision back to project-native-only if lifecycle independence turns out to be false.

That is not "after a real second project." I have moved on this: a scratch project shape plus the §13 measurement is sufficient to justify *building* the generic source at SUPPORTED_GENERIC level. A real second project remains required only to declare anything STABLE_GENERIC_CONTRACT (§3).

```text
COMPARATIVE_PKIA_REVIEW_COMPLETE: YES
PREFERRED_TOPOLOGY: PROJECT_SOVEREIGN_MATERIALIZED_FRAMEWORK
PROJECT_SELF_CONTAINMENT_REQUIRED: YES
GENERIC_UPSTREAM_JUSTIFIED_IN_TARGET_ARCHITECTURE: YES
MECHANISM_EXTRACTION_JUSTIFIED_NOW: NO
RESIDENCY_DECISION_SHOULD_PRECEDE_FINAL_INTERNAL_HIERARCHY: YES
MATERIAL_RESEARCH177_CHANGE_RECOMMENDED: YES
MATERIAL_RESEARCH218_CHANGE_RECOMMENDED: YES
MATERIAL_SPECIFICATION028_CHANGE_RECOMMENDED: NO
PKIA_E01_READY_FOR_CHATGPT_RECONCILIATION: YES

MC0022=ACTIVE
PHASE=CLAUDE_COMPARATIVE_RESIDENCY_REVIEW
INDEPENDENT_MESSAGE_001=FROZEN
CHATGPT_CANDIDATE=PROJECT_SOVEREIGN_MATERIALIZED_FRAMEWORK
CLAUDE_COMPARATIVE_POSITION=PSMF_ACCEPTED_WITH_G1_LIFECYCLE_MEASUREMENT_GATE
NEXT=CHATGPT_RECONCILIATION
```

`GENERIC_UPSTREAM_JUSTIFIED_IN_TARGET_ARCHITECTURE: YES` is stated conditionally in prose and cannot be in the flag: it is justified *as a target* on the accidental-upstream argument alone, which holds at N=1. The lifecycle-independence argument, which is PSMF's stronger justification, remains unmeasured, and G1 should be able to revoke it.
