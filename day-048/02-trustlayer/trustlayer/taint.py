import re
PATTERNS=(r'ignore (?:all |the )?(?:previous|prior) instructions',r'override (?:the )?(?:policy|system)',r'\bsystem message\b',r'exfiltrat',r'reveal (?:the )?(?:secret|token|key)',r'bypass (?:approval|security)')
def inspect_text(text):
    return [p for p in PATTERNS if re.search(p,str(text),re.I)]