# MC-0022 Message 001: Claude Independent Residency and Reuse Architecture

```text
Thread                          MC-0022
Message                         001
Author / collaborator           Claude
Role                            INDEPENDENT_REVIEWER / COUNTER_DESIGNER / ARCHITECT / CRITIC
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Branch head seen                89bc4037b71d924eae84cb3ce07f143774d7c890 (routing/thread files only)
Independent substantive base    c7252e182b6068954aca804fb064a10e37e298a4
Mode                            INDEPENDENT_THEN_COMPARATIVE / candidate-blind, history-allowed
Purpose                         Independently determine the natural residency, ownership, reuse and
                                 instantiation architecture of the project-development knowledge and
                                 control system, before ChatGPT freezes a topology recommendation
```

## 0. Independence statement

From the coordination branch I read only the five permitted files: `docs/current_routing.json`, `docs/model_collaboration/REVIEW_INBOX.md`, and MC-0022's `BRIEF.md`, `THREAD.md`, `STATE.json`.

All substantive evidence is bound to `c7252e182b6068954aca804fb064a10e37e298a4`: Research 218, Research 219, Research 223, `docs/project_knowledge/architecture/whole_architecture.md`, `tools/project_knowledge/services/discovery.py`, `tools/project_knowledge/views.py`, `tools/project_knowledge/capture.py`, `tools/project_knowledge/declaration.py`, `tools/project_knowledge/adapters/pure.py`, `schemas/project_knowledge/defs.v1.schema.json`, `schemas/project_knowledge/project_boundary.v1.schema.json`, and the repository root listing.

I did **not** read Research 236, Research 237, Checkpoint 567, `docs/CURRENT_STATE.md`, `docs/KNOWLEDGE_MAP.md`, or any descendant PKIA candidate synthesis, diff, commit listing or search result. No PKIA-E01 framing was exposed to me.

Preserved `claude-03` context from MC-0011 through MC-0018 is used as the brief permits and desires.

## 1. What is actually being architected (task A)

The current work is not one thing. It is three things that happen to share a repository, and the residency question is really the question of whether that sharing is essential or incidental.

```text
MECHANISM
    declaration parsing, schema validation, identity transitions,
    authority resolution, workstream DAG, capture/promotion lifecycle,
    view building with manifest/freshness binding, snapshot modes,
    and the AO-4 evolution-classification semantics

INSTANCE POLICY
    which profiles exist, which authority classes exist, which lifecycle
    states exist, which views are produced, where carriers live, what the
    discovery policy admits, what the subject vocabulary is

PROJECT KNOWLEDGE AND EVIDENCE
    the actual accepted meaning, history, decisions, workstreams and
    provenance of one project
```

There is a fourth thing that is easy to miss and matters a lot here:

```text
MIGRATION AND COMPATIBILITY ADAPTERS
    CURRENT_STATE.md / current_routing.json / KNOWLEDGE_MAP.md shadowing,
    legacy Knowledge Map routing evidence, the W0-W8 wave machinery
```

That fourth layer is **wholly ADS-specific and inherently temporary**. It exists because ADS had a prior continuity architecture to migrate from. A new project would have none of it. Any reuse reasoning that treats the current codebase as one undifferentiated "framework" will over-count its genericity by whatever fraction of it is migration scaffolding.

The natural ownership boundaries follow from the authority model rather than from the paths. KA-I01/KA-R19 make the repository the single project-development authority; Git-blob-bound revisions make the repository the provenance root; KA-R36 requires provider portability. Those three together say: **project knowledge and instance policy are owned by the project, unconditionally.** They say nothing yet about mechanism, which is the only genuinely open part of the question.

One observation the brief's framing invites but the repository already answers: ADS is *already* a two-tenant repository. `src/`, `frontend/`, `migrations/`, `experiments/` are the ADS product. `tools/project_knowledge/`, `schemas/project_knowledge/`, `docs/project_knowledge/` are the project-development method. Two unrelated subject matters, one repo, one lifecycle, separated by directory boundary and enforced import layering — and it works. That is a live, years-long instance of exactly the question being asked, and its answer so far is that a directory boundary plus enforced layering was sufficient and a repository boundary was not needed.

## 2. The decisive constraint I found (and did not expect)

