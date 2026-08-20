#!/usr/bin/env python3
"""Synthetic viability spike for a SQLite-centered V1 architecture.

This script is not a production benchmark and must not be interpreted as one.
Its purpose is narrower: test whether the workload scale assumed by the
Autonomous Data Science System's V1 implementation requirements obviously
requires a dedicated graph database, vector database, or server database.

The spike exercises the capabilities that are most relevant to the current
architecture decision:

1. stable relational lookup;
2. typed incoming and outgoing relationship lookup;
3. bounded recursive relationship traversal;
4. FTS5 lexical retrieval;
5. exact dense-vector similarity search in process.

The generated data are synthetic. Timings depend on hardware, SQLite build,
Python/NumPy build, filesystem, cache state, and generated graph structure.
The results therefore provide feasibility evidence only. They are useful for
falsifying claims such as "SQLite cannot plausibly serve these workloads at
V1 scale", but they do not establish production capacity or latency SLOs.

Example:

    python experiments/architecture_spikes/sqlite_v1_viability.py

A larger run can be requested explicitly:

    python experiments/architecture_spikes/sqlite_v1_viability.py \
        --assets 50000 \
        --relations 500000 \
        --embedding-assets 100000

The script writes its temporary SQLite database to a temporary directory and
removes it automatically. It prints one JSON report to standard output so the
result can be archived or compared across environments without parsing human
formatted logs.
"""

from __future__ import annotations

import argparse
import json
import random
import sqlite3
import statistics
import tempfile
import time
from pathlib import Path
from typing import Any, Callable

import numpy as np


RELATION_TYPES = (
    "REQUIRES",
    "COMPLEMENTS",
    "ALTERNATIVE_TO",
    "PART_OF",
    "GOVERNED_BY",
)

VOCABULARY = (
    "missing",
    "temporal",
    "validation",
    "forest",
    "feature",
    "eligibility",
    "class",
    "imbalance",
    "distribution",
    "prediction",
    "evidence",
    "calibration",
    "outlier",
    "drift",
    "preprocessing",
    "leakage",
)


def _timed_ms(fn: Callable[[], Any], repetitions: int) -> dict[str, float]:
    """Return median and p95 wall-clock latency in milliseconds.

    The function is intentionally small and uses repeated wall-clock timing
    rather than a microbenchmark framework. The objective is to establish
    order-of-magnitude feasibility under the same process that builds the
    synthetic workload.
    """

    values: list[float] = []
    for _ in range(repetitions):
        start = time.perf_counter()
        fn()
        values.append((time.perf_counter() - start) * 1_000.0)

    values.sort()
    p95_index = min(len(values) - 1, int(round(0.95 * (len(values) - 1))))
    return {
        "median_ms": statistics.median(values),
        "p95_ms": values[p95_index],
        "max_ms": max(values),
    }


