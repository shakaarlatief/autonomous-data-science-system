# Research 682: Provider-native CI receipt and natural-owner trust-root admission contract

**Date:** 2026-11-14
**Status:** TWO_LIVE_GITHUB_SOURCE_HISTORIES_INSPECTED / OFFLINE_ADMISSION_CONTRACT_EXECUTED / NO_AUTHENTICATED_OFFLINE_PROVIDER_PROOF / NO_OWNER_TRUST_ROOT_ADMITTED
**Scope:** Test a bounded source-relative evidence admission interface against two actual GitHub Actions histories, distinguish structural consistency from provider authentication, and specify concrete trust-root and currentness requirements without changing governing authority.
**Authority:** Exposed, unscored development research. Research 512 sections 3-9 and 14, Research 673, Research 676 and Research 680-681 remain authoritative in their original scopes. No new experimental J1, governing RELATIONAL J2, J3 SATISFIED, formal P03 score, credential creation, branch-policy change, physical target or migration.
**Initial shared head:** e29329b3097b593a917a386d33f900a3cf97b193 (Checkpoint 942, clean).
**Code:** experiments/r0_p03_navigation_probe/v03_provider_ci_admission_contract_v01.py
**Frozen derived source transcription:** experiments/r0_p03_navigation_probe/v03_provider_ci_receipt_source_snapshot_v01.json
**Immutable result:** experiments/r0_p03_navigation_probe/v03_provider_ci_receipt_admission_result_v01.json
**Tests:** tests/unit/test_r0_p03_v03_provider_ci_admission_contract_v01.py
**Validation:** 379. **Checkpoint:** 943. **Collaboration:** MC-0030 Message 096.

## 1. Actual connected provider observations

The authenticated, bounded GitHub App read interface was used directly in this interaction to fetch check-runs by exact commit SHA, native workflow-run records, and GitHub Git-commit signature verification. These reads are provider-source observations in the live tool context. A later model-authored JSON copy of their values does not itself become an independently authenticated provider response.

Two original real event histories are compared:

| Exact source revision | GitHub checks | GitHub workflows | Commit signature verification |
| --- | --- | --- | --- |
| 511224a037bf63031ead0eda61754702361eebd7 (Checkpoint 941) | 8 completed: six success, two Windows failure | Five runs, collaboration and integrity failed | verified=false, reason=unsigned |
| e29329b3097b593a917a386d33f900a3cf97b193 (Checkpoint 942) | 8 completed: all success | Five runs, all success | verified=false, reason=unsigned |

For the failed revision, GitHub identified:

    check 132549849947: validate-collaboration-state (windows-latest), run 43628566028, failure
    check 132549849558: repository-integrity (windows-latest), run 43628566327, failure

For the repaired revision, GitHub independently identified:

    check 132556677403: validate-collaboration-state (windows-latest), run 43630785845, success
    check 132556677109: repository-integrity (windows-latest), run 43630785821, success

The other six Checkpoint 942 check IDs are 132556677606, 132556676962, 132556677135, 132556676868, 132556676884 and 132556676772. All eight reported a matching SHA, completed status, issuer app github-actions (app ID 15368), and success. Its five provider-native workflow run IDs are 43630785845 (Model collaboration state), 43630785821 (Repository integrity), 43630785793 (Current routing consistency), 43630785731 (Checkpoint metadata) and 43630785693 (Knowledge map integrity). Each reported event=push, attempt=1, completed success, and the exact Checkpoint 942 commit SHA. Native workflow actors identify the GitHub account, not the initiating model session.

Direct provider source links:

    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43628566028
    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43628566327
    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43630785845
    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43630785821

This is a source-relative pair, not a policy declaring those exact eight names universally required. Different repository changes can trigger different workflows. A passing older commit is not evidence that the current head passed.

## 2. Experimental evidence compiler and immutable source identity

The code stores a 10,143-byte model-transcribed copy of the actual provider returns, SHA-256 cd37b2222f9efd1e10ba0c884f2fe27af63209abf7605015b7267f265de610bd. Its explicitly limited source role is DERIVED_EXPOSED_MODEL_TRANSCRIPTION_OF_GITHUB_APP_API_READS; offline_provider_authentication is false. This record is not GitHub-signed and is not an independent trust anchor. Pinning its bytes detects accidental drift, not a malicious rewrite of both the copy and its expected digest. Both the exact source transcription and its derived output are now explicitly marked -text in .gitattributes so Windows CRLF checkout cannot silently change their raw-byte identity. A dedicated negative-regression test checks their declared Git attributes, LF bytes and source digest.

The compiler rechecks the *actual local Git commit objects* and the original parent of both historical commits. Those facts are OBSERVABLE Git source data, not CI proof. It also reopens Research 680's original accepted four-effect experiment-only J1 source context, refusing changed effect scope or magically installed natural-owner/provider-verifier capabilities.

The strict admission specimen validates: source role and repository, exact event SHA, provider check IDs, positive run IDs and attempt, exact check-to-workflow/run association, app issuer, completed statuses, workflow outcome consistency, duplicate/missing checks, additional unapproved source fields, false signed-commit claims, and cross-SHA evidence substitution. Its explicit results are:

    CHECKPOINT_941 = STRUCTURALLY_RED_UNAUTHENTICATED_REPLAY, six success, two failure
    CHECKPOINT_942 = STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY, eight success, zero failure
    independently_authenticated_provider_receipt_offline = false
    independently_authenticated_model_or_connector = false
    qualified_relational_j2 = false
    eligible_for_governing_j3_completion = false

