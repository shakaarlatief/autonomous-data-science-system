# ADS Private Local-Runtime Repository

**Status:** Accepted repository-role contract / bootstrap in progress
**Date:** 2026-09-03
**Scope:** Define the role, authority, synchronization model, security boundary, and bootstrap rules for the private repository that preserves non-secret ADS machine-local/runtime implementation state which would otherwise exist only under Git-ignored `.ads-private/`.
**Authority:** Repository-role and continuity contract. The public ADS repository remains sole project-development authority; this private runtime repository preserves implementation/materialization evidence only.

## Repository identity

```text
GitHub repository
    shakaarlatief/autonomous-data-science-system-local-runtime

visibility
    private

intended default branch
    main
```

The local clone is expected to exist as a sibling of the public ADS checkout when this machine is being used for local Codexless development.

## Why this repository exists

The public ADS checkout intentionally ignores:

```text
.ads-private/
```

That directory has grown beyond one small configuration file. It now contains material such as:

```text
Codexless source candidates
activation/publication scripts
focused regression scripts
runtime experiments/probes
exact candidate snapshots and hashes
machine-local Codexless authority configuration
Source Vault execution-ready local state
```

Keeping all of that only on one workstation creates unnecessary continuity and reproducibility risk. The private local-runtime repository provides durable Git history for the non-secret portion of that state.

## Authority model

The repository hierarchy is:

```text
PUBLIC autonomous-data-science-system
    sole ADS project-development authority
    owns what is accepted/current and why
    owns architecture, specifications, decisions, research, checkpoints,
    public code/tests and public development history

PRIVATE autonomous-data-science-system-private
    private continuity knowledge complement
    owns exact private facts deliberately delegated to it
    does not own ADS implementation evolution

PRIVATE autonomous-data-science-system-local-runtime
    versioned runtime/materialization evidence
    preserves non-secret local implementation bytes and deployment artifacts
    does not own current ADS project state or architectural acceptance

LOCAL public-checkout/.ads-private
    execution-ready machine-local materialization
    may be synchronized with the private runtime repository

SECRET STORAGE
    credentials and secrets
    never ordinary Git merely because a repository is private
```

When the runtime repository contains several historical candidates, the public ADS repository still determines which candidate was accepted/published and what experiment or checkpoint gives it meaning.

## Relationship to `.ads-private/`

The runtime repository should preserve an explicit tree corresponding to the local ignored material rather than silently becoming another public-project checkout.

Preferred shape:

```text
README.md
RUNTIME_STATE.json
.ads-private/
    codexless/
        ... non-secret candidate / activation / regression material ...
    ... other reviewed non-secret local state ...
```

The exact synchronization implementation may evolve, but it must keep provenance explicit. A file existing in the runtime repository is evidence that the file/version was preserved, not automatic evidence that it was the live accepted deployment.

## Single-owner semantics for private operational facts

Some local runtime files materialize facts whose durable semantic owner is the private companion repository.

Example:

```text
private companion
    owns the durable exact private Source Vault coordinates/observations

runtime repository snapshot of .ads-private/source_vault_bootstrap.json
    may preserve the exact execution-ready materialization/version
    does not become the semantic authority for those private facts
```

If the two disagree, reconcile explicitly. Do not treat the newest Git timestamp in the runtime repository as authority over the private companion or the public ADS state.

## What may be committed

Allowed examples include reviewed non-secret material such as:

```text
Codexless candidate source
focused regression scripts
activation/publication scripts
release/candidate hashes
runtime manifests
non-secret machine paths needed for reproducibility
non-secret permission/profile configuration
non-secret Source Vault execution coordinates when the governing private contract permits their private preservation
runtime experiment notes
```

Machine-specific information is not prohibited merely because it is machine-specific. The repository is private specifically so useful private/local implementation evidence can survive across machines and collaborators.

## What must never be committed

Never commit ordinary secrets or authentication material, including:

```text
passwords
API keys
OAuth/access/refresh tokens
GitHub tokens
browser cookies/session material
private keys
service-account credentials
encryption passwords or encryption keys
recovery codes
credential-manager exports
control-plane credentials
```

Private GitHub visibility is not a secrets manager.

The first import of `.ads-private` must therefore pass a deliberate sensitivity/secret audit before commit.

## Source Vault payload boundary

This repository is not Source Vault or backup storage.

Do not store:

```text
source PDFs/books/slides/datasets
Source Vault object bytes
registry database snapshots merely as backup payloads
encrypted or unencrypted bulk backup archives
```

Those remain governed by the Source Universe/Vault/backup architecture.

## Runtime synchronization manifest

The repository should maintain a machine-readable `RUNTIME_STATE.json` that can state, without becoming public ADS authority:

```text
schemaVersion
publicAdsCommit
publicAdsCheckpoint
capturedAt
runtime/candidate identity
important live/candidate file hashes
source local materialization class
```

The manifest is a synchronization/provenance pointer. It must not duplicate `CURRENT_STATE.md` or claim a later ADS state than the public authority supports.

## Git and authority policy

The private runtime repository should become a registered Codexless workspace under Research 116's two-layer model:

```text
Codex project/root trusted
+
Codexless workspace registry admits the exact root/capabilities
```

Once the stable multi-repository surface is accepted, ordinary repository operations should use the same bounded semantic Git contracts as other registered repositories rather than bespoke host commands.

Expected capabilities include:

```text
read
write
agent when explicitly useful
git_fetch
git_pull_ff_only
git_commit_paths
git_push_ff_only
```

Repository-specific integrity policy must include at least a secret/sensitivity gate and runtime-manifest/coherence verification before publication.

## Claude / multi-model access

One explicit purpose of the repository is to make actual ADS-local Codexless implementation evidence available to collaborators that cannot access the user's workstation directly.

For MC-0010, Claude should be able to inspect:

```text
public ADS repository
    project authority, architecture, research, validations, checkpoints

private local-runtime repository
    exact relevant Codexless candidate/runtime implementation evidence
```

Claude must not interpret private runtime code as accepted merely because it exists there. The public ADS evidence chain owns acceptance/status.

## Bootstrap sequence

The initial repository bootstrap is:

```text
1. establish flexible Codex/Codexless authority for the local clone
2. inventory the current .ads-private tree
3. run deliberate secret/sensitivity review
4. classify files as preserve / exclude / transform
5. populate the private runtime repository
6. create README + RUNTIME_STATE synchronization evidence
7. run runtime-repository integrity checks
8. commit and push through bounded semantic Git
9. update public ADS / MC-0010 routing to the exact private runtime boundary
```

Do not bulk-copy and push the directory before the sensitivity review.

## Continuity rule

A future collaborator should reconstruct in this order:

```text
public ADS authority first
    -> determine whether local-runtime evidence is relevant
    -> read private runtime repository when available
    -> read private companion when exact private continuity facts are relevant
    -> materialize/verify local .ads-private only when execution requires it
```

Loss or inaccessibility of the runtime repository must not cause the public project state to be downgraded or rewritten from memory.
