# Validation 265: R0-P03 S1 fictional transport and simulated evidence-journal exercise

**Date:** 2026-10-20
**Status:** SYNTHETIC_MECHANICS_PASS / S1_REAL_CUSTODY_NOT_QUALIFIED / REAL_SOURCE_REVIEW_HOLD
**Scope:** Evidence-bound qualification of the first source-free S1 transport/custody simulation following Research 597 and prospective Validation 264. This is an actual *engineering test report*, **not** a pass for actual restricted reviewer storage, independence, real source inspection or scientific reference custody.
**Authority:** Code-and-test-only, no modification of Checkpoint 898, Specification 028, Research 513/559/576, source admission, independent author source world, old W5 gold or B0–B4 scoring.

## 1. Exact test target and synthetic boundary

```text
Implementation: experiments/r0_p03_navigation_probe/s1_transport_custody_synthetic.py
Focused tests:  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
Existing tests: tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py
Source inputs: 3 constant fictional text blobs created inside the module
Fixture marker: S1_FICTIONAL_ONLY_NO_REAL_PROJECT_SOURCES_OR_GOLD
Source pin actually read: NONE
External network/LLM/Git corpus read in trial: NONE
Runtime credentials, private reviewer output or actual old relevance answers: NONE
Trial journal path: pytest tmp_path; path name synthetic_s1_events.jsonl
Restricted reviewer storage selected or changed: NONE
```

The prototype is **not** an authorized source-admission or private-ledger tool. It uses in-memory fixture bytes, optionally writing only the invented event records under isolated temporary pytest directories. The journal's allowed actor strings are mock permissions, not independently authenticated principals.

## 2. Executed regression results

First execution:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_s1_synth_20261020
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py

17 passed in 0.31s
```

After adding an explicit externally supplied journal head/sequence comparison, the second execution used the new test module **plus** the pre-existing fake C1 custody-classifier module:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_s1_synth_20261020b
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
  tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py

29 passed in 0.26s
```

A final dependency-reapproval adversarial test was then added. The earlier journal behavior could have allowed a dependent simulated release to become usable again after a parent was invalidated and later re-approved, without re-challenging the dependent. The corrected simulation requires the dependent's ready event to postdate its current parent's ready event. A fresh dependent proposal/challenge/approval is necessary after parent re-approval.

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_s1_synth_20261020c
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
  tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py

