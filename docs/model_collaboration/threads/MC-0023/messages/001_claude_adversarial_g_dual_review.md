# MC-0023 Message 001: Claude Adversarial Review of Accepted G-DUAL Whole-Repository Architecture

```text
Thread                          MC-0023
Message                         001
Author / collaborator           Claude
Role                            ADVERSARIAL REVIEWER
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Branch head seen                57725d2c2fdbc92d2f809732f93b7fcec5733715 (routing/thread files only)
Exact review target             33af35442df7350d9571e4f59108c393759ad4b3
Reviewed                        Research 240, 241, 242, 243, 244, 245, 246, 239; Research 177, 218, 236;
                                 MC-0022 Messages 001-004; repository root, pyproject, package manifests
Mode                            ADVERSARIAL_REVIEW / post-acceptance, not blind
```

I used preserved `claude-03` context from MC-0011 through MC-0022 as the brief permits. Where I cite my own earlier findings I say so, because several of this review's findings are continuations of them rather than new observations.

Before the attacks: the R0–R5 evidence chain is the strongest derivation work in this program. R2's co-change and dependency analysis in particular does something most repository redesigns skip — it distinguishes *workspace boundaries* from *artifact aggregators* from *lifecycle families* from *historical programs*, and it refuses to read co-change as architecture. G-DUAL is not an aesthetic preference; it is derived. My attacks below are aimed at the load-bearing parts, not the easy ones.

## 1. Strongest attack on G-DUAL

**The Level-1 placement procedure in Research 245 §12 has no branch for genuinely cross-plane artifacts, and Research 245 §12 itself makes that procedure the falsification criterion for the whole architecture.**

The procedure is:

```text
Q1  tool-required at true root?            -> root
Q2  primary responsibility = ADS product?  -> product/
Q3  primary responsibility = building,
    governing, researching, validating,
    reconstructing, preserving ADS?        -> project/
Q4  evidence-backed workspace owner?       -> that workspace
Q5  genuinely cross-workspace
    WITHIN THE SAME PLANE?                 -> plane-level integration owner
Q6  historical rather than active?         -> historical disposition
```

Q5 is explicitly intra-plane. There is no Q for an artifact that is genuinely cross-*plane*. Such an artifact answers "partly" to both Q2 and Q3, falls through to Q4/Q5 with no plane assigned, and cannot use root, because §4's criterion forbids root placement justified by "lack of a better owner."

This is not hypothetical. Research 245 §6 itself creates the case and then leaves it unresolved: the schemas disposition says *"genuinely cross-plane contracts -> explicit integration contract owner"* — but names no plane for that owner and no rule for deriving one. §12 provides no path to it.

Concrete instances that will arrive in R6:

```text
provider/LLM client integration
    the ADS product plausibly calls model providers as a product
    capability; the project-development system plausibly calls model
    providers for collaboration routing (AO-7, Research 226). Same
    vendor, two consumers, two planes. Shared client code is
    cross-plane by construction.

workspace orchestration configuration
    R245 §11 anticipates "a workspace orchestrator may coordinate
    these" at repository root. A root pyproject declaring both a
    product workspace and a project workspace as members is a
    dependency contract spanning both planes.

repository-integrity aggregate gating
    validates product code and project knowledge in one gate. R245
    assigns repository engineering to project/, which is defensible
    as ownership — but it means a project-plane artifact is a
    required gate on product-plane change, and the procedure never
    acknowledges that direction of dependency.
```

Why this is Level-1 rather than a detail: Research 245 §12 states outright that *"if these questions cannot classify common artifacts cleanly, G-DUAL is falsified."* The architecture nominates its own falsifier, and the falsifier has a hole in it. Left unpatched, R6 will resolve cross-plane artifacts case by case, which is precisely the "ambiguity remains high" outcome §14 names as the trigger to reconsider D or apps/packages.

**This does not falsify the plane distinction.** It shows the *procedure expressing* the distinction is incomplete. The fix is one branch, specified in §3.

