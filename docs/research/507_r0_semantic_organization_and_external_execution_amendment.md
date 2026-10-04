# Research 507: R0 neutral charter amendment for semantic organization and external execution infrastructure

**Date:** 2026-10-04
**Status:** NEUTRAL R0 CHARTER AMENDED / APPLIES TO BOTH INDEPENDENT DESIGNS
**Parent:** Research 503, 506
**Selected logical target:** THIN_CENTRED_HYBRID_V03
**Scope:** Add two previously implicit but decision-relevant R0 obligations before Claude's independent physical/software design: first-principles semantic organization/navigation and a clean external execution-infrastructure boundary.
**Authority:** Neutral realization-design amendment. This does not select a semantic-navigation architecture, Runtime Bridge topology, physical architecture, implementation, migration, or cutover.

## 1. Why this amendment exists

Research 503 correctly froze a broad first-principles realization charter, but subsequent owner review identified two obligations that should not remain implicit.

First:

    semantic organization / discovery / navigation

remains genuinely open after Research 313 preserved the question and removed preservation rights from the Research 217 subject architecture.

Second:

    generic execution infrastructure ownership

must distinguish the ADS Project System from Codexless Runtime Bridge and other executor/provider surfaces.

Both can materially affect the physical architecture.

They must therefore be explicit before the independent Claude design and before physical-target selection.

## 2. Semantic organization is a separate architecture question

R7 information-role architecture answers:

    what role information plays
    who naturally owns it
    where responsibility belongs.

V03 answers:

    what governing semantic/control authority is
    how accepted effects realize
    how J3 truth derives.

Neither by itself determines:

    what a body of knowledge is about
    how semantic concepts relate
    how humans browse it
    how fresh agents discover it
    how retrieval selects context
    how AO finds relevant knowledge
    how impact analysis discovers affected knowledge.

Therefore semantic organization/navigation remains its own R0 concern.

## 3. Status of Research 217

Research 217 remains important empirical evidence.

Its controlled architecture included:

    18 assignable subjects
    6 navigation parents
    polyhierarchy
    preferred_subject
    source-owned memberships
    generated navigation projection.

Later Research 313 explicitly removed target-preservation rights from the exact vocabulary, hierarchy, membership mechanism and even the assumption that a subject-based architecture must remain primary.

Therefore:

    Research 217 = comparator/evidence
    old 18-subject system = not inherited target
    semantic navigation = unresolved.

## 4. Added neutral R0 requirements

The following requirements amend Research 503 prospectively.

### Semantic organization / discovery / navigation

R0-R45. Treat semantic organization as distinct from information-role ownership, governing semantic authority and physical location.

R0-R46. Derive semantic-organization requirements from first principles rather than preserving the Research 217 subject vocabulary by default.

R0-R47. Compare materially different candidate families, including at least:
    
    controlled subject/facet taxonomy
    typed-relational / graph-like semantic organization
    search/retrieval-first organization
    deliberate hybrids.

These are comparison families, not privileged finalists.

R0-R48. Evaluate human navigation and orientation, including the ability to answer "where should I look?" without requiring repository archaeology.

R0-R49. Evaluate fresh-agent reconstruction and context retrieval, including relevance, provenance, bounded context size and failure visibility.

R0-R50. Evaluate AO activation usefulness separately from authority. Semantic retrieval may surface candidates; it must not silently become governing authority.

R0-R51. Evaluate impact analysis, migration reasoning and architecture-evolution support, including cross-cutting knowledge that does not fit one hierarchy cleanly.

R0-R52. Distinguish authoritative/source-owned semantic declarations from generated or probabilistic retrieval/index signals. Generated semantic similarity must remain non-authoritative unless explicitly elevated through a governed acceptance path.

R0-R53. Preserve multi-dimensional navigation when justified. Information role, semantic concern, lifecycle/currentness, responsibility, relation, workstream and search relevance must not be collapsed into one accidental hierarchy merely for storage convenience.

R0-R54. Before physical-target selection, either:
    
    select a semantic-organization architecture with evidence,
    or
    explicitly freeze a bounded unresolved interface that allows the physical architecture to proceed without prejudging the later choice.

Silent inheritance of the old subject architecture is not allowed.

### External execution infrastructure

R0-R55. Give the Project System a provider-neutral executor/action-adapter boundary rather than embedding one tool product as the Project System itself.

R0-R56. Treat Codexless Runtime Bridge as reusable external developer infrastructure unless evidence proves a narrower/broader boundary is superior.

R0-R57. Separate:
    
    generic Runtime Bridge product behavior
    generic optional modules
    ADS-specific policy/capability packs
    host-private deployment state
    historical/experimental mechanisms.

R0-R58. Prevent Runtime Bridge, GitHub, Claude-side connectors, local executors or future providers from becoming semantic authority merely because they execute actions.

R0-R59. Define a normalized receipt/evidence return path from execution providers into AO, J2 and WARRANT-F.

R0-R60. Define capability discovery, version compatibility, safe degradation/fallback and project/workspace policy without hard-coding ADS semantics into the generic bridge.

R0-R61. Keep generic Runtime Bridge source, private host/deployment state and ADS integration ownership separable in the physical architecture.

R0-R62. Do not begin Runtime Bridge extraction solely to satisfy R0. First freeze what ADS actually requires from the executor boundary; then run a dedicated extraction/professionalization program unless an earlier empirical probe is necessary.

Research 503's original R0-R01 through R0-R44 remain unchanged.

## 5. Independent-design fairness

ChatGPT R0-CANDIDATE-A was frozen before this amendment.

To keep the independent comparison fair:

    ChatGPT must freeze a bounded Candidate-A addendum addressing R0-R45 through R0-R62 before Claude begins.

Claude will then receive:

    Research 503
    Research 506
    Research 507

as neutral task inputs while remaining blind to:

    Research 504
    the ChatGPT Candidate-A addendum
    Checkpoint 841
    any derivative/comparative Candidate-A material.

Thus both independent positions answer the same amended requirements.

## 6. Decision-relevant probes

At minimum, the comparative phase must decide whether empirical probes are required for:

    semantic organization/navigation
    owner/developer retrieval burden
    fresh-agent reconstruction
    AO activation recall/precision
    impact analysis
    executor interface portability
    Runtime Bridge multi-project policy separation
    execution receipt integration.

No large probe should run merely because it was listed. Use the smallest discriminating test that can change the architecture decision.

## 7. Current disposition

    R0_BASE_CHARTER=RESEARCH_503
    R0_AMENDMENT=RESEARCH_507
    TOTAL_NAMED_REQUIREMENTS=62

    SEMANTIC_ORGANIZATION_FINAL_TARGET=OPEN
    RESEARCH_217=PRESERVED_AS_COMPARATOR
    RUNTIME_BRIDGE_BOUNDARY=EXTERNAL_REUSABLE_INFRASTRUCTURE_DESIGN_INPUT

    PHYSICAL_ARCHITECTURE_SELECTED=false
    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    NEXT=FREEZE_CHATGPT_CANDIDATE_A_ADDENDUM