The code is not connected to GitHub and cannot refresh provider data. All offline decisions remain non-governing diagnostics even where the exposed interaction separately queried GitHub as a real source.

## 3. The decisive adversarial control

The 52 focused tests include wrong target SHA, stale/replayed success, missing or extra checks, duplicate IDs/names, wrong source SHA in a check/run, fabricated GitHub app identity, changed run attempt, incomplete or contradictory status, false commit signing, authority-field injection, source-copy mutation and revision-to-effect transplantation.

One deliberately forged specimen changes both actual failed 941 check results to success *and* changes their workflow conclusions to success. It is internally consistent. The checker calls it STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY. It still does not certify native provider authentication, model identity, J2 RELATIONAL coverage or J3. This is an intentional demonstrated boundary: no offline parser can derive issuer authenticity solely from plausible source text, regardless of how strict the schema is.

The exact source-relative inquiry set is frozen for this bounded engineering test. It must not be converted into a production required-check policy, a newly ratified J1 effect or a scored R0-P03 navigation task.

## 4. Proposed admission and trust-root contract

This section is prospective implementation guidance, **not owner approval** of a credential or policy.

**Governing owner and J1:** Research 512 sections 3-8 require an independently verifiable owner-exclusive acceptance statement for consequential governing decisions, bound to the exact acceptance envelope, displayed digest, semantic base, signer-set version and project context. GitHub author/committer names and a model-authored JSON field cannot replace that proof. The existing four experimental J1 effects remain conversationally owner-accepted in their bounded development world, not independently signed production acts.

**Natural owner and J2 RELATIONAL:** The natural realizer/source owner who declares COVERS is a separate principal. A qualified declaration must match the exact accepted effect/component and realization revision, be authenticated under a governing authorized principal/trust-root policy, and be unique per natural-owner fact tuple. A co-committed source claim without such verification is still only a candidate.

**Provider action and J2 OBSERVABLE/EPHEMERAL:** Git commit objects, provider CI check-runs, workflow-run resources and artifact digests can be independently observed where source platform APIs expose them. A provider-specific EPHEMERAL action requires an appropriate durable event receipt when its execution fact cannot be reconstructed otherwise. These facts must be bound to exact repository, SHA, resource/run/check ID, attempt, source issuance and an authorized provider issuer. The qualified adapter needs a server-owned authenticated read or independently verifiable signed statement, rather than a caller-selected token, URL or claimed authentication flag.

**Replay, freshness and recovery:** Retried actions, rerun attempts, changing check states, missing/filtered workflows, stale refs, deleted evidence and platform outages must produce exact currentness and bounded UNKNOWN behavior. Do not infer that absence of a check means success or that a historical 8/8 result satisfies the current branch tip. Recovery follows Research 512 section 14's actual provider capabilities, not an invented idempotency guarantee. Exact CI success does not establish that the status check was required before pushing on an unprotected branch.

**Semantic completion:** A verified CI job can prove only its own scoped execution/result. It does not prove Claude used a particular GitHub connector, that a given model authored the change, or that D1 E01's TRANSPORT_ATTESTED_GITHUB_CONNECTOR is satisfied. A separate J3 evaluator must apply the unchanged accepted REQUIRE components and ALL_REQUIRED rule. Source-owned OBSERVABLE facts need no invented RELATIONAL carrier; J2 RELATIONAL needs its genuine natural owner declaration; missing required evidence remains HOLD/UNKNOWN.

**Confidentiality and governance:** Any future provider adapter must avoid public secrets, keep sensitive receipts protected, permit revocation/rotation without rewriting history, and preserve explicit source-of-truth ownership. Candidate designs include authenticated GitHub App read adapters, independently verifiable provider-native attestations, source-owner scoped signing, signed owner acceptance, or combinations. None is selected by this test. No credential generation, Git signing, branch-protection change or CI policy upgrade has been performed.

## 5. Exact uncompleted questions

It is not yet established whether either model provider exposes an independently verifiable model-session/action signing key or durable native transport receipt, whether source owners need an agent-specific identity mechanism, whether a dedicated trusted adapter is operationally desirable, whether signed CI provenance could be made detached-verifiable, or whether the development branch should enforce mandatory checks.

The live connected GitHub service is suitable for provider-native check/run queries; the current Python verifier can only examine an exposed snapshot. Those are different capability levels. An actual qualified source-adapter integration, with a declared trust root and authorized owner policy, remains to be demonstrated. The user did not accept any new governing effect or operational policy simply by asking to continue the experiment.

Research 673's one finite formal admission method, Research 513/559/576 protected reference requirements, current Specification 028, historical D1_AMEND and the unselected physical architecture are untouched.

    RESEARCH=682
    GITHUB_NATIVE_EVENT_HISTORIES=2
    ORIGINAL_941_CI=6_SUCCESS_2_FAILURE
    ORIGINAL_942_CI=8_SUCCESS
    SOURCE_COPY=DERIVED_UNAUTHENTICATED
    OFFLINE_PROTOCOL=STRUCTURALLY_QUALIFIED_NON_GOVERNING
    NEW_ACCEPTED_J1=0
    EXISTING_P03_EXPERIMENT_ONLY_J1=4
    NEW_QUALIFIED_RELATIONAL_J2=0
    INDEPENDENT_MODEL_IDENTITY=UNVERIFIED
    ORIGINAL_E01_J3=HOLD
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
    NEXT=ACTUAL_TRUSTED_SOURCE_ADAPTER_AND_AUTHENTIC_SOURCE_OWNER_FEASIBILITY
