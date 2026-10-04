# MC-0030 Message 001: Claude Independent R0 Physical Realization Architecture — LEDGER-KERNEL

```text
Thread                          MC-0030
Message                         001
Author / collaborator           Claude
Role                            INDEPENDENT REVIEWER / COUNTER-DESIGNER (blind independent pass)
Interaction environment         Claude
Interaction session             conversation "04 - Assurance and Delivery Architecture Design"
                                (STATE.json lists the Claude slot as claude-05; see §0)
Coordination branch             v1-source-vault-bootstrap-resume
Head verified                   64fa62f5c19c419937eb4ebc58b8b72734a692af
Frozen substantive base         c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc
Selected logical target         THIN_CENTRED_HYBRID_V03 (D-036)
Neutral R0 basis                Research 503 + 506 + 507 (R0-R01..R0-R62)
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Verification, blindness and session disclosure

```text
remote head (git ls-remote)        64fa62f5c19c419937eb4ebc58b8b72734a692af = expected
current_routing.json boundary      claude-blind-design
MC-0030 lifecycle / phase          OPEN / R0_CLAUDE_INDEPENDENT_DESIGN_AMENDED
next_expected_actor                claude
independence.status                BLIND_TO_CANDIDATE
selected logical target            THIN_CENTRED_HYBRID_V03; physical architecture not selected;
                                   implementation and migration not authorized
routing contradiction              none
```

**Read by exact path at head:**

- `docs/current_routing.json`
- MC-0030 `STATE.json`, `THREAD.md` and `BRIEF.md`
- Research 503, 506 and 507

**Read at frozen ref `c459e9c8`:**

- Research 500, 501 and 502;
- D-036 in `docs/DECISIONS.md`;
- file *names* only for `docs/research/493..502` and the `docs/` top level.

I also used my own MC-0028 and MC-0029 knowledge, which predates the frozen base: R7, R8-A, WMR-H, WARRANT-F, AO-3..AO-7 and the V01–V03 evidence.

**Not read:**

- Research 504 and 508;
- Checkpoints 841 and 844;
- Research 505 and 509 (handoff records, not needed);
- `docs/CURRENT_STATE.md` and `docs/ARCHITECTURE_PROGRAM_OVERVIEW.md` at any revision;
- any comparative MC-0030 artifact.

No broad current-branch search was run. **No accidental exposure occurred.**

**Session disclosure.** MC-0030 `STATE.json` names the Claude participant session `claude-05`. This message was authored in the Claude conversation titled "04 - Assurance and Delivery Architecture Design". That conversation carries MC-0028/MC-0029 context, all of which predates the frozen base and is permitted by `known_exposures`. The next-actor role (`claude`) matches. The label difference is recorded for the thread record.

## 1. Executive summary

**LEDGER-KERNEL** realizes V03 as **five physically separated concerns with one direction of authority**:

```text
1  ACCEPTANCE LEDGER (authority)      immutable, owner-signed, Git-native records of every
                                      governing act: exact package shown, decision, accepted
                                      effects, completion contracts, lineage. Append-only by
                                      construction. The ONLY normative source.

2  NATURAL-OWNER FACT SOURCES (J2)    realization manifests co-located with what realizes;
                                      execution receipts; activation/control records; WARRANT-F
                                      evidence/decisions. Each owned where it naturally lives,
                                      revision-bound, never normative.

3  PURE KERNEL (computation)          one deterministic library + CLI: ledger fold, lineage
                                      resolution, versioned predicate registry, J3 derivation,
                                      control compilation, orientation, navigation, validation.
                                      No state of its own; same inputs -> same bytes.

4  DERIVED PLANE (never authority)    SQLite/FTS index, J3 snapshots, orientation, navigation
                                      maps, compatibility projections — rebuilt from 1+2,
                                      published to a separate derived ref and CI artifacts,
                                      never committed to the authority branch.

5  EXECUTOR PORT (outside world)      provider-neutral action/receipt contract; Codexless
                                      Runtime Bridge, GitHub connector, Claude-side connector,
                                      local CLI and humans are adapters. Generic bridge is
                                      external infrastructure; ADS owns only its policy pack,
                                      adapter, version pin and qualification.
```

Seven design decisions carry most of the weight:

```text
D1  Authenticity by OWNER-HELD SIGNING KEY, not by GitHub identity.
    All agents act through the owner's shared GitHub identity (MC-0028), so platform approval
    cannot prove the owner decided. An acceptance is valid only when the commit adding its
    decision record is signed by a key in a governed allowed-signers list that no agent
    holds. Hardware or OS-keychain keys need physical presence. Weaker attestation classes
    exist but are visible and cannot authorize consequential effects.

D2  Content-canonical digests for semantics, Git-blob digests for carriers.
    Semantic identity hashes parsed canonical content, which is immune to CRLF/LF and
    formatting. File provenance hashes committed Git blobs. Working-tree bytes are never a
    hash basis. This removes the recurring hash-basis defect class by construction (R0-R23).

D3  Path-independent identities without global counters.
    Machine identities are collision-free ULID-style IDs minted at drafting. Human ordinals
    (Research N, D-N) become display aliases. Concurrent branches never collide on identity.

D4  Linear, merge-queued authority branch.
    Ledger order = first-parent order of the protected accepted-state branch, advanced only
    by exact-result evaluation. This one invariant gives deterministic folds, effective-
    boundary ordering and stale-write protection.

D5  Derived plane on a separate ref.
    Generated orientation, navigation, indexes and compatibility projections live on a
    bot-maintained derived ref bound to source-commit digests. Connector-only agents can read
    them; they can never be committed into, or confused with, authority. No regeneration
    commit loops.

D6  Relation-first semantic organization.
    Navigation, AO activation and impact analysis run primarily over the typed graph V03
    already produces (effects, subjects, lineage, completion, coverage, evidence, carrier
    links), plus lexical search. A small concern vocabulary is a bounded, governed extension
    point, not a primary hierarchy. Research 217 is the comparator.

