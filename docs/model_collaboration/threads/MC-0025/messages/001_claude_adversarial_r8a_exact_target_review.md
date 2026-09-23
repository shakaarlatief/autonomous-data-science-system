# MC-0025 Message 001: Claude Adversarial Review of R8-A Exact Target Repository Realization

```text
Thread                          MC-0025
Message                         001
Author / collaborator           Claude
Role                            ADVERSARIAL REVIEWER
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Branch head seen                2cc203bf608b9a14664d463ae0231f1227063b91 (routing/inbox/thread only)
Exact review target             39435d148b4170e13d150e178022d66408de0df1
Reviewed at target              Research 257, 256, 255, 254, 253, 252, 251, 250, 249, 248;
                                 Research 235 (AO-9/P7); Specification 028; repository tree,
                                 pyproject.toml, frontend/package.json
Prior context used              MC-0021 through MC-0024
Mode                            ADVERSARIAL_REVIEW / owner decision on R8-A pending
```

I produced the A1/A2 amendments that Research 248–250 implement, and the A1–A6 amendments that Research 255 carries. Where a finding below is a continuation of my own prior work I say so, and where Research 257 has correctly satisfied one of those amendments I say that too.

## 1. Summary before the detail

Research 257 is a disciplined translation. Root count is 9 against a preregistered bound of 12; the five legitimate root responsibility classes from the A2 contract each map to exactly one entry class; zero A1 root integration contracts were needed; the operations/engineering bound was preregistered *before* population as A4 required; and the dependency invariants in §14 are stated as fail-closed architecture checks rather than conventions. None of my six MC-0024 amendments were dropped.

My disposition is **AMEND**, with five amendments that must be decided before the representation stage and four before the file-level migration manifest. The plane architecture, the workspace count, the JW1 boundary and the AO residency all survive attack.

The strongest finding is that **R8-A introduces exactly one new cross-plane coupling — shared dependency resolution — and it is the one coupling the accepted architecture's own empirical evidence argues against.**

## 2. A. The exact root

### 2.1 What survives

Mapping the nine entries against the A2 contract from MC-0023, which Research 249 §9 preregistered:

```text
repository-host integration      .github/  .gitignore
external-tool-required anchors   pyproject.toml  uv.lock  .python-version
workspace orchestration          pyproject.toml (dual role, legitimate)
cold-start entry                 README.md (human) + project_anchor.json (machine)
named root integration contracts none (0)
accepted planes                  product/  project/
```

Exactly one machine-readable anchor, as A2 required. No entry is present for lack of a better owner. **KEEP.**

### 2.2 AM-1 — the shared `uv.lock` is a cross-plane lifecycle coupling, and it is the wrong one to accept

This is my strongest finding and it spans tasks A and I.

Research 257 §14 states the dependency invariants as import rules:

```text
product/runtime      MUST NOT import project/system
product/interaction  MUST NOT import project/system
```

and says repository tests must eventually encode them fail-closed. Good. But the invariants are stated and enforced at the **import** layer, while the strongest coupling R8-A actually introduces sits at the **dependency-resolution** layer, where nothing checks it.

One `uv.lock` means one resolution across both planes. A Product runtime dependency upgrade can force a Project system dependency change, and the reverse. No import occurs; the invariant is not violated; the planes are coupled anyway.

Three reasons this is not a nitpick:

```text
1  It contradicts the measured basis for the plane split.
   Research 239's G1 measurement — the test I proposed in MC-0022 and
   which was preregistered in Research 238 — found 61.1% FRAMEWORK_ONLY
   against a 30% floor and only 13.9% SPANS_LAYERS, across two
   structurally different project eras. Lifecycle independence is the
   best-evidenced claim in the whole program. R8-A then couples the two
   lifecycles at the one layer where they were previously independent.

2  It reopens the PSMF upgrade channel as a dependency path.
   Under PSMF, project/system is materialized from a generic upstream.
   A framework upgrade pulls upstream's dependency expectations into a
   lock shared with the Product runtime. A framework upgrade could then
   force a Product runtime dependency change. That is precisely the
   "authority leak via upgrade channel" failure I named as F2 in
   MC-0022 §12, arriving through resolution rather than semantics.

3  It is not separable from the workspace choice.
   uv workspaces resolve to a single lockfile at the workspace root by
   design. "One workspace" therefore entails "one lock." The real
   question is not lock granularity; it is whether the two planes should
   be one uv workspace at all.
```

**Proposed amendment.** Two independently resolved Python projects rather than one workspace:

```text
product/runtime/pyproject.toml   +  product/runtime/uv.lock
project/system/pyproject.toml    +  project/system/uv.lock

root pyproject.toml              repository-wide TOOL configuration only
                                 (formatter, linter, type-checker settings)
                                 NOT workspace membership
```

Consequences, stated honestly:

```text
root count    9 -> 8, because uv.lock leaves the root
coupling      removed at the only layer where it existed
PSMF          upgrade cannot perturb Product resolution
cost          two installs instead of one; CI must install per plane;
              cross-plane incompatibility is discovered at integration
              rather than at resolution
```

That cost is real. I judge it smaller than the coupling, because integration-time discovery is exactly what `project/engineering/tests/` exists for, and because the planes are already asserted never to import one another — so a shared resolution is buying compatibility between things that never meet.

**Classification: AMEND. Must be decided before the representation stage**, because representation will assume a dependency and packaging topology.

### 2.3 AM-1b — `.python-version` carries a stated condition with no detector

§2.1 justifies it "while Product runtime and Project system share the same supported Python line." That is a genuine conditional, and nothing detects when it stops holding. Under PSMF, the Project system's supported line may be set by upstream while the Product runtime tracks its own needs.

If AM-1 is accepted, `.python-version` should move per-plane and the root retains at most a repository-wide floor, or drops it entirely (root 8 → 7). If AM-1 is rejected, the condition should be stated as a falsifier in §15. **AMEND, folded into AM-1.**

### 2.4 `project_anchor.json` — CLARIFY, not amend

Two small things:

```text
naming    the root's one machine anchor is Project-plane-named. That is
          correct — repository cold start is J03, a Project
          responsibility, and the Product does not need a machine anchor
          to operate. But R257 does not say so, and a reader will ask
          why there is no product_anchor.json. One sentence.

format    the filename embeds the serialization. If the anchor's format
          ever changes, the root entry name changes with it — churn at
          exactly the surface the root contract exists to stabilize.
          JSON is the right default for a tiny machine anchor and I do
          not recommend changing it; I recommend noting the coupling.
```

### 2.5 No missed root integration contract

I looked for one. The candidates are provider credentials (per-plane), build provenance metadata (Research 250 §9 already resolves it as asymmetric ownership under A1), and shared type contracts between runtime and web (product-internal, not cross-plane). **Zero remains correct.**

## 3. B. Product realization

### 3.1 The six runtime modules are the six PC contexts, and that is mostly defensible

`project_intelligence`=PC1, `methodological_knowledge`=PC2, `evidence_provenance`=PC3, `reasoning`=PC4, `execution`=PC5, `runtime_platform`=PC7, with PC6 in `product/interaction/`.

Research 250 §1.1 warned that "a bounded context does not automatically deserve its own package, process, service or repository." R257 gives each a *source directory* inside one package, which is weaker than any of those. Refusing a global `domain/`/`application/`/`infrastructure/` split in favour of context-first modules is the right call and is a genuine improvement on the current `src/ads_system/{application,domain,infrastructure}`. **KEEP.**

### 3.2 AM-2 — `runtime_platform/` drops an explicit R250 requirement

Research 250 §3 states, of PC7:

> R6 must preserve internal separation among persistence, external integrations, security and operations so they can split later if actual lifecycle/deployment evidence demands it.

That is an instruction to R8, and R257 §4.1 does not carry it. `runtime_platform/` appears as one module with four responsibilities (P09, P10, P11, P12) and no stated internal boundary. R250's split-later provision becomes unenforceable the moment the four are implemented as one undifferentiated module — which is exactly how PC7 would become the "miscellaneous infrastructure owner" that R250 §3 explicitly says it is not.

**Amendment:** `runtime_platform/` declares its four internal sub-boundaries (persistence, integration, security, operations) as a condition of the module's acceptance. This is a one-line addition that preserves a requirement already accepted at R6.

**Classification: AMEND. Before the file-level migration manifest**, since current `src/ads_system/infrastructure/` will be split into it.

### 3.3 CL-1 — cross-context orchestration has no named owner

R250 §4 refers to "bounded reasoning tasks/context from application/domain orchestration," implying an orchestration layer exists. R257 §4.1 retires the global `application/` layer — correctly — without naming where a use case spanning PC1 + PC3 + PC5 lives.

The conventional modular-monolith answer is that each context owns its own application layer and a cross-context flow is owned by the *initiating* context, with other contexts reached through their published contracts. That is almost certainly the intended reading. It should be stated, because today `src/ads_system/application/` holds exactly this material and its migration target is currently undefined. **CLARIFY.**

