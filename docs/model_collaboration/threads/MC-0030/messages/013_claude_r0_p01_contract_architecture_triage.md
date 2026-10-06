# MC-0030 Message 013: Claude Architectural Triage of the R0-P01 Implementation-Contract Audit

```text
Thread                          MC-0030
Message                         013
Author / collaborator           Claude
Role                            CRITIC / BOUNDED ARCHITECTURAL TRIAGE
Interaction environment         Claude
Interaction session             claude-04 / "04 - Assurance and Delivery Architecture Design"
Coordination branch             v1-source-vault-bootstrap-resume
Head verified                   c891cc88246a3dae7cc949b02ba534e2d3fca55a
Candidate                       GOVERNED_LEDGER_KERNEL_V02 (logical target THIN_CENTRED_HYBRID_V03)
Probe                           R0-P01 (Research 513 §5; Research 518; Checkpoint 854)
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Verification and routing disclosure

```text
remote head (git ls-remote)        c891cc88246a3dae7cc949b02ba534e2d3fca55a = handoff head
current_routing.json boundary      p-one-harness-implementation
MC-0030 STATE phase / next actor   R0_P02_CANDIDATE_IMPLEMENTATION / chatgpt   (stale; see below)
```

**Routing disclosure.** Neither the routing nor `STATE.json` routes this triage to Claude, and `STATE.json` still names the R0-P02 phase although Research 517 records R0-P02 as PASS. This message was written because the owner's handoff explicitly authorizes exactly this one bounded Message 013. The state lag should be reconciled by the task owner. Nothing else was written.

**Read:**

- Research 511, 512, 513 and 518; Checkpoint 854;
- every frozen P01 file: `fixture.json`, `implementation_contract.md`, `security_control_contract.md`, `result_contract.json`, `legacy_volume_inventory_rule.json`;
- MC-0030 Messages 002, 003 and 004.

No harness was implemented. No credential operation, owner trial or P01 result was performed or observed.

## 1. Overall disposition

```text
PROBE_CLARIFICATION_ONLY
```

This holds on one condition: six **architecture clarifications** (AC-1..AC-6, §3) must be recorded as clarifications of what Research 511/512 already imply. Each one follows from existing V02 text, such as prospective revocation, in-ledger order, issued_at being provenance only, signing that cannot include itself, and the AMEND-then-new-draft flow. None adds or changes authority semantics.

If the task owner or the owner prefers a *different* interpretation for AC-2 (admission-time signer authority) or AC-4 (what consumes an acceptance_id), that choice would change trust semantics. The disposition would then become `ARCHITECTURE_AMENDMENT_REQUIRED` for that item only.

One genuine architectural gap exists, but it is **not P01-blocking**: who may declare a compromise of which credential (§3.5). P01 can legitimately treat the compromise declaration as a trusted synthetic input. The gap is recorded for R1.

## 2. The 13 audit blockers

```text
#   FINDING                                   CLASS                 REASONING
1   digest algorithm / string representation  PROBE CONTRACT        V02 fixes SHA-256 + standard canonicalization; hex
                                                                    vs prefixed vs base64url is instantiation only
2   exact Acceptance Envelope projection      R0 REALIZATION CHOICE V02's semantics are determinable (AC-1); the exact
                                              + CLARIFY (AC-1)      production envelope schema is R1; P01 must pick a
                                                                    probe projection
3   semantic-base projection; signer-set      R0 REALIZATION CHOICE dual role is implied by V02 (AC-2); exact projection
    placement                                 + CLARIFY (AC-2, AC-3) is a probe choice; fixture's source_revision needs
                                                                    removal or redefinition (AC-3)
4   security baseline vectors / proof reuse   PROBE CONTRACT        intent is unambiguous; only the vector table and
                                                                    which owner proof each control reuses are missing
5   rotation dry-run exact transition         PROBE CONTRACT        V02 §7 fixes who may rotate; the template is missing
                                              (needs AC-6 state model)
6   recovery dry-run exact transition         PROBE CONTRACT        same; V02 §7 fixes that recovery is a governed
                                              (needs AC-6)          rotation event
