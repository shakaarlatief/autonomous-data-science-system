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

W0 through W4 are accepted. W5 is in progress. Research 208 freezes the future physical/authoring V0.2 subset after MC-0018, while the semantic-subject vocabulary, item-registry identity contract, historical-navigation preservation and production navigation realization remain gated by C1/T1/T3/T4. Broader current semantic migration follows only after those empirical gates close and the remaining W5 information-architecture contract is frozen.

The broader migration program remains staged. Current continuity remains operational authority; live compatibility paths are still maintained by that architecture, successor outputs remain non-authoritative, and `AUTHORITY_SWITCH_ALLOWED=false` until a later explicit qualified W8 authority-switch decision.
