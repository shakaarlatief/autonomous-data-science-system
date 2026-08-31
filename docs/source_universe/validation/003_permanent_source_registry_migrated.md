# Permanent Source Registry Migration

**Date:** 2026-08-31  
**Status:** `PERMANENT_SOURCE_REGISTRY_MIGRATED_VERIFIED`  
**Scope:** Public-safe evidence for creation and verification of the clean permanent Source Registry before any first-corpus ingestion.

## Result

The clean permanent Source Registry has been created successfully at the previously resolved private location and migrated to the accepted Alembic head.

```text
Python runtime                 3.13.1
uv                             0.12.5
Alembic                        1.19.1
SQLAlchemy                     2.0.52
registry existed before step   NO
migration command              COMPLETED WITHOUT ERROR
Alembic revision               0003_source_universe (head)
SQLite table count             33
working tree after verify      CLEAN
source corpus ingested         NO
Source Vault artifact writes   NO
```

The local `uv` executable had been absent after machine cleanup. It was restored at the repository-pinned version `0.12.5` before the governed migration was run. The ADS Python environment remained healthy on Python 3.13.1 with the expected Alembic and SQLAlchemy versions.

## Schema verification

The resulting database reported `0003_source_universe` as the current Alembic revision and contained the full migrated V1 persistence schema:

```text
alembic_version
kg_asset
kg_asset_revision
kg_collection
kg_collection_member
kg_component
kg_component_revision
kg_content_revision
kg_content_revision_extension
kg_content_revision_provenance
kg_governance_event
kg_node
kg_provenance_source
kg_relation
kg_relation_current
kg_relation_governance_event
kg_relation_revision
kg_relation_revision_provenance
kg_relation_revision_state
kg_revision_governance
kg_rule_provenance
kg_rule_spec
prj_entity
prj_finding
prj_knowledge_ref
prj_project
src_artifact
src_collection
src_collection_membership
src_derived_artifact
src_ingestion_event
src_locator
src_source
```

The database file existed after migration and remained outside public Git. No exact private filesystem path, private database content, source binary, credential, or secret is preserved here.

## Gate interpretation

This closes the registry-migration step of the permanent bootstrap. It does not yet prove successful corpus ingestion, working-store integrity, independent backup, or disaster recovery.

The next governed action is prospective comparison of the original VU Amsterdam Machine Learning corpus against the reviewed first-corpus manifest and fingerprints before any source ingestion occurs.

```text
permanent registry migration      COMPLETE / VERIFIED
prospective first-corpus compare  NEXT
source ingestion                  BLOCKED pending comparison review
working-store audit               NOT YET RUN
independent encrypted backup      NOT YET VERIFIED
clean restore                     NOT YET VERIFIED
Course 2                          BLOCKED
```
