# Research 597: Source-free S1 reviewer transport and custody architecture threat review

**Date:** 2026-10-20
**Status:** NONSCORED_ARCHITECTURE_THREAT_REVIEW_COMPLETED / SYNTHETIC_HARNESS_SELECTED_FOR_TRIAL / FINAL_RESTRICTED_CUSTODY_UNDECIDED
**Scope:** Compare architectural approaches to S1 independent source-status review, distinguish what can be proven by a bounded fictional-only harness from the separate secure reviewer and source-world gates, and record triggers for redesign at every implementation level.
**Basis:** Research 513/559/576/590–596; Validation 262 and Validation 264; Checkpoint 898 and Specification 028. Public prechange HEAD `fd6a9f8358f2f403110d5eedfa53e86da0c1c579`.
**Authority:** Engineering research and a test-harness selection only. This does not select a final restricted reviewer solution or change the scientific/source architecture authority. Historical R0-P03 source pin and the 406 plus 2,133 inventory are descriptive references, not source inputs to the trial.

## 1. Correct target: independently reviewable evidence, not merely a folder or a ZIP

The role of S1 is to ensure that, **before potentially contaminated historical source bytes are supplied**, a real non-arm reviewer and separate challenger can receive exactly approved content, preserve decisions without accidental loss or unauthorized disclosure, and prevent their private context from reaching the fresh primary author. A reviewer correctly classifying a fictional input is not evidence for any of these runtime/identity/custody properties.

An adequate future solution needs separately reasoned controls for:

1. **Source evidence origin and transport:** pinned identities and content, complete delivery accounting, faithful representation, expected/actual hashes, and explicit partial/unsupported status.
2. **Role and identity:** what reviewer, challenger, authorizer, exposed coordinator and future neutral author can actually see, not only their declared names or chat titles.
3. **Restricted reviewer evidence:** confidentiality, integrity, audit history, durable and independently recoverable state, append-only revisions, and protected material that must never enter public Git or a fresh author packet.
4. **Semantic method:** source claim truth, temporal scope, authority, uncertainty, contamination, exact original excerpt dependencies, full-file inspection, and independently challenged candidate dispositions.
5. **Author-view boundary:** independently approved packet, exact rendering/asset/link/navigation surface, safe generated metadata, and source-world completeness.
6. **Public coordination:** nonanswer-bearing progress only, including cumulative-publication diff/join safety, without any implicit public release of private reviewer reasoning.

These are separable **control, content, evidence, identity and release planes**, but nothing here requires a fixed process count, deployment topology or existing ADS folder structure. Their implementation and workflow can change together when evidence warrants it.

## 2. Threats and experimentally falsifiable failure routes

| Threat | Mechanism of failure | Required witness in a qualified future solution |
| --- | --- | --- |
| Source identity substitution | A same-named file changes between manifest and reviewer read | Exact pinned blob/byte count/cryptographic hash comparison at reception and read |
| Missing/partial delivery | Roster is complete but contents truncate or disappear | Full expected-versus-observed roster, delivered bytes and explicit HOLD |
| Semantic inspection inflation | File hash PASS is misrepresented as whole source read | Separate instrumented representation coverage and reviewer inspection statement |
| Role collision | Reviewer of old answer-bearing content later presents as blind task author | Verified independently maintained exposure and role ledger, tested actual permissions |
| Ledger disclosure | Private contamination notes appear in logs, public commits or packet metadata | Restricted output destination, route-scoped access-denial tests and reproducible redaction |
| Journal loss or tamper | Last entries deleted, reordered, overwritten or forged | Append-only event identity, durable readback, external head/sequence anchoring, backup and recovery |
| False role security | Code checks the string `reviewer` but OS/service identity is unchanged | Actual Windows/service/provider identity and authorization tests |
| Dynamic author rendering | Hash of Markdown is static while loaded image/citation/snippet changes | Frozen asset/renderer manifest, observed end-to-end UI and readback |
| Packet inference leak | Two safe-looking paths, receipts or batches collectively reveal a protected answer | Packet-level and cumulative public-history adversarial disclosure challenge |
| Semantic authority inflation | A proposal is promoted to current deployment by a convenience tag | Source-grounded time/domain/authority/context witnesses and independent challenge |
| Circular co-release | Two legitimate source excerpts require each other for correct reading | Explicit conditional bundle and atomic packet challenge, without premature admission |
| Inappropriate blanket exclusion | Uncertain deployment, inert link or nonnormative evidence suppresses safe historical observation | Per-claim and per-disclosure materiality, supported narrower statements |

