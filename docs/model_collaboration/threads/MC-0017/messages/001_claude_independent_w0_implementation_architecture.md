# MC-0017 Message 001: Claude Independent W0 Implementation Architecture

```text
Thread                          MC-0017
Message                         001
Author / collaborator           Claude
Role                            INDEPENDENT_REVIEWER / COUNTER_DESIGNER / RESEARCHER / CRITIC
Interaction environment         Claude
Project / workspace             Autonomous Data Science System
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Repository head seen            ec506b32eb6dec27c8f40412d0b0dd377ad444c2 (routing surfaces only)
Independent substantive base    1f09fc812e8d7b1f31771a8b545864b76ea61db0
Selected architecture           PKA-CANDIDATE-01 (D-035)
Governing contract              Specification 028 (FROZEN)
Purpose                         Independent production W0 implementation architecture, before exposure
                                 to ChatGPT's separately frozen Research 178 design
```

## 0. Independence statement

From the current coordination branch I read only the five authorized routing surfaces (`current_routing.json`, `REVIEW_INBOX.md`, and MC-0017's `BRIEF.md` / `THREAD.md` / `STATE.json`). Every substantive read was bound to `1f09fc812e8d7b1f31771a8b545864b76ea61db0`: Specification 028, Research 175/176/177, D-035 in `DECISIONS.md`, `docs/README.md`, `docs/CONTINUITY.md`, and `scripts/research/project_knowledge_candidate01_real_shadow_v01.py` as a representative prototype. I did not read Research 178, Checkpoint 524 or later bodies, or descendant current-state synthesis. I carry my own MC-0011 through MC-0016 reasoning, which the brief explicitly permits.

`INDEPENDENT_W0_DESIGN_CONTAMINATED: NO`

## A. Package and module architecture

I would not build a flat responsibility package. Research 177's fourteen-module list is a good *responsibility* enumeration but a poor *dependency* statement: it says what exists, not what may import what, and a flat package is exactly where circular imports appear (`authority` needs identity resolution; `identity` needs relation parsing; `views` needs both; `validation` needs all of them; and everything needs `model`). I would keep Specification 028's Section 3 module names as the public surface, because that is contractual, and impose a four-layer dependency rule underneath them.

```text
L0  model/            pure value objects, enums, errors, result types
                       imports: stdlib only
                       no I/O, no Git, no filesystem, no jsonschema

L1  adapters/         gitio, fsio, schema loading/validation, clock
                       imports: L0 only
                       the ONLY layer permitted to touch the outside world

L2  domain/           declaration parsing, identity closure, authority
                       resolution, workstream DAG, capture rules,
                       reconstruction planning, view *computation*
                       imports: L0 only
                       receives already-read bytes/records as arguments

L3  services/         orchestration: discovery -> parse -> validate ->
                       compute -> render -> compare/write
                       imports: L0, L1, L2

L4  cli/              argument parsing, exit codes, output formatting
                       imports: L3, L0
```

The load-bearing rule is that **L2 takes no dependency on L1**. Domain functions accept `(path, bytes)` pairs or already-constructed records, never a repository handle. That single constraint prevents circular imports structurally rather than by convention, makes every semantic rule testable without a Git fixture, and is what makes PKA-G013 (full/incremental equivalence) provable rather than merely observed — if identical inputs are fed to identical pure functions, equivalence is an argument about the *input set*, not about generator behavior. That reframing matters: it converts the hardest W0 gate from an empirical comparison into a much narrower question about dependency computation.

Mapping to Specification 028's required names, which stay as the package's public modules and re-export from the layers:

```text
model.py         -> model/ package (records, enums, errors)
declaration.py   -> domain/declaration.py  + adapters/schema.py
references.py    -> domain/references.py   + adapters/gitio.py
identity.py      -> domain/identity.py
authority.py     -> domain/authority.py
workstreams.py   -> domain/workstreams.py
views.py         -> domain/views/*.py (compute) + services/generation.py (render/write)
reconstruction.py-> domain/reconstruction.py
capture.py       -> domain/capture.py
migration.py     -> domain/migration.py + services/migration_audit.py
validation.py    -> domain/rules/*.py + services/validation.py
git.py           -> adapters/gitio.py
cli.py           -> cli/
```

I'd note explicitly that this is a *refinement* of Specification 028 Section 3, not a departure: that section already says "Exact internal helper decomposition MAY differ when implementation evidence supports a cleaner design, but these logical responsibility boundaries MUST remain explicit and testable." The layering makes them more testable, not less.

Pure-function/value-object discipline: everything in L0 and L2. Concretely, `resolve_authority(query, sources, relations, transitions) -> AuthorityResult` is a pure function of its arguments. The service layer is what knows that `sources` came from a repository scan.

On `tools/project_knowledge/` versus `src/ads_system/`: I found no Specification 028 defect here. The boundary is correct and well-argued in Research 177 Section 2. The one thing I'd add is that `tools/` needs to be importable under the repository's existing `uv`/`pyproject` setup without becoming a published distribution — a `[tool.pytest.ini_options]` path entry or equivalent, decided at implementation time, not an architecture question.

## B. Typed semantic model

The minimum internal representation, all frozen dataclasses with `slots=True`, all comparable and hashable where used as keys:

```text
SemanticId         NewType over str + validated construction
                    NOT auto-generated; construction requires an explicit
                    declared value (this is what enforces selectivity)

AuthorityClass     enum: CANONICAL CANDIDATE HISTORICAL DERIVED EVIDENCE CAPTURE
Profile            enum: the eight V1 profiles
LifecycleState     enum: ACTIVE PAUSED BLOCKED COMPLETED SUPERSEDED
RelationMode       enum: REPLACE SUPPLEMENT SPECIALIZE CORRECT
TransitionClass    enum: the seven V1 transition classes

Scope              structured, see Section E; NOT a bare string
Relation           (mode, target: SemanticId|PathRef, scope: Scope|None)
SourceRevision     (source_path, source_commit|None, hash_algorithm,
                    hash_basis, content_digest) exactly per Spec 028 §18

GovernedSource     (carrier_path, profile, authority_class,
                    semantic_id: SemanticId|None, state, scope,
                    relations, provenance, triggers, temporal, raw_declaration)

Workstream         a GovernedSource projection with required semantic_id
                    plus parent/depends_on/pause_reason/return_condition/
                    resume_target/current_anchor/expected_revision

ActionContract     (constraints: ordered tuple[ConstraintId],
                    preconditions, prohibitions, postconditions,
                    fail_closed) — constraint IDs are stable and ordered

AuthorityQuery     (action, target_scope, workstream, actor, consequence, at_time)
AuthorityResult    (status, governing: tuple[GoverningSource], receipt)
AuthorityReceipt   per Spec 028 §25, serializable, deterministic field order

ViewManifest       per Spec 028 §21
ReconstructionPlan (task_class, must_load, optional, negative,
                    freshness_requirements, receipt_requirements, fail_conditions)
Capture            (capture_id, recorded_at, provenance, status, subject_link)
Diagnostic         (code, severity, carrier_path, semantic_id|None,
                    message, remediation)
```

On the H3 question: this is not a universal semantic-object model, and the specific property that keeps it from becoming one is that `SemanticId` has no auto-generating constructor anywhere in the codebase. A `GovernedSource` with `semantic_id=None` is a first-class, fully valid citizen — it participates in the source catalog and subject index but not in the identity index or authority closure. If a future implementer wants every source to have an ID, they have to add a code path that mints one, which is a visible, reviewable change rather than drift. I'd make "no function in the package generates a `SemanticId` from a path, title, or hash" an explicit W0 test (see Section P).

## C. Schema composition

Genuinely common across all eight profiles: `schema_version`, `profile`, `kind`, `authority_class`. That is the entire honest common envelope — Specification 028 §9 is right, and I'd resist the temptation to promote `semantic_id` or `scope` into it, because both are conditionally required and hoisting them invites `"semantic_id": null` boilerplate on every source, which is the first step toward universal identity.

```text
schemas/project_knowledge/
    $defs.v1.schema.json            semantic_id pattern, scope, relation,
                                    source_revision, temporal, provenance
    envelope.v1.schema.json         the four common fields, additionalProperties: true
    semantic_source.v1.schema.json  allOf: [envelope] + own required/properties
    workstream.v1.schema.json       ... + if/then for PAUSED
    governing_procedure.v1.schema.json
    project_boundary.v1.schema.json
    identity_transition.v1.schema.json
    joint_authority.v1.schema.json
    capture.v1.schema.json
    derived_view_manifest.v1.schema.json
```

`additionalProperties` policy — I'd split it deliberately rather than applying one rule:

```text
leaf profile schemas        additionalProperties: false
                             typos in governed control fields must fail loudly;
                             this is what makes PKA-G002's negative fixtures meaningful

$defs sub-objects           additionalProperties: false
envelope (composed via allOf) additionalProperties: true
                             required, or every allOf composition fails
```

Versioning: filename-embedded major version (`workstream.v1.schema.json`) plus a `schema_version` integer in the payload. A v2 profile is a new file; v1 is never edited in place once a canonical source depends on it. The `profile` field selects the schema — dispatch is a dict lookup, not inference.

Conditional validation belongs in JSON Schema where it is local and structural (`if state == PAUSED then require pause_reason, return_condition, resume_target` — Specification 028 §15 states this and it is expressible as `if/then`), and in Python semantic validators where it is cross-source (does `resume_target` resolve? does `depends_on` cycle?). The split rule: **schema validates one document against itself; Python validates documents against each other.**

Schema-to-Python mapping: I would *not* auto-generate models from schemas. Generated models tend to reproduce schema shape rather than domain shape, and here the domain shape (`Scope` as a structured matcher, `SemanticId` as a validated NewType) is deliberately richer than the wire shape. I'd hand-write the dataclasses and add a W0 test that every schema-required field appears in the corresponding dataclass — catching drift without coupling the domain model to a code generator.

**Possible under-specification I found:** Specification 028 §8 requires `project_boundary.v1.schema.json` but nowhere in §1-§46 defines what a project-boundary source actually contains, unlike workstream (§15), governing procedure (§17), identity transition (§11), joint authority (§13), and capture (§27), which all get explicit field contracts. Research 177 §5 describes it only as "narrow project-global integration facts with a natural global owner." This is the thinnest of the eight and the one most likely to become a junk drawer. See Section Q.

## D. Markdown declaration parsing and source discovery

**Parsing.** Byte-level, no Markdown parser, no regex for the outer extraction (regex on a document-scale string invites catastrophic backtracking and is harder to make exact about "at most one block"). The algorithm:

```text
1. read carrier bytes; decode UTF-8 strict (a decode error is a hard failure,
   not a silent replacement)
2. find ALL occurrences of BEGIN marker and ALL of END marker
   - 0 BEGIN, 0 END        -> NoDeclaration (valid)
   - >1 BEGIN or >1 END    -> PKA-E-MULTIPLE-BLOCK (hard)
   - unbalanced            -> PKA-E-UNTERMINATED-BLOCK (hard)
   - END before BEGIN      -> PKA-E-INVERTED-MARKERS (hard)
3. slice between markers; strip only leading/trailing whitespace
4. json.loads with object_pairs_hook=reject_duplicate_keys
5. after the parsed value, assert nothing but whitespace remains
6. assert the top-level value is a dict
7. dispatch on profile -> schema validate
```

Duplicate-key rejection needs the `object_pairs_hook`, since `json.loads` silently keeps the last value otherwise; this is Specification 028 §6's explicit requirement and the default behavior violates it.

CRLF: normalize `\r\n` to `\n` *only within the extracted block* before parsing, and never rewrite the carrier. JSON permits `\r` as whitespace between tokens, so most cases would parse anyway, but normalizing makes the digest of the semantic object independent of checkout line-ending settings, which matters for PKA-G003 and for Windows contributors.

**Discovery without a manual central registry.** This is the question I'd most want compared, because the naive answer (scan everything) and the wrong answer (maintain a list) are both bad. My design:

```text
scan roots      the tracked-file set from `git ls-files` at the target ref,
                NOT os.walk — this automatically excludes untracked scratch
                files, build output, and anything gitignored, and it gives
                the same answer on any checkout

candidate filter extension in {.md, .json} AND path not under an
                excluded prefix

excluded prefixes (declared in one config constant, not scattered):
                docs/project_knowledge/generated/     (derived output)
                docs/project_knowledge/captures/      (capture, not canonical)
                docs/research/project_knowledge_*/    (frozen fixtures)
                scripts/research/                     (research code)
                prototype_v0/                         (historical)

classification  a candidate with no declaration block -> not governed, recorded
                in the catalog as UNDECLARED with its path only
                a candidate with a declaration -> governed, profile-dispatched
```

The key safety property: **exclusion is by declared prefix, and every excluded path is still enumerated and counted in the source catalog under an `excluded` bucket with its reason.** That makes the exclusion set auditable — if a governed source is ever accidentally added under an excluded prefix, it appears in the catalog as `EXCLUDED_BUT_DECLARED`, which is a validation warning rather than silence. That is the specific mechanism that stops fixtures/generated/history from being mistaken for current authority: not that we skip them, but that we record skipping them and flag the contradiction.

Captures are deliberately excluded from the *canonical* scan and discovered by a separate, explicit capture scan. A capture must never be able to enter authority resolution through the same code path as a canonical source — this is KA-I16 enforced structurally rather than by checking `authority_class` after the fact.

**Incremental refresh source identification.** `git diff --name-only <ref>..HEAD` gives changed paths. Apply the same candidate filter. Then compute the affected set as the transitive closure over a *generated* dependency index (see Section H), falling back to full rebuild when: a changed path is a schema, a changed path is in the excluded-prefix config, the dependency index is missing or stale, or any changed governed source declares a relation whose target is not in the index. Specification 028 §24 requires this fallback and I'd make the fallback *loud* — a diagnostic saying why, not a silent upgrade.

**Native JSON carriers without two discovery systems.** One scan, one classifier, two extractors. `extract_declaration(path, bytes) -> DeclarationResult` dispatches on extension: `.md` runs the marker extractor, `.json` parses the whole document and looks for the envelope fields at top level. Both produce the identical `RawDeclaration` record, and everything downstream is extension-blind. The drift risk Specification 028 §7 worries about is handled by one rule: a `.json` carrier is governed only if it contains all four envelope fields; a JSON file with a frozen compatibility schema simply won't have them and is classified `UNDECLARED` — no allowlist needed.

## E. Scope and authority semantics

Scope is the part of this design I'd flag as most under-specified in the frozen contract, and where "match the scope" is doing the most unearned work. Specification 028 §12 requires "an explicit target and scope when the relation is not globally applicable" and §25 requires a `UNRESOLVED_SCOPE_REQUIRED` status, but never defines what scope *is* structurally.

I'd define it as a conjunctive facet set with explicit unknown:

```text
Scope = {
    action_classes: frozenset[str] | ANY
    targets:        frozenset[str] | ANY     (path prefixes / semantic IDs)
    domains:        frozenset[str] | ANY
    interval:       (effective_from, effective_to) | ALWAYS
}
```

Matching between a query scope `Q` and a declared scope `D`:

```text
facet_match(Q_f, D_f):
    D_f is ANY            -> MATCH_WEAK   (declared applies broadly)
    Q_f is unspecified    -> UNDERSPECIFIED
    Q_f subset of D_f     -> MATCH_STRONG
    Q_f disjoint D_f      -> NO_MATCH
    otherwise (partial)   -> UNDERSPECIFIED

scope_match = NO_MATCH        if any facet NO_MATCH
              UNDERSPECIFIED  else if any facet UNDERSPECIFIED
              MATCH_STRONG    else if all facets MATCH_STRONG
              MATCH_WEAK      otherwise
```

Three properties I care about. Ordering is total and deterministic (`NO_MATCH < UNDERSPECIFIED < MATCH_WEAK < MATCH_STRONG`), so precedence never depends on iteration order. `UNDERSPECIFIED` is a first-class outcome rather than a coin flip, which is what makes `UNRESOLVED_SCOPE_REQUIRED` derivable rather than hand-raised. And specificity is computable — `MATCH_STRONG` on more facets beats `MATCH_WEAK` — which is what `SPECIALIZE` needs to mean something precise.

**Resolver algorithm:**

```text
resolve_authority(query, catalog, indexes) -> AuthorityResult

1. CANDIDATE SET
   all CANONICAL sources whose declared governed-action classes intersect
   query.action. (DERIVED/CAPTURE/EVIDENCE/CANDIDATE excluded here by class,
   before any scoring — KA-I14 and KA-R24 enforced structurally.)
   If empty -> MISSING_REQUIRED_AUTHORITY.

2. SCOPE FILTER
   compute scope_match for each candidate.
   drop NO_MATCH.
   if the surviving set is empty -> MISSING_REQUIRED_AUTHORITY.
   if any survivor is UNDERSPECIFIED and consequence is high
       -> UNRESOLVED_SCOPE_REQUIRED (with the specific facet named).

3. TEMPORAL FILTER
   drop sources whose effective/authority interval excludes query.at_time.
   (absent temporal fields = always applicable; Spec 028 §14)

4. RELATION CLOSURE — the core, and the place order matters
   iterate to fixpoint over the relation graph restricted to survivors:
     REPLACE   (S replaces P for scope X):
               if scope_match(query, X) != NO_MATCH, remove P
     CORRECT   (S corrects P for scope X):
               same removal as REPLACE, but the receipt records
               CORRECTION rather than SUPERSESSION — semantically
               different provenance, identical current-authority effect
     SPECIALIZE(S specializes P for narrower scope X):
               if query scope_match against X is MATCH_STRONG, remove P;
               if only MATCH_WEAK, keep BOTH and record that the
               specialization was not strongly applicable
     SUPPLEMENT(S supplements P):
               keep both, mark the pair as jointly required, record order
   detect cycles; a cycle in REPLACE/CORRECT is
       UNRESOLVED_AUTHORITY_CONFLICT, never an arbitrary tie-break.

5. JOINT AUTHORITY
   if a qualified joint_authority.v1 declaration covers the surviving set,
   apply its combination rule (ALL_REQUIRED / PRECEDENCE / BASE_PLUS_SUPPLEMENT).
   A joint declaration may only constrain members already surviving steps 1-4;
   it can never ADD a governing source that scope/temporal filtering excluded.
   That restriction is what stops the exception from becoming a back door.

6. CONFLICT CHECK
   if >1 source survives with no SUPPLEMENT/joint relation binding them and
   no specificity ordering between them -> UNRESOLVED_AUTHORITY_CONFLICT.
   Never pick by recency, path order, or retrieval rank.

7. FRESHNESS
   verify each survivor's SourceRevision against the target ref.
   mismatch -> STALE_REQUIRED_AUTHORITY.

8. PRIVATE DEPENDENCY
   if any survivor declares an unsatisfiable private dependency and the
   consequence class requires it -> REQUIRED_PRIVATE_STATE_UNAVAILABLE.

9. CONTRACT ACTIVATION
   collect ordered constraint IDs from surviving governing_procedure sources.

-> RESOLVED with receipt.
```

Minimum durable receipt, exactly Specification 028 §25 plus the two fields I think it needs to be auditable: the **scope match grade per governing source** (so a later reader knows whether authority applied strongly or weakly) and the **removed-source list with removal reason** (so "why is P not governing?" is answerable from the receipt alone rather than by re-running the resolver). Both are cheap and both turn the receipt from a claim into evidence.

Retrieval nominations never enter this function. If a retrieval layer exists later, it produces a candidate *path list* that is fed to step 1's filter like any other — and the receipt records that the candidate set was retrieval-nominated. Nomination can only ever shrink work, never change a disposition.

## F. Identity transitions

Two structures with deliberately different cost profiles:

```text
identity_index.json   generated, flattened, bounded
    semantic_id -> { current_carrier, status, transition_chain_depth,
                     terminal_class }
    every historical ID appears with its *final resolved* target
    lookup is one dict access; no chain walking at query time

transitions/*.md      authoritative, append-mostly, never scanned on the
    one file per transition, each an identity_transition.v1 source
    normal path
```

Per class:

```text
MOVE_OR_RENAME              index entry updated to new carrier; the declaration
                            itself usually lives in the moved source, and a
                            separate transition record is created ONLY when the
                            old path is externally referenced. This is the
                            single biggest volume control — most renames need
                            no transition record at all.

REPRESENTATION_REPLACEMENT  same ID, new carrier/form; index updated; a record
                            is warranted because the form change is provenance.

MERGE                       A,B -> C. index: A -> C (status MERGED_INTO),
                            B -> C, C -> C. record holds both predecessors.

SPLIT                       A -> B,C. index: A -> [B,C] with status SPLIT.
                            A lookup returns a *set*; callers must handle it.
                            I'd make the index value always a list to avoid
                            a type switch at every call site.

SUPERSEDE                   ID stays resolvable, status SUPERSEDED, plus a
                            pointer to the superseding ID. Distinct from
                            MERGE: the identity survives, the authority does not.

RETIRE                      resolvable, status RETIRED, no successor.

REDIRECT                    pure alias; index maps to target, status ALIAS.
```

Bounded lookup with full provenance: the index is built by a full scan of transition records at rebuild time, with chains flattened eagerly (a `A -> B -> C` chain stores `A -> C` directly, plus `chain_depth: 2`). Normal lookup never walks. Cycle detection and dangling-target detection happen at build time, not query time — this is Specification 028 §11's requirement and also what my MC-0016 Section C concern was actually about.

What stops this becoming a manual global registry: a transition record is created only when the transition itself carries provenance meaning, the index is derived and deletable, and — the metric I'd actually track — `transition_record_count / governed_source_count`. If that ratio climbs, the selectivity discipline is failing. I'd put it in the complexity metrics of Section P.

## G. Workstreams and concurrency

```text
domain/workstreams.py  (pure)
    build_graph(workstream_sources) -> WorkstreamGraph
    validate_graph(graph) -> tuple[Diagnostic]
        - depends_on targets exist
        - parent targets exist
        - no cycle in depends_on (DFS, three-color)
        - no cycle in parent
        - PAUSED => pause_reason, return_condition, resume_target present
        - resume_target resolves (path, semantic ID, or anchor)
        - COMPLETED workstream has no ACTIVE children (warning, not error)
    active_route(graph) -> tuple[SemanticId]
        deterministic: topological order over ACTIVE nodes whose
        depends_on are all COMPLETED, tie-broken by semantic_id sort
        NOT by file order — the prototype's fixture-order tie-break is
        exactly the kind of accidental determinism that shouldn't reach
        production
    salience(graph, task_context) -> set[SemanticId]
        which PAUSED workstreams must enter bootstrap
        (per the paused-salience rule: parent/task intersection,
        satisfied return condition, due review trigger)

services/workstream_ops.py  (orchestration)
    read sources, call pure functions, write receipts, check revisions
```

**Interruption recovery** derives completed work from durable receipts plus repository evidence, never from a plan. Concretely: a multi-step operation writes an ordered step-receipt file after *each* completed step; recovery reads the receipts, compares against the declared step sequence, and classifies each step as `COMPLETED` / `PENDING` / `INDETERMINATE`. `INDETERMINATE` (receipt absent but side effects possibly present) fails visibly rather than replaying — Specification 028 §16 requires exactly this and it is the one place I'd resist any "just re-run it, it's idempotent" shortcut, because idempotency of a consequential mutation is a claim that needs its own proof.

**Stale-write rejection:** every authoritative mutation takes `expected_revision: SourceRevision`. The service re-reads the current revision immediately before writing and compares `content_digest`. Mismatch raises before any write. This is optimistic concurrency, fail-visible, no locking — matching Specification 028 §16's explicit scope. The check must be in the service layer, not the CLI, so it cannot be bypassed by a new command.

## H. Derived-view engine

One engine, one generation path, three output modes. The design that makes full and incremental *structurally* equivalent rather than two implementations:

```text
every view is declared as a Generator with:
    view_id
    input_selector   which governed sources it consumes (by profile/predicate)
    compute(inputs) -> view value object     PURE, L2
    render(value)   -> bytes                 PURE, deterministic serialization
    manifest(inputs, value) -> ViewManifest  PURE

full rebuild:
    inputs = all governed sources matching input_selector
    -> compute -> render -> stage -> compare/publish

incremental refresh:
    changed = filtered git diff
    affected_views = { g for g in generators
                       if input_selector(g) intersects changed
                       OR g depends on a view whose inputs changed }
    inputs for each affected view = ALL sources matching its selector
                                    (re-read, not patched)
    -> identical compute -> render -> stage -> compare/publish
```

The decisive choice: **incremental refresh narrows which views are regenerated, never which inputs a view sees.** A view is always computed from its complete input set. That makes PKA-G013 equivalence true by construction — the same pure function on the same input set — and reduces the gate to testing the *selector intersection logic*, which is a small, directly testable surface. The alternative (patching view state incrementally) would be faster at 10x scale and would make equivalence an empirical hope. At this repository's size, correctness is worth far more than the saved milliseconds, and this is reversible later if measurement ever justifies it.

Determinism: one shared `render_json(value) -> bytes` implementing Specification 028 §22 (UTF-8, LF, final newline, 2-space indent, sorted keys, per-schema array ordering, no timestamps). Refresh timestamps live in the manifest, never the view — §22 explicitly permits this and it keeps byte-comparison viable.

Same-commit binding per §19: manifests bind ordered input paths + per-input content digests + generator identity + generator version. No self-referential commit hash. Generator version should be a digest of the generator module's source, computed at runtime — that way a generator logic change invalidates freshness automatically rather than depending on someone remembering to bump a constant.

**Challenge to the committed-view list.** Specification 028 §20 requires eight persisted artifacts. I think two are questionable and I'll say so before implementation rather than after:

```text
worth committing (routing/authority/bootstrap critical, read by fresh
collaborators before tooling is available):
    source_catalog.json      yes
    identity_index.json      yes
    authority_index.json     yes
    workstream_graph.json    yes
    current_state_core.json  yes
    CURRENT_STATE_CORE.md    yes

questionable:
    subject_index.json         this is navigation, fully regenerable, and
                               its committed form is the closest thing in
                               the new design to the old KNOWLEDGE_MAP
                               drift surface. Committing it means every
                               new source produces an index churn diff.
    risk_obligation_index.json genuinely useful, but it is a query over
                               source-declared triggers rather than a
                               structural index; it could be computed on
                               demand at negligible cost.
```

I am **not** proposing to amend §20. Both are cheap to generate and byte-stable, the churn is real but small, and there is a legitimate argument that a fresh collaborator without tooling benefits from both being readable in the tree. I'd implement all eight as specified and instrument diff-churn per view during W0/W2; if `subject_index.json` dominates the diff volume, that is prospective evidence for a §20 amendment at W2, made with data rather than taste. Recording the reservation now is the point — see Section Q, classified `DEFER_TO_W1_OR_LATER`.

## I. Reconstruction planner

The boundary I'd draw hard: **model-assisted intent classification may only ever produce a `TaskIntent`; every downstream step is deterministic.**

```text
free-text task description
        |
        v   [may be model-assisted, may be explicit CLI flags,
        |    may be a hand-written task spec file — all equivalent]
   TaskIntent { task_class, action, target_scope, consequence, workstream? }
        |
        v   [fully deterministic from here down, project-controlled]
   plan_reconstruction(intent, catalog, indexes) -> ReconstructionPlan
```

A misclassified intent can therefore produce the *wrong plan*, but never an *unsafe* one: authority closure, must-load sets, and fail conditions are all computed by the same deterministic functions regardless of how the intent was produced. And because `TaskIntent` is a small explicit record, a human or a test can supply it directly — which is how the planner gets tested without a model in the loop.

```text
BROAD_CONTINUATION
    must_load     bootstrap core, current_state_core, active route workstreams,
                  salient paused workstreams (Section G), open risks
    optional      domain sources on demand
    negative      historical checkpoints, superseded sources, capture backlog
    freshness     current_state_core must be fresh; stale -> warn and
                  fall back to the deterministic core + source links
    receipt       sources consumed, freshness status

NARROW_GOVERNED_TASK
    must_load     bootstrap rule + resolve_authority(intent) governing set
                  + activated action contract
    optional      minimum supporting evidence cited by the governing sources
    negative      broad orientation is explicitly NOT required — this is the
                  budget win, and it must be represented as an explicit
                  negative rather than an omission, so a collaborator can see
                  that skipping it was a decision
    freshness     every governing source revision verified
    fail          any non-RESOLVED authority status halts the plan

EXPLORATORY_RESEARCH
    must_load     nothing governing by default
    optional      structured/lexical discovery results
    negative      none
    freshness     advisory
    receipt       explicit uncertainty retained; results marked
                  NON_AUTHORITATIVE
```

Representation: `ReconstructionPlan` is a value object that serializes to JSON, so a plan can be emitted by the CLI, handed to a different collaborator or provider, and independently checked. That is also the cross-provider portability story (KA-R36) — the plan is the portable artifact, not the tool.

## J. The Claude-history activation failure

I'm the collaborator that failed here, so let me state what actually happened rather than analyze it abstractly. Asked whether Claude had participated in Candidate 01's design, I answered from what was salient in my working context — the later qualification stages — and gave an answer that understated MC-0011/MC-0013/MC-0014/MC-0015/MC-0016. The owner pointed out that the Claude threads live in the repository. I then read them and corrected the answer. Nothing was missing; nothing was hard to find; `docs/README.md` already names `docs/model_collaboration/` as a governed domain and `CONTINUITY.md` already carries a model-collaboration route.

**Disposition: this is not evidence for a new topology registry.** It is an instance of the failure class I named in MC-0011 Message 001 Section 2 as *dispatch* rather than *reconstruction* — the information was available and locatable; retrieval was never initiated because a plausible answer was already at hand. Adding a repository self-model would be solving the wrong problem, and worse, would recreate exactly the hand-maintained-global-map failure mode Candidate 01 exists to escape. I want to be blunt about the incentive here: it would be convenient for me to propose new machinery in response to my own error, and that is precisely why the bar should be higher than usual.

**Does Candidate 01 already cover it?** Partially, and I want to be precise about which part.

```text
covered   if the question is asked as a governed task, the reconstruction
          planner's NARROW_GOVERNED_TASK path resolves authority for
          "what is the collaboration history of X" and the source catalog
          + subject index return the MC threads. The mechanism exists.

NOT covered  the failure was that no task classification happened at all.
          A conversational question doesn't pass through a planner. No
          derived view helps if nothing queries it.
```

So the honest answer is: Candidate 01's mechanisms are *sufficient* for this failure class when invoked, and Candidate 01 contains no mechanism that causes them to be invoked for a question that doesn't look like a governed task. That gap is real, and it is also — I'd argue — not W0's problem and possibly not solvable by architecture at all, which is the same conclusion I reached in MC-0011 Section 1 and had to walk back partway in MC-0011 Message 003. The narrow, honest version: a collaborator protocol ("before answering a question about project history from working memory, check the catalog") is a `CONTINUITY.md` amendment, not a W0 module.

**What I'd actually add, which is small:** the source catalog should carry a `domain` facet (already implied by the subject index), and `CURRENT_STATE_CORE.md` should include a one-line "governed domains present" enumeration generated from it. That is not a topology registry — it is a generated line in an existing generated view, it cannot drift, and it costs nothing. It raises the chance that a collaborator reading the bootstrap surface sees that a collaboration-history domain exists before being asked about it.

**Smallest falsifying W0 regression scenario:**

```text
PKA-W0-J1
  given   the frozen W0 fixture corpus containing >=2 governed domains,
          one of which is a model-collaboration-like domain whose sources
          are NOT referenced by the active workstream
  when    plan_reconstruction(TaskIntent(BROAD_CONTINUATION), ...) runs
  then    the resulting plan's generated current-state core enumerates
          that domain by name
  and     a NARROW_GOVERNED_TASK intent targeting that domain resolves
          to its sources with a RESOLVED receipt
  falsifies  if either fails, the existing mechanisms genuinely do not
             cover this class and a distinct self-model concept must be
             argued on its own merits rather than assumed
```

## K. Capture and promotion

W0 builds the contracts and validation; W4 runs a real promotion. What W0 must get right:

```text
capture.v1 requires   capture_id, recorded_at, provenance, status
                      authority_class MUST be literally "capture"
                      (schema const, not enum — a capture cannot even
                      express canonical authority)

structural non-authority  captures live under captures/open/, are excluded
                      from the canonical discovery scan, and are read only
                      by a separate capture scan. resolve_authority() has
                      no code path that reaches them.

PromotionPlan (W0)    a computable, reviewable value object:
                      { capture_id, target_carrier, target_semantic_id?,
                        expected_target_revision, accepted_statement,
                        provenance_chain, diagnostics }
                      W0 can COMPUTE and VALIDATE this. It does not apply it.

promotion (W4)        verify expected_target_revision; update/create the
                      natural canonical source; write a promotion record
                      that carries the capture provenance; only then may
                      the capture move to historical/
```

The preservation rule that matters: a capture may be archived or removed **only if** the promotion record plus the updated canonical source together contain the accepted statement and the provenance chain. W0 implements `verify_provenance_retained(promotion_record, canonical_source) -> bool` as a pure function and tests it against fixtures where it must return false (accepted statement present but provenance dropped; provenance present but the statement was paraphrased away).

No CLI command in W0 mutates a canonical source. `promotion-plan` is read-only and emits the plan; applying it is W4 and gets its own command with its own gate.

## L. Public/private boundary

```text
declaration side
    a public source may declare:
        private_dependency: { requirement_id, description, verification_status }
    where verification_status ∈ { VERIFIED, STALE, UNAVAILABLE }
    and description is free text constrained by the leakage validator

leakage validator (pure, runs on every public view before publication)
    reject:  absolute filesystem paths
             known private-root tokens (.ads-private, private repo names)
             anything matching declared secret patterns
             private semantic IDs not in the public-safe allowlist
    the validator runs on RENDERED BYTES, not on the value object —
    leakage through a description field or a diagnostic message is
    exactly as bad as leakage through a structured field, and only
    byte-level checking catches both

resolver side
    step 8 of the algorithm in Section E:
    consequence >= the declared threshold AND verification_status != VERIFIED
        -> REQUIRED_PRIVATE_STATE_UNAVAILABLE
    consequence below threshold
        -> RESOLVED, with the receipt recording the unverified dependency
```

`RESOLVED_PRIVATE` semantics from `CONTINUITY.md` are preserved by never conflating three states: the project knows the value (resolved), this surface cannot see it (unavailable to surface), and the project doesn't know it (unresolved). The resolver distinguishes the second and third; it never downgrades the first. This is an existing continuity rule I'd carry into the implementation verbatim rather than re-deriving.

## M. Validation and diagnostics

Layered by dependency radius, matching Specification 028 §33, with one structure:

```text
Diagnostic(code, severity, carrier_path, semantic_id, message, remediation)

severity:
    ERROR    hard failure; blocks rebuild/publish; non-zero exit
    WARNING  does not block; must appear in output; counted
    INFO     observability only

code:     stable, greppable, namespaced — PKA-E-DUP-KEY,
          PKA-E-CYCLE-DEPENDS-ON, PKA-W-SUBJECT-ORPHAN
          stable codes matter because they become the vocabulary of CI
          failures and of the migration audit; free-text messages drift
remediation: one line, imperative. A diagnostic that says what's wrong
          but not what to do is half a diagnostic.
```

Layer assignment:

```text
local        parse, schema, conditional fields, ID format, revision
             descriptor shape                        (no cross-source reads)
cross-source relation targets, identity closure, dependency cycles,
             joint-authority membership, duplicate IDs
semantic     authority closure coherence, workstream resume consistency,
             procedure prose/contract drift
privacy      leakage on rendered public views
freshness    manifest input bindings, generator version, stale views
equivalence  incremental vs full on the fixture corpus
migration    inbound references, parity, rollback representability
```

Prose/contract drift (Specification 028 §17) is the one genuinely hard check. W0 should implement the cheap, honest version: flag when a governing procedure's prose body changes in a commit where its structured contract does not, as a WARNING requiring human disposition. That is detection, not semantic comparison, and I'd rather ship an honest heuristic that surfaces the case than claim semantic equivalence checking that doesn't exist. This is the same residual gap I named in MC-0016 Message 003 Section B; it's still the right size of answer.

## N. CLI and application boundary

```text
READ-ONLY (never write outside a temp dir)
    validate              parse + all validation layers
    check-freshness       manifest verification
    resolve-authority     emits receipt to stdout
    reconstruct           emits plan to stdout
    migration-audit       emits disposition report
    promotion-plan        emits a PromotionPlan (W0 addition, read-only)

STAGED-WRITE (writes only to docs/project_knowledge/generated/, and only
with an explicit publish flag; default is stage-and-diff)
    rebuild [--publish]
    refresh --changed-since <ref> [--publish]

FUTURE (not implemented in W0)
    promote               W4
    cutover               W6+
```

Structural safety properties, enforced by the layering rather than by review:

```text
no CLI command imports a canonical-source writer  — none exists in W0
rebuild/refresh write only under generated/        — a single path guard
                                                     in services/generation.py
resolve-authority cannot return RESOLVED on a conflict — the status is
                                                     computed, never passed in
no command takes an --authority-switch or equivalent flag
exit codes: 0 pass, 1 validation ERROR, 2 usage, 3 unresolved authority
            (distinct from 1 so CI can distinguish "your repo is broken"
             from "this query has no clean answer")
```

Default-stage-not-publish is the choice I'd defend hardest: it means the dangerous direction requires an explicit flag, and a CI job that forgets the flag produces a diff report rather than a commit.

## O. Architecture documentation and visualization

Six documents per Specification 028 §31. For diagrams:

```text
source format   Mermaid, in fenced blocks inside the .md documents
                themselves, not separate .mmd files
rendered        optional committed SVG under architecture/rendered/,
                regenerated by an explicit script, never required for the
                document to be readable
```

Why Mermaid-in-document rather than a separate diagram source: GitHub renders it natively, so the diagram is visible in the repository without any build step; it diffs as text and is reviewable in a PR; it requires no toolchain to read; and keeping it inside the document it illustrates prevents the diagram/prose drift that a separate file invites. The cost is expressive ceiling — Mermaid cannot produce a truly polished presentation-grade figure. I think that trade is right for W0: the requirement is professional and version-controlled, and a genuinely presentation-grade figure can be produced later from the same content if a specific external audience needs it.

The distinction Specification 028 §41 insists on — that a picture of files is not the logical architecture — I'd enforce by making `whole_architecture.md`'s primary diagram show **semantic roles and authority flow** (canonical sources -> semantic control -> derived access -> reconstruction/action -> migration boundary), with the physical directory layout appearing only in a clearly separate, clearly subordinate figure labeled as physical realization.

## P. Test architecture and W0 gates

```text
tests/project_knowledge/
    unit/          pure L0/L2 functions, no I/O, no fixtures on disk
    contract/      schema positive/negative fixture validation
    corpus/        the frozen W0 fixture corpus
    behavioral/    the qualified Candidate 01 hard cases as regressions
    determinism/   byte-stability, rebuild idempotence, full/incremental
```

Gate mapping, with my assessment of each rather than a restatement:

```text
G001 package boundary          trivial, real, keep — an import-path test
G002 eight schemas +/- fixtures strong; the negative fixtures are what
                               give it teeth
G003 parser malformed/CRLF     strong
G004 model without universal IDs  GOOD BUT WEAK AS WRITTEN. "represents ...
                               without universal IDs" is satisfiable by a
                               model that merely *permits* None. I'd
                               strengthen it to assert that no function in
                               the package derives a SemanticId from a path,
                               title, or digest — a source-level test.
                               This is the gate that protects against H3
                               drift, and it should test the absence of a
                               capability, not the presence of an option.
G005 revision helper           strong
G006 identity index rebuild    strong
G007 authority resolver        strong; I'd add UNRESOLVED_SCOPE_REQUIRED
                               explicitly, since the gate text names
                               ambiguity but scope-underspecification is a
                               distinct status per §25
G008 workstream engine         strong
G009 view framework + stale    strong
G010 current-state-core        strong
G011 capture non-authority     GOOD BUT WEAK. Enforcing "validation" is
                               weaker than enforcing structure. I'd add:
                               assert no import path exists from the
                               authority resolver to the capture scanner.
G012 public/private leakage    strong; must run on rendered bytes (Section L)
G013 full/incremental equiv    strong, and my Section H design is chosen
                               specifically to make it provable
G014 CLI determinism/exit      strong
G015 architecture docs + diagram GOOD BUT WEAK. "exists" is checkable;
                               "professional" is not. I'd keep the gate
                               as-is and not pretend otherwise — it is
                               honestly a presence check and should be
                               labeled one.
G016 repo integrity PASS       strong
G017 unit suite PASS           strong
```

**Missing test class I'd add** (as tests, not new gates — I don't think W0 needs an eighteenth gate):

