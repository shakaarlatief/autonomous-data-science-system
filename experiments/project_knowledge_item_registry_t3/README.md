# W5 T3: Item-Registry Identity and Carrier Experiment

**Status:** Frozen non-authoritative research fixture before execution
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Authority:** Research fixture only. It does not migrate live decisions/backlog items or change the declaration substrate.

## Purpose

T3 tests the item-registry problem identified in Research 208 and MC-0018:

```text
aggregate files such as DECISIONS.md / OPEN_ARCHITECTURE_BACKLOG.md
    can contain independently governed items

but

V1 typed relations target semantic IDs
and
the current Markdown declaration parser admits one declaration per carrier
```

The experiment compares:

```text
A  selective per-item carrier + semantic ID
B  multiple declaration blocks in one aggregate carrier
C  aggregate carrier + anchor-only item identity
```

## Real cases

`D-011` is the primary hard case because it retains residual applicability while seven later decisions supersede different scopes.

`AB-032` is the secondary case because W4 already had to refer to it as a path-plus-heading anchor even though it has an independent lifecycle and could later need first-class typed reference.

## Mechanical checks

The evaluator uses the production schema validator, declaration parser and authority resolver.

It checks that:

- A resolves every scoped D-011 successor and the residual D-011 base;
- A lets AB-032 satisfy a required semantic identity when represented as its own carrier;
- B is rejected by the current parser, quantifying that it is a substrate redesign rather than a free encoding choice;
- C cannot resolve a typed relation target to anchor-only D-011;
- C cannot satisfy required first-class identity for anchor-only AB-032.

No live repository carriers are changed.

## Output

Running:

```powershell
.\.venv\Scripts\python.exe experiments/project_knowledge_item_registry_t3/evaluate.py
```

materializes `result.json` as non-authoritative research output.
