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

W0, W1 and W2 are accepted. The successor now has a qualified bounded live-control semantic slice plus the complete persistent eight-view structural shadow set derived from those owners. W3 compatibility shadow is the next migration wave and has not yet started.

The broader migration program remains staged. Current continuity remains operational authority; live compatibility paths are still maintained by that architecture, successor outputs remain non-authoritative, and `AUTHORITY_SWITCH_ALLOWED=false` until a later explicit qualified W8 authority-switch decision.
