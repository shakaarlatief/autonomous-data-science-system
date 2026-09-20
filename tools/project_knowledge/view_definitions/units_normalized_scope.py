"""Data-only pure-unit declarations shared by more than one view.

Read as a literal from a view's own committed implementation blobs; never imported by the bound worker.
"""

PURE_UNITS = (
    ('normalized_scope.v1', 'tools/project_knowledge/pure_normalized_scope.py', 'normalized_scope', (('unique', 'unique_values.v1'),), ('sorted_values', 'is_text')),
)
