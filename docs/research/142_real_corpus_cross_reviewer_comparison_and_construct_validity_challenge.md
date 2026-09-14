# Research 142: Real-Corpus Cross-Reviewer Comparison and Construct-Validity Challenge

**Date:** 2026-09-14
**Status:** TWO INDEPENDENT JUDGMENT SETS FROZEN / 12 OF 15 LABEL AGREEMENT / THREE MATERIAL DISAGREEMENTS / TAXONOMY CONSTRUCT VALIDITY OPEN / COMPARATIVE CLAUDE TURN REQUIRED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Validate Claude's independent MC-0015 judgment, normalize the second reviewer result, compare it mechanically with ChatGPT's already-frozen labels, analyze the three disagreements at case and construct level, and determine whether the admission taxonomy is stable enough for later mechanization.
**Authority:** Supporting Research 124 architecture evidence only. Requirements V0.2 remain frozen candidate-acceptance authority. Reviewer labels are evidence, not ground truth.
**Declared references:** `research:124`, `research:139`, `research:140`, `research:141`, `path:docs/model_collaboration/threads/MC-0015/messages/001_claude_independent_real_corpus_judgment.md`, `path:docs/model_collaboration/threads/MC-0015/messages/002_chatgpt_cross_reviewer_comparison_and_construct_validity_handoff.md`, `path:docs/research/project_knowledge_real_corpus_v01/CHATGPT_JUDGMENTS_V01.json`, `path:docs/research/project_knowledge_real_corpus_v01/CLAUDE_JUDGMENTS_V01.json`, `path:docs/research/project_knowledge_real_corpus_v01/CHATGPT_CLAUDE_COMPARISON_V01.json`, `checkpoint:486`

## 1. Independent-review integrity

Claude Message 001 reports that current-branch reads were restricted to the five authorized MC-0015 routing surfaces and all substantive reads were pinned to the exact corpus-freeze base `ae87c1facbf7c7d7508414e86a935bc439404c24`. The incoming repository change contains only the authorized Claude message. No repository evidence indicates exposure to ChatGPT's descendant judgment artifact before Claude's set was frozen.

The independent reviewer-label pass is therefore accepted.

A separate source-grounding issue exists for RC-012 and is treated as a protocol-fidelity problem rather than contamination.

The normalized Claude judgment artifact is:

```text
docs/research/project_knowledge_real_corpus_v01/CLAUDE_JUDGMENTS_V01.json
SHA-256: 681910e326dabb8bcfb81b887f2d91bb20a612964e25da90f5b2f4b0df09a09a
```

The mechanical comparison artifact is:

```text
docs/research/project_knowledge_real_corpus_v01/CHATGPT_CLAUDE_COMPARISON_V01.json
SHA-256: fb73a1cd3eb3a0322f2c9f951a36001926c8518a87e23cb495d99a4244fc5554
```

## 2. Reviewer marginals

```text
                           ChatGPT    Claude
SOURCE_LOCAL                  10        12
FIRST_CLASS_SEMANTIC_OBJECT    2         0
DERIVED_ONLY                   2         3
UNRESOLVED                     1         0
```

Confidence marginals:

```text
                           ChatGPT    Claude
HIGH                          12        10
MEDIUM                         3         5
LOW                            0         0
```

## 3. Agreement result

Exact primary-label agreement is:

```text
12 / 15 = 0.80
```

Descriptive Cohen's kappa is:

```text
0.5454545455
```

The expected agreement under the observed marginals is `0.56`. Kappa is recorded only as a descriptive statistic because the sample is small and strongly class-imbalanced. The case-level disagreements carry more architectural information than the scalar.

## 4. Twelve independent agreements

The reviewers independently agree that the following real ADS patterns can remain source-local or derived without a separately authoritative semantic object:

```text
RC-001  scoped supersession                    SOURCE_LOCAL
RC-002  multi-successor scoped supersession    SOURCE_LOCAL
RC-003  same-branch CI obsolescence            DERIVED_ONLY
RC-004  checkpoint governance                  SOURCE_LOCAL
RC-007  process reopen triggers                SOURCE_LOCAL
RC-008  review-base / exposure bookkeeping     SOURCE_LOCAL
RC-009  evidence provenance                    SOURCE_LOCAL
RC-010  subject-to-artifact navigation         DERIVED_ONLY
RC-011  public/private authority rule          SOURCE_LOCAL
RC-013  collaboration write/actor state        SOURCE_LOCAL
RC-014  review branch/base binding              SOURCE_LOCAL
RC-015  architecture-transition policy         SOURCE_LOCAL
```

This is meaningful support for **source-local-by-default plus derived views where the relationship is computable/navigation-only**. It also shows that cross-objectness, multiplicity of participants and governance significance do not by themselves justify reification.

## 5. Disagreement RC-005: first-class workstream versus source-local workstream document

```text
ChatGPT  FIRST_CLASS_SEMANTIC_OBJECT / HIGH
Claude   SOURCE_LOCAL / HIGH
```

