"""View definition: specification and view-private pure-unit declarations for `source_inventory`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('source_inventory.v1', 'tools/project_knowledge/pure_source_inventory.py', 'source_inventory', (('entry', 'inventory_entry.v1'),), ()),
    ('inventory_entry.v1', 'tools/project_knowledge/pure_source_inventory.py', 'inventory_entry', (), ()),
)


def source_inventory_specification() -> ViewSpecification:
    """Small G009 structural view with its explicit implementation closure."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/source_inventory.py",
        "tools/project_knowledge/pure_source_inventory.py",
    )
    return ViewSpecification(
        "source_inventory", GENERATED_ROOT + "source_inventory.json",
        GENERATED_ROOT + "manifests/source_inventory.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_source_inventory", "1", files),
        "source_inventory.v1", "canonical_json.v1",
    )