### 3.4 CL-2 — API transport ownership is stated but not assigned

R257 §4.2: "A backend API transport does not automatically become a separate interaction workspace. It remains with the runtime." But R250 §3 assigns PC6 "external client/API/CLI presentation contracts where product-facing." So the API *contract* is PC6 and the transport *implementation* stays in runtime — and under the six modules, an HTTP layer would land in `runtime_platform/`, conflating transport with persistence, security and operations.

This is a concrete instance of AM-2: if `runtime_platform/` declares internal sub-boundaries, transport either gets one or is explicitly assigned elsewhere. **CLARIFY, resolved by AM-2.**

### 3.5 CL-3 — two rename standards are applied without stating the rule

`ads_system` is retained to avoid import churn (§3.1). `project_knowledge` is replaced by `ads_project_system` to escape legacy framing (§8). Both are right, but the document applies two different tests in two sections.

The consistent rule, which R257 should state once: **rename when the name is semantically wrong, not when it is merely old.** `project_knowledge` named the implementation after the problem domain — semantically wrong. `ads_system` correctly names the ADS product system — semantically fine. Retention is then a principled conclusion rather than migration conservatism, which is what the brief asks me to distinguish. **CLARIFY.**

### 3.6 `interaction/` as a one-child parent — KEEP

A parent with a single occupant invites the "reserved name" objection, and §4.2 itself forbids creating empty future workspaces. But `interaction/` is not empty and not reserved: it is the physical expression of PC6 being a distinct bounded context from PC1–PC5/PC7. That is a classification level with semantic content. **KEEP.**

## 4. C. Project non-knowledge realization

### 4.1 AM-3 — the `engineering/` ↔ JW1 validator boundary is undefined, and it is the highest-cost ambiguity in the migration

`project/engineering/checks/` holds "repository-wide deterministic validators/check entrypoints." JW1's `views/` and `migration/` modules also produce validation. Today's `scripts/` contains both kinds mixed together, and R257 §12 disposes of `scripts/` by splitting it "among project/engineering, project/system, project/research, or retire."

So the single most ambiguous migration in the whole target depends on a boundary the target does not define. Take a concrete case: a validator that checks whether project-knowledge declarations satisfy the Specification 028 contract. Is that JW1 semantics (it *is* the contract) or repository engineering (it is a repository-wide gate)? Both readings are fully available.

This is the same "or" shape I flagged as A-1 in MC-0024 and as A1 in MC-0023: a placement rule with an unresolvable branch, fixed by splitting responsibility rather than arbitrating placement.

**Proposed rule**, derivable from the accepted contexts rather than invented:

```text
JW1 (project/system)       owns SEMANTIC validation — does this artifact
                           satisfy the project-knowledge/control contract

project/engineering        owns REPOSITORY validation — structural,
                           integrity and cross-workspace gates — and owns
                           INVOCATION: the CI entrypoints that call both

direction                  engineering MAY invoke JW1; JW1 MUST NOT
                           depend on engineering
```

The direction clause matters for a reason R257 does not state: JW1 is PSMF-materializable and `engineering/` is ADS-specific and never extractable. A JW1 dependency on engineering would put non-extractable code inside the materialized framework's dependency graph.

**Classification: AMEND. Before the file-level migration manifest.**

That same argument, incidentally, defeats the obvious simplification of merging `engineering/` into `system/` — one project-plane executable workspace instead of two. It would resolve the ambiguity but would place permanently ADS-specific code inside the area PSMF intends to materialize from upstream. The split is right; it needs the rule.

### 4.2 AM-4 — `project/research/` drops the disposition discipline that justifies retiring `experiments/`

Research 250 §8 is explicit:

> Research execution workspaces: EPHEMERAL / PROGRAM-SCOPED BY DEFAULT... After completion each receives an explicit disposition: promote implementation / preserve executable reproduction package / retain evidence only where independently re-derivable / archive / retire.

R257 §5.2 describes `project/research/` as active execution and says durable results move to `knowledge/evidence/`, but does not restate the mandatory-disposition-at-completion obligation.

That obligation is the *entire* difference between `project/research/` and the `experiments/` root it replaces. Without it, R257 retires a universal bucket and creates a renamed one. **AMEND: restate the four-way disposition as a completion obligation. Before the migration manifest**, because current `experiments/` migrates into it.

### 4.3 AM-4b — `reproductions/` has a reason test and no admission gate

§5.3 defines it narrowly and says "It must not become a dumping ground for stale code." That is a reason test without an admission rule — the same shape I attacked for the root in MC-0023 and for `operations/engineering/` in MC-0024.

