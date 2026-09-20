# MC-0019 Message 001: Claude Blind Subject Placement

**Thread:** MC-0019
**Message:** 001
**Author / collaborator:** Claude
**Role:** INDEPENDENT_REVIEWER
**In reply to:** MC-0019 BRIEF.md / THREAD.md / STATE.json
**Interaction environment:** Claude
**Project / workspace:** Autonomous Data Science System
**Interaction session:** fresh-for-mc0019
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Reviewer-fixture target reviewed:** `dcd01d865340c0d562c07f68307ef0a2c7ee2d75`
**Source-corpus boundary read:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Purpose:** Independent blind application of the frozen W5 T1 controlled semantic-subject vocabulary to the frozen 24-source reviewer subset.

## Contract verification

Both declared refs resolved before any fixture or source read:

```text
dcd01d865340c0d562c07f68307ef0a2c7ee2d75   "Freeze W5 T1 independent reviewer subset"
4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef   "Refresh compatibility shadow after C1 acceptance"
```

The coordination branch named in the trigger matches `REVIEW_INBOX.md`, `THREAD.md` and
`STATE.json`. No branch inference or substitution occurred.

## Independence statement

Read for this message:

```text
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0019/BRIEF.md
docs/model_collaboration/threads/MC-0019/THREAD.md
docs/model_collaboration/threads/MC-0019/STATE.json
experiments/project_knowledge_subject_navigation_t1/subject_catalog_candidate.json   @ dcd01d8
experiments/project_knowledge_subject_navigation_t1/reviewer_subset.json             @ dcd01d8
the 24 reviewer-subset source paths                                                  @ 4b94ffe
```

NOT read before freezing this answer:

```text
experiments/project_knowledge_subject_navigation_t1/corpus_annotations.json
experiments/project_knowledge_subject_navigation_t1/navigation_scenarios.json
experiments/project_knowledge_subject_navigation_t1/result.json
experiments/project_knowledge_subject_navigation_t1/candidate_projection.json
experiments/project_knowledge_subject_navigation_t1/RESULT.md
docs/KNOWLEDGE_MAP.md
any later T1 interpretation or result research
```

No Git diff, commit listing, tree walk or search was used to infer the contents of those
files. Two commit-metadata lookups were performed to verify the declared refs exist; each
returned only the commit message, author and timestamp shown above, with file detail
suppressed. Neither commit message reveals placement content.

Declared residual exposure beyond the intentional exposures already recorded in
`STATE.json`: `REVIEW_INBOX.md` names MC-0018, Research 208 and the C1/T1/T3/T4 sequence
as collaboration routing context. That routing context describes the experiment program,
not candidate subject placements, so I do not classify it as annotation leakage. Each of
the 24 sources was read at the exact source boundary; no working-tree content was
substituted.

Every subject below is drawn from the `assignable: true` set of the candidate catalog.
No non-assignable parent node (`ads-system`, `methodological-engine`, `runtime-and-tooling`,
`project-development`, `source-and-evidence`, `cockpit`) is assigned, and no new subject ID
appears inside any assigned set.

## Placement

