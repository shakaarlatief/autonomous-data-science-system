# Autonomous Data Science System

The Autonomous Data Science System (ADS) is a rigorous adaptive environment for data-science projects in which a strong LLM is one reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

This root README is intentionally stable. Live branch, checkpoint, review and verification state are not duplicated here because those details change frequently and have dedicated owners.

## Start here

Open `docs/README.md` first. It is the structural table of contents for the repository and provides the maintained fast-routing table to current state, semantic knowledge, development method, continuity, canonical documentation and historical evidence.

For an active development continuation, resume from `docs/CURRENT_STATE.md`. For recovery after context loss, follow `docs/CONTINUITY.md`. For an older or cross-cutting subject, use `docs/KNOWLEDGE_MAP.md` rather than guessing document numbers from memory.

The root README deliberately does not maintain a second full catalog of canonical documentation routes. That catalog belongs to `docs/README.md`.

## Core repository areas

```text
src/           V1 implementation code
frontend/      professional interaction surface and design/verification work
schemas/       machine-readable interchange contracts
migrations/    persistent-schema evolution
scripts/       repository/development/validation utilities
tests/         implementation regression tests
experiments/   governed experiment implementations and outputs that belong in Git
prototype_v0/  preserved minimum-falsification prototype

docs/          canonical state, durable rationale, evidence, contracts, history,
               topic routing and specialized knowledge indexes
```

The detailed role, authority and lifecycle of each documentation family is defined in `docs/README.md`.

## Governing principle

Repository artifacts are authoritative across chats and models. Historical material is provenance, not automatic current authority. Current state, durable rationale, bounded evidence, explicit contracts and chronological history remain separate so that future collaborators can reconstruct both **what is true now** and **why the project arrived there** without relying on hidden model memory.