Before proposing topologies, one finding constrains the space harder than any preference, and it comes from the implementation rather than the design prose.

Every persistent view's manifest binds its generator as:

```text
implementation_basis   GIT_BLOB_BYTES_AT_COMMIT
implementation_files   ordered repo-relative paths
implementation_digest  sha256 over path || 0x00 || git_blob_bytes || 0x00
```

`views.py::implementation_digest` requires exact Git bytes for every declared implementation path, and `validate_specifications` runs each through `validate_source_path`, whose pattern in `defs.v1.schema.json` forbids a leading `/` and forbids any `.` or `..` component. The paths are therefore necessarily **repository-relative and resolvable as Git blobs at the same commit**.

The consequence is structural, not stylistic:

```text
a generator that lives outside the project's Git tree cannot have its
implementation_digest computed at all

therefore no derived view could bind its own provenance

therefore the project could not prove that its own views correspond to
its own sources under its own contract
```

An installed package, a submodule pinned to a foreign lineage, or a hosted service all fail this. The already-frozen freshness contract in Specification 028 §19 does not merely *prefer* in-tree residency of mechanism code — it **requires** it for any project that produces governed derived views.

I want to be precise about the scope of that claim. It constrains where the *executed* mechanism must reside. It does not constrain where the mechanism is *authored*, *versioned upstream*, or *distributed from*. That distinction is exactly the one the brief asks not to collapse, and it turns out the repository has already answered half of it.

## 3. Topology space (task B)

I generated these from the ownership/authority constraints rather than from a menu. Six are worth stating; two of them are worth stating mainly so they can be ruled out on evidence rather than taste.

### T-A — Project-native, no generic source (status quo)

```text
generic design/code         none; ADS is the only artifact
inside a project            everything
external after creation     nothing
authority reconstruction    clone the repo; everything is present
offline/alone               yes, completely
version binding             n/a
upgrades                    ordinary development
divergence                  meaningless at N=1
rollback                    ordinary Git
project extensions          ordinary development
flow-back                   n/a
generic source disappears   n/a
```

### T-B — Vendored mechanism with recorded upstream lineage

Generic mechanism is authored in a separate upstream repository. Each project contains a **complete committed copy** in its own tree, recorded against an exact upstream revision and digest. Upgrades are explicit in-tree merges. Local divergence is permitted and recorded.

```text
generic design/code         upstream repo (authoring/distribution only)
inside a project            full materialized mechanism + instance policy
                            + knowledge + recorded upstream ref/digest
external after creation     nothing required
authority reconstruction    clone; nothing external consulted
offline/alone               yes
version binding             recorded upstream ref + content digest, in-tree
upgrades                    explicit governed in-tree merge, AO-4 classified
divergence                  first-class; local amendments are ordinary commits
rollback                    ordinary Git revert of the upgrade commit
project extensions          ordinary in-tree code; may or may not flow back
flow-back                   patch/PR upstream, project decides
generic source disappears   project entirely unaffected
```

This is the only topology with an upstream that survives §2's constraint, because the vendored files *are* project Git blobs.

### T-C — Framework as installed runtime dependency

```text
inside a project            sources, config, lockfile
external after creation     the package
offline/alone               only with a warm cache; not durably
authority reconstruction    depends on resolving an external artifact
version binding             lockfile
generic source disappears   project cannot validate or rebuild views
```

**Ruled out by §2**, not by preference: `implementation_digest` cannot be computed over site-packages paths under `GIT_BLOB_BYTES_AT_COMMIT`.

### T-D — Framework as hosted service / control plane

Fails offline reconstruction, fails KA-R36 portability, and places governing semantics behind an availability and vendor boundary. **Ruled out** on the authority model.

### T-E — Contracts-as-data reuse; implementation left to each project

The reusable artifact is the **specification set**, not the code: the profile schemas, Requirements V0.2, the Specification 028 contract semantics, and the AO-4 classification vocabulary. Each project vendors the schemas as data and implements or re-derives tooling against them.

```text
inside a project            vendored schemas + own implementation
external after creation     nothing required
offline/alone               yes
version binding             schema_version + vendored file digest
upgrades                    schema version bump; v1 never edited in place
divergence                  natural; a project may add profiles
generic source disappears   unaffected; schemas are already in-tree
```

