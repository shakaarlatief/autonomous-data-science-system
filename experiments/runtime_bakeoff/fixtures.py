"""Deterministic ADS-shaped fixture for Specification 005."""

from __future__ import annotations

from .harness import (
    KnowledgeRevisionRef,
    MethodologicalContextPack,
    ProjectContextSnapshot,
    RuntimeWorkloadInput,
)


def representative_workload(*, run_id: str = "runtime-bakeoff-001") -> RuntimeWorkloadInput:
    project = ProjectContextSnapshot(
        project_id="customer-churn-prediction",
        snapshot_id="project-snapshot-runtime-001",
        facts={
            "prediction_moment": "Before the retention-contact decision for the coming billing cycle.",
            "production_missingness": "Several support and billing-derived features can be absent or delayed at scoring time.",
            "validation_design": "Chronological validation is currently selected.",
        },
    )
    context_pack = MethodologicalContextPack(
        pack_id="mh-runtime-missingness-validation-001",
        revisions=(
            KnowledgeRevisionRef(
                asset_key="prediction-moment-information-availability",
                revision_id="kr-prediction-moment-r1",
            ),
            KnowledgeRevisionRef(
                asset_key="production-missingness",
                revision_id="kr-production-missingness-r2",
            ),
            KnowledgeRevisionRef(
                asset_key="chronological-validation",
                revision_id="kr-chronological-validation-r1",
            ),
        ),
        rationale=(
            "The prediction moment is unresolved enough to affect admissible feature information.",
            "Production missingness may differ from development missingness.",
            "Validation should reproduce information availability at the intended decision time.",
        ),
        hard_constraints=(
            "Do not use information unavailable at the prediction moment.",
            "Do not create authoritative project state without approval.",
        ),
    )
    return RuntimeWorkloadInput(
        run_id=run_id,
        user_intent="What should we investigate next about missingness and validation?",
        project=project,
        context_pack=context_pack,
    )


REFERENCE_FIXTURE = {
    "missingness validation leakage": (
        "Treat production-time feature availability as part of the prediction contract; "
        "validation must not rely on values that will be absent or delayed when scoring occurs."
    )
}