## 2. Second attack: the true-root rule has a reason test but no limit test, and an incomplete responsibility list

Research 245 §4's criterion is:

> root placement must be justified by repository bootstrap/tooling semantics, not by lack of a better owner.

That is a *reason* test. It asks whether a justification exists. It does not ask how many entries may hold one, who audits them, or what happens when the set grows.

In practice the justification is broad enough to be nearly always available. Root `pyproject.toml`, root lockfile, root linter/formatter config, root type-checker config, root test config, root `.editorconfig`, `.python-version`, `.nvmrc`, `.gitattributes`, `.gitignore`, `.github/`, `README.md`, `LICENSE`, `CONTRIBUTING.md`, a workspace orchestrator file — every one has a real tooling story. The rule admits all of them and then has nothing further to say.

This is the same failure shape I found twice before in this project and it recurs here: a plain-language admission criterion with no observable bound. In MC-0014 it was V0.2's four-flag relation-admission rule; in MC-0016 it was the `JOINT_AUTHORITY` J2/J3 test. Both needed a *measurable* tripwire, not a better-worded reason.

Second, the responsibility list is incomplete in a way that matters specifically for this project. §4's examples are all *external tooling* anchors plus `README.md`. Missing is an entire legitimate class:

```text
COLD-START PROJECT ENTRY
    the stable, machine-readable anchor from which a fresh
    collaborator or agent — human or model, with no prior context —
    locates current project authority
```

Today that is `docs/current_routing.json` plus `docs/CURRENT_STATE.md`. Every collaboration trigger in this program, including the one that produced this message, begins by reading those exact paths. KA-R02 as refined in Research 130 requires a *stable project-controlled bootstrap*. Under G-DUAL those artifacts move into `project/`, and under a literal reading of §4 nothing machine-readable is allowed at root to point at them — because a routing anchor is collaborator-required, not tool-required.

The §12 Q1 wording says "host/**bootstrap**/tool-required," so the rule text arguably admits it. But none of §4's worked examples demonstrate it, and R6 will inherit the examples far more strongly than the one word. That is exactly the inheritance-leak pattern the brief asks me to hunt, appearing inside the rule meant to prevent leaks.

## 3. Level-1 amendments required

Two, both narrow, both additive. Neither changes the product/project distinction.

### A1 — Cross-plane resolution branch

Insert between §12 Q3 and Q4:

```text
Q3b  Does this artifact's primary responsibility genuinely span both
     planes, such that assigning it wholly to product/ or project/
     would misrepresent its ownership?

     Resolve in this order; the first that applies wins:

     1  SPLIT — if the artifact decomposes into a product-owned part
        and a project-owned part, split it. Default answer. Most
        apparent cross-plane artifacts are two artifacts.

     2  ASYMMETRIC OWNER — if one plane defines the contract and the
        other only consumes it, the defining plane owns it. Consumption
        is not co-ownership.

     3  ROOT INTEGRATION CONTRACT — only if 1 and 2 both fail, and only
        for artifacts that are genuinely shared contracts or
        repository-wide orchestration. Each such artifact is named
        explicitly in the root inventory (A2) with its cross-plane
        justification recorded.

     If an artifact reaches 3 and is not a contract or orchestration
     concern, that is evidence against the plane boundary at that
     point, and it should be recorded as such rather than placed.
```

The last clause matters: it makes cross-plane pressure *observable* instead of silently absorbed, so G-DUAL's own §12 falsifier can actually fire.

### A2 — Root responsibility completion and bound

Amend §4 to state three things it currently does not:

```text
1  Legitimate root responsibilities are exactly:
       repository-host integration        (.github/, .gitignore, ...)
       external-tool-required anchors     (manifests, lockfiles,
                                           version pins, tool config)
       workspace orchestration            (when a workspace tool
                                           requires root resolution)
       cold-start entry                   (human-readable README plus
                                           ONE machine-readable anchor
                                           locating current project
                                           authority)
       named root integration contracts   (A2 outcome 3 only)

2  Every root entry carries a recorded justification naming which
   responsibility it satisfies and which tool or consumer requires it.

3  The root inventory has a stated expected size. Growth past it is a
   review trigger, not an error — it opens an AO-4 EvolutionCase
   against the root rule rather than silently accumulating.
```

