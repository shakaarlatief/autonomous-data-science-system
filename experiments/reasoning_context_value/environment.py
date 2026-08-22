"""Deterministic isolated environment for Specification 014.

The live reasoning experiment must consume the same governed reusable-knowledge
fixture, accepted-current navigation seam, and deliberately wide
MethodologicalHorizon that were validated before the reasoning experiment.
This module prepares that state in an isolated temporary SQLite database.

No model call is made here. Once setup is complete the accepted snapshot is
recorded and treated as immutable for the duration of the experiment. The
runner verifies that digest again after execution so provider activity cannot
silently mutate methodological authority.
"""

from __future__ import annotations

from dataclasses import dataclass
import copy
import json
import os
from pathlib import Path
from typing import Callable

from alembic import command
from alembic.config import Config
from sqlalchemy import Engine

from ads_system.application.horizon import build_methodological_horizon
from ads_system.application.horizon_models import HorizonSeed, MethodologicalHorizon
from ads_system.application.knowledge_interchange import (
    accept_candidate_bundle,
    export_current_accepted_snapshot,
    import_candidate_bundle,
)
from ads_system.application.ports import UnitOfWork
from ads_system.infrastructure.interchange.knowledge_bundle import (
    load_bundle,
    semantic_digest,
    validate_bundle,
    validate_import_safety,
)
from ads_system.infrastructure.persistence.engine import (
    create_operational_engine,
    sqlite_database_url,
)
from ads_system.infrastructure.persistence.uow import SqlAlchemyUnitOfWork


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KNOWLEDGE_FIXTURE = (
    ROOT / "tests" / "fixtures" / "knowledge" / "reusable_knowledge_stress_v1.json"
)
DEFAULT_SELECTIVE_FIXTURE = (
    ROOT / "tests" / "fixtures" / "retrieval" / "selective_context_v1.json"
)

UnitOfWorkFactory = Callable[[], UnitOfWork]


@dataclass(slots=True)
class PreparedReasoningEnvironment:
    """Isolated accepted-current knowledge state used by the frozen experiment."""

    engine: Engine
    uow_factory: UnitOfWorkFactory
    horizon: MethodologicalHorizon
    accepted_snapshot_digest: str
    accepted_stable_revision_pairs: tuple[tuple[str, str], ...]
    max_assets: int
    common_known_context: dict[str, object]

    def assert_authoritative_state_unchanged(self) -> None:
        """Fail if reusable-knowledge authority changed after environment setup."""

        snapshot = export_current_accepted_snapshot(uow_factory=self.uow_factory)
        observed_digest = semantic_digest(snapshot)
        if observed_digest != self.accepted_snapshot_digest:
            raise RuntimeError(
                "authoritative reusable-knowledge state changed during reasoning experiment: "
                f"expected {self.accepted_snapshot_digest}, observed {observed_digest}"
            )
        observed_pairs = tuple(
            sorted(
                (str(asset["stable_key"]), str(asset["revision_id"]))
                for asset in snapshot["assets"]
            )
        )
        if observed_pairs != self.accepted_stable_revision_pairs:
            raise RuntimeError("accepted stable-key/revision identities changed during experiment")

    def assert_current_context(
        self,
        stable_revision_pairs: tuple[tuple[str, str], ...],
    ) -> None:
        """Verify every preassembled context identity is still exact accepted-current."""

        with self.uow_factory() as uow:
            for stable_key, revision_id in stable_revision_pairs:
                asset = uow.navigation.get_context_asset(stable_key, revision_id)
                if asset is None:
                    raise RuntimeError(
                        "preassembled reasoning context is no longer exact accepted-current: "
                        f"{stable_key}@{revision_id}"
                    )

    def close(self) -> None:
        self.engine.dispose()

    def __enter__(self) -> "PreparedReasoningEnvironment":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


def prepare_reasoning_environment(
    database_path: Path,
    *,
    knowledge_fixture: Path = DEFAULT_KNOWLEDGE_FIXTURE,
    selective_fixture: Path = DEFAULT_SELECTIVE_FIXTURE,
) -> PreparedReasoningEnvironment:
    """Create the frozen accepted-current catalog and ten-asset wide Horizon."""

    selective = json.loads(selective_fixture.read_text(encoding="utf-8"))
    cases = selective["cases"]
    max_assets_values = {int(case["max_assets"]) for case in cases}
    if max_assets_values != {3}:
        raise ValueError(
            "Specification 014 inherits max_assets=3 from the accepted selective fixture; "
            f"observed {sorted(max_assets_values)}"
        )

    database_url = sqlite_database_url(database_path)
    _upgrade_database(database_url)
    engine = create_operational_engine(database_url)
    uow_factory: UnitOfWorkFactory = lambda: SqlAlchemyUnitOfWork(engine)

    try:
        candidate_bundle = copy.deepcopy(load_bundle(knowledge_fixture))
        candidate_bundle["bundle_kind"] = "CANDIDATE_SET"
        validate_bundle(candidate_bundle)
        validate_import_safety(candidate_bundle)
        import_candidate_bundle(candidate_bundle, uow_factory=uow_factory)
        accept_candidate_bundle(candidate_bundle, uow_factory=uow_factory)

        snapshot = export_current_accepted_snapshot(uow_factory=uow_factory)
        snapshot_digest = semantic_digest(snapshot)
        accepted_pairs = tuple(
            sorted(
                (str(asset["stable_key"]), str(asset["revision_id"]))
                for asset in snapshot["assets"]
            )
        )
        if len(accepted_pairs) != 10:
            raise ValueError(
                "frozen reasoning experiment requires exactly ten accepted benchmark assets; "
                f"observed {len(accepted_pairs)}"
            )

        seeds: list[HorizonSeed] = []
        with uow_factory() as uow:
            for stable_key in selective["wide_horizon_seed_keys"]:
                asset = uow.navigation.get_current_asset(str(stable_key))
                if asset is None:
                    raise ValueError(f"missing accepted wide-Horizon seed: {stable_key}")
                seeds.append(
                    HorizonSeed(
                        stable_key=asset.stable_key,
                        revision_id=asset.revision_id,
                        title=asset.title,
                    )
                )

        common_known_context = dict(selective["common_known_context"])
        horizon = build_methodological_horizon(
            seeds,
            known_context=common_known_context,
            uow_factory=uow_factory,
        )
        if len(horizon.included) != int(selective["expected_wide_horizon_included_count"]):
            raise ValueError(
                "wide MethodologicalHorizon included-count drift: "
                f"expected {selective['expected_wide_horizon_included_count']}, "
                f"observed {len(horizon.included)}"
            )
        if horizon.excluded:
            raise ValueError(
                "frozen wide MethodologicalHorizon unexpectedly contains excluded candidates"
            )
        horizon_pairs = tuple(
            sorted((item.stable_key, item.revision_id) for item in horizon.included)
        )
        if horizon_pairs != accepted_pairs:
            raise ValueError(
                "frozen wide MethodologicalHorizon no longer equals the ten-asset accepted catalog"
            )

        return PreparedReasoningEnvironment(
            engine=engine,
            uow_factory=uow_factory,
            horizon=horizon,
            accepted_snapshot_digest=snapshot_digest,
            accepted_stable_revision_pairs=accepted_pairs,
            max_assets=3,
            common_known_context=common_known_context,
        )
    except Exception:
        engine.dispose()
        raise


def _upgrade_database(database_url: str) -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, "head")
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)
