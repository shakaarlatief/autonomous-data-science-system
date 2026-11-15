# Validation 392: Exact-Git content-role witnesses and shared-core runtime parity

**Date:** 2026-11-15
**Status:** 24_SOURCE_CONTENT_INSPECTIONS_PASS / FIVE_SHARED_CORE_RUNTIME_LABELS_EQUAL / 53_FOCUSED_TESTS_PASS / SEMANTIC_ELIGIBILITY_AND_FORMAL_R0_P03_HOLD
**Research:** 695. **Checkpoint:** 956. **MC-0030:** Message 109.
**Scope:** Reproduce immutable source-content role evidence and the bounded source-read/search/semantic/orientation common API from a 24-source original-Git pilot.
**Authority:** Unscored engineering validation only; no formal 60/20, independent referee, separate navigation arm qualification, selected physical architecture or new production J1/J2/J3.

Exact source revision is Checkpoint 954 Git `17ea403ef64092f275e3c7d6492d99929804f8e5`. The frozen coordinator seed remains SHA-256 `d10d1f4a5f50f082b73689f4858b2a4f003746969fb098add7e8fa9bedb7a6b4`.

Content preflight: **24 original-Git source blobs and line witnesses** inspected. Observed modalities: 11 Markdown, 9 Python, 2 TSX, 1 JSON Schema and 1 GitHub workflow YAML. `docs/DECISIONS.md` has 36 decision entries with 11 distinct authored status strings, so no whole-file status can be promoted. Research 217's W5-only authority and Research 254's owner-decision-required proposal were explicitly source-verified. Code, schema, test and workflow source only establish what is authored, not that execution/J2/CI succeeded. Zero formal semantic eligibility or owner/currentness adjudications were undertaken.

Common runtime: five facades call an identical real Git source API with strict read/search budgets, original source/line digests, content-source role observations, qualified experimental weak-assurance S1 J1/J2/J3 facts and a disposable **process-local** derived orientation. All five synthetic engineering API observation payload hashes equal `5d2fe1ff0300b53b1f7daee9b9cabbc2cbc233a743f1ea4fd4481153277399a5`, and observed method call counts are identical. This is **not** actual distinct B0–B4 runtime parity or generated-index deletion of the future system.

Create-only receipts:

    source content SHA-256 d1da9fb5a8dfe4f75d81a22eed1fb1725a737ac66bc49591c416c2631aa7d63b
    shared core SHA-256 06b6042dd6228a83a8df9e41e4994867ae20afb42cb54e6f79a39d987f975ce2

Reproduce:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_r0_p03_source_content_role_preflight_v01
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_r0_p03_shared_core_runtime_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=2 -p no:cacheprovider tests/unit/test_r0_p03_v03_source_content_and_shared_runtime_v01.py
```

Observed **53 passed in 27.25 s**. Tests include artificial tampering/false status, source not admitted as authority, hard-scoped Git reads, per-line source evidence, independent of returned mutable copies, exact API equality and limited cache-drop reconstruction. Tests do not independently assign gold or qualify semantic eligibility.

Repository integrity, prior J3/source pilot regressions, publication, local/remote branch status and GitHub CI need separate verification on the final commit.