def _create_schema(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    connection.execute("PRAGMA synchronous = NORMAL")

    connection.executescript(
        """
        CREATE TABLE asset (
            asset_id INTEGER PRIMARY KEY,
            stable_key TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            current_revision_id INTEGER
        );

        CREATE TABLE revision (
            revision_id INTEGER PRIMARY KEY,
            asset_id INTEGER NOT NULL REFERENCES asset(asset_id),
            revision_number INTEGER NOT NULL,
            purpose TEXT NOT NULL,
            scope TEXT NOT NULL,
            body TEXT NOT NULL,
            governance_state TEXT NOT NULL,
            UNIQUE(asset_id, revision_number)
        );

        CREATE TABLE component (
            component_id INTEGER PRIMARY KEY,
            revision_id INTEGER NOT NULL REFERENCES revision(revision_id),
            component_key TEXT NOT NULL,
            component_type TEXT NOT NULL,
            content TEXT NOT NULL,
            UNIQUE(revision_id, component_key)
        );

        CREATE TABLE relation (
            relation_id INTEGER PRIMARY KEY,
            source_asset_id INTEGER NOT NULL REFERENCES asset(asset_id),
            relation_type TEXT NOT NULL,
            target_asset_id INTEGER NOT NULL REFERENCES asset(asset_id),
            rationale TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1
        );

        CREATE INDEX relation_source_type_idx
            ON relation(source_asset_id, relation_type);

        CREATE INDEX relation_target_type_idx
            ON relation(target_asset_id, relation_type);

        CREATE VIRTUAL TABLE knowledge_fts USING fts5(
            stable_key,
            title,
            purpose,
            scope,
            body
        );
        """
    )


def _populate(
    connection: sqlite3.Connection,
    *,
    assets: int,
    relations: int,
    seed: int,
) -> None:
    rng = random.Random(seed)

    asset_rows: list[tuple[Any, ...]] = []
    revision_rows: list[tuple[Any, ...]] = []
    fts_rows: list[tuple[str, str, str, str, str]] = []
    component_rows: list[tuple[Any, ...]] = []

    component_id = 1
    for asset_id in range(1, assets + 1):
        words = rng.sample(VOCABULARY, 5)
        stable_key = f"asset.{asset_id}"
        title = f"{words[0].title()} {words[1].title()} {asset_id}"
        purpose = f"Reason about {' '.join(words)} in project methodology."
        scope = f"Applicable to {' '.join(words[:3])} contexts."
        body = (" ".join(words) + " ") * 8 + "methodological explanation"

        asset_rows.append((asset_id, stable_key, title, asset_id))
        revision_rows.append(
            (
                asset_id,
                asset_id,
                1,
                purpose,
                scope,
                body,
                "accepted",
            )
        )
        fts_rows.append((stable_key, title, purpose, scope, body))

        for component_type in ("rule", "interpretation", "limitation"):
            component_rows.append(
                (
                    component_id,
                    asset_id,
                    component_type,
                    component_type,
                    f"{component_type} component for asset {asset_id}",
                )
            )
            component_id += 1

    connection.executemany(
        "INSERT INTO asset VALUES (?, ?, ?, ?)",
        asset_rows,
    )
    connection.executemany(
        "INSERT INTO revision VALUES (?, ?, ?, ?, ?, ?, ?)",
        revision_rows,
    )
    connection.executemany(
        "INSERT INTO component VALUES (?, ?, ?, ?, ?)",
        component_rows,
    )
    connection.executemany(
        "INSERT INTO knowledge_fts VALUES (?, ?, ?, ?, ?)",
        fts_rows,
    )

    relation_rows: list[tuple[Any, ...]] = []
    relation_id = 1

    # A simple chain guarantees at least one traversable path through the
    # generated graph. Remaining edges add random local branching.
    chain_edges = min(max(0, assets - 1), relations)
    for source in range(1, chain_edges + 1):
        relation_rows.append(
            (relation_id, source, "REQUIRES", source + 1, "synthetic chain", 1)
        )
        relation_id += 1

    while len(relation_rows) < relations:
        relation_rows.append(
            (
                relation_id,
                rng.randint(1, assets),
                rng.choice(RELATION_TYPES),
                rng.randint(1, assets),
                "synthetic rationale",
                1,
            )
        )
        relation_id += 1

    connection.executemany(
        "INSERT INTO relation VALUES (?, ?, ?, ?, ?, ?)",
        relation_rows,
    )
    connection.commit()


def _sqlite_benchmarks(
    connection: sqlite3.Connection,
    *,
    assets: int,
    traversal_depth: int,
) -> dict[str, Any]:
    target = max(1, min(assets, int(assets * 0.77)))

    direct = _timed_ms(
        lambda: list(
            connection.execute(
                "SELECT * FROM asset WHERE stable_key = ?",
                (f"asset.{target}",),
            )
        ),
        100,
    )

    outgoing = _timed_ms(
        lambda: list(
            connection.execute(
                """
                SELECT *
                FROM relation
                WHERE source_asset_id = ? AND relation_type = ?
                """,
                (target, "REQUIRES"),
            )
        ),
        100,
    )

    incoming = _timed_ms(
        lambda: list(
            connection.execute(
                """
                SELECT *
                FROM relation
                WHERE target_asset_id = ? AND relation_type = ?
                """,
                (target, "REQUIRES"),
            )
        ),
        100,
    )

    # The query terms intentionally occur frequently in the synthetic corpus.
    # This makes the lexical workload less selective and therefore avoids
    # presenting an unrealistically easy FTS case.
    fts = _timed_ms(
        lambda: list(
            connection.execute(
                """
                SELECT rowid, bm25(knowledge_fts)
                FROM knowledge_fts
                WHERE knowledge_fts MATCH ?
                ORDER BY bm25(knowledge_fts)
                LIMIT 20
                """,
                ("temporal validation",),
            )
        ),
        30,
    )

    traversal_sql = """
        WITH RECURSIVE walk(node, depth) AS (
            VALUES (?, 0)
            UNION
            SELECT relation.target_asset_id, walk.depth + 1
            FROM walk
            JOIN relation
                ON relation.source_asset_id = walk.node
            WHERE walk.depth < ?
        )
        SELECT COUNT(*) FROM walk
    """

    traversal_count = connection.execute(
        traversal_sql,
        (target, traversal_depth),
    ).fetchone()[0]

    traversal = _timed_ms(
        lambda: connection.execute(
            traversal_sql,
            (target, traversal_depth),
        ).fetchone(),
        30,
    )

    return {
        "direct_identity_lookup": direct,
        "outgoing_typed_relation_lookup": outgoing,
        "incoming_typed_relation_lookup": incoming,
        "fts5_top20": fts,
        "bounded_relation_traversal": {
            **traversal,
            "depth": traversal_depth,
            "rows_reached": traversal_count,
        },
    }


def _vector_benchmark(
    *,
    items: int,
    dimensions: int,
    seed: int,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    matrix = rng.normal(size=(items, dimensions)).astype(np.float32)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-12

    query = rng.normal(size=(dimensions,)).astype(np.float32)
    query /= np.linalg.norm(query)

    def search() -> None:
        scores = matrix @ query
        top = np.argpartition(scores, -20)[-20:]
        top[np.argsort(scores[top])[::-1]]

    timings = _timed_ms(search, 20)
    return {
        **timings,
        "items": items,
        "dimensions": dimensions,
        "matrix_mebibytes": matrix.nbytes / (1024.0 * 1024.0),
        "algorithm": "exact normalized dot-product cosine search",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets", type=int, default=10_000)
    parser.add_argument("--relations", type=int, default=100_000)
    parser.add_argument("--traversal-depth", type=int, default=3)
    parser.add_argument("--embedding-assets", type=int, default=20_000)
    parser.add_argument("--embedding-dimensions", type=int, default=768)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.assets < 2:
        raise SystemExit("--assets must be at least 2")
    if args.relations < 1:
        raise SystemExit("--relations must be positive")
    if args.embedding_assets < 20:
        raise SystemExit("--embedding-assets must be at least 20")
    if args.embedding_dimensions < 1:
        raise SystemExit("--embedding-dimensions must be positive")

    with tempfile.TemporaryDirectory(prefix="ads-sqlite-spike-") as directory:
        database_path = Path(directory) / "spike.sqlite"
        connection = sqlite3.connect(database_path)
        try:
            _create_schema(connection)
            start = time.perf_counter()
            _populate(
                connection,
                assets=args.assets,
                relations=args.relations,
                seed=args.seed,
            )
            population_seconds = time.perf_counter() - start

            sqlite_results = _sqlite_benchmarks(
                connection,
                assets=args.assets,
                traversal_depth=args.traversal_depth,
            )
            database_bytes = database_path.stat().st_size
        finally:
            connection.close()

        vector_results = _vector_benchmark(
            items=args.embedding_assets,
            dimensions=args.embedding_dimensions,
            seed=args.seed,
        )

    report = {
        "purpose": "V1 architecture feasibility smoke test, not production benchmark",
        "environment": {
            "sqlite_version": sqlite3.sqlite_version,
            "numpy_version": np.__version__,
        },
        "workload": {
            "assets": args.assets,
            "components": args.assets * 3,
            "relations": args.relations,
            "traversal_depth": args.traversal_depth,
            "embedding_assets": args.embedding_assets,
            "embedding_dimensions": args.embedding_dimensions,
        },
        "population_seconds": population_seconds,
        "sqlite_database_mebibytes": database_bytes / (1024.0 * 1024.0),
        "sqlite": sqlite_results,
        "semantic_exact_search": vector_results,
    }

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
