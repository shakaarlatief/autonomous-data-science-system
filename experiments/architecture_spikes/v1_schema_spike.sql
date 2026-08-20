-- V1 architecture falsification schema.
-- This is experiment code for Specification 001, not production DDL.

CREATE TABLE sys_schema_migration (
    version INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    checksum TEXT NOT NULL,
    applied_at TEXT NOT NULL
) STRICT;

CREATE TABLE kg_node (
    node_id TEXT PRIMARY KEY,
    node_type TEXT NOT NULL CHECK (node_type IN ('ASSET', 'COMPONENT')),
    created_at TEXT NOT NULL
) STRICT;

CREATE TABLE kg_content_revision (
    revision_id TEXT PRIMARY KEY,
    node_id TEXT NOT NULL REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    revision_no INTEGER NOT NULL CHECK (revision_no >= 1),
    created_at TEXT NOT NULL,
    semantic_content_hash TEXT NOT NULL,
    UNIQUE(node_id, revision_no),
    UNIQUE(node_id, revision_id)
) STRICT;

CREATE TABLE kg_asset (
    asset_id TEXT PRIMARY KEY REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    slug TEXT NOT NULL UNIQUE,
    current_accepted_revision_id TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY(asset_id, current_accepted_revision_id)
        REFERENCES kg_content_revision(node_id, revision_id)
        DEFERRABLE INITIALLY DEFERRED
) STRICT;

CREATE TABLE kg_revision_governance (
    revision_id TEXT PRIMARY KEY REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    current_status TEXT NOT NULL CHECK (current_status IN ('CANDIDATE','REVIEWED','ACCEPTED','SUPERSEDED','REJECTED')),
    updated_at TEXT NOT NULL
) STRICT;

CREATE TABLE kg_governance_event (
    event_id TEXT PRIMARY KEY,
    revision_id TEXT NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    from_status TEXT,
    to_status TEXT NOT NULL,
    actor TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    note_text TEXT
) STRICT;

CREATE TABLE kg_asset_revision (
    revision_id TEXT PRIMARY KEY REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    asset_id TEXT NOT NULL REFERENCES kg_asset(asset_id) ON DELETE RESTRICT,
    intrinsic_kind TEXT NOT NULL,
    title TEXT NOT NULL,
    purpose TEXT NOT NULL,
    scope_text TEXT,
    limitations_text TEXT,
    reasoning_traits_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(reasoning_traits_json)),
    retrieval_profile_json TEXT CHECK (retrieval_profile_json IS NULL OR json_valid(retrieval_profile_json)),
    applicability_spec_json TEXT CHECK (applicability_spec_json IS NULL OR json_valid(applicability_spec_json)),
    context_requirements_json TEXT CHECK (context_requirements_json IS NULL OR json_valid(context_requirements_json)),
    FOREIGN KEY(asset_id, revision_id)
        REFERENCES kg_content_revision(node_id, revision_id),
    UNIQUE(revision_id, asset_id)
) STRICT;

CREATE TABLE kg_component (
    component_id TEXT PRIMARY KEY REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    parent_asset_id TEXT NOT NULL REFERENCES kg_asset(asset_id) ON DELETE RESTRICT,
    component_key TEXT NOT NULL,
    component_kind TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(parent_asset_id, component_key),
    UNIQUE(component_id, parent_asset_id)
) STRICT;

CREATE TABLE kg_component_revision (
    revision_id TEXT PRIMARY KEY REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    component_id TEXT NOT NULL,
    parent_asset_id TEXT NOT NULL,
    parent_asset_revision_id TEXT NOT NULL,
    body_text TEXT,
    payload_json TEXT CHECK (payload_json IS NULL OR json_valid(payload_json)),
    position INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(component_id, revision_id)
        REFERENCES kg_content_revision(node_id, revision_id),
    FOREIGN KEY(component_id, parent_asset_id)
        REFERENCES kg_component(component_id, parent_asset_id),
    FOREIGN KEY(parent_asset_revision_id, parent_asset_id)
        REFERENCES kg_asset_revision(revision_id, asset_id),
    UNIQUE(revision_id, component_id)
) STRICT;

