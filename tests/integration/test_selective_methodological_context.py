from __future__ import annotations

import copy
import json
import os
from pathlib import Path

from alembic import command
from alembic.config import Config

from ads_system.application.context_models import (
    MethodologicalContextPack,
    MethodologicalContextRequest,
    SelectedContextKnowledge,
)
from ads_system.application.context_selection import (
    StaleContextKnowledgeError,
    methodological_context_pack_payload,
    select_methodological_context,
    serialize_methodological_context_pack,
)
from ads_system.application.horizon import build_methodological_horizon
from ads_system.application.horizon_models import HorizonCandidate, HorizonSeed, MethodologicalHorizon
from ads_system.application.knowledge_interchange import (
    accept_candidate_bundle,
    export_current_accepted_snapshot,
    import_candidate_bundle,
)
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
KNOWLEDGE_FIXTURE = (
    ROOT / "tests" / "fixtures" / "knowledge" / "reusable_knowledge_stress_v1.json"
)
CONTEXT_FIXTURE = (
    ROOT / "tests" / "fixtures" / "retrieval" / "selective_context_v1.json"
)

FORBIDDEN_MODEL_CONTEXT_FIELDS = {
    "aliases",
    "asset_id",
    "channel",
    "component_id",
    "governance_status",
    "lexical_terms",
    "negative_cues",
    "provenance_source_ids",
    "score",
    "semantic_cues",
}


def _upgrade(database_url: str) -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, "head")
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)


def _candidate_bundle() -> dict:
    bundle = copy.deepcopy(load_bundle(KNOWLEDGE_FIXTURE))
    bundle["bundle_kind"] = "CANDIDATE_SET"
    validate_bundle(bundle)
    validate_import_safety(bundle)
    return bundle


def _context_benchmark() -> dict:
    return json.loads(CONTEXT_FIXTURE.read_text(encoding="utf-8"))


def _snapshot_asset_map(snapshot: dict) -> dict[str, dict]:
    return {asset["stable_key"]: asset for asset in snapshot["assets"]}


def _control_pack(
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory,
) -> MethodologicalContextPack:
    """Materialize the full included Horizon only as a benchmark size control."""

    items: list[SelectedContextKnowledge] = []
    with uow_factory() as uow:
        for candidate in horizon.included:
            asset = uow.navigation.get_context_asset(
                candidate.stable_key,
                candidate.revision_id,
            )
            assert asset is not None
            items.append(
                SelectedContextKnowledge(
                    asset=asset,
                    selection_reason="CONTROL_INCLUDED",
                    origin=candidate.origin,
                    applicability_state=candidate.applicability_state,
                    missing_context_keys=candidate.missing_context_keys,
                    relation_source_key=candidate.relation_source_key,
                    relation_type=candidate.relation_type,
                    relation_revision_id=candidate.relation_revision_id,
                )
            )

    aggregate_missing = tuple(
        sorted({key for item in items for key in item.missing_context_keys})
    )
    return MethodologicalContextPack(
        schema_version=1,
        task_id=request.task_id,
        requested_reasoning_functions=tuple(sorted(request.requested_reasoning_functions)),
        knowledge=tuple(items),
        missing_context_keys=aggregate_missing,
    )


def _all_mapping_keys(value) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(_all_mapping_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_all_mapping_keys(child))
    return keys


