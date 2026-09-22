# MC-0024 Message 001: Claude Comparative Review of Research 218 Versus R7 Target Information Architecture

```text
Thread                          MC-0024
Message                         001
Author / collaborator           Claude
Role                            COMPARATIVE ARCHITECTURE REVIEWER
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Branch head seen                fed9fb95a2d5ec8f367c936f7476d88ed11f128e (routing/thread files only)
Exact review target             b0ff5c59411b2fae2786a87d6b93ea722e7cdfe5
Reviewed                        Research 206, 208, 212, 214, 217, 218; Research 240, 246, 248, 249,
                                 250, 251, 252, 253, 254; Research 237, 239; MC-0018 and MC-0023
                                 collaboration records
Mode                            COMPARATIVE_ARCHITECTURE_REVIEW / owner decision on R254 pending
```

I participated in the design path under review. MC-0018 shaped Research 208 and Research 218; MC-0023 produced the A1/A2 amendments that Research 248–250 implemented. Where my own prior contribution is part of what I am now assessing, I say so rather than reviewing it as though it were someone else's.

## 1. The short answer before the detail

Research 218 was not weak work. It answered a different question, well, and its most valuable results survive into Research 254 intact.

The honest causal story is roughly:

```text
~50%   the question changed     docs/ organization -> whole repository
~20%   the owner changed the objective  R246 from-scratch clarification
~15%   genuine architectural correction  level-mixing in 218's tree is real
~10%   method change            audit-first -> derivation-first
~5%    residual anchoring       real, methodological, and bounded
```

Those percentages are a summary of judgment, not a measurement, and I would not defend the exact numbers. The ordering I would defend.

Research 254 is materially better as a target, and it contains two defects that will produce wrong R8 output if they are not fixed first. My disposition is AMEND, not ACCEPT and not REOPEN.

## 2. A. Why the architectures are so different

### 2.1 The dominant cause is scope, and it is legitimate

Research 218's frozen tree is **entirely under `docs/`**. It contains no `tools/`, no `schemas/`, no `src/`, no root. That is not an oversight; it is the boundary of the question it was asked.

Research 237 §2.4 confirms this from the audit side:

> The design question was repeatedly framed as the future **repository** information architecture for ADS.

— meaning *within* the repository's existing shape. Research 218 never asked whether `docs/` should be the universal Project-information root, because "organize the knowledge inside `docs/`" was the task. Research 240 then changed the task to the whole repository.

When the question moves from "organize `docs/`" to "organize the repository," a `docs/`-rooted answer is necessarily superseded — not because it was wrong, but because its root was given rather than chosen. This is the single largest cause of the difference and it implies nothing bad about Research 218.

### 2.2 The owner clarification changed what counts as a valid answer

Research 246 §2 is a genuine change in design objective, not a restatement:

```text
Research 208 §2.3   epistemic families "remain justified"
Research 208 §2.4   domain homes "remain valid"
Research 246 §2     nothing below Level 1 is protected merely by existing
```

Under 208's objective, "this family already exists and encodes a real role" was a sufficient answer. Under 246's, it is not. That alone would produce a different output on identical evidence.

### 2.3 The method changed, and method change alone moves the answer

```text
Research 206/207/208    AUDIT-FIRST
    representative corpus audit
    -> family/disposition matrix over CURRENT units
    -> KEEP / KEEP_BUT_REFINE / REPLACE / SPLIT

Research 249/250/253/254  DERIVATION-FIRST
    responsibilities (J01-J12)
    -> bounded contexts (JC1-JC6)
    -> information classes (I1-I7)
    -> physical hierarchy
```

These methods differ in what they *can* output, not only in what they did output. I develop this under F, because it is the substance of the anchoring question.

### 2.4 There is a genuine architectural correction, independent of scope

Research 254 §22's diagnosis is accurate and would hold even if the scope had never changed:

```text
docs/research/            epistemic stage
docs/cockpit/             subsystem / domain
docs/project_knowledge/   infrastructure
docs/DECISIONS.md         governance registry
docs/KNOWLEDGE_MAP.md     compatibility surface
```

Five different kinds of thing as physical peers at one level. That is level-mixing, and Research 218 froze it. Research 208 §2.2 partially saw it — it split the root singletons into narrative / item-registry / selective-chronology / compatibility roles — but it stopped at the root *files* and never applied the same analysis to the root *directories*.

So a real correction exists. It is not the largest cause, but it is not zero.

### 2.5 What did NOT cause the difference

