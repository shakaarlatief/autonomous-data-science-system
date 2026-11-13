# Research 654: Objective original-Git event witnesses and externally reported CI execution evidence

**Date:** 2026-11-13
**Status:** ACTUAL_ORIGINAL_GIT_3230_COMMIT_CENSUS_AND_16_CASE_SOURCE_SAMPLE / EXTERNAL_ACTIONS_27_RUNS_RECORDED / NO_C02_REFERENCE_CLOSURE
**Scope:** Address the source-evidence limitation revealed by independently originated C02 questions, without reading protected case text or inventing another self-authored scored query set. Distinguish recorded source changes from independently reported workflow execution, job-level partial failure, evidence publication and genuinely operative authority.
**Authority:** Frozen pre-source-result Git sample rule, exact historical Git pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`, actual Git original tree and diff metadata, fixed 16 sampled commits, real read-only GitHub Actions provider-run/job/step observations, three exact immutable JSON receipts, Validation 353, Checkpoint 917.
**Science boundary:** Source-independent mechanism/evidence feasibility only; **no new private reference admission or formal R0-P03 score**. Earlier Research 513/559/576 and Research 637–641 retain their owner authority.

## 1. Why the independently originated question route is not ready for scoring

The experiment already contains a **genuinely separate authoring attempt**, prospective C02. Research 638 establishes twelve independently originated candidate information needs, retained outside exposed public coordination. Research 639/641 establish **eight distinct, two substantive duplicates and two equivalence-uncertain** candidates, with **zero complete as-stated source/answer closures among ten non-excluded candidates**, even after the original-source review. The protected reviewer reported checking the exact bytes of 37 original source files but did not independently establish those files' Git historical tree membership. Neither the coordinating session nor this audit accesses the protected original questions, question-to-source mappings or source-specific reviewer ledger.

The problem is not simply that the coordinating model keeps writing insufficiently paraphrased questions. The actual independently originated questions already exist. They are not yet answerable at full historical/operative scope under a valid independently qualified reference world. Research 641 therefore explicitly requires an owner-scoped prospective method choice before supplemental authoring, new source admissions, a replacement cohort or scoring. A generic "proceed" with engineering is **not** silently a protocol replacement decision.

This checkpoint advances a **source-independent capability** instead: exact reproducible original Git change occurrence, plus separately attributable provider-reported CI runs, jobs and specific step conclusions. This demonstrates what a partial source-evidence ladder can establish, and which claims remain outside its authority.

## 2. Fixed original Git source frame and deterministic sample

The V01 contract was written before seeing its sampled Git-event output. At the C02 *upper evidence horizon* `47ed6344a9153dcf366769e95722840fbf1a8f8b`, the actual reachable non-merge commit population is **3,230**. Changed file path names only, not source contents or commit-message semantics, define four mutually exclusive strata in priority order. A fifth category retains nonmatching events in the total denominator:

| Mutually exclusive changed-path stratum | Actual original Git commits | Frozen sample |
| --- | ---: | ---: |
| Workflow definition change | **117** | **4** |
| Test-related change | **203** | **4** |
| Implementation/code-related change | **615** | **4** |
| Documentation-only change | **2,047** | **4** |
| Other / not classified | **248** | **0** |
| **Total** | **3,230** | **16** |

The four per stratum were selected by SHA-256 of a frozen seed + class + 40-character commit ID, before any provider workflow check. Selection is a **deterministic stratified probe**, not a probability-representative sample. Every selected Git commit is verified as a real Git object, ancestor of the exact historical pin, with original `git diff-tree --no-commit-id --name-only -r --root` changed-file path list exactly agreeing with the separate `git log` pass. Original stdout SHA-256, complete changed paths, author/committer Git timestamp metadata and parents are preserved in the first immutable JSON.

**Direct original-Git fact:** a commit/tree/path change occurred. **Not implied:** a changed test passed, a new workflow ran, a particular operational effect was accepted, the version was deployed, an independent source witness authenticated the source content, or the information is currently governing. Git timestamps are source metadata, not independently witnessed wall-clock times.

## 3. Real provider execution evidence beyond Git commits

A first limited PR-only association lookup returned no runs for some sampled commits. It proved nothing about push-triggered workflows. A corrected all-event GitHub Actions query, `GET /repos/shakaarlatief/autonomous-data-science-system/actions/runs?head_sha=<sha>&per_page=100`, was subsequently run for **all sixteen original frozen sampled SHAs**, without changing the sample. The API scope correction is recorded as an exploratory, after-initial-observation change. Every returned run head SHA was checked against the originally chosen commit; complete single-page responses were obtained for these bounded lookups.

Actual externally reported result:

| Exact scoped provider observation | Count |
| --- | ---: |
| Fixed sampled Git commits queried | **16** |
| Commits with one or more Actions runs matching their exact head SHA | **9** |
| Commits with no runs returned by this particular query | **7** |
| Matching provider-reported workflow runs | **27** |
| Completed successful workflow-run conclusions | **25** |
| Completed failed workflow-run conclusions | **2** |

The seven zero-result queries are **NOT_MATCHED_IN_THIS_API_QUERY**, not evidence that no tests, builds or other executions occurred. A provider-reported run is stronger evidence of a CI event than a changed `tests/` or `.github/workflows/` file, but it does not verify the semantic correctness of a test, exact saved artifacts, deployment or an owner-accepted governing effect.

An intentionally **purposive after-observation** job-detail inspection examined three workflow runs, two failed and one successful. It found **15 jobs, 13 success and 2 failure**. The purpose is to expose the layers of evidence, not estimate a population job failure rate.

### Decisive actual examples

The sampled original Git commit `842676c04ce6d0305365de60bddec876a530e185` has four matching provider runs, **three successes and one failure**. The failing run is <https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/32356647189>. Its six `interchange-contract` platform/Python-version test jobs all reported **success**, while the seventh job `persist-result` reported **failure**. The actual provider step `Persist successful interchange evidence` failed. This demonstrates that **tests passed**, **the overall workflow passed**, and **evidence was persisted** must be separate facts.

For another sampled original commit, the database diagnosis run <https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/32359491623> reported **failure**, and its step `Run and persist PostgreSQL diagnostic` failed. The record alone cannot establish whether the underlying database condition, artifact publication, or environmental permission caused the failure without further job logs, and no such diagnosis is claimed.

The successful cross-platform run <https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/32356647199> reported seven successful jobs, including `persist-reproducibility-evidence`; the step `Persist successful evidence and lockfile` was also reported successful. This is a source-backed **CI-step conclusion**, but **not** byte-level verification of the resulting saved artifact or a statement about operative production acceptance.

The three job-detail cases were selected **after** the initial run conclusions were seen. They are not a blinded or random comparison. A distinct supplementary immutable 6,624-byte step-level receipt preserves exact provider metadata and its purposive selection declaration.

## 4. Five-level evidence distinction

1. **Source carrier/provenance:** SHA-addressed original Git commit exists, is historically reachable and modifies recorded paths. Independently replayable against that historical repository.
2. **Claim/document semantics:** requires reading exact original source contents, lifecycle/identity and semantic effect. This audit deliberately does **not** access or adjudicate those bodies.
3. **External execution:** GitHub Actions reports a specific run and job/step outcome tied to the exact historical commit. Successful execution is **scoped to named workflow/test jobs**, not all tests or a release.
4. **Persisted evidence/realization:** requires verifying the actual artifact bytes/receipt and linking them to the specific attempted run, target effect and state change. A success label on a persistence step alone does not provide that proof.
5. **Current operative governing authority:** additionally requires authentic owner-governing acceptance, bounded effective time/scope, applicable realization/activation and currentness/rollback evidence. Git history plus CI event metadata is **insufficient**.

This stratification is not a new source-authoring ontology or a scored B2 edge design. It distinguishes observable facts from gaps and makes future source/answer closure demands testable.

## 5. Original scientific implication and stop boundary

A **source-specific original evidence** study for the protected C02 questions might need Git tree membership, a precise CI job/step or artifact receipt, owner authorization, an effective-time transition or an operational validation. This public audit cannot tell which specific protected cases need which evidence, and does not repair any C02 full-scope source closure. Independent C02 adjudication still holds at **0 complete**, two duplicates retained, two uncertain equivalences retained. The three historical failure classes and their older source evidence are unchanged.

The useful next step for formal R0-P03 is an **explicit owner-scoped Route B prospective redesign** (or Route A targeted evidence recovery if justified by protected reviewer needs): a representative and independently answerable task/source frame, challenge categories retained, missing-evidence HOLDs preserved, fresh author/reviewer role separation, and arm-neutral B0–B4 evaluation with a real embedding option if fair and feasible. The source-first evidence layers in this audit may inform that future protocol, but are **not sufficient to silently authorize it**. A provider-neutral model collaborator may still help design/falsify a protocol without becoming scored gold.

**This audit ends a bounded original-evidence availability question**: we can prove original Git change occurrence for the sample and provider-reported CI results for the matching subset, while falsifying the invalid shortcuts Git-commit = execution, tests green = full workflow green, and workflow green = durable effect. Do not keep creating variations on exposed self-authored questions to substitute for full-scoped independently qualified source/answer evidence.

    PRIMARY_SOURCE_CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_R0_SOURCE_EVENT_WITNESS_CAPACITY_CONTRACT_V01.md
    PRIMARY_RUNNER=experiments/r0_p03_navigation_probe/exploratory_r0_source_event_witness_capacity_v01.py
    PRIMARY_RESULT=experiments/r0_p03_navigation_probe/exploratory_r0_source_event_witness_capacity_result_v01.json
    PRIMARY_RESULT_BYTES=27509
    PRIMARY_RESULT_SHA256=2c50e692a63f8542307fd325f987fc792a7a7cd9698f5c68885b01e120d11900
    EXTERNAL_CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_R0_SOURCE_EVENT_EXTERNAL_CI_WITNESS_CONTRACT_V01.md
    EXTERNAL_RESULT=experiments/r0_p03_navigation_probe/exploratory_r0_source_event_external_ci_witness_result_v01.json
    EXTERNAL_RESULT_BYTES=30236
    EXTERNAL_RESULT_SHA256=a320ddea0a0905805dc2550661c54b17e9c1c08dc30288a1f584be54921aa65a
    STEP_RESULT=experiments/r0_p03_navigation_probe/exploratory_r0_source_event_external_ci_step_witness_v01.json
    STEP_RESULT_BYTES=6624
    STEP_RESULT_SHA256=654771d41ab68adecb4ec28f787579c9b7cd4a88aa0162d8573e9fc1dc14775d
    SELECTED_COMMITS=16
    REPORTED_MATCHING_ACTIONS=27
    CI_RUN_SUCCESS=25
    CI_RUN_FAILURE=2
    INDEPENDENT_C02_CASE_CLOSURES=0
    PRIVATE_REFERENCE_ACCESS=NONE
    SCORING=NONE
