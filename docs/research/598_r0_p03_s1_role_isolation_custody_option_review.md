# Research 598: S1 reviewer identity, role separation and protected-custody route criteria

**Date:** 2026-10-20
**Status:** SOURCE-FREE_SECURITY_BOUNDARY_REVIEWED / MOCK_POLICY_AND_NEGATIVE_CONTROL_TESTED / REAL_IDENTITY_AND_CUSTODY_HOLD
**Scope:** Extend Research 597 and Validation 265's transport/journal qualification with concrete reviewer/challenger/authorizer role constraints, identity-collision attack cases, author-packet release gates and public-receipt disclosure limitations. Compare candidate deployment approaches without assigning real reviewers or selecting the final private store.
**Basis:** Research 513/559/575/576/590–597, Validations 264–265; project HEAD at the start of this work: `9c2134d0219151989e94b20b8a92fc3175747c8f`.
**Provenance:** Exposed ChatGPT engineering coordinator, not a non-arm independent reviewer, neutral reference annotator or scored arm author.
**Authority:** Source-free engineering design and executed mock tests only. No acceptance of V0.4's semantic contract, real historical-source review, author-source admission, protected reviewer ledger, independent challenger, gold, B0–B4 score, Checkpoint 898 change or Specification 028 replacement.

## 1. Necessary distinction: a policy decision is not an authenticated caller

A policy such as “reviewer may propose; challenger may challenge; authorizer may authorize” is useful but only becomes an enforceable security boundary if the runtime **independently authenticates the invoking principal** and binds sessions, identities, permissions and past protected exposure across relevant systems.

The existing source-free S1 journal in Research 597 uses Python strings for fictional actors. Validation 265 correctly describes those as mock roles. This Research adds a fictional access-decision layer but **does not upgrade its labels to operating-system users or actual independent model identities**.

The project’s current Runtime Bridge has purpose-specific Codex workspace/trust controls, read-only and inherited permission profiles, and host-backed semantic Git operations. Those boundaries are useful for ADS tool execution; they do **not** prove that an independent reviewer, challenger, owner or future blind author is a separate authenticated principal, nor that all ChatGPT/Claude/provider context paths are isolated. Tool-root refusal is not Windows ACL denial. No external reviewer tool or trusted confidential output destination was qualified during this stage.

## 2. Roles, resources and required separation

The proposed logical security roles are:

| Role | Allowed purpose | Critical prohibition |
| --- | --- | --- |
| Independent non-arm source reviewer | Receive only approved source-status batches, preserve nuanced source and contamination assessments | Cannot become blind primary-task author, neutral gold/reference adjudicator, scored arm author or evaluator |
| Separate source-status challenger | Independently inspect appropriately scoped restricted evidence and preserve disagreements | Cannot be the original reviewer relabeled in another session |
| Owner-approved authorizer/custodian | Hold release authority, attested private journal and exact-asset commitments, source-world packet signoff | Cannot substitute a positive policy flag for verified reviewer identity, secure custody or sufficient source evidence |
| Future blind primary-task author | Receive only independently admitted, frozen neutral original source world | No reviewer ledger, old expected relevance, comparator-design hints, hidden gold or unqualified broad repo/tool access |
| Exposed engineering coordinator | Public-safe methods, code, aggregated progress and synthetic test evidence | No ability to certify independent semantic review by restating its own conclusions or to silently publish restricted output |

These are separable *trust functions*, not an instruction to create five specific user accounts or processes. Actual implementation can consolidate or distribute infrastructure only after demonstrating preserved security and scientific boundaries. A person's multiple devices/sessions are not independent simply because their session names differ; a distinct person/model/session can still share a disqualifying prior-exposure route.

For each actual actor and request, future S1 requires a grounded role/admission record with: stable externally supported actor identity, service/process/session context, independently observed permitted tools, access and historical exposure, approved resource scope, expiry/revocation, audit destinations and challenged linkage to other identities. Unknown attribution must remain a HOLD.

## 3. Negative evidence from the fictional trial

The new model in `experiments/r0_p03_navigation_probe/s1_role_boundary_synthetic.py` fixes an exact allowlist mapping of **five mock roles** to their simulated actions. A directory refuses changing one registered mock principal from reviewer to blind author and retains recorded fictional protected exposure across another session under the **same fake principal key**.

However, the new negative-control test deliberately enrolls a **different fake principal ID that could be an alias for the same real operator**. Because the directory has no external identity binding, it permits the supposed blind-author action. The test passes because it accurately exposes this vulnerability rather than pretending that a local dictionary prevents human/session identity substitution.

This is a fundamental architecture constraint, **not** a failure of a particular Python test. A real design needs an identity link or documented, accepted alternative that is strong enough for the role and Level B scope. It cannot claim success through an unverified self-attested user ID, a new Temporary Chat title, a prompt saying “act independently,” a model-generated signature or an unrelated Git identity.

Additional simulated tests establish only logic: self-claimed role override ignored, unregistered caller held, role-action matrix enforced against caller-supplied session string, public coordinator denied mock private ledger, mock exposure recorded, all fictional release-witness fields required, and deliberately variable public progress receipts refused. There is no actual username-to-session attestation, authenticated IPC, independent challenge, OS ACL, encrypted private store, cryptographic journal signature, protected external anchor or observed author UI.

## 4. Candidate identity and storage architectures, still open

The following routes can be combined; their ranking is **provisional risk-oriented guidance for choosing a testable next trial**, not an owner-approved deployment decision.