Survives §2 trivially, because schemas are inputs, not generators.

### T-F — Pattern-only reuse

Publish the architecture as documented pattern and case study; each new project re-derives with AI assistance. No shared artifact at all.

```text
version binding             none
divergence                  total, by construction
generic source disappears   irrelevant
reuse value                 depends entirely on whether the *reasoning*
                            transfers better than the *code*
```

Weaker than it sounds. Most architecture genuinely propagates this way, and at N=1 it is the option that makes no unfalsifiable genericity claim.

### T-G — Split ADS into framework repo + project repo now

```text
offline/alone               yes for each, but the project needs the
                            framework materialized anyway (§2)
coordination cost           two lifecycles, two acceptance programs,
                            cross-repo provenance, cross-repo AO-4
reuse benefit at N=1        zero
```

This is the topology that most resembles professional practice and least survives the evidence. It pays the full coordination cost of separation while N=1 means there is nothing on the other side of the boundary to serve.

## 4. Challenging reuse itself (task C)

The brief asks not to assume reuse is valuable because mechanisms look generic. I want to answer this with the project's own hardest-won epistemic lesson rather than with intuition.

In MC-0014 I found that V0.2's relation-admission rule was near-circular: four hand-set boolean flags in a fixture, checked by a four-term boolean AND, reporting 0 false positives across 100 repetitions. The rule was validated against the only instance it was derived from. The project accepted that finding and rebuilt the discriminator against real unlabeled cases.

**Extracting a generic framework from ADS at N=1 is the same error at repository scale.** Every mechanism in the current tooling was derived from an ADS failure: AB-022's restart-order miss, KF-SD-03's dispatch miss, BL-001's task-contract fidelity failure, the 2026-09-20 AB-027/AB-031 activation miss. A framework extracted from that evidence is validated against exactly the corpus that produced it. It would look generic and be untested.

Splitting the current mechanisms honestly:

```text
LIKELY GENUINELY REUSABLE
    declaration parsing and strict carrier extraction
    schema-validated profile contracts (the *pattern*, not the set)
    selective semantic identity + identity transitions
    scope/relation-based authority resolution with fail-visible statuses
    workstream DAG, pause/resume, dependency closure
    capture -> review -> revision-bound promotion -> archival
    complete-input view building with manifest/freshness/digest binding
    COMMIT vs WORKTREE snapshot discipline
    AO-4 KEEP/CLARIFY/AMEND/SUPERSEDE/REOPEN evolution classification

GENERIC-SHAPED BUT INSTANCE-CONFIGURED
    the specific eight profiles
    the six authority classes and five lifecycle states
    the specific eight persistent views
    the DiscoveryPolicy instance
    the restricted pure-unit registry contents

ONLY LOOKS GENERIC BECAUSE ADS IS THE SOLE INSTANCE
    the 18-subject controlled catalog (Research 217/218) — wholly ADS
    the scope:* facet vocabulary — by construction an open namespace with
        no controlled meaning, as I established in MC-0018 C2
    the domain homes (cockpit, source_universe, local_execution, ...)
    the W0-W8 wave structure and compatibility shadowing
    the private-companion boundary
    `.ads-private` and the 19 hardcoded fixture roots in DiscoveryPolicy
```

What a second unrelated project would have to establish, to convert the first list from hypothesis to evidence:

```text
that its knowledge failures are the same *classes*, not merely that it
    also has knowledge problems
that the profile set needs extension rather than replacement
that authority resolution over scope facets is meaningful when its
    facets are drawn from an unrelated domain
that the capture/promotion lifecycle matches its actual authoring
    ergonomics rather than ADS's
that its subject vocabulary is expressible in the same shape with
    entirely different content
that the configuration effort is dominated by *policy*, not by editing
    mechanism code
```

That last one is the real test, and it is measurable.

## 5. Self-containment versus shared infrastructure (task D)

The brief is right that these collapse too easily. My answers differ per dimension, which is the point:

```text
SOURCE OWNERSHIP        shared upstream is acceptable (T-B/T-E)
RUNTIME DEPENDENCY      must be zero; forced by §2 and KA-R36
DISTRIBUTION MECHANISM  external is acceptable; it is not authority
PROJECT AUTHORITY       must be wholly in-project, always
BOOTSTRAP               must work from a bare clone with no network
UPGRADE CHANNEL         may be external, but must land as ordinary
                        in-tree commits subject to AO-4, never as
                        runtime resolution
PROVENANCE LINEAGE      may point upstream; must not depend on upstream
                        remaining reachable to be interpretable
```

