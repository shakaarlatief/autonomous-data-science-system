PHRASES = (
    "must", "shall", "required", "requires", "may not", "cannot",
    "only after", "only if", "remain blocked", "remains blocked",
    "prohibited", "prohibit", "invalid", "before"
)

def classify(text):
    s=text.lower()
    return "LEAK" if any(p in s for p in PHRASES) else "NO_LEAK"
