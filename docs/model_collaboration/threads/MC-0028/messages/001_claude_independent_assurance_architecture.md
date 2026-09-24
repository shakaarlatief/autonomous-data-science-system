# MC-0028 Message 001: Claude Independent Assurance Architecture — WARRANT

```text
Thread                          MC-0028
Message                         001
Author / collaborator           Claude
Role                            INDEPENDENT_REVIEWER / RESEARCHER / CRITIC / COUNTER_DESIGNER
Interaction environment         Claude
Interaction session             claude-03 (thread participant slot)
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Frozen independent base         cac7a699eb012c5a02e1c5fab349ebc9e5726145
Mode                            INDEPENDENT_THEN_COMPARATIVE / independent candidate
Architecture name               WARRANT — Warranted, Bound-Evidence Assurance
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Independence boundary and material read

This message was produced in a new Claude chat with no carried conversation context. The conversation title changes from 03 to 04 to mark that; the thread participant slot remains `claude-03` because MC-0028 `STATE.json` names it and is outside my write boundary.

**Read at branch head (contract/routing only):** `docs/current_routing.json`, `docs/model_collaboration/REVIEW_INBOX.md`, and MC-0028 `STATE.json`, `BRIEF.md`, `THREAD.md`. These exposed only the facts that ChatGPT's candidate exists, is called FACET, and is frozen as Research 274. No design content was exposed. I did not open Research 274, any file added after the frozen base, or any later ChatGPT assurance material, and I did not infer anything from the name.

**Read at the frozen base `cac7a699…` (substantive evidence):** Research 273 and 272 in full; Research 262, 259 and 258 in full; Research 252 in full; Research 257 §5.1 and §13 (engineering residency and root tooling); `CURRENT_STATE.md` by targeted search; the root `pyproject.toml`; the `.github/workflows/` inventory with `repository-integrity.yml` and `v1-reasoning-context-value-live.yml` in full; the `scripts/` inventory with `check_repository_integrity.py`, `repository_integrity.py` and `check_model_collaboration_state.py` in full; `tools/project_knowledge/declaration.py`; the `tests/integration/` inventory; and my own MC-0027 Message 001.

**External sources (independent searches):** NIST SSDF project and publication pages (SP 800-218 v1.1 final; SP 800-218r1 / v1.2 initial public draft of 2025-12-17; SP 800-218A generative-AI community profile, final); the SLSA levels specification (v1.2 current, with Build track L0–L3 and a Source track formalized in 1.2); industry summaries of the same. Standards are used as cross-checks, not imported as architecture.

**Known exposure.** I authored MC-0027 Message 001, whose central lesson — a check can carry the right name, return PASS and be unable to fail — is the most load-bearing single input to this design. That exposure is intentional per Research 273 §1 and is within the frozen base.

## 1. Summary

WARRANT treats assurance as **adjudicating admissible evidence about exact subjects at governed transitions**, not as running a set of jobs.

Research 273's claim-first primitive is necessary but not sufficient. The P-R8B-01 history shows the failure is rarely a missing claim. It is a verifier that could not have failed, evidence bound to the wrong bytes, a PASS reached by retrying, or a result that silently expired. WARRANT therefore makes six things first-class:

```text
CLAIM          what must hold, about what kind of subject, owned by whom
VERIFIER       a versioned mechanism that observes a subject
WARRANT        why a verifier's PASS supports a claim — including
               SENSITIVITY WITNESSES proving the verifier can fail
EVIDENCE       an immutable record binding one observation to exact
               subject digests, verifier/warrant versions, producer and tier
GATE POLICY    which claims a transition requires, with which consequence,
               at which trust tier and freshness
DECISION       the adjudicated result of a transition, citing its evidence
```

Eight architectural commitments distinguish the candidate:

```text
1. NO WARRANT, NO BLOCK
   A claim can back a blocking gate only through a verifier whose
   sensitivity witnesses currently FAIL it as intended.

2. FEDERATED DECLARATION, SINGLE ADJUDICATION
   Product, JW1 and engineering own their claims and verifiers.
   One small engineering-owned kernel evaluates every gate.

3. ADAPTER AT THE CONSUMER
   No workspace imports assurance machinery. The kernel adapts each
   owner's native result format. Product stays assurance-agnostic;
   JW1 never depends on engineering.

4. BASE-REVISION POLICY RATCHET
   A change is judged by the policy of the branch it targets.
   It may add or strengthen claims. It may not weaken them without a
   recorded owner decision bound to the policy diff.

5. TRUST TIERS, NOT LOCATIONS
   Evidence is admissible according to who produced it and how,
   not merely where it ran. Hosted ephemeral execution is required for
   blocking promotion evidence because every authoring actor today
   shares one Git-host identity.

6. EXACT-RESULT EVALUATION
   The gate evaluates the exact tree that will become the protected head.
   Under fast-forward or merge-queue promotion, pre-merge and integrated
   qualification collapse into one subject.

7. ONE EVIDENCE MODEL, SPLIT BY VISIBILITY AND DURABILITY
   Local, CI, release, deploy and live evidence share one record model.
   Storage separates ephemeral from decision-grade and public from private.

8. STOCHASTIC CLAIMS ARE CAMPAIGNS
   Model-dependent quality is judged by preregistered, budgeted,
   non-retryable campaigns, never by per-commit pass/fail sampling.
```

Recommended outcome for comparison: keep the upstream architecture; exercise the R8-A §5.1 deferred decision by giving `project/engineering` an independently resolved Python environment; treat every current workflow, script and test as oracle-or-archive evidence under an explicit extraction ledger; do not lock into a CI provider.

## 2. Evidence that shaped the design

These are facts at the frozen base, each with the design consequence it forces.

```text
E1  UNFALSIFIABLE CHECKS ARE REAL, RECENT AND SELF-AUTHORED
    MC-0027: 7 of 18 preregistered gates could not fail; one reported a
    hardcoded measurement. Research 272 §7 keeps this as design evidence.
    -> sensitivity witnesses are mandatory for blocking claims (§5.3)

E2  SHARED AUTHORING IDENTITY
    check_model_collaboration_state.py states its guard is "not an
    authenticated lock" because provider integrations share the user's
    GitHub authority. CURRENT_STATE records a GitHub App with live
    Administration=write used by the same Runtime Bridge that authors content.
    -> hosted ephemeral evidence is the only producer independent of the
       author's environment; identity separation is an open owner decision
       (§14.1); SLSA Source L4-style two-party review cannot be claimed

E3  NO ENFORCEMENT AT PROMOTION
    CURRENT_STATE: no rulesets, no required checks; a fixed branch-safety
    baseline blocks force-push and deletion only; automation fast-forward
    pushes to the promoted integration branch; active_pr = null.
    -> gates must work for direct-push, fast-forward promotion as well as PRs

E4  PATH-FILTERED BLOCKING TRIGGERS UNDER-TEST
    repository-integrity.yml runs `uv run --locked` but uv.lock and
    pyproject.toml are not in its trigger paths; a dependency change that
    breaks the gate does not run the gate.
    -> no provider-level path filters on blocking gates (§15.2)

E5  HASH-BASIS AND LINE-ENDING DEFECTS RECUR
    P-R8B-01 freeze hashes were CRLF working-tree bytes; Candidate-01 and
    Runtime Release manifests hit the same CRLF/LF split; the accepted
    remedy is GIT_BLOB_BYTES_AT_COMMIT.
    -> one kernel-wide hash basis; Windows is a first-class verification OS

E6  CONFIRMATORY EVIDENCE HAS PROVIDER-RETENTION LIFETIME
    v1-reasoning-context-value-live uploads its frozen result bundle with
    retention-days: 30; MC-0027 found durable evidence was a manual copy of
    gitignored results.
    -> provider retention is never decision-grade storage (§18)

E7  EVALUATION RUNS WITH UNLOCKED DEPENDENCIES
    the same workflow executes the live experiment with
    `--with openai-agents==0.19.4` outside uv.lock.
    -> every evidence-producing environment must be lock-bound (§13)

E8  INCONSISTENT ACTION PINNING
    setup-uv is SHA-pinned; actions/checkout@v7 and upload-artifact@v4 are
    tag-referenced in the same files.
    -> all third-party execution is digest-pinned (§14)

E9  REAL DELIVERY ALREADY EXISTS — FOR PROJECT TOOLING, PRIVATELY
    Runtime Bridge releases in the private local-runtime repository use
    immutable releases, manifests, activation and post-activation
    verification. Recorded defects: a publisher whose rollback path re-ran
    target-only regressions; a directly launched process reporting healthy
    HTTP while missing its dependency binding.
    -> CD design must cover Project tooling, not only a future Product;
       health != semantic readiness; rollback must itself be qualified

E10 SELECTION ERRORS HAPPEN
    CURRENT_STATE records independent review catching a real
    under-selection in incremental view regeneration (G014).
    -> affected-scope selection must be conservative and audited (§19)

E11 ONE AGGREGATE PASS HIDES STRUCTURE
    check_repository_integrity.py folds family contracts, JW1 validation,
    three focused validators and routing into PUBLIC_REPOSITORY_INTEGRITY.
    -> decisions are conjunctions of individually-consequenced claims;
       an aggregate is a derived view only (§11.4)

E12 PRODUCT CARRIES PROJECT-VALIDATION DEPENDENCIES TODAY
    root pyproject makes jsonschema a Product runtime dependency; R8-A
    splits resolution but nothing yet proves the split stays clean.
    -> "absence execution" claims (§11.2)

E13 ENGINEERING RESIDENCY WAS DELIBERATELY DEFERRED
    Research 257 §5.1: project/engineering "is not a Python package by
    default"; substantial engineering code "requires a later architecture
    decision". Research 258 removed the root uv workspace.
    -> WARRANT triggers that decision (§21, U1)

E14 A STRICT MARKER DETECTOR ALREADY MISCLASSIFIED PROSE
    Research 262 §13: discussing a declaration marker token in a
    collaboration message tripped the validator.
    -> verifiers need declared scope and false-positive witnesses too
```

## 3. Design principles

```text
P1  Subject before mechanism. Every result names the exact bytes/artifact/
    environment it is about. Unbound results are observations, not evidence.

P2  A verifier is presumed blind until shown to see. Blocking use requires
    demonstrated sensitivity (it fails on seeded violations) and, where
    false positives are plausible, demonstrated specificity.

P3  Consequence belongs to the transition. A claim carries a consequence
    FLOOR; each gate binding chooses the actual consequence at or above it.

P4  Assurance must not be weakened by the change it assures.

P5  No actor grades its own work at a blocking gate. Blocking evidence comes
    from a producer the author does not control at run time.

P6  Retries diagnose; they never launder. Every attempt is recorded; a
    deterministic claim that flips is a defect, not a pass.

P7  Freshness is part of truth. Evidence fails stale, never silently carries.

P8  Owners declare; the kernel adjudicates; nobody imports the kernel.

P9  One logical command graph for local and hosted execution; differences are
    declared (trust tier, secrets, platform), never incidental.

P10 Stochastic claims are experiments with preregistered stopping rules.

P11 Provider mechanisms are adapters. Semantics live in the repository.

P12 Durable decisions outlive providers. Decision-grade evidence is
    content-addressed and stored where a provider change cannot delete it.

P13 Proportionality. Machinery is admitted only when a present subject needs
    it: artifact attestation at first external consumption, deployment
    control at first live environment.

P14 The kernel is a small trusted computing base with its own warranted claims.
```

## 4. Positions on the required challenges

**Is claim-first sufficient?** No. Claims are the right unit of *meaning*, but the observed failures sit between claim and evidence. The missing first-class abstraction is the **warrant** — the argument, carried as data, that a verifier's PASS supports a claim, together with witnesses that prove the verifier can fail. This is the minimal part of assurance-case practice (claim / argument / evidence, as in GSN and ISO/IEC/IEEE 15026) worth adopting. Full argument graphs are rejected as disproportionate. A second missing abstraction is **gate policy separated from the claim**, because the same claim is advisory while authoring and blocking at promotion.

**Are ten lifecycle gates the right granularity?** They are the right *coverage* and the wrong *shape*. LG0 governs no transition; it is a feedback profile. LG1 and LG2 collapse into one gate under exact-result evaluation. LG8 (recovery) and LG9 (continuous) are not transitions but evidence-maintenance processes whose outputs other gates consume through freshness rules. WARRANT uses **one feedback profile, seven transition gates and two maintenance processes**, mapped one-to-one onto LG0–LG9 in §8.1 so nothing in Research 273 is lost.

**One orchestrator or federated owners?** Both, split cleanly. Ownership of claims, verifiers and witnesses is federated to semantic owners. Adjudication is single: one gate evaluator, one outcome lattice, one evidence model. Federated adjudication would let each owner define PASS differently, which is exactly the drift the aggregate currently hides.

**Should local and CI share one logical command graph?** Yes. One planner produces the plan for any profile. Hosted execution is the same plan with a higher trust tier and some declared hosted-only verifiers. Undeclared local/hosted divergence is itself a defect class.

**Should release and deploy evidence share one evidence plane?** One *model*, not one *store*. Release, deploy and live records share the schema and outcome lattice and chain by digest. Storage splits by visibility (runtime environment evidence is often private) and durability.

**Does stochastic/AI evaluation belong in normal CI?** Its deterministic parts do: evaluator harness correctness, scoring code, replayed model interactions. Live sampling does not run per commit. It runs as preregistered campaigns at release-candidate, on schedule for drift, and on authorized dispatch.

**Should repository governance be a blocking aggregate?** Governance should block; an aggregate should not be the blocking object. Each governance claim carries its own consequence; some block (identity uniqueness, reference integrity, routing consistency, public/private safety), others are advisory. The gate decision is the conjunction. A summary line is a derived report.

**Is build provenance warranted before distribution/deployment exists?** Split the answer. Source-to-evidence binding and **evidence-bundle provenance** are warranted now: migration cutover and research integrity already depend on them, and E6/E7 show present gaps. Artifact provenance with platform signing is warranted at the first artifact consumed outside the process that built it. Two already exist in spirit: Runtime Bridge releases, and any future Product wheel or web bundle.

**Is hosted CI needed for trusted evidence?** For blocking promotion, release and cutover evidence, yes — not for hosted CI's own sake, but because under E2 an ephemeral runner started from a committed tree is the only producer outside every author's control at run time. Local evidence remains fully valid for feedback and for owner-reviewed, declared hosted-infeasible claims. If the owner later separates authoring identities and hardens a local runner, a local trust tier could qualify; that is a falsifiable, open decision (§23).

**Should historical workflows be retired, archived or retained as live oracles?** By classification, not by default. Only workflows enforcing a currently accepted invariant with no qualified successor are retained as **live oracles**, and only until their successor's kill set covers theirs (§12.4). Experiment and live-evaluation runners become frozen reproduction evidence. Repository mutators leave assurance entirely. A preliminary classification of all 34 workflows is in §12.6.

## 5. The assurance primitive model

### 5.1 Claim

```text
claim_id            stable, owner-scoped identifier (never a file path)
owner               PRODUCT:<context> | JW1:<capability> | ENGINEERING |
                    GOVERNANCE | RESEARCH:<program>
family              AC1..AC15
subject_type        SOURCE_TREE | WORKSPACE | ARTIFACT | RELEASE |
                    ENVIRONMENT | AUTHORITY_STATE | EVIDENCE_BUNDLE |
                    HISTORY_RANGE | MODEL_CONFIGURATION