```text
discovery-exclusion       a governed declaration placed under an excluded
                          prefix produces EXCLUDED_BUT_DECLARED, not silence
                          (Section D — this is the mechanism that protects
                          against fixtures becoming authority, and nothing
                          in G001-G017 tests it)
scope-matching table      a truth table over the facet-match grid (Section E)
receipt completeness      every RESOLVED receipt contains all §25 fields
                          plus removal reasons
PKA-W0-J1                 Section J's falsifier
```

No gate is redundant. No gate should be weakened. Three (G004, G011, G015) are weaker than their intent, and two of those (G004, G011) I'd strengthen because they are the two gates guarding the architecture's two most important negative properties — no universal identity, no capture authority.

## Q. Specification 028 amendment audit

```text
REQUIRED_BEFORE_W0
    (none)
```

I found no clause that must be amended before implementation begins. Every concern below is either implementation freedom the specification already grants or evidence-dependent and better decided with W0/W2 data.

```text
SAFE_IMPLEMENTATION_FREEDOM

§3   module list           the four-layer decomposition in Section A keeps
                           every named responsibility explicit and testable;
                           §3 explicitly permits internal decomposition

§12  scope structure       §12 requires "explicit target and scope" without
                           defining scope's shape; Section E's facet model
                           is a permitted concretization

§25  receipt contents      §25 says "MUST record" a minimum; adding scope-match
                           grade and removal reasons is additive

§32  CLI surface           §32 permits additional flags/commands that do not
                           widen authority; promotion-plan is read-only

§31  diagram technology    §31 requires version-controlled, human-reviewable
                           source; Mermaid satisfies it without amendment
```

