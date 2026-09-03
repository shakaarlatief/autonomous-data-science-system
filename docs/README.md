# Repository and Documentation Guide

**Status:** Current structural guide  
**Authority:** Navigation and artifact-role contract. Source artifacts remain authoritative for their own scope.  
**Last reviewed:** 2026-08-30

## Purpose

This file is the structural table of contents for the Autonomous Data Science System repository. It answers questions such as:

```text
What kinds of files do we have?
What is each file family for?
Where does current truth live?
Where does deep reasoning live?
Where does historical evidence live?
Where do I look when two artifacts appear to disagree?
```

It is deliberately different from both `docs/CURRENT_STATE.md` and `docs/KNOWLEDGE_MAP.md`:

```text
docs/README.md
    structure -> artifact family -> role

docs/CURRENT_STATE.md
    present project state -> exact active boundary -> next step

docs/KNOWLEDGE_MAP.md
    subject -> all relevant durable knowledge sources
```

## Fast routing

| Need | Primary route |
|---|---|
| What is happening now? | `docs/CURRENT_STATE.md` |
| Machine-readable current pointer | `docs/current_routing.json` |
| What does each repository/document family mean? | `docs/README.md` |
| Find everything relevant to a subject | `docs/KNOWLEDGE_MAP.md` |
| Current project vision | `docs/VISION.md` |
| Current governing principles | `docs/PRINCIPLES.md` |
| Accepted explicit decisions | `docs/DECISIONS.md` |
| Unresolved important questions | `docs/OPEN_QUESTIONS.md` |
| How ADS itself is developed | `docs/DEVELOPMENT_METHOD.md` |
| How to reconstruct after context loss | `docs/CONTINUITY.md` |
| Private companion knowledge-repository boundary | `docs/private_companion/README.md` |
| Private local-runtime repository boundary | `docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md` |
| Selective structural history | `docs/MAJOR_CHANGES.md` |
| Deep durable rationale | `docs/foundations/` |
| Explicit scoped contracts | `docs/specifications/` |
| Bounded investigations/evidence | `docs/research/` |
| Historical project-state boundaries | `docs/checkpoints/` |
| Exact implementation evolution | Git history + code/tests |

## Canonical documentation surfaces

### `docs/CURRENT_STATE.md`

The **sole human-readable owner of live project state**.

It may contain the current checkpoint, branch, active review boundary, verification status, current unresolved gate and exact next step. It should stay present-tense and relatively concise. Older reasoning does not belong here once it becomes historical.

### `docs/current_routing.json`

The **sole compact machine-readable live routing pointer**.

It exists so scripts and collaborators can identify the current checkpoint/branch/promotion boundary without scraping prose. Human-readable explanation belongs in `CURRENT_STATE.md`, not in this JSON manifest.

### `docs/VISION.md`

The current high-level target and long-term system direction. It should contain durable target-system intent, not detailed temporary implementation state.

### `docs/PRINCIPLES.md`

Current cross-project working principles. Principles are more stable than hypotheses but remain explicitly revisable when evidence changes them.

### `docs/DECISIONS.md`

Accepted explicit cross-project decisions and their status. A decision record should not become a dump of every local implementation choice.

### `docs/OPEN_QUESTIONS.md`

Important unresolved questions whose uncertainty materially affects future design or scientific interpretation. Closed questions should be resolved into the appropriate stronger layer rather than accumulating indefinitely.

### `docs/DEVELOPMENT_METHOD.md`

The current operational method used to design, implement, verify, review, preserve and evolve ADS itself. This includes checkpointing, promotion, verification tiers, collaboration governance and knowledge reconciliation.

### `docs/CONTINUITY.md`

The stable protocol for continuing across chats, models, branches and unexpected context loss. It explains **how to reconstruct** current state. It does not duplicate the actual current state.

### `docs/KNOWLEDGE_MAP.md`

The **evergreen semantic subject library**.

Its question is: “What repository knowledge is relevant to this topic?” It routes subjects to canonical documents, foundations, specifications, research, selected checkpoints and specialized indexes. A source may belong to multiple subjects. It is not the current-state document and is not an authority database.

