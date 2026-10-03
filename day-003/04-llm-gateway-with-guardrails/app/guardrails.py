import re
PATTERNS=[r'ignore (all|any|previous) instructions',r'reveal (the|your) system prompt',r'bypass (the|all) safety']
def inspect(prompt):
 hits=[p for p in PATTERNS if re.search(p,prompt.lower())]; return len(hits)==0,hits
