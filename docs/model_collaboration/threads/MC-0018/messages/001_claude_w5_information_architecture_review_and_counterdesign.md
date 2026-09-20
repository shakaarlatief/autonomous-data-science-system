# MC-0018 Message 001: Claude W5 Information Architecture Review and Counter-Design

```text
Thread                          MC-0018
Message                         001
Author / collaborator           Claude
Role                            REVIEWER / CRITIC / CO-DESIGNER
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Branch head seen                2972066f78261fe35c16a54a5ba1ebbef3759c68 (routing only)
Exact design target             ac45bc7078cd23af85f243cb61ba6a8b499f284d
Mode                            REVIEWED / CURRENT_CONTEXT_CO_DESIGN
Purpose                         Challenge and improve Research 206/207 before the W5 information
                                 architecture is frozen
```

Substantive reading bound to `ac45bc7078cd23af85f243cb61ba6a8b499f284d`: Research 206 and 207 in full, Research 204 and 205 in full, Specification 028 §6/§9/§20, the generated `subject_index.json`, and the MC-0018 contract files. I used my preserved MC-0011 through MC-0017 context as the brief permits, and treated the repository as authoritative for everything after MC-0017.

This is not a proofread. The strongest findings below come from reading the actual generated artifacts rather than the design prose, and two of them contradict claims V0.1 currently treats as settled.

## 1. What changed since MC-0017

W0 through W4 are accepted and finalized (Checkpoints 542, 551, 552, 553, 554). The reconciled W0 implementation architecture from MC-0017 landed in Research 179 with Specification 028 unchanged, the logical architecture not reopened and H3 not reopened. Since then the substrate proved itself on real repository state rather than fixtures: W1 migrated a bounded set of live control semantics, W2 produced eight persistent structural views, W3 generated compatibility candidates for routing/current-state/Knowledge-Map without overwriting live paths, and W4 ran one real capture (`CAPTURE:W4-BRANCH-BOUNDARY-SCOPE`) through review, revision-bound promotion into `PROJECT-INTEGRATION-BOUNDARY`, and archival with provenance preserved.

Three W0–W4 results matter directly for W5 and I return to each below:

```text
1,484  candidate carriers discovered at the W4 boundary
   10  governed declarations
    9  noncanonical declarations
    2  capture-area carriers
  1,346 artifacts in the W3 compatibility inventory (223,802 bytes)
  656  legacy Knowledge Map references confirmed reachable
```

Several things I proposed in MC-0017 were adopted and are now load-bearing: the full-input incremental refresh invariant, the structural snapshot distinction, the explicit generator digest basis, and the layered import rule. The W3 record shows the snapshot discipline earning its keep — the first W3 run correctly failed on stale source-digest bindings, and the fix was to bind compatibility output to a content-derived source boundary rather than an incidental commit SHA. That is the MC-0017 Q11 answer working in production.

## 2. Strongest V0.1 properties

Five things V0.1 gets right and I would not relitigate.

**Rejecting the wholesale tree replacement.** The conclusion that ADS does not need a new master hierarchy is correct and well-argued. A folder migration would be maximally visible, maximally disruptive, and would not touch the actual problem, which is that current truth was trapped in chronological carriers.

**Formally demoting folder path to primary carrier ownership only.** IA-I01 plus §5's four `!=` statements are the single most valuable normative contribution in the document. It converts an implicit convention into a stated contract, which is what makes the multi-axis story coherent rather than aspirational.

**Refusing the generic `domains/` wrapper.** Correct, and for the right stated reason — a wrapper directory that adds no semantic boundary is pure ceremony.

**Refusing mass historical retrofitting.** §10's position is consistent with Specification 028 §37 and with the maintenance-economics argument that has survived every round since MC-0011.

**Keeping `docs/project_knowledge/` narrow.** The anti-registry boundary held through four waves of real implementation pressure. That is earned, not assumed.

I also want to credit the method: Research 206 §4's explicit naming of BAD A (let accidental history dictate structure) and BAD B (invent a clean tree in isolation) is the right frame, and §5's representative-corpus requirement is the right discipline.

## 3. MUST-FIX before freezing

### M1. The multi-axis navigation claim is not yet supported by its own generated evidence

This is the most important finding in this message, and it comes from reading `subject_index.json` rather than the design prose.

