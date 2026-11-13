# V03: Existing governed reference grammars and historical source-owned evidence audit

**Date:** 2026-11-13
**Status:** EXPLORATORY_POST_REVIEW_DESCRIPTIVE / METHOD_FIXED_BEFORE_SAVED_V03_OUTPUT / NO_INDEPENDENT_GOLD
**Review context:** MC-0030 Message 064, exposed Claude critic. Source-specific counts and counterexamples have already been discussed by Claude and ChatGPT; **this is not blind preregistration**.
**Scope:** Correct the V01/V02 path-only blind spot using the repository's own parser implementations. Preserve the source-owned slot and fragment identity, the open-world boundary, and exact original witness evidence.

## Fixed corpus and inputs

Use the exact same 65 historical Git source originals at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, source-byte fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`. Verify published V01 original-path audit 177638-byte SHA-256 `e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299` and V02 corrected-path audit 175032-byte SHA-256 `25b26e66e3bb03232d4ee7931e66aceb6bd6eaf28d2f5ae0ff207713c333831d`. Never alter them or Checkpoints 905-911.

This 65-source corpus is now **only an exposed regression/audit set**, not a fresh navigation benchmark. No source selection, new model scores, B0-B4 winner, independent author/evaluator or physical architecture target is authorized.

## Mandatory existing parser reuse

1. For **Specification 025 header declarations**, import `scripts.repository_integrity.read_header_fields` and `parse_declared_reference_field`; supply each exact historical Git byte sequence in an isolated temporary file to the actual header parser. Do not parse arbitrary Markdown body text into header fields. Preserve the source-authored token and declaring source header line. Keep the parser's first-100-lines and pre-first-H2 bounds. Verify token locations in exact original lines.
2. For **Specification 028 structured declarations**, import `tools.project_knowledge.declaration.parse_markdown` and supply exact Git bytes directly. Preserve individual `references`, `provenance` and `relations` slots separately. Do not treat profile/authority_class as a verified governing assertion merely because parsing succeeds; cross-source schema/semantic/currentness validation is an additional requirement. Require identifiable marker lines and source witnesses.
3. Index in-corpus numbered document identities mechanically using `scripts.repository_integrity.FAMILY_CONTRACTS` and exact numbered filename conventions; resolve `research:N`, `specification:N`, `foundation:N`, `checkpoint:N` within the 65-source frame. A well-formed identifier missing from the sample is `OUTSIDE_SAMPLED_65`, **not a nonexistent artifact**. Resolve `path:` to exact sampled carriers when present. Do not infer paths from prose-only topic similarity. Retain each `#fragment` separately from its carrier and do not automatically equate a fragment to an accepted decision or operative authority. Preserve exact original token when unresolved.
4. Preserve `RELATIONSHIP_FIELDS` header claims as a distinct diagnostics channel where recognized by the existing validator, **not** merge them into generic declared-reference edges or silently promote their truth. A separate `Governing decision` prose header may be informative but is not automatically covered by that validator.
5. Compare only the mechanically parsed source-owned cross-file pair set against the old **110** path-literal pairs. Report in-corpus declared references by slot, union pairs, overlap and omissions; retain **out-of-sampled-frame** tokens separately. Compute old 130-query structurally empty cases that have a source-owned typed reference to sampled members, but label this as **coverage difference**, not a retrospective scoring failure on explicitly path-worded queries.
6. Output every original source-owned token occurrence with source path, Git source SHA-256, SHA-1, line number and exact line text, slot, raw token, typed target member if present, fragment and resolution state. Do not mutate external files or require executing real source migrations.

## Already exposed preflight and expected challenges

Claude's non-committed exploratory script claimed **29** source-owned in-corpus pairs, **10** absent from 110. ChatGPT independently used `read_header_fields`, `parse_declared_reference_field` and `parse_markdown` on pinned original Git objects and observed **31** unique pairs, **12** absent from the old path-only graph, including parsed `specification:028` references from `docs/DECISIONS.md` and `docs/project_knowledge/selected_architecture_workstream.md`. This difference **must not be silently resolved by changing the cohort**. The V03 full trace and deterministic tests shall explain the raw slot/token differences, and preserve Claude's 29/10 as separate provisional review claims.

The two original parsers validate grammar and extraction only. Parsed `authority_class: canonical` is an authored statement whose live governance/currentness still requires qualified validation. Typed header dependencies are not automatically real J2 effects or B2 editorial links.

## Regression and experimental boundaries

Assert no source-byte changes, no V01/V02 result changes, no duplicate token expansion, no collapse of provenance into references, no loss of `DECISIONS.md#D-035` or `OPEN_ARCHITECTURE_BACKLOG.md#AB-032` fragments, and a negative case where a `Declared references` string appears in ordinary body/fence but not in the governed header.

Provide two-channel answer **design guidance only**: an assertion channel with `ASSERTED_SOURCE_DECLARATION` / `NOT_FOUND_IN_COVERED_SCOPE` / `UNSUPPORTED_SCOPE` plus exact typed witnesses and coverage, and separately ranked candidate documents. Do not report a closed-world absence or merge lexical candidate results into asserted edges. No scoring on newly exposed 65 variants.

Use a single exclusive-create deterministic V03 JSON trace and tests that rerun full extraction from the original Git bytes. Preserve outputs under `.gitattributes -text`.

    SOURCE_WORLD=PINNED_65_EXPOSED_REGRESSION_ONLY
    REFERENCE_PARSERS=EXISTING_SPEC025_AND_SPEC028
    AUTHORITY_ADMISSION=NONE
    USER_GOLD=NONE
    PHYSICAL_ARCHITECTURE_SELECTION=NONE
    FORMAL_R0_P03_SCORING=NONE