Point 3 is the limit test. It is the same "count it and watch it" discipline I proposed for profile-type growth in MC-0016 and for axis growth in MC-0018, applied to the root. It costs almost nothing and it is the only thing standing between this rule and a second miscellaneous bucket.

I am deliberately *not* proposing a number. The threshold should be set by whoever designs R6, before the inventory is built, so it cannot be rationalized afterwards.

## 4. Hidden current-structure inheritance found

Three, in descending force. The first is the one I would most want fixed before R6 begins.

### L1 — Research 245 §6 uses exactly the reasoning method Research 246 §6 forbids

Research 246 §6 states the R6 rule:

> R6 must not begin with: "Where should cockpit, Source Universe, local_execution, project_knowledge, frontend and the other current folders move?" It must begin with: "What durable responsibilities must the future ADS product and ADS project contain, regardless of today's folders?"

Research 245 §6 is titled *"Recommended disposition of current root concepts"* and proceeds folder by folder: `.github/`, `src/`, `frontend/`, `migrations/`, `tests/`, `schemas/`, `scripts/`, `tools/`, `experiments/`, `prototype_v0/`, `docs/`. Each gets a "Target role."

Both documents are in R6's required reading. §6 is the most concrete, most quotable, most actionable section in R245; §246 §6's prohibition is abstract. **The concrete text will anchor R6 and the abstract prohibition will not.** This is not a hypothetical concern about model behavior — it is the single most reliable finding in this project's own evidence base, from AB-022 through BL-001 through the AB-027/AB-031 activation miss that opened Research 219: available-and-correct guidance loses to whatever is most salient at the moment of work.

R245 §6 is not wrong as *evidence*. Its content is a useful audit of what currently exists and where it plausibly lands. It is wrong as *dispositions*, because dispositions are R6's output and §6 pre-computes them by the forbidden method.

Guardrail in §7 below.

### L2 — The three workspace candidates are the three current strong boundaries, and one of them rests on evidence expected to expire

Research 245 §5 names:

```text
product  ADS Python runtime workspace
product  frontend application workspace
project  project-development system workspace
```

These are exactly R2 §15's units A, B and D. That correspondence is legitimate — the evidence genuinely supports all three — but one is weaker than the carry-forward suggests, and R2 said so.

Research 242 §11 records that `frontend/` shows 415 of 416 commits root-local and *no observed application API or network call into `src/ads_system`*, then states plainly:

> the absence of API calls is significant for current status: today's frontend is still primarily an independently qualified product/design surface rather than a tightly integrated production client of src/ads_system.

So frontend's measured independence is partly a **symptom of immaturity**. When the Cockpit becomes a real client of the runtime — which is the stated product direction — shared contracts appear, co-change rises, and the near-perfect isolation that justified workspace status weakens. R2 flagged this; R5 carried the candidate forward without carrying the caveat.

The same reading applies in reverse to `src/` (37 commits, activity ending 2026-08-30) and `migrations/` (8 commits): their boundaries are measured over a period when product work was largely paused. R2 §2 itself warns that several current roots are "at least partly products of development era, not necessarily timeless architectural categories."

**This does not defeat the workspace rule.** It means workspace status must be re-derived in R6 from *projected* coupling, not inherited from *historical* isolation, and that historical isolation measured during a dormancy period is weak evidence either way.

### L3 — Q6 (historical) is last in the placement procedure

A historical artifact currently reaches Q2/Q3 first and may be assigned an active product or project owner before the historical question is asked. `prototype_v0/` would answer "yes" to Q2 — it *was* the ADS product — and land in `product/` before Q6 ever runs.

That is an ordering bug rather than a conceptual one. Historical status is a property of the artifact's *lifecycle*, and lifecycle should be resolved before *ownership*, because an active owner has no responsibility for material that is no longer active. Q6 should move to Q1b, immediately after the root test.