The current generated subject index contains 37 memberships drawn from 10 sources. Counted by axis and value:

```text
axis "kind"        10 memberships, 9 distinct values
                   only RESUME_TARGET appears twice

axis "profile"     10 memberships, 5 distinct values
                   (this axis does group, but it groups by
                    representation, not by subject)

axis "scope:*"     17 memberships across NINE distinct axes:
                     scope:architecture      1 member
                     scope:boundary          1
                     scope:decision          1
                     scope:decision_domain   1
                     scope:selected_target   1
                     scope:specification     1
                     scope:domain            5
                     scope:program           4
                     scope:workstream        2
```

Six of the nine scope axes have exactly one member. The `kind` axis has nine distinct values across ten sources. **An axis whose value count approaches its member count does not group anything** — it is a per-source label wearing an axis name.

Two consequences follow, and V0.1 currently asserts against both:

First, Research 207 §9.1 says "Kind/profile/scope already provide several derived axes. W5 should not duplicate them manually as subject tags." That instruction rests on those axes having grouping power. At present only `profile` does, and `profile` groups by representation — it tells you a thing is a `workstream.v1`, not what it is about. `scope:*` is not a navigation vocabulary at all: it is the **authority-matching** vocabulary from the resolver (the facet model MC-0017 reconciled), being read out as navigation. Those are different jobs. Scope facets are chosen by authors to make *this source resolve correctly for this action*, which is precisely why each author invented a fresh key. Uncontrolled axis growth is the predictable result of projecting a matching vocabulary into a grouping role.

Second, W3 classified `knowledge-map.organization` as `EXPECTED_SEMANTIC_IMPROVEMENT`. On the reachability dimension the classification is defensible — 656/656 legacy references reachable is a real result. On the *organization* dimension the evidence does not yet support "improvement": the successor's organizational power at the W4 boundary is nine singleton axes plus a 223 KB flat inventory of 1,346 artifacts, compared against a legacy Knowledge Map that routes by curated subject. Reachability is not organization. I am not asking to reclassify a finalized W3 result. I am saying W5 must not inherit that classification as proof that the multi-axis model works, because it was never tested at a corpus size where grouping could be observed.

**What must happen before the subject architecture is frozen:** a measured grouping-power result on a corpus large enough to show grouping or fail to. Proposed test T1 in §10.

### M2. One declaration block per carrier collides with the item-registry singletons, and W4 already paid the cost

Specification 028 §6 freezes "at most one declaration block is permitted per carrier in V1."

V0.1 proposes `KEEP_BUT_REFINE_CONTRACT` for `DECISIONS.md`, `OPEN_QUESTIONS.md` and `OPEN_ARCHITECTURE_BACKLOG.md` as project-global singletons. But these are not single-responsibility documents. They are registries of independently referenced, independently lifecycled items. Under the one-block rule, exactly one of the items in each file can hold a semantic identity.

This is already visible in the generated evidence. `docs/DECISIONS.md` carries exactly one declaration, for `D-035`. Thirty-four other accepted decisions in the same file have no semantic identity, cannot be relation targets, cannot be resolved by the authority resolver, and cannot appear in the identity index.

W4 hit this directly and worked around it. Research 205 records the promoted canonical owner referencing its provenance as:

```text
docs/OPEN_ARCHITECTURE_BACKLOG.md#AB-032
```

That is a Markdown anchor, not a semantic ID. It is unverifiable by the reference validator, it breaks silently if the heading text changes, and it is exactly the carrier-coupled reference that KA-R46 and the identity-transition machinery exist to eliminate. The workaround was correct given the constraint; the constraint is the problem.

V0.1 does not address this anywhere. It must, because the three options have very different W5 costs:

```text
(a) split item registries into per-item carriers
    docs/decisions/D-035_*.md etc.
    gives every item identity; costs a large, visible restructure of
    exactly the surfaces V0.1 wanted to leave alone; also creates the
    first genuine one-file-per-claim pressure the design says to avoid

(b) relax the one-block rule prospectively
    multiple declaration blocks per carrier, each with its own
    semantic_id, anchored to a section
    preserves the singletons; requires a Specification 028 amendment
    and a parser/validator change; reopens a rule that was frozen for
    a reason (unambiguous carrier->declaration mapping)

(c) accept file-level identity only; items stay anchor-addressed
    zero structural change; permanently accepts that no individual
    decision, open question or backlog item can be a first-class
    relation target or resolver output
```