The gate already exists and only needs binding: admission to `reproductions/` is the outcome of R250 §8's explicit "preserve executable reproduction package" disposition, recorded as a decision, not an author's judgment at move time. **AMEND, folded into AM-4.**

On whether `reproductions/` deserves first-level status with one expected occupant: I think yes. Its lifecycle differs from active research (frozen versus active) and from knowledge (executable versus informational), and collapsing it into either would misclassify it. **KEEP the area; gate the admission.**

### 4.4 The five Project areas — KEEP

`system / engineering / research / reproductions / knowledge` map to JC2 / JC4-executable / JC3-execution / JC6-executable / JC1+JC3-evidence+JC4-knowledge+JC5+JC6-records. No context is unhomed and no area is contextless. The information/execution split at this level is the right one.

## 5. D. JW1 and `ads_project_system`

### 5.1 AM-5 — five of the ten modules exist for capability that is not implemented, and §4.2's no-empty-reservation rule is not applied to them

The ten modules map to current implementation as follows:

```text
semantics       <- model + declaration + identity + authority + references
views           <- views
preservation    <- capture
migration       <- services/compatibility
adapters        <- adapters
orchestration   <- workstreams, plus new AO-6 material
reconstruction  <- partly in services today; largely new
activation      <- NEW; AO-3, held pending AO-10
evolution       <- NEW; AO-4, held pending AO-10
continuity      <- NEW; AO-5, held pending AO-10
```

Three modules (`activation`, `evolution`, `continuity`) exist purely for AO capability that AO-10 has not implemented and that R257 §10 explicitly keeps held. A fourth (`reconstruction`) is largely prospective.

R257 §4.2 states the right rule for workspaces — "No empty future workspace is created merely to reserve a name" — and does not apply it to JW1 modules. Freezing directory structure ahead of implementation means the first implementation is shaped by the taxonomy rather than by the code, which is the failure this project has diagnosed twice (MC-0014's self-confirming admission rule; MC-0016's untested `JOINT_AUTHORITY` criterion).

§8 gets close — "These are module-responsibility boundaries, not mandatory one-file-per-concept rules" — and should go one step further.

**Amendment:** apply §4.2's rule uniformly. The ten are accepted *responsibility* boundaries for JW1; physical module directories are created as capability lands, not in advance. **Before the representation stage**, because representation will otherwise be designed per-module for modules that do not yet exist.

### 5.2 AM-6 — `adapters/` sits on the PSMF framework/instance seam and the document does not say which side

This is the finding I would most want checked, because it is the first place the PSMF seam becomes concrete rather than conceptual.

R257 §3.2 separates:

```text
src/ads_project_system/   framework mechanism
instance/policy/          ADS instance policy
```

which is exactly the seam MC-0022 §6 said was half-built in the current implementation. Good. But §8 places `adapters/` — including "collaboration/provider" and "local-runtime/tool integration" — inside `src/`.

Provider adapters are close to the definition of instance policy. In MC-0022 §4 I classified provider integration as the specific duplication risk across planes, and in MC-0022 §12 I named the upgrade channel as a failure mode. If concrete provider bindings live in `src/`, a PSMF framework upgrade overwrites ADS-specific integration.

**Amendment:** state whether `adapters/` holds generic adapter *interfaces* (framework, `src/`) with concrete provider bindings in `instance/policy/`, or concrete adapters (instance). I would take the former. **Before the representation stage**, because `instance/policy/`'s representation depends on what it must hold.

### 5.3 `semantics/` and `views/` reproduce old framing — and that is correct here

The brief asks. `views/` is the current module name verbatim; `semantics/` is the current model+declaration+identity+authority grouping. So two of ten are carried forward.

That is not anchoring, because these are precisely the parts that were implemented and qualified through W0–W4. Carrying forward a qualified boundary is evidence-backed. But R257 does not distinguish "retained because qualified" from "newly derived," and Research 255 §2/§3 shows the project knows how to make that distinction explicitly. **CLARIFY:** label which JW1 modules are retained-qualified and which are prospective, for the same reason 255 labels retained-versus-superseded contracts.

### 5.4 `ads_project_system` naming — KEEP with a note

Under PSMF the framework is generic and the instance is ADS. A package named `ads_project_system` that contains generic mechanism is misnamed for eventual extraction. But R257 §3.2 calls it "the target local JW1 package identity" — local, hence ADS-scoped, hence correct. The `src/` + `instance/` split inside it already anticipates the extraction boundary. **KEEP;** note that extraction will need a generic upstream name and that the internal split is what makes that possible.

