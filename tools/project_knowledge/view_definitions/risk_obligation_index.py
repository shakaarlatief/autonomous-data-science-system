"""View definition: specification and view-private pure-unit declarations for `risk_obligation_index`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('obligation_rows.v1', 'tools/project_knowledge/pure_risk_obligation_index.py', 'obligation_rows', (), ('sequence_range', 'length')),
    ('risk_obligation_index.v1', 'tools/project_knowledge/pure_risk_obligation_index.py', 'risk_obligation_index', (('unique', 'unique_values.v1'), ('obligations_for', 'obligation_rows.v1')), ('sorted_values',)),
)


def risk_obligation_index_specification() -> ViewSpecification:
    """Persistent source-owned risk/reopen and obligation projection."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/risk_obligation_index.py",
        "tools/project_knowledge/view_definitions/units_unique_values.py",
        "tools/project_knowledge/pure_risk_obligation_index.py",
        "tools/project_knowledge/pure_unique_values.py",
    )
    return ViewSpecification(
        "risk_obligation_index", GENERATED_ROOT + "risk_obligation_index.json",
        GENERATED_ROOT + "manifests/risk_obligation_index.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_risk_obligation_index", "1", files),
        "risk_obligation_index.v1", "canonical_json.v1",
    )