A threat review that finds a defect must record which plane failed and whether a different architecture, data representation, work procedure or authorization method is needed, rather than automatically patching an inherited folder/process.

## 3. Candidate architectures and trade-offs

The following are **unselected alternatives**, not a vote to preserve the present repository or Codexless Runtime Bridge.

| Candidate | Potential strengths | Open risks and hard qualification work | Present decision |
| --- | --- | --- | --- |
| A. Owner-mediated ZIP and separately hosted reviewer chat, storing responses manually | Little implementation work for synthetic intake; inspectable exact artifacts | Chat history and attachments are not qualified private storage, persistence/readback and actor isolation are external, manual transfer can leak or truncate protected notes | Valid for fictional intake only; insufficient evidence for real protected S1 |
| B. Owner-controlled local restricted workspace, dedicated reviewer/challenger credential boundary and encrypted event storage | Strong local data ownership and precise source-byte control are feasible in principle | Key lifecycle, actual user/process isolation, reviewer remote access, backup, crash recovery, external digest custody, telemetry and Windows behavior need direct tests | Viable candidate, not approved |
| C. Dedicated authenticated managed reviewer service with immutable content store and restricted journal | Explicit typed APIs, declarative access policy, possible service audit/automation | Service/network/provider trust, secret handling, deployment/CI, lateral access, logging, retention and compromise recovery; costs complexity | Viable candidate, not approved |
| D. Split content-addressed transport, independently restricted reviewer evidence store, separate authorization/presentation gateway | Modular substitution of storage/renderer/identity mechanisms, precise trust boundaries, independent packet sign-off | Distributed consistency, cross-system provenance, anchor custody, reviewer access and end-to-end release challenges need proof | **Promising logical decomposition for tests**, not a chosen physical deployment |
| E. An alternative found through engineering/prototyping | May outperform A–D in cost, assurance or ergonomics | Must demonstrate the same independently evidenced science and security controls | Explicitly open |

**Current decision:** Do not select a final real restricted ledger, local-vs-service topology, key format, branch structure or workflow. Select only a **disposable Python standard-library test harness** under `experiments/r0_p03_navigation_probe/` with tests in `tests/unit/`. The harness tests cross-plane failure logic without claiming actual authenticated endpoints, operating-system isolation or a reviewer database. The selected **harness architecture** is not a binding future architecture.

## 4. Prototype boundary and exact data

Prototype: `experiments/r0_p03_navigation_probe/s1_transport_custody_synthetic.py`.

It defines **exactly three, hard-coded, invented textual source blobs** bearing `S1_FICTIONAL_ONLY_NO_REAL_PROJECT_SOURCES_OR_GOLD`. No Git historical source, current R0-P03 source, private file, network endpoint, LLM source adjudication, cloud service or secret key is read or accepted through the fixtures. Manifest identities use byte count, SHA-256, simulated ref and real Git-blob-algorithm identity calculated **on those invented bytes**. Inputs to delivery verification are in-memory and restricted to the exact fake manifest.

The prototype separately models:

- exact-delivery agreement and explicit missing/altered/unexpected source failures;
- confirmed fake protected-exposure veto alongside separate missing-byte and possible-leak blockers;
- dynamic loaded assets, unfrozen navigable links, generated metadata and public history joins as independent fake author-view HOLD reasons;
- fictional conditional joint source release and missing/prohibited dependency holds;
- a local, append-only, fsynced **simulated** event journal in a caller-owned test directory, with mock reviewer, challenger and authorizer roles, proposal/challenge/disagreement, simulated release-ready state, invalidation and dependent invalidation;
- complete JSONL event-chain verification on reopen, detecting changed/reordered/torn records; and
- an externally supplied expected last digest/sequence comparison, detecting an otherwise internally valid shortened journal prefix.

