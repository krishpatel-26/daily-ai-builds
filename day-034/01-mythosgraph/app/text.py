import re
def tokens(value):return set(re.findall(r"[a-z0-9_']+",(value or "").lower()))
def similarity(query,text):
 a,b=tokens(query),tokens(text)
 return len(a&b)/max(1,len(a|b))