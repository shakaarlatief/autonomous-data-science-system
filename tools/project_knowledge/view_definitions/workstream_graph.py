"""View definition: specification and view-private pure-unit declarations for `workstream_graph`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('workstream_dependency_closure.v1', 'tools/project_knowledge/pure_workstream_graph.py', 'workstream_dependency_closure', (('unique', 'unique_values.v1'),), ('length', 'fail_view')),
    ('workstream_parent_chain.v1', 'tools/project_knowledge/pure_workstream_graph.py', 'workstream_parent_chain', (), ('length', 'fail_view')),
    ('workstream_node.v1', 'tools/project_knowledge/pure_workstream_graph.py', 'workstream_node', (('dependency_closure', 'workstream_dependency_closure.v1'), ('parent_chain', 'workstream_parent_chain.v1'), ('unique', 'unique_values.v1'), ('temporal', 'has_temporal_control.v1')), ('length', 'fail_view')),
    ('workstream_graph.v1', 'tools/project_knowledge/pure_workstream_graph.py', 'workstream_graph', (('unique', 'unique_values.v1'), ('node', 'workstream_node.v1')), ('sorted_values', 'any_true', 'length', 'fail_view')),
)


def workstream_graph_specification() -> ViewSpecification:
    """Persistent workstream/navigation projection over the current canonical corpus."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/workstream_graph.py",
        "tools/project_knowledge/view_definitions/units_temporal.py",
        "tools/project_knowledge/view_definitions/units_unique_values.py",
        "tools/project_knowledge/pure_workstream_graph.py",
        "tools/project_knowledge/pure_temporal.py",
        "tools/project_knowledge/pure_unique_values.py",
    )
    return ViewSpecification(
        "workstream_graph", GENERATED_ROOT + "workstream_graph.json",
        GENERATED_ROOT + "manifests/workstream_graph.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_workstream_graph", "1", files),
        "workstream_graph.v1", "canonical_json.v1",
    )