property            human-readable invariant, plus a machine predicate where one exists
consequence_floor   minimum consequence at any gate past the feedback profile
criticality_reason  why the floor is what it is
status              PROPOSED | ACTIVE | AMENDED | SUPERSEDED | RETIRED
lineage             extracted-from (current mechanism + invariant) or new
```

A claim states no mechanism, no test file and no CI job. Claims are authored by their semantic owner as inert data beside the owner's code, read only by the kernel, and excluded from any Product runtime artifact.

### 5.2 Verifier

```text
verifier_id         stable identifier
owner               same ownership vocabulary as claims
entrypoint          native command in the owner's own environment
native_result       the owner's result format (pytest/JUnit, a JW1 JSON
                    report, a browser-test report, a campaign result)
evidence_class      EC1..EC14 (Research 273 §7)
determinism         DET | DET_PLATFORM | STOCHASTIC | LIVE | HUMAN
platforms           where the claim is sensitive (e.g. linux+windows)
declared_inputs     path/glob set + lock + toolchain it reads
trust_minimum       lowest tier whose evidence it may produce for blocking use
secrets / network   NONE | named capability (hosted protected environment only)
budget              time / cost ceiling per run
```

A verifier never writes the subject. Verifiers that mutate are tooling, not assurance, and are governed under AC10 as mutations.

### 5.3 Warrant and sensitivity witnesses

```text
warrant_id
claim_id            the claim it supports
verifier_ids        one or more (a claim may need several evidence classes)
argument            why these observations support this property, and the
                    known gaps (what the verifier does NOT exercise)
sensitivity         witnesses: seeded violations the verifier MUST FAIL on
specificity         witnesses: near-miss valid inputs it MUST PASS on
                    (required where false positives are plausible, cf. E14)
coverage_note       which part of the claim's scope each witness exercises
witness_digest      content digest of the witness corpus
last_witnessed      evidence record of the most recent witness run
```

A sensitivity witness is a concrete input or subject mutation, not a promise: a duplicated numbered identity, a stale-write attempt, a Product module importing `project/`, a seeded fake credential in a public carrier, a CRLF-only blob change, an evaluation run with a mislabelled model id. It is exactly the mutation technique MC-0027 used to classify gates, promoted from an audit method into a standing requirement.

Warrant rules:

```text
W1  A claim may bind at consequence BLOCK or QUARANTINE only through an
    ACTIVE warrant whose witnesses passed (verifier FAILED each seeded
    violation, PASSED each specificity case) against the current verifier
    version.

W2  Changing a verifier, its declared inputs or its witness corpus
    re-triggers witnessing before any blocking use of that verifier.

W3  Removing or narrowing witnesses of a blocking warrant is a policy
    weakening (§5.6) and requires an owner decision.

W4  A warrant states its known gaps. Gaps are review material, not failures;
    they stop a PASS being read as broader than it is.

W5  Advisory and observational bindings do not require witnesses, but their
    reports must display UNWARRANTED so they cannot masquerade as guarantees.
```

### 5.4 Evidence record

```text
record_id           content digest of the canonical record
claim_id, warrant_id, verifier_id + verifier_digest
subject             typed subject with digests:
                      source commit + tree digest
                      declared-input digest (GIT_BLOB_BYTES basis, always)
                      lock digests per resolved environment
                      artifact digest / environment identity / model id
                      fixture or corpus digest / manifest version
producer            runner identity, trust tier, platform, toolchain digest,
                    run id, attempt number
outcome             one value of the attempt lattice (§5.5)
observations        bounded structured detail + pointer to full bundle
bundle_digest       digest of the complete raw output bundle
freshness           valid-until rule: input-bound | time-bound | model-bound |
                    environment-bound
visibility          PUBLIC | PRIVATE (private records publish digest only)
```

The record is semantically an in-toto-style statement (typed subjects with digests plus a predicate). Later attestation becomes a signature envelope around an existing record, not a redesign. The exact predicate format is an open decision.

### 5.5 Outcome lattice

Per attempt, exactly one of:

```text
PASS                verifier ran validly; property held
FAIL                verifier ran validly; property violated         (CLAIM FAILURE)
HARNESS_INVALID     verifier itself defective or witnesses failed    (HARNESS FAILURE)
INFRA_ERROR         runner/network/provider failure before a valid observation
INCOMPLETE          valid run that could not observe the full scope
MUTATION_UNCERTAIN  a mutating step may or may not have completed
```

Per claim at a gate, derived by the evaluator:

```text
SATISFIED           admissible, fresh, warranted PASS for this exact subject
VIOLATED            admissible FAIL
UNVERIFIED          no admissible evidence (missing, INFRA_ERROR, INCOMPLETE,
                    insufficient trust tier)
STALE               evidence exists but its binding no longer matches
UNWARRANTED         evidence exists but the warrant is not currently witnessed
NONDETERMINISTIC    a DET verifier produced both PASS and FAIL for one input digest
INCONCLUSIVE        stochastic campaign interval straddles the acceptance bound
WAIVED              explicit, expiring owner waiver bound to claim + subject scope
```

Only SATISFIED and WAIVED count toward admission of a BLOCK claim. Everything else fails closed.

### 5.6 Gate policy and the base-revision ratchet

A gate policy binds claims to a gate with a consequence (BLOCK, QUARANTINE, REVIEW_REQUIRED, ADVISORY, OBSERVE — Research 273 §8), a minimum trust tier and a freshness requirement. The actual consequence must be at or above the claim's floor.

```text
EFFECTIVE POLICY for evaluating a candidate against target branch B:

    base policy        policy, claims and warrants at the head of B
  + candidate adds     new claims, new bindings, raised consequences,
                       added witnesses — applied immediately
  - candidate weakens  removed claims, lowered consequences, relaxed
                       thresholds, narrowed scope, removed witnesses,
                       lowered trust minimum — NOT applied unless an owner
                       decision record binds the exact policy-diff digest

WEAKENING DETECTION is mechanical: the evaluator diffs base and candidate
policy objects and classifies every change as ADD / STRENGTHEN / NEUTRAL /
WEAKEN. Unclassifiable changes are treated as WEAKEN.
```

This makes AC14 ("review requirements cannot be silently bypassed") enforceable against the change itself. It deliberately allows a candidate's *own new verifier code* to run, since new code needs new tests. That code still cannot bypass witnessing: a verifier gutted to always pass fails its base-revision witnesses and becomes UNWARRANTED.

Residual risk: a verifier that special-cases its known witness inputs. Mitigations are listed in §22 (F2 and the witness-rotation open decision).

### 5.7 Decision

```text
decision_id, gate, subject, effective-policy digest
per-claim derived status with cited evidence record ids (every attempt)
result              ADMIT | REFUSE | REVIEW_REQUIRED
owner_decision_ref  required for REVIEW_REQUIRED resolution, waivers,
                    weakening diffs, release authorization, cutover
```

Human owner decisions remain governance events (AC14), stored under Project governance knowledge and referenced by digest. A decision record cites them; it never becomes one. Model-collaborator reviews, including this message, are evidence (EC13-like), never approvals — they are not authenticated second parties under E2.

### 5.8 Trust tiers

```text
T0 LOCAL_UNATTESTED
   any workstation or agent sandbox, possibly dirty tree
   admissible: feedback profile, ADVISORY, OBSERVE

T1 LOCAL_RECORDED
   clean tree at an exact commit; kernel records toolchain, platform,
   lock and input digests
   admissible: REVIEW_REQUIRED claims; declared hosted-infeasible claims
   (e.g. a local-only integration) with owner disposition

T2 HOSTED_EPHEMERAL
   fresh ephemeral runner, checkout of the exact subject, platform run
   identity, base-revision policy, no author-controlled state
   admissible: BLOCK / QUARANTINE at change and promotion gates

