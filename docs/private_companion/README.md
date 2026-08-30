# Private Companion Knowledge Repository

**Status:** Accepted preservation architecture; companion repository creation pending  
**Date:** 2026-08-30  
**Scope:** Define the role, authority, content boundary, and continuity contract for a private companion repository used to preserve private ADS knowledge that should remain available across conversations but must not be committed to the public development repository.

## Core decision

The Autonomous Data Science System continues to be **developed in the public `autonomous-data-science-system` repository**.

The private companion repository is not a second development repository, not a private fork, and not an alternate source of implementation truth.

Its sole purpose is durable preservation of project knowledge that is useful for continuity or execution but inappropriate for public Git.

Conceptually:

```text
PUBLIC ADS REPOSITORY
    sole project-development repository
    code / tests / schemas / migrations
    architecture / specifications / decisions
    foundations / research / checkpoints
    public-safe current state and provenance
    public-safe Source Universe metadata

PRIVATE COMPANION KNOWLEDGE REPOSITORY
    private project knowledge only
    exact local paths and machine coordinates
    private operational observations
    private source-location mappings
    private continuity facts that should survive chat rotation
    private reports whose usefulness is primarily knowledge preservation

PRIVATE SOURCE VAULT / BACKUP STORAGE
    source binaries
    datasets / PDFs / books / slides
    registry snapshots and backup payloads
    large or binary private evidence artifacts

SECRET STORAGE
    passwords / API keys / tokens / credentials
    never ordinary Git content, even in the private companion repository
```

## Authority boundary

The public ADS repository remains authoritative for:

```text
what ADS is
what is being built
implementation state
accepted architecture
specifications and contracts
decisions
checkpoints and chronological development state
public current routing
verification and promotion state
public-safe Source Universe evidence
```

The private companion repository is authoritative only for private knowledge fields explicitly delegated to it by the public repository.

A private record must not silently override or contradict public project-development authority. If a conflict is discovered, the public repository records the disposition and the private record is corrected or superseded transparently.

## No development in the private companion repository

The following are explicitly out of scope:

```text
ADS application code
frontend code
tests
schemas
migrations
experiments that define project behavior
feature branches for ADS development
pull requests that implement ADS product changes
canonical specifications or architectural decisions
copies of CURRENT_STATE.md intended to compete with the public version
```

A private note may reference public commits, checkpoints, or stable IDs, but development changes themselves belong in the public repository.

## Knowledge ownership without duplication

Each fact should have one primary owner.

Example:

```text
public CURRENT_STATE
    ORIGINAL_SOURCE_ROOT = RESOLVED_PRIVATE
    capacity preflight = FAILED_INSUFFICIENT_FREE_SPACE
    cleanup required = YES

private companion
    exact ORIGINAL_SOURCE_ROOT path
    exact observed storage figures
    machine/profile context for that observation
```

The private repository should not duplicate large public documents merely to make them easier to find. It should store the private complement to public state.

## Relationship to machine-local `.ads-private/`

The Git-ignored local directory remains useful:

```text
.ads-private/
```

Its role is **machine-local execution configuration**.

The private companion repository has a different role: **durable private knowledge and cross-chat reconstruction**.

A normal pattern is:

```text
private companion knowledge
    durable private value / observation
        ->
local .ads-private file
    execution-ready machine-local representation
```

The local file may be regenerated or synchronized from private knowledge when appropriate. It should not be treated as the only durable copy of important private continuity information once the companion repository exists.

## Repository name

The intended companion repository name is:

```text
autonomous-data-science-system-private
```

It must be created as a private repository under the same project owner's GitHub account unless a later explicit decision selects a different ownership boundary.

## Initial structure

The initial repository should remain intentionally small:

```text
README.md
CURRENT_PRIVATE_STATE.md

source_universe/
    source_vault_bootstrap.json

machines/
    README.md
```

Additional structure should be earned by real private-knowledge needs rather than designed speculatively.

## Initial private Source Vault state

The first migrated private knowledge should include the facts already established during Source Vault preflight:

```text
ORIGINAL_SOURCE_ROOT
    exact value preserved privately
    public status remains RESOLVED_PRIVATE

capacity observation
    exact observed total / used / free / percent values
    public conclusion remains FAILED_INSUFFICIENT_FREE_SPACE

remaining Source Vault locations
    remain unresolved until selected
```

The private repository must not contain the Machine Learning PDFs themselves, registry backups, Source Vault object bytes, or credentials.

## Cross-chat continuity

Repository-first reconstruction remains public-first:

```text
1. reconstruct project state from autonomous-data-science-system
2. inspect whether the active public state references private companion knowledge
3. when relevant and accessible, read the corresponding private companion state
4. preserve the public/private authority boundary while continuing work
```

A new conversation must not require the project owner to repeat a value already marked `RESOLVED_PRIVATE` merely because the public repository intentionally withholds its exact value.

If the private companion repository is temporarily inaccessible, the public repository still preserves whether the private value is resolved and what the current project blocker is. Inaccessibility is not equivalent to unresolved knowledge.

## Security and privacy boundary

The companion repository is private, but that does not make it suitable for all sensitive material.

Do not store ordinary secrets such as:

```text
API keys
passwords
access tokens
private keys
service-account credentials
recovery codes
```

Do not use it as bulk binary storage. Large source artifacts belong in the Source Vault / backup architecture.

## Bootstrap status

The public-side authority contract is accepted.

Remaining bootstrap work:

```text
1. create the private GitHub repository
2. confirm the connected GitHub integration can read/write it
3. initialize the minimal private structure
4. migrate the already-known Source Vault private state
5. verify a fresh ChatGPT reconstruction can retrieve the private complement
6. only then classify the companion repository bootstrap as complete
```

Until step 4 is complete, the existing Git-ignored `.ads-private/` mechanism remains the local execution-state route and the public repository continues to preserve `RESOLVED_PRIVATE` / gate status without exposing exact values.
