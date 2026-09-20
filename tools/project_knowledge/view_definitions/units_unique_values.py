"""Data-only pure-unit declarations shared by more than one view.

Read as a literal from a view's own committed implementation blobs; never imported by the bound worker.
"""

PURE_UNITS = (
    ('unique_values.v1', 'tools/project_knowledge/pure_unique_values.py', 'unique_values', (), ('sorted_values',)),
)
