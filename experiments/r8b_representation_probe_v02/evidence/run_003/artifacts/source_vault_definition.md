# Permanent Source Vault Bootstrap Workstream

```toml project-meta
contract = "project-knowledge-carrier/1"
id = "WS-SOURCE-VAULT-BOOTSTRAP"
kind = "workstream-definition"
authority = "canonical"
lifecycle = "active"
subjects = ["permanent-source-vault-bootstrap", "source-universe"]
provenance = ["research:156", "research:157", "research:158", "research:168", "checkpoint:448", "checkpoint:544"]
declared_references = ["path:docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md", "path:docs/source_universe/validation/003_permanent_source_registry_migrated.md", "path:docs/source_universe/validation/004_permanent_first_corpus_prospective_compare_all_match.md", "path:docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md"]

[scope]
domain = "source-universe"
program = "permanent-source-vault-bootstrap"

[[relations]]
type = "governed-by"
target = "PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP"
```

## Objective

Complete the first permanent user-controlled Source Vault bootstrap and unblock Course 2 only after accepted recovery proof.

## Governing procedure

PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP

## Pause semantics

A PAUSED state is routing and does not by itself mean completion or supersession. Current pause/resume facts live in Project-system control state.

## Public/private boundary

The public source intentionally records only the public-safe private-dependency classification. Exact private paths, credentials, storage coordinates and other private execution values remain outside this public semantic source.

## Durable risk and reopen triggers

- RK-RECOVERY-FAILURE
- RK-REMOTE-ROUNDTRIP-FAILURE
- RK-PRIVATE-LEAK