### 5.5 Activation/orchestration as a separate runtime or process — no

Nothing in AO-3 or AO-5 requires a daemon. Progressive Control Closure is per-interaction and bounded. A separate process would add operational surface with no accepted requirement behind it. **KEEP as in-package modules.**

## 6. E. Activation/orchestration residency

### 6.1 No circularity, but the direction should be stated

`project/knowledge/` is information and not importable (§14). `project/system/` reads knowledge carriers and writes into `system/generated/`, not into knowledge. So no code cycle exists.

There is a mutual *reference*: knowledge carriers conform to declaration schemas owned by `system/contracts/schemas/`, while human-readable architecture *about* the system lives in knowledge per A3. That is mutual reference, not circular dependency, and it is fine — but R257 should state the direction explicitly: **system owns machine contracts, knowledge owns human contracts about the system, neither imports the other.** **CLARIFY.**

### 6.2 No Product-runtime dependency on Project system

§14 forbids it and the module map contains nothing that would require it. **KEEP.**

### 6.3 AM-7 — `migration/` holds a permanent capability under a transitional name

R257 §9 maps AO-7 (Authority-Preserving Successor Bridge) to `migration/ + activation/orchestration boundary`, and §8 describes `migration/` as "compatibility shadows, successor bridge support, migration audit, cutover/rollback support" — all transition-shaped.

But under AO-4, architecture evolution is continuous and governed. Successor transitions recur; they are not a one-time cutover. So the successor bridge is a permanent capability sitting in a module whose name implies it retires.

This matters concretely for representation: if `migration/` is transitional, its state is disposable; if permanent, its state (bridge receipts, authority-transition evidence) is durable and needs a representation decision. **AMEND: decide whether `migration/` is a permanent transition-management capability or a temporary migration scaffold, and name it accordingly. Before the representation stage.**

### 6.4 CL — AO-6 splits between JW1 policy and engineering mechanics

R257 maps AO-6 to `orchestration/ + adapters/git`. Research 249 J07 assigns "repository bootstrap, workspace orchestration, CI execution architecture" to project engineering. Branch lifecycle sits between them.

The discriminator: AO-6 binds branches to *workstream purpose*, which is JC2/JW1 semantics. Branch protection rules, CI triggers and host configuration are JC4 mechanics. So JW1 owns the policy and engineering owns the enforcement surface. Not stated. **CLARIFY.**

### 6.5 KA-R51 and KA-R52 imply no new durable information class, but KA-R52 spans two owners

The brief asks whether either implies a responsibility R7 does not represent. Checking both:

```text
KA-R51  control-miss / owner-reminder observability
        produces miss evidence -> knowledge/evidence/qualification/
        COVERED, and R257's mapping is correct

KA-R52  accepted-MUST realization traceability
        Research 235 §4 requires no untracked third state: every accepted
        MUST is either realized or explicitly deferred with a preserved
        blocking reason and reactivation condition.

        the OBLIGATION originates in governance — an accepted MUST in a
        specification or decision

        the REALIZATION STATUS is control state — JW1

        the EXPLICIT DEFERRAL, with blocking reason and reactivation
        condition, is durable governance information and has a home in
        knowledge/governance/planning/, which R254 §4.4 already scopes to
        "explicit deferred decisions"
```

So KA-R52 is covered, but across two owners, and R257 maps it only to "orchestration obligation-realization traceability" — the system half. **CLARIFY:** state that obligation identity and governed deferral are governance-knowledge, realization status is system control state, and the two are bound by a typed relation. No new class is needed, and no AO semantic contract needs amendment.

### 6.6 No AO semantic contract requires amendment

I checked AO-3 through AO-9 plus P7-D01 against the target. R8-A changes residency and representation, not semantics, as §9 claims. The only AO-adjacent amendment I raise is AM-7, which is about a module's name and permanence rather than about AO-7's contract. **AO_RESIDENCY_ACCEPTABLE: YES.**

## 7. F. Operations/engineering taxonomy

### 7.1 The six are derived and the bound is principled — KEEP

`repository / environments / verification / security / release / recovery` map to J07 / J11 / J06 / J08 / J09 / J11+J12. Every accepted JC4 responsibility has a home and no subarea is contextless. The bound of 8 was preregistered before population, which is exactly what A4 required and what the root bound did successfully. **KEEP.**

I checked for missing responsibilities against R249's J06–J09 and J11: development observability lands in `environments/`; cost and resource efficiency are quality attributes rather than owners per R249 §4. No gap found.

