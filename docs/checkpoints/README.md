# Checkpoint Records

**Status:** Current checkpoint-format contract  
**Authority:** Governs metadata and interpretation of files in `docs/checkpoints/`  
**Effective from:** Checkpoint 100  
**Last reviewed:** 2026-08-19

## Purpose

Checkpoint files preserve historical project state, experiment milestones, design transitions, verification records, and continuity boundaries. They are provenance records rather than automatic current authority.

The checkpoint body may legitimately differ by checkpoint type, but the metadata at the top of every checkpoint should be consistent enough that a future reader can determine what the record is, where it belongs in the project lifecycle, and how much authority it has without inferring those facts from the filename or surrounding Git history.

This contract was introduced after a repository audit found that early design checkpoints often contained rich contextual metadata while later operational checkpoints sometimes contained only a date. The content itself remained preserved, but the metadata drift reduced consistency, discoverability, and professional robustness.

## Mandatory metadata core

Every checkpoint must begin immediately after its H1 title with the following fields:

```text
**Date:** YYYY-MM-DD
**Status:** ...
**Checkpoint class:** ...
**Project stage:** ...
**Scope:** ...
**Authority:** ...
```

These six fields form the minimum checkpoint metadata contract.

### Date

The date on which the checkpoint was created or the recorded milestone was formally preserved.

### Status

The lifecycle role of the record. Typical values include:

```text
Historical design checkpoint
Historical experiment record
Historical verification record
Historical infrastructure record
Historical preservation-method record
Historical continuity boundary
```

A checkpoint may use a more specific status where that is genuinely useful.

### Checkpoint class

The kind of event or reasoning being preserved. Typical classes include:

```text
DESIGN
EXPERIMENT_EXECUTION
EXPERIMENT_VERIFICATION
INFRASTRUCTURE
PRESERVATION_METHOD
CONTINUITY
MIXED
```

This is classification metadata, not a claim that all checkpoint bodies must share one schema.

### Project stage

The stage of the Autonomous Data Science System project at the time represented by the checkpoint, for example:

```text
Initial conceptual design
Conceptual research and system definition
Prototype V0 development calibration
Prototype V0 held-out execution
Post-V0 product and architecture design
```

The field describes historical context. It should not be retroactively rewritten to the current project stage.

### Scope

A concise statement of what the checkpoint actually records. This prevents a narrow operational record from appearing to make broader project-level claims than it does.

### Authority

A concise statement of how the checkpoint should be interpreted relative to current documents.

The normal default is conceptually:

```text
Historical provenance. Current canonical documents, frozen contracts,
and final experiment reports govern their declared scopes.
```

A checkpoint that records a frozen contract, experiment boundary, or other stronger scope may state that explicitly, but historical prominence alone does not make a checkpoint canonical.

## Type-specific metadata extensions

The common core should be extended when additional metadata is genuinely useful for the checkpoint type.

### Design and continuity checkpoints

Possible fields include:

```text
**Design session:** ...
**ChatGPT project:** ...
**Session title:** ...
**Implementation status:** ...
**Origin:** ...
```

Session metadata is useful historical provenance but is not required when the checkpoint was not created from a design-chat milestone or when the information is unavailable.

### Experiment-execution checkpoints

Possible fields include:

```text
**Experiment:** ...
**Variant:** ...
**Condition:** ...
**Run / slot / attempt:** ...
**Evaluation status:** ...
**Blinding status:** ...
```

### Verification or infrastructure checkpoints

Possible fields include:

```text
**Artifact / component:** ...
**Verification boundary:** ...
**Treatment impact:** ...
**Change constraint:** ...
```

### Promotion or supersession metadata

Where relevant:

```text
**Promoted to:** ...
**Supersedes:** ...
**Superseded by:** ...
```

## Why the contract uses a common core plus extensions

A design checkpoint and a held-out treatment terminal record are not the same kind of artifact. Requiring every checkpoint to carry the exact same long list of fields would create meaningless or misleading metadata.

The professional requirement is therefore:

```text
small mandatory semantic core
    +
type-specific metadata where useful
```

This mirrors the broader project principle that heterogeneous objects should not be forced into one oversized universal schema merely for superficial uniformity.

## Historical normalization policy

Checkpoints `000` through `099` predate this explicit contract and contain several metadata styles.

They should be normalized mechanically and conservatively:

1. preserve the checkpoint title and substantive body;
2. preserve the historical date and historical meaning;
3. add the mandatory metadata core using information already supported by the checkpoint, repository stage, frozen experiment records, or surrounding authoritative documentation;
4. do not invent unavailable session metadata;
5. do not retroactively promote a historical checkpoint into current authority;
6. do not rewrite old conclusions merely because later evidence changed the project;
7. use type-specific fields only when they materially improve interpretation.

Metadata repair is therefore allowed even though checkpoint bodies are historical provenance. The repair changes discoverability and classification, not the historical substantive record.

Until the historical normalization pass is complete, a legacy checkpoint that lacks an explicit `Status` or `Authority` field should be interpreted conservatively as historical provenance unless a frozen specification, experiment protocol, or other authoritative source explicitly grants it a stronger role.

## Required header template

A new checkpoint should normally begin like this:

```markdown
# Checkpoint NNN: Descriptive title

**Date:** YYYY-MM-DD  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 product and architecture design  
**Scope:** Records ...  
**Authority:** Historical provenance; current promoted sources govern current interpretation.
```

Then add type-specific metadata only where useful.

## Checkpoint body expectations

Checkpoint bodies remain purpose-specific. A substantive design checkpoint should normally preserve the current focus, important reasoning, accepted conclusions, active hypotheses, unresolved questions, explicit non-decisions, promotion-audit result, and exact continuation point.

A narrow experiment terminal record may instead focus on the operational evidence needed to establish the experiment milestone. Consistent metadata does not require artificial narrative padding.

## Relationship to current project authority

The general repository authority hierarchy still applies. Checkpoints preserve what the project believed, observed, or did at a particular time. They do not silently override current canonical documents, later promoted foundations, frozen contracts within their declared scope, or final experiment reports.

## Enforcement direction

Future checkpoint creation should treat the mandatory core as a contract rather than a stylistic suggestion.

If metadata drift recurs, the repository should introduce or strengthen mechanical validation rather than relying on repeated manual cleanup. A lightweight checker is appropriate because the required fields are precise and inexpensive to verify.