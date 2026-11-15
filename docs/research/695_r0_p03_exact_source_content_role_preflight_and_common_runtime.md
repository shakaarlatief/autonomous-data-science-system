# Research 695: Exact-source content-role preflight and runnable shared B0-B4 common core

**Date:** 2026-11-15
**Status:** 24_EXACT_GIT_CONTENT_CLAIMS_INSPECTED / REAL_SHARED_CORE_API_REPRODUCIBLE / 53_ADVERSARIAL_TESTS_PASS / SEMANTIC_ELIGIBILITY_AND_ARM_PARITY_HOLD
**Scope:** Build the next non-scored R0-P03-V2 source-content eligibility preflight and actual shared-core runtime on the 24-source original-Git pilot established in Research 694, without admitting candidate source role/currentness claims or selecting formal comparison arms or hidden reference material.
**Authority:** Reproducible, coordinator-authored engineering evidence within the owner-accepted R0-P03 experimental method. Governing methodology remains Research 513, Research 559, Research 576 and Research 673; accepted experiment-only semantic authority remains the exact Checkpoint 954 J1/J2/J3 evidence. No independent referee, formal 60/20 sample, scorer, physical target or production switch is established.

## 1. Source-content roles rather than path-based authority

Checkpoint 955 showed 1,586 original-Git Markdown path candidates in the ten-stratum census and 2,897 potentially reviewable textual paths in the broader frame. Those are capacity counts, not source-content eligibility decisions. A sampled path, a matching filename, a document's own Status heading, or an implementation symbol cannot automatically be a current accepted governing fact.

The new content inspector opens each of the **same 24 source records** at immutable original ADS Git:

    17ea403ef64092f275e3c7d6492d99929804f8e5

The inspector validates the original Git blob OID, byte SHA-256 and line witnesses supplied by the prior seed. It then derives **content-visible, recoverable evidence**, without using the seed's role label as a semantic oracle. Its inspected types:

| Format | Sources | What is actually evidenced |
| --- | ---: | --- |
| Markdown | 11 | Exact heading; source-authored Status/Authority/Scope and related header witnesses; for `DECISIONS.md`, each decision's own header and reported status |
| Python | 9 | Python AST parses, module docstring presence and actual top-level function/class declarations |
| TypeScript / TSX | 2 | Source-visible exported declarations from two ADS frontend components |
| JSON Schema | 1 | Parseable declared schema dialect, title and property keys |
| CI workflow YAML | 1 | Workflow name, trigger and jobs definition fields, not a CI execution result |

This is a genuine content inspection, but deliberately **not** independent factual adjudication of 24 sources as formal gold or as currently governing. Every record remains `semantic_eligibility=NOT_ADJUDICATED`, `accepted_authority=NOT_INFERRED_FROM_SOURCE_CONTENT_OR_ROLE` and `formal_cohort_membership=NOT_SELECTED`.

## 2. Substantive mixed-currentness and nonauthority observations

The exact `docs/DECISIONS.md` Git blob contains **36 decision entries** with **11 distinct raw Status strings**. It must be interpreted by individually scoped decision/status evidence; a whole-file `ACCEPTED` label would lose the distinction between superseded, accepted and differently scoped decisions.

The original Research 217 file itself states both `T1 ACCEPTED` and `Authority: W5 design result only`. Research 254 explicitly records an architecture supersession proposal requiring an owner decision, with no physical migration. The Architecture Program Overview declares itself `NON-AUTHORITATIVE / NON-GOVERNING`. Specification 028 explicitly states its frozen implementation contract does not switch operational authority. These are **source-authored textual claims at exact Git lines**, not new evidence of owner signature or a current V03 J1 admission. The later accepted owner policy and separately qualified experiment-only S1 remain the proper bounded authority for the navigation experiment.

The content of G006/G007/G009/G013 modules, the Product source services, frontend components, schema, test files and integrity workflow is demonstrably defined in source, but a parsed function, exported UI component, validator source or GitHub workflow is **not proof** that it ran, passed, naturally owns a J2 relation or satisfies production J3.

This resolves a concrete preparation risk: the cohort reviewer cannot infer authority from an entire information family. The next independent source referee must adjudicate semantic eligibility, effective status, provenance, cross-plane closure, privacy/exposure, contradictions and coverage before selecting any formal build/held-out set. The exposed ChatGPT coordinator that wrote this inspector is **not** that independent referee.

## 3. Executable shared-core access, not just an interface diagram

A second new module implements a real, bounded **common source interface**:

    experiments/r0_p03_navigation_probe/v03_r0_p03_shared_core_runtime_v01.py

For each of the five B0-B4 labels, its `SharedCoreRuntime` uses the same exact original-Git source roster, source-content observations and experiment-only J1/J2/J3 facts. The runtime exposes:

