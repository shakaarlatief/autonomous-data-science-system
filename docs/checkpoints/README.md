# Checkpoint Records

**Status:** Current checkpoint-format contract  
**Authority:** Governs metadata and interpretation of files in `docs/checkpoints/`  
**Initial contract effective from:** Checkpoint 100  
**Provider-neutral provenance effective from:** Checkpoint 204  
**Last reviewed:** 2026-08-27

## Purpose

Checkpoint files preserve historical project state, experiment milestones, design transitions, verification records, collaboration boundaries, and continuity state. They are provenance records rather than automatic current authority.

The body may differ by checkpoint class, but the header must identify enough historical, authority, and interaction context that a future collaborator can interpret the checkpoint without inferring those facts from filenames, chat memory, or surrounding Git history.

---

## Mandatory historical/authority core

Every checkpoint must begin immediately after its H1 title with:

```text
**Date:** YYYY-MM-DD
**Status:** ...
**Checkpoint class:** ...
**Project stage:** ...
**Scope:** ...
**Authority:** ...
```

These six fields apply across all current checkpoint eras.

### Date

The date on which the checkpoint was created or the represented milestone was formally preserved.

### Status

The lifecycle role of the record, for example historical design checkpoint, experiment record, verification record, infrastructure record, preservation-method record, or continuity boundary.

### Checkpoint class

Typical values include:

```text
DESIGN
EXPERIMENT_EXECUTION
EXPERIMENT_VERIFICATION
INFRASTRUCTURE
PRESERVATION_METHOD
CONTINUITY
MIXED
```

This classifies the record without forcing every checkpoint body into one schema.

### Project stage

The historical ADS stage represented by the checkpoint. It must not be rewritten later merely because the project advanced.

### Scope

A concise statement of what the checkpoint actually records.

### Authority

A concise statement describing how the record should be interpreted relative to current canonical documents/specifications.

The ordinary default remains conceptually:

```text
Historical provenance. Current canonical documents, accepted/frozen contracts,
and final result reports govern their declared scopes.
```

---

# Interaction provenance contracts

The repository has two prospective interaction-provenance eras.

## Era A: ChatGPT-specific provenance through Checkpoint 203

Checkpoints 100 through 203 were created while the project-development process was formally ChatGPT-specific.

They retain:

```text
**Design session:** ...
**ChatGPT project:** ...
**Session title:** ...
```

Earlier Checkpoints 000 through 099 were conservatively normalized with the same known historical ChatGPT provenance during the v0.4 migration.

Those fields remain historically correct and must not be rewritten merely because the project later adopted multi-model development.

## Era B: provider-neutral provenance from Checkpoint 204 onward

Beginning with Checkpoint 204, every new checkpoint must also record:

```text
**Interaction environment:** ...
**Project / workspace:** ...
**Interaction session:** ...
**Conversation title:** ...
**Primary collaborator:** ...
```

### Interaction environment

The product/runtime in which the checkpoint-producing interaction occurred, for example:

```text
ChatGPT
Claude
Claude Code
Human
another future environment
```

### Project / workspace

The human-facing project/workspace context where applicable. The current shared name is:

```text
Autonomous Data Science System
```

If an environment does not expose a formal workspace, record a truthful non-empty descriptor rather than inventing one.

### Interaction session

Stable repository-facing interaction identity such as:

```text
chatgpt-06
claude-01
```

Interaction environments maintain their own sequence. A provider-local ID is intentionally preferred over one artificial global conversation counter.

### Conversation title

The visible conversation/session title when available. If the environment has no titled conversation, record a truthful non-empty session descriptor rather than leaving the field empty.

### Primary collaborator

The collaborator principally responsible for preserving the checkpoint, for example:

```text
ChatGPT
Claude
Human
```

Provider/model identity is provenance rather than methodological authority.

---

## Optional interaction/collaboration extensions

Where materially useful, checkpoints may additionally include:

```text
**Collaboration thread:** MC-NNNN
**Collaboration role:** ...
**Model / configuration:** ...
**Effort / reasoning mode:** ...
**Interaction surface:** ...
```

Do not add fields merely because the UI exposes them.

A value that the model cannot reliably introspect should not be guessed. Human-reported or product-displayed values may be preserved with their source clear in the body when consequential.

SOLO work does not need a collaboration-thread field.

---

## Type-specific metadata extensions

The common metadata should be extended where useful for the checkpoint class.

### Design and continuity

Possible fields:

```text
**Implementation status:** ...
**Origin:** ...
```