The single sentence that captures it: **a project may have an upstream, but must never have a dependency.** Upstream is a source of patches; it is not a source of truth, not a source of validity, and not a source of availability.

## 6. Framework / instance / knowledge boundary (task E) and where ADS blurs it

The cleanest separation, and the current realization's conformance to it:

```text
MECHANISM
    tools/project_knowledge/{model,declaration,references,identity,
    authority,workstreams,views,capture}.py, adapters/, services/
    -> mostly clean; blurred where noted below

INSTANCE POLICY
    DiscoveryPolicy, profile set, view specifications, pure-unit
    registry, subject catalog
    -> partially expressed as policy, partially hardcoded

KNOWLEDGE / EVIDENCE
    docs/**
    -> clean

MIGRATION / COMPATIBILITY ADAPTERS
    services/compatibility.py, the W-wave machinery, legacy routing
    evidence
    -> cleanly separable by file, but not labeled as a distinct layer

PROVIDER / TOOL INTEGRATION
    -> essentially absent from the knowledge substrate, which is a
       genuine strength and consistent with KA-R36
```

**The concrete blur, with evidence.** The instance-policy seam exists in exactly one place and is missing everywhere else.

`services/discovery.py` defines `DiscoveryPolicy` as a frozen dataclass whose every ADS-specific value is a *default*: `production_roots=("docs",)`, nineteen hardcoded `docs/research/project_knowledge_*` fixture roots, `capture_root`/`generated_root`/`manifest_root` under `docs/project_knowledge/`, and `excluded_components` containing the literal `.ads-private`. That is a real framework/instance seam, correctly shaped — the mechanism is parameterized, the policy is an instance value.

`views.py` has no such seam. `GENERATED_ROOT = "docs/project_knowledge/generated/"` is a module constant. `PURE_UNIT_REGISTRY` hardcodes `tools/project_knowledge/pure_units.py` as a literal path in a data tuple. `source_inventory_specification()` hardcodes an implementation-closure list including `schemas/project_knowledge/*.schema.json` and the tool module paths themselves.

So: **the boundary is half-built and inconsistent.** Discovery is parameterized; generation is hardcoded. That is not a design position, it is an artifact of the order things were built.

Is the blur harmful today? Mostly no — at N=1, hardcoded paths are honest and cheaper than premature indirection. It becomes harmful in exactly one scenario: if extraction is ever attempted, this is the work, and it grows with every new view and pure unit added.

## 7. Evolution across many projects (task F)

The project has already built this and, I think, does not realize the AO-4 model *is* the multi-project evolution model.

```text
framework release            an upstream revision; nothing happens in a
                             project until someone merges it
project-local customization  ordinary in-tree commits; permanently allowed
breaking schema change       new schema version file; v1 never edited in
                             place, exactly as the current v1 discipline
                             already requires
security/correctness fix     an upstream patch; still merged explicitly
upgrade selection            per-project, per-commit; no global push
conflict resolution          ordinary Git merge, then AO-4 classification
                             of any semantic delta
intentional divergence       a first-class outcome, recorded as local
                             amendment; the project simply stops merging
                             the diverged region
contribution upstream        patch; upstream decides; neither side gains
                             authority over the other
framework retirement         no effect on any project; every project
                             already holds a complete working copy
```

The property I would insist on: **no hidden global authority.** An upstream must never be able to change a project's governing semantics by publishing. Under T-B that is structurally guaranteed, because an upgrade is a commit a human accepted in that project's repository, subject to the project's own AO-4 discipline. Under T-C it is not guaranteed at all — a lockfile bump can change validation semantics, which is an authority transition disguised as dependency management.

## 8. Disaster recovery and independence (task G)

Tested against each surviving topology:

```text
                              T-A    T-B    T-E    T-C
upstream repo unavailable     n/a    pass   pass   FAIL
framework abandoned           n/a    pass   pass   FAIL
clone to clean machine        pass   pass   pass   degraded
AI provider changes           pass   pass   pass   pass
runtime integration gone      pass   pass   pass   pass
untouched for years           pass   pass   pass   FAIL
```