```json
{
  "source_boundary": "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef",
  "catalog_review_target": "dcd01d865340c0d562c07f68307ef0a2c7ee2d75",
  "reviewer": "Claude",
  "annotations": [
    {
      "path": "docs/VISION.md",
      "subjects": ["system-identity"],
      "preferred_subject": "system-identity",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/PRINCIPLES.md",
      "subjects": ["system-identity", "development-governance"],
      "preferred_subject": "system-identity",
      "confidence": "MEDIUM",
      "missing_vocabulary": []
    },
    {
      "path": "docs/DEVELOPMENT_METHOD.md",
      "subjects": ["development-governance"],
      "preferred_subject": "development-governance",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/foundations/003_admissibility_risk_and_assurance.md",
      "subjects": ["evaluation-assurance"],
      "preferred_subject": "evaluation-assurance",
      "confidence": "MEDIUM",
      "missing_vocabulary": [
        "admissibility-and-authority: whether an action is permitted, constraint provenance, residual-risk acceptance authority, and dynamic human-gate activation, as distinct from evaluation/falsification/assurance intensity"
      ]
    },
    {
      "path": "docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md",
      "subjects": ["project-orchestration"],
      "preferred_subject": "project-orchestration",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/foundations/006_knowledge_activation_and_open_world_reasoning.md",
      "subjects": ["knowledge-representation", "retrieval-context"],
      "preferred_subject": "knowledge-representation",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md",
      "subjects": ["recommendation-action", "evaluation-assurance"],
      "preferred_subject": "recommendation-action",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md",
      "subjects": ["retrieval-context", "methodological-knowledge", "evaluation-assurance"],
      "preferred_subject": "retrieval-context",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md",
      "subjects": ["system-identity", "retrieval-context", "methodological-knowledge"],
      "preferred_subject": null,
      "confidence": "MEDIUM",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/033_methodological_knowledge_universe_construction_framework.md",
      "subjects": ["methodological-knowledge", "knowledge-representation"],
      "preferred_subject": "methodological-knowledge",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md",
      "subjects": ["source-universe"],
      "preferred_subject": "source-universe",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/035_multi_model_development_collaboration_architecture.md",
      "subjects": ["model-collaboration"],
      "preferred_subject": "model-collaboration",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md",
      "subjects": ["cockpit-product", "cockpit-visual-language", "cockpit-interaction"],
      "preferred_subject": "cockpit-product",
      "confidence": "MEDIUM",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md",
      "subjects": ["cockpit-visual-language"],
      "preferred_subject": "cockpit-visual-language",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md",
      "subjects": ["development-governance"],
      "preferred_subject": "development-governance",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md",
      "subjects": ["cockpit-implementation"],
      "preferred_subject": "cockpit-implementation",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/105_codexless_local_execution_bridge_evaluation.md",
      "subjects": ["tooling-integrations"],
      "preferred_subject": "tooling-integrations",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/research/124_scalable_repository_knowledge_architecture_and_reconstruction_redesign.md",
      "subjects": ["project-knowledge-architecture"],
      "preferred_subject": "project-knowledge-architecture",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md",
      "subjects": ["source-universe"],
      "preferred_subject": "source-universe",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md",
      "subjects": ["cockpit-implementation", "cockpit-visual-language", "cockpit-interaction"],
      "preferred_subject": "cockpit-implementation",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/local_execution/README.md",
      "subjects": ["tooling-integrations"],
      "preferred_subject": "tooling-integrations",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/model_collaboration/README.md",
      "subjects": ["model-collaboration"],
      "preferred_subject": "model-collaboration",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/methodological_knowledge/COVERAGE_MAP.md",
      "subjects": ["methodological-knowledge"],
      "preferred_subject": "methodological-knowledge",
      "confidence": "HIGH",
      "missing_vocabulary": []
    },
    {
      "path": "docs/project_knowledge/architecture/whole_architecture.md",
      "subjects": ["project-knowledge-architecture"],
      "preferred_subject": "project-knowledge-architecture",
      "confidence": "HIGH",
      "missing_vocabulary": []
    }
  ]
}
```

## Vocabulary terms that were hard to distinguish

### 1. `knowledge-representation` versus `methodological-knowledge`

This was the hardest boundary in the catalog. Both labels cover the reusable knowledge
universe. My working rule was:

```text
knowledge-representation      how reusable knowledge is structured, activated and versioned
methodological-knowledge      the Methodological Knowledge Universe as a body of content
```

That rule is mine, not the catalog's. Foundation 006 and Research 033 both sit on the
boundary and I assigned them to opposite sides. Another reviewer applying the same catalog
could reasonably invert both. The labels alone do not make the distinction decidable,
because "Knowledge representation, activation and lifecycle semantics" describes exactly
the properties Research 033 is pressure-testing, while "Methodological Knowledge Universe"
names the object Foundation 006 is reasoning about.

### 2. `retrieval-context` versus `knowledge-representation`

Foundation 006 is about activation from project state. The catalog places activation inside
`knowledge-representation`, but "Retrieval, relevance and selective reasoning context"
covers candidate relevance, state slices and applicability, which is a large part of that
memo. I used the `activation` keyword in the `knowledge-representation` label as the
tiebreaker; without that keyword I would have preferred `retrieval-context`.

### 3. `development-governance` versus `project-knowledge-architecture`

`docs/DEVELOPMENT_METHOD.md` contains a substantial repository-information-architecture
section, exhaustive routing rules and Knowledge Map contracts. Research 124 and
`whole_architecture.md` redesign exactly those concerns. I separated them by operational
status:

```text
development-governance             the current operating repository method
project-knowledge-architecture     the successor architecture program
```

Status is explicitly not supposed to be a placement substitute, so I am uneasy about this
split. If the successor is ever promoted to current authority, this rule silently inverts
and the two subjects collide. A definition based on subject matter rather than lifecycle
stage would be more durable.

### 4. `cockpit-product` versus `cockpit-interaction` versus `cockpit-visual-language`

Bounded Cockpit slices placed cleanly: Research 046 is category/silhouette grammar,
Research 089 is implementation provenance. Broad Cockpit design documents did not. Research
037 spans the world substrate, connector semantics, conversation workspace architecture,
motion language and renderer selection with roughly comparable weight. I routed it to
`cockpit-product` as the broadest Cockpit subject, but the catalog does not state that
`cockpit-product` is the intended default for whole-Cockpit design work rather than for
product architecture specifically.

### 5. The product/project axis inside `tooling-integrations` and `source-universe`

Two subjects collapse a distinction the repository otherwise maintains carefully.

`tooling-integrations` is labelled "Developer tooling, local execution and external
integrations" with `preferred_parent: runtime-and-tooling`, which reads as ADS-product
runtime tooling. Both paths I placed there (Research 105 and `docs/local_execution/README.md`)
are about the ADS *project's* own local execution bridge, which belongs under
`project-development`. The dual `broader` list admits both, but a reviewer weighting the
preferred parent more heavily could conclude these carriers do not belong here at all.

