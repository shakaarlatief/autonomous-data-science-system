# Independent-reference readiness: objective Git-event witness capacity V01

**Date:** 2026-11-13
**Status:** BEFORE_OUTPUT_METHOD_FREEZE / REAL_SOURCE_ONLY / NO_QUESTION_OR_GOLD_DISCLOSURE
**Purpose:** Examine what independently reproducible historical Git evidence actually establishes about source/change occurrence, versus unsupported claims of accepted authority, test execution and deployment. This is an **evidence-availability and proof-boundary audit**, not a substitute for protected C02 reference adjudication, B0–B4 scoring, independent question origination or another corpus of conveniently answerable tasks.

## Frozen scope

Anchor to the previously authorized prospective C02 **upper evidence horizon** `47ed6344a9153dcf366769e95722840fbf1a8f8b`, but DO NOT treat the pin as a scored corpus admission, owner evidence acceptance or permission to look at C02 private task/source mappings.

Read only *public repository* Git **commit metadata, tree membership and changed-file pathnames** through `git log`, `rev-list`, `cat-file` and `diff-tree` from that exact pin. Do NOT read changed source contents, unpublished/private reports, C01/C02 restricted task text, reference gold, answer keys, private owner credentials or output of any scored arm. Do NOT infer historical execution from commit messages or status labels.

Define the population as all reachable non-merge original commits at the pin. Root commits are included. Ignore empty diff commits with no changed paths. On each commit, the source category is assigned exclusively using pathnames, in this order:

1. `WORKFLOW_CHANGE`: any changed path starts `.github/workflows/`.
2. `TEST_CHANGE`: any changed path starts `tests/` or its filename starts `test_` or ends `_test.py`.
3. `IMPLEMENTATION_CHANGE`: at least one path starts `src/`, `tools/`, `scripts/`, `frontend/`, `backend/`, `app/`, or has extension `.py`, `.js`, `.ts`, `.tsx`.
4. `DOCUMENTATION_ONLY`: every changed path is under `docs/` and is a Markdown/text/JSON/YAML document. Does not claim the underlying text was correct or accepted.

All other commits have class `OTHER_OR_UNCLASSIFIED`, remain in the full counted denominator, but are not drawn. A `WORKFLOW_CHANGE` label means **workflow definition modified**, not that any workflow executed. `TEST_CHANGE` does not establish test pass. `IMPLEMENTATION_CHANGE` means a code-path change landed in Git, not a successful runtime or deployment.

Freeze deterministic case selection before inspecting specific sampled identities:
- For each of the four classes, sort matching commits by SHA-256 of exact string `R0-SOURCE-EVENT-WITNESS-V01|<class>|<40-char-commit-sha>` and then commit SHA to break ties.
- Select first **four** per class if available. If fewer than four, record actual shortfall, do not substitute other classes.
- Do not sample, drop or replace cases based on changed-file descriptions, commit age, source ability, workflow outcomes or later model assessments.
- Source event records contain exactly sampled commit hash, parent hashes, ISO Git-authored and committed time (metadata only), complete changed path list, claimed path-derived class, exact `git diff-tree` original result SHA-256 and change flags. No commit message or file contents.

## Independent audit checks and scientific output

A second audit recomputes the selected roster against the full Git log and independent `git diff-tree --no-commit-id --name-only -r --root` for all sampled commits, verifies each SHA as a Git commit and its existence in the pinned original history, validates the exhaustive stratum counts and checks that exactly the fixed SHA-selected items were retained.

Evidence ladder must distinguish:
- `GIT_COMMIT_AND_PATH_MEMBERSHIP_VERIFIED`: direct reproducible original Git historical occurrence and changed file paths.
- `CONTENT_OR_SEMANTICS_UNINSPECTED`: unchanged by this pilot.
- `TEST_EXECUTION_PROVEN=false` from a Git path alone, even if `tests/` or `.github/workflows/` is changed.
- `CURRENT_OPERATIVE_AUTHORITY_PROVEN=false` from a Git path alone.
- `EXTERNAL_CI/RELEASE_RECEIPTS=NOT_ASSESSED` until independently inspected and bound to exact commit/attempt. The absence of a first-page PR workflow result is not evidence of no push run, no local testing or no execution.

Store *all sampled events* and the full stratum population counts, exact method identifiers and source-bound negative semantics in one exclusive-create deterministic JSON under `experiments/r0_p03_navigation_probe`. The method and source archive are non-blind and reused for mechanism qualification; never turn sampled cases into scored questions or select easy ones to satisfy Research 513 gates. No full-content read or score is authorized. Publish an engineering finding only, with direct original Git check receipts and neutral cost.

The old owner-controlled C02 case file remains private and does not enter this experiment; original C02 reports **8 distinct / 2 duplicate / 2 uncertain, 0 complete closures among 10 nonduplicates**. The original Research 641 requires a separately explicit owner-scoped choice before a new primary protocol, supplemental authoring, full source admission or B0–B4 scores. A user request to continue engineering is not silently a replacement-protocol acceptance.

    SOURCE_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    POPULATION=ALL_REACHABLE_NONMERGE_COMMITS_AT_PIN
    SAMPLING_CLASSES=WORKFLOW_CHANGE,TEST_CHANGE,IMPLEMENTATION_CHANGE,DOCUMENTATION_ONLY
    N_PER_CLASS=4_IF_AVAILABLE
    SOURCE_FILE_CONTENT_READ=false
    PRIVATE_CASE_ACCESS=false
    LIVE_CI_OR_DEPLOYMENT_ASSERTION=false
    INDEPENDENT_QUESTION_AUTHOR=false
    SCORING=NONE
    ORIGINAL_R0_P03_OUTCOME=INCOMPLETE
    OUTPUT=EXCLUSIVE_CREATE
