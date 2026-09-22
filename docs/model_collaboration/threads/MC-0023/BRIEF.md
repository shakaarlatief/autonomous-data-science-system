# MC-0023 Brief: Adversarial Review of Accepted G-DUAL Whole-Repository Architecture

**Thread:** MC-0023
**Date opened:** 2026-09-22
**Review mode:** ADVERSARIAL_REVIEW
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact review target:** `33af35442df7350d9571e4f59108c393759ad4b3`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. The owner has accepted G-DUAL as the Level-1 target, but this review may identify evidence requiring clarification, amendment or reopening before R6/R7 detailed design. It cannot itself migrate files, amend Research 177/218/Specification 028, or switch authority.

## 1. Why this review exists

The whole-repository redesign has now moved beyond the original Research 218 documentation problem.

Research 240 explicitly widened the scope to the complete ADS physical repository architecture.

Research 241-242 inventoried and classified the current repository and analyzed lifecycle, dependency, qualification and co-change boundaries.

Research 243 froze six repository architecture families.

Research 244 performed professional-pattern and future-growth stress review and synthesized Candidate G.

Research 245 derived the exact Level-1 recommendation:

    G-DUAL
    PRODUCT_PROJECT_DUAL_PLANE_ROLE_FIRST_BOUNDED_WORKSPACE

Research 246 records the owner's acceptance of that Level-1 architecture and an important stronger clarification:

> below Level 1, the redesign remains from-scratch. No current folder, subsystem, file family, name or conceptual grouping is protected merely because it exists today.

Before ChatGPT begins R6 subsystem design and R7 information-architecture design under that accepted target, perform one adversarial review.

This is deliberately **post-acceptance** and **not blind**. The goal is to catch a material flaw before detailed design hardens around it.

## 2. Exact review target

Bind the review to exact commit:

```text
33af35442df7350d9571e4f59108c393759ad4b3
```

At minimum read the exact-target versions of:

```text
docs/research/240_pkia_e01_whole_repository_physical_architecture_scope_and_design_program.md
docs/research/241_whole_repository_r0_inventory_and_r1_responsibility_classification.md
docs/research/242_whole_repository_r2_lifecycle_dependency_and_cochange_analysis.md
docs/research/243_whole_repository_r3_repository_architecture_archetype_synthesis.md
docs/research/244_whole_repository_r4_professional_pattern_and_growth_stress_review.md
docs/research/245_whole_repository_r5_root_role_derivation_and_recommended_target.md
docs/research/246_whole_repository_r5_owner_acceptance_and_from_scratch_lower_level_boundary.md

docs/checkpoints/570_whole_repository_physical_architecture_scope_clarified.md
docs/checkpoints/571_whole_repository_r2_boundaries_identified.md
docs/checkpoints/572_whole_repository_r3_candidate_archetypes_frozen.md
docs/checkpoints/573_whole_repository_r4_candidate_g_convergence.md
docs/checkpoints/574_whole_repository_r5_g_dual_target_recommended.md
docs/checkpoints/575_g_dual_accepted_lower_level_architecture_open.md

docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md
docs/research/218_w5_final_information_architecture_reconciliation_and_target_freeze.md
docs/research/236_project_knowledge_information_architecture_evolution_case_and_residency_boundary.md
docs/research/239_pkia_e01_g1_historical_lifecycle_independence_measurement.md

docs/model_collaboration/threads/MC-0022/messages/001_claude_independent_residency_and_reuse_architecture.md
docs/model_collaboration/threads/MC-0022/messages/002_chatgpt_materialized_project_sovereignty_candidate_and_comparative_exposure.md
docs/model_collaboration/threads/MC-0022/messages/003_claude_comparative_residency_and_reuse_review.md
docs/model_collaboration/threads/MC-0022/messages/004_chatgpt_reconciliation_and_residency_disposition.md

README.md
pyproject.toml
frontend/package.json
prototype_v0/pyproject.toml
alembic.ini
```

Inspect the actual repository tree, code, tests, schemas, workflows and current physical groupings as needed.

Use your preserved MC-0011 through MC-0022 architectural context where helpful.

You may use external professional sources if they materially discriminate the architecture. Distinguish those sources from ADS evidence.

## 3. Accepted target under review

The owner has accepted only this Level-1 structure:

```text
TRUE ROOT
    repository-host/bootstrap/tool-required anchors

product/
    operational ADS system and product-owned assets

project/
    machinery, knowledge, evidence, engineering and history used to
    build, govern, understand, validate, reconstruct and preserve ADS
    as a development project
```

Within the two planes, only evidence-backed lifecycle/build boundaries should become workspaces.

The accepted target is intentionally **not** a final folder tree.

## 4. Critical owner clarification you must test

Do not assume today's lower-level units survive.

The owner explicitly means that **any current architecture below Level 1 can be redesigned from scratch**.

Examples include:

```text
cockpit/
source_universe/
local_execution/
model_collaboration/
methodological_knowledge/
private_companion/
project_knowledge/
research/
specifications/
checkpoints/
experiments/
frontend/
src/ads_system/
migrations/
tests/
schemas/
scripts/
tools/
prototype_v0/
current root files
all current subfolders/file boundaries
```

For any such thing, the eventual design may:

```text
retain
rename
move
restructure
split
merge
absorb into several owners
replace with another mechanism
externalize
retire
preserve only as historical evidence
eliminate the current folder while preserving relevant content/history
```

