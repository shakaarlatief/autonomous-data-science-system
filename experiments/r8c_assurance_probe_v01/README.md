# R8-C Assurance Decision Probe Harness

Temporary research/qualification machinery for the decision-relevant R8-C probes preregistered in Research 277.

This directory is evidence infrastructure only. It has no target-architecture preservation right.

## P-D6

`p_d6_executor_capability.py` tests executor-capability versus trust separation.

## P-D3

`p_d3_boundary_independence.py` implements the preregistered two-layer Product/JW1 boundary-independence probe. It binds both the harness commit and a frozen source commit, performs explicit-import scans, executes current-shaped and target-shaped isolated fixtures, and includes forbidden-dependency injection controls.

Every concrete probe harness must be committed and Git-blob-hash frozen before execution.