### 7.2 AM-8 — three areas share the word "continuity/recovery"

```text
project/system/src/.../continuity/     mechanized interaction continuity,
                                        interruption/resume, independent
                                        recovery, break-glass routing

knowledge/operations/engineering/recovery/
                                        break-glass, incident, backup,
                                        development-continuity procedures

knowledge/operations/collaboration/     "continuity/handoff procedure where
                                        human-readable" (R254 §6.2)
```

All three are legitimate and the split is real — mechanized versus procedural versus handoff. But a contributor deciding where a recovery artifact belongs has three candidate homes with near-identical names, and this is the only place in the target where that happens.

**Amendment:** state the three-way rule explicitly, or rename to remove the collision. The rule: JW1 `continuity/` is mechanized and executable; `operations/engineering/recovery/` is human break-glass and incident procedure; `operations/collaboration/` is handoff between contributors. **Before the migration manifest.**

### 7.3 CL — verification and security both need the A4 declarative/procedural restatement

`operations/engineering/verification/` ("how qualification is executed and interpreted") versus `evidence/qualification/` (qualification results) is exactly the A4 procedural/declarative split, and it is correct. Same for `security/` (procedures) versus security policy (governance). Neither is restated in R257, and the names are close enough that the distinction will be re-litigated at migration time. One sentence each. **CLARIFY.**

## 8. G. Cold start

### 8.1 AM-9 — the break-glass path exists structurally but is not stated, and AO-5 requires it

R257 §7 routes both cold-start paths through generated artifacts:

```text
human    root README -> project/system/generated/orientation/current.md
machine  project_anchor.json -> project/system/generated/orientation/current.json
```

AO-5 requires *independent recovery* — recovery that does not depend on the component being recovered. If the generator is broken, a migration is half-complete, or the clone is fresh and nothing has been generated yet, both stated first hops fail.

The structure does support a generate-independent path, and §7.2 nearly says so: the canonical control/routing area is `project/system/instance/control/` — under `instance/`, which is authored and committed, not under `generated/`. So:

```text
BREAK-GLASS (generate-independent)
    project_anchor.json -> instance/control/ -> knowledge/

ACCELERATED (generated)
    project_anchor.json -> generated/orientation/current.json
```

R257 does not state that the generated orientation is an accelerator rather than a required hop. Since AO-5 makes independent recovery a requirement rather than a nicety, the omission is an unmet accepted requirement, not a stylistic gap.

**Amendment:** state that generated orientation is never a required hop, and that break-glass resolves anchor → `instance/control/` → knowledge with no generated input. **Before the representation stage**, because the representation of `instance/control/` must support being read without the generator.

The human path is better off than the machine path: §7.1 already requires the root README to link to `project/README.md` and `project/knowledge/README.md` alongside the generated orientation, so no single point of failure exists there.

### 8.2 CL — anchor staleness has no detector

`project_anchor.json` holds locators. If paths move — and R8 exists precisely to move paths — the anchor goes stale silently. It should be validated by a deterministic check in `project/engineering/checks/`, in the same class as the existing routing-consistency guard. **CLARIFY.**

### 8.3 Hop gates otherwise met

§7.3's mapping against A5 is sound and the counts are right. **KEEP**, subject to §7.3's own caveat that exact link qualification must be executed before path freeze.

## 9. H. Hidden representation assumptions

This is the brief's central task, so I want to separate serialization defaults from architectural lock-in carefully.

```text
project_anchor.json          SERIALIZATION DEFAULT, minor name coupling
    JSON for a tiny machine anchor is the right default. The only
    architectural cost is that the format is in the filename (§2.4).

contracts/schemas/           SERIALIZATION-SUGGESTIVE, low risk
    "schemas" implies JSON Schema, which is what exists. Compatible with
    any representation, since even a DB-backed system has schema files.

instance/policy/
instance/control/
instance/captures/           DIRECTORY RESERVATION, PARTLY PREJUDGING
    Three directories for three logical classes presume each is
    directory-resident. If representation selects SQLite for control
    state, instance/control/ holds one file and the directory is
    vestigial; if it selects an event log, likewise. Harmless in
    outcome, but R257 claims to defer representation and these paths
    quietly assume a file-shaped world.

generated/                   LOW RISK, same reasoning

generated/orientation/
    current.md
    current.json             TWO EXPLICIT FORMAT CHOICES
    This is the clearest instance. R257 §1 and §11 defer representation,
    and §7 then selects Markdown for human orientation and JSON for
    machine orientation. Both are sensible defaults. They are still
    representation decisions made inside a document that says it is not
    making them.

one Python package for JW1   MILD, and partly unavoidable
    Commits project-control implementation to Python. Low risk given the
    project's language, but "one Python workspace" and "one Python
    package" are different commitments and §3.2 elides the difference.

one shared Git repository    NOT A NEW PREJUDGMENT
    Already accepted under G-DUAL and PSMF materialization. KEEP.
```