**Migration conservatism did not.** Research 208 §2.2 states plainly, "This is a semantic role split. It is not a mass-move instruction," and 218 refused mass historical retrofit on maintenance-economics grounds. That was *stated policy*, argued from evidence — a deliberate choice to minimize churn, which is different from being unable to see past the current tree.

**Specification 028 did not.** Spec 028 constrains implementation paths, declaration syntax and manifest binding. It says nothing about the `docs/` hierarchy. It is not a causal factor here.

**New empirical evidence did not, in the direction people might assume.** T1, T3, T4 and C1 all *confirmed* Research 218's contracts. None of them pushed toward a different tree. Research 254 §20 retains every one of them. If new evidence had undermined 218, its semantic contracts would not have survived — and they did.

## 3. B. Was Research 218 wrong?

Assessed separately, as the brief requires.

**Internally coherent for its stated W5 problem — yes, strongly.** It froze exactly the parts that had converged and explicitly withheld freeze on the four that had not (Research 208 §1), then gated each on an empirical test. That is better discipline than most architecture work achieves, and it is the reason its contracts are reusable now.

**Too constrained by the existing `docs/` structure — partly.** See §7.

**Does the R240/R246 clarification materially change the correct design objective — yes, decisively.** This is the crux. Research 218 is not being overturned by better reasoning about the same question; it is being superseded because the question was enlarged and the constraints were released.

**What remains strong and must survive.** Research 254 §20's retain list is correct and I would not remove anything from it. Four items are load-bearing and were bought with real empirical work:

```text
controlled semantic subjects with source-owned membership
    Research 217, T1: 22/24 preferred-route agreement

selective first-class identity + one declaration per carrier
    Research 212, T3: D-011 as the primary hard case

historical navigation evidence before legacy-map retirement
    Research 214, T4: cold retrieval measured with the map withheld

narrowed per-view implementation closures
    C1, from my MC-0018 finding that all eight views shared one
    maximal closure
```

**What should be superseded.** The physical tree, exactly as §20 says. `docs/` as universal root; epistemic families and domain homes as physical peers; `docs/project_knowledge/` as infrastructure home; the prospective `docs/decisions/`, `docs/open_questions/`, `docs/architecture_backlog/` paths.

**Verdict.** Research 218 was correct for its question and is superseded by a better question. The distinction matters practically: if 218 had been *wrong*, its contracts would not transfer. They do, unchanged, which is the strongest available evidence that the two documents are answering different questions rather than the same question at different quality.

## 4. C. Is Research 254 actually better?

Per dimension, with the weak ones named.

```text
conceptual coherence            BETTER
    one question per level (R254 §22) versus five kinds of thing as peers

professional IA quality         BETTER
    responsibility-first, with artifact role one level down or in metadata

future scale                    BETTER
    §23's growth cases are answered without new root categories

human cold start                MIXED — see below

agent cold start                BETTER
    the Q1-Q8 authoring tree is more determinate than 218's, with two
    exceptions I name in §5 and §6

authority clarity               MUCH BETTER
    system/knowledge separation resolves a genuine live ambiguity

evidence/provenance separation  BETTER
    evidence/{research,qualification,provenance} is a real distinction
    that 218 collapsed into one research/ family

operational knowledge           BETTER
    218 had no operations class at all; procedures were scattered
    across domain homes and DEVELOPMENT_METHOD.md

historical preservation         BETTER IN PRINCIPLE, COSTLY IN PRACTICE
    §7.2's "primary current responsibility, not age" rule is right;
    the physical consequence is a new cost — see §6

dumping-ground avoidance        MOSTLY BETTER, one exposure at
                                operations/engineering — see §6

migration feasibility           WORSE, and honestly so
    root change + class taxonomy change + checkpoint family retirement
    + foundation family retirement, concurrently

Candidate 01 compatibility      PRESERVED
    §20 retains every semantic contract; path != identity is unaffected

PSMF compatibility              PRESERVED AND IMPROVED
    project/system/ gives the instance-policy layer one enclosing owner,
    which is the MC-0022 §7 / Research 239 §7 open question partially
    resolved

evolve without another redesign UNPROVEN — the central question
```

**Human cold start is the one dimension where 254 is not clearly better.** Compare depth-to-document:

```text
Research 218     docs/foundations/014_knowledge_preservation.md        2 levels
Research 254     project/knowledge/governance/architecture/rationale/  5 levels
```

