"""Host-side catalog of view definitions; never part of any view's bound closure.

Each view definition module owns its specification and view-private unit
declarations. Only the bound worker's TCB decides generation semantics, and it
reads unit declarations from a view's own committed implementation blobs.
"""

from ..model import ViewSpecification
from . import (
    authority_index, current_state_core, current_state_core_markdown, identity_index,
    risk_obligation_index, source_catalog, source_inventory, subject_index, units_current_state_core,
    units_normalized_scope, units_temporal, units_unique_values, workstream_graph,
)

from .authority_index import authority_index_specification
from .current_state_core import current_state_core_specification
from .current_state_core_markdown import current_state_core_markdown_specification
from .identity_index import identity_index_specification
from .risk_obligation_index import risk_obligation_index_specification
from .source_catalog import source_catalog_specification
from .source_inventory import source_inventory_specification
from .subject_index import subject_index_specification
from .workstream_graph import workstream_graph_specification

DECLARATION_MODULES = (
    authority_index, current_state_core_markdown, identity_index, risk_obligation_index, source_catalog,
    source_inventory, subject_index, units_current_state_core, units_normalized_scope, units_temporal,
    units_unique_values, workstream_graph,
)

# Host-side aggregate for tests and tooling; the worker never sees this object.
PURE_UNIT_REGISTRY = tuple(record for module in DECLARATION_MODULES for record in module.PURE_UNITS)


def production_view_specifications() -> tuple[ViewSpecification, ...]:
    """The eight persistent W0 artifacts required by Specification 028."""
    return (
        source_catalog_specification(),
        identity_index_specification(),
        authority_index_specification(),
        workstream_graph_specification(),
        subject_index_specification(),
        risk_obligation_index_specification(),
        current_state_core_specification(),
        current_state_core_markdown_specification(),
    )