**Verdict: PARTLY.** Nothing here disables a later representation choice. But R257 should add one sentence — *these paths name responsibility areas; whether each holds many files, one file, or one database is a representation-stage decision* — and should label the two orientation extensions as provisional defaults. **CLARIFY, not AMEND**, because the brief correctly says not to amend for matters belonging to the next stage; the only ask here is honest labelling of what has already been chosen.

## 10. I. Workspace and dependency coupling

Covered as AM-1 in §2.2. Summarizing the assessment the brief asks for:

```text
one repository-level uv workspace        AMEND — the coupling it creates is
                                         the one R8-A newly introduces, and
                                         G1 evidence argues against it

root orchestration pyproject.toml        KEEP for repository-wide TOOL
                                         config; drop workspace membership

one shared uv.lock                       AMEND — not separable from the
                                         workspace decision under uv

separate product/runtime/pyproject.toml  KEEP
separate project/system/pyproject.toml   KEEP
independent Node under interaction/web/  KEEP — correct, and §13's refusal
                                         to create a root npm workspace for
                                         a single JS package is right
```

Long-term extraction cost is the deciding factor: under PSMF, `project/system/` must eventually be materialized from and upgraded against an upstream. A shared resolution makes every upgrade a Product-plane event.

## 11. J. Migration feasibility

R257 is not a manifest, so I tested absorbability rather than sequence.

```text
src/           -> product/runtime/src/            clean
migrations/    -> product/runtime/                clean; alembic.ini moves with it
frontend/      -> product/interaction/web/        clean for promoted implementation;
                                                  the design-lab/history split is
                                                  deferred, which is correct
tools/PK/      -> project/system/src/...          clean in principle; module mapping
                                                  depends on AM-5
schemas/PK/    -> project/system/contracts/schemas/  clean
scripts/       -> four-way split                  HIGHEST AMBIGUITY, depends on AM-3
tests/         -> five-way split                  same dependency
experiments/   -> project/research/               depends on AM-4's disposition rule
prototype_v0/  -> project/reproductions/          depends on AM-4b's admission gate
docs/          -> knowledge + system              LARGEST REFERENCE SURFACE
```

**The reference-instability risk is concentrated in `docs/`,** and R257 §15's falsifier list does not include it. Every collaboration trigger, every checkpoint cross-reference and every research citation in this repository points at `docs/...`. In MC-0023 I raised this as guardrail G7-4; it should be restated at R8-A level as an explicit migration obligation rather than discovered during the manifest.

**Does any migration cost signal a wrong ownership boundary?** No. The `scripts/` and `tests/` ambiguity signals an *underspecified* boundary (AM-3), not a wrong one — and §4.1's PSMF argument shows the boundary is right. That is the honest distinction the brief asks for.

**Temporary-becoming-permanent risk:** one instance, AM-7's `migration/` module.

## 12. K. Strongest alternative

The strongest alternative is not a different tree. It is **R8-A with independently resolved plane workspaces** — the AM-1 variant:

```text
root/
    .github/  .gitignore  README.md  project_anchor.json
    pyproject.toml        (tool configuration only)
    product/  project/

product/runtime/     pyproject.toml + uv.lock + .python-version
project/system/      pyproject.toml + uv.lock + .python-version
```

Root drops to 7–8 entries. Coupling at the resolution layer disappears. PSMF upgrade becomes a single-plane event. The cost is two installs and integration-time rather than resolution-time discovery of cross-plane incompatibility.

I considered two more radical alternatives and both lose:

```text
JW1 at root as a third top-level
    Argument: it governs both planes, so it is not a sibling of either.
    Loses: rejected as a third plane by Research 249 §8 and by my own
    MC-0023 §5 — every candidate third plane is a lifecycle stage or a
    cross-cutting owner within a plane, not a peer of "the thing built"
    and "the activity of building it."

merge engineering/ into system/
    Argument: resolves AM-3's ambiguity by eliminating the boundary.
    Loses: engineering is permanently ADS-specific and never extractable;
    system is PSMF-materializable. Merging places non-extractable code
    inside the materialized framework. This is the decisive argument and
    it turns AM-3 from "maybe wrong boundary" into "right boundary,
    missing rule."
```

