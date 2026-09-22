# Research 246: Whole-Repository R5 Owner Acceptance and From-Scratch Lower-Level Design Boundary

**Date:** 2026-09-22
**Status:** G-DUAL ACCEPTED AS LEVEL-1 TARGET / LOWER-LEVEL ARCHITECTURE REMAINS FULLY OPEN / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Accepted recommendation:** Research 245
**Owner decision:** ACCEPT
**Repository base before acceptance:** a2341810c0e8a91d3e71c2c26ad2624d1aaa87a2
**Scope:** Record the owner's acceptance of the Product/Project dual-plane Level-1 repository architecture and make explicit that this acceptance does not preserve any current lower-level folder, subsystem, artifact family or conceptual grouping merely because it exists today.

## 1. Owner decision

The owner accepts the R5 recommended Level-1 target:

    G-DUAL
    PRODUCT_PROJECT_DUAL_PLANE_ROLE_FIRST_BOUNDED_WORKSPACE

Accepted durable Level-1 roles:

    TRUE ROOT
        repository-host/bootstrap/tool-required anchors only

    product/
        the operational ADS system and product-owned assets

    project/
        machinery, knowledge, evidence, engineering and history used to
        build, govern, understand, validate, reconstruct and preserve ADS
        as a development project

This acceptance authorizes R6/R7 detailed architecture design against that Level-1 model.

It does **not** authorize physical migration.

## 2. Critical owner clarification: the redesign remains from-scratch below Level 1

The owner explicitly clarifies that acceptance of G-DUAL must not be misread as:

> preserve today's lower-level entities and fit them underneath product/ or project/.

The opposite rule applies.

Below the accepted Level-1 planes, the architecture remains design-from-scratch.

Every current folder, file family, subsystem name, conceptual grouping and representation is evidence only until independently justified.

This includes, without limitation:

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
    current subdirectories inside any of these
    current file boundaries
    current names

## 3. Structural freedom is ontological, not positional

For each current thing, later design may decide to:

    retain it as one coherent owner
    rename it
    move it
    restructure it internally
    split it into multiple independent owners
    merge it with another concern
    absorb its contents into several different owners
    replace it with a different mechanism
    externalize part or all of it
    retire it from active architecture
    preserve only selected parts as historical evidence
    preserve its historical record while eliminating the current folder
    delete obsolete generated/redundant carriers through governed migration

The future architecture does not need to retain today's folder boundary merely because useful content currently lives inside it.

Example:

    cockpit/

may ultimately remain a product workspace, become part of another product surface, split into product UI + historical design evidence + project research, or cease to exist as a single folder at all.

The same is true for every other present grouping.

## 4. Content preservation is not container preservation

This distinction is now controlling:

    valuable/authoritative content
        may need preservation, migration or semantic continuity

    current container/folder/file grouping
        has no automatic preservation claim

A future architecture may move the content of one current folder into several different natural owners.

Likewise several current folders may collapse into one better owner.

Historical truth and accepted authority must remain reconstructable, but their current representation is not sacred.

## 5. G-DUAL is a Level-1 constraint, not a lower-level template

The accepted architecture fixes only the highest-order distinction:

    product responsibility
        versus
    project-development responsibility
        versus
    true repository-root/bootstrap concerns

It does not freeze:

    workspace count
    product subsystem count
    project subsystem count
    names below product/ or project/
    current domain boundaries
    current documentation families
    current experiment model
    current testing model
    current schema model
    current prototype model
    current project-development-system internal shape

R6 must derive those boundaries from first principles.

R7 must derive the project information architecture from first principles.

## 6. R6 reasoning rule

R6 must not begin with:

> Where should cockpit, Source Universe, local_execution, project_knowledge, frontend and the other current folders move?

It must begin with:

> What durable responsibilities must the future ADS product and ADS project contain, regardless of today's folders?

Only after the durable responsibilities and boundaries are derived may current artifacts be mapped into them.

That mapping may be many-to-one, one-to-many, partial or historical-only.

## 7. R7 reasoning rule

R7 must not begin with:

> How should Research 218's current folders be nested more neatly?

It must begin with:

> What information/knowledge architecture should the project plane have if designed from scratch for long-term ADS scale, authority, evidence, reconstruction and human/agent navigation?

Research 218 remains evidence and frozen historical baseline until disposition.

It is not the skeleton the new hierarchy must preserve.

## 8. Relationship to PSMF

PSMF remains compatible with and subordinate to the accepted Level-1 architecture:

    generic project-development framework
        ->
    ADS project plane
        ->
    future project-development system boundary

The exact local system boundary, name and internal organization remain open.

No framework extraction is authorized.

## 9. Adversarial review before R6/R7 detail

Because G-DUAL is a material architecture decision, the owner has explicitly allowed another Claude review.

A post-acceptance adversarial review is useful here.

Its purpose is not to create artificial uncertainty or require consensus.

Its purpose is to test:

    whether product/project is a durable and non-arbitrary Level-1 distinction
    whether any important third role is being incorrectly forced into one plane
    whether G-DUAL creates hidden circularity
    whether current-folder assumptions still leak into the recommendation
    whether the from-scratch lower-level boundary is strong enough
    whether PSMF and Research 218 implications are correctly sequenced
    whether a simpler or more professional alternative remains materially stronger

R6/R7 detailed design should wait for this bounded adversarial review and reconciliation.

## 10. Current state

    R5=OWNER_ACCEPTED
    ACCEPTED_LEVEL1_TARGET=G_DUAL
    PRODUCT_PROJECT_DUAL_PLANE=ACCEPTED
    LOWER_LEVEL_ARCHITECTURE=FULLY_OPEN
    CURRENT_FOLDERS=EVIDENCE_ONLY
    CURRENT_CONCEPTUAL_GROUPINGS=EVIDENCE_ONLY
    CONTENT_PRESERVATION_DOES_NOT_IMPLY_CONTAINER_PRESERVATION=true
    PHYSICAL_MIGRATION_AUTHORIZED=false
    PSMF=ACCEPTED_INPUT_NOT_EXTRACTION_AUTHORITY
    R6=HELD_FOR_BOUNDED_ADVERSARIAL_REVIEW
    R7=HELD_FOR_BOUNDED_ADVERSARIAL_REVIEW
    RESEARCH218=FROZEN_BASELINE
    RESEARCH177=UNCHANGED
    SPECIFICATION028=UNCHANGED
    W5_F0=PAUSED
    AO10=HELD
    AUTHORITY_SWITCH_ALLOWED=false
    NEXT=MC0023_ADVERSARIAL_G_DUAL_REVIEW
