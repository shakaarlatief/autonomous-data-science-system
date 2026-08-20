# Checkpoint Records

**Status:** Current checkpoint-format contract  
**Authority:** Governs metadata and interpretation of files in `docs/checkpoints/`  
**Effective from:** Checkpoint 100  
**Last reviewed:** 2026-08-20

## Purpose

Checkpoint files preserve historical project state, experiment milestones, design transitions, verification records, and continuity boundaries. They are provenance records rather than automatic current authority.

The checkpoint body may legitimately differ by checkpoint type, but the metadata at the top of every checkpoint should be consistent enough that a future reader can determine what the record is, where it belongs in the project lifecycle, which ChatGPT project/session produced it, and how much authority it has without inferring those facts from the filename or surrounding Git history.

This contract was introduced after a repository audit found that early design checkpoints often contained rich contextual metadata while later operational checkpoints sometimes contained only a date. The content itself remained preserved, but the metadata drift reduced consistency, discoverability, continuity, and professional robustness.

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

These six fields form the methodological/historical metadata core.

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
Post-V0 methodological-navigation and reusable-knowledge design
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

## Mandatory ChatGPT session provenance

The current repository-development process is conducted inside a ChatGPT Project. Session identity is therefore part of checkpoint provenance and must not depend on author style.

Every checkpoint created under this development process must also record:

```text
**Design session:** ...
**ChatGPT project:** ...
**Session title:** ...
```

For the current session:

```text
Design session: 02
ChatGPT project: Autonomous Data Science System
Session title: 02 - Methodological Brain & Knowledge Units
```

The previous session was:

```text
Design session: 01
ChatGPT project: Autonomous Data Science System
Session title: 01 - Foundations & Checkpoint 0
```

These fields are provenance, not methodological authority. They allow a future session to reconstruct where a checkpoint was produced and make proactive session rotation auditable.

If project development later moves outside ChatGPT or adopts a different interaction environment, this contract and its validator should be deliberately revised to represent the new provenance model. The fields should not simply disappear through metadata drift.

## Type-specific metadata extensions

The common and session-provenance fields should be extended when additional metadata is genuinely useful for the checkpoint type.

### Design and continuity checkpoints

Possible additional fields include:

```text
**Implementation status:** ...
**Origin:** ...
```

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

A design checkpoint and a held-out treatment terminal record are not the same kind of artifact. Requiring every checkpoint to carry the exact same long list of type-specific fields would create meaningless or misleading metadata.

The professional requirement is therefore:

```text
small mandatory historical/authority core
    +
mandatory interaction-session provenance
    +
type-specific metadata where useful
```

This mirrors the broader project principle that heterogeneous objects should not be forced into one oversized universal schema merely for superficial uniformity.

## Historical normalization status and policy

Checkpoints `000` through `099` predate the explicit checkpoint contract and originally contained several metadata styles.

On 2026-08-20 they were normalized mechanically and conservatively by the repository migration workflow. The normalization added the mandatory metadata core and the now-confirmed Session 01 provenance while preserving titles and substantive bodies. The successful workflow commit is:

```text
bae5b8d00fa5da16029afee790c1a6762dc6c0fc
Normalize legacy checkpoint metadata
```

Historical metadata repair follows these rules:

1. preserve the checkpoint title and substantive body;
2. preserve the historical date and historical meaning;
3. add mandatory metadata using information already supported by the checkpoint, repository stage, frozen experiment records, repository history, or explicitly confirmed session provenance;
4. do not invent unavailable session information;
5. do not retroactively promote a historical checkpoint into current authority;
6. do not rewrite old conclusions merely because later evidence changed the project;
7. use type-specific fields only when they materially improve interpretation.

Metadata repair is therefore allowed even though checkpoint bodies are historical provenance. The repair changes discoverability and classification, not the historical substantive record.

## Required header template

A new checkpoint in the current ChatGPT session should normally begin like this:

```markdown
# Checkpoint NNN: Descriptive title

**Date:** YYYY-MM-DD  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 methodological-navigation and reusable-knowledge design  
**Scope:** Records ...  
**Authority:** Historical provenance; current promoted sources govern current interpretation.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units
```

Then add type-specific metadata only where useful.

## Checkpoint body expectations

Checkpoint bodies remain purpose-specific. A substantive design checkpoint should normally preserve the current focus, important reasoning, accepted conclusions, active hypotheses, unresolved questions, explicit non-decisions, promotion-audit result, and exact continuation point.

A narrow experiment terminal record may instead focus on the operational evidence needed to establish the experiment milestone. Consistent metadata does not require artificial narrative padding.

## Relationship to current project authority

The general repository authority hierarchy still applies. Checkpoints preserve what the project believed, observed, or did at a particular time. They do not silently override current canonical documents, later promoted foundations, frozen contracts within their declared scope, or final experiment reports.

## Enforcement

Checkpoint metadata is mechanically validated by:

```text
scripts/check_checkpoint_metadata.py
```

The validator checks both the historical/authority core and the session-provenance fields. Metadata drift should be corrected mechanically rather than tolerated as a stylistic variation.