`source-universe` has the same shape. Research 034 designs the ADS product's Source Universe;
`SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md` is the project's own bootstrap of a real vault. I
placed both in `source-universe` because the vocabulary offers nothing else, but they are
different kinds of object.

## Cases where `preferred_subject = null` was necessary

One, `docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md`.

The memo states in its own purpose section that it captures three architectural conclusions:
system-owned project state as the defining distinction, methodological navigation as the next
defining component, and the governed methodological universe as the long-term knowledge base.
Those map to `system-identity`, `retrieval-context` and `methodological-knowledge`
respectively, with no one of them subordinate to the others. Section 19 then synthesises all
three as co-equal layers. Forcing a default route here would encode my weighting of body
length rather than a property of the source.

I considered and rejected `null` in two further cases:

- `docs/PRINCIPLES.md` mixes system-design principles with repository-method principles. I
  kept `system-identity` as preferred because the large majority of the principles constrain
  the ADS system's behaviour rather than the development method, but the margin is thin and
  confidence is MEDIUM.
- `docs/research/037` spans three Cockpit subjects. I kept `cockpit-product` because a
  whole-Cockpit exploration map plausibly has a broadest-subject default, but I would not
  treat disagreement here as a placement error.

## Repeated missing-vocabulary pressure

One genuine gap, raised once in the machine-readable block but visible at more than one path.

**Admissibility and authority.** Foundation 003 develops a sustained distinction between
whether an action is *permitted* (admissibility, constraint provenance, authority to accept
residual risk, dynamic human gates) and how much *confidence and control* a permitted action
requires (assurance). The catalog collapses both into `evaluation-assurance`, whose label
reaches admissibility only through the word "assurance". The same neighbourhood surfaces in
`docs/VISION.md`, which treats admissibility, epistemic integrity and risk-sensitive
assurance as separate constitutional concerns, and it is a distinct top-level neighbourhood
in `COVERAGE_MAP.md` (AL) separate from assurance (AM). A reader routing to
`evaluation-assurance` looking for "who may authorise this action" would be routed by a
label that does not advertise that content.

This is a proposal for later redesign, not an implicit catalog edit; no such ID appears in
any assigned set above.

Two further observations that I do **not** raise as missing vocabulary:

- `runtime-persistence` received no assignment from this subset. That is a property of the
  24 chosen paths rather than evidence of a catalog defect.
- Several carriers mix ADS-product and ADS-project content. That is a parent-axis question
  (should `project-development` versus `ads-system` be a facet rather than a parent?) rather
  than a missing leaf subject, so it is recorded above under label ambiguity instead.

## Catalog label or definition ambiguity that could cause collaborator drift

1. **The catalog carries labels but no definitions, scope notes or inclusion/exclusion
   examples.** Every hard case above was resolved from a label plus my own inferred rule.
   Two capable collaborators will invent different rules for the same label. If placement
   agreement is the T1 diagnostic, the absence of per-subject scope notes is a confound:
   low agreement would not distinguish "vocabulary is unclear" from "vocabulary is clear but
   undocumented".

2. **`legacy_topics` is doing invisible disambiguating work.** `development-governance`,
   `project-knowledge-architecture` and `model-collaboration` all carry the legacy topic
   `development-governance`, which tells me they were split out of one predecessor but not
   where the new boundaries run. A reviewer who reads `legacy_topics` as a hint will place
   differently from one who ignores it. I treated it as provenance only.

3. **`preferred_parent` competes with `broader` on the dual-parent subjects.**
   `knowledge-representation`, `project-knowledge-architecture`, `tooling-integrations` and
   `cockpit-implementation` each declare two parents. It is unstated whether the preferred
   parent narrows the subject's meaning or only fixes its display position. Under the first
   reading, `tooling-integrations` is primarily product runtime tooling and both of my
   placements there are wrong; under the second, they are right.

4. **No stated guidance on multiple-assignment discipline.** The brief permits one or more
   subjects but sets no bound and gives no threshold for when a mentioned neighbourhood earns
   membership. I used "the carrier develops the subject substantively" rather than "mentions
   it", which kept `docs/VISION.md` at a single subject even though it touches nearly every
   subject in the catalog. A reviewer using a looser rule would produce far larger subject
   sets from the same corpus, and raw set-overlap agreement metrics would drop for reasons
   unrelated to vocabulary quality.

5. **Four labels encode more than one concept in one string**, which makes partial matches
   ambiguous: "Evaluation, falsification, assurance and execution integrity",
   "Knowledge representation, activation and lifecycle semantics",
   "Project state, dependency and orchestration", and
   "Development governance, continuity and repository method". A carrier matching only the
   third element of such a label is a weaker member than one matching all elements, but the
   annotation format has no way to express that.

No comparison against ChatGPT's annotations was attempted, and none of the prohibited
fixtures were opened before freezing this message.
