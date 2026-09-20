"""View definition: specification and view-private pure-unit declarations for `source_catalog`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('catalog_entry.v1', 'tools/project_knowledge/pure_source_catalog.py', 'catalog_entry', (('normalize_scope', 'normalized_scope.v1'),), ()),
    ('source_catalog.v1', 'tools/project_knowledge/pure_source_catalog.py', 'source_catalog', (('catalog', 'catalog_entry.v1'),), ()),
)


def source_catalog_specification() -> ViewSpecification:
    """Persistent governed-source catalog required by Specification 028."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/source_catalog.py",
        "tools/project_knowledge/view_definitions/units_normalized_scope.py",
        "tools/project_knowledge/view_definitions/units_unique_values.py",
        "tools/project_knowledge/pure_source_catalog.py",
        "tools/project_knowledge/pure_normalized_scope.py",
        "tools/project_knowledge/pure_unique_values.py",
    )
    return ViewSpecification(
        "source_catalog", GENERATED_ROOT + "source_catalog.json",
        GENERATED_ROOT + "manifests/source_catalog.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_source_catalog", "1", files),
        "source_catalog.v1", "canonical_json.v1",
    )