T-A, T-B and T-E are equivalent on recovery, which is the point: **vendoring converts an availability dependency into a historical fact.** The upstream's disappearance costs future patches, not present function. T-C fails three of six, and the "untouched for years" row is the one that matters most for a project whose stated purpose includes surviving long gaps.

## 9. Preferred architecture (output 1)

**Remain project-native (T-A) now, and pay only a small, independently-justified reversibility premium that makes T-B reachable later without committing to it.**

Why:

```text
1  §2 makes in-tree materialization mandatory for any project producing
   governed views. So the reachable upstream topologies (T-B, T-E) differ
   from T-A only in *authoring origin and patch flow*, not in what a
   project contains. The difference is therefore smaller than it looks,
   and deferring it costs less than it appears to.

2  At N=1, extracting mechanism encodes ADS's accidents as generic. That
   is MC-0014's circularity lesson at repository scale, and this project
   has already paid once to learn it.

3  The migration/compatibility layer is a large fraction of the current
   surface and is 100% non-transferable. Extraction now would either drag
   it along or require untangling it first, and untangling it is wasted
   work because it is scheduled to retire at W8 anyway.

4  The existing two-tenant split (src/ product vs tools/project_knowledge/
   method) demonstrates that a directory boundary with enforced layering
   already separates unrelated concerns adequately in this repository.
   No repository boundary has been needed to achieve that.

5  AO-10 is held, W5-F0 is paused, and Research 219 already names an
   interposed governed evolution boundary. Adding a residency migration
   on top of a paused migration compounds unfinished transitions, which
   is the specific failure the single-authority invariant exists to avoid.
```

The reversibility premium, all three items justified on today's merits independent of any reuse claim:

```text
R1  Unify the instance-policy seam.
    Move GENERATED_ROOT, the manifest root, the schema path list and the
    pure-unit registry's implementation paths behind the same policy
    object DiscoveryPolicy already is. This removes hardcoded-path
    duplication across view definitions, and it is the natural companion
    to the C1 per-view closure work already accepted in Research 209.

R2  Keep contracts physically separable and version-disciplined.
    Already true: schemas/project_knowledge/ is data, v1 files are never
    edited in place, Requirements V0.2 and Specification 028 are discrete
    documents. Requires no work; requires only not regressing.

R3  Maintain a genericity claim register.
    One carrier recording, per mechanism, whether it is claimed generic,
    instance-configured, or ADS-specific — with the evidence for the
    claim. This is a claim register, not a package boundary. It costs
    almost nothing, it is falsifiable, and it is what a future extraction
    would need in order not to be a guess.
```

What this explicitly does **not** do: create a second repository, create a package, introduce a runtime dependency, or make any genericity claim the evidence does not support.

## 10. Strongest alternative (output 2)

**T-E, contracts-as-data extraction.** If the owner wants something reusable *now* rather than later, this is the option I would defend rather than T-B or T-G.

Its case is genuinely strong:

```text
it survives §2 trivially, because schemas are inputs not generators
the durable value in ADS may well be the contracts rather than the code —
    Requirements V0.2, the profile contracts, the authority statuses and
    the AO-4 classification vocabulary are the parts that took the most
    evidence to earn
schemas are already data, already versioned, already vendored-by-default
it makes no claim about implementation, so a second project is free to
    build differently and still be comparable
divergence is trivially expressible: a project adds a profile
```

Its weakness is that contracts without an implementation transfer much less leverage, and a second project would have to rebuild the substrate. That is a real cost. But it is a cost that *produces the evidence* the mechanism claim currently lacks — a second independent implementation of the same contracts is exactly the N=2 discriminator.

If I am wrong about deferring, I think I am wrong in the direction of T-E, not T-B or T-G.

## 11. Strongest criticism of my preferred architecture (output 3)

I want to state this at full strength rather than softening it.

**"Defer until evidence" can become "never," and the coupling cost grows monotonically.** Every view added, every pure unit registered, every profile introduced increases the extraction surface. The `implementation_files` closure already lists twenty-plus paths per view. There is a real risk that the window in which extraction is affordable closes quietly, and R1/R3 are too weak a hedge to keep it open.