7   trust-state mapping, roles, versions,     PROBE CONTRACT + R0   history/replay rules follow from V02 (AC-2, AC-4,
    historical verification, replay scope,    REALIZATION CHOICE    AC-6); scenario isolation and order are pure probe
    isolation/order                           + CLARIFY (AC-6)      design
8   compromise authorization, boundary,       PROBE CONTRACT        boundary coordinate follows from V02 (AC-5);
    affected position, comparison records     + CLARIFY (AC-5)      declaration authority = R1 gap, not P01-blocking
9   WebAuthn ceremony lifecycle, signCount    PROBE CONTRACT        standard RP policy choices; no V02 semantics
10  Arm C trial choice / provenance / timing  PROBE CONTRACT        C is non-selection; any fixed choice is fine
11  mechanical-timing ordering conflict       PROBE CONTRACT        internal contradiction in the contract text only
12  success / unavailable / failed            PROBE CONTRACT        result-schema completeness
    normalization
13  inventory byte basis (CRLF worktree)      PROBE CONTRACT        V02 already mandates Git-blob basis; the frozen
                                                                    artifact violated the architecture's own rule;
                                                                    semantic counts are unaffected
```

```text
ARCHITECTURAL DEFECT (blocking P01)        none
ARCHITECTURAL GAP (non-blocking, R1)       compromise-declaration authority matrix (§3.5)
```

## 3. Resolution of the five architecture-sensitive areas

### 3.1 AC-1 — Acceptance Envelope boundary (finding 2)

There is no contradiction between Research 511 and Research 512. They describe **three different objects**, and only one reading is non-circular. A signature cannot cover an object that contains the signature, so the "envelope" that `envelope_digest` hashes cannot contain the decision proof.

```text
AcceptanceEnvelope        the canonical SEMANTIC PROPOSAL, fixed before any decision
  (hashed -> envelope_digest)
    project_id, acceptance_id                (identity; must equal the statement's fields)
    governing source bindings                (exact carrier refs)
    effective boundary
    accepted effects (ordered) with closed accounting and completion / lineage /
      standing / authorization payloads
    dependency SELECTOR                      which governing state it depends on
                                             (effect IDs, contract IDs, signer-set subject
                                             when applicable, grammar/predicate versions)
    EXCLUDES  decision, shown bytes, proof, signer-set version, issued_at, provenance,
              semantic_base_digest

SignedAcceptanceStatement the owner's DECISION over that proposal (Research 512 §5 fields)
    envelope_digest + shown_digest + decision + semantic_base_digest
    + signer_set_version + context + project_id + acceptance_id + issued_at

AcceptanceRecord          what the ledger stores
    envelope + statement + proof + renderer profile/version + drafter/decision provenance
```

Research 511's "logical Acceptance Envelope containing ... decision, decision provenance, owner-authenticity proof" describes the **record**. Research 512 already separated the statement, which implicitly narrowed the hashed envelope.

Separating the dependency *selector* (in the envelope) from the dependency *digest* (in the statement) has a useful consequence. When a decision is invalidated by `STALE_SEMANTIC_BASE`, the owner re-decides the **same** envelope against a new base. The envelope digest is unchanged, and only the statement differs.

### 3.2 AC-2 — Semantic base versus trust root (finding 3)

**Both, for different reasons, without redundancy:**

```text
signer_set_version (statement field, ALWAYS)
    = the authorization context: which trust state authorizes this proof.
    ADMISSION RULE: statement.signer_set_version MUST equal the current signer-set version at
    the admission position. A statement signed under an older version is not admitted after
    a rotation; the owner re-decides under the current set.

signer-set state inside semantic_base (ONLY when the acceptance's SUBJECT is the trust root)
    rotation, recovery, compromise declaration, checkpoint policy: here the signer set is the
    thing being changed, so it is a substantive dependency, exactly like a predecessor
    effect's lineage head.
```

**Why this is implied by V02 rather than chosen.** Research 512 §7 makes revocation and rotation *prospective* and anchored to the effective boundary, and §8 makes order in-ledger. If admission accepted any statement merely valid under its *declared* historical signer set, an old-version statement could be admitted after the key was rotated out or revoked. That would defeat prospective revocation. The equality check at admission is therefore required, not optional.

It does not cause unnecessary invalidation. Rotations are rare governing events, and ordinary acceptances do not carry signer state in their semantic base, so unrelated acceptances never interact through it.

Consequence for the fixture: placing `signer_set_version` outside `semantic_base` is **correct for owner trials S01–L01**. For controls 11 and 12, the semantic base must additionally contain the signer-set state being changed (version plus a member-set digest).

### 3.3 AC-3 — Semantic-base hygiene (finding 3, unflagged defect)

Two properties follow from F-02/Research 512 §4 and must be explicit:

```text
NO REPOSITORY BINDING  the semantic base must not contain a repository/commit/source revision.
                       fixture.semantic_base.source_revision ("R0-P01-SYNTHETIC-BASE-V1")
                       must either be REMOVED from the digested projection or REDEFINED as a
                       synthetic governing-state label that no repository landing can change.
                       Otherwise control 9 tests nothing.
ABA SAFETY             each dependency enters the base with a monotonic version, such as a
                       lineage head or last-modifying ledger entry, not only its current value.
                       This prevents an old stale signed statement becoming admissible again if
                       a value later reverts.
```

### 3.4 AC-4 — acceptance_id consumption (findings 4 and 7)

Separate the two stages explicitly:

```text
VERIFY  (stateless)  proof + statement + signer public key -> VALID | INVALID
ADMIT   (stateful)   VALID statement + ledger state ->
                       acceptance_id unconsumed
                       signer_set_version == current (AC-2)
                       semantic_base_digest == recomputed current base (AC-3)
                     -> append LedgerEntry; acceptance_id CONSUMED
```

**Consumption predicate:** an acceptance_id is consumed by the first *admitted* decision statement for it, whatever the decision (ACCEPT, AMEND or REJECT).

- **ACCEPT** folds the effects.
- **AMEND / REJECT** record a final decision with no effects. A revised proposal receives a new acceptance_id that links to the predecessor draft.
- **A signed but unadmitted statement** — for example one rejected as stale — consumes nothing, so a re-decision under the same ID remains possible.

This matches the existing "AMEND → new draft revision; nothing accepted" flow and the "folds at most once" text. It gives every acceptance_id exactly one final decision in history.

For P01, control 1's PASS condition should read: **VERIFY = VALID and ADMIT succeeds**. Control 7B tests ADMIT on an already-consumed ID.

### 3.5 AC-5 and AC-6 — Trust-root state machine and compromise (findings 5–8)

Research 512 §7 already determines enough of the state machine for P01, provided the implied rules are written down:

```text
STATE            per project ledger: current signer-set version Vn = {members with roles}
ROLES            PRIMARY   authorizes ordinary acceptances and ordinary rotation
                 RECOVERY  authorizes ONLY trust-root transitions (recovery rotation; compromise
                           declaration); never ordinary acceptances           (AC-6)
GENESIS          V1 established once; TOFU recorded explicitly
ORDINARY ROTATE  statement by a V(n) PRIMARY; admission yields V(n+1); the target/new signer
                 alone cannot authorize it
RECOVERY ROTATE  statement by a V(n) RECOVERY credential; admission yields V(n+1)
REVOCATION       prospective: effective at its admission position
HISTORICAL       an admitted entry stays valid; it is verified against the signer set in force
VERIFICATION     at ITS sequence position, not the current one
COMPROMISE       declaration names boundary b = a LEDGER SEQUENCE POSITION              (AC-5)
                 (issued_at is provenance only, so time cannot be the boundary coordinate)
                 entries at sequence <= b signed by the key: unaffected
                 entries at sequence  > b signed by the key: REVIEW_REQUIRED / GOVERNING_OWNER
                 a conservative widening may move b earlier; it can never retroactively
                 invalidate, only route to review
```

**The genuine gap, non-blocking.** Research 512 says the declaration must be authorized by "a still-trusted current or recovery credential". It does not say which credential may declare which other credential compromised. A defensible default for R1:

- any credential may declare **itself** compromised, since the worst case is a denial of service routed to review;
- RECOVERY may declare PRIMARY compromised;
- PRIMARY may **not** declare RECOVERY compromised.

**Answer to area 5.** P01 control 13 tests the *classification consequence* of a boundary: post-boundary records go to review, pre-boundary records are untouched. It does **not** test declaration authorization. P01 may therefore treat the declaration as a prospectively trusted synthetic scenario input, provided the result labels it `DECLARATION_TRUSTED_SYNTHETIC_INPUT`. Requiring a signed declaration would add an owner signing event without testing any intended P01 property.

## 4. Smallest prospective clarification set to freeze before Codex resumes

The set is a superseding contract addendum, frozen before any credential use. No result has been observed, so Research 513 §2.1 permits prospective correction.

```text
P01-C01 DIGESTS            all digests SHA-256; repository/JSON fields lowercase hex, no prefix;
                           Arm B challenge = base64url (no padding) of the raw 32-byte
                           SHA-256(canonical statement bytes); Arm C line = lowercase hex of the
                           same digest
P01-C02 ENVELOPE           exact probe projection per AC-1:
                           {schema:"R0-P01-ENVELOPE-V01", project_id, acceptance_id, item_id
                            (trial or control id), title, summary, effects[fixture order,
                            all fields], dependency_selector}
                           canonical bytes per PROBE_JSON_V01; envelope_digest = hex SHA-256
P01-C03 SEMANTIC BASE      projection {grammar_version, predicate_semantics_version,
                           dependencies[sorted by effect_id: effect_id, status, lineage_head,
                           contract_revision]} (+ {signer_set:{version, members_digest}} for
                           trust-root items only); source_revision removed or redefined (AC-3)
P01-C04 ADMISSION MODEL    VERIFY vs ADMIT (AC-4); one isolated in-memory probe ledger per arm
                           per scenario; deterministic sequence numbers; consumed-ID registry
                           per ledger
P01-C05 TRUST STATE        per arm: V1 = {PRIMARY: arm credential; RECOVERY: Arm-A recovery
                           key}; role matrix per AC-6; historical verification per AC-5
P01-C06 SECURITY VECTORS   baseline = VALID_ACCEPTANCE statement (one owner proof P0);
                           controls 2-10 are in-memory mutations of P0 per the security
                           contract (7A changed ID; 7B second ADMIT of P0; 9 unrelated
                           metadata change outside every statement field)
P01-C07 ROTATION TEMPLATE  item TRUST_ROOT_ROTATION: V1 -> V2 {PRIMARY: target public key
                           (A: recovery public key; B: Arm-A primary public key)}; PRIMARY
                           signs (proof P5); negative control: same statement signed by the
                           target alone is rejected; version advances only after ADMIT
P01-C08 RECOVERY TEMPLATE  fresh isolated ledger at V1; item RECOVERY_ROTATION: V1 -> V2R
                           {PRIMARY: recovery public key as interim primary}; RECOVERY signs
                           (proof P6); negative control: a harness-generated in-memory test
                           key (not an owner credential) is rejected as unregistered; P0
                           re-verifies historically at its V1 position
P01-C09 COMPROMISE         ledger: seq1 GENESIS(V1); seq2 P0; boundary b = 2; seq3 one owner
        TEMPLATE           trial proof by the same PRIMARY (e.g. S01); declaration =
                           DECLARATION_TRUSTED_SYNTHETIC_INPUT; expected: P0 ADMITTED/unchanged;
                           S01 entry REVIEW_REQUIRED / GOVERNING_OWNER; both rows in the
                           comparison record
P01-C10 RUN ORDER          per arm: setup -> P0 + controls 1-10 -> S01, S02, S03, L01 ->
                           rotation (P5) -> recovery (P6) -> compromise classification;
                           owner security signing events per arm = 3 (P0, P5, P6)
P01-C11 WEBAUTHN           registration: server random 32-byte challenge, single use,
                           timeout-bound; one registration per arm attempt, recorded as a SETUP
                           event; owner cancellation is not NOT_REALIZABLE (one setup retry,
                           recorded); assertion: allowCredentials = registered ID; signCount
                           RECORDED, NOT GATED (synced passkeys may report 0); a deterministic
                           assertion challenge is safe because replay is prevented by AC-4
P01-C12 ARM C              S01 + L01; complete = exact expected line observed in a user-authored
                           message; provenance = chat message reference (unverifiable, recorded
                           as such); interaction count only, no timing gate
P01-C13 TIMING             decision-capture instant = semantic stop = mechanical start (one
                           timestamp); the final statement preview is displayed INSIDE the
                           mechanical window
P01-C14 NORMALIZATION      trial success = proof VERIFY VALID over the owner's chosen decision
                           (decision recorded; non-ACCEPT allowed for burden trials);
                           NOT_REALIZABLE / unavailable / failed -> success=false, timings null,
                           arm ineligible; L01 success has the same definition; eligibility
                           with any null = false
P01-C15 INVENTORY BASIS    rebind legacy_volume_inventory_rule.json to Git-blob basis:
                           source_bytes 119155,
                           source_sha256 2a3be898be6d7ac61d045a41492374d9fedb2ed3bf91734e4e07f0f20053355c;
                           record 71fd3b69... / 119279 as SUPERSEDED_WORKTREE_CRLF_BASIS;
                           counts re-verified unchanged (97 / 157; 62 / 17 / 11 / 7)
```

The architecture clarifications AC-1..AC-6 should be stated once in the freeze record as **clarifications of V02, not amendments**.

## 5. What must NOT change

```text
arms A / B / C, their exact mechanisms, and Arm C selection-ineligibility
the 13 security controls, their intent and the zero-miss gate
owner-trial packet S01 / S02 / S03 / L01 and its effect counts
mechanical thresholds (median small <= 60 s, max small <= 120 s, L01 <= 120 s, edits = 0)
proof-viability versus full-eligibility distinction and the REOPEN / AMEND / PASS rule
A-versus-B selection rule and the B tie-break
legacy volume gates (>100 acceptances or >90 minutes) and inventory counts
owner-result blindness: no trial result observed before the addendum freeze
no-retry-to-green and attempt integrity (Attempt 001 starts at the first trial credential
  invocation; WebAuthn registration is a recorded SETUP event under P01-C11)
secret boundary (no passphrase, private key or authenticator secret anywhere)
R0-P02 = PASS; GOVERNED_LEDGER_KERNEL_V02 retained; V03 not reopened
Specification 028 operational authority; no migration, production, extraction or
  authority switch
```

## 6. Evidence that would cause me to reopen GOVERNED_LEDGER_KERNEL_V02, not merely refine P01

```text
1  admission-time signer authority (AC-2) cannot be enforced without trusted time or Git
   topology, i.e. prospective revocation is unenforceable in-ledger
2  the semantic base cannot be made ABA-safe without repository-global binding (AC-3)
3  the envelope / statement / record split (AC-1) cannot preserve sign-what-you-see, e.g. the
   shown bytes cannot be bound without including mutable presentation state
4  compromise handling requires retroactive invalidation of pre-boundary entries, or a
   boundary coordinate other than ledger position
5  the task owner or owner rejects AC-2 or AC-4 in favour of an interpretation that weakens
   revocation or allows two decisions for one acceptance_id
6  the P01 result itself classifies REOPEN under its frozen rule (no proof-viable A/B arm)
```

Absent these, the 13 findings are probe-contract and realization-instantiation work, and V02 stands.

```text
MC0030_MESSAGE013=COMPLETE
DISPOSITION=PROBE_CLARIFICATION_ONLY (conditional on AC-1..AC-6 recorded as clarifications)
ARCHITECTURAL_DEFECT_BLOCKING_P01=none
ARCHITECTURAL_GAP_R1=compromise-declaration authority matrix
UNFLAGGED_FIXTURE_ISSUE=semantic_base.source_revision (AC-3)
HARNESS_IMPLEMENTED=false
OWNER_CREDENTIAL_OPERATIONS=none
P01_RESULT=NOT_OBSERVED
NEXT=CHATGPT_FREEZE_P01_CONTRACT_ADDENDUM_THEN_CODEX_IMPLEMENTATION
```