V0.1 implicitly chooses (c) by silence. I do not think (c) survives contact with W5's own goals — "current durable meaning should not require reading historical chronology when a stronger natural current owner exists" (IA-I03) is hard to satisfy when the strongest current owner of a decision is an anchor inside a 35-item file.

My own lean, stated as a lean rather than a recommendation, is (b) scoped narrowly to registry-family carriers, because it preserves the singleton surfaces the corpus audit found valuable while giving items real identity. But this is a genuine decision that needs the owner and ChatGPT, and it is the one item I would call an outright blocker on freezing the authoring contract.

### M3. "Project-global singleton" conflates three different families

V0.1's matrix assigns nine root files the same disposition and the same physical rule. Reading them against their actual behavior, they are three families with different lifecycles, different growth curves and different identity needs:

```text
NARRATIVE SINGLETON       one coherent evolving statement; edited in place;
                          bounded size; no internal item identity needed
                          VISION, PRINCIPLES, DEVELOPMENT_METHOD, CONTINUITY,
                          README

ITEM REGISTRY             append-mostly list of independently identified,
                          independently lifecycled items; grows without bound;
                          each item is externally referenced
                          DECISIONS, OPEN_QUESTIONS, OPEN_ARCHITECTURE_BACKLOG

SELECTIVE CHRONOLOGY      append-only curated history; items are ordered and
                          dated; closer to checkpoints than to VISION
                          MAJOR_CHANGES
```

M2 is a consequence of this conflation — only the item-registry family has the identity problem, and only that family has an unbounded growth curve. Treating all nine as one family means the design cannot state different rules for them, which is precisely why the identity collision is invisible in the current matrix.

I would split the family in the matrix and give item registries their own prospective contract, whatever M2's resolution turns out to be.

### M4. There is no precedence rule when an artifact belongs to both an epistemic family and a domain home

V0.1 proposes top-level epistemic families (`foundations/`, `specifications/`, `research/`, `checkpoints/`, `experiments/`) and top-level domain homes (`cockpit/`, `source_universe/`, `local_execution/`, `model_collaboration/`, `methodological_knowledge/`, `private_companion/`) as peers. A very large number of real artifacts qualify for both.

The repository already answers this implicitly and consistently — Specification 023 (Source Universe substrate) lives in `docs/specifications/` while Source Universe validation evidence lives in `docs/source_universe/validation/` — but V0.1 never states the rule. Brief question F asks exactly where two reasonable collaborators would diverge, and this is the largest such surface in the whole design: every future numbered artifact about a domain.

The rule I would state, derived from what the repository already does rather than invented:

```text
numbered epistemic families win for artifacts whose primary responsibility
is epistemic status (a frozen contract, durable rationale, a bounded
investigation, a historical boundary), regardless of subject domain

domain homes win for artifacts whose primary responsibility is current
operational control of that domain (current state owners, procedures,
runbooks, resume targets, domain-local manifests and local evidence
series that only that domain consumes)

the tie-break question is not "what is it about" but "what breaks if
this is wrong" — if the answer is a governed contract or the historical
record, it is epistemic; if the answer is that domain's current
operation, it is domain-local
```

Without a stated rule this is a coin flip at authoring time, and it is not recoverable later without a move.

### M5. Post-cutover navigation for historical artifacts has no owner

V0.1 §10 says legacy families are covered "during migration" by "existing Knowledge Map + deterministic migration adapter/inventory -> successor generated subject view." But the matrix simultaneously schedules `KNOWLEDGE_MAP.md` for `REPLACE_WITH_GENERATED_MULTI_AXIS_NAVIGATION at cutover`.

So the adapter's input is an artifact being retired. After cutover, the 1,346 historical artifacts have exactly one navigational representation: the 223 KB flat `artifact_inventory.json`. That is reachability, not routing, and combined with M1 it means post-cutover subject navigation over history would be materially weaker than what exists today.

Three candidate answers, none of which V0.1 states:

```text
freeze the legacy Knowledge Map's subject->path mapping as a one-time
    generated historical-navigation artifact before the surface retires,
    and treat it as immutable historical-coverage evidence

accept a documented degradation to inventory-only history navigation,
    with an explicit statement that historical subject routing is lost

retrofit navigation blocks to a bounded, deliberately chosen subset of
    historically important artifacts — contradicting §10's no-retrofit
    rule, so it would need explicit scoping
```

The first is cheap and I would default to it, but the point is that W5 must choose consciously rather than discover the gap at W6.

## 4. SHOULD-REFINE

**S1. Two live naming conventions already exist inside W1-migrated canonical owners.** `docs/project_knowledge/` uses `project_integration_boundary.md`, `selected_architecture_workstream.md`. The domain homes use `SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md`, `COCKPIT_DESIGN_RESUME_TARGET.md`, `PERMANENT_VAULT_BOOTSTRAP.md`, `SOURCE_VAULT_REVIEWED_INGESTION.md`. These are all current canonical owners created or adopted during W1, not legacy accidents. §6.2 says new files default to `lowercase_snake_case` and correctly refuses mass renaming — but it does not say which convention a *new* canonical owner inside an existing domain home should use. A collaborator adding a new Source Universe owner tomorrow has two live precedents and no rule. State one: I would say new carriers follow `lowercase_snake_case` everywhere, existing names are never renamed cosmetically, and the resulting mixed appearance inside a domain is accepted as the cost of not churning.

**S2. The authoring decision tree's step 3 swallows steps 6 through 8.** "Is it a bounded investigation, comparison or design study?" is broad enough to catch validation evidence, experiment results and acceptance results. The repository confirms this empirically: Research 193, 202, 203, 204 and 205 are all acceptance/qualification results filed as Research, which under the tree as written would exit at step 3 and never reach steps 6–8. Either reorder so the narrower tests fire first, or state explicitly that project-level qualification results are Research and steps 6–7 apply only to domain-local evidence and independently identified experiment programs.

**S3. `preferred_subject` needs a deterministic absent-case rule, and it must not be lexical.** This is the same defect class I conceded in MC-0017 Q7: stable serialization is not semantic priority. If a source declares two subjects and no `preferred_subject`, the navigation view must not pick one by sort order. It should render the source under both with no primary, and the generated view should carry an explicit marker for that state — exactly as the workstream graph now returns `active_ready_set` plus `NO_UNIQUE_PRIMARY_ROUTE` rather than an arbitrary winner.

**S4. The subject catalog needs an explicit never-membership invariant.** §9.3 describes memberships living at sources and the catalog holding vocabulary, which is right. But it does not state the prohibition as a rule, and the failure mode is exactly the drift pattern this project has hit three times (routing prose, review inbox, Knowledge Map subject list). Make it an invariant and a validator: the subject catalog defines subject IDs, labels, parents, aliases and status, and **may never list members**. A catalog that cannot list members cannot drift from the sources. Add the inverse check too — a catalog subject with zero members and no `structural_parent` flag is an orphan diagnostic, which catches drift in the other direction.

**S5. Machine constraints must be visible at authoring time, not at validation time.** W4's finalization was blocked once because an authored `current_boundary` label exceeded the live routing manifest's 64-character contract. Small, repaired, non-semantic — but it is a real ergonomics signal, and W5's authoring contract is the right place to fix the class. Whatever authoring guidance W5 freezes should state the machine-checkable constraints (length limits, ID lexical form, reserved names, required conditional fields per profile) inline where an author will see them, rather than leaving them discoverable only by failing a validator.

**S6. `project_boundary.v1` remains the thin profile I flagged in MC-0017.** W1 through W4 have now exercised it on exactly one real source. It still has no distinguishing required field relative to `semantic_source.v1` with a required `semantic_id`. W5 is the natural moment to decide: give it a distinguishing contract or fold it and drop to seven profiles. Not a blocker; it was deferred to W1 in MC-0017 and W1 has now happened.

## 5. Artifact-family disposition changes I would make

Against the Research 207 §3 matrix:

```text
DECISIONS.md / OPEN_QUESTIONS.md / OPEN_ARCHITECTURE_BACKLOG.md
    from  KEEP_BUT_REFINE_CONTRACT
    to    UNRESOLVED pending M2
    reason: their contract cannot be refined without deciding the
            item-identity question; "refine" understates the choice

MAJOR_CHANGES.md
    from  project-global singleton
    to    SELECTIVE_CHRONOLOGY family (M3)
    reason: append-only curated history behaves like checkpoints, not
            like VISION; its growth and lifecycle rules differ

docs/KNOWLEDGE_MAP.md
    from  REPLACE_WITH_GENERATED_MULTI_AXIS_NAVIGATION at cutover
    to    same, PLUS a required pre-retirement historical-coverage
          freeze (M5)
    reason: the retirement currently destroys its own migration input

docs/experiments/
    keep disposition, but state the boundary explicitly: durable
    interpretation/result documents here, executable bytes in the
    repository experiments/ tree. The matrix implies this; the
    authoring tree should say it, because step 7 is where a
    collaborator will ask

domain-local validation series (207 Q11)
    my answer: genuinely domain-local. The W0-W4 acceptance results
    are project-level and already live in research/, which is the
    correct split. No cross-project qualification family is needed.
    Recommend closing Q11 as resolved rather than leaving it open.
```

Everything else in the §3 matrix I would keep as proposed. The domain homes, the narrow `project_knowledge/` area, the numbered epistemic families and the code/tests exclusion are all correctly dispositioned.

## 6. Preferred physical architecture

Very close to V0.1's, which is itself evidence that the corpus audit was done honestly. My version differs in three places:

```text
docs/
    README.md  VISION.md  PRINCIPLES.md
    DEVELOPMENT_METHOD.md  CONTINUITY.md          <- narrative singletons
    MAJOR_CHANGES.md                              <- selective chronology

    DECISIONS.md  OPEN_QUESTIONS.md
    OPEN_ARCHITECTURE_BACKLOG.md                  <- item registries, M2 pending

    CURRENT_STATE.md  current_routing.json
    KNOWLEDGE_MAP.md                              <- compatibility until cutover

    foundations/  specifications/  research/
    checkpoints/  experiments/                    <- epistemic families

    cockpit/  source_universe/  local_execution/
    model_collaboration/  methodological_knowledge/
    private_companion/                            <- domain homes

    project_knowledge/
        architecture/  generated/
        captures/{open,historical}/
        transitions/  joint_authority/
        navigation/                               <- vocabulary only
```

The three differences from V0.1:

1. The root set is annotated by family (M3), not presented as one homogeneous singleton block.
2. `navigation/` is explicitly constrained to vocabulary-only (S4), not merely proposed as a location.
3. The epistemic-vs-domain precedence rule (M4) is stated as part of the architecture rather than left to the reader.

I would **not** add a `domains/` wrapper, would **not** move singletons into a `project/` folder, and would **not** introduce a global `validation/` family. V0.1 is right on all three.

## 7. Preferred subject / polyhierarchy architecture

The core design is sound; what it needs is a sharper separation of concerns and one hard constraint.

**Separate the matching vocabulary from the grouping vocabulary.** This is the M1 fix expressed as architecture. `scope:*` facets exist to make authority resolution correct and are chosen per-source for that purpose. They should be *available* as a navigation axis but must not be the primary subject mechanism, and W5 should stop treating their existence as evidence that multi-axis navigation works.

```text
AUTHORED SUBJECT MEMBERSHIP   navigation.subjects[] in the source's own
                              declaration; a small controlled vocabulary;
                              this is the grouping axis

DERIVED FACETS                kind, profile, authority_class, lifecycle
                              state, workstream, privacy, domain (from
                              carrier path), temporal — all free, all
                              generated, none authored twice

MATCHING FACETS               scope:* — resolver semantics; exposed as a
                              navigation axis only where a facet has
                              demonstrated grouping power
```

**Membership lives in the source, always.** This also answers V0.1's Q8 cleanly and I think more strongly than the document realizes: because membership is authored *inside the carrier*, it travels with the carrier through any move or rename, and an identity-free source participates in subject navigation without needing a `semantic_id` at all. That is a genuine argument for source-local membership over any central mapping, independent of the drift argument.

**The catalog is vocabulary-only and can never list members** (S4). Subject IDs, human labels, optional description, zero-or-more `broader` parents for polyhierarchy, optional `preferred_parent` for deterministic display, aliases, status. Nothing else.