ChatGPT focused on semantic continuity of the Cockpit workstream across pause, branch/head anchors and future resume. Claude focused on the fact that `docs/cockpit/README.md` already owns that state coherently.

Those are not necessarily contradictory claims. A workstream can be a first-class semantic object while one source artifact is its natural authoritative carrier.

This suggests the taxonomy may conflate:

```text
semantic first-classness
with
authoritative source locality
```

The problem is important because MC-0014 had already exposed an analogous conflation between relation reification and physical/namespace placement.

## 6. Disagreement RC-006: workstream objects versus aggregate route projection

```text
ChatGPT  FIRST_CLASS_SEMANTIC_OBJECT / HIGH
Claude   DERIVED_ONLY / MEDIUM
```

Claude's rationale decomposes the case into source-owned per-workstream state plus a derived aggregate answer to "what is active, paused and next?". That decomposition is compatible with Requirements V0.2: KA-R25..R29 can require durable workstream identity/state while the global route view remains rebuildable.

The single corpus case may therefore combine two semantic layers that should not share one label:

```text
workstream/activity identity and state
aggregate current-routing projection
```

This is a likely case-granularity/construct issue rather than evidence that one reviewer simply failed.

## 7. Disagreement RC-012: packet-grounding failure

```text
ChatGPT  UNRESOLVED / MEDIUM
Claude   SOURCE_LOCAL / HIGH
```

The packet only displays the `current_routing.json` tuple. It does not say whether the fields are canonical, derived or mixed. ChatGPT therefore returned `UNRESOLVED`.

Claude's rationale asserts that the file is "deliberately authoritative" and that no other repository surface separately owns the facts. Those claims are not present in the packet. Claude declared no additional source reads and explicitly stated it did not fill packet gaps from memory.

The original Claude record must not be silently rewritten. Instead, Message 003 must audit whether this one judgment was protocol-nonconforming and, if so, identify the packet-only answer.

## 8. Construct-validity implication

The first real-corpus protocol successfully removed V0.2's answer-bearing fixture flags, but it now exposes a deeper issue. The four mutually exclusive labels may combine at least three dimensions:

```text
1. Does the semantic thing itself deserve durable addressable identity/lifecycle?
2. Where does authoritative state about that thing naturally live?
3. Is the queried relationship/state unique authority or a rebuildable derived view?
```

A first-class semantic object can have one natural source; a source-local object's aggregate status can also feed a derived view. Therefore `SOURCE_LOCAL`, `FIRST_CLASS_SEMANTIC_OBJECT` and `DERIVED_ONLY` may not be mutually exclusive at the same semantic level unless the unit of judgment is defined more carefully.

A mechanized admission rule is blocked until this construct is repaired. Otherwise the project would formalize an unstable target label.

## 9. Comparative turn required

MC-0015 Message 003 is warranted because the thread contract allows additional dialogue when material case-level disagreement has clear value. Claude is now intentionally exposed to ChatGPT's labels and Message 002.

The comparative turn is narrowly limited to:

```text
RC-005 taxonomy orthogonality
RC-006 object/view decomposition
RC-012 packet-grounding audit
smallest corrected conceptual axes
architecture-neutral evidence implication
```

It must not select a storage technology, target architecture or mechanized classifier.

## 10. Current disposition

```text
CLAUDE_INDEPENDENT_PASS=ACCEPTED
EXACT_LABEL_AGREEMENT=12_OF_15
AGREEMENT_RATE=0.80
DESCRIPTIVE_KAPPA=0.5454545455
RC012_SOURCE_GROUNDING=QUESTIONED
FIRST_CLASS_VS_SOURCE_LOCAL_ORTHOGONALITY=OPEN
WORKSTREAM_OBJECT_VS_ROUTE_VIEW_DECOMPOSITION=OPEN
MECHANIZED_RULE=BLOCKED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=MC0015_CLAUDE_MESSAGE003_COMPARATIVE_CONSTRUCT_REVIEW
```

## 11. Comparative resolution

Claude Message 003 confirms the construct-validity diagnosis and resolves all three disagreements without another model round. RC-005 demonstrates that durable first-class identity can coexist with one natural authoritative source. RC-006 must be decomposed into durable per-workstream semantic units and a derived aggregate route projection. Claude explicitly marks its original RC-012 `SOURCE_LOCAL / HIGH` label as protocol-nonconforming; the packet-only answer is `UNRESOLVED`.

Research 143 freezes the corrected judgment model for subsequent architecture reasoning. The 12/15 original-label agreement remains historical experiment evidence but is not treated as the final semantic classification scheme. Mechanized admission-rule work remains deferred.

```text
TAXONOMY_CONSTRUCT_VALIDITY=RESOLVED_BY_TWO_AXIS_MODEL
MC0015=RESOLVED
NEXT=WHOLE_ARCHITECTURE_CANDIDATE_SYNTHESIS
```