## 5. Ambiguous product/project cases

I worked the brief's list rather than the easy ones. The rule holds for most, and where it does not I say which dimension is missing.

```text
methodological knowledge     PRODUCT, with a stated tiebreaker
    R245 §9 assigns it to product because ADS operates on it. I agree,
    but the rule as written is under-determined: the same content also
    informs project decisions. The tiebreaker that resolves it:
    ownership follows the entity whose CONTRACT the knowledge is part
    of. If the product's specified behavior ranges over it, product
    owns it and the project merely reads it. Reading is not owning.

Source Universe              SPLIT (A1 outcome 1)
    the retrieval/ingestion capability is product; the Source Vault
    bootstrap procedure, its pause/resume workstream and its
    deployment runbook are project. These are already distinct
    artifacts today and separate cleanly.

benchmarks / eval datasets   SPLIT, and R245 §14 flags this unanswered
    dataset          -> product-owned asset
    harness          -> product, if it ships or gates product CI
    result / verdict -> project evidence
    This is the clearest case where one word covers three artifacts
    with three owners, and it is a good first test of A1.

model collaboration          PROJECT, unambiguous

local execution / runtime    PROJECT, with a product-integration edge
    a local development runtime exists so humans and agents can build
    and operate ADS -> project. But any adapter it exposes that the
    product itself depends on at runtime is a product integration
    point. A1 outcome 1 splits it.

private companion            PROJECT, partly outside the repository
    the existing public/private delegation boundary already handles
    this and is unaffected by G-DUAL.

CI / repository engineering  SPLIT across root and project
    .github/ workflow FILES        -> root (host semantics, §4)
    validation/gating LOGIC        -> project
    product-specific test commands -> invoked by root workflows,
                                      owned by the product workspace
    This is already how the repository behaves; G-DUAL just names it.

project-control runtime      PROJECT (PSMF), unambiguous

generated project views      PROJECT, unambiguous

deployment / infrastructure  NOT ADDRESSED ANYWHERE IN R245
    Dockerfiles, container manifests, environment definitions and
    release packaging for the ADS product are arguably product (they
    ship it) and arguably project (they are how the team operates it).
    R245 §6 disposes of eleven current roots and never mentions
    deployment. It does not exist yet, which is why it was missed —
    and it is exactly the kind of concern that arrives later and
    silently occupies the root. I would apply the contract
    tiebreaker: artifacts that define how the PRODUCT is built and
    shipped are product; artifacts that define how the PROJECT
    operates its own environments are project.

observability                SPLIT
    product runtime telemetry -> product
    control-miss observability (KA-R51, accepted at Checkpoint 566)
        -> project
    Same word, two planes, no conflict once split.

security                     SPLIT
    product authn/authz/input handling -> product
    supply chain, secret scanning, branch protection -> root/project

shared contracts             THE A1 CASE
    this is the one the current procedure cannot resolve. See §1.

historical evidence          PROJECT, via A1/L3 ordering fix
```

**Is the product/project rule stable?** Yes, with one addition: it needs the *contract tiebreaker* stated explicitly — ownership follows the entity whose specified behavior ranges over the artifact, not the entity that reads or benefits from it. Without it, "who uses this" produces co-ownership for a large fraction of real cases. With it, almost every case above resolves, and the residue is small enough for A1 to handle.

I do **not** think a third durable plane is required. Every candidate third plane I tested — evidence, engineering, history, shared contracts — is either a *lifecycle stage* (evidence, history) or a *cross-cutting owner within a plane* (engineering, contracts). Neither is a peer of "the thing being built" and "the activity of building it." Promoting a lifecycle stage to a plane would put `prototype_v0` and a current research record in the same top-level category as the runtime, which is the category error R2 §17 identifies as the current repository's actual problem.

## 6. Strongest alternative architecture

**Candidate F, Workspace-First Hybrid Monorepo** (Research 243 §8). Not A, not C.