```text
DEFER_TO_W1_OR_LATER

§8/§5  project_boundary.v1 is the only one of the eight profiles with no
       field contract anywhere in §1-§46 (Section C). W0 can implement it
       minimally from the common envelope plus a free `facts` object. I'd
       want its contract tightened in W1 once the real Project Integration
       Boundary source exists — writing a speculative field list now would
       be inventing requirements, and this is exactly the "under-specified
       profile" the brief asked me to look for.

§20    committed view set — the subject_index / risk_obligation_index
       reservation in Section H. Implement all eight as specified;
       instrument diff churn; revisit at W2 with data.

§17    prose/contract semantic drift — W0 ships the change-asymmetry
       heuristic (Section M). A genuine semantic comparator, if it is ever
       worth building, needs its own design and evidence.
```

## Required conclusion

**1. Preferred W0 architecture, compact.** A four-layer package under `tools/project_knowledge/` — pure value objects, I/O adapters, pure domain logic, orchestration services, CLI — where domain logic never imports adapters. Eight `allOf`-composed profile schemas over a deliberately minimal four-field envelope, with `additionalProperties: false` on every leaf. Byte-level marker parsing with duplicate-key rejection; discovery via `git ls-files` plus a declared exclusion set where every exclusion is recorded and contradictions are flagged. Scope as a conjunctive facet set with a four-grade match ordering and `UNDERSPECIFIED` as a first-class outcome. A nine-step deterministic resolver where authority class filters candidates before any scoring and joint authority may only constrain, never add. A flattened identity index for bounded lookup over complete transition history. One view engine where incremental refresh narrows which views regenerate but never which inputs they see. Model assistance confined to producing a `TaskIntent`; everything after it deterministic.