Do not critique G-DUAL as though it requires preserving these entities.

Conversely, actively search for places where Research 245/246 still **accidentally inherit** present-day groupings or concepts despite the from-scratch requirement.

## 5. Adversarial tasks

### A. Attack the Product / Project distinction

Ask whether `product/` versus `project/` is genuinely a durable Level-1 distinction or merely a neat abstraction.

Look for concerns that do not fit without distortion.

Examples to probe:

```text
methodological knowledge
Source Universe
benchmarks/evaluation datasets
model collaboration
local execution
private companion
CI / repository engineering
project-control runtime
generated project views
developer tooling
deployment/infrastructure
observability
security
shared contracts
historical evidence
```

If a third durable plane is required, identify it precisely and explain why it cannot be a workspace/cross-plane owner instead.

### B. Attack "true root"

Determine whether the "tool-required root only" rule is strong enough to prevent the root from becoming another miscellaneous bucket.

Identify the minimum legitimate root responsibilities and any false positives in Research 245.

### C. Attack the workspace rule

The current strong workspace candidates are:

```text
ADS Python runtime
frontend
project-development system
```

Ask whether this is still leaking current structure.

Could the runtime itself need to be decomposed differently?

Could frontend be only one surface inside a broader product-interface architecture?

Could the project-development system actually be multiple systems?

Could repository engineering belong inside it or remain separate?

Do not preserve current workspace candidates automatically.

### D. Attack the from-scratch claim

Assess whether Research 246 is actually strong enough to prevent migration-by-relabeling.

Search for hidden assumptions such as:

```text
current folder == future subsystem
current document family == future knowledge family
current package == future workspace
current prototype == future experiment model
current project_knowledge boundary == future project system
```

If you find inheritance leakage, identify the exact downstream guard R6/R7 needs.

### E. Attack product-owned versus project-owned knowledge

The recommendation distinguishes:

```text
product-owned knowledge
    knowledge the ADS product operates on/exposes

project knowledge
    knowledge about developing/governing ADS
```

Stress-test hard ambiguous cases.

Determine whether this is a stable authority rule or whether another dimension is needed.

### F. Attack PSMF placement

Test whether the materialized project-development framework naturally belongs under the project plane, including:

```text
framework mechanism
project instance policy
control state
schemas/contracts
tests
upgrade lineage
provider/runtime integrations
```

Identify any part that naturally belongs outside project/ or outside the ADS repository.

### G. Attack the historical/evidence model

Test the claim that:

```text
active execution
    ->
qualified durable evidence
    ->
historical executable material when worth retaining
```

is sufficient for experiments/prototypes.

Identify what must remain executable/reproducible versus what can collapse to evidence.

### H. Compare against the strongest alternative

Do not merely critique G-DUAL internally.

State the strongest architecture that would replace it if G-DUAL failed.

This may be:

```text
refined artifact-first
bounded-context hybrid without dual planes
workspace-first hybrid
apps/packages/platform
a three-plane model
another design
```

Explain the discriminator.

### I. Decide whether R6/R7 can proceed

The review must end with one of:

```text
SURVIVES
    no Level-1 change required; bounded clarifications may be added

AMEND
    G-DUAL remains the family but a material Level-1 rule must change

REOPEN
    product/project Level-1 target is not reliable enough for R6/R7
```

## 6. Required output structure

Message 001 must include:

1. strongest attack on G-DUAL;
2. what survives unchanged;
3. any Level-1 amendment required;
4. any hidden current-structure inheritance found;
5. treatment of ambiguous product/project cases;
6. strongest alternative architecture;
7. exact R6/R7 guardrails recommended;
8. impact on PSMF;
9. impact on Research 218;
10. whether R6/R7 may proceed after ChatGPT reconciliation.

End with exactly:

```text
G_DUAL_ADVERSARIAL_DISPOSITION: SURVIVES|AMEND|REOPEN
MATERIAL_LEVEL1_AMENDMENT_REQUIRED: YES|NO
CURRENT_STRUCTURE_INHERITANCE_LEAK_FOUND: YES|NO
PSMF_PLACEMENT_REMAINS_VALID: YES|NO
RESEARCH218_MUST_REMAIN_CHILD_SCOPE: YES|NO
R6_R7_READY_AFTER_RECONCILIATION: YES|NO
```

## 7. Required output path

Write exactly one response at:

```text
docs/model_collaboration/threads/MC-0023/messages/001_claude_adversarial_g_dual_review.md
```

Include collaboration provenance, exact reviewed commit, interaction `claude-03`, and conversation title `03 - Project Knowledge Architecture Foundations and Design Method`.

Do not modify any other repository path.

## 8. Write boundary

Claude may write only:

```text
docs/model_collaboration/threads/MC-0023/messages/**
```

Do not modify routing, current state, research, checkpoints, implementation, tests, schemas, generated views or prior collaboration threads.

```text
MC0023=OPEN
MODE=ADVERSARIAL_REVIEW
EXACT_REVIEW_TARGET=33af35442df7350d9571e4f59108c393759ad4b3
G_DUAL=OWNER_ACCEPTED_LEVEL1_TARGET
LOWER_LEVELS=FULLY_OPEN
R6=HELD
R7=HELD
NEXT=CLAUDE_MESSAGE_001
```
