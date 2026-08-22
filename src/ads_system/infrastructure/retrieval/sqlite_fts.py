"""SQLite FTS5 adapter for accepted-current reusable-knowledge retrieval.

The adapter implements Specification 009's first lexical baseline. FTS5 is a
rebuildable projection over authoritative reusable-knowledge persistence: it
must never become the source of truth for knowledge identity, revision history,
governance, or project state.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterable, Mapping
from typing import Any

from sqlalchemy import Engine, select
from sqlalchemy.exc import DatabaseError

from ads_system.application.retrieval import KnowledgeRetrievalHit
from ads_system.infrastructure.persistence.interchange_schema import (
    kg_content_revision_extension,
)
from ads_system.infrastructure.persistence.schema import (
    kg_asset,
    kg_asset_revision,
    kg_component,
    kg_component_revision,
    kg_revision_governance,
)

_INDEX_NAME = "idx_knowledge_fts"
_TOKEN_RE = re.compile(r"\w+", flags=re.UNICODE)
_STOPWORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "been",
        "by",
        "can",
        "do",
        "does",
        "for",
        "from",
        "has",
        "have",
        "how",
        "i",
        "if",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "our",
        "should",
        "that",
        "the",
        "this",
        "to",
        "use",
        "using",
        "was",
        "we",
        "were",
        "what",
        "when",
        "where",
        "which",
        "with",
    }
)


class SqliteFtsKnowledgeRetrieval:
    """Rebuild and query the V1 accepted-current lexical knowledge projection."""

    channel = "LEXICAL"

    def __init__(self, engine: Engine) -> None:
        if engine.dialect.name != "sqlite":
            raise ValueError("SqliteFtsKnowledgeRetrieval requires a SQLite engine")
        self._engine = engine

    def rebuild(self) -> int:
        """Rebuild the complete FTS projection from current accepted knowledge.

        Returns the number of indexed asset revisions. The transaction writes
        only to the derived FTS virtual table; authoritative knowledge tables
        remain untouched.
        """

        with self._engine.begin() as connection:
            self._ensure_index(connection)
            connection.exec_driver_sql(f"DELETE FROM {_INDEX_NAME}")

            rows = connection.execute(
                select(
                    kg_asset.c.stable_key,
                    kg_asset.c.current_accepted_revision_id.label("revision_id"),
                    kg_asset_revision.c.title,
                    kg_asset_revision.c.purpose,
                    kg_asset_revision.c.scope_text,
                    kg_content_revision_extension.c.structured_json,
                )
                .join(
                    kg_asset_revision,
                    kg_asset_revision.c.revision_id
                    == kg_asset.c.current_accepted_revision_id,
                )
                .join(
                    kg_revision_governance,
                    kg_revision_governance.c.revision_id
                    == kg_asset.c.current_accepted_revision_id,
                )
                .outerjoin(
                    kg_content_revision_extension,
                    kg_content_revision_extension.c.revision_id
                    == kg_asset.c.current_accepted_revision_id,
                )
                .where(
                    kg_asset.c.current_accepted_revision_id.is_not(None),
                    kg_revision_governance.c.current_status == "ACCEPTED",
                )
                .order_by(kg_asset.c.stable_key)
            ).mappings().all()

            for row in rows:
                revision_id = str(row["revision_id"])
                extension = self._load_json_object(row["structured_json"])
                profile = extension.get("retrieval_profile") or {}
                components = self._accepted_components(connection, revision_id)

                connection.exec_driver_sql(
                    f"""
                    INSERT INTO {_INDEX_NAME}
                        (stable_key, revision_id, title, lexical_terms, aliases,
                         semantic_cues, body)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        row["stable_key"],
                        revision_id,
                        row["title"],
                        self._join_text(profile.get("lexical_terms")),
                        self._join_text(profile.get("aliases")),
                        self._join_text(profile.get("semantic_cues")),
                        self._body_text(
                            purpose=row["purpose"],
                            scope=row["scope_text"],
                            extension=extension,
                            components=components,
                        ),
                    ),
                )

            return len(rows)

    def search(self, query: str, *, limit: int = 10) -> tuple[KnowledgeRetrievalHit, ...]:
        """Return a bounded, deterministically ordered lexical candidate set."""

        if limit <= 0:
            return ()
        match_query = self._compile_match_query(query)
        if not match_query:
            return ()

        with self._engine.connect() as connection:
            self._ensure_index(connection)
            rows = connection.exec_driver_sql(
                f"""
                SELECT
                    stable_key,
                    revision_id,
                    title,
                    -bm25({_INDEX_NAME}, 8.0, 0.0, 6.0, 5.0, 3.0, 2.0, 1.0)
                        AS score
                FROM {_INDEX_NAME}
                WHERE {_INDEX_NAME} MATCH ?
                ORDER BY score DESC, stable_key ASC
                LIMIT ?
                """,
                (match_query, int(limit)),
            ).mappings().all()

        return tuple(
            KnowledgeRetrievalHit(
                stable_key=row["stable_key"],
                revision_id=str(row["revision_id"]),
                title=row["title"],
                score=float(row["score"]),
                channel=self.channel,
            )
            for row in rows
        )

    def indexed_document_count(self) -> int:
        """Return the current derived-index row count for diagnostics/tests."""

        with self._engine.connect() as connection:
            self._ensure_index(connection)
            value = connection.exec_driver_sql(
                f"SELECT count(*) FROM {_INDEX_NAME}"
            ).scalar_one()
            return int(value)

    @staticmethod
    def _ensure_index(connection) -> None:
        try:
            connection.exec_driver_sql(
                f"""
                CREATE VIRTUAL TABLE IF NOT EXISTS {_INDEX_NAME} USING fts5(
                    stable_key,
                    revision_id UNINDEXED,
                    title,
                    lexical_terms,
                    aliases,
                    semantic_cues,
                    body,
                    tokenize = 'unicode61 remove_diacritics 2'
                )
                """
            )
        except DatabaseError as exc:
            raise RuntimeError(
                "SQLite FTS5 is unavailable; the accepted V1 lexical adapter cannot initialize."
            ) from exc

    @staticmethod
    def _load_json_object(value: str | None) -> dict[str, Any]:
        if value is None:
            return {}
        loaded = json.loads(value)
        if not isinstance(loaded, dict):
            raise ValueError("Knowledge revision extension must decode to a JSON object")
        return loaded

    @classmethod
    def _accepted_components(cls, connection, parent_revision_id: str) -> list[dict[str, Any]]:
        extension = kg_content_revision_extension.alias("component_extension")
        rows = connection.execute(
            select(
                kg_component.c.component_key,
                kg_component.c.component_kind,
                kg_component_revision.c.body_text,
                extension.c.structured_json,
            )
            .join(
                kg_component_revision,
                kg_component_revision.c.component_id == kg_component.c.component_id,
            )
            .join(
                kg_revision_governance,
                kg_revision_governance.c.revision_id
                == kg_component_revision.c.revision_id,
            )
            .outerjoin(
                extension,
                extension.c.revision_id == kg_component_revision.c.revision_id,
            )
            .where(
                kg_component_revision.c.parent_asset_revision_id == parent_revision_id,
                kg_revision_governance.c.current_status == "ACCEPTED",
            )
            .order_by(kg_component.c.component_key)
        ).mappings().all()

        result: list[dict[str, Any]] = []
        for row in rows:
            component_extension = cls._load_json_object(row["structured_json"])
            result.append(
                {
                    "component_key": row["component_key"],
                    "component_kind": row["component_kind"],
                    "body": row["body_text"],
                    "reasoning_functions": component_extension.get("reasoning_functions") or [],
                }
            )
        return result

    @classmethod
    def _body_text(
        cls,
        *,
        purpose: str,
        scope: str | None,
        extension: Mapping[str, Any],
        components: Iterable[Mapping[str, Any]],
    ) -> str:
        parts: list[str] = [purpose]
        if scope:
            parts.append(scope)

        parts.extend(cls._strings(extension.get("limitations")))
        parts.extend(cls._strings(extension.get("reasoning_functions")))

        for requirement in extension.get("context_requirements") or []:
            if isinstance(requirement, Mapping):
                parts.extend(cls._strings(requirement.get("key")))
                parts.extend(cls._strings(requirement.get("description")))
                parts.extend(cls._strings(requirement.get("required_for")))

        parts.extend(cls._strings(extension.get("semantic_checks")))

        for facet in extension.get("narrative_facets") or []:
            if isinstance(facet, Mapping):
                parts.extend(cls._strings(facet.get("facet_kind")))
                parts.extend(cls._strings(facet.get("body")))

        for component in components:
            parts.extend(cls._strings(component.get("component_key")))
            parts.extend(cls._strings(component.get("component_kind")))
            parts.extend(cls._strings(component.get("body")))
            parts.extend(cls._strings(component.get("reasoning_functions")))

        return " ".join(part for part in parts if part)

    @classmethod
    def _join_text(cls, value: Any) -> str:
        return " ".join(cls._strings(value))

    @classmethod
    def _strings(cls, value: Any) -> list[str]:
        if value is None:
            return []
        if isinstance(value, str):
            return [value]
        if isinstance(value, Mapping):
            result: list[str] = []
            for key in sorted(value):
                result.extend(cls._strings(value[key]))
            return result
        if isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
            result = []
            for item in value:
                result.extend(cls._strings(item))
            return result
        return []

    @classmethod
    def _compile_match_query(cls, query: str) -> str:
        tokens: list[str] = []
        seen: set[str] = set()
        for match in _TOKEN_RE.finditer(query.casefold()):
            token = match.group(0)
            if token in _STOPWORDS or token in seen:
                continue
            seen.add(token)
            tokens.append(token)
        return " OR ".join(f'"{token}"' for token in tokens)