**2. Three highest-risk implementation choices.** (i) Scope semantics — I am concretizing something Specification 028 left open, and a wrong facet model would quietly distort every authority resolution downstream. (ii) Discovery exclusion by declared prefix — it is the single point where a fixture or generated file could be mistaken for authority, and its correctness depends on a config constant staying right. (iii) Always-full-inputs incremental refresh — I am buying provable equivalence with recompute cost, and if the corpus grows far beyond current projections that trade could need revisiting.

**3. Strongest simplification.** Making incremental refresh narrow only the *set of views*, never the *inputs per view*. It converts the hardest W0 gate from an empirical equivalence test into a structural argument, and removes an entire class of state-patching bugs.

**4. Strongest place more structure is necessary.** Scope. "Match the scope" is not implementable, and `UNRESOLVED_SCOPE_REQUIRED` cannot be derived without a real match ordering. This is the one place where W0 must add genuine structure rather than reuse a prototype behavior.

**5. Disposition of the Claude-history activation failure.** Not evidence for a new topology registry. It is a dispatch failure, not a reconstruction failure — the material was present, routed, and documented, and no query was issued. Candidate 01's existing mechanisms cover the class when invoked and do not cause invocation for a conversational question; that residual gap is a collaborator-protocol matter, not a W0 module. The only change I'd make is a generated "governed domains present" line in `CURRENT_STATE_CORE.md`, which cannot drift because it is derived. Falsifier: `PKA-W0-J1`.

