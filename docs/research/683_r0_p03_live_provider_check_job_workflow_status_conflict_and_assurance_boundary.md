# Research 683: Live GitHub provider-source reconciliation, contradictory check status, and finite trust-root escalation boundary

**Date:** 2026-11-14
**Status:** ACTUAL_CONNECTED_PROVIDER_READS_EXECUTED / ONE_REPEATABLE_CROSS_ENDPOINT_CONTRADICTION / STRICT_NONPROMOTING_RECONCILER_EXECUTED / SOURCE_OWNER_AUTHENTICATION_NOT_AVAILABLE_FROM_INSPECTED_SURFACES
**Scope:** Reopen the exact source result from Checkpoint 943 that could not be qualified as eight completed successes. Reconcile multiple real, server-owned-authentication GitHub App read surfaces, preserve their exact source IDs and report a bounded state contradiction rather than silently overruling any source. Evaluate whether present connectors can bind an agent-exclusive natural owner and establish a credible next architecture discriminator.
**Authority:** Exposed unscored source and architecture qualification under Research 512 sections 3-9, 14, Research 673, Research 676 and Research 680-682. No accepted new J1, genuine RELATIONAL J2, original historical D1 provider proof, governing J3, production credentials, CI policy, architecture selection, migration or formal P03 score.
**Starting exact clean shared HEAD:** 2a7f8fe3f170840262122296d9b7f3e54664bc39.
**Code:** experiments/r0_p03_navigation_probe/v03_live_ci_provider_reconciliation_v01.py
**Exposed provider-source relay:** experiments/r0_p03_navigation_probe/v03_live_ci_provider_conflict_source_v01.json
**Derived replay result:** experiments/r0_p03_navigation_probe/v03_live_ci_provider_reconciliation_result_v01.json
**Tests:** tests/unit/test_r0_p03_v03_live_ci_provider_reconciliation_v01.py
**Validation:** 380. **Checkpoint:** 944. **Collaboration:** MC-0030 Message 097.

## 1. Actual current provider evidence, not a hypothetical fixture

Checkpoint 943's real published commit is:

    source_commit = 2a7f8fe3f170840262122296d9b7f3e54664bc39
    parent = e29329b3097b593a917a386d33f900a3cf97b193
    repository = shakaarlatief/autonomous-data-science-system
    workflow_run_id = 43633469851
    check_run_id = 132565047313
    specific_check = validate-current-routing (ubuntu-latest)
    provider_app = github-actions, app ID 15368

The connected Codexless GitHub App tools queried the check-run resource, the parent workflow-run resource, the workflow's jobs, all five steps of the specific job and the full eight-check list for the exact source SHA. These were real native provider-source API calls with a server-owned authorized GitHub App user token and fixed endpoint contracts, not URL-selected user-supplied HTTP requests. The authorization metadata reported configured=true, authorized=true, storedAuthorization=true, authMode=github-app-user-token-device-flow. No credential bytes were accessed, transported into the repository or published.

Actual results were:

| Source-owned resource | Relevant returned state |
| --- | --- |
| Specific check run 132565047313 | status=in_progress, conclusion=success, completedAt=2026-11-14T19:41:49Z |
| GitHub Actions job 132565047313 in run 43633469851 | status=in_progress, conclusion=success, completedAt=2026-11-14T19:41:49Z |
| Parent workflow run 43633469851 | status=completed, conclusion=success, runAttempt=1 |
| Five job steps | all status=completed and conclusion=success |
| Exact SHA's eight check runs | seven status=completed/conclusion=success; the above eighth is not reported completed |

The SHA, check ID, suite ID, workflow ID, app identity and corresponding job were internally consistent. The disagreement concerns state completion, not whether the source commit exists. The check's successful conclusion and non-null completion time contradict its nonterminal status. The completed successful parent and successful steps do not make the child check's terminal status true.

Repeated direct reads of the same GitHub App tools yielded the same state after the workflow had already completed. The separately connected GitHub connector's workflow-job and step readers also reported the same job and step states. The evidence does not identify whether this is an upstream GitHub API persistence issue, a data normalization issue shared by the providers or another source/adapter defect. It would be unsound to assign a root cause without a verified raw provider transport capture.