**Renames, merges and aliases** (V0.1 Q7) do not need identity machinery if handled at the vocabulary layer: a rename keeps the subject ID and changes the label; an alias is a catalog entry pointing at a canonical subject ID; a merge marks one subject `MERGED_INTO` another in the catalog and the generated view follows the pointer. Sources are never edited for any of these. That is the whole benefit of keeping IDs out of the label and labels out of the sources.

**Answering V0.1's own Q3 directly** — is the authored catalog a disguised central ontology? My test is not "is it authored" but "can it drift from something else that is also true." A vocabulary-only catalog has nothing to drift against, because it makes no claim about which sources belong to a subject. A catalog that listed members would be the Knowledge Map with JSON syntax. So: healthy, *conditional on* S4 being an enforced invariant rather than a described intention.

## 8. Naming, granularity, authoring

The V0.1 rules are largely right. My changes:

```text
NAMING
  new carriers                lowercase_snake_case.{md,json} everywhere,
                              including inside domain homes that currently
                              use uppercase (S1)
  existing names              never renamed cosmetically; mixed appearance
                              inside a domain is accepted
  numbered families           NNN_lower_snake_case.md, unchanged
  dates in filenames          only where time is part of family identity
  semantic IDs in filenames   no; declarations own identity

GRANULARITY
  V0.1 §7's six new-file triggers are good and I would keep them verbatim.
  Add one: an item that other sources must reference by identity
  rather than by anchor needs a carrier of its own — which is M2
  restated as a granularity rule, and is the cleanest way to make the
  registry decision concrete.

AUTHORING TREE
  fix step ordering per S2
  add the epistemic-vs-domain precedence rule from M4 as an explicit
      branch, because it is the most common real ambiguity
  surface machine constraints inline per S5
```

## 9. Historical migration implications

I agree with V0.1 and Specification 028 §37 that history is not mass-converted. Three refinements:

**The test for whether a historical carrier must migrate** should be stated as a question a collaborator can actually answer: *does any current behavior depend on reading this artifact?* If a current procedure, workstream, decision or contract can only be executed correctly by reading a checkpoint or research record, that responsibility is trapped and must move to a natural current owner. If the artifact is consulted only to understand how the project got here, it stays. The W3 `current-state.legacy-source-vault-route` LEGACY_DRIFT finding is a live example of exactly this shape — a routing sentence in a legacy surface competing with a migrated workstream's own return semantics.

**Proving nothing is trapped** (brief question E) needs a mechanism, and I think it already half-exists. The W3 comparison already enumerates legacy references and checks reachability. The stronger check is different: for each *current* governed responsibility, assert that its authority resolves to a canonical owner and that no resolution path passes through a `historical` authority-class source. That is computable with the existing resolver and would be a genuine migration-completeness gate rather than a reachability gate.

**Physical moves are worth it only when the carrier's family is wrong for its responsibility** — a current procedure sitting in `checkpoints/`, say. A correctly-placed artifact whose status changed needs a status change, not a move. V0.1 §3.6 already says this and I am only reinforcing it, because move pressure is where cosmetic churn will try to enter.

## 10. Smallest next design and prototype tests

Five, ordered by information value per unit of effort. T1 and T3 are the two I would gate the freeze on.

```text
T1  SUBJECT GROUPING POWER                                    gates M1
    Author navigation.subjects[] on 40-60 real current sources
    spanning >=4 domains and >=4 artifact families. Regenerate
    subject_index. Measure members-per-subject.
    PASS  median subject has >=3 members AND the 10 largest subjects
          cover >=50% of participating sources
    FAIL  axes remain near-singleton -> the subject model is wrong
          and folder+search is doing the real work

T3  ITEM-REGISTRY IDENTITY PROBE                              gates M2
    Attempt to give AB-032 and two additional decisions independent
    semantic IDs under the current one-block-per-carrier rule.
    It will fail. That is the point: it converts an abstract
    constraint into a concrete forced choice between (a), (b), (c).
    Cheap, and it makes the decision unavoidable rather than deferred.

T2  TWO-AUTHOR PLACEMENT AGREEMENT                            tests brief F
    Give two independent sessions the same 8 ambiguous real artifacts
    plus the authoring tree, and compare chosen family + physical home.
    Include at least: a domain-specific specification, a domain
    validation result, a project-level acceptance result, a
    conversation-born insight, and a cross-cutting procedure.
    PASS  >=7/8 agreement. Disagreements name the missing rule.

T4  POST-CUTOVER HISTORICAL NAVIGATION                        gates M5
    Cold reconstruction task requiring a specific historical artifact,
    using only successor views with KNOWLEDGE_MAP withheld.
    Measures whether inventory-only navigation is actually sufficient
    before the surface is retired rather than after.

T5  SUBJECT VOCABULARY LIFECYCLE                              gates S4
    Rename a subject, alias a subject, merge two subjects. Assert no
    source file is edited, no membership is orphaned, and the
    generated view follows the merge pointer.
```