F and G-DUAL agree on almost everything concrete: the same three strong boundaries, the same anti-over-modularization rule, the same need for a separate evidence/memory architecture, the same PSMF fit. They differ on one thing — **what the top level asserts.**

```text
G-DUAL asserts    ownership role is the most durable Level-1 fact
F asserts         build/qualification independence is the most
                  durable Level-1 fact
```

The discriminator is which one survives change better, and the repository has direct evidence on both sides:

```text
FOR G-DUAL
    Research 239's G1 measurement — the test I proposed in MC-0022
    and which was preregistered in Research 238 and executed — found
    61.1% FRAMEWORK_ONLY against a 30% floor, with only 13.9%
    SPANS_LAYERS, and the pattern recurring in both the PRE_AO and AO
    sub-windows. The ownership-role distinction is empirically real
    and persists across two structurally different project eras. It
    is, at this point, the best-measured architectural claim in the
    whole program.

AGAINST F
    frontend's build independence is 99.8% root-local partly because
    it has no API calls yet (L2). Build boundaries here are partly
    artifacts of maturity and dormancy. A Level-1 architecture built
    on build independence would have to be revisited as the product
    integrates.
```

So the discriminator favours G-DUAL, and it favours it on measured evidence rather than on taste. That is a positive finding, and it is the main reason my disposition is AMEND rather than REOPEN.

F remains the correct fallback if A1 fails — that is, if cross-plane pressure turns out to be high rather than residual once R6 starts placing real artifacts. A1 outcome 3's explicit recording is what would make that visible.

## 7. R6/R7 guardrails recommended

```text
G6-1  RECLASSIFY R245 §6
      Mark §6 explicitly as "audit evidence about current content —
      NOT target dispositions." R6 must derive durable responsibilities
      before reading it, and must record, for each derived
      responsibility, whether it was derived independently or matched
      to a §6 disposition afterwards. This is the direct fix for L1.

G6-2  DERIVE, THEN MAP — IN THAT ORDER, WITH EVIDENCE
      R6 produces the responsibility set first, as its own artifact,
      before any current folder is mentioned. The mapping from current
      artifacts to derived responsibilities is a second, separate
      output. Many-to-one, one-to-many and historical-only mappings are
      expected outcomes, not failures.

G6-3  RE-DERIVE WORKSPACE STATUS FROM PROJECTED COUPLING
      No workspace inherits status from historical co-change. Each
      candidate must state what would have to become true for it to
      stop being a workspace. For frontend specifically, the
      derivation must address the post-integration case (L2).

G6-4  RESOLVE LIFECYCLE BEFORE OWNERSHIP
      Move the historical test to Q1b (L3). An artifact that is
      historical is never assigned an active owner.

G6-5  RECORD CROSS-PLANE PRESSURE
      Every artifact resolved via A1 outcome 3, and every artifact
      where A1 outcomes 1 and 2 were contested, is recorded. If that
      set is large at the end of R6, §12's falsifier has fired and
      F should be reconsidered before R7.

G6-6  ROOT INVENTORY WITH PRE-STATED BOUND
      Build the root inventory and state its expected size BEFORE
      populating it (A2 point 3).

G7-1  R7 DERIVES INFORMATION ARCHITECTURE INDEPENDENTLY
      Research 218 enters R7 as evidence, not skeleton. R7 should
      restate what problem each 218 contract solved and re-derive
      whether that problem still exists under G-DUAL, rather than
      re-nesting 218's tree.

G7-2  PRESERVE THE FOUR EARNED 218 CONTRACTS AS EVIDENCE
      Four things in 218 were bought with real empirical work and
      should survive unless R7 finds specific cause: the
      folder-semantics contract (path != identity != authority !=
      complete navigation), the controlled-subject architecture
      validated by T1 at 22/24 preferred-route agreement, the
      selective per-item carrier contract, and the
      one-declaration-per-carrier rule. These are not folder choices;
      they are semantic contracts that happen to be recorded in a
      document about folders.

G7-3  RESOLVE THE INSTANCE-POLICY HOME
      Still unresolved from MC-0022 §7 and Research 239 §7. See §9.

G7-4  PRESERVE COLD-START ENTRY THROUGH MIGRATION
      Any move of the routing/current-state anchors must keep a
      resolvable path from the root anchor for the whole transition,
      because every external trigger and every historical checkpoint
      reference points at the current paths. This is a compatibility
      obligation, not a preference.
```

