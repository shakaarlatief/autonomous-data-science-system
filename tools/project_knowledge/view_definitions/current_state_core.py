"""View definition: specification and view-private pure-unit declarations for `current_state_core`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


def current_state_core_specification() -> ViewSpecification:
    """Research 185 orientation projection; no publication or authority switch.

    All canonical profiles participate so references can resolve without a
    carrier-path registry. Unrelated sources can alter provenance membership,
    but only the explicit semantic roles influence the view's value."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/current_state_core.py",
        "tools/project_knowledge/view_definitions/units_current_state_core.py",
        "tools/project_knowledge/pure_current_state_core.py",
    )
    return ViewSpecification(
        "current_state_core", GENERATED_ROOT + "current_state_core.json",
        GENERATED_ROOT + "manifests/current_state_core.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_current_state_core", "1", files),
        "current_state_core.v1", "canonical_json.v1",
    )