D7  Executors observed, not trusted.
    Every action yields a normalized ExecutionReceipt. Executors that cannot emit receipts,
    such as the GitHub connector, get receipts derived by a verifier from observable Git
    facts, exactly as D-1's J2 facts were. The attestation class is explicit. No executor is
    semantic authority.
```

The rest of this message specifies each element, compares three materially different alternatives, assigns dispositions to current mechanisms, and names the probes that should run before physical-target selection.

## 2. First principles that drive the design

```text
FP-1  Authority must be cheap to verify and impossible to obtain by accident.
      -> signed, immutable, few records; everything else derived.
FP-2  The owner is a scarce reviewer, not an operator.
      -> the owner sees rendered meaning and signs; never edits schemas or runs pipelines.
FP-3  Agents are many, concurrent, provider-diverse and fallible.
      -> no shared mutable files on the authority path; identities collision-free; every
         consequential agent action verified from observable facts.
FP-4  Most project knowledge is NOT governing semantics.
      -> keep it human (Markdown carriers); link it typed and cheaply; never force it into
         the kernel.
FP-5  Derived things rot; sources do not.
      -> derived artifacts are disposable, digest-bound to sources and fail-visible when stale.
FP-6  Git is already the project's durable, reviewable, distributed substrate.
      -> use it as the authority store; reject a second authoritative store unless it wins
         decisively.
FP-7  Proportionality.
      -> no daemon, no server database, no new hosted service is required for correctness.
```

## 3. Preferred architecture: concrete repository and software boundaries

### 3.1 Repositories

```text
REPOSITORY                                  OWNS                                   VISIBILITY
autonomous-data-science-system (ADS)        Product; Project System instance; ledger;  public
                                            knowledge carriers; ADS executor policy
                                            pack and adapter integration
ADS private companion (exists; to be        private evidence, private carrier          private
  classified per Research 506 §2B)          content, host-specific ADS deployment
                                            state, salted-commitment preimages
codexless-runtime-bridge (future; not       generic bridge product                     public or
  created now)                                                                         product choice
host deployment repo/state (future;         machine install, credentials refs, logs    private
  classification)
```

The PSMF framework is **not** extracted now (Research 309 defers it). It is kept extractable by the framework/instance seam inside `project/system` (§3.2).

### 3.2 ADS repository layout (target)

This refines the accepted R8-A tree rather than replacing it. R8-A already won on evidence; its decisions are reused where they still win.

```text
README.md                         human entry
project_anchor.json               break-glass locator: authority branch, ledger root,
                                  allowed-signers path, kernel version, private companion ref
.github/                          thin triggers + required checks (WARRANT-F adapters only)

product/                          ADS Product (unchanged boundary; never imports project/)
  runtime/  interaction/

project/
  system/                         JW1 = the V03 kernel (Python package, own lock)
    src/ads_project_system/
      framework/                  generic, PSMF-extractable
        model/                    typed records + canonicalization + digests
        ledger/                   load, verify signatures, fold (current set at ledger order)
        lineage/                  CARRY_FORWARD..REINSTATE, portion closure, boundaries
        completion/               contracts, components, composition rules
        predicates/               VERSIONED PREDICATE REGISTRY (pure functions + semver)
        j3/                       derivation engine, regression, review routing
        compile/                  ActionContract / ControlObligationSet compiler
        orient/                   orientation + next-gap + enforcement/authorization views
        navigate/                 relation graph, carrier links, search adapters (§9)
        validate/                 structural + semantic validators with coded diagnostics
        port/                     executor-port contract types (ActionRequest/Receipt)
        cli/                      `ads ...` commands
      instance/                   ADS-specific: owner classes, branch roles, consequence
                                  classes, concern vocabulary, review routing table
    tests/                        unit, golden, property, regression corpus (D-1/D-2/D-3)

  engineering/                    independent Python project (accepted R8-A amendment)
    assurance/                    WARRANT-F kernel (claims, warrants, gates, ratchet)
    executors/
      contract/                   pinned copy of port schema version used by ADS
      ads-policy-pack/            ADS workspace policy for bridge/other executors (data)
      adapters/                   runtime-bridge, github-observed, local-cli, manual
      qualification/              ADS qualification tests against pinned executor versions
      executor-lock.toml          exact qualified Runtime Bridge release + digest
    migration/                    R3-R7 tooling: inventory, shadow, parity, wave, rollback
    ci/                           CI adapter code invoked by .github workflows

  ledger/                         AUTHORITATIVE V03 RECORDS (append-only; §4)
    acceptances/<accept-id>/
      package.toml                accepted effects + bindings (structured, reviewable)
      shown.md                    exact owner-visible rendering (generated, then frozen)
      decision.json               decision payload + digests (commit must be owner-signed)
    domain-contracts/<contract-id>/<revision-id>.toml   accepted domain completion contracts
    allowed_signers               governed signer list (changes are themselves acceptances)

  control/                        AO control state (machine-written JSON shards; WMR-H)
    authority_mode.json           single operational authority pointer (Spec 028 until cutover)
    focus/  threads/  bridge/     sharded control records with expected-revision fields
    receipts/<yyyy>/<receipt-id>.json   control/execution receipts (immutable, in-tree)
    realization/<owner>/...       J2 manifests for realizers that are not repo artifacts
                                  (procedures, migrations, external deliverables)

  knowledge/                      human carriers per R7: governance/ evidence/ operations/ history/
  research/  reproductions/       per R8-A