CREATE TABLE kg_relation (
    relation_id TEXT PRIMARY KEY,
    source_node_id TEXT NOT NULL REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    target_node_id TEXT NOT NULL REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    relation_type TEXT NOT NULL,
    current_accepted_revision_id TEXT,
    created_at TEXT NOT NULL,
    UNIQUE(relation_id, current_accepted_revision_id),
    FOREIGN KEY(relation_id, current_accepted_revision_id)
        REFERENCES kg_relation_revision(relation_id, relation_revision_id)
        DEFERRABLE INITIALLY DEFERRED
) STRICT;

CREATE TABLE kg_relation_revision (
    relation_revision_id TEXT PRIMARY KEY,
    relation_id TEXT NOT NULL REFERENCES kg_relation(relation_id) ON DELETE RESTRICT,
    revision_no INTEGER NOT NULL CHECK (revision_no >= 1),
    scope_text TEXT,
    rationale_text TEXT,
    created_at TEXT NOT NULL,
    UNIQUE(relation_id, revision_no),
    UNIQUE(relation_id, relation_revision_id)
) STRICT;

CREATE INDEX idx_kg_relation_source_type ON kg_relation(source_node_id, relation_type);
CREATE INDEX idx_kg_relation_target_type ON kg_relation(target_node_id, relation_type);

CREATE TABLE kg_rule_spec (
    rule_spec_id TEXT PRIMARY KEY,
    owner_content_revision_id TEXT NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    rule_key TEXT NOT NULL,
    condition_json TEXT NOT NULL CHECK (json_valid(condition_json)),
    consequence_type TEXT NOT NULL,
    consequence_payload_json TEXT CHECK (consequence_payload_json IS NULL OR json_valid(consequence_payload_json)),
    force TEXT NOT NULL CHECK (force IN ('HARD','STRONG','HEURISTIC','INFORMATIONAL')),
    unknown_behavior TEXT NOT NULL CHECK (unknown_behavior IN ('ASK','DEFER','BLOCK_DEPENDENT','NO_INFERENCE')),
    rationale_text TEXT,
    UNIQUE(owner_content_revision_id, rule_key)
) STRICT;

CREATE TABLE kg_provenance_source (
    source_id TEXT PRIMARY KEY,
    source_type TEXT NOT NULL,
    title TEXT,
    locator TEXT,
    metadata_json TEXT CHECK (metadata_json IS NULL OR json_valid(metadata_json))
) STRICT;

CREATE TABLE kg_content_revision_provenance (
    revision_id TEXT NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    source_id TEXT NOT NULL REFERENCES kg_provenance_source(source_id) ON DELETE RESTRICT,
    provenance_role TEXT NOT NULL,
    note_text TEXT,
    PRIMARY KEY(revision_id, source_id, provenance_role)
) STRICT;

CREATE TABLE prj_project (
    project_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    created_at TEXT NOT NULL
) STRICT;

CREATE TABLE prj_entity (
    entity_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES prj_project(project_id) ON DELETE CASCADE,
    entity_type TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(entity_id, project_id)
) STRICT;

CREATE TABLE prj_definition (
    definition_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    key TEXT NOT NULL,
    value_json TEXT NOT NULL CHECK (json_valid(value_json)),
    version_no INTEGER NOT NULL CHECK (version_no >= 1),
    updated_at TEXT NOT NULL,
    FOREIGN KEY(definition_id, project_id)
        REFERENCES prj_entity(entity_id, project_id) ON DELETE RESTRICT,
    UNIQUE(project_id, key)
) STRICT;

CREATE TABLE prj_question (
    question_id TEXT PRIMARY KEY REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    question_key TEXT,
    question_text TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('OPEN','RESOLVED','DEFERRED','BLOCKED')),
    created_at TEXT NOT NULL,
    resolved_at TEXT
) STRICT;

CREATE TABLE prj_evidence (
    evidence_id TEXT PRIMARY KEY REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    evidence_type TEXT NOT NULL,
    summary_text TEXT NOT NULL,
    payload_json TEXT CHECK (payload_json IS NULL OR json_valid(payload_json)),
    created_at TEXT NOT NULL
) STRICT;