def test_frozen_rh_c_selective_context_gate(tmp_path: Path) -> None:
    database_url = sqlite_database_url(tmp_path / "selective_context.sqlite3")
    _upgrade(database_url)
    engine = create_operational_engine(database_url)
    uow_factory = lambda: SqlAlchemyUnitOfWork(engine)

    try:
        benchmark = _context_benchmark()
        candidate_bundle = _candidate_bundle()
        import_candidate_bundle(candidate_bundle, uow_factory=uow_factory)
        accept_candidate_bundle(candidate_bundle, uow_factory=uow_factory)

        snapshot_before = export_current_accepted_snapshot(uow_factory=uow_factory)
        digest_before = semantic_digest(snapshot_before)
        snapshot_assets = _snapshot_asset_map(snapshot_before)

        seeds: list[HorizonSeed] = []
        with SqlAlchemyUnitOfWork(engine) as uow:
            for stable_key in benchmark["wide_horizon_seed_keys"]:
                asset = uow.navigation.get_current_asset(stable_key)
                assert asset is not None
                seeds.append(
                    HorizonSeed(
                        stable_key=asset.stable_key,
                        revision_id=asset.revision_id,
                        title=asset.title,
                    )
                )

        horizon = build_methodological_horizon(
            seeds,
            known_context=benchmark["common_known_context"],
            uow_factory=uow_factory,
        )
        assert len(horizon.included) == benchmark["expected_wide_horizon_included_count"]
        assert horizon.excluded == ()

        horizon_keys = {item.stable_key for item in horizon.included}
        catalog_keys = set(snapshot_assets)
        assert horizon_keys == catalog_keys

        # Relation-source provenance is required by bounded REQUIRES_CONCEPT
        # support closure and must point to a direct seed.
        direct_keys = {
            item.stable_key for item in horizon.included if item.origin == "DIRECT"
        }
        for item in horizon.included:
            if item.origin == "DIRECT":
                assert item.relation_source_key is None
            else:
                assert item.relation_source_key in direct_keys
                assert item.relation_type is not None
                assert item.relation_revision_id is not None

        case_results: dict[str, dict] = {}
        for case in benchmark["cases"]:
            request = MethodologicalContextRequest(
                task_id=case["task_id"],
                requested_reasoning_functions=tuple(
                    case["requested_reasoning_functions"]
                ),
                max_assets=int(case["max_assets"]),
            )
            selection = select_methodological_context(
                horizon,
                request,
                uow_factory=uow_factory,
            )
            selected = selection.pack.knowledge
            selected_keys = {item.asset.stable_key for item in selected}
            required_keys = set(case["required_selected_keys"])

            assert selected_keys == required_keys, (
                case["case_id"],
                sorted(required_keys),
                sorted(selected_keys),
            )
            assert len(selected) <= case["max_assets"]
            assert selection.pack.missing_context_keys == tuple(
                case["required_missing_context_keys"]
            )

            expected_reasons = case["expected_selection_reasons"]
            for item in selected:
                assert item.asset.revision_id == snapshot_assets[item.asset.stable_key][
                    "revision_id"
                ]
                assert item.selection_reason == expected_reasons[item.asset.stable_key]

            decisions = {decision.stable_key: decision for decision in selection.decisions}
            assert set(decisions) == horizon_keys
            assert all(decision.reason for decision in decisions.values())
            assert {
                key for key, decision in decisions.items() if decision.selected
            } == selected_keys

            selective_serialized = serialize_methodological_context_pack(selection.pack)
            selective_repeat = serialize_methodological_context_pack(selection.pack)
            assert selective_repeat == selective_serialized

            full_pack = _control_pack(
                horizon,
                request,
                uow_factory=uow_factory,
            )
            full_serialized = serialize_methodological_context_pack(full_pack)

            # The deliberately wide Horizon equals the ten-asset global catalog,
            # so the same compact projection is also the global-size control.
            global_serialized = full_serialized
            ratio = selective_serialized.utf8_bytes / full_serialized.utf8_bytes

            assert selective_serialized.utf8_bytes < full_serialized.utf8_bytes
            assert ratio <= 0.65, (case["case_id"], ratio)
            assert selective_serialized.utf8_bytes < global_serialized.utf8_bytes

            payload = methodological_context_pack_payload(selection.pack)
            assert "decisions" not in payload
            assert "omitted" not in payload
            assert {
                item["stable_key"] for item in payload["knowledge"]
            } == selected_keys
            assert not (
                _all_mapping_keys(payload) & FORBIDDEN_MODEL_CONTEXT_FIELDS
            )

            # The compact projection must still contain substantive governed
            # methodological content rather than only titles/IDs.
            by_key = {item.asset.stable_key: item.asset for item in selected}
            if "histogram" in by_key:
                assert any(
                    component.component_key == "binning-sensitivity"
                    for component in by_key["histogram"].components
                )
                assert any(
                    facet.facet_kind == "CLAIM_BOUNDARY"
                    for facet in by_key["histogram"].narrative_facets
                )
            if "class-imbalance" in by_key:
                assert any(
                    component.component_key == "metric-sensitivity"
                    for component in by_key["class-imbalance"].components
                )
                assert any(
                    rule.rule_key == "inspect-minority-sensitive-evidence"
                    for rule in by_key["class-imbalance"].rules
                )
            if "prediction-time-feature-eligibility" in by_key:
                assert any(
                    component.component_key == "availability-boundary"
                    for component in by_key["prediction-time-feature-eligibility"].components
                )

            case_results[case["case_id"]] = {
                "task_id": case["task_id"],
                "requested_reasoning_functions": case[
                    "requested_reasoning_functions"
                ],
                "selected": [
                    {
                        "stable_key": item.asset.stable_key,
                        "revision_id": item.asset.revision_id,
                        "selection_reason": item.selection_reason,
                        "origin": item.origin,
                        "applicability_state": item.applicability_state,
                        "missing_context_keys": item.missing_context_keys,
                    }
                    for item in selected
                ],
                "omitted": [
                    {
                        "stable_key": decision.stable_key,
                        "reason": decision.reason,
                    }
                    for decision in selection.decisions
                    if not decision.selected
                ],
                "aggregate_missing_context_keys": selection.pack.missing_context_keys,
                "selected_asset_count": len(selected),
                "full_horizon_asset_count": len(horizon.included),
                "global_asset_count": len(snapshot_assets),
                "selective_utf8_bytes": selective_serialized.utf8_bytes,
                "full_horizon_utf8_bytes": full_serialized.utf8_bytes,
                "global_control_utf8_bytes": global_serialized.utf8_bytes,
                "selective_to_full_ratio": round(ratio, 8),
                "selective_sha256": selective_serialized.sha256,
            }

        # Exact context lookup is fail-closed for a stale revision.
        with SqlAlchemyUnitOfWork(engine) as uow:
            assert (
                uow.navigation.get_context_asset(
                    "random-forest",
                    "00000000-0000-0000-0000-000000000000",
                )
                is None
            )

        rf = next(item for item in horizon.included if item.stable_key == "random-forest")
        stale_rf = HorizonCandidate(
            stable_key=rf.stable_key,
            revision_id="00000000-0000-0000-0000-000000000000",
            title=rf.title,
            origin=rf.origin,
            relation_type=rf.relation_type,
            relation_revision_id=rf.relation_revision_id,
            applicability_state=rf.applicability_state,
            missing_context_keys=rf.missing_context_keys,
            relation_source_key=rf.relation_source_key,
            reasoning_functions=rf.reasoning_functions,
        )
        stale_horizon = MethodologicalHorizon(included=(stale_rf,), excluded=())
        try:
            select_methodological_context(
                stale_horizon,
                MethodologicalContextRequest(
                    task_id="stale-context-check",
                    requested_reasoning_functions=("MODEL_OPTION",),
                    max_assets=1,
                ),
                uow_factory=uow_factory,
            )
        except StaleContextKnowledgeError:
            pass
        else:
            raise AssertionError("stale context revision was silently accepted")

        snapshot_after = export_current_accepted_snapshot(uow_factory=uow_factory)
        assert snapshot_after == snapshot_before
        assert semantic_digest(snapshot_after) == digest_before

        result = {
            "specification": "013-v0.1",
            "benchmark_id": benchmark["benchmark_id"],
            "wide_horizon_included_count": len(horizon.included),
            "global_accepted_count": len(snapshot_assets),
            "cases_passed": len(case_results),
            "case_results": case_results,
            "authoritative_knowledge_unchanged": True,
        }
        print("V1_SELECTIVE_CONTEXT_JSON=" + json.dumps(result, sort_keys=True))
    finally:
        engine.dispose()