```

**Where J2 manifests live.** A realizing artifact in the repository carries its own manifest next to it, for example `project/engineering/assurance/REALIZES.toml` or `product/runtime/.../REALIZES.toml`. The manifest changes in the same commit as the code it describes, so revision binding is automatic. That is the natural-owner rule, applied physically. Realizers without a repository home use `project/control/realization/`.

**Outside the qualified tree:**

- WARRANT-F decision evidence — content-addressed receipts, per the accepted WARRANT-F non-self-mutating rule;
- the derived ref `derived/<authority-branch>`;
- the private companion.

### 3.3 Dependency directions

```text
product/            -> nothing in project/  (reads exported derived JSON only, if ever)
project/system      -> stdlib + small pinned deps; never engineering/
project/engineering -> invokes project/system via CLI/result contract (WF-A15); never imported back
executors (external)-> know nothing of V03; receive policy + ActionContract data only
derived plane       <- built by system CLI in CI; consumed by humans/agents/Product
```

## 4. Storage and source of truth

### 4.1 What is authoritative

```text
AUTHORITATIVE (durable, verified, never derived)
  ledger/acceptances/*          J1 governing acts
  ledger/domain-contracts/*     accepted domain completion contracts (pinned revisions)
  ledger/allowed_signers        authenticity root
  project_anchor.json           locator
  control/authority_mode.json   operational authority pointer (governed transitions only)

NATURAL-OWNER FACTS (durable, revision-bound, not normative)
  REALIZES.toml manifests       coverage facts
  control/receipts/*            execution / control receipts
  control/* shards              activation and operational control state
  WARRANT-F evidence store      evidence, qualification, assurance decisions
  private companion             private facts (referenced by salted commitment)

HUMAN CARRIERS (authoritative as text; machine-relevant only through ledger references)
  knowledge/*, research/*       narrative, rationale, evidence prose

DERIVED (disposable, digest-bound)
  everything on derived/<branch>, SQLite/FTS, J3 snapshots, compiled controls, CI artifacts
```

### 4.2 Acceptance record format

`package.toml` is TOML because humans and agents review it in diffs (WMR-H's human-authored machine-semantics rule). An illustrative shape:

```text
[acceptance]
id                  = "ACC-01J9Z..."              # ULID-style, minted at drafting
kind                = "OWNER_DECISION"            # closed list of governed acceptance kinds
supersedes_draft    = []                          # prior AMEND drafts
source_carriers     = [{path="...", git_blob_sha256="..."}]
effective_boundary  = "LEDGER_ORDER"              # or explicit later ledger position / condition
creates_no_effects  = false

[[effect]]
id                  = "AE-01J9Z..."
statement           = "..."                       # accepted human statement (bound)
type                = "REQUIRE"                   # REQUIRE|PROHIBIT|GATE|AUTHORIZE|DEFER|LIFECYCLE|SEQUENCE
subjects            = ["AE-..", "ART:path#sym", "CTR-.."]  # typed refs (navigation + activation)
accounting          = "REALIZATION_TRACKED"       # or NO_REALIZATION_REQUIRED + reason code
completion          = {authority="GOVERNING_ACCEPTANCE", components=["C1","C2"],
                       rule="ALL_REQUIRED", evidence=true, qualification=true, activation=false}
# or completion = {authority="ACCEPTED_DOMAIN_CONTRACT", contract="CTR-..", revision="REV-.."}
standing            = {mode="ENFORCED", control="CTL-.."}  # or DETECTIVE_ONLY (PROHIBIT/GATE/SEQUENCE)
authorization       = {exact_scope=..., receipt_required=true}       # AUTHORIZE only
lineage             = {relation="REPARTITION", predecessors=[..], mapping=[[..]],
                       retired=[..], unaffected=[..], realization="OPEN_RESET",
                       carry=[..], deferral_rebind=[..]}             # LIFECYCLE only
```

`decision.json` is machine-written:

```text
{acceptance_id, package_canonical_sha256, shown_sha256, decision: "ACCEPT|AMEND|REJECT",
 verbatim_decision: {mode: "PUBLIC_TEXT"|"SALTED_COMMITMENT", value|commitment},
 drafter_provenance: {actor, model, session}, reviewer_aids: [second-model review refs],
 signer_fingerprint, decided_at}
```

### 4.3 Hash bases (R0-R23)

```text
semantic digest       SHA-256 over canonical JSON of the parsed record (sorted keys, UTF-8,
                      no insignificant whitespace, normalized line endings inside strings).
                      Used for effect identity continuity, package binding, CARRY_FORWARD
                      equality, J3 input binding.
file provenance       SHA-256 over committed Git blob bytes at a commit (never working tree).
                      Used for carrier/manifest/artifact binding.
J3 / derived          SHA-256 over canonical serialization of outputs + input digest manifest.
```

The kernel's own test suite carries witness fixtures: CRLF variants of every record type must produce identical semantic digests and different blob digests.

## 5. Authority and authenticity

### 5.1 Acceptance flow

```text
1  DRAFT      agent (any provider) writes package.toml in a work branch; kernel validates
              grammar, closed accounting, lineage closure, completion authority, policy.
2  RENDER     `ads render ACC-..` produces shown.md: source meaning beside proposed effects,
              compact lifecycle diff, accounting, completion. The exact bytes are frozen and
              digested; this IS "the package shown to the owner" (R0-R01).
3  ADVISE     optional second-model faithfulness review (advisory; V03 §18); findings
              attached as reviewer_aids, never gating validity.
4  DECIDE     owner sees shown.md (PR view, chat or local), answers ACCEPT / AMEND / REJECT.
              AMEND -> new draft revision; nothing accepted.
5  SIGN       decision.json is committed in a commit SIGNED by the owner's key (§5.2).
6  ADMIT      merge queue evaluates the exact resulting ledger: signature valid, signer in
              allowed_signers at the parent revision, package digest = shown digest binding,
              fold valid (no lineage conflict, no double retirement, closure intact).
7  APPEND     fast-forward of the authority branch. Ledger order is fixed.
```

### 5.2 Why owner-held signing keys

- **The shared-identity problem.** MC-0028 established that ChatGPT, Claude, Codex and the bridge all act through the owner's GitHub identity. A GitHub approval, a "verified" web commit or an attested agent transcription therefore cannot prove the owner decided.
- **What a key adds.** A signing key held only by the owner (hardware token or OS keychain, requiring user presence) gives tamper-evident, chat-independent authenticity (R0-R02) verifiable with standard `git verify-commit` against `allowed_signers`.
- **Burden.** The bridge, or any executor, can prepare the commit; only the owner's touch signs it.

Attestation classes are explicit:

```text
OWNER_SIGNED            required for: governing acceptances creating/retiring consequential
                        effects, domain-contract acceptance, allowed_signers change,
                        authority_mode change (cutover/rollback), kernel grammar/predicate
                        semantic changes
OWNER_ATTESTED          verbatim owner text captured by an executor with provenance, no
                        signature; allowed only for NON-consequential acceptances (e.g.
                        PRINCIPLE-only, NO_REALIZATION_REQUIRED documentation acts); visible
                        in every view; upgradable by later signature
INVALID                 anything else; never folds into the current set
```

### 5.3 No accidental competing authority (R0-R03)

The fold reads only `ledger/` records whose admitting commit verifies. Derived outputs carry a `derived: true` header and an input-digest manifest, and live on another ref. Validators reject any ledger record citing a derived artifact as source. Model proposals exist only as drafts on work branches until signed.

## 6. J1, J2 and J3 realization

### 6.1 J1

J1 is the ledger fold:

```text
current_set(ledger@L) = fold over acceptances in first-parent order up to L:
    add effects; apply LIFECYCLE relations at their effective boundaries;
    produce: current effects, retired history, lineage graph, active completion contracts,
             standing bindings, authorizations (with consumption state from receipts),
             LEGACY_UNRECONCILED registry entries.
```

Historical meaning is immutable (R0-R04): records are never edited. Correction of a drafting error is itself an acceptance (CLERICAL versus NORMATIVE correction, per MC-0029 T-2).

### 6.2 J2

J2 consists of natural-owner facts:

```text
REALIZES.toml      realizer id, owner, artifact refs (path+symbol), covered
                   (effect_id, component) pairs, FULL/PARTIAL, revision = containing commit
receipts           ExecutionReceipt / control receipts (§10)
evidence           WARRANT-F evidence + qualification decisions (content-addressed)
activation         control/ shards (e.g. deployment/activation facts)
```

Natural owners publish facts without touching J1 (R0-R12). The kernel rejects any manifest that declares or alters completion criteria (INV-07).

### 6.3 Predicates and J3

The predicate registry is `framework/predicates/` (R0-R13):

- Each predicate is a pure function with an ID, a semantic version, a typed input schema and golden tests.
- The registry version is part of every J3 input digest.
- WARRANT-F consumes the *same* predicates through `ads predicates eval` (JSON contract). There is one executable semantic source, and engineering never re-implements it.

J3 derivation (R0-R14, R0-R15):

```text
j3(ledger@L, facts@F, registry@V) -> snapshot S  (pure, deterministic, digest = H(inputs, outputs))
  per current REQUIRE: coverage completeness (FULL/PARTIAL composition), evidence/freshness,
  qualification, activation, deferral, conflict, satisfaction, regression vs previous S'
  per PROHIBIT/GATE/SEQUENCE: enforcement binding status; detective violations
  per AUTHORIZE: exercise status from receipts
  review routing: (condition -> resolving owner class) table from instance/
```

Stratification is enforced structurally, mirroring D-3. Downstream assurance about snapshot S binds S's digest. Feedback is admitted only as facts at a later revision (`facts@F+1`), so a same-revision cycle cannot be expressed.

### 6.4 Orientation (R0-R16, R0-R17)

`ads orient` renders the four-state orientation plus `next_gap`, review ownership, and the enforcement and authorization views. It is versioned with the kernel and published only to the derived plane. Every REVIEW_REQUIRED item carries a resolving owner class and a reference.

## 7. Lineage and realization succession

Lineage is declared inside LIFECYCLE effects of acceptances (§4.2) and resolved by `framework/lineage`:

```text
relations         CARRY_FORWARD | REPLACE | SPLIT | MERGE | REPARTITION | RETIRE | REINSTATE
portion closure   every scoped predecessor portion mapped once / retired / unaffected (validator)
boundary rule     a predecessor contributing to >1 successor: synchronized boundaries (validator)
currentness       fold-time resolution at ledger position
succession        realization_initialization = ordered 0..N records {effect_id, mode}
                  default OPEN_RESET; CARRY_FACTS_FOR_REVALIDATION only via valid carry block;
                  deferral rebinding only by explicit successor reacceptance
REINSTATE         new identity + REINSTATES edge; retirement history preserved
```

The D-2 fixtures and both independent evaluators become the lineage regression corpus. The production implementation must pass all 14 fixtures; any disagreement is a kernel defect, not a fixture change.

## 8. Control compilation and execution contracts (R0-R18..R0-R21)

`ads compile` deterministically turns the current set plus J3 into versioned control artifacts:

- `ActionContract` per AUTHORIZE / GATE / SEQUENCE;
- `ControlObligationSet` per scope;
- gate inputs for WARRANT-F.

Each artifact binds input digests, is invalidated when stale, and is never authority.

AUTHORIZE exercise binds `{authorization effect id, exact scope, ActionContract digest}` into the ActionRequest. The resulting receipt is the J2 fact that consumes the authorization.

## 9. Semantic organization, discovery and navigation (R0-R45..R0-R54)

### 9.1 Requirements derived from first principles

```text
N1  "Where should I look?" for a human with no archaeology        (R0-R48)
N2  bounded, provenance-carrying context for a fresh agent        (R0-R49)
N3  candidate surfacing for AO activation, never authority        (R0-R50)
N4  impact analysis across cross-cutting knowledge                (R0-R51)
N5  authoritative vs probabilistic signals always distinguishable (R0-R52)
N6  independent dimensions not collapsed into one hierarchy       (R0-R53)
N7  near-zero extra authoring burden; organization must not decay
```

### 9.2 Families compared

```text
F-TAX   controlled subject/facet taxonomy (Research 217 family)
        + strong human browsing; measured 9/9 scenario recall vs legacy map
        - authoring + maintenance burden; vocabulary drift; R2-era evidence showed category
          judgments are the least reproducible construct; conflates concern with ownership
F-GRAPH typed relational organization
        + V03 already PRODUCES most edges as a by-product (effect subjects, lineage,
          completion, coverage, evidence, receipts); deterministic; impact analysis native
        - prose-only knowledge (research history, rationale) is weakly connected unless linked
F-SEARCH retrieval-first (lexical FTS +/- embeddings)
        + zero authoring; good recall for fresh agents
        - non-deterministic ranking; poor for "what governs X"; must never imply authority
F-HYB   deliberate hybrid (preferred, below)
```

### 9.3 Preferred: relation-first hybrid

```text
DIMENSION              SOURCE                                    AUTHORITY CLASS
information role/owner location (R7 tree)                         structural, deterministic
governing relations    ledger (subjects, lineage, completion)    AUTHORITATIVE-DERIVED
realization relations  REALIZES manifests, receipts, evidence    FACT-DERIVED
carrier links          small source-owned `links` metadata in    SOURCE-OWNED
                       carriers: {about: [AE-..|CTR-..|ART:..|ACC-..]}
lifecycle/currentness  fold                                       AUTHORITATIVE-DERIVED
workstream/focus       control/                                   CONTROL
concerns               OPTIONAL governed vocabulary (instance/),  SOURCE-OWNED, bounded
                       source-owned assignment, cap on size
search relevance       SQLite FTS5; optional embedding cache       PROBABILISTIC (labelled)
```

Generated navigation surfaces, all on the derived plane:

- **Effect dossier:** statement, source, lineage, completion, coverage, J3 state, evidence and linked carriers.
- **Artifact "what governs this?":** reverse coverage plus subjects.
- **Owner-area maps.**
- **Recent-acceptances digest.**
- **Search results:** always showing authority class and source digest.

**AO activation** (N3) is a deterministic traversal: event → touched paths, IDs and subjects → affected current effects (via subjects and coverage) → candidate obligations. Search may *add* candidates, but they are labelled PROBABILISTIC_CANDIDATE and can never satisfy or suppress an obligation.

### 9.4 Disposition under R0-R54

- **Selected now:** the relation-first core and the authority labelling of every signal. These follow from V03 and impose no new authoring.
- **Frozen as a bounded unresolved interface:** the `concerns` vocabulary (empty or minimal at start) and any embedding-based retrieval. The interface (`instance/concerns.toml`, the carrier `links.concerns` field, the projection schema) is fixed so the physical architecture can proceed. Whether concerns are needed, and at what size, is decided by probe P4 against Research 217 as comparator.
- The old 18-subject vocabulary is **not inherited**.

## 10. External execution boundary (R0-R55..R0-R62)

### 10.1 The executor port (owned by the Project System)

```text
ActionRequest   {request_id, actor, executor_class, capability, workspace, ActionContract
                 digest, authorization effect id (if any), inputs (refs/digests),
                 expected preconditions (branch head, paths), policy pack version}
ExecutionReceipt{request_id, executor {id, product, version}, capability, started/ended,
                 outcome, outputs {commit, parent, changed_paths, artifacts+digests},
                 provider_native_refs, attestation_class, policy decisions applied}
attestation     EXECUTOR_RECORDED      bridge/local adapter wrote the receipt at execution
classes         OBSERVED_FROM_GIT      verifier reconstructed it from Git facts (GitHub/Claude
                                       connectors cannot emit receipts; D-1 proved this path)
                SELF_REPORTED          agent statement only -> never sufficient for
                                       consequential authorization consumption
```

Receipts land in `control/receipts/`, are folded into J2, and are consumed by WARRANT-F through the same predicates (R0-R59). No executor writes `ledger/`, except by preparing a commit the owner signs.

### 10.2 Ownership split (Research 506 applied)

```text
GENERIC_CORE (bridge product)      capability runtime, workspace sandboxing, Git/GitHub ops,
                                   process control, credential mediation, receipt emission
                                   in the PORT schema, capability descriptor, release/update
GENERIC_OPTIONAL_MODULE            browser automation, tool mediators, etc.
ADS_CAPABILITY_OR_POLICY_PACK      ADS repo: allowed paths per branch role, forbidden actions,
                                   acceptance-signing handoff, ADS bounded procedures as
                                   declarative pack — DATA, not bridge code
HOST_PRIVATE_DEPLOYMENT            install, keys/credential refs, logs (host repo/state)
HISTORICAL_OR_EXPERIMENTAL / RETIRE classified during the extraction program
```

Key properties:

- **Capability discovery and compatibility (R0-R60):** each executor publishes a capability descriptor plus port-schema version. ADS pins `executor-lock.toml` and runs `executors/qualification/` against the pinned version. An incompatible version results in DEGRADED mode, not silent use.
- **Multi-project:** one installed bridge serves many workspaces through per-workspace policy namespaces and credentials. The bridge knows workspace IDs and policy data, never ADS semantics.
- **Fallback (R0-R60):** if the bridge is unavailable, AO routes the same ActionRequest to another adapter (GitHub connector with OBSERVED_FROM_GIT receipts, local CLI, or manual human) and records the mediation class (MEDIATED / COOPERATIVE / UNMEDIATED, MC-0029 AMEND-6). Consequential actions requiring EXECUTOR_RECORDED attestation wait or route to review.
- **Timing (R0-R62):** no extraction now. R1 freezes the port schema and the ADS requirements list from §10.1. The dedicated bridge program follows.

## 11. Validation, test and CI architecture

The accepted WARRANT-F model is reused; here is the concrete realization.

```text
TEST LAYERS (project/system/tests)
  unit          pure kernel modules
  golden        D-1, D-2, D-3 fixtures + evaluators as permanent regression corpus
  property      lineage invariants (closure, acyclicity, boundary sync), fold commutation
                over independent acceptances, canonical-digest invariance under formatting
  witness       seeded violations per validator (MC-0027 lesson): every gate must be shown
                able to fail
  rebuild       full rebuild == incremental refresh (byte-identical derived outputs)
  migration     parity: V03 shadow decisions vs Spec 028 decisions on real scopes

CI (thin .github triggers -> project/engineering/ci)
  PR (any)            G1: kernel validate + affected tests + policy lint
  merge queue         G2 exact-result: full validate, signature verification for new
                      acceptances, fold admission, rebuild equivalence (sampled), assurance
                      gates; ONE required status per gate class
  post-advance        derived-plane publish to derived/<branch>; artifact upload
  scheduled           full rebuild from scratch; hermeticity; dependency/security; drift
                      sentinels; break-glass drill (anchor -> ledger -> rebuild)
```

Diagnostics are coded and attributable (R0-R40). Every failure carries `{code, record id, field, resolving owner class, remediation hint}`; there are no generic INVALID states.

## 12. Branch, workflow and concurrency (R0-R27, R0-R30)

```text
BRANCHES
  authority branch (main after cutover; designated accepted-state branch before)
      protected; linear history; advanced ONLY by merge queue; no direct pushes
  work/<actor>/<topic>   any collaborator; short-lived
  derived/<authority>    bot-only, force-updated, never authority

CHANGE CLASSES (governed path policy in instance/, enforced in G2)
  GOVERNING    ledger/*, allowed_signers, authority_mode, predicate semantics, grammar
               -> owner-signed decision required
  REALIZATION  code, manifests, tests, executors, migration tooling
               -> assurance gates; no owner signature unless a GATE effect demands it
  KNOWLEDGE    carriers, research, collaboration messages
               -> light gates; auto-merge when green
  DERIVED      bot only, derived ref only

CONCURRENCY
  identities   ULID-style, minted at draft time: no counter collisions across branches
  ledger       new files only -> no textual conflicts; LOGICAL conflicts (two acceptances
               retiring the same effect, overlapping lineage) detected by exact-result fold
               in the merge queue; the later one fails and needs a rebased re-decision
  control      every shard carries expected_revision; stale writes rejected (R0-R27)
  threads      per-thread STATE shards; inbox generated (derived), never hand-maintained
```

**Collaborators without merge-queue access** (connector-only agents) push to `work/` branches. The bridge or CI opens the PR. Interruption is resumable from Git plus control receipts alone (R0-R28).

## 13. Public and private (R0-R26)

Private facts live in the private companion. Public records reference them as:

```text
PrivateRef {store, id, salted_sha256}
```

The salt is kept private, which prevents brute-forcing short private texts such as verbatim owner decisions. A public-only rebuild produces J3 with `PRIVATE_UNAVAILABLE`. Affected requirements orient as REVIEW_REQUIRED (owner class INTEGRATION_OWNER), never SATISFIED. Degradation is visible, not silent. CI leak claims (WARRANT-F AC8) scan ledger, carriers, receipts and derived outputs before publication.

## 14. Recovery and rebuild (R0-R22, R0-R24, R0-R25)

```text
break-glass   project_anchor.json -> authority branch -> ledger/ (human-readable TOML +
              shown.md) -> allowed_signers -> `git verify-commit` -> `ads rebuild --full`
loss of derived plane      rebuild from sources; equivalence check vs last published digests
loss of SQLite/caches      irrelevant to correctness
loss of WARRANT-F evidence affected J3 items regress to EVIDENCE gaps (visible), not silent pass
fail-visible states        STALE, CONFLICT, ORPHAN, CYCLE, PARTIAL_MIGRATION,
                           UNACCOUNTED, LEGACY_UNRECONCILED, PRIVATE_UNAVAILABLE, UNSIGNED
```

## 15. Migration, shadow and cutover (R0-R31..R0-R36)

```text
R3 INVENTORY      by responsibility and accepted obligation: every live Spec 028 /
                  continuity obligation gets a legacy ID `LEG:<source>#<anchor>` registered
                  as LEGACY_UNRECONCILED (visible in orientation; never counted complete)
R4 SHADOW         reconciliation acceptances create V03 effects with LIFECYCLE REPLACE/SPLIT
                  from LEG: identities (realization OPEN_RESET); kernel computes J3/orientation
                  in shadow while authority_mode = SPEC_028; parity harness compares DECISIONS
                  (e.g. admissible? satisfied? next gap?) on real events, not bytes
R5 WAVES          scope = one responsibility area; entry: lineage closure, no duplicate
                  authority (validator), parity window passed, reverse-reference safety,
                  rollback drill; exit: wave receipt
COMPATIBILITY     current_routing.json, CURRENT_STATE successors, KNOWLEDGE_MAP successor
                  = generated on the derived plane only while a named transition needs them;
                  each has a retirement condition
R6 CONFIRMATION   fresh evaluators (different models, no MC-0030 context) on the real
                  implementation + migrated state; P1-P7 rechecked
R7 CUTOVER        authority_mode change = OWNER_SIGNED acceptance; rollback = signed
                  reverse transition within a declared window; ledger is append-only, so
                  rollback never deletes V03 records, only switches the pointer
```

Physical and semantic migration are never done in the same step (MC-0029 KEYSTONE rule). File moves into the R8-A tree are a separate, authorized wave with path-to-ID redirect validation.

## 16. Project versus ADS Product boundary (R0-R37)

The kernel is Project-only. The Product never imports `project/`. If Product features ever need Project governance information, for example a cockpit showing project state, they read exported derived JSON with a versioned schema. The Product's own runtime semantics stay Product-owned. V03 governs Project development, not Product behaviour, unless an accepted Project effect explicitly covers a Product deliverable through REALIZES manifests.

## 17. Observability and architecture evolution (R0-R40..R0-R42)

**Metrics**, published on the derived plane:

- unaccounted effects;
- LEGACY_UNRECONCILED count by area;
- REVIEW_REQUIRED backlog by owner class;
- J3 regressions;
- stale derived outputs;
- rebuild time;
- signature failures;
- degraded executor routes;
- authorization consumption;
- leak-check results.

**Evolution:**

- The grammar, predicate semantics, routing table, concern vocabulary, orientation derivation and executor port schema are versioned.
- Changing any of them is a GOVERNING change: an owner-signed acceptance under AO-4.
- Domain extensions register through a plugin interface (Python entry points) with their own contract schemas. They cannot add kernel consequence types without a governed grammar change, which keeps the kernel from becoming a universal type system (R0-R41).

**Documentation from the same boundary (R0-R42).** Architecture docs are human carriers that *link* accepted IDs. Machine contracts (JSON Schemas of records and the port) are generated from the kernel's typed models and published, so prose and contracts cannot drift silently.

## 18. Alternatives considered

```text
ALT-A  EMBEDDED DECLARATIONS (Candidate-01/Spec-028 style, modernized)
       J1 as visible TOML blocks inside Markdown governance carriers; indexes generated.
       + one artifact for humans; familiar
       - "exact package shown + decision" binding is weak (carriers are edited later);
         immutability needs extra machinery; signatures over mixed prose/structure;
         historical meaning harder to freeze; R2-era evidence shows embedded structure in
         prose invites drift
       VERDICT  rejected for J1; retained for carrier `links` metadata only

ALT-B  DATABASE-AUTHORITATIVE (SQLite/Postgres ledger + exported snapshots)
       + strong transactional concurrency; rich queries
       - authority leaves Git: PR review, diffs, signing and offline break-glass weaken;
         second store must be backed up and secured; exports risk becoming competing
         authority; higher operating burden (R0-R43, R0-R44)
       VERDICT  rejected; SQLite kept strictly derived

ALT-C  SERVICE CONTROL PLANE (AO/kernel as a running service with API + state)
       + real-time mediation; natural home for MEDIATED preflight
       - availability/security burden; break-glass depends on the service; provider
         coupling; violates proportionality before demonstrated need
       VERDICT  rejected as authority; a future OPTIONAL read-through cache/mediator over
                the same ledger remains possible without architecture change

ALT-D  FULL EVENT SOURCING OF ALL PROJECT STATE
       - previously rejected by WMR-H for good reasons; LEDGER-KERNEL event-sources ONLY the
         inherently event-shaped governance acts (acceptances), not all state
```

LEDGER-KERNEL is the deliberate hybrid: Research 503's family 2 (structured semantic records with rendered human carriers) and family 3 (append-only accepted records with derived snapshots), on Git, with family 4 (embedded relational index) strictly derived.

## 19. Evaluation against R0 dimensions (brief)

```text
semantic fidelity     high: every V03 invariant maps to a validator or structural rule (§20)
authority clarity     very high: one signed ledger; all else labelled derived/fact
failure visibility    high: closed list of fail-visible states; coded diagnostics
rebuildability        high: pure kernel; derived plane disposable
concurrency           high for identity/text; logical conflicts caught at merge queue
migration / rollback  high: LEG: identities, shadow parity, pointer-switch rollback
owner burden          low-moderate: read shown.md + touch a key; needs P1
developer burden      moderate: REALIZES manifests + PR discipline; needs P3
CI ergonomics         good: thin triggers, few required statuses
collaboration         good: provider-neutral port; connector agents fully supported
fresh-agent           good: anchor + derived ref + dossiers; needs P4
public/private        good: salted PrivateRefs; visible degradation
extensibility         bounded by governed grammar + plugin contracts
portability           Git + Python + SQLite only; no provider lock
operational cost      low: no service, no server DB
implementation risk   moderate: signing workflow and merge-queue discipline are new
```

## 20. V03 invariant mapping

```text
INV-01/02  draft-only proposals; derived ref; derived:true headers; validator rejects
           derived citations as sources
INV-03     package.toml effect record + semantic digest + shown.md digest
INV-04     REQUIRE granularity lint (one independently acceptable effect)
INV-05     closed accounting validator; creates_no_effects flag
INV-06     standing binding validator; DETECTIVE_ONLY explicit; enforcement view
INV-07     manifests cannot carry criteria; completion only in ledger/domain-contracts;
           same-owner criterion+realizer -> independent qualification required
INV-08/09  J3 from criteria + facts; single predicate registry consumed via CLI by WARRANT-F
INV-10     append-only ledger; corrections are acceptances
INV-11/12  lineage validators (closure, acyclicity, boundary sync)
INV-13     OPEN_RESET default; carry validator
INV-14     orientation derived only; no reported-state inputs to J3
INV-15     routing table completeness test (every condition -> owner class)
INV-16     domain plugins; grammar change governed
INV-17     LEG: registry; completeness views exclude unreconciled
INV-18     ordered 0..N initialization (D-1 amendment) in kernel types + golden tests
```

## 21. Reuse and retire dispositions for major current mechanisms

```text
tools/project_knowledge (W0-W4 package)
  identity/relation/authority-resolver/revision-descriptor concepts  REFINE_AND_PROMOTE
                                                                      (into framework/)
  embedded JSON declaration parser                                    KEEP_AS_COMPATIBILITY_ONLY
                                                                      -> RETIRE_AFTER_SUCCESSOR
  generated views (identity/authority/...)                            REIMPLEMENT_BEHIND_SAME_
                                                                      CONTRACT on derived plane
  capture/promotion path (W4)                                         REFINE_AND_PROMOTE as the
                                                                      KNOWLEDGE-class flow
Specification 028                                                     current authority ->
                                                                      migration source; LEG:
                                                                      inventory; superseded
                                                                      only by signed successor
current_routing.json                                                  REIMPLEMENT_BEHIND_SAME_
                                                                      CONTRACT (generated from
                                                                      control/), then RETIRE
CURRENT_STATE.md                                                      RETIRE_AFTER_SUCCESSOR
                                                                      (bounded derived
                                                                      orientation)
KNOWLEDGE_MAP.md / Research 217 subjects                              KEEP_AS_TEST_OR_REFERENCE
                                                                      (P4 comparator) ->
                                                                      RETIRE_AFTER_SUCCESSOR
checkpoints family                                                    historical; stop creating
                                                                      (milestone acceptances +
                                                                      receipts replace)
numbered Research/Decision families                                   KEEP as human carriers;
                                                                      ordinals become display
                                                                      aliases of IDs
model_collaboration threads                                           REFINE: STATE as control
                                                                      shard; REVIEW_INBOX
                                                                      generated; messages stay
repository-integrity + focused validators                             KEEP_AS_COMPATIBILITY until
                                                                      WARRANT-F successors pass
                                                                      kill-set + known-good
D-1/D-2/D-3 evaluators + fixtures; C-probe fixtures                   KEEP_AS_TEST_OR_REFERENCE
                                                                      (regression corpus)
34 GitHub workflows                                                   per WARRANT-F oracle
                                                                      classification
direct pushes to the coordination branch                              RETIRE_AFTER_SUCCESSOR
                                                                      (merge-queued authority
                                                                      branch)
Codexless Runtime Bridge generic code                                 external product (506);
                                                                      ADS keeps policy pack +
                                                                      adapter + lock
experiments/*                                                         historical reproduction
```

## 22. Material risks and falsifiers

```text
RISK                                              FALSIFIER (would change the architecture)
R-1 owner signing too burdensome / unavailable    P1: owner cannot complete signed acceptance
    on owner's devices                            in <=2 min median, or key UX fails on owner's
                                                  real devices -> fall back to platform-
                                                  separated identity (dedicated owner GitHub
                                                  account + required review) and record
                                                  weaker class
R-2 merge-queue linearity unavailable or too      P2: host cannot enforce linear exact-result
    slow on host plan                             advancement -> bridge-run promotion with
                                                  equivalent checks; if neither, ledger order
                                                  needs explicit sequence records (REDESIGN of
                                                  D4)
R-3 REALIZES manifests too costly/forgotten       P3: >X% realizations lack manifests or
                                                  manifest effort > budget -> central
                                                  realization registry per owner area
R-4 relation-first navigation insufficient        P4: fresh-agent/human tasks fail vs 217
                                                  comparator -> activate concern vocabulary
                                                  (bounded interface already exists)
R-5 OBSERVED_FROM_GIT receipts insufficient for   P5: verifier cannot bind action to request
    some consequential actions                    unambiguously -> require EXECUTOR_RECORDED
                                                  for that class
R-6 full rebuild too slow at real scale           P6: rebuild > budget -> persistent memoized
                                                  J3 snapshots keyed by input digests
R-7 canonical-digest scheme subtly unstable       property tests + cross-implementation
                                                  digest check (two languages) fail -> adopt an
                                                  external canonicalization standard (RFC 8785
                                                  JCS) verbatim
R-8 ULID IDs hurt human usability                 owner/dev feedback -> generated display
                                                  ordinals and slugs (no authority change)
R-9 logical ledger conflicts frequent under       P2 conflict rate high -> per-scope ledger
    concurrency                                   partitions with explicit cross-scope ordering
```

## 23. Empirical probes required before physical-target selection

Each is small, uses real repository material or synthetic fixtures, and has a preregistered abandonment rule:

```text
P1 OWNER SIGNED ACCEPTANCE            one real low-consequence governing act end-to-end:
                                      draft -> shown.md -> owner decision -> owner-key signed
                                      commit -> merge-queue verification; plus negative
                                      control: an agent-prepared unsigned/forged decision is
                                      rejected. Measure owner minutes and failure modes.
P2 CONCURRENT LEDGER ADMISSION        two branches with conflicting LIFECYCLE effects + one
                                      independent acceptance; verify deterministic fold,
                                      conflict detection, stale control-shard rejection on the
                                      actual host merge mechanism.
P3 REALIZER MANIFEST BURDEN           3 real realizations (code module, procedure, migration)
                                      declare REALIZES; J3 derives correctly; measure effort.
P4 NAVIGATION / FRESH-AGENT           preregistered tasks (217's 9 scenarios + new
                                      "what governs X" / impact / activation tasks) for
                                      relation-first+search vs 217 comparator, fresh agents
                                      with no project memory; measure success, context size,
                                      provenance correctness, false-authority errors.
P5 EXECUTOR PORT PORTABILITY          one bounded authorized action via bridge (EXECUTOR_
                                      RECORDED), GitHub connector (OBSERVED_FROM_GIT) and
                                      local CLI; identical normalized receipts' semantic
                                      fields; forced bridge unavailability -> correct fallback
                                      and mediation class.
P6 REBUILD EQUIVALENCE AND SCALE      full vs incremental derived plane on a realistic synthetic
                                      ledger (e.g. 2,000 effects, 500 lineage events);
                                      byte-equivalence + timing.
P7 PRIVATE DEGRADED REBUILD           public-only rebuild produces PRIVATE_UNAVAILABLE and
                                      correct review routing; leak scan catches seeded leaks.
```

P1, P2 and P4 are decision-critical. P3, P5, P6 and P7 can follow selection if time-boxed, but each has a falsifier that would amend the design.

## 24. Upstream consistency

```text
V03 logical invariants           preserved; no AMEND/SUPERSEDE/REOPEN required
R8-A repository/workspace target reused and refined (ledger/, control/ placement; derived ref)
WMR-H representation             reused: TOML human-authored machine semantics, JSON control
                                 shards, immutable receipts, SQLite/FTS derived, bounded
                                 orientation. CLARIFY candidate: the acceptance ledger is ONE
                                 standalone record class (not a per-record count against
                                 WMR-H's direct-record review bound)
WARRANT-F                        reused; predicates shared via CLI; exact-result promotion
                                 realized by merge queue; identity separation (MC-0028 OD1)
                                 realized by owner-held signing keys
AO-3..AO-7                       executor port realizes AO-10 mediation classes; bridge modes
                                 unchanged
Specification 028                current authority; migration source only
```

## 25. Final position

```text
PREFERRED_ARCHITECTURE           LEDGER-KERNEL
ALTERNATIVES_CONSIDERED          ALT-A embedded declarations; ALT-B database-authoritative;
                                 ALT-C service control plane; ALT-D full event sourcing
SEMANTIC_ORGANIZATION            relation-first hybrid selected for the core; concern
                                 vocabulary + embeddings frozen as a bounded open interface
                                 pending P4; Research 217 = comparator only
EXECUTION_BOUNDARY               provider-neutral executor port owned by the Project System;
                                 Runtime Bridge = external reusable infrastructure; ADS owns
                                 policy pack, adapter, version lock, qualification
AUTHENTICITY                     owner-held signing key; explicit attestation classes
DECISION_CRITICAL_PROBES         P1, P2, P4 (then P3, P5, P6, P7)
V03_CHANGE_REQUIRED              none (one WMR-H CLARIFY candidate)
PHYSICAL_TARGET_SELECTED         false
IMPLEMENTATION_AUTHORIZED        false
MIGRATION_AUTHORIZED             false
SPECIFICATION_028_AUTHORITY      unchanged
BLINDNESS_BOUNDARY               intact; no accidental exposure
NEXT                             comparative exposure (after this message is durable)
```