30 passed in 0.38s
```

These tests were executed via the registered Runtime Bridge `codex.command_exec` operation, in the authorized public ADS workspace, with the inherited local Codex permission profile. No native Git staging/commit/push bypass was used for project publication.

## 3. Observed passing properties and their limited meanings

| Trial | Actual verified behavior | What remains unproved |
| --- | --- | --- |
| Fixed manifest source identities | Exact in-memory fake content sizes, SHA-256, Git-blob-style OIDs and a deterministic manifest digest | Real historical source scope, independently controlled source pin or source access |
| Missing/changed/unexpected/truncated delivery | Returns HOLD and explicit absent/changed/extra records; nonbytes and alternative manifest rejected | Network, ZIP, identity attestation, replay prevention across separate machines |
| Candidate status without release | A completely simulated, safe source can be `ELIGIBLE_PROPOSED` without actual author exposure | Independent semantic reviewer or author authorization |
| Compound blocker | Confirmed fake protected exposure retains `PROHIBITED_EXPOSURE` even when expected bytes are missing; deficit remains separate | Correctly detecting real protected content or evidence materiality |
| Viewer and public-receipt risk flags | Simulated changing assets, navigable links, metadata and prior-receipt join conditions yield HOLD; inert nonmaterial citation does not | Instrumented actual author UI/render/citation/download, cumulative history visibility |
| Atomic fake bundle | Jointly sufficient fictional pair can be conditional without earlier individual authorization; missing/prohibited dependency remains held | Real semantic source closure or complete family coverage |
| Journal mock actors | Reviewer proposal, challenger accept/dispute, simulated authorizer and author denial follow intended in-process states | Windows/OS ACLs, genuine independent identity, credential handling, cross-provider data separation |
| Journal write/readback/reopen | JSONL hash-linked event append and fsync, recovery of all completed fake records across new Python object, duplicate and illegal transitions rejected | Complete OS crash/power-loss durability, malicious writer resistance, encrypted confidential storage |
| Corruption and invalidation | Edited/reordered/torn record fails; upstream invalidation causes downstream simulated release-readiness to become false; re-approval of the parent does not automatically revive the old child without a new child review | Full versioned dependency invalidation of a real multi-system author packet |
| Valid-prefix truncation and external anchor | A shortened but internally consistent JSONL prefix is **not** detected by the chain alone; supplying the expected last digest and event count detects it | Independent custody/authentication/anti-rollback of that external anchor |

The test outcome is intentionally **two-sided**: it includes cases preventing false release and cases preventing unnecessary exclusion of fictional, harmless source material. No generated simulated status is a real author release or scored result.

## 4. Architecture qualification implications

**Positive engineering proof:** Byte equality and a bounded in-memory role/event state machine can be mechanically checked; journal open/readback catches detectable internal corruption; a separately supplied expected last digest/sequence is necessary to catch valid-prefix loss. The existing fake custody-classifier regression still rejects conflation of workspace-root refusal with actual Windows OS denial.

**Important unqualified properties:**

1. **Confidentiality:** No encryption, key management, independent access-controlled identity or protected real destination was tested. A public code module and pytest temp files are deliberately not an actual restricted reviewer ledger.
2. **Tamper resistance:** Hash chaining detects accidental corruption but a privileged malicious writer can replace all rows and recompute hashes. The test supplies an external expected anchor in memory; it does not provide a trusted **separate** anchoring service or durable external custody.
3. **Role independence:** Mock labels are forgeable in the same process; an author permission exception proves only the branch, not denied OS/tool/cloud/browser access. No real reviewer/challenger/authorizer has been assigned.
4. **Delivery and representation:** Fixed fabricated in-memory text is far narrower than a real pinned historical corpus, binary/unsupported representations or end-to-end batch transport across an actual reviewer tool.
5. **Author-view enforcement:** Boolean risk flags are manually supplied, not inferred or instrumented. Nothing inspects actual viewer-generated download headers, citations, redirects, generated snippets, navigable links or cumulative public release history.
6. **Semantic judgment and independent challenge:** No human/model source-status claim was actually evaluated. The old nine-case W5 reference route, 406+2,133 historical review population and scientific stage gates were not exercised.

**Architecture trigger identified:** A self-contained hash chain cannot prove journal completeness after valid-prefix truncation. Real reviewer custody must supply an independently protected external head/count commitment with recovery semantics, or another validated architecture with equivalent independently verified anti-rollback. The choice of source of truth, test harness, restricted store, CI/CD, branch scheme and workflow stays open; do not treat this simulated file format as a mandated production foundation.

## 5. Qualification status and next action

Validation 264 is still a prospective qualification plan; this Validation 265 executes only its **fictional source-free** stage. Research 597 documents competing logical/physical architectures, trust planes and evolution triggers. The prototype's successful unit tests are a narrow validated property of source-free mechanics and justify starting a **separate S1 role/custody/transport boundary evaluation**, not opening protected historical materials.

The next engineering decision is **which actual reviewer/challenger/access and durable confidential evidence-custody route can be observed and independently qualified**, comparing owner-controlled local, managed service, mediated and hybrid approaches, including full readback/recovery, restrictive identities and author-view disclosure behavior. Obtain owner approval before connecting any real protected destination, granting permissions, rotating keys or delivering historical source batches. A V0.4 synthetic independent method critique can be performed in parallel but does not count as S1 qualification.

```text
VALIDATION_265=SYNTHETIC_SOURCE_FREE_MECHANICS_PASS
S1_FOCUSED_TESTS_FIRST_RUN=17_PASS
S1_PLUS_PRIOR_FAKE_CUSTODY_TESTS_INITIAL=29_PASS
S1_PLUS_PRIOR_FAKE_CUSTODY_TESTS_FINAL=30_PASS
DEPENDENCY_REAPPROVAL_INVALIDATION=TESTED_FAKE_ONLY
EXTERNAL_HEAD_COMPARISON=TESTED_WITH_FAKE_EXPECTED_VALUE
EXTERNAL_ANCHOR_CUSTODY=NOT_TESTED
OS_ACCESS_ISOLATION=NOT_TESTED
RESTRICTED_DATA_CONFIDENTIALITY=NOT_TESTED
REVIEWER_INDEPENDENCE=NOT_QUALIFIED
REAL_SOURCE_INSPECTION=ZERO
S0_V04_INDEPENDENT_ACCEPTANCE=NOT_DONE
S1_REAL_CUSTODY_AND_TRANSPORT=NOT_QUALIFIED
AUTHOR_SOURCE_ADMISSIONS=0
B0_B4_SCORE=NOT_RUN
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
