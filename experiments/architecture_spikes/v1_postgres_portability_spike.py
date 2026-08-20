"""PostgreSQL portability gate for Specification 001 / FT-12.

This is not a PostgreSQL V1 implementation. It verifies that the core SQLite
architecture maps to PostgreSQL without redesigning durable identity, revision
history, project-to-knowledge references, relations, or stored rule semantics.
"""

from __future__ import annotations

import json
import os
import uuid
from datetime import datetime, timezone

import psycopg


DDL = r"""
CREATE TABLE kg_node (
    node_id uuid PRIMARY KEY,
    node_type text NOT NULL CHECK (node_type IN ('ASSET','COMPONENT')),
    created_at timestamptz NOT NULL
);

CREATE TABLE kg_content_revision (
    revision_id uuid PRIMARY KEY,
    node_id uuid NOT NULL REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    revision_no integer NOT NULL CHECK (revision_no >= 1),
    created_at timestamptz NOT NULL,
    semantic_content_hash text NOT NULL,
    UNIQUE(node_id, revision_no),
    UNIQUE(node_id, revision_id)
);

CREATE TABLE kg_asset (
    asset_id uuid PRIMARY KEY REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    slug text NOT NULL UNIQUE,
    current_accepted_revision_id uuid,
    created_at timestamptz NOT NULL
);

CREATE TABLE kg_asset_revision (
    revision_id uuid PRIMARY KEY REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    asset_id uuid NOT NULL REFERENCES kg_asset(asset_id) ON DELETE RESTRICT,
    intrinsic_kind text NOT NULL,
    title text NOT NULL,
    purpose text NOT NULL,
    scope_text text,
    limitations_text text,
    reasoning_traits_json jsonb NOT NULL DEFAULT '[]'::jsonb,
    retrieval_profile_json jsonb,
    applicability_spec_json jsonb,
    context_requirements_json jsonb,
    FOREIGN KEY(asset_id, revision_id)
        REFERENCES kg_content_revision(node_id, revision_id),
    UNIQUE(revision_id, asset_id)
);

ALTER TABLE kg_asset ADD CONSTRAINT fk_asset_current_revision
    FOREIGN KEY(asset_id, current_accepted_revision_id)
    REFERENCES kg_content_revision(node_id, revision_id)
    DEFERRABLE INITIALLY DEFERRED;

CREATE TABLE kg_component (
    component_id uuid PRIMARY KEY REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    parent_asset_id uuid NOT NULL REFERENCES kg_asset(asset_id) ON DELETE RESTRICT,
    component_key text NOT NULL,
    component_kind text NOT NULL,
    created_at timestamptz NOT NULL,
    UNIQUE(parent_asset_id, component_key),
    UNIQUE(component_id, parent_asset_id)
);

CREATE TABLE kg_component_revision (
    revision_id uuid PRIMARY KEY REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    component_id uuid NOT NULL,
    parent_asset_id uuid NOT NULL,
    parent_asset_revision_id uuid NOT NULL,
    body_text text,
    payload_json jsonb,
    position integer NOT NULL DEFAULT 0,
    FOREIGN KEY(component_id, revision_id)
        REFERENCES kg_content_revision(node_id, revision_id),
    FOREIGN KEY(component_id, parent_asset_id)
        REFERENCES kg_component(component_id, parent_asset_id),
    FOREIGN KEY(parent_asset_revision_id, parent_asset_id)
        REFERENCES kg_asset_revision(revision_id, asset_id),
    UNIQUE(revision_id, component_id)
);

CREATE TABLE kg_relation (
    relation_id uuid PRIMARY KEY,
    source_node_id uuid NOT NULL REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    target_node_id uuid NOT NULL REFERENCES kg_node(node_id) ON DELETE RESTRICT,
    relation_type text NOT NULL,
    created_at timestamptz NOT NULL
);

CREATE INDEX idx_kg_relation_source_type ON kg_relation(source_node_id, relation_type);
CREATE INDEX idx_kg_relation_target_type ON kg_relation(target_node_id, relation_type);

CREATE TABLE kg_rule_spec (
    rule_spec_id uuid PRIMARY KEY,
    owner_content_revision_id uuid NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    rule_key text NOT NULL,
    condition_json jsonb NOT NULL,
    consequence_type text NOT NULL,
    consequence_payload_json jsonb,
    force text NOT NULL,
    unknown_behavior text NOT NULL,
    rationale_text text,
    UNIQUE(owner_content_revision_id, rule_key)
);

CREATE TABLE prj_project (
    project_id uuid PRIMARY KEY,
    title text NOT NULL,
    created_at timestamptz NOT NULL
);

CREATE TABLE prj_entity (
    entity_id uuid PRIMARY KEY,
    project_id uuid NOT NULL REFERENCES prj_project(project_id) ON DELETE CASCADE,
    entity_type text NOT NULL,
    created_at timestamptz NOT NULL,
    UNIQUE(entity_id, project_id)
);

CREATE TABLE prj_knowledge_ref (
    ref_id uuid PRIMARY KEY,
    project_entity_id uuid NOT NULL REFERENCES prj_entity(entity_id) ON DELETE RESTRICT,
    knowledge_revision_id uuid NOT NULL REFERENCES kg_content_revision(revision_id) ON DELETE RESTRICT,
    reference_type text NOT NULL,
    created_at timestamptz NOT NULL,
    UNIQUE(project_entity_id, knowledge_revision_id, reference_type)
);
"""


