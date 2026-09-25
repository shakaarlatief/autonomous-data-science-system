# DRP-01 Semantic Annotation Packet V0.1

This packet supports Research 316 DRP-01.

The reviewer evaluates the frozen 30-carrier corpus at commit
`870689734673e6e8c2212035afcdf27daf733c15`.

## Purpose

Judge whether the V0.3 minimal shared semantic substrate can remain small and
seam-justified, and whether role/status semantics are practical on real mixed
ADS carriers.

Do not grade the candidate by preference. A primitive may be rejected. A role
model may fail. Existing paths and Research 217 have no preservation right.

## Carrier annotation

For each of the 30 corpus carriers:

1. Use the entire carrier as one semantic unit if it is genuinely homogeneous.
2. Split only when independently consequential meaning would otherwise mix
   different information roles or governing statuses.
3. Use a stable heading or JSON-field anchor.
4. Assign exactly one candidate role to each unit where possible.
5. Mark `irreducibly_multirole=true` only when further practical
   decomposition would destroy or distort the unit.
6. GOVERNING units receive a governing status. Other roles use null.
7. Record whether the classification required treating filesystem path as
   identity or authority. The expected method is semantic-content based; do
   not use path as authority.

Roles and provisional statuses are defined in definitions.json.

## Shared primitive annotation

For each candidate primitive:

- state a single canonical meaning;
- inspect every frozen seam S1-S9;
- mark whether consequential correctness requires the two domains to agree on
  that primitive's meaning;
- cite source anchors supporting the seam judgment;
- mark any semantic incompatibility explicitly;
- admit the primitive only if the evidence supports a genuinely shared
  cross-domain contract, not generic reuse convenience.

A shared primitive should normally have at least two consequential seam
citations, but the reviewer must not force this threshold. Report the evidence
and let the frozen harness classify the result.

## Negative controls

Judge the four domain-internal concepts independently. Do not reject them
merely because they are labeled negative controls. If the evidence really
shows two or more consequential domains must share their exact semantics,
admit them and explain why. The harness will then produce the preregistered
architecture consequence.

## Independence

Two semantic annotations are required before scoring:

- ChatGPT annotation;
- Claude annotation.

Each must be frozen without reading the other's annotation.

The final harness compares both reviewer results. The point is reproducibility,
not consensus pressure.

## Output

Use annotation_schema.json exactly.

Rationales should be concise but technically specific. Source references use:

    repository/path::heading-or-json-field

Do not include long copied passages.