The single associated annotation is an Ubuntu runner-image migration NOTICE, not evidence that the routing test failed. Thus the correct outcome is neither a failed test nor a fully completed eighth check:

    SOURCE_REPORTED_CONTRADICTION
    seven_fully_completed_successful_checks = 7
    failed_completed_checks = 0
    conflicting_check = 132565047313
    qualified_eight_completed_success = NOT_ESTABLISHED

Do not flatten this to PASS by selecting the parent or steps as a more convenient source. Do not flatten it to FAILED merely because the child is inconsistent. Requery, record both source IDs and retain a bounded HOLD.

## 2. What can be authenticated with the current connected capabilities

The Codexless Runtime Bridge Github authorization metadata confirms it has an authorized bounded GitHub App integration; tool read contracts keep credentials and endpoint selection server-owned. In the present interaction, these calls can genuinely observe online GitHub check/run/step resources as platform-origin results. This is materially stronger than trusting a copied JSON field that says provider_authenticated=true.

However, the connected tool outputs are not detached GitHub-signed source receipts and the repository-local Python program cannot call the protected provider interface on its own. The in-repository 5,091-byte JSON relay is explicitly labelled DERIVED_COORDINATOR_RELAY_OF_LIVE_CONNECTED_GITHUB_APP_READS, with source_authentication_from_copied_file=false. Its SHA-256 is:

    1d968a4eb516780c70cfd70ae51a82eadbcad8e92e043b861a2a1f5b0c776bf2

The checked-in source relay is not evidence of which model initiated a write. The authorization's GitHub account is a shared user, not a model-exclusive credential. No verified actor key, device attestation, provider signed operation token or unique source-owner signature was observed. This fact remains separate from the already existing owner-accepted conversational four-effect experiment-only J1 packet and the original Claude Message 091 CANNOT_ATTEST result.

The current tools expose separate bounded read calls, not one sealed server-owned composite assertion that binds source snapshot, check, workflow, jobs, evidence freshness and source-owner identity. Combining source objects in model reasoning or a copied file does not itself establish a new privileged verification service.

## 3. Executed reconciliation contract

The new deterministic Python reference checks original Git commit ancestry, the exact-pinned source relay and its closed source-role schema, and then reconciles the same source episode by ID, exact SHA, suite, GitHub Actions issuer, run attempt, workflow-run parent, individual check, check-list member, job member and each of five steps.

It produces a status on two independent axes:

1. Source report coherence: SOURCE_REPORTED_CONTRADICTION, SOURCE_REPORTED_COMPLETE_SUCCESS, SOURCE_REPORTED_FAILURE, HOLD_INCOMPLETE, HOLD_MISSING or REJECT_WRONG_SHA/REJECT_UNTRUSTED_SOURCE_SHAPE.
2. Governing assurance: always false for independent provider authentication, authenticated model/connector identity, qualified RELATIONAL J2 and governing J3 completion in the current offline reference implementation.

The actual source produces SOURCE_REPORTED_CONTRADICTION, seven completed successful checks, zero completed failures, one conflicting check ID and multiple explicit reason codes including NONTERMINAL_CHECK_WITH_TERMINAL_CONCLUSION and COMPLETED_WORKFLOW_CONFLICTS_WITH_NONTERMINAL_JOB.

The tests include a hypothetical corrected view where all eight check statuses become completed and successful, with all matching jobs and steps. That copy can produce SOURCE_REPORTED_COMPLETE_SUCCESS as **a structurally coherent replay**, but the four governing assurance fields remain false. Changed SHAs, forged issuers, removed checks, incorrect job/run associations, duplicate provider IDs, failure/pending states and false source-owner proof fields fail closed. An unrelated workflow's failure is not incorrectly interpreted as failure of the selected routing workflow.

The source and result JSON artifacts are marked -text in .gitattributes to prevent a second Windows CRLF raw-byte drift failure. They are derived non-authoritative artifacts, not an alternative natural source of GitHub status.

## 4. Architecture finding: source-first reconciliation and a real boundary to cross

There are now two well-demonstrated facts:

**The live provider observation path exists.** The bridge can read bounded GitHub source records through an authenticated app. This can be a viable source-side interface for CI OBSERVABLE or provider execution EPHEMERAL facts when the governing policy accepts such online source reads.

**A transport-authenticated read is not the same as a qualified agent/source-owner claim or a detached verifiable receipt.** A model-authored derived projection, even if exact and comprehensive, cannot re-issue a signed GitHub statement. The GitHub App's user identity cannot prove whether ChatGPT or Claude triggered the operation. The exact original E01 connector transport assertion is a different event and remains unproven by CI.

A meaningful next architecture discriminator is a *provider-owned composite source-read and status-reconciliation capability* behind an existing authenticated Runtime Bridge or provider-native adapter boundary. The provider-side component, not a model-supplied JSON dict, should fetch exact commit, run, check, job, steps and attempt under one declared operation, return source references and explicit conflicts, and bind the result to an authorized project/request context with a recoverability policy. Its contract should expose whether the output is an online authenticated read, a signed portable receipt, or a copied relay. These classes must never be conflated.

A second independent discriminator is **natural-owner identity**. An agent-exclusive action/realizer attribution will require an actual source-side trust root and an authorized relationship to an accepted effect. Possibilities include provider-side operation journaling, scoped action identities, source-owner signatures or explicit owner-governed human principal delegation. We have NOT established that the current model providers expose a stable signed agent-session claim, nor that any of these approaches satisfies the governing threat model.

No specific technology, Git branch policy, storage format, CI scheme or permanent workflow is preselected. The whole architecture and working method remain redesignable with evidence.

## 5. Finite stop, rather than more untrusted fixture elaboration

The last three stages have established that source snapshot parsing is not the missing capability. Further manually copied source dictionaries cannot create a provider-issued signature or authenticate an agent. After the concrete real-source contradiction test, further copies should stop **unless the actual connected provider integration or trust-root availability changes**.

Recommended next work is to evaluate and, if within separately authorized scope, implement a server-owned composite provider read or a genuine natural-owner authentication mechanism. If neither is available, record a finite capability HOLD and return to the higher-value shared real-content R0-P03 architecture and formal-task preparation rather than indefinitely extending evidence simulations. Any owner-exclusive credential, production policy or new experimental J1 acceptance must be separately proposed and explicitly approved.

This is not an R0-P03 B0-B4 score or physical architecture selection. The already accepted four experimental J1 effects remain unchanged. The original E01 J3 remains HOLD, formal R0-P03 remains INCOMPLETE, and Specification 028 and Research 673's scoring/independence controls remain intact.

    RESEARCH=683
    LIVE_PROVIDER_READS=EXECUTED_MULTIPLE_ENDPOINTS
    ORIGINAL_COMMIT=2a7f8fe3f170840262122296d9b7f3e54664bc39
    SOURCE_CHECK=132565047313
    PARENT_WORKFLOW=43633469851
    STATUS_CONTRADICTION=IN_PROGRESS_WITH_SUCCESS_AND_COMPLETION
    CI_COMPLETED_SUCCESS=7_OF_8
    CI_FAILURES=0
    FULL_EIGHT_COMPLETED_CI=NOT_ESTABLISHED
    CONNECTED_GITHUB_APP_AUTHORIZATION=AVAILABLE
    COPY_DETACHED_PROVIDER_AUTHENTICATION=false
    INDEPENDENT_MODEL_SESSION_IDENTITY=false
    PREEXISTING_ACCEPTED_EXPERIMENT_J1=4
    NEW_ACCEPTED_J1=0
    QUALIFIED_RELATIONAL_J2=0
    HISTORICAL_E01_J3=HOLD
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
    NEXT=FINITE_PROVIDER_OWNED_COMPOSITE_SOURCE_AND_SOURCE_OWNER_IDENTITY_FEASIBILITY
