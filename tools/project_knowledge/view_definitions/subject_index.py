"""View definition: specification and view-private pure-unit declarations for `subject_index`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('subject_memberships.v1', 'tools/project_knowledge/pure_subject_index.py', 'subject_memberships', (('unique', 'unique_values.v1'),), ('sorted_values', 'is_text')),
    ('subject_index.v1', 'tools/project_knowledge/pure_subject_index.py', 'subject_index', (('memberships', 'subject_memberships.v1'),), ('sorted_values',)),
)


def subject_index_specification() -> ViewSpecification:
    """Persistent multi-axis navigation memberships from profile/kind/scope metadata."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/subject_index.py",
        "tools/project_knowledge/view_definitions/units_unique_values.py",
        "tools/project_knowledge/pure_subject_index.py",
        "tools/project_knowledge/pure_unique_values.py",
    )
    return ViewSpecification(
        "subject_index", GENERATED_ROOT + "subject_index.json",
        GENERATED_ROOT + "manifests/subject_index.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_subject_index", "1", files),
        "subject_index.v1", "canonical_json.v1",
    )