T3 HOSTED_ATTESTED
   T2 plus platform-signed provenance of the artifact or evidence bundle
   required: release and activation gates once any external consumer or
   live environment exists
```

Tiers describe the evidence producer, not the verifier's correctness. Correctness is the warrant's job.

## 6. Logical components

```text
ENGINEERING-OWNED ASSURANCE KERNEL  (small trusted computing base)

  CATALOG        loads claims, verifiers, warrants and gate policies from
                 all owners; validates references; builds the effective
                 policy; runs weakening detection

  PLANNER        subject + gate + profile -> execution plan
                 affected-scope selection from declared inputs
                 evidence reuse by declared-input digest
                 resource classes (default Linux, Windows, browser,
                 protected-secret evaluation)

  RUNNER         executes owner entrypoints in their OWN environments;
                 records attempts; classifies INFRA_ERROR vs verifier
                 outcome; enforces budgets; never interprets semantics

  ADAPTERS       native result -> evidence record, one per native format
                 (pytest/JUnit, JW1 validator report, web-test report,
                 campaign result, deploy probe). Adapters live in the
                 kernel, so dependency points consumer -> producer.

  WITNESS RUNNER applies sensitivity/specificity witnesses to verifiers

  LEDGER         content-addressed evidence records; ephemeral and durable
                 stores; public/private split (§18)

  EVALUATOR      effective policy + evidence -> per-claim status -> decision
                 the only component that may say ADMIT

  PUBLISHER      provider adapter: one status per gate, summary report,
                 bundle upload, receipt persistence

  SCHEDULER      maintenance processes: freshness revalidation, drills,
                 drift sentinels, dependency/security rescans, hermeticity
                 audits (§8.3)

DOMAIN SERVICES BUILT ON THE KERNEL  (engineering or research owned)

  CAMPAIGN MANAGER      preregistration, sampling, budgets, statistics (§10)
  SHADOW COMPARATOR     old/new verdict differential and kill sets (§12)
  BUILD/RELEASE SERVICE build-once, digest, SBOM, provenance (§13)
  DEPLOYMENT CONTROLLER preflight, activate-once, postflight, rollback (§16)
```

The kernel's own correctness is claimed and warranted like anything else (§22.3). Kernel changes are adjudicated by the kernel version at the target base.

## 7. Ownership

### 7.1 Ownership table

```text
PRODUCT RUNTIME (PW1, contexts PC1..PC7)
  claims      AC1; AC2 task/quality semantics; Product parts of AC10, AC11
  verifiers   unit, contract, integration tests; eval harness code and
              Product-owned eval fixtures
  witnesses   own
  kernel      never imports or runs it

PRODUCT INTERACTION (PW2)
  claims      AC1 for clients
  verifiers   component and client-local end-to-end tests
  witnesses   own
  kernel      never imports or runs it

JW1 (project/system)
  claims      AC3; AC5 semantics; semantic parts of AC6, AC10, AC12
  verifiers   semantic validators (JW1-owned CLI + result contract), JW1 tests
  witnesses   own
  kernel      never imports it; is invoked by it

PROJECT ENGINEERING (project/engineering)
  claims      AC4, AC7, AC8, AC9, AC15; orchestration parts of AC6, AC11, AC12
  verifiers   repository/architecture checks, absence execution,
              cross-workspace qualification, build/release/deploy probes
  owns        the kernel, all gate bindings, adapters, host adapters

PROJECT RESEARCH (project/research)
  claims      AC13; AC2 campaign designs for research programs
  verifiers   harness-validity checks, preregistration fidelity
  kernel      uses it for campaigns and result acceptance

GOVERNANCE KNOWLEDGE
  claims      AC14; consequence floors for governance-critical claims
  evidence    owner-decision records referenced by decisions

TRUE ROOT / HOST
  provider trigger and adapter files only; no semantics
```

Rules:

```text
O1  Semantic owner writes the claim. Engineering writes gate bindings.
    A Product claim's meaning is never authored in engineering.

O2  Verifiers run in the owner's environment with the owner's lock.
    Product tests run in the Product environment; JW1 validators in the
    JW1 environment. The kernel invokes them as processes.

O3  Engineering MAY invoke JW1 (process or path dependency).
    JW1 MUST NOT import engineering, the kernel, or its record schema.

O4  Product MUST NOT import Project anything. Product claim declarations
    are inert data excluded from Product artifacts.

O5  Branch roles are JW1 semantics (AO-6 / Research 258 CL-6).
    Engineering binds gate requirements to those roles and implements
    host enforcement.

O6  Root host files are triggers and adapters only; they contain no
    claim semantics and no gate logic.

O7  Evaluation fixtures are owned by whoever owns the task semantics
    (Product for Product quality claims, research for research programs);
    the campaign machinery is Project-owned.
```

### 7.2 The engineering workspace decision (exercises R8-A's deferred decision)

WARRANT's kernel is non-trivial executable engineering code, which is precisely the trigger Research 257 §5.1 reserved. The options:

```text
(a) engineering code inside project/system's Python project
    REJECT: couples JW1's resolution to ADS-specific engineering (the AM-1
    argument, applied inside the Project plane) and pollutes the PSMF
    framework with non-framework dependencies

(b) root pyproject / root environment
    REJECT: recreates the root coupling AM-1 removed

(c) project/engineering as its own independently resolved Python project
    (own pyproject + lock), depending on JW1 only through its CLI or as a
    path dependency, never depended on by JW1 or Product
    RECOMMEND
```

This is an AMEND candidate under AO-4, not a reopen: it completes a decision R8-A explicitly left for this stage.

## 8. Lifecycle model

### 8.1 Gates and mapping to Research 273

```text
FEEDBACK PROFILE (no transition)
  F0  author        LG0

TRANSITION GATES (each governs a subject changing state)
  G1  CHANGE        candidate tree proposed        LG1 (early signal)
  G2  PROMOTE       exact tree becomes protected   LG1 + LG2
                    branch head
  G3  ARTIFACT      built bytes become qualified   LG3
  G4  RELEASE       qualified artifact becomes     LG4
                    releasable (authorization)
  G5  ACTIVATE      release enters a live          LG5
                    environment
  G6  LIVE          activation becomes accepted    LG6
                    (or rolled back)
  G7  CUTOVER       authority moves from old       LG7
                    representation/mechanism to new

MAINTENANCE PROCESSES (produce evidence consumed via freshness)
  M1  DRILLS        exercised recovery evidence    LG8
  M2  REVALIDATION  drift, expiry, dependency and  LG9
                    security changes, hermeticity
```

Why G1 and G2 are separate but LG1/LG2 collapse: G1 gives early, affected-scope, possibly cached signal on any candidate branch. G2 is the only blocking source gate, and it evaluates **the exact tree that becomes the protected head**. With fast-forward-only promotion that is the candidate itself. With merges it is the merge result, which a merge queue (or an equivalent pre-computed merge) must evaluate. No "pre-merge" result is admissible for a tree other than the resulting head. Residual integrated-only properties — history-range claims such as the WMR-H monotonic-revision rule over merges — are HISTORY_RANGE subjects evaluated at G2 over the range the promotion adds.

### 8.2 Flows

```text
F0 AUTHOR (local, T0)
   assure check [--changed]            fast: static, schema, focused tests
   assure check --gate promote         same plan as hosted G2, locally
   median target: seconds; ceiling: about one minute for --changed

G1 CHANGE (hosted T2; any non-protected branch push or PR update)
   affected-scope plan + evidence reuse
   result is advisory for the branch; it cannot admit promotion