And the sharpest form of that criticism, which I think is correct: **my proposed seam only addresses the syntactic coupling.** Parameterizing paths is the easy half. The expensive coupling is semantic — the eight profiles, the six authority classes, the eight views, and above all the 18-subject catalog encode ADS's domain shape, and no amount of path indirection touches them. R1 buys less reversibility than it appears to.

There is also a genuine historical counterexample I should not hide behind my own N=2 argument: **Rails was extracted from a single application.** So was Django, from a single newspaper CMS. Both are N=1 extractions that worked well. My claim that N=2 is required is therefore not a law.

What I think distinguishes this case, stated as a distinction rather than a dismissal:

```text
Rails/Django extracted *implementation conveniences* where a wrong guess
    costs a refactor

here the candidate extraction includes *authority and validity semantics*
    where a wrong guess is encoded into governing contracts and, by this
    project's own AO-4 discipline, reversal requires a governed
    supersession with qualification

Rails' extractors immediately used it on further projects, so N=2 arrived
    within weeks; there is no second ADS-like project in view

DHH had broad prior evidence about web applications generally; ADS has
    deep evidence about one project's specific knowledge failures
```

That is a defensible distinction, but it is a judgment, not a proof, and a reasonable architect could weigh it the other way.

## 12. Three most dangerous long-term failure modes (output 5)

```text
F1  EXTRACTION_BEFORE_EVIDENCE
    A generic layer is extracted at N=1, encodes ADS accidents, then
    accretes configuration options to serve a second project that does
    not fit. The configurability spiral is the classic terminal state,
    and it is the exact shape of the MC-0014 circularity error.

F2  AUTHORITY_LEAK_VIA_UPGRADE_CHANNEL
    If a framework upgrade can change validation or authority semantics
    without a governed in-project decision, an external actor effectively
    holds authority over the project's governing semantics. This violates
    KA-I01/KA-R19 while looking like ordinary dependency management, and
    it is the failure T-C makes structurally possible.

F3  PROVENANCE_FRACTURE
    Generator bytes move outside the project's Git tree, implementation
    digests become uncomputable or bound to a foreign lineage, and the
    project loses the ability to prove its own derived views correspond
    to its own sources. §2 shows this is not hypothetical; it is what
    the current contract already forbids.
```

## 13. Three highest-value simplifications (output 6)

```text
S1  Unify the instance-policy seam (R1). One policy object, not one
    hardcoded constant per view definition. Wins today on maintenance
    grounds alone; wins again later if extraction ever happens.

S2  Treat contracts-as-data, not code, as the reuse unit. Schemas and
    requirement documents are already separable, already versioned, and
    already the part with the strongest evidence behind it.

S3  Do not create a second repository. The two-tenant reality is already
    handled by directory boundary plus enforced import layering, and a
    repository boundary adds coordination cost without adding a single
    invariant that layering does not already provide.
```

## 14. Falsification (output 7)

What would falsify my preferred topology, stated so it can actually be run:

```text
FALSIFIER 1  initialize a genuinely unrelated second project against the
             current architecture. If more than roughly half the setup
             effort is spent editing *mechanism* code rather than
             *policy* values, the seam hypothesis in R1 is wrong and
             extraction should be contract-first (T-E), because the
             mechanism is not as generic as it looks.

FALSIFIER 2  observe ADS's own change pattern over the next several
             waves. If mechanism modules repeatedly require edits that
             only ADS needs, then mechanism/instance is not a real
             boundary here and no extraction target exists yet.

FALSIFIER 3  attempt a vendoring rehearsal: copy the mechanism into a
             scratch tree and verify that manifest binding, freshness and
             the C1 per-view closures still hold with an upstream ref
             recorded. If manifest binding cannot be preserved, T-B is
             dead and only T-A and T-E remain.

FALSIFIER 4  measure the migration/compatibility fraction of the current
             mechanism surface. If it is large, extraction should wait
             until after W8 retirement regardless of everything else,
             because that fraction is scheduled to disappear.
```

## 15. Is a second real project required before extracting? (output 8)

**Split answer, and I think the split is the substance of it.**