**6. Specification 028 amendment before coding.** No. Five items are implementation freedom the specification already grants; three are deferred with reasons.

**7. Candidate 01 / H3 reopen.** No. Producing this design surfaced no contradiction with the selected logical architecture. The identity model stays selective, joint authority stays exceptional and constrained, and nothing forced a universal object substrate — the one place it could have crept in (auto-minted IDs) is closed by an explicit negative test.

**8. What I most want compared against ChatGPT's design.** In priority order: (i) **scope semantics** — whether ChatGPT concretized it at all, and if so whether the two models agree, since divergence here is the most consequential silent incompatibility available; (ii) **the incremental-refresh equivalence strategy** — full-inputs versus patched state is a genuine fork with different correctness properties, and I want to know if the other design took the faster road; (iii) **the discovery/exclusion mechanism**, because both designs must solve "don't mistake fixtures for authority" and there may be a better answer than declared prefixes; (iv) whether ChatGPT also identified `project_boundary.v1` as the under-specified profile, which would be independent confirmation rather than my preference; (v) the layering question — whether a flat responsibility package was preferred, and if so how circular imports are prevented.

```text
INDEPENDENT_W0_DESIGN_CONTAMINATED: NO
SPECIFICATION_028_AMENDMENT_REQUIRED_BEFORE_W0: NO
LOGICAL_ARCHITECTURE_REOPEN_REQUIRED: NO
H3_REOPEN_TRIGGERED: NO
W0_IMPLEMENTATION_SAFE_AFTER_COMPARATIVE_RECONCILIATION: YES
```
