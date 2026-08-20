"""Application services for governed reusable-knowledge import/export.

All structural and semantic bundle validation happens before a database
transaction begins. Candidate creation and explicit acceptance are separate
operations so external files cannot silently become accepted methodological
authority.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

from ads_system.application.ports import UnitOfWork
from ads_system.infrastructure.interchange.knowledge_bundle import (
    KnowledgeBundleValidationError,
    normalize_bundle,
    resolve_node_ref,
    validate_bundle,
    validate_import_safety,
)

UnitOfWorkFactory = Callable[[], UnitOfWork]


def import_candidate_bundle(
    bundle: Mapping[str, Any],
    *,
    uow_factory: UnitOfWorkFactory,
    actor: str = "knowledge-import",
    allow_benchmark_fixture: bool = False,
) -> None:
    """Import candidate/reviewed knowledge without advancing accepted pointers."""

    validate_bundle(bundle)
    validate_import_safety(bundle)
    if bundle["bundle_kind"] == "ACCEPTED_SNAPSHOT":
        raise KnowledgeBundleValidationError(
            "Normal candidate import cannot consume an ACCEPTED_SNAPSHOT."
        )
    if bundle["bundle_kind"] == "BENCHMARK_FIXTURE" and not allow_benchmark_fixture:
        raise KnowledgeBundleValidationError(
            "BENCHMARK_FIXTURE import requires an explicit test/evaluation override."
        )

    with uow_factory() as uow:
        for source in bundle["provenance_sources"]:
            uow.interchange.import_provenance_source(source)

        for asset in bundle["assets"]:
            uow.interchange.import_asset_revision(asset, actor=actor)
            for component in asset["components"]:
                uow.interchange.import_component_revision(
                    parent_asset_revision_id=asset["revision_id"],
                    component=component,
                    actor=actor,
                )
            for rule in asset["rules"]:
                uow.interchange.import_rule(
                    owner_content_revision_id=asset["revision_id"],
                    rule=rule,
                )

        for relation in bundle["relations"]:
            source_asset_id, source_component_id = resolve_node_ref(
                bundle, relation["source_ref"]
            )
            target_asset_id, target_component_id = resolve_node_ref(
                bundle, relation["target_ref"]
            )
            uow.interchange.import_relation_revision(
                relation,
                source_node_id=source_component_id or source_asset_id,
                target_node_id=target_component_id or target_asset_id,
                actor=actor,
            )
        uow.commit()


def accept_candidate_bundle(
    bundle: Mapping[str, Any],
    *,
    uow_factory: UnitOfWorkFactory,
    actor: str = "knowledge-review",
) -> None:
    """Explicitly accept all revisions in a validated CANDIDATE_SET.

    This is deliberately not called by ``import_candidate_bundle``. Review and
    authorization may occur between the two operations in a real workflow.
    BENCHMARK_FIXTURE material cannot be accepted through this path.
    """

    validate_bundle(bundle)
    validate_import_safety(bundle)
    if bundle["bundle_kind"] != "CANDIDATE_SET":
        raise KnowledgeBundleValidationError(
            "Explicit acceptance requires bundle_kind=CANDIDATE_SET."
        )

    with uow_factory() as uow:
        for asset in bundle["assets"]:
            uow.interchange.accept_content_revision(
                asset["revision_id"], actor=actor
            )
            for component in asset["components"]:
                uow.interchange.accept_content_revision(
                    component["revision_id"], actor=actor
                )
        for relation in bundle["relations"]:
            uow.interchange.accept_relation_revision(
                relation["relation_revision_id"], actor=actor
            )

        for collection in bundle["collections"]:
            node_ids: list[str] = []
            for member in collection["members"]:
                asset_id, component_id = resolve_node_ref(bundle, member["ref"])
                node_ids.append(component_id or asset_id)
            uow.interchange.sync_collection(
                collection_key=collection["collection_key"],
                title=collection["title"],
                node_ids=node_ids,
            )
        uow.commit()


def export_current_accepted_snapshot(
    *,
    uow_factory: UnitOfWorkFactory,
) -> dict[str, Any]:
    """Export current accepted reusable knowledge as a validated deterministic bundle."""

    with uow_factory() as uow:
        snapshot = uow.interchange.export_current_accepted_snapshot()

    validate_bundle(snapshot)
    validate_import_safety(snapshot, trusted_accepted_snapshot=True)
    return normalize_bundle(snapshot)