Depth is a genuine cold-start cost, and Research 254 does not measure or budget it. This is not a reason to reject the hierarchy — deep trees with good signposting outperform shallow mixed ones — but it is a real trade that the document presents as costless. I recommend a measurement gate rather than a redesign (§9, A-5).

**"Evolve without another disruptive redesign" is the question the owner is actually asking**, and R254 cannot answer it by assertion. What it *can* offer is a structural argument: a hierarchy derived from *responsibilities* should outlive one derived from *artifact types*, because responsibilities change more slowly than the forms their outputs take. I think that argument is correct. But I note that Research 208 §2.3 made a structurally identical claim — that its families were retained "because they encode distinct epistemic/lifecycle roles, not merely because the legacy repository already has those directories" — and that claim did not prevent supersession two days later. An assertion of non-anchoring is not evidence of non-anchoring. §7 is about exactly this.

## 5. D. Attack on the four-class hierarchy

### 5.1 Orthogonality — three of four share an axis, one does not

```text
governance   what currently governs      authority axis
evidence     why we believe it           authority axis
history      no longer current authority authority axis
operations   how to act                  ??? 
```

Research 253 §3.3 says operational knowledge "may be operationally governing within its scope." So operations *is* governance by authority; it is separated by something else. The defensible reading — which Research 254 never states — is **declarative versus procedural**: governance records what is decided and true; operations records how to act. That is a standard and durable split (policy versus procedure), but leaving it implicit invites precisely the confusion §3.3's own sentence creates.

**This is fixable by one sentence, not by restructuring.** I recommend stating it (§9, A-4a).

### 5.2 `operations/` is the realistic dumping-ground exposure

It maps to JC4 + JC5. Research 250 §7 formed JC4 by grouping five responsibilities (J06–J09, J11) with the explicit justification that they "operate the software-development lifecycle of the repository" and "are highly coupled through CI/build/release/verification." So it is *derived*, not arbitrary — which substantially answers the brief's suspicion.

But it is the only knowledge class formed by merging two bounded contexts, and `operations/engineering/`'s stated scope (Research 254 §6.1) is the longest list in the hierarchy: repository engineering, development environments, build/CI, verification, secure development, dependency/supply-chain governance, release/change/configuration management, local/private boundaries, incident/recovery. Nine heterogeneous areas under one leaf.

Research 254 §23 says subareas may develop "only when volume/lifecycle warrants them" — a reason test with no limit test. That is the same shape I attacked in MC-0023 for the root rule, and the fix is the same: a pre-stated bound that opens an AO-4 case when crossed, rather than silent accumulation.

### 5.3 `history/` as a physical parent creates a cost 218 did not have

Research 254 §7.2 is good architecture: history receives material only when its *primary current responsibility* becomes historical reconstruction, not by age. That defuses the obvious "history is a lifecycle stage, not a parent" objection.

But it has an unstated consequence. **If class membership can change over time, then artifacts physically move between parents as they age.** Under Research 218 a research record stayed in `docs/research/` forever. Under Research 254, a research record whose responsibility becomes purely historical moves from `evidence/research/` to `history/`.

`path != semantic identity` is already frozen, so semantic identity survives the move. But every inbound *path* reference breaks, and Research 254 §18 acknowledges reference cost only for renames ("where references/history make renaming expensive"), not for lifecycle-driven relocation. Over a long project this is a recurring churn source that the four-class model introduces and the three-class alternative would not.

This is the strongest argument for the alternative in §8, and it is the single point where I think Research 254 has genuinely overreached.

### 5.4 `governance/decisions/` versus `governance/architecture/` is ambiguous in the document itself

Research 254 §8 routes checkpoint responsibilities and writes:

> owner/architecture decision boundary -> governance/decisions **or** architecture

An authoring tree that says "or" has a hole. Take a real case: **D-035**, the decision that selected Candidate 01 as the project-knowledge architecture. Is it a decision (→ `governance/decisions/`) or architecture (→ `governance/architecture/`)? Both apply, and §17's Q4 cannot separate them because both are "governs current project."

This is structurally identical to the MC-0023 A1 finding — a placement procedure with an unresolvable branch — and it should be fixed the same way, by splitting the artifact rather than arbitrating the placement (§9, A-1).

### 5.5 Are rationale/specifications grouped correctly?

Yes. `architecture/{rationale, specifications}` correctly separates *why we reason this way* from *what is contractually required*, and Research 254 §4.2's note that "a rationale record is not automatically normative implementation contract" is an improvement on the current Foundations family, where that distinction was implicit and frequently unclear.