```text
CODE / MECHANISM EXTRACTION     yes, a second real project is required
    the genericity claim is currently unfalsifiable; every mechanism was
    derived from ADS failures; N=1 extraction validates against the
    corpus that produced it

CONTRACT EXTRACTION             no, not required
    schemas and requirement documents can be published and vendored as
    data without asserting that any implementation is reusable, and a
    second independent implementation against them is itself the
    strongest available N=2 evidence
```

So the honest sequencing is: contracts may be extracted on evidence already in hand; mechanism may not.

## 16. Impact on Research 177, Research 218, Specification 028 (output 9)

Under my preferred topology: **no material impact on any of the three.**

```text
RESEARCH 177    unchanged and, I would argue, strengthened. Its
                tools/project_knowledge vs src/ads_system boundary is
                precisely the mechanism/product separation the residency
                question is about, and it is holding at scale.

RESEARCH 218    unchanged. The frozen tree, placement precedence, naming,
                granularity, item-registry and subject contracts are all
                orthogonal to residency. Nothing in §1-§15 above requires
                a different physical hierarchy.

SPEC 028        unchanged, and §19 is *reinforced* rather than
                challenged — my §2 finding is that its implementation_files
                contract already forces in-tree mechanism residency.
```

The one narrow prospective amendment candidate, and I want to name it precisely so it is not discovered later: **if T-B is ever selected, Specification 028 would need to state whether vendored upstream files count as project implementation files for manifest binding, and whether the recorded upstream ref is part of the manifest.** My reading is that vendored files trivially qualify because they are ordinary project Git blobs, so the amendment would be a clarification rather than a semantic change — AO-4 `CLARIFY`, not `AMEND`. But it should be decided rather than assumed.

I found no reason to reopen Candidate 01 semantics. This question does not reach them.

## 17. Residency before internal hierarchy? (output 10, task I)

**Largely independent; residency does not need to block the hierarchy, with one narrow exception.**

The reasoning:

```text
Research 218's contracts are about where a *carrier* lives by primary
responsibility. Residency is about where *mechanism* is authored and
distributed. Those axes do not intersect for any carrier in the frozen
tree.

Research 218 already isolates docs/project_knowledge/ as narrow
infrastructure rather than a universal home, which is exactly the
property a later framework/instance separation would need.

The one exception: if a vendored upstream layer is ever introduced, it
needs a physical home, and that is a single new directory question. It
does not disturb the rest of the hierarchy.
```

So I would not sequence residency ahead of the hierarchy work on dependency grounds. If the owner wants residency first, the justification has to be attention and coherence, not blocking.

I will add one caution that cuts the other way, because I think it is real: an AO-4 evolution case against Research 218's hierarchy and a residency decision are both large architecture questions opened while W5-F0 is paused, AO-10 is held, and the W5 migration is incomplete. The project currently has three unfinished transitions stacked. That is itself an architectural risk independent of which question is answered first, and I would rather name it than let it pass.

## 18. Stress test (brief §6)

### 18.1 ADS — existing, large, highly evolved

```text
INITIALIZATION   already initialized; T-A is the status quo, so there is
                 no initialization event

USE              unchanged; R1 is an internal refactor with no authoring
                 or semantic consequence

EVOLUTION        mechanism and policy evolve together in one lifecycle,
                 governed by AO-4; R3's claim register accumulates
                 evidence about which parts are generic as they are
                 exercised

RECOVERY         clone and run; nothing external; unchanged from today
```

### 18.2 A materially different second project

I deliberately chose something that shares the *continuity* problem and almost none of the *domain*: **a long-running academic research group's protocol and methods knowledge base** — multi-year, high personnel turnover, grant-cycle rhythm, wet-lab protocols, regulatory/ethics obligations, no software product at all.

```text
INITIALIZATION   under T-A: copy tools/ and schemas/, delete the
                 migration/compatibility layer entirely (it has no legacy
                 continuity architecture to shadow), rewrite
                 DiscoveryPolicy's values, replace the subject catalog
                 wholesale, keep the profile set mostly intact

                 the profiles transfer better than expected:
                     workstream          -> a study/experiment line
                     governing_procedure -> a lab protocol, with the
                                            ordered action contract doing
                                            real work for a wet-lab SOP
                     capture             -> bench observation before review
                     identity_transition -> protocol revision continuity
                     joint_authority     -> protocol + ethics approval
                                            jointly governing one action
                     project_boundary    -> does NOT transfer; its
                                            promoted_branch/promoted_commit
                                            contract is Git-specific

USE              the authority resolver's value is high here: "which
                 protocol revision governs this run, at this date, under
                 this approval" is exactly a scope+temporal+relation
                 query, and the fail-visible statuses matter more than in
                 ADS because the consequence class is physical

EVOLUTION        AO-4's classification vocabulary transfers essentially
                 unchanged; a protocol amendment is literally an AMEND
                 with prospective realization and no retroactive rewrite
                 of past runs — which is exactly what research-integrity
                 practice already requires

RECOVERY         a clone plus Git; no network; survives the group losing
                 every original member, which is the actual failure this
                 project would be buying the architecture for
```

