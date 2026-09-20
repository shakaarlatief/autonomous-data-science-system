"""View definition: specification and view-private pure-unit declarations for `current_state_core_markdown`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('current_state_core_markdown.v1', 'tools/project_knowledge/pure_current_state_core_markdown.py', 'current_state_core_markdown', (), ('utf8_text', 'length', 'as_text')),
)


def current_state_core_markdown_specification() -> ViewSpecification:
    """Human deterministic representation of the same accepted current-state core."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/current_state_core_markdown.py",
        "tools/project_knowledge/view_definitions/units_current_state_core.py",
        "tools/project_knowledge/pure_current_state_core.py",
        "tools/project_knowledge/pure_current_state_core_markdown.py",
    )
    return ViewSpecification(
        "current_state_core_markdown", GENERATED_ROOT + "CURRENT_STATE_CORE.md",
        GENERATED_ROOT + "manifests/current_state_core_markdown.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_current_state_core_markdown", "1", files),
        "current_state_core.v1", "current_state_core_markdown.v1",
    )