| Candidate | Strongest possible S1 evidence | Major cost, risk or missing qualification | Engineering direction |
| --- | --- | --- | --- |
| A. One local account and user-mediated session handoffs | Simple exact file transport, owner visibility and fast fictional tests | Same user and process can read both “roles”; session alias spoofing, chats and uploads outside restricted custody | **Insufficient alone** for claims of independent reviewer-private custody |
| B. Distinct owner-controlled OS principals, private ACLs and independent artifact anchor | Testable Windows access-denial, separate principal tokens and owner-owned private readback | Full process, service, backup, log, key and model/tool session exposure still require proof | Suitable *next synthetic real-principal test candidate* if approved, not automatically final |
| C. Authenticated, purpose-specific managed reviewer service with isolated storage | Central role-policy enforcement, narrow action APIs, event log and short-lived scope-bound grants | Provider trust/retention, service operations, deployment, credential lifecycle, log leakage and network risk | Suitable candidate for a source-free service-boundary test |
| D. Hybrid of isolated content delivery, restricted evidence ledger and separate publication gateway | Can decouple actor admission, evidence confidentiality, journal anchoring and author-facing disclosure | End-to-end consistency, principal mappings and multi-system recovery still challenging | **Promising conceptual test decomposition**, not an imposed future topology |
| E. Other discovered architecture or workflow | May meet constraints more simply or with stronger evidence | Must satisfy the same witnessed controls without importing unexamined assumptions | Explicitly available |

A real reviewer service may offer a stronger policy plane than a raw folder; a properly configured local principal setup may be easier to audit than a cloud endpoint. Neither is currently qualified. We must not select architecture solely because the existing ADS Runtime Bridge or Windows account can reach it.

## 5. Acceptance criteria for the next actual S1 security-boundary trial

The next owner-approved trial should use **fictional content only** and test, at minimum:

1. **Independent identity:** two actor identities are actually distinct in the chosen trust substrate (Windows tokens, provider-authenticated app actors or another justified mechanism), with verified principal/session continuity; a relabeled alias is rejected or the inability to detect it is explicitly bounded.
2. **Enforced authorization:** caller cannot select a trusted role, permission profile, unrestricted path or resource by supplying a string; test unauthorized reads and writes through every chosen actual interface and distinguish host OS denial from tool/workspace refusal.
3. **Private record security:** chosen restricted store enforces confidentiality and tamper/rollback detection with independently protected last-digest/sequence commitments; restarting processes and a recovery procedure cannot silently discard decisions.
4. **Exact transport and viewer:** manifest and renderer tests bind delivered and actually visible bytes, metadata and loaded/navigable assets, with attested source pin and explicit missing/unsupported conditions.
5. **Challenger and release:** a reviewer cannot self-challenge or authorize; unsettled material objections and parent revisions invalidate dependent proposed releases, without accidentally denying safe historical evidence.
6. **Anti-leakage publication:** old and new public receipts, names, counts, links, aliases and viewer-generated data are jointly checked against plausible externally known rosters; simulated filtering alone cannot certify safe disclosure.
7. **Audited owner authority:** exact permitted destinations, keys, identities, expiration/rotation and recovery are positively approved before actual protected data. No public Git, ordinary chat transcript or unreviewed private runtime folder becomes default reviewer-only storage.

The test plan must record what was actually executed, as well as what was blocked or unobservable. A failure in real identity or confidential access cannot be repaired by marking a Python role test PASS. The simplest adequate route should be preferred only after the competing alternatives have a comparable threat-and-cost evaluation.

## 6. Operational work boundaries and architecture-evolution triggers

During every build or trial, actively check: identity alias collision, permission bypass, unintentional logs/telemetry, stale session or secret bindings, leak through public metadata, uncertain backup/restore, inability to revoke issued grants, source-representation drift, journal rollback without independent anchor, time-scoped access changes and false restriction of harmless source claims.

When any trigger appears, evaluate whether the appropriate response is a change in **data structures, trust architecture, number of processes, provider, folder topology, Git branches, local execution, testing, CI/CD, owner handoff or scientific procedure**. All levels are redesignable. Preserve the authorized science and owner-facing evidence contracts while changing their implementation.

**Explicit stop:** The next trial requires approval before setting ACLs, creating privileged reviewer identities, connecting storage or apps, provisioning secrets, changing private repository routes, or exposing any genuine source/review material. Read-only capability inventory and synthetic code/tests are permissible without such mutation.

## 7. Bounded conclusion

The simulated role and receipt contract passed its adversarial tests (Validation 266), including a **successful negative control demonstrating that unlinked fake identities bypass mock continuity**. This narrows the architecture work: future qualification must obtain an *actual attested identity and independently held confidential evidence path*, rather than another series of increasingly detailed mock session flags.

The source-disposition V0.4 contract remains prospectively unaccepted, and no source-status reviewer, storage, challenger, gold annotator or scorer has been admitted. The path forward is a jointly evaluated, actual security-boundary **synthetic-only qualification trial** plus the targeted independent V0.4 method challenge when appropriate.

```text
S1_IDENTITY_ROLE_THREAT_REVIEW=COMPLETED_FICTIONAL
ROLE_POLICY_SIMULATION=TESTED
UNLINKED_ALIAS_IMPERSONATION_RISK=OBSERVED_AS_NEGATIVE_CONTROL
ACTUAL_IDENTITY_SEPARATION=NOT_TESTED
CONFIDENTIAL_CUSTODY=NOT_SELECTED_OR_TESTED
PUBLIC_PROGRESS_PRIVATE_INFERENCE_SAFETY=NOT_PROVEN
REVIEWER_OUTPUT=NO_REAL_DATA
S0_V04_INDEPENDENT_ACCEPTANCE=PENDING
S1_REAL_REVIEW=HOLD
SOURCE_ADMISSIONS=ZERO
REFERENCE_GOLD=NONE
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