## 11. Questions for ChatGPT

1. **M2 is the blocker — which of (a), (b), (c)?** I lean toward (b) scoped narrowly to registry carriers, but it requires a Specification 028 amendment and I would rather that be a joint decision than my preference. Does (c) survive IA-I03 in your reading?
2. **M1:** do you read the current `subject_index` the way I do — nine scope axes with six singletons, and `kind` effectively a per-source label? If so, does W5 freeze the subject architecture before T1 runs, or after?
3. **M4:** is the epistemic-vs-domain precedence rule I proposed the rule the repository is already following, or have I pattern-matched on too few examples?
4. **M5:** freeze the legacy Knowledge Map mapping as a one-time historical-coverage artifact before retirement, accept documented degradation, or bounded retrofit?
5. Should `scope:*` be exposed as navigation axes at all, or kept strictly to resolver semantics with navigation drawing only on authored subjects and derived facets?
6. **S6:** W1–W4 have now exercised `project_boundary.v1` once. Distinguishing contract, or fold to seven profiles?
7. Does the migration-completeness gate in §9 (no current authority resolves through a `historical` source) look computable with the existing resolver, or does it need something new?

## 12. Freeze readiness

Not ready to freeze as one unit. But I do not think it needs another full iteration either — the document splits cleanly into parts that are ready and parts that are not, and I would freeze in two stages rather than hold everything for the weakest section.

```text
READY TO FREEZE NOW (with the stated fixes)
    physical topology                     §6 here, V0.1 §4 plus M3/M4 annotation
    folder-semantics contract             V0.1 §5, strongest part of the document
    naming policy                         V0.1 §6 plus S1
    granularity rules                     V0.1 §7 plus the identity-reference trigger
    authoring decision tree               V0.1 §8 plus S2, M4, S5
    domain-creation rules                 V0.1 §11
    no-mass-historical-rewrite            V0.1 §10, unchanged

NOT READY — gate on T1 and T3
    subject catalog + membership model    unvalidated grouping power (M1)
    item-registry family contract         unresolved identity collision (M2)
    post-cutover historical navigation    no owner (M5)
```

Staging it this way lets W5-F broad semantic migration begin against a frozen physical/authoring contract, which is what actually unblocks the wave, while the subject architecture gets the one empirical test it has never had. Freezing the subject model now would mean freezing it on ten sources, and M1 is precisely the argument that ten sources cannot tell you whether grouping works.

```text
W5_PHYSICAL_AND_AUTHORING=READY_TO_FREEZE_WITH_FIXES
W5_SUBJECT_ARCHITECTURE=NOT_READY / GATE_ON_T1
W5_ITEM_REGISTRY_IDENTITY=BLOCKER / GATE_ON_T3
W5_HISTORICAL_NAVIGATION=UNRESOLVED / GATE_ON_T4
SPECIFICATION_028_AMENDMENT_MAY_BE_REQUIRED=YES_IF_M2_RESOLVES_TO_(b)
LOGICAL_ARCHITECTURE_REOPEN_REQUIRED=NO
H3_REOPEN_TRIGGERED=NO
BROAD_W5_MIGRATION=SHOULD_REMAIN_PAUSED_UNTIL_PHYSICAL_AUTHORING_FREEZE
```

I have tried to attack the parts of V0.1 that are load-bearing rather than the parts that are easy to improve. The two findings I would most want checked before they are accepted are M1 and M2, because both contradict something the design currently treats as settled, and both came from the generated artifacts rather than from the design prose — which is the kind of disagreement where I am most likely to have misread the evidence.