def main() -> int:
    dsn = os.environ["ADS_POSTGRES_DSN"]
    now = datetime.now(timezone.utc)

    with psycopg.connect(dsn, autocommit=True) as con:
        with con.cursor() as cur:
            for table in (
                "prj_knowledge_ref",
                "prj_entity",
                "prj_project",
                "kg_rule_spec",
                "kg_relation",
                "kg_component_revision",
                "kg_component",
                "kg_asset_revision",
                "kg_asset",
                "kg_content_revision",
                "kg_node",
            ):
                cur.execute(f"DROP TABLE IF EXISTS {table} CASCADE")

            cur.execute(DDL)

            asset_id = uuid.uuid4()
            asset_revision = uuid.uuid4()
            component_id = uuid.uuid4()
            component_revision = uuid.uuid4()
            related_asset = uuid.uuid4()
            related_revision = uuid.uuid4()

            cur.execute("INSERT INTO kg_node VALUES (%s,%s,%s)", (asset_id, "ASSET", now))
            cur.execute("INSERT INTO kg_asset(asset_id,slug,current_accepted_revision_id,created_at) VALUES (%s,%s,NULL,%s)", (asset_id, "missing-data", now))
            cur.execute("INSERT INTO kg_content_revision VALUES (%s,%s,%s,%s,%s)", (asset_revision, asset_id, 1, now, "asset-hash"))
            cur.execute(
                """INSERT INTO kg_asset_revision(
                    revision_id,asset_id,intrinsic_kind,title,purpose,reasoning_traits_json
                ) VALUES (%s,%s,%s,%s,%s,%s::jsonb)""",
                (asset_revision, asset_id, "FRAMEWORK", "Missing Data", "Reason about missingness.", "[]"),
            )
            cur.execute("UPDATE kg_asset SET current_accepted_revision_id=%s WHERE asset_id=%s", (asset_revision, asset_id))

            cur.execute("INSERT INTO kg_node VALUES (%s,%s,%s)", (component_id, "COMPONENT", now))
            cur.execute("INSERT INTO kg_component VALUES (%s,%s,%s,%s,%s)", (component_id, asset_id, "production-missingness", "QUESTION", now))
            cur.execute("INSERT INTO kg_content_revision VALUES (%s,%s,%s,%s,%s)", (component_revision, component_id, 1, now, "component-hash"))
            cur.execute(
                """INSERT INTO kg_component_revision(
                    revision_id,component_id,parent_asset_id,parent_asset_revision_id,body_text,payload_json,position
                ) VALUES (%s,%s,%s,%s,%s,%s::jsonb,%s)""",
                (component_revision, component_id, asset_id, asset_revision, "Will missingness occur in production?", json.dumps({"kind": "question"}), 0),
            )

            cur.execute("INSERT INTO kg_node VALUES (%s,%s,%s)", (related_asset, "ASSET", now))
            cur.execute("INSERT INTO kg_asset(asset_id,slug,current_accepted_revision_id,created_at) VALUES (%s,%s,NULL,%s)", (related_asset, "information-legitimacy", now))
            cur.execute("INSERT INTO kg_content_revision VALUES (%s,%s,%s,%s,%s)", (related_revision, related_asset, 1, now, "related-hash"))
            cur.execute(
                "INSERT INTO kg_asset_revision(revision_id,asset_id,intrinsic_kind,title,purpose,reasoning_traits_json) VALUES (%s,%s,%s,%s,%s,%s::jsonb)",
                (related_revision, related_asset, "FRAMEWORK", "Information Legitimacy", "Govern legitimate information use.", "[]"),
            )
            cur.execute("UPDATE kg_asset SET current_accepted_revision_id=%s WHERE asset_id=%s", (related_revision, related_asset))

            relation_id = uuid.uuid4()
            cur.execute("INSERT INTO kg_relation VALUES (%s,%s,%s,%s,%s)", (relation_id, asset_id, related_asset, "GOVERNED_BY", now))

            rule_id = uuid.uuid4()
            condition = {"predicate": "project.definition.equals", "args": {"key": "production_missingness", "value": True}}
            cur.execute(
                """INSERT INTO kg_rule_spec(
                    rule_spec_id,owner_content_revision_id,rule_key,condition_json,consequence_type,
                    consequence_payload_json,force,unknown_behavior,rationale_text
                ) VALUES (%s,%s,%s,%s::jsonb,%s,%s::jsonb,%s,%s,%s)""",
                (
                    rule_id,
                    asset_revision,
                    "production-missingness",
                    json.dumps(condition),
                    "RECOMMEND_OPTION",
                    json.dumps({"strategy": "retain_missingness"}),
                    "STRONG",
                    "ASK",
                    "Portability gate",
                ),
            )

            project_id = uuid.uuid4()
            finding_id = uuid.uuid4()
            ref_id = uuid.uuid4()
            cur.execute("INSERT INTO prj_project VALUES (%s,%s,%s)", (project_id, "Portability Project", now))
            cur.execute("INSERT INTO prj_entity VALUES (%s,%s,%s,%s)", (finding_id, project_id, "FINDING", now))
            cur.execute("INSERT INTO prj_knowledge_ref VALUES (%s,%s,%s,%s,%s)", (ref_id, finding_id, asset_revision, "CRITERION", now))

            cur.execute("SELECT current_accepted_revision_id FROM kg_asset WHERE asset_id=%s", (asset_id,))
            assert cur.fetchone()[0] == asset_revision

            cur.execute("SELECT knowledge_revision_id FROM prj_knowledge_ref WHERE project_entity_id=%s", (finding_id,))
            assert cur.fetchone()[0] == asset_revision

            cur.execute("SELECT condition_json,consequence_payload_json FROM kg_rule_spec WHERE rule_spec_id=%s", (rule_id,))
            condition_json, consequence_json = cur.fetchone()
            assert condition_json["predicate"] == "project.definition.equals"
            assert consequence_json["strategy"] == "retain_missingness"

            cur.execute("SELECT COUNT(*) FROM kg_relation WHERE source_node_id=%s AND relation_type='GOVERNED_BY'", (asset_id,))
            assert cur.fetchone()[0] == 1

    print("FT-12: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