G2 PROMOTE (hosted T2; required before any protected-branch head advance)
   all BLOCK claims bound to G2 for the target branch role
   evaluated on the exact resulting tree; reuse allowed only by exact
   declared-input digest at >= T2
   includes: repository/architecture, JW1 semantic, Product deterministic,
   cross-workspace, public/private, history-range, deterministic eval harness
   emits ONE required status per gate (e.g. assure/promote)

G3 ARTIFACT (hosted T2 now, T3 once externally consumed)
   build once from the admitted tree; record artifact digest, lock digests,
   builder identity, SBOM; artifact-specific tests run on the built bytes

G4 RELEASE (T3 when applicable)
   requires: G3 SATISFIED for this digest, fresh campaign evidence for
   release-bound AC2 claims, fresh M1 drill evidence for claims depending
   on recoverability, declared rollback mode, owner release authorization
   promotion never rebuilds: the released digest == the qualified digest

G5 ACTIVATE (deployment controller)
   preflight: release decision + provenance verified, environment identity,
   config schema, target version, mutation authority, rollback availability
   activate exactly once; uncertain activation -> MUTATION_UNCERTAIN,
   reconcile by read, never blind-retry

G6 LIVE (bounded observation window)
   postflight: running identity == released digest; semantic readiness
   probes (capability-level, not HTTP liveness — E9); error/latency budgets
   where SLOs exist; on failure: rollback by the qualified rollback mode,
   escalate on rollback failure

G7 CUTOVER (JW1 transitions + engineering orchestration)
   shadow equivalence and intentional-divergence disposition, reference
   integrity, derivative-free reconstruction, rollback drill, fresh M1,
   explicit owner authorization bound to the exact transition manifest
```

### 8.3 Maintenance processes

```text
M1 DRILLS      each drill is a verifier with a freshness window consumed by
               G4/G7 (and any claim whose property depends on recoverability)
M2 REVALIDATE  scheduled: re-run time-bound claims; dependency vulnerability
               and licence rescans; provider-model drift sentinels; credential
               and permission expiry checks; hermeticity audits for reuse;
               full unselected runs to audit the planner
```

## 9. Claim-family coverage

Default floors below are proposals, not fixed policy.

```text
AC1  Product functional       PW1/PW2 owners; EC3 EC4 EC5 EC6; G1 G2 G3;
                              floor BLOCK for published contracts
AC2  Product AI/DS quality    Product-owned tasks, Project campaigns; EC9 plus
                              EC3 for harness; G4 (campaign), M2 (drift);
                              floor REVIEW_REQUIRED; harness claims BLOCK
AC3  JW1 semantics            JW1; EC2 EC3 EC6; G1 G2; floor BLOCK
AC4  architecture integrity   engineering; EC1 static import graph + EC5
                              absence execution; G2; floor BLOCK
AC5  representation/info      JW1 validators, engineering invocation; EC2
                              EC6 EC7; G2 G7; floor BLOCK for identity/
                              authority/reference, ADVISORY for historical
                              metadata completeness
AC6  compatibility/migration  JW1 transitions + engineering shadow; EC7 EC8;
                              G7 (and G2 while shadowing); floor BLOCK at G7
AC7  build/dependency         engineering; EC1 EC12; G2 G3 M2; floor BLOCK
AC8  security/privacy         engineering + governance floors; EC1 EC10 EC12;
                              G2 G3 M2; floor BLOCK for public/private leakage
AC9  artifact/release prov.   engineering; EC12; G3 G4 G5; floor BLOCK
AC10 mutation/live safety     owning mutator (JW1 for control state, delivery
                              for deploys, bridge for host mutations);
                              EC4 EC6 EC11; G2 G5; floor BLOCK
AC11 runtime reliability      Product PC7 + delivery; EC11; G6 M2;
                              floor REVIEW_REQUIRED until SLOs exist
AC12 recovery/continuity      JW1 continuity mechanism + engineering
                              drills; EC8; M1 feeding G4 G7; floor BLOCK
                              where a gate declares recoverability
AC13 research integrity       research; EC6 EC12 EC14; result-acceptance
                              decisions; floor BLOCK for protocol fidelity
AC14 governance integrity     governance + evaluator ratchet; EC13 EC14;
                              every gate; floor BLOCK
AC15 delivery/deployment      delivery; EC11 EC12; G4 G5 G6; floor BLOCK
```

## 10. Deterministic versus stochastic and AI assurance

```text
DET           same input digest -> same outcome, on any declared platform
DET_PLATFORM  deterministic per platform; verified on each declared platform
STOCHASTIC    sampling-dependent (model outputs, randomized algorithms)
LIVE          depends on external mutable state (provider, network, service)
HUMAN         an owner or reviewer judgment
```

**Deterministic rules.** A DET verifier producing PASS and FAIL for one input digest yields NONDETERMINISTIC, which is a harness defect. The verifier is quarantined; the claim becomes UNVERIFIED; a blocking claim therefore refuses admission until the verifier is repaired, an alternative warranted verifier exists, or a time-boxed owner waiver is recorded. Quarantine never silently deletes a claim from a gate.

**AI and model-dependent claims** use three layers.

```text
L-A  HARNESS CORRECTNESS          DET, in G1/G2, BLOCK floor
     scoring code, metric computation, sampling code, dataset loaders,
     judge-prompt assembly; witnesses include seeded mis-scored cases

L-B  REPLAY REGRESSION            DET, in G1/G2
     recorded model interactions (fixed request/response pairs bound to
     model id and prompt digest) exercise orchestration and parsing code
     without live calls; replay files are evidence fixtures, not truth
     about model quality

L-C  LIVE CAMPAIGNS               STOCHASTIC / LIVE, never per commit
     run at G4 for release-bound claims, at M2 as drift sentinels, and on
     explicitly authorized dispatch for research
```

A campaign is preregistered before execution:

```text
subject          artifact or source digest, model identity as returned by
                 the provider, prompt/config digest, corpus digest,
                 harness digest, judge identity if any
design           sample size n, seeds where controllable, metric, acceptance
                 rule (e.g. lower 95% bound >= tau, or non-inferiority margin
                 delta vs an accepted baseline), stopping rule
negative control a condition the harness must score as failing
budget           tokens / money / wall-clock ceilings
outcomes         PASS | FAIL | INCONCLUSIVE | HARNESS_INVALID | INCOMPLETE
```

Campaign rules:

```text
C1  No optional stopping. A rerun is a new campaign; all campaigns on the same
    claim and subject are reported together. Pooling only if a sequential
    design was preregistered.

C2  Returned model identity must equal declared identity; a mismatch is
    HARNESS_INVALID, not a result.

C3  LLM-as-judge is a verifier and needs its own warrant: agreement with a
    human-labelled calibration set and a negative control, recorded per
    judge identity.

C4  INCONCLUSIVE routes to REVIEW_REQUIRED; it is never rounded to PASS.

C5  Provider-side model changes without a commit are detected by M2 drift
    sentinels (small fixed n, OBSERVE or REVIEW) and invalidate model-bound
    freshness of release campaigns.

C6  Credentials exist only in a protected evaluation environment requiring
    explicit authorization, retaining the good current pattern of typed
    confirmation for cost-bearing live runs.
```

Research 273 cross-checks: this operationalizes NIST AI RMF TEVV as specific evidence rules rather than adopting the framework. SP 800-218A (final) adds a relevant point: AI-assisted *development* is itself in scope; §14.4 treats model-authored changes accordingly.

## 11. Repository architecture, integrity and JW1 semantic validation

### 11.1 JW1 semantic validation

JW1 owns its validators and exposes them as a CLI with a JW1-owned, versioned result contract (per-rule identifiers, subjects, outcomes). Engineering's adapter maps that into evidence records. JW1 tests live in `project/system/tests`. Semantic claims include authority resolution, identity and transitions, generated-view rebuildability and freshness, capture versus promotion, the WMR-H stale-write precondition and monotonic revision history, and the governed-or-error recognition rule (Research 272 §2). Each has witnesses drawn from the P-R8B-01-R2 corrected gates, which already encode seeded violations.

### 11.2 Architecture boundary claims via absence execution

Static import analysis (EC1) is necessary but insufficient; it misses dynamic imports, shared resolution and data-path coupling. WARRANT adds **absence execution** (EC5):

```text
AB1  Product runtime tests pass in a checkout where project/ does not exist
     (Product runtime independence, AC4)