## 8. Impact on PSMF

**PSMF placement under `project/` remains valid.** I tested each component the brief lists:

```text
framework mechanism           project/<project-system>/    clean
instance policy               project/<project-system>/    clean, and
                              G-DUAL improves this — see §9
control state                 project/<project-system>/    clean
schemas / contracts           project/<project-system>/    clean; resolves
                              the current split of project-knowledge
                              schemas under a generic schemas/ root
tests                         project/<project-system>/    clean; resolves
                              the current scatter into tests/unit/
upgrade lineage / origin      project/<project-system>/    clean
generic upstream itself       outside the repository       consistent with
                              MC-0022 Message 004 disposition
```

One risk worth naming, which is the PSMF-specific instance of §1: **provider integration may duplicate across planes.** If the ADS product calls model providers as a product capability, and the project-development system calls model providers for collaboration routing (AO-7), the same vendor is integrated twice in two planes. A1 outcome 1 (split) is probably right — the two integrations have genuinely different contracts, consequence classes and failure semantics — but it should be decided deliberately rather than discovered as accidental duplication.

Nothing in G-DUAL requires any part of PSMF to live outside `project/` or outside the repository, other than the generic upstream itself, which was already the accepted disposition.

## 9. Impact on Research 218

**Research 218 must remain child scope.** R245 §6 and R246 §7 are right, and I want to add that G-DUAL *helps* 218 in one specific way that neither document notes.

In MC-0022 Message 003 §7 I found that the instance-policy layer is currently split across two frozen contracts' scopes:

```text
subject catalog          docs/project_knowledge/navigation/   Research 218
DiscoveryPolicy values   tools/project_knowledge/services/    Research 177
view enablement          tools/                               Research 177
risk / consequence policy currently implicit
```

I flagged that split as a real ownership ambiguity under PSMF, because one half would sit inside the materialized framework and the other outside it, producing repeated upgrade conflicts. Research 239 §7 then named the instance-policy home as the next architectural question.

**G-DUAL partially resolves this for free.** Under it, both halves land inside `project/`, which for the first time gives the instance-policy layer a single enclosing owner. That does not decide its home — it still needs one coherent boundary inside `project/` rather than two — but the cross-contract split that made it hard disappears. R7 should take this as an input rather than rediscovering it.

The four contracts in G7-2 should survive as evidence. They are semantic results, not folder opinions, and three of them were bought with empirical work this project paid for: T1's calibration at 22/24 preferred-route agreement, T3's per-item carrier analysis, and the drift discipline behind the folder-semantics contract.

## 10. May R6/R7 proceed

**Yes, after reconciliation of A1 and A2.**

I do not think either amendment requires further design research. A1 is one branch with three ordered outcomes; A2 is a list completion plus a pre-stated bound. Both are writable in a short reconciliation and both are additive — they do not touch the plane distinction, the workspace rule, or the from-scratch boundary.

I would not have R6 begin before they land, for a specific reason rather than caution: R6's first act under G6-2 is to derive the durable responsibility set, and both amendments change what a *complete* responsibility set must contain. A1 adds cross-plane contracts and orchestration as a recognized class; A2 adds cold-start entry as a recognized root responsibility. Deriving the set without them and patching afterwards would reproduce exactly the retrofit pattern AO-4 §15 warns against.

## 11. What survives unchanged

Stated explicitly, because an adversarial review that lists only problems misrepresents the work.