### `docs/MAJOR_CHANGES.md`

A selective structural history for major changes in how the project is understood, built, evaluated or preserved. It is not a commit changelog.

## Numbered durable knowledge families

### `docs/foundations/`

**Role:** deep durable rationale.

Foundations preserve the richest reasoning behind major concepts that should survive individual experiments or stages. They explain motivations, distinctions, assumptions, examples, failure modes and design logic that would be too detailed for canonical summaries.

A foundation is not automatically current authority. Later accepted decisions/specifications may refine or supersede part of it. The Knowledge Map routes every numbered foundation by subject.

### `docs/specifications/`

**Role:** explicit scoped contracts.

Specifications freeze what a bounded implementation, experiment, interface or guard is supposed to do. They are stronger than exploratory research within their accepted scope because they define exact expectations before or during governed execution.

Specification status matters. Accepted, failed, incomplete, superseded and exploratory specifications must not be conflated. The Knowledge Map routes every numbered specification by subject.

### `docs/research/`

**Role:** bounded investigations, evidence, alternatives and design studies.

Research records preserve questions, candidate architectures, comparisons, experiments, human-review findings and lessons. Research can support later promotion, but recent research is not automatically canonical truth.

The Knowledge Map routes every numbered research record by subject, including records that are useful under more than one topic.

### `docs/checkpoints/`

**Role:** meaningful historical project-state and continuity boundaries.

Checkpoints answer: “What had become true or important at this point in the project's chronology?” They preserve accepted/rejected human review, experiment milestones, stage changes, continuation points and major method changes.

They are not the live state. `docs/checkpoints/README.md` defines the metadata contract and granularity policy. Git carries micro-level implementation history, so one open review question may absorb several small refinements without creating a checkpoint per commit.

Because checkpoints are numerous, `KNOWLEDGE_MAP.md` assigns every numbered checkpoint to one or more semantic topic ranges and directly links especially important checkpoints. Exact chronological lookup remains available through the checkpoint directory, specialized ledgers and Git.

## Specialized documentation domains

### `docs/cockpit/`

Specialized Project Cockpit decision/provenance indexes. In particular:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
    disposition and human-review history for the Phase-C design program

docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    human-readable accepted implementation provenance

docs/cockpit/accepted_implementation_manifest.json
    machine-readable exact implementation provenance
```

These specialized indexes exist because duplicating all Cockpit detail in the global Knowledge Map would reduce clarity.

### `docs/methodological_knowledge/`

Specialized Methodological Knowledge Universe documentation. `COVERAGE_MAP.md` is the domain-level coverage/navigation surface for the methodological universe and construction program.

### `docs/source_universe/`

Source Universe architecture, permanent-vault bootstrap material and validation records. This domain preserves the distinction between source artifacts/evidence provenance and the reusable Methodological Knowledge Universe derived from sources.

### `docs/private_companion/`

Public-side authority and continuity contract for the private companion knowledge repository.

The private companion repository is a **knowledge-preservation complement**, not a second ADS development repository. It may preserve exact private paths, machine/storage observations, private source-location mappings and similar cross-chat continuity facts that should not be exposed in public Git.

The public `autonomous-data-science-system` repository remains the sole location for ADS code, tests, architecture, specifications, decisions, checkpoints and implementation evolution. Large private source artifacts belong in the Source Vault/backup architecture, and credentials/secrets do not belong in ordinary Git even when a repository is private.

### `docs/model_collaboration/`

Provider-neutral collaboration protocol, review inbox and per-thread state. Per-thread records preserve exact coordination/review provenance; they do not override product/scientific authority merely because another model agreed.

### `docs/experiments/`

Documentation for experiment programs whose durable evidence belongs in the documentation tree, including final classifications and result interpretation.

## Implementation and operational repository areas

### `src/`

Current V1 application/domain implementation. Code is the exact executable mechanism, not a substitute for the rationale or contract that explains why it exists.

### `frontend/`

Frontend implementation, design-lab experiments, browser regression tests and professional interaction-surface work. Accepted visual behavior may have exact provenance in specialized Cockpit manifests.

### `schemas/`

Machine-readable interchange/data contracts used across components and tests.

### `migrations/`

Persistent database-schema evolution. Migration chronology is implementation history and must remain compatible with accepted persistence contracts.

### `scripts/`

Repository-owned development, validation, launch, audit and maintenance utilities. Small deterministic validators are preferred when a concrete recurring integrity problem has earned them.

### `tests/`

Implementation regression tests for the V1 system and repository contracts.

### `experiments/`

Executable governed experiment material and durable experiment artifacts appropriate for Git. An experiment's scientific conclusion still belongs in its frozen specification/result/research/checkpoint evidence chain.

### `prototype_v0/`

Preserved minimum-falsification prototype and its implementation. It remains historical evidence after V0's scientific conclusion; it is not the current V1 architecture.

### `.github/workflows/`

Continuous-integration and repository-governance workflows. A green workflow is evidence only for the checks that actually ran. Verification tier and scope must remain explicit.

### `pyproject.toml`, `uv.lock`, `.python-version`

Python project/dependency/runtime tooling contracts. The lockfile preserves the resolved dependency environment.

### `alembic.ini`

Alembic migration configuration.

## Cross-repository authority boundary

ADS now uses three Git repository roles with deliberately different authority:

```text
public autonomous-data-science-system
    sole development repository
    sole authority for project-development state

