# OPERATIVE SP-4 detector packet

## Task

Each item is a short excerpt placed in the recital / non-operative part of an otherwise accepted governing artifact.

Classify the excerpt as LEAK or NO_LEAK.

LEAK means the excerpt itself asserts a current binding machine-relevant consequence that would need an accepted operative clause or exact domain-contract/control reference if the Project system is expected to act on it deterministically.

NO_LEAK means the excerpt is rationale, evidence, history, quotation, description of an already-existing rule, rejected or hypothetical possibility, example syntax, prediction, open research question, or a human-governing principle that deliberately has no direct deterministic machine consequence.

Important distinctions:

1. Normative-looking words are not sufficient for LEAK.
2. A sentence can be genuinely important to humans and still be NO_LEAK if it is deliberately outside claimed machine-operational meaning.
3. Merely describing an already-authoritative operative rule is NO_LEAK; the authority remains in the referenced rule.
4. Hypothetical, rejected, quoted, illustrative, historical, or explanatory language is NO_LEAK.
5. If the excerpt itself establishes a gate, prohibition, authorization, required effect, sequence, lifecycle condition, or machine-validity rule that a consumer would otherwise have to infer from recital text, classify LEAK.
6. Do not repair or rewrite the excerpt. Only classify what it does in context.

## Output

Follow annotation_schema.json exactly.

Use one pass over all items.

Do not inspect evaluator_key.json, lexical_baseline.py, score_sp4.py, or any result derived from them before committing your annotation.