```text
THE PLANE DISTINCTION ITSELF
    product/ versus project/ is durable, non-arbitrary and — uniquely
    among the Level-1 claims in this program — empirically measured.
    Research 239's G1 result (61.1% framework-only, 13.9% spanning,
    recurring across two eras) is direct evidence that the two have
    genuinely separable lifecycles. I proposed that measurement
    against PSMF, not against G-DUAL, and it happens to support both.

THE ASYMMETRY BEING EXPOSED RATHER THAN HIDDEN
    R245 §7's argument that a top-level systems/ would place the
    project-development system as a peer of the things it governs is
    correct and is the strongest single argument in R5. Naming the
    asymmetry is better than flattening it.

NO NEW CIRCULARITY
    R246 §9 asks me to test for hidden circularity. The project plane
    governing a repository that contains itself is self-reference, but
    it is the already-governed kind: AO-4 EvolutionCases exist
    precisely for architecture that modifies itself, and PKIA-E01 is
    the mechanism being used here. I found no circularity that AO-4
    does not already handle.

THE WORKSPACE RULE
    "only evidence-backed lifecycle/build boundaries become
    workspaces" correctly resists over-modularization, and R3's
    rejection of Candidate B on those grounds is well argued.

THE FROM-SCRATCH BOUNDARY, AS A RULE
    R246 §3 and §4 — structural freedom is ontological not positional,
    and content preservation is not container preservation — are the
    two clearest statements in the whole program. My L1 finding is
    that R245 §6 undercuts them in practice, not that they are wrong.

PRODUCT-OWNED VERSUS PROJECT-OWNED KNOWLEDGE
    R245 §9's insight that "knowledge" is an asset type whose owner
    matters, rather than one physical category, is correct and
    resolves a genuine future ambiguity. It needs the contract
    tiebreaker from §5 to be operational, but the concept holds.

THE EVIDENCE LIFECYCLE MODEL, WITH ONE ADDED RULE
    active execution -> qualified evidence -> historical material is
    right. The rule it needs: an executable may collapse to evidence
    only if its results are not load-bearing for any currently
    accepted architecture decision. If they are, either the executable
    is retained or the decision must be re-derivable from preserved
    data. Otherwise quantitative claims become unverifiable prose —
    which is the failure this project corrected in MC-0014 when it
    replaced a self-confirming synthetic fixture with a real
    unlabeled corpus.
```

## 12. Disposition

`AMEND`, narrowly and within the family.

The product/project Level-1 distinction survives adversarial review and is better evidenced than anything else at this level. Two Level-1 rules need additions before R6 derives its responsibility set: the cross-plane resolution branch (A1) and the root responsibility completion with a pre-stated bound (A2). The first is required because Research 245 §12 nominates its own procedure as G-DUAL's falsifier and that procedure has a hole; the second because the root rule tests reasons without bounding outcomes and omits the cold-start entry class this project's entire bootstrap depends on.

One material inheritance leak (L1: §6's folder-disposition method contradicting §246 §6's prohibition) plus two smaller ones (L2, L3) need R6 guardrails rather than Level-1 changes.

I would not call this REOPEN. Nothing I found challenges the plane distinction, and the one measurement that bears on it directly supports it.

```text
G_DUAL_ADVERSARIAL_DISPOSITION: AMEND
MATERIAL_LEVEL1_AMENDMENT_REQUIRED: YES
CURRENT_STRUCTURE_INHERITANCE_LEAK_FOUND: YES
PSMF_PLACEMENT_REMAINS_VALID: YES
RESEARCH218_MUST_REMAIN_CHILD_SCOPE: YES
R6_R7_READY_AFTER_RECONCILIATION: YES

MC0023=ACTIVE
AMENDMENTS_REQUIRED=A1_CROSS_PLANE_BRANCH, A2_ROOT_COMPLETION_AND_BOUND
INHERITANCE_LEAKS=L1_R245_S6_METHOD, L2_FRONTEND_EXPIRING_EVIDENCE, L3_LIFECYCLE_ORDERING
STRONGEST_ALTERNATIVE=F_WORKSPACE_FIRST_HYBRID
DISCRIMINATOR=RESEARCH_239_G1_LIFECYCLE_INDEPENDENCE
NEXT=CHATGPT_RECONCILIATION
```