private autonomous-data-science-system-private
    durable private knowledge complement only
    no competing product-development state

private autonomous-data-science-system-local-runtime
    versioned non-secret local/runtime implementation evidence
    preserves `.ads-private` materialization/candidates/deployment provenance
    no competing product-development state
```

The local-runtime contract is:

```text
docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md
```

A private record may reference public commits, checkpoints or stable identifiers, but must not silently redefine them. If private knowledge exposes a reason to change the ADS product or development method, the actual change is made and preserved in the public repository through the normal development process.

## Authority and conflict resolution

Repository location alone does not determine truth. Use status, scope, chronology and explicit supersession.

Practical order within the relevant scope:

```text
accepted/frozen specification or explicit contract
    -> accepted explicit decision / current canonical document
    -> current principles, vision, development method and continuity
    -> foundation rationale
    -> bounded research evidence
    -> checkpoint/collaboration provenance
    -> raw historical material
```

`CURRENT_STATE.md` is special because it owns **what is active now**, but it should route to the stronger source when explaining a scientific, architectural or product claim.

The private companion repository is authoritative only for private fields explicitly delegated to it. It cannot overrule the public hierarchy above for project development.

If two durable artifacts genuinely conflict and the hierarchy/status/chronology does not resolve the conflict, record the ambiguity rather than guessing.

## Anti-duplication contract

Each navigation layer has one primary job:

```text
root README               stable entry point
docs/README               structural repository map
CURRENT_STATE             live human-readable state
current_routing.json       live machine-readable pointer
KNOWLEDGE_MAP             evergreen semantic subject library
CONTINUITY                 reconstruction/recovery protocol
DEVELOPMENT_METHOD         operational development method
MAJOR_CHANGES              selective structural history
private companion          private knowledge complement only
```

A small amount of cross-linking is expected. Repeating volatile current checkpoint/branch/test details across several of these files is not.

## Reconciliation rule

At meaningful project boundaries, ask separately:

```text
Did current state change?              -> CURRENT_STATE + current_routing
Did repository structure/roles change? -> docs/README
Did durable subject knowledge change?  -> KNOWLEDGE_MAP
Did the development method change?     -> DEVELOPMENT_METHOD
Did continuity procedure change?       -> CONTINUITY
Was the change structurally major?     -> MAJOR_CHANGES
Did deeper rationale/evidence emerge?  -> foundation/research/specification
Did chronology materially advance?     -> checkpoint
Did private continuity knowledge change? -> private companion repository when appropriate
```

This separation is intended to make the repository easier to reconstruct as it grows, not merely more documented.