AB2  JW1 tests and validators pass in a checkout where project/engineering/
     does not exist (JW1 must not depend on engineering)

AB3  JW1 framework tests pass with the ADS instance replaced by a fixture
     instance (PSMF framework/instance seam)

AB4  Product and Project environments resolve from their own locks with no
     root lock present (independent dependency resolution)
```

Each has a witness: seed a forbidden import and the absence run must FAIL.

### 11.3 Repository integrity claims

Extracted from the current aggregate (Research 273 §3), each as its own claim: numbered identity uniqueness, family/header consistency, reference integrity (declared, path and link), legacy validation-evidence preservation, routing consistency against governing state, collaboration-state coherence, knowledge-navigation integrity, root-anchor freshness (Research 258 CL-9), root-entry bound, and hash-basis/line-ending normalization. Each is dispositioned (§12) against the accepted R7/R8 information architecture rather than ported.

### 11.4 No aggregate as gate object

The G2 decision is the conjunction of individually consequenced claims. A human-readable "repository integrity: PASS" line may be generated from the decision. It is a view, never an input.

## 12. Migration, shadow and equivalence qualification

### 12.1 Extraction ledger

For every current workflow, script and test:

```text
mechanism -> actually enforced invariant(s), found by reading AND by
             mutation (break the mechanism and observe; name alone is not
             evidence, cf. E1)
          -> historical evidence depending on it
          -> disposition RETAIN | AMEND | SUPERSEDE | RETIRE (Research 273 §13)
          -> successor claim(s) or retirement reason
          -> known-bad corpus: inputs the mechanism is known to reject
             (its own regression tests plus seeded mutations)
```

### 12.2 Shadow operation

Successor claims run in OBSERVE mode alongside the current mechanism on the same subjects: every promotion, a sampled corpus of historical commits, and the known-bad corpus. Verdict pairs are classified:

```text
AGREE
SUCCESSOR_STRICTER      acceptable if the stricter rule is an intended amendment
SUCCESSOR_WEAKER        blocking divergence unless explicitly amended by owner
OLD_WRONG               old mechanism false positive or false negative
BOTH_WRONG              both miss a seeded violation; new claim required
```

### 12.3 Equivalence target

Parity is at the claim level, never output text or workflow name (Research 273 §13). Intentional divergences are recorded with owner disposition.

### 12.4 Release criterion for an old mechanism (kill-set rule)

```text
K1  For each RETAIN/AMEND invariant, the successor's kill set on the
    known-bad corpus is a superset of the old mechanism's kill set
    (or every difference is an owner-accepted amendment)
K2  No unexplained SUCCESSOR_WEAKER divergence across a preregistered
    number of consecutive promotions
K3  Successor warrant ACTIVE with witnesses passing
K4  Explicit owner release decision per mechanism or mechanism group
```

Only then does the old mechanism lose oracle duty. The kill-set rule is sharp and measurable, and it is exactly what MC-0027 lacked.

### 12.5 G7 cutover for the W5 / R8 authority switch

Beyond equivalence: reference-graph integrity over the full inbound-reference set (Research 258 §12), derivative-free reconstruction from `project_anchor.json`, rule-based loss-accounted conversion evidence, rollback executed in a drill (not only documented), and owner authorization bound to the exact transition-manifest digest.

### 12.6 Preliminary classification of current mechanisms

PRELIMINARY — by name and the files read above; every row still requires extraction per §12.1.

```text
LIVE ORACLES (retain oracle duty until K1-K4)
  repository-integrity, checkpoint-metadata, current-routing-consistency,
  knowledge-map-integrity, model-collaboration-state, public-release-audit
  scripts: repository_integrity, check_repository_integrity,
  check_current_routing, check_checkpoint_metadata, check_knowledge_map,
  check_model_collaboration_state, check_private_continuity,
  check_chat_rotation_preflight, public_release_audit
  + JW1 validator invocation; the current unit tests for these paths