`evidence/{research, qualification, provenance}` is also correct and is a genuine advance over 218. Research 218 had one `research/` family absorbing bounded investigations, acceptance results, adversarial reviews and provenance evidence indiscriminately — Research 193, 202–205, 239 are all "research" today despite being qualification results. §5.2's rule that "a checkpoint that primarily proves a gate belongs here rather than in one universal checkpoint family" fixes a real defect.

## 6. E. Attack on project/system versus project/knowledge

**This is durable, not a rename, and it is the strongest single improvement in Research 254.** The current `project_knowledge` name genuinely denotes two different things — the *problem domain* (all knowledge about the project) and the *implementation subsystem* (the PKA machinery). Research 254 §2's observation that "almost everything under `docs/` was project knowledge in ordinary language" is accurate, and the split resolves it cleanly.

Testing each item the brief names:

```text
generated views          system        clear, correct
current routing          system + root anchor
                                       correct; matches the MC-0023 A2
                                       cold-start-entry amendment
captures                 system        clear, correct
machine schemas          system        clear, correct
operational procedures   operations    clear, correct
collaboration state      system active / evidence or history when
                                       complete — stated in §6.2, correct

declarations             CONTRADICTION — see below
human-readable system
architecture             UNASSIGNED — see below
```

### 6.1 Declarations cannot move to `project/system/`

Research 254 §14 lists "source declarations" among things that "do **not** belong in `project/knowledge/`" and instead "belong to `project/system/`."

That is physically impossible under the governing contract. Specification 028 §6 requires at most one declaration block **per carrier**, embedded in the carrier itself. A declaration on a governance record lives inside that governance record's bytes. It cannot be relocated to `system/` without abandoning the carrier-embedded declaration model that W0–W4 implemented and qualified.

The correct statement is a three-way split:

```text
declaration INSTANCES        remain inside their carriers, wherever those
                             carriers live (Spec 028 §6)
declaration SCHEMAS          project/system/
declaration-derived INDEXES  project/system/ (generated)
```

Left uncorrected, R8 will generate a migration item that cannot be executed. This is a small defect with a concrete downstream consequence, which is why I classify it as required rather than recommended.

Note that §14's neighbouring item, "transition records used as executable control state," *is* correctly placed in system — those are standalone carriers. The error is specific to declarations, which are not.

### 6.2 Human-readable system architecture has no assigned class

Research 254 §14 ends: "Human-readable architecture/operating contracts about the system belong in Project knowledge." Which of the four classes?

Today `docs/project_knowledge/architecture/` holds six whole-architecture documents. Under Research 254 they could plausibly land in `governance/architecture/rationale/` (durable architectural reasoning), `governance/architecture/specifications/` (governed contracts), or `operations/engineering/` (how the system is operated). The document does not say, and the authoring tree's Q4 does not discriminate.

This is smaller than 6.1 — it is an unassigned case rather than an impossible one — but it affects six real current documents and should be resolved before R8 builds a disposition manifest.

## 7. F. The current-structure anchoring hypothesis

**Answer: PARTLY — and the anchoring was methodological rather than attitudinal.** This distinction matters, because it changes what the project should conclude about its own process.

### 7.1 The disclaimer was sincere and insufficient

Research 208 §2.3 states the families are retained "because they encode distinct epistemic/lifecycle roles, **not merely because the legacy repository already has those directories**." Research 208 §2.4 gives domain homes a similar justification, and explicitly rejects a `docs/domains/` wrapper "because it adds containment without a new semantic boundary" — which is genuine architectural reasoning, not inertia.

I have no reason to think that disclaimer was insincere. It was nonetheless insufficient, for a structural reason.

### 7.2 The audit-first method bounded the answer space

Research 207's method was: audit a representative corpus of current artifacts, build a family matrix, assign each family a disposition. The available dispositions were KEEP, KEEP_BUT_REFINE_CONTRACT, REPLACE, SPLIT.

Every row in that matrix was a **currently existing unit**. There was no row for a family that ought to exist but does not, and no disposition meaning "this entire level is the wrong kind of level." The method could refine, relabel, split and merge current families. It could not produce `evidence/qualification/` — a class with no current counterpart — and it could not question `docs/` itself, because `docs/` was the frame, not a row.

So the anchoring is a property of **audit-first design applied to a corpus**, not of the designers' intent. A disclaimer cannot escape it, because the constraint operates on what the method can generate, not on what the authors believe.

Research 253 §12 states the correction precisely, and it is the right one:

> physical hierarchy should first express a small number of stable information responsibility classes; artifact role is represented one level lower or through metadata where appropriate.