The journal contains no actual protected evidence. Its actor names are **string labels**, and its hash chain has no digital signature or external confidentiality. A malicious writer able to rewrite the entire log can recompute its chain; a missing independent last-digest anchor cannot be detected simply from a valid prefix. A Python role check does **not** prove denied operating-system, cloud, browser, connected-app, chat-history or side-channel access. A fake boolean author-view condition does **not** mean that a real renderer, dynamic asset loader or publication-history leak has been instrumented.

The prototype has no release/export operation for real sources and no invocation that contacts the registered ADS historical source pin. It intentionally does not mutate the 406+2,133 population, old W5 65-carrier source world, experiment fixtures, protected reviewer registry or any current scored work.

## 5. Concrete redesign and improvement triggers from the trial

| Finding | Evidence | Implication |
| --- | --- | --- |
| Hash-chain valid-prefix truncation | A first-record-only journal can pass internal link verification after loss of the second record | **Observed architecture trigger:** require a separately durable, access-separated head/count commitment and explicitly protected resumption authority. Prototype now tests comparison against such a supplied commitment, not its storage |
| Dependency invalidation/reapproval | A dependent simulated authorization must remain invalid when a parent is re-approved after changing, rather than become active based only on the parent's latest status | **Observed architecture trigger:** pin the dependent authorization to parent evidence/version; require a fresh dependent review after any parent revision. An added synthetic regression now tests the corrected ordering |
| Role check limited to mock labels | `SIMULATED_REVIEWER`/challenger/authorizer checks run inside one Python interpreter | **Unqualified:** actual independent identities, ACL/service policy and reviewer-challenger separation require another tested boundary |
| File consistency does not establish author rendering | Fake asset, navigable link and generated-metadata booleans trigger HOLD | **Unqualified:** choose/qualify an instrumented viewer and immutable rendered snapshot; file-level hash alone cannot close this gate |
| Repository-root refusal differs from OS access denial | Existing `synthetic_custody_evidence_candidate.py` explicitly distinguishes tool root refusal, platform refusal and direct Windows denial | **Retain the distinction:** do not claim protected storage because Codexless refuses a path, or because tests pass in a sandbox |
| Strict exact batch cannot evaluate semantic importance | Delivery can certify three hardcoded files without interpreting their meaning | **Unqualified:** actual content-meaning review, time/status/materiality and separate challenger remain independent method/actor tasks |

The engineering team must continue looking for architecture redesign triggers during real S1 design, implementation and qualification. Files, directory structures, branch rules, testing, CI/CD, runtime tools and working procedures can all be redesigned. Any proposed migration or redesign must preserve trusted evidence, explicit owner authority, experimental independence and existing hard scientific gates.

## 6. Evidence standard and next bounded step

The complementary Validation 265 records actually executed Python tests. Passing them qualifies a **source-free prototype's narrow behavior**, not S1 readiness. No restricted storage path, key, real batch, independent actor, challenger, final author-rendering surface or release gateway has been approved. The experiment's source-world HOLD remains unchanged.

**Next bounded work:** evaluate/qualify the actual reviewer/challenger/custody authority options and a real testable transport+viewer architecture using only synthetic fixtures. Compare security boundary enforcement under the actual tools, readback after restart, external digest anchoring and packet metadata leak testing. If these are feasible only by redesigning repository layouts, external connectors, local account boundaries or workflows, explicitly propose that redesign with owner-reviewed authority and tests rather than silently inheriting the current arrangement.

The optional V0.4 bounded separate-session synthetic critique should target the newly resolved D1–D4 ambiguities plus the real-message/display distinctions. Its completion is **not** a substitute for actual S1 security qualification, and its pending status does not prohibit content-free engineering.

```text
S1_ARCHITECTURE_COMPARISON=RECORDED_NO_REAL_SELECTION
SYNTHETIC_HARNESS=SELECTED_AND_IMPLEMENTED
SYNTHETIC_SOURCE_COUNT=3_HARDCODED_FICTIONAL
REAL_SOURCE_READ_COUNT=0
REAL_REVIEWER_ONLY_LEDGER=NONE
REAL_IDENTITY_OR_ACL_PROOF=NONE
REAL_OUTPUT_CUSTODY=UNQUALIFIED
AUTHOR_VIEW_RENDER_PROOF=NONE
SCORED_R0_P03=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