- `read_source(path,start,end)`: exact Git blob, source SHA-256, source line text and per-line SHA-256 with a 40-line budget, refusing unlisted paths.
- `literal_search(query,limit)`: casefold literal search over exactly the 24 pilot source bytes, fixed maximum 20 returned source-located hits; no semantic result ranking or authority inference.
- `source_role_observation(path)`: a defensive copy of source-content witnesses, with the still-unadjudicated status explicit.
- `experimental_semantics()`: the **same qualified experiment-only**, weak-assurance accepted J1/J2/J3 facts for all labels, never production J2/J3.
- `derived_orientation()` and `drop_derived()`: a transient, explicitly non-governing in-memory orientation view, with source-relative reconstruction after cache drop. This is **not** general production generated-index deletion qualification.

All returned structures are defensive copies. The source read API does not traverse arbitrary repository paths, leak hidden gold, or expose task answers. The core is one shared implementation called by five arm-labelled facades. It neither implements B1 controlled facets, B2 about-links, B3 concern memberships nor B4 embeddings, nor exposes a winning comparator.

The fixed synthetic **engineering-only** request trace for each arm included two exact source excerpts, a role observation, literal search, qualified experimental semantics, derived orientation, cache drop and rebuild. Results were byte-identical across all five labels, and method call counts were the same.

    prior common-interface SHA-256
      33d3ab8fef047f55313ebdab0fb097389859953b8fed0eee5027e288e4e51bdb
    shared executable common-API observation SHA-256
      5d2fe1ff0300b53b1f7daee9b9cabbc2cbc233a743f1ea4fd4481153277399a5
    all five arm-labelled common API results
      IDENTICAL
    all five arm-labelled common API call counts
      IDENTICAL

**This proves repeatable shared runtime behavior for the 24-file prototype, not actual fairness/quality of separate B0-B4 arm implementations, indexing budgets, authoring cost, full source closure, future provenance APIs or held-out maintenance.** The synthetic API calls are not the twelve primary information needs or nine historical reference cases.

## 4. Published artifacts, exact hashes and adversarial checks

The two non-scoring create-only receipts are:

    experiments/r0_p03_navigation_probe/v03_r0_p03_source_content_role_preflight_result_v01.json
    SHA-256 d1da9fb5a8dfe4f75d81a22eed1fb1725a737ac66bc49591c416c2631aa7d63b

    experiments/r0_p03_navigation_probe/v03_r0_p03_shared_core_runtime_result_v01.json
    SHA-256 06b6042dd6228a83a8df9e41e4994867ae20afb42cb54e6f79a39d987f975ce2

Execution:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_r0_p03_source_content_role_preflight_v01
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_r0_p03_shared_core_runtime_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=2 -p no:cacheprovider tests/unit/test_r0_p03_v03_source_content_and_shared_runtime_v01.py
```

**53 focused adversarial tests PASS**. They check all 24 exact source-content witnesses, mixed decision-status reporting, specific historical/operational source limitations, Python/TypeScript/schema/workflow definitions, no J2/CI/test execution inferred from code presence, invalid source hash/syntax rejection, working five-label common API parity, strict line/query/tool budgets, forbidden paths, defensive returned copies, derived cache reconstruction and immutable receipt reproduction.

The previous 38-source pilot tests and 77 separate experimental J3 tests must be rerun as additional regressions; these 53 tests alone are not whole-repository qualification. A GitHub green workflow establishes only checks it actually runs.

## 5. Next controls and scientific boundary

The **source-content observational gate** has advanced. The **formal independent source-semantic eligibility gate has not**. No chosen 60/20 build/held-out set, eligible 80-carrier closure, 3:1 fallback, hidden source membership, independent gold, primary task packet, neutral Research 559 legacy packet, arm-specific B1-B4 implementation or scored response exists.

Before formal arm freeze, separately qualify the source-referee role, a source-content eligibility rubric including contradiction/currentness/authority and full evidence closure, prospective custodian of source split and gold exclusion, and all-arm common connector/runtime equality. Keep source-world exposure boundaries and the 65-source historical packet separate. The next step should apply a content/authority review contract to an independently controlled representative frame, not turn these 24 convenient coordinator-authored witnesses into presumed formal sample members.

Physical architecture, branch strategy, file layout, CI, collaboration and implementation workflow remain fully revisable when evidence justifies changes. Nothing here selects a new physical target, changes Specification 028's operational standing or authorizes migration.

    RESEARCH=695
    VALIDATION=392
    CHECKPOINT=956
    MC0030_MESSAGE=109
    CONTENT_SOURCE_WITNESSES=24
    CONTENT_SEMANTIC_ELIGIBILITY_ADJUDICATED=0
    COMMON_API_EXECUTABLE=YES_UNSCORED_PILOT
    COMMON_API_PARITY=FIVE_LABELS_IDENTICAL
    ARM_SPECIFIC_RUNTIME_PARITY=NOT_QUALIFIED
    J1_J2_J3=EXPERIMENT_ONLY_WEAK_ASSURANCE
    FORMAL_60_20=NOT_SELECTED
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
    NEXT=INDEPENDENT_SOURCE_CONTENT_ELIGIBILITY_AND_FULL_SHARED_CONNECTOR_CLOSURE
