# Project-Knowledge Architecture

**Status:** W0 architecture documentation for the selected `PKA-CANDIDATE-01` design
**Governing contract:** Specification 028
**Implementation design:** Research 179, with Research 185 for the G010 current-state input refinement
**Operational authority:** Current continuity architecture remains authoritative until an explicit qualified W8 authority-switch decision.

This directory is the durable architecture guide for the successor project-development knowledge system. It documents the selected logical architecture and its repository implementation without treating file layout as the architecture itself.

## Logical architecture versus physical implementation

The **logical architecture** defines semantic responsibilities: canonical ownership, selective identity, authority resolution, workstream state, derived access, reconstruction, capture/promotion, and controlled migration.

The **physical implementation** realizes those responsibilities through repository files, Python modules, JSON Schemas, generated artifacts, CLI surfaces, and tests. A file path is a carrier or implementation location. It is not, by itself, a semantic identity or an authority rule.

## Documentation map

| Document | Primary concern |
| --- | --- |
| [Whole architecture](whole_architecture.md) | End-to-end logical boundaries and current physical realization |
| [Semantic authority model](semantic_authority_model.md) | Ownership, identity, authority, relations, scope, time, retrieval |
| [Knowledge lifecycle](knowledge_lifecycle.md) | Capture, review, promotion, canonical ownership, derived consumption |
| [Reconstruction and action](reconstruction_and_action.md) | Fresh-collaborator reconstruction, task classes, authority, safe action |
| [Migration and cutover](migration_and_cutover.md) | Current authority, shadow successor, qualification, cutover, rollback |

## Diagram source

The canonical diagram source is Mermaid embedded directly in these Markdown files. No rendered SVG or PNG is committed at W0. If rendered artifacts are committed later, they are derived outputs and must remain deterministically regenerable from the version-controlled source.

## Current implementation status

W0 through W4 are accepted. W5 is in progress. Research 218 reconciles the Research 208 physical/authoring freeze, Research 209 C1 result, Research 212 T3 item-carrier contract, Research 214 T4 historical-navigation contract and Research 217 T1 controlled-subject architecture into the frozen full W5 information architecture. Checkpoint 555 opens broader current semantic migration under that target. The production navigation realization is `subject_index` V2 over a vocabulary-only subject catalog plus source-owned memberships; W5 acceptance still requires the broader migration and W5-G qualification.

The broader migration program remains staged. Current continuity remains operational authority; live compatibility paths are still maintained by that architecture, successor outputs remain non-authoritative, and `AUTHORITY_SWITCH_ALLOWED=false` until a later explicit qualified W8 authority-switch decision.
