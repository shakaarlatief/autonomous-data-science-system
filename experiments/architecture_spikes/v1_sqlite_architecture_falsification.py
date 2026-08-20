"""Narrow SQLite architecture falsification harness for Specification 001.

This is experimental code, not production V1 implementation. It verifies the
SQLite-side architecture contracts FT-01 through FT-11. FT-12 is exercised by
a separate PostgreSQL portability spike.
"""

from __future__ import annotations

import array
import hashlib
import json
import math
import sqlite3
import tempfile
import threading
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE / "v1_schema_spike.sql"
MODEL_KEY = "toy-semantic-v1"


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def new_id() -> str:
    # UUIDv4 keeps this spike compatible with Python versions lacking uuid.uuid7().
    # Specification 001 prefers UUIDv7 for the eventual application layer.
    return str(uuid.uuid4())


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def connect(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(path, timeout=5.0, isolation_level=None, check_same_thread=False)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA journal_mode = WAL")
    con.execute("PRAGMA synchronous = FULL")
    con.execute("PRAGMA busy_timeout = 5000")
    return con


def initialize(con: sqlite3.Connection) -> None:
    schema = SCHEMA_PATH.read_text(encoding="utf-8")
    con.executescript(schema)
    con.execute(
        "INSERT INTO sys_schema_migration(version,name,checksum,applied_at) VALUES (1,?,?,?)",
        ("v1_schema_spike", sha256_text(schema), now_utc()),
    )


def add_node(con: sqlite3.Connection, node_type: str) -> str:
    node_id = new_id()
    con.execute(
        "INSERT INTO kg_node(node_id,node_type,created_at) VALUES (?,?,?)",
        (node_id, node_type, now_utc()),
    )
    return node_id


def create_asset(con: sqlite3.Connection, slug: str) -> str:
    asset_id = add_node(con, "ASSET")
    con.execute(
        "INSERT INTO kg_asset(asset_id,slug,current_accepted_revision_id,created_at) VALUES (?,?,NULL,?)",
        (asset_id, slug, now_utc()),
    )
    return asset_id


def publish_asset_revision(
    con: sqlite3.Connection,
    asset_id: str,
    *,
    kind: str,
    title: str,
    purpose: str,
    scope: str = "",
    fail_after_insert: bool = False,
) -> str:
    next_no = con.execute(
        "SELECT COALESCE(MAX(revision_no),0)+1 FROM kg_content_revision WHERE node_id=?",
        (asset_id,),
    ).fetchone()[0]
    revision_id = new_id()
    content_hash = sha256_text(canonical_json({"kind": kind, "title": title, "purpose": purpose, "scope": scope}))

    con.execute("BEGIN IMMEDIATE")
    try:
        con.execute(
            "INSERT INTO kg_content_revision VALUES (?,?,?,?,?)",
            (revision_id, asset_id, next_no, now_utc(), content_hash),
        )
        con.execute(
            """INSERT INTO kg_asset_revision(
                revision_id,asset_id,intrinsic_kind,title,purpose,scope_text,reasoning_traits_json
            ) VALUES (?,?,?,?,?,?,?)""",
            (revision_id, asset_id, kind, title, purpose, scope, "[]"),
        )
        con.execute(
            "INSERT INTO kg_revision_governance VALUES (?,?,?)",
            (revision_id, "ACCEPTED", now_utc()),
        )
        con.execute(
            "INSERT INTO kg_governance_event VALUES (?,?,?,?,?,?,?)",
            (new_id(), revision_id, None, "ACCEPTED", "spike", now_utc(), "publication"),
        )
        if fail_after_insert:
            raise RuntimeError("injected publication failure")

        old = con.execute(
            "SELECT current_accepted_revision_id FROM kg_asset WHERE asset_id=?", (asset_id,)
        ).fetchone()[0]
        con.execute(
            "UPDATE kg_asset SET current_accepted_revision_id=? WHERE asset_id=?",
            (revision_id, asset_id),
        )
        if old:
            con.execute(
                "UPDATE kg_revision_governance SET current_status='SUPERSEDED',updated_at=? WHERE revision_id=?",
                (now_utc(), old),
            )
            con.execute(
                "INSERT INTO kg_governance_event VALUES (?,?,?,?,?,?,?)",
                (new_id(), old, "ACCEPTED", "SUPERSEDED", "spike", now_utc(), "new accepted revision"),
            )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise

    refresh_search_document(con, asset_id, revision_id)
    return revision_id


def create_component(
    con: sqlite3.Connection,
    asset_id: str,
    asset_revision_id: str,
    key: str,
    kind: str,
    body: str,
) -> str:
    component_id = add_node(con, "COMPONENT")
    component_revision_id = new_id()
    con.execute(
        "INSERT INTO kg_component VALUES (?,?,?,?,?)",
        (component_id, asset_id, key, kind, now_utc()),
    )
    con.execute(
        "INSERT INTO kg_content_revision VALUES (?,?,?,?,?)",
        (component_revision_id, component_id, 1, now_utc(), sha256_text(body)),
    )
    con.execute(
        "INSERT INTO kg_component_revision VALUES (?,?,?,?,?,?,?)",
        (component_revision_id, component_id, asset_id, asset_revision_id, body, None, 0),
    )
    con.execute(
        "INSERT INTO kg_revision_governance VALUES (?,?,?)",
        (component_revision_id, "ACCEPTED", now_utc()),
    )
    return component_id


def create_relation(
    con: sqlite3.Connection,
    source_node: str,
    target_node: str,
    relation_type: str,
    rationale: str,
) -> str:
    relation_id, revision_id = new_id(), new_id()
    con.execute("BEGIN IMMEDIATE")
    try:
        con.execute(
            "INSERT INTO kg_relation VALUES (?,?,?,?,NULL,?)",
            (relation_id, source_node, target_node, relation_type, now_utc()),
        )
        con.execute(
            "INSERT INTO kg_relation_revision VALUES (?,?,?,?,?,?)",
            (revision_id, relation_id, 1, None, rationale, now_utc()),
        )
        con.execute(
            "UPDATE kg_relation SET current_accepted_revision_id=? WHERE relation_id=?",
            (revision_id, relation_id),
        )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    return relation_id


def add_rule(
    con: sqlite3.Connection,
    owner_revision: str,
    key: str,
    condition: dict[str, Any],
    consequence_type: str,
    consequence_payload: dict[str, Any],
    force: str,
    unknown_behavior: str,
) -> str:
    rule_id = new_id()
    con.execute(
        """INSERT INTO kg_rule_spec(
            rule_spec_id,owner_content_revision_id,rule_key,condition_json,consequence_type,
            consequence_payload_json,force,unknown_behavior,rationale_text
        ) VALUES (?,?,?,?,?,?,?,?,?)""",
        (
            rule_id,
            owner_revision,
            key,
            canonical_json(condition),
            consequence_type,
            canonical_json(consequence_payload),
            force,
            unknown_behavior,
            "architecture spike",
        ),
    )
    return rule_id


def refresh_search_document(con: sqlite3.Connection, asset_id: str, revision_id: str) -> None:
    row = con.execute(
        "SELECT title,purpose,COALESCE(scope_text,'') FROM kg_asset_revision WHERE revision_id=?",
        (revision_id,),
    ).fetchone()
    component_text = "\n".join(
        r[0]
        for r in con.execute(
            "SELECT COALESCE(body_text,'') FROM kg_component_revision WHERE parent_asset_revision_id=? ORDER BY position",
            (revision_id,),
        )
    )
    title = row["title"]
    body = "\n".join(x for x in [row["purpose"], row[2], component_text] if x)
    digest = sha256_text(title + "\n" + body)
    con.execute("DELETE FROM idx_search_document WHERE asset_id=?", (asset_id,))
    con.execute(
        "INSERT INTO idx_search_document VALUES (?,?,?,?,?)",
        (asset_id, revision_id, 1, title + "\n" + body, digest),
    )
    con.execute("DELETE FROM idx_knowledge_fts WHERE asset_id=?", (asset_id,))
    con.execute(
        "INSERT INTO idx_knowledge_fts(asset_id,revision_id,title,body) VALUES (?,?,?,?)",
        (asset_id, revision_id, title, body),
    )


def rebuild_search(con: sqlite3.Connection) -> None:
    con.execute("DELETE FROM idx_search_document")
    con.execute("DELETE FROM idx_knowledge_fts")
    for row in con.execute(
        "SELECT asset_id,current_accepted_revision_id FROM kg_asset WHERE current_accepted_revision_id IS NOT NULL"
    ):
        refresh_search_document(con, row["asset_id"], row["current_accepted_revision_id"])


def fts_ids(con: sqlite3.Connection, query: str, limit: int = 5) -> set[str]:
    return {
        row["asset_id"]
        for row in con.execute(
            """SELECT asset_id FROM idx_knowledge_fts
               WHERE idx_knowledge_fts MATCH ? ORDER BY bm25(idx_knowledge_fts) LIMIT ?""",
            (query, limit),
        )
    }


SYNONYMS = {
    "unequal": "imbalance",
    "minority": "imbalance",
    "future": "temporal",
    "chronological": "temporal",
    "unavailable": "eligibility",
    "leakage": "eligibility",
    "null": "missing",
    "nan": "missing",
    "distribution": "histogram",
}


def tokens(text: str) -> list[str]:
    normalized = "".join(c if c.isalnum() else " " for c in text.lower())
    return [SYNONYMS.get(token, token) for token in normalized.split() if token]


def toy_embedding(text: str, dimension: int = 64) -> list[float]:
    vec = [0.0] * dimension
    for token in tokens(text):
        digest = int(hashlib.sha256(token.encode()).hexdigest(), 16)
        vec[digest % dimension] += 1.0 if ((digest >> 8) & 1) == 0 else -1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def pack_vector(values: list[float]) -> bytes:
    return array.array("f", values).tobytes()


def unpack_vector(blob: bytes) -> list[float]:
    values = array.array("f")
    values.frombytes(blob)
    return list(values)


def rebuild_embeddings(con: sqlite3.Connection) -> None:
    con.execute("DELETE FROM idx_embedding WHERE embedding_model_key=?", (MODEL_KEY,))
    for row in con.execute("SELECT revision_id,canonical_text,content_hash FROM idx_search_document"):
        vector = toy_embedding(row["canonical_text"])
        con.execute(
            "INSERT INTO idx_embedding VALUES (?,?,?,?,?,?,?)",
            (row["revision_id"], MODEL_KEY, 1, row["content_hash"], len(vector), pack_vector(vector), now_utc()),
        )


def semantic_ids(con: sqlite3.Connection, query: str, limit: int = 5) -> set[str]:
    q = toy_embedding(query)
    scores: list[tuple[str, float]] = []
    for row in con.execute(
        """SELECT a.asset_id,e.vector_blob FROM kg_asset a
           JOIN idx_embedding e ON e.revision_id=a.current_accepted_revision_id
           WHERE e.embedding_model_key=?""",
        (MODEL_KEY,),
    ):
        score = sum(a * b for a, b in zip(q, unpack_vector(row["vector_blob"])))
        scores.append((row["asset_id"], score))
    scores.sort(key=lambda item: item[1], reverse=True)
    return {asset_id for asset_id, _ in scores[:limit]}


def embedding_health(con: sqlite3.Connection) -> tuple[int, int, int]:
    healthy = missing = stale = 0
    for row in con.execute(
        """SELECT a.current_accepted_revision_id revision_id,s.content_hash
           FROM kg_asset a JOIN idx_search_document s ON s.revision_id=a.current_accepted_revision_id"""
    ):
        emb = con.execute(
            "SELECT content_hash FROM idx_embedding WHERE revision_id=? AND embedding_model_key=?",
            (row["revision_id"], MODEL_KEY),
        ).fetchone()
        if emb is None:
            missing += 1
        elif emb[0] != row["content_hash"]:
            stale += 1
        else:
            healthy += 1
    return healthy, missing, stale


def create_project(con: sqlite3.Connection) -> str:
    project_id = new_id()
    con.execute("INSERT INTO prj_project VALUES (?,?,?)", (project_id, "Architecture Spike", now_utc()))
    return project_id


def create_entity(con: sqlite3.Connection, project_id: str, entity_type: str) -> str:
    entity_id = new_id()
    con.execute("INSERT INTO prj_entity VALUES (?,?,?,?)", (entity_id, project_id, entity_type, now_utc()))
    return entity_id


def set_definition(con: sqlite3.Connection, project_id: str, key: str, value: Any) -> str:
    row = con.execute(
        "SELECT definition_id FROM prj_definition WHERE project_id=? AND key=?", (project_id, key)
    ).fetchone()
    if row:
        definition_id = row[0]
        con.execute(
            "UPDATE prj_definition SET value_json=?,version_no=version_no+1,updated_at=? WHERE definition_id=?",
            (canonical_json(value), now_utc(), definition_id),
        )
        return definition_id
    definition_id = create_entity(con, project_id, "DEFINITION")
    con.execute(
        "INSERT INTO prj_definition VALUES (?,?,?,?,?,?)",
        (definition_id, project_id, key, canonical_json(value), 1, now_utc()),
    )
    return definition_id


def get_definition(con: sqlite3.Connection, project_id: str, key: str) -> tuple[bool, Any]:
    row = con.execute(
        "SELECT value_json FROM prj_definition WHERE project_id=? AND key=?", (project_id, key)
    ).fetchone()
    return (False, None) if row is None else (True, json.loads(row[0]))


Predicate = Callable[[sqlite3.Connection, str, dict[str, Any]], str]


def definition_equals(con: sqlite3.Connection, project_id: str, args: dict[str, Any]) -> str:
    found, value = get_definition(con, project_id, args["key"])
    if not found:
        return "UNKNOWN"
    return "TRUE" if value == args["value"] else "FALSE"


PREDICATES: dict[str, Predicate] = {"project.definition.equals": definition_equals}


@dataclass
class EvalResult:
    result: str
    outcomes: list[dict[str, Any]]


def evaluate_condition(con: sqlite3.Connection, project_id: str, condition: dict[str, Any]) -> EvalResult:
    if "predicate" in condition:
        name = condition["predicate"]
        result = PREDICATES[name](con, project_id, condition.get("args", {}))
        return EvalResult(result, [{"predicate": name, "args": condition.get("args", {}), "result": result}])
    if "all" in condition:
        parts = [evaluate_condition(con, project_id, child) for child in condition["all"]]
        values = [part.result for part in parts]
        result = "FALSE" if "FALSE" in values else ("UNKNOWN" if "UNKNOWN" in values else "TRUE")
        return EvalResult(result, [item for part in parts for item in part.outcomes])
    if "any" in condition:
        parts = [evaluate_condition(con, project_id, child) for child in condition["any"]]
        values = [part.result for part in parts]
        result = "TRUE" if "TRUE" in values else ("UNKNOWN" if "UNKNOWN" in values else "FALSE")
        return EvalResult(result, [item for part in parts for item in part.outcomes])
    if "not" in condition:
        part = evaluate_condition(con, project_id, condition["not"])
        return EvalResult({"TRUE": "FALSE", "FALSE": "TRUE", "UNKNOWN": "UNKNOWN"}[part.result], part.outcomes)
    raise ValueError(f"Unsupported condition: {condition}")


def evaluate_rule(con: sqlite3.Connection, project_id: str, rule_id: str) -> dict[str, Any]:
    row = con.execute("SELECT * FROM kg_rule_spec WHERE rule_spec_id=?", (rule_id,)).fetchone()
    evaluated = evaluate_condition(con, project_id, json.loads(row["condition_json"]))
    consequence_type = None
    consequence_payload = None
    if evaluated.result == "TRUE":
        consequence_type = row["consequence_type"]
        consequence_payload = json.loads(row["consequence_payload_json"])
    elif evaluated.result == "UNKNOWN":
        if row["unknown_behavior"] == "ASK":
            consequence_type = "OPEN_QUESTION"
            consequence_payload = {"reason": "required context unresolved"}
        elif row["unknown_behavior"] == "BLOCK_DEPENDENT":
            consequence_type = "BLOCK_DEPENDENT"
    trace_id = new_id()
    con.execute(
        "INSERT INTO prj_rule_trace VALUES (?,?,?,?,?,?,?,?,?)",
        (
            trace_id,
            project_id,
            rule_id,
            evaluated.result,
            canonical_json(evaluated.outcomes),
            consequence_type,
            canonical_json(consequence_payload) if consequence_payload else None,
            "spike-evaluator-v1",
            now_utc(),
        ),
    )
    return {"result": evaluated.result, "consequence_type": consequence_type}


def integrity(con: sqlite3.Connection) -> None:
    assert con.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    assert con.execute("PRAGMA foreign_key_check").fetchall() == []


def seed_catalog(con: sqlite3.Connection) -> dict[str, dict[str, str]]:
    specifications = [
        ("histogram", "METHOD", "Histogram", "Visualize empirical numeric distribution.", "distribution bins skew numeric"),
        ("missing-data", "FRAMEWORK", "Missing Data", "Reason about missing values, production missingness and labels.", "missing null production imputation labels"),
        ("temporal-validation", "FRAMEWORK", "Temporal Validation", "Design evaluation for future temporal generalization.", "time future chronological rolling validation"),
        ("random-forest", "METHOD", "Random Forest", "Tree ensemble using bagging and feature randomness.", "bagging trees nonlinear interactions"),
        ("feature-eligibility", "RULE", "Prediction-Time Feature Eligibility", "Require features to exist at prediction time.", "availability leakage future eligibility"),
        ("class-imbalance", "FRAMEWORK", "Class Imbalance", "Reason about unequal prevalence and minority performance.", "imbalance minority prevalence metric threshold"),
        ("pca", "METHOD", "Principal Component Analysis", "Linear dimensionality reduction.", "dimension variance orthogonal"),
        ("kmeans", "METHOD", "K-Means", "Centroid-based clustering.", "cluster centroid unsupervised"),
        ("qqplot", "METHOD", "Q-Q Plot", "Compare empirical and reference quantiles.", "quantiles normality diagnostic"),
    ]
    catalog: dict[str, dict[str, str]] = {}
    for slug, kind, title, purpose, scope in specifications:
        asset_id = create_asset(con, slug)
        revision_id = publish_asset_revision(con, asset_id, kind=kind, title=title, purpose=purpose, scope=scope)
        catalog[slug] = {"asset_id": asset_id, "revision_id": revision_id}
    return catalog


def run() -> dict[str, str]:
    results: dict[str, str] = {}
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "architecture_spike.sqlite"
        con = connect(db_path)
        initialize(con)
        catalog = seed_catalog(con)
        project_id = create_project(con)

        # FT-01: historical knowledge revision pinning.
        missing = catalog["missing-data"]
        question_id = create_entity(con, project_id, "QUESTION")
        con.execute(
            "INSERT INTO prj_question VALUES (?,?,?,?,?,NULL)",
            (question_id, "missing-data", "How should missingness be handled?", "OPEN", now_utc()),
        )
        r1 = missing["revision_id"]
        r1_hash = con.execute("SELECT semantic_content_hash FROM kg_content_revision WHERE revision_id=?", (r1,)).fetchone()[0]
        con.execute(
            "INSERT INTO prj_knowledge_ref VALUES (?,?,?,?,?)",
            (new_id(), question_id, r1, "INFORMED_BY", now_utc()),
        )
        r2 = publish_asset_revision(
            con,
            missing["asset_id"],
            kind="FRAMEWORK",
            title="Missing Data",
            purpose="Reason about missingness with production and claim constraints.",
            scope="missing values production imputation labels sensitivity",
        )
        missing["revision_id"] = r2
        assert con.execute("SELECT current_accepted_revision_id FROM kg_asset WHERE asset_id=?", (missing["asset_id"],)).fetchone()[0] == r2
        assert con.execute("SELECT knowledge_revision_id FROM prj_knowledge_ref WHERE project_entity_id=?", (question_id,)).fetchone()[0] == r1
        assert con.execute("SELECT semantic_content_hash FROM kg_content_revision WHERE revision_id=?", (r1,)).fetchone()[0] == r1_hash
        results["FT-01"] = "PASS"

        # FT-02: component/relation integrity and bounded traversal.
        rf = catalog["random-forest"]
        mechanism = create_component(con, rf["asset_id"], rf["revision_id"], "mechanism", "MECHANISM", "Bootstrap rows, randomize candidate features, aggregate trees.")
        bagging_asset = create_asset(con, "bagging")
        bagging_revision = publish_asset_revision(con, bagging_asset, kind="CONCEPT", title="Bagging", purpose="Aggregate learners over bootstrap samples.", scope="ensemble variance reduction")
        catalog["bagging"] = {"asset_id": bagging_asset, "revision_id": bagging_revision}
        create_relation(con, rf["asset_id"], bagging_asset, "USES_ENSEMBLE_PRINCIPLE", "Random Forest uses bagging.")
        create_relation(con, mechanism, bagging_asset, "EXPLAINS_WITH", "Mechanism component references Bagging.")
        assert con.execute("SELECT COUNT(*) FROM kg_relation WHERE target_node_id=?", (bagging_asset,)).fetchone()[0] == 2
        reached = con.execute(
            """WITH RECURSIVE walk(node_id,depth,path) AS (
                 SELECT ?,0,?
                 UNION ALL
                 SELECT r.target_node_id,walk.depth+1,walk.path||'>'||r.target_node_id
                 FROM walk JOIN kg_relation r ON r.source_node_id=walk.node_id
                 WHERE walk.depth < 2 AND instr(walk.path,r.target_node_id)=0
               ) SELECT node_id FROM walk""",
            (rf["asset_id"], rf["asset_id"]),
        ).fetchall()
        assert bagging_asset in {row[0] for row in reached}
        integrity(con)
        results["FT-02"] = "PASS"

        # FT-03: Missing Data tri-valued rules.
        condition = {"predicate": "project.definition.equals", "args": {"key": "production_missingness", "value": True}}
        rule = add_rule(con, missing["revision_id"], "production-missingness", condition, "RECOMMEND_OPTION", {"strategy": "retain_missingness"}, "STRONG", "ASK")
        unknown = evaluate_rule(con, project_id, rule)
        assert unknown == {"result": "UNKNOWN", "consequence_type": "OPEN_QUESTION"}
        set_definition(con, project_id, "production_missingness", True)
        assert evaluate_rule(con, project_id, rule)["result"] == "TRUE"
        set_definition(con, project_id, "production_missingness", False)
        assert evaluate_rule(con, project_id, rule) == {"result": "FALSE", "consequence_type": None}
        hard = add_rule(
            con,
            missing["revision_id"],
            "train-only-imputation",
            {"predicate": "project.definition.equals", "args": {"key": "uses_learned_imputation", "value": True}},
            "APPLY_VALIDITY_CONSTRAINT",
            {"constraint": "fit_on_training_information_only"},
            "HARD",
            "BLOCK_DEPENDENT",
        )
        assert evaluate_rule(con, project_id, hard) == {"result": "UNKNOWN", "consequence_type": "BLOCK_DEPENDENT"}
        results["FT-03"] = "PASS"

        # FT-04: criterion Finding chain.
        feature_id = create_entity(con, project_id, "VARIABLE")
        evidence_id = create_entity(con, project_id, "EVIDENCE")
        con.execute("INSERT INTO prj_evidence VALUES (?,?,?,?,?)", (evidence_id, "DOCUMENTARY", "Feature arrives after scoring cutoff.", None, now_utc()))
        finding_id = create_entity(con, project_id, "FINDING")
        con.execute("INSERT INTO prj_finding VALUES (?,?,?,?,NULL)", (finding_id, "CRITERION", "Feature X is ineligible.", now_utc()))
        criterion_revision = catalog["feature-eligibility"]["revision_id"]
        con.execute("INSERT INTO prj_criterion_finding VALUES (?,?,?,?,?,?)", (finding_id, feature_id, criterion_revision, "INELIGIBLE", None, "Feature arrives after prediction moment."))
        con.execute("INSERT INTO prj_finding_evidence VALUES (?,?)", (finding_id, evidence_id))
        con.execute("INSERT INTO prj_knowledge_ref VALUES (?,?,?,?,?)", (new_id(), finding_id, criterion_revision, "CRITERION", now_utc()))
        decision_id = create_entity(con, project_id, "DECISION")
        con.execute("INSERT INTO prj_decision VALUES (?,?,?,?,?,?)", (decision_id, "FEATURE_ELIGIBILITY", "Exclude feature X", "Criterion is blocking.", "ACCEPTED", now_utc()))
        con.execute("INSERT INTO prj_decision_support VALUES (?,?)", (decision_id, finding_id))
        assert con.execute("SELECT criterion_knowledge_revision_id FROM prj_criterion_finding WHERE finding_id=?", (finding_id,)).fetchone()[0] == criterion_revision
        results["FT-04"] = "PASS"

        # FT-05: architecture-only hybrid retrieval fixture.
        rebuild_search(con)
        rebuild_embeddings(con)
        cases = [
            ("missing values production", "missing-data"),
            ("chronological future evaluation", "temporal-validation"),
            ("minority unequal classes", "class-imbalance"),
            ("tree bagging interactions", "random-forest"),
            ("feature unavailable leakage", "feature-eligibility"),
            ("numeric distribution bins", "histogram"),
        ]
        for query, expected_slug in cases:
            union = fts_ids(con, query) | semantic_ids(con, query)
            assert catalog[expected_slug]["asset_id"] in union
            assert len(union) < len(catalog)
        results["FT-05"] = "PASS_ARCHITECTURE_ONLY"

        # FT-06: stale/missing embedding is explicit and lexical fallback survives.
        _, missing_count, stale_count = embedding_health(con)
        assert (missing_count, stale_count) == (0, 0)
        current_imbalance_revision = catalog["class-imbalance"]["revision_id"]
        con.execute("DELETE FROM idx_embedding WHERE revision_id=?", (current_imbalance_revision,))
        assert embedding_health(con)[1] >= 1
        assert catalog["class-imbalance"]["asset_id"] in fts_ids(con, "imbalance minority", 10)
        rebuild_embeddings(con)
        assert embedding_health(con)[1:] == (0, 0)
        results["FT-06"] = "PASS"

        # FT-07: bounded context pack always retains required items.
        items = [
            {"id": "feature-eligibility", "required": True, "priority": 100, "cost": 20},
            {"id": "temporal-constraint", "required": True, "priority": 90, "cost": 20},
        ] + [
            {"id": f"optional-{i}", "required": False, "priority": 100 - i, "cost": 5}
            for i in range(100)
        ]
        ordered = sorted(items, key=lambda x: (0 if x["required"] else 1, -x["priority"], x["id"]))
        chosen, used, budget = [], 0, 100
        for item in ordered:
            if item["required"] or used + item["cost"] <= budget:
                if used + item["cost"] > budget:
                    raise AssertionError("required context exceeds budget")
                chosen.append(item["id"])
                used += item["cost"]
        assert used <= budget and "feature-eligibility" in chosen and len(chosen) < len(items)
        results["FT-07"] = "PASS"

        # FT-08: failure injection rolls back semantic publish unit.
        histogram = catalog["histogram"]
        before_pointer = con.execute("SELECT current_accepted_revision_id FROM kg_asset WHERE asset_id=?", (histogram["asset_id"],)).fetchone()[0]
        before_count = con.execute("SELECT COUNT(*) FROM kg_content_revision WHERE node_id=?", (histogram["asset_id"],)).fetchone()[0]
        try:
            publish_asset_revision(con, histogram["asset_id"], kind="METHOD", title="Histogram", purpose="Injected failure", fail_after_insert=True)
        except RuntimeError:
            pass
        else:
            raise AssertionError("failure injection did not fire")
        assert con.execute("SELECT current_accepted_revision_id FROM kg_asset WHERE asset_id=?", (histogram["asset_id"],)).fetchone()[0] == before_pointer
        assert con.execute("SELECT COUNT(*) FROM kg_content_revision WHERE node_id=?", (histogram["asset_id"],)).fetchone()[0] == before_count
        integrity(con)
        results["FT-08"] = "PASS"

        # FT-10: online backup/restore and integrity checks.
        with tempfile.TemporaryDirectory() as backup_dir:
            backup_path = Path(backup_dir) / "backup.sqlite"
            destination = sqlite3.connect(backup_path)
            con.backup(destination)
            destination.close()
            restored = connect(backup_path)
            integrity(restored)
            assert restored.execute("SELECT COUNT(*) FROM kg_asset").fetchone()[0] > 0
            restored.close()
        results["FT-10"] = "PASS"

        # FT-11: derived index destruction/rebuild does not affect authority.
        asset_count = con.execute("SELECT COUNT(*) FROM kg_asset").fetchone()[0]
        con.execute("DELETE FROM idx_embedding")
        con.execute("DELETE FROM idx_search_document")
        con.execute("DELETE FROM idx_knowledge_fts")
        assert con.execute("SELECT COUNT(*) FROM kg_asset").fetchone()[0] == asset_count
        rebuild_search(con)
        rebuild_embeddings(con)
        assert con.execute("SELECT COUNT(*) FROM idx_search_document").fetchone()[0] == asset_count
        integrity(con)
        con.close()
        results["FT-11"] = "PASS"

        # FT-09: WAL reader remains active while short writer proceeds.
        reader_ready = threading.Event()
        release_reader = threading.Event()
        errors: list[Exception] = []

        def reader() -> None:
            try:
                rc = connect(db_path)
                rc.execute("BEGIN")
                rc.execute("SELECT COUNT(*) FROM kg_asset").fetchone()
                reader_ready.set()
                release_reader.wait(5)
                rc.execute("SELECT COUNT(*) FROM kg_asset").fetchone()
                rc.execute("COMMIT")
                rc.close()
            except Exception as exc:  # pragma: no cover - spike diagnostic
                errors.append(exc)

        thread = threading.Thread(target=reader)
        thread.start()
        assert reader_ready.wait(5)
        writer = connect(db_path)
        start = time.perf_counter()
        writer.execute("BEGIN IMMEDIATE")
        writer.execute("INSERT INTO kg_node VALUES (?,?,?)", (new_id(), "ASSET", now_utc()))
        writer.execute("ROLLBACK")
        elapsed = time.perf_counter() - start
        release_reader.set()
        thread.join(5)
        writer.close()
        assert not errors and elapsed < 2.0
        results["FT-09"] = "PASS"

    return results


def main() -> int:
    results = run()
    results["FT-12"] = "SEPARATE_POSTGRESQL_GATE"
    for name in sorted(results):
        print(f"{name}: {results[name]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