### 7.3 My own contribution shows the same bound

I should be explicit, because it is evidence rather than modesty. In MC-0018 Message 001 I attacked Research 207 hard — I found the subject-axis grouping failure, the item-registry identity collision, the epistemic-versus-domain precedence gap, the missing post-cutover navigation owner. Every one of those findings was a *refinement of the family matrix*. I proposed splitting "project-global singleton" into three families and adding a precedence rule between two existing family types.

I did not ask whether `docs/` should be the root. The question was not available to me inside the method I was reviewing, and I did not step outside it.

That is the cleanest available demonstration that the bound was methodological: an adversarial reviewer working the same method reproduced the same boundary.

### 7.4 What was NOT anchored

The empirical layer was not anchored at all. T1, T3, T4 and C1 tested *mechanisms* against real corpora, and their results transfer into Research 254 unchanged. Research 217's controlled-subject architecture, Research 212's selective-carrier rule, Research 214's historical-navigation evidence rule and the C1 closure narrowing are all retained verbatim by §20.

**Anchoring affected the tree. It did not affect the contracts.** That is exactly the split between what Research 254 supersedes and what it retains, which is a useful confirmation that the supersession boundary is drawn in the right place.

### 7.5 Combined answer

```text
justified evidence-based conclusion    partly — the family roles ARE real
pragmatic migration constraint         yes, and explicitly stated as policy
hidden assumption from current tree    yes, at the root and level structure,
                                       operating through the method rather
                                       than through intent
```

## 8. G. Strongest alternative

Not "retain Research 218 with amendments" — its root is superseded by a scope change that is not reversible by amendment.

The strongest alternative is **three knowledge classes with history as a state rather than a parent**:

```text
project/knowledge/
    governance/
    evidence/
    operations/

project/archive/          outside the knowledge corpus
    born-historical records (milestone snapshots)
    preserved executable historical workspaces
```

Under this variant, a research record whose responsibility becomes historical acquires a `historical` status on its existing carrier and appears in generated navigation under history; it does not move. Only artifacts *born* historical — milestone snapshots, byte-preserved prototypes — live in `archive/`.

**The discriminator is precise: should an artifact physically move when its primary responsibility changes?**

```text
if YES   four classes are right; history/ is a real parent and relocation
         is the intended expression of lifecycle transition

if NO    three classes plus status metadata is strictly more expressive,
         because status can change without breaking any inbound path
         reference, and generated navigation can present the same
         grouping without physical movement
```

My reading favours **NO**, for a reason internal to this architecture: `path != semantic identity` is already frozen, generated navigation already exists, and Research 254 §13.4 already plans a generated navigation projection. Given all three, physical relocation buys grouping that navigation already provides, at the cost of reference churn that metadata avoids.

But I do not think this difference is large enough to block acceptance, for two reasons. Research 254 §7.2's "primary current responsibility, not age" rule already suppresses most relocation. And `history/milestones/` has a genuine role for born-historical artifacts that the three-class variant also needs to place somewhere. So the variant is a refinement of the same design, not a competing one — which is why my disposition is AMEND on other grounds rather than REOPEN on this one.

## 9. Exact amendments

**Required before R8** — both produce incorrect R8 output if left:

```text
A-1  DECISION / ARCHITECTURE PLACEMENT AMBIGUITY (§5.4)

     Replace §8's "governance/decisions or architecture" with a split
     rule, following the same logic as the MC-0023 A1 outcome 1:

         governance/decisions/
             the decision RECORD — what was decided, by whom, when,
             on what evidence, with what status and supersession

         governance/architecture/
             durable architecture CONTENT — rationale that outlives the
             decision, and specifications that govern implementation

     A decision that selects an architecture produces two artifacts with
     two homes, not one artifact with an ambiguous home. D-035 is the
     worked example: the selection record goes to decisions/, and the
     durable explanation of what Candidate 01 is goes to
     architecture/rationale/.

A-2  DECLARATIONS CANNOT RELOCATE (§6.1)

     Correct §14 to state:

         declaration INSTANCES        carrier-resident, per Spec 028 §6
         declaration SCHEMAS          project/system/
         declaration-derived INDEXES  project/system/, generated

     Without this, R8's disposition manifest will contain an
     unexecutable migration item.
```

**Recommended before R8** — cheap, and each closes a gap that will otherwise be discovered later:

```text
A-3  SYSTEM-ARCHITECTURE DOCUMENT CLASS (§6.2)
     Assign the six current docs/project_knowledge/architecture/
     documents a class explicitly. My reading: durable reasoning about
     why the system is shaped this way -> governance/architecture/
     rationale/; contracts the system must satisfy ->
     governance/architecture/specifications/; how to operate it ->
     operations/engineering/. Three homes, stated, not inferred.

A-4  OPERATIONS BOUND AND DECLARATIVE/PROCEDURAL STATEMENT (§5.1, §5.2)
     (a) State the governance/operations distinction as
         declarative versus procedural, so §3.3's "may be operationally
         governing" cannot be read as overlap.
     (b) Give operations/engineering/ a pre-stated subarea bound, on the
         same model as the root's 12-entry review bound, set before the
         area is populated.

A-5  COLD-START DEPTH GATE (§4)
     Before R8 freezes paths, measure depth-to-authority for a cold
     human and a cold agent against the target tree. Not a redesign —
     a gate, with the threshold stated in advance.

A-6  LIFECYCLE-RELOCATION REFERENCE RULE (§5.3)
     Either state how inbound path references survive an artifact moving
     between knowledge classes, or narrow history/ to born-historical
     artifacts only and express lifecycle transition through status plus
     generated navigation.
```

## 10. Answers to the required questions, consolidated

**A.** Scope change dominant; owner clarification second; genuine level-mixing correction third; method change fourth; residual methodological anchoring fifth. Migration conservatism and Specification 028 were not causal. New empirical evidence pushed *toward* retaining 218's contracts, not away.

**B.** Research 218 was internally coherent and correct for its question, partly over-constrained by a root it was given rather than chose, and legitimately superseded by an enlarged objective. Its four empirically-gated contracts survive and must.

**C.** Yes, materially better on ten of thirteen dimensions, mixed on human cold-start, worse on migration feasibility, and unproven on the dimension the owner most cares about — which no architecture document can prove by assertion.

**D.** The four classes are defensible but not orthogonal on one axis; `operations/` is derived rather than arbitrary but is the realistic bucket exposure; `history/` as a physical parent introduces a relocation cost 218 did not have; and the decisions/architecture boundary is ambiguous in the document's own text.

**E.** `system/` versus `knowledge/` is genuinely durable and is the strongest single improvement. Two items in §14 are wrong or unassigned.

**F.** PARTLY, methodologically rather than attitudinally. The audit-first method could not generate families that did not already exist or question the root, and my own MC-0018 review reproduced the same bound while explicitly trying to break the design.

**G.** Three classes with history as a state, discriminated by whether artifacts should physically move as their responsibility changes. A refinement, not a competitor.

## 11. Disposition

`AMEND`. Two required amendments (A-1, A-2), four recommended (A-3 through A-6). None of them touches the four-class model, the system/knowledge separation, the information model in Research 253, or anything Research 254 §20 retains from Research 218.

I want to be clear about what I am *not* saying. I am not saying Research 254 overreaches in substance. The class model is derived, the system/knowledge split fixes a real live ambiguity, and the evidence subdivision corrects a genuine defect in the current research family. The overreach I do find is narrow and specific: making `history/` a physical parent, and retiring the checkpoint and foundation families concurrently with a root change and a taxonomy change, in a project that already has W5-F0 paused and AO-10 held.

That last point is sequencing risk rather than architectural error, and it belongs to R8.

```text
R7_COMPARATIVE_DISPOSITION: AMEND
RESEARCH218_PHYSICAL_SUPERSESSION_JUSTIFIED: YES
RESEARCH218_WAS_OVERCONSTRAINED_BY_CURRENT_TREE: PARTLY
R254_IS_MATERIALLY_BETTER_TARGET: YES
R254_OVERREACTS_TO_PRIOR_CONSTRAINTS: PARTLY
OWNER_CAN_ACCEPT_R7_AFTER_CHATGPT_RECONCILIATION: YES

MC0024=ACTIVE
REQUIRED_AMENDMENTS=A1_DECISION_ARCHITECTURE_SPLIT, A2_DECLARATION_RESIDENCY
RECOMMENDED_AMENDMENTS=A3_SYSTEM_ARCH_CLASS, A4_OPERATIONS_BOUND, A5_COLD_START_DEPTH_GATE, A6_LIFECYCLE_RELOCATION_RULE
ANCHORING_CAUSE=AUDIT_FIRST_METHOD_NOT_INTENT
STRONGEST_ALTERNATIVE=THREE_CLASS_HISTORY_AS_STATE
NEXT=CHATGPT_RECONCILIATION
```