What this exercise actually taught me, and I did not expect it: the **authority-resolution and evolution-governance layers transfer far better than the knowledge-organization layer.** Subject catalogs, domain homes, the compatibility machinery and the view set are all ADS-shaped. The resolver, the workstream engine, the capture lifecycle and AO-4 are not. If an extraction is ever done, that is the seam the evidence points at — and it is *not* the seam the current directory structure would suggest.

## 19. External patterns that informed this (output 11)

Clearly separated from ADS evidence; none adopted because it exists.

```text
Vendoring with recorded lineage — Go's original vendor directories,
    git subtree, and the cookiecutter/cruft template-upgrade pattern.
    Informed T-B's shape: a complete in-tree copy plus a recorded
    upstream revision, with upgrades as explicit merges.

Framework extraction from a single application — Rails from Basecamp,
    Django from a newspaper CMS. Cited above as a genuine counterexample
    to my own N=2 requirement, not as support for my position.

Speculative generality / rule of three — the widely-held heuristic that
    an abstraction should wait for a third instance. Directionally
    consistent with my recommendation, but I did not lean on it, because
    a heuristic is weaker than the §2 structural finding.

Semantic versioning and never-edit-a-published-schema discipline —
    already present in this project's v1 schema files; informed the
    upgrade/divergence reasoning in §7.

Inner-source patch flow — informed the contribution direction in §7:
    upstream receives patches, never gains authority.

OAIS and archival independence — already part of this project's evidence
    base from Research 125/127; informed §8's insistence that recovery
    must not depend on an external party remaining reachable.
```

I did not use any of these as a template. The load-bearing reasoning is §2 (a structural finding in this repository's own frozen contract) and §4 (this project's own MC-0014 lesson about N=1 validation).

## 20. Required output summary

1. **Preferred:** project-native (T-A) plus a small reversibility premium (R1 seam unification, R2 contract separability maintained, R3 genericity claim register). §9.
2. **Strongest alternative:** T-E contracts-as-data extraction. §10.
3. **Strongest criticism:** deferral may become permanent, the coupling cost grows monotonically, my seam addresses only syntactic coupling while the expensive coupling is semantic, and Rails/Django are real N=1 counterexamples to my evidence bar. §11.
4. **Generic vs project-specific:** three-way split in §4; the transferable core is resolver + workstream + capture lifecycle + AO-4, not the knowledge-organization layer. §18.2 sharpens this.
5. **Failure modes:** extraction-before-evidence, authority leak via upgrade channel, provenance fracture. §12.
6. **Simplifications:** unify the policy seam, reuse contracts not code, do not create a second repository. §13.
7. **Falsifiers:** four, in §14.
8. **Second project required?** Yes for mechanism, no for contracts. §15.
9. **Impact:** none material on Research 177, Research 218 or Specification 028; one narrow §19 clarification candidate if T-B is ever selected. §16.
10. **Residency before hierarchy?** No dependency; largely parallel; one narrow exception; plus a caution about three stacked unfinished transitions. §17.
11. **External patterns:** §19, with Rails/Django cited against my own position.

```text
INDEPENDENT_PKIA_RESIDENCY_REVIEW_CONTAMINATED: NO
PREFERRED_RESIDENCY_TOPOLOGY_READY_FOR_COMPARISON: YES
GENERIC_REUSABLE_LAYER_JUSTIFIED: NO
PROJECT_SELF_CONTAINMENT_REQUIRED: YES
MATERIAL_RESEARCH218_IMPACT_FOUND: NO
MATERIAL_SPECIFICATION028_IMPACT_FOUND: NO
```