CREATE TABLE prj_finding (
    finding_id TEXT PRIMARY KEY REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    finding_type TEXT NOT NULL,
    statement_text TEXT NOT NULL,
    created_at TEXT NOT NULL,
    superseded_by_finding_id TEXT REFERENCES prj_finding(finding_id) ON DELETE RESTRICT
) STRICT;

CREATE TABLE prj_criterion_finding (
    finding_id TEXT PRIMARY KEY REFERENCES prj_finding(finding_id) ON DELETE RESTRICT,
    subject_entity_id TEXT NOT NULL REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    criterion_knowledge_revision_id TEXT NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    verdict TEXT NOT NULL,
    conditions_json TEXT CHECK (conditions_json IS NULL OR json_valid(conditions_json)),
    rationale_text TEXT NOT NULL
) STRICT;

CREATE TABLE prj_finding_evidence (
    finding_id TEXT NOT NULL REFERENCES prj_finding(finding_id) ON DELETE RESTRICT,
    evidence_id TEXT NOT NULL REFERENCES prj_evidence(evidence_id) ON DELETE RESTRICT,
    PRIMARY KEY(finding_id, evidence_id)
) STRICT;

CREATE TABLE prj_decision (
    decision_id TEXT PRIMARY KEY REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    decision_type TEXT NOT NULL,
    action_text TEXT NOT NULL,
    rationale_text TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('PROPOSED','ACCEPTED','REJECTED','SUPERSEDED')),
    created_at TEXT NOT NULL
) STRICT;

CREATE TABLE prj_decision_support (
    decision_id TEXT NOT NULL REFERENCES prj_decision(decision_id) ON DELETE RESTRICT,
    finding_id TEXT NOT NULL REFERENCES prj_finding(finding_id) ON DELETE RESTRICT,
    PRIMARY KEY(decision_id, finding_id)
) STRICT;

CREATE TABLE prj_knowledge_ref (
    ref_id TEXT PRIMARY KEY,
    project_entity_id TEXT NOT NULL REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    knowledge_revision_id TEXT NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    reference_type TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(project_entity_id, knowledge_revision_id, reference_type)
) STRICT;

CREATE TABLE prj_event (
    event_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES prj_project(project_id) ON DELETE CASCADE,
    entity_id TEXT REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    payload_json TEXT CHECK (payload_json IS NULL OR json_valid(payload_json))
) STRICT;

CREATE TABLE prj_rule_trace (
    trace_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES prj_project(project_id) ON DELETE CASCADE,
    rule_spec_id TEXT NOT NULL REFERENCES kg_rule_spec(rule_spec_id) ON DELETE RESTRICT,
    aggregate_result TEXT NOT NULL CHECK (aggregate_result IN ('TRUE','FALSE','UNKNOWN')),
    predicate_outcomes_json TEXT NOT NULL CHECK (json_valid(predicate_outcomes_json)),
    consequence_type TEXT,
    consequence_payload_json TEXT CHECK (consequence_payload_json IS NULL OR json_valid(consequence_payload_json)),
    evaluator_version TEXT NOT NULL,
    created_at TEXT NOT NULL
) STRICT;

CREATE TABLE idx_search_document (
    asset_id TEXT NOT NULL REFERENCES kg_asset(asset_id) ON DELETE CASCADE,
    revision_id TEXT NOT NULL REFERENCES kg_asset_revision(revision_id) ON DELETE CASCADE,
    document_schema_version INTEGER NOT NULL,
    canonical_text TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    PRIMARY KEY(asset_id, revision_id)
) STRICT;

CREATE VIRTUAL TABLE idx_knowledge_fts USING fts5(
    asset_id UNINDEXED,
    revision_id UNINDEXED,
    title,
    body
);

CREATE TABLE idx_embedding (
    revision_id TEXT NOT NULL REFERENCES kg_asset_revision(revision_id) ON DELETE CASCADE,
    embedding_model_key TEXT NOT NULL,
    embedding_schema_version INTEGER NOT NULL,
    content_hash TEXT NOT NULL,
    dimension INTEGER NOT NULL,
    vector_blob BLOB NOT NULL,
    created_at TEXT NOT NULL,
    PRIMARY KEY(revision_id, embedding_model_key, embedding_schema_version)
) STRICT;