PRODUCT REGRESSION SOURCES (extract Product invariants into Product claims;
oracle for those invariants only)
  v1-persistence-vertical-slice, v1-source-universe-substrate,
  v1-knowledge-roundtrip, v1-knowledge-interchange,
  v1-methodological-horizon(-builder), v1-selective-context,
  v1-semantic-retrieval, v1-retrieval-fusion, v1-disposition-semantics,
  v1-python-project-tooling, v1-architecture-falsification
  + tests/integration/* and Product unit tests

FROZEN RESEARCH / LIVE-EVALUATION RUNNERS (reproduction evidence under
AC13; research terminal disposition applies; not target oracles)
  v1-reasoning-context-value(-live, -preserve), v1-disposition-semantics-live,
  v1-blocking-calibration, v1-runtime-bakeoff, v1-live-launcher-probe,
  v1-persistence-tooling-spike, v1-autonomous-live-experiment-launcher-ci
  (its provider-free preflight tests may yield Product harness claims)

REPOSITORY MUTATORS (leave assurance; re-home as governed tooling with AC10
mutation-safety claims, or retire)
  normalize-legacy-checkpoint-metadata, refresh-frontend-visual-baselines,
  v1-autonomous-live-experiment-launcher

PAUSED PRODUCT-INTERACTION / DESIGN FIDELITY (dormant oracles; re-evaluate
when frontend work resumes)
  cockpit-implementation-provenance, cockpit-reintegration-fidelity,
  v1-frontend-spike
  scripts: check_cockpit_*, select_cockpit_verification

HISTORICAL REPRODUCTION
  prototype-v0-tests

COLLABORATION / BRIDGE EVIDENCE VALIDATORS (oracles for their manifests;
owner likely JC5 or bridge governance, private-companion boundary)
  check_github_app_*, check_github_connector_*
```

Nothing is deleted by classification. Git history already preserves every mechanism; "archive" means untriggered and dispositioned, not removed.

## 13. Build, dependency integrity and artifact/release provenance

```text
B1  Every evidence-producing environment resolves from its owner's lock in
    locked mode; ad-hoc additions (E7) make the record HARNESS_INVALID for
    blocking use.
B2  Lock drift, dependency-policy and licence claims run at G2 and M2.
B3  One hash basis for every source digest: committed Git blob bytes.
    Working-tree digests are never evidence.
B4  Build once at G3 from the admitted tree; record artifact digest, builder
    identity and all lock digests; generate an SBOM at build (format open).
B5  Artifact-specific tests run against the built bytes, not the source tree.
B6  Promotion and release reference artifacts by digest and never rebuild.
B7  Platform-signed provenance (SLSA Build L2-equivalent) begins at the first
    artifact consumed outside its builder's process. Build L3 hardening is
    not targeted until a threat model warrants it. No SLSA level is claimed
    by default.
B8  Signed provenance counts only when verified at consumption: G4 and G5
    verify provenance against expected builder, source and policy.
```

Existing Project-tooling releases (E9) are the first concrete G3–G6 subject. Their assurance can adopt this model inside the private companion, publishing public digests only.

## 14. Security, privacy and supply chain

### 14.1 Identity and authority — the largest open risk

Under E2, every author (owner, ChatGPT, Claude, Codex, automation) acts through one Git-host identity, and one integration holds repository administration. Consequences:

```text
- any author could, in principle, change branch protection, workflows or
  gate policy; the ratchet (§5.6) detects weakening in content, but not a
  host-settings change made outside content
- model-to-model review is not authenticated two-party review; SLSA
  Source-track two-party review cannot be honestly claimed
- AC14 "review cannot be silently bypassed" is enforceable in content,
  unenforceable at the host-settings layer
```

Recommended direction (owner decision required): separate identities by role — owner (admin), authoring automation (content write, no admin), gate evaluator and publisher (status and evidence write only), deployment controller (environment scope only). Host settings (protection, required checks, environments) become a scheduled M2 claim: live settings equal a declared, owner-approved baseline; drift is REVIEW_REQUIRED.

### 14.2 CI supply chain

```text
S1  All third-party actions/images digest-pinned; update through reviewed
    change with automated freshness proposals (E8)
S2  Default token permission read-only; write permissions only in a
    separate publish job after adjudication
S3  No secrets in G1/G2 jobs; secrets only in protected evaluation or
    delivery environments with explicit authorization
S4  Never execute candidate code in a privileged, secret-bearing context
    triggered by untrusted input (fork PRs, comment triggers)
S5  Provider path filters never gate blocking evaluation (E4)
```

### 14.3 Public/private boundary

Leak claims (secrets, private paths including UNC and drive-relative forms, private companion identifiers) run at G2 with seeded-secret witnesses, extending the witness set the W0 G012 work already found necessary. Private evidence publishes only digest and classification publicly.

### 14.4 AI-authored change

Model-authored changes pass the same gates as any change. Additionally: agent instructions and repository content are data, never authority to change gate policy (§5.6 ratchet enforces this); large model-authored assurance-surface changes receive REVIEW_REQUIRED automatically.

## 15. CI logical topology and provider boundary

### 15.1 Trigger classes

```text
T-CHANGE     push to any non-protected branch, PR update      -> G1
T-PROMOTE    attempt to advance a protected branch            -> G2
             (merge-queue entry or pre-push evaluation of the exact
             fast-forward tree; one required status per gate)
T-ARTIFACT   release request / tag intent                     -> G3, G4
T-DEPLOY     authorized deployment request                    -> G5, G6
T-SCHEDULE   time                                             -> M1, M2
T-DISPATCH   explicitly authorized campaign / research run    -> campaigns
```

### 15.2 Logical job graph (per gate)

```text
PLAN        catalog + effective policy + selection + reuse lookup
  -> EXECUTE  fan-out by resource class (linux, windows where declared,
              browser, protected evaluation); each job runs owner
              entrypoints, emits records
  -> WITNESS  re-witness any changed verifier
  -> ADJUDICATE  evaluator -> decision
  -> PUBLISH  one gate status, report, bundle, durable receipt if
              decision-grade
```

### 15.3 Provider boundary

Provider configuration contains only triggers, runner selection, checkout, toolchain bootstrap, one kernel invocation per job, artifact upload and status publication. It contains no claim list, test list, threshold or path filter. Branch protection references one stable status per gate, so the claim catalog evolves without host reconfiguration.

GitHub Actions is an acceptable first provider — co-located with the repository host, with ephemeral runners and platform provenance — but nothing in WARRANT requires it. A provider change rewrites adapters and trigger files, not claims, warrants or evidence.

## 16. CD, deployment and live qualification

No Product environment exists today. G5 and G6 are specified and dormant until the first live Product environment. Project tooling delivery (E9) is live now and is the first subject.

```text
D1  Environment is a typed subject: identity, config schema version,
    secret references (never values), mutation authority.
D2  Deployment controller admits only releases with G4 ADMIT and verified
    provenance for this exact digest and environment class.
D3  Each release declares rollback mode:
      REVERSIBLE        prior release re-activatable, data compatible
      RESTORE_REQUIRED  rollback requires data restore (drill-backed)
      FORWARD_ONLY      no rollback; owner authorization explicit at G4
D4  Activation is single-attempt; uncertain outcomes are reconciled by read.
D5  Readiness is semantic: probes exercise capabilities the release claims
    (E9: HTTP 200 while missing a dependency binding is a known false ready).
D6  The rollback path is itself qualified. It must not depend on
    target-release-only tests (E9 publisher defect).
D7  No live mutation from unrelated repository activity: only T-DEPLOY
    reaches an environment.
```

Environment topology (dev / preview / production), push versus pull deployment, and SLOs remain open (§23).

## 17. Failure, retry and flaky-test policy

```text
R1  Every attempt is a record. Decisions cite all attempts.
R2  INFRA_ERROR may be retried automatically, bounded (default 1), by the
    runner, which classifies infrastructure failure before any verifier
    outcome exists. A verifier cannot request its own retry.
R3  FAIL is never retried to PASS for DET verifiers. A later PASS on the
    same input digest yields NONDETERMINISTIC.
R4  Flaky verifiers are quarantined as verifiers; their claims become
    UNVERIFIED (§10). Quarantine creates a tracked item with owner and
    expiry; expiry without resolution raises the claim to REVIEW_REQUIRED
    at every gate.
R5  MUTATION_UNCERTAIN is never retried; reconciliation reads decide.
R6  Stochastic claims are not retried; see C1.
R7  Flake rate per verifier is an M2 observational metric with a
    preregistered threshold that triggers quarantine review.
```

## 18. Evidence retention and publication

```text
CLASS            STORE                                RETENTION
EPHEMERAL        provider run artifacts, local cache  days-weeks; never
                                                      decision-grade
DECISION         content-addressed receipts (WMR-H    permanent
                 individual immutable JSON), stored
                 OUTSIDE the qualified tree so recording
                 a decision never changes the subject
                 (candidate: dedicated append-only
                 evidence ref in the same repository)
RELEASE          bundle bound to the release           lifetime of release
                 identity                              + declared tail
RESEARCH         result bundle + harness digests +     permanent while any
                 preregistration digest; committed or  accepted conclusion
                 durable store; never provider-only    cites it
PRIVATE          private companion store; public       per private policy
                 receipt holds digest + class
```

Human-readable qualification summaries under `project/knowledge/evidence/qualification/` cite receipt digests. They are carriers of meaning, not evidence stores. Every decision-grade receipt carries the harness/verifier digests that produced it — the provenance gap MC-0027 found in `result.json`.

## 19. Cost, latency and scalability

```text
L1  Budgets per profile: F0 seconds (--changed) / about a minute (full local
    promote plan where feasible); G1 minutes; G2 target <= 15 minutes
    wall-clock; campaigns budgeted in money and tokens with hard ceilings
L2  Evidence reuse by exact declared-input digest at >= required tier
L3  Conservative selection: an unclassified changed path forces full
    selection; G2 always covers every BLOCK claim through fresh evidence
    or exact-digest reuse
L4  Hermeticity audit (M2): run verifiers with only declared inputs present;
    any mismatch disables reuse for that verifier (reuse fails safe)
L5  Platform matrix only where a verifier declares platform sensitivity;
    Windows mandatory for path, line-ending and hash-basis claims
L6  Assurance observability: per-claim duration, cost, flake rate, witness
    status, stale-evidence count, reuse hit rate, unwarranted-binding count
L7  Kernel TCB budget: kept deliberately small (order of low thousands of
    lines); exceeding it triggers re-evaluation (F6)
```

Heavy hermetic build systems are rejected at current scale and remain a scaling option if L2–L4 prove insufficient.

## 20. Phased realization — after acceptance, still without physical migration

Sequencing only; each step needs its own owner authorization and remains subject to Specification 028 reconciliation and AO-10.

```text
PHASE 0  extraction ledger for current oracles (no code)
PHASE 1  minimum kernel: catalog, adapters for existing pytest and
         validators, records, evaluator — OBSERVE mode beside current
         workflows (shadow from day one)
PHASE 2  warrants and witnesses for the first BLOCK set (governance + JW1)
PHASE 3  single required promote status + base-revision ratchet;
         begin kill-set releases of old oracles
PHASE 4  artifact/release service at the first external artifact
PHASE 5  deployment controller at the first live Product environment
         (Project-tooling delivery may adopt earlier inside the private
         companion)
```

## 21. Upstream findings

```text
U1  AMEND (exercises a deferred R8-A decision): project/engineering becomes
    an independently resolved Python project; see §7.2.

U2  CLARIFY/AMEND (low priority): R8-A engineering subareas checks/, tests/,
    tooling/ may need assurance-kernel, qualification and delivery homes.
    Exact physical names left to synthesis.

U3  CLARIFY Research 273 §8: consequence is a floor on the claim plus an
    actual consequence on each gate binding (§5.6).

U4  CLARIFY Research 273 §6: LG0 is a profile; LG1+LG2 collapse under
    exact-result evaluation; LG8/LG9 are processes (§8.1).

U5  REQUIREMENT AT RISK, not an architecture reopen: AC14 and trusted-
    evidence claims are only partly enforceable while all authors share one
    Git-host identity with admin-capable integration (§14.1). Owner
    decision needed on identity separation.

U6  CONSISTENT: WMR-H receipts (individual immutable JSON, content-derived
    locator) are adopted; storage location outside the qualified tree is a
    realization choice (§18).

U7  CONSISTENT: Product/Project split, independent resolution, JW1 semantic
    validation versus engineering repository validation and invocation
    direction, stable break-glass anchor — all retained and strengthened
    by absence execution (§11.2).

U8  SPECIFICATION 028 DELTA (later): validator residency, generated-view
    freshness claims, hash-basis declaration, receipt location — listed for
    reconciliation, not changed here.
```

No upstream accepted contract is materially falsified by this design.

## 22. Failure modes and falsifiers

### 22.1 Biggest failure modes

```text
FM1 CEREMONY OVERLOAD      declaring claims/warrants costs more than it
                           protects; the project builds assurance instead of
                           ADS
FM2 WARRANTED THEATRE      witnesses exist but are trivial; verifiers
                           special-case witness inputs
FM3 SELF-GRADING           an author weakens assurance through host settings
                           or unratcheted paths
FM4 SELECTION UNDER-TEST   declared inputs incomplete; reuse admits a
                           stale PASS
FM5 EVIDENCE LOSS          decision-grade evidence left in provider retention
FM6 STOCHASTIC LAUNDERING  campaigns rerun until PASS; model drift unnoticed
FM7 ORACLE LIMBO           old mechanisms never released; two systems forever
FM8 KERNEL FRAGILITY       the small TCB becomes a large, bug-prone
                           single point of failure
```

### 22.2 Falsifiers (any one amends or reopens WARRANT)

```text
F1  Maintaining claim/warrant declarations exceeds a preregistered share of
    change effort across the first N real changes -> collapse to
    test-embedded claim tags
F2  Witness gaming observed (a verifier passes a rotated witness it should
    fail) -> introduce hidden/rotated witness corpora held at base revision
F3  Sensitivity witnesses infeasible for more than a preregistered share of
    intended BLOCK claims -> the warrant bar is too strict for this project
F4  Adapter-at-consumer breaks repeatedly because native formats are
    unstable -> a neutral result contract is needed; test whether it
    requires a named root integration contract (Research 248 A1)
F5  The ratchet blocks legitimate evolution too often (owner-decision load
    above a preregistered rate) -> finer weakening classification
F6  Kernel exceeds its TCB budget or has blocking defects in shadow ->
    adopt an existing framework for execution, keep only claim/warrant data
F7  Hermeticity audit finds undeclared inputs that reuse would have
    admitted -> reuse disabled globally until input declaration is fixed
F8  Local/hosted divergence rate above threshold -> parity assumption false;
    split local and hosted plans explicitly
F9  Campaigns cannot reach decision power within budget -> AI quality
    claims stay REVIEW/ADVISORY; do not pretend to block on them
F10 Identity separation impossible on the host -> T2 independence weakens;
    reassess whether any evidence can be called author-independent
F11 An absence-execution claim (AB1-AB4) fails for a legitimate reason ->
    upstream falsification evidence for runtime/dependency independence;
    reopen through AO-4 rather than patch the claim
F12 A kill-set comparison cannot be constructed for a current oracle ->
    fall back to reviewed invariant equivalence and record the weaker basis
```

### 22.3 Kernel self-assurance

Minimum kernel claims, each with witnesses: FAIL never admits; stale evidence never admits; UNWARRANTED never admits at BLOCK; weakening without a bound decision never applies; reuse never crosses a digest mismatch; every attempt appears in the decision; a candidate kernel is adjudicated by the base kernel.

## 23. Open decisions

```text
OD1  identity separation on the Git host (U5) — owner decision
OD2  claim/warrant carrier: per-owner TOML manifests versus test-embedded tags
OD3  evidence record serialization (in-toto-compatible predicate or custom)
OD4  durable decision-receipt store (evidence ref versus external store)
OD5  test frameworks, static analysers, coverage tools (pytest plausible;
     not selected)
OD6  first CI provider confirmation and host enforcement mechanism for
     fast-forward promotion (required status on push versus merge queue)
OD7  witness rotation / hidden corpora (only if F2 fires)
OD8  budgets, freshness windows, flake thresholds, campaign sample sizes
OD9  SBOM format, signing mechanism, attestation store
OD10 Product environment topology, deployment mode, SLOs
OD11 physical names inside project/engineering (U2)
OD12 which current oracles receive kill-set treatment first
```

## 24. Comparison-ready summary

```text
ARCHITECTURE             WARRANT — Warranted, Bound-Evidence Assurance
PRIMITIVE                claim + verifier + WARRANT + evidence record +
                         gate policy + decision
CLAIM-FIRST SUFFICIENT   no; warrant with sensitivity witnesses added;
                         consequence moved to gate binding (floor on claim)
GATE SHAPE               1 feedback profile + 7 transition gates +
                         2 maintenance processes (covers LG0-LG9)
LG1 vs LG2               collapse under exact-result evaluation
ORCHESTRATION            federated declaration, single adjudication
DEPENDENCY DIRECTION     adapter at consumer; no workspace imports the kernel
LOCAL / CI               one plan graph; trust tiers T0-T3
TRUSTED EVIDENCE         hosted ephemeral (T2) required for blocking
                         promotion because authoring identity is shared
POLICY INTEGRITY         base-revision ratchet with mechanical weakening
                         detection
AGGREGATE                derived view only; never the gate object
STOCHASTIC / AI          harness + replay in CI; live sampling only as
                         preregistered, budgeted, non-retryable campaigns
RETRY                    diagnose only; DET flip = NONDETERMINISTIC defect
PROVENANCE NOW           source/evidence-bundle binding, one hash basis
PROVENANCE LATER         artifact signing at first external consumer
EVIDENCE PLANE           one model; stores split by durability and visibility
CD                       designed, dormant for Product; live for Project
                         tooling; rollback qualified, readiness semantic
MIGRATION                extraction ledger -> shadow -> kill-set superset ->
                         owner release per oracle
CURRENT WORKFLOWS        6 live oracles; product regression sources;
                         frozen research runners; mutators exit assurance
PROVIDER                 GitHub Actions acceptable first adapter; not required
UPSTREAM                 no reopen; engineering workspace AMEND (U1);
                         clarifications U3 U4; identity risk U5
BIGGEST RISKS            ceremony overload, witness theatre, shared identity
```

INDEPENDENT_ASSURANCE_CANDIDATE=COMPLETE
UPSTREAM_ARCHITECTURE_REOPEN=NO
CURRENT_MECHANISM_PRESERVATION_REQUIRED=NO
PROVIDER_LOCK_IN_REQUIRED=NO
PHYSICAL_MIGRATION_AUTHORIZED=NO