### Experiment execution

Possible fields:

```text
**Experiment:** ...
**Variant:** ...
**Condition:** ...
**Run / slot / attempt:** ...
**Evaluation status:** ...
**Blinding status:** ...
```

### Verification or infrastructure

Possible fields:

```text
**Artifact / component:** ...
**Verification boundary:** ...
**Treatment impact:** ...
**Change constraint:** ...
```

### Promotion/supersession

Possible fields:

```text
**Promoted to:** ...
**Supersedes:** ...
**Superseded by:** ...
```

---

## Why the contract is versioned prospectively

A checkpoint's interaction provenance should describe the environment that actually produced it.

Therefore:

```text
historical ChatGPT checkpoint
    keeps historical ChatGPT fields

new multi-model-era checkpoint
    uses provider-neutral fields
```

The project does not rewrite old records simply to make every header look the same.

This follows the broader rule that historical metadata repair may improve classification/discoverability but must not rewrite historical substantive conclusions or invent unavailable provenance.

---

## Historical normalization status

Checkpoints 000 through 099 were normalized mechanically and conservatively on 2026-08-20 while preserving titles and substantive bodies.

Successful normalization commit:

```text
bae5b8d00fa5da16029afee790c1a6762dc6c0fc
Normalize legacy checkpoint metadata
```

Checkpoints 100 through 102 received confirmed Session 02 provenance in:

```text
ce6b029af78a33bb64f85377f5ff753f088ba190
Backfill Session 02 checkpoint provenance
```

That historical repair is closed. The v0.5 provider-neutral migration begins prospectively at Checkpoint 204.

---

## Required templates

### Checkpoint 204+ template

```markdown
# Checkpoint NNN: Descriptive title

**Date:** YYYY-MM-DD  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** ...  
**Scope:** Records ...  
**Authority:** Historical provenance; current promoted sources govern current interpretation.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-06  
**Conversation title:** 06 - Methodological Knowledge Universe Construction  
**Primary collaborator:** ChatGPT
```

Add collaboration/model fields only when useful.

### Historical ChatGPT-era template

The earlier required shape remains valid for Checkpoints through 203:

```text
Design session
ChatGPT project
Session title
```

No historical backfill to the new provider-neutral names is required.

---

## Checkpoint body expectations

A substantive design checkpoint should normally preserve current focus, important reasoning, accepted conclusions, hypotheses, unresolved questions, explicit non-decisions, promotion-audit result, and exact continuation point.

A narrow execution/verification checkpoint may focus on the evidence required to establish that milestone.

Consistent metadata does not require artificial narrative padding.

---

## Granularity during rapid iterative work

A checkpoint represents a meaningful continuity or evidence boundary, not every repository commit.

Within an already-open browser/design/implementation gate, small corrections should normally remain in ordinary Git history and the active research record when they do not materially change project interpretation. Examples include:

```text
pixel-level visual tuning
small geometry corrections
copy/label refinements
implementation defects that do not alter the tested hypothesis
exact-target refreshes within the same human review gate
```

Create a new checkpoint when the refinement materially changes one or more of:

```text
the human review question
the accepted/rejected design evidence
the semantic interpretation
the promotion status
the active repository route
the next continuation boundary
```

This keeps checkpoint history informative as the project grows while preserving fine-grained implementation provenance in Git.

---

## Relationship to project authority

The normal repository authority hierarchy still applies.

Checkpoints preserve historical state and human/model-review evidence. They do not silently override current canonical documents, accepted/frozen specifications within scope, accepted decisions, or final experiment reports.

Multi-model consensus inside a checkpoint also does not create automatic authority.

---

## Enforcement

Checkpoint metadata is mechanically validated by:

```text
scripts/check_checkpoint_metadata.py
```

The validator applies the ChatGPT-specific contract to checkpoints before 204 and the provider-neutral contract to Checkpoint 204 onward.

This versioned validation is deliberate. Metadata should evolve prospectively rather than drift silently.

### Operational acceptance gate

A checkpoint-producing repository change is not considered operationally closed until the checkpoint metadata validation for that change has completed successfully.

The active collaborator should therefore:

```text
write checkpoint
-> inspect the Checkpoint metadata check result
-> if failed, repair the checkpoint before treating the gate as closed
-> only then rely on the checkpoint as a clean continuation boundary
```

A failed metadata check does not invalidate the substantive historical evidence in the checkpoint body, but it is a repository-integrity defect and should not be ignored while continuing to accumulate later checkpoints.