## 13. Findings by classification

```text
KEEP
    nine-entry root structure and the A2 responsibility mapping
    zero A1 root integration contracts
    Product/Project plane realization
    six context-first runtime modules
    interaction/ as a classification level
    five first-level Project areas
    six operations/engineering subareas and bound 8
    JW1 as one workspace and one package
    activation/orchestration in-package, not a separate process
    independent Node package management, no root npm workspace
    hop-gate design
    AO-3 through AO-9 semantics unchanged by residency

CLARIFY
    CL-1  cross-context orchestration owner in product runtime
    CL-2  API transport module owner (resolved by AM-2)
    CL-3  one stated rename rule for both planes
    CL-4  project_anchor.json naming rationale and format coupling
    CL-5  knowledge/system reference direction
    CL-6  AO-6 policy (JW1) versus mechanics (engineering)
    CL-7  KA-R52 obligation split across governance and system
    CL-8  verification and security declarative/procedural restatement
    CL-9  anchor staleness check in engineering/checks/
    CL-10 retained-qualified versus prospective JW1 modules
    CL-11 representation-provisional labelling (§9)

AMEND — before the representation stage
    AM-1  independent plane dependency resolution; root pyproject for
          tool config only; .python-version per plane (AM-1b)
    AM-5  no empty JW1 module directories; apply §4.2's rule uniformly
    AM-6  adapters/ framework-versus-instance decision (PSMF seam)
    AM-7  migration/ permanence and naming
    AM-9  break-glass path stated as generate-independent (AO-5)

AMEND — before the file-level migration manifest
    AM-2  runtime_platform/ internal sub-boundaries (carries R250 §3)
    AM-3  engineering ↔ JW1 validator boundary and direction
    AM-4  research/ completion-disposition obligation;
          reproductions/ admission gate (AM-4b)
    AM-8  continuity/recovery naming collision

REOPEN
    none
```

No finding requires reopening an accepted R5, R6 or R7 premise. AM-1 is the largest, and it amends a realization choice R8-A made, not an architecture the owner has already accepted.

## 14. Disposition

`AMEND`. Five amendments before the representation stage, four before the migration manifest, eleven clarifications. The plane architecture, workspace count, JW1 boundary, AO residency and operations model all survive.

I want to state plainly what I am not claiming. R8-A is careful work that satisfied every amendment from MC-0023 and MC-0024 that applied to it, preregistered its bounds before populating them, and kept representation genuinely open in the places that matter most. The single substantive disagreement is AM-1, and it is a disagreement about one coupling rather than about the architecture that coupling sits inside.

```text
R8A_ADVERSARIAL_DISPOSITION: AMEND
ROOT_REALIZATION_ACCEPTABLE: YES
PRODUCT_WORKSPACE_REALIZATION_ACCEPTABLE: YES
PROJECT_WORKSPACE_REALIZATION_ACCEPTABLE: YES
JW1_BOUNDARY_ACCEPTABLE: YES
AO_RESIDENCY_ACCEPTABLE: YES
OPERATIONS_ENGINEERING_MODEL_ACCEPTABLE: YES
COLD_START_REALIZATION_ACCEPTABLE: NO
REPRESENTATION_PREJUDGMENT_FOUND: PARTLY
SHARED_PYTHON_WORKSPACE_MODEL_ACCEPTABLE: NO
OWNER_CAN_DECIDE_R8A_AFTER_CHATGPT_RECONCILIATION: YES

MC0025=ACTIVE
PRE_REPRESENTATION_AMENDMENTS=AM1_PLANE_DEPENDENCY_INDEPENDENCE, AM5_NO_EMPTY_JW1_MODULES, AM6_ADAPTERS_PSMF_SEAM, AM7_MIGRATION_MODULE_PERMANENCE, AM9_BREAK_GLASS_PATH
PRE_MIGRATION_AMENDMENTS=AM2_RUNTIME_PLATFORM_SUBBOUNDARIES, AM3_ENGINEERING_JW1_BOUNDARY, AM4_RESEARCH_DISPOSITION_AND_REPRODUCTIONS_GATE, AM8_CONTINUITY_RECOVERY_NAMING
STRONGEST_ALTERNATIVE=R8A_WITH_INDEPENDENT_PLANE_WORKSPACES
DECISIVE_EVIDENCE=RESEARCH_239_G1_LIFECYCLE_INDEPENDENCE
NEXT=CHATGPT_RECONCILIATION
```
