from functools import cache

def match(text: str, pattern: str) -> bool:
    n = len(text)
    p = len(pattern)
    
    @cache
    def dp(i, k):
        if k == p:
            return i == n
        if i == n:
            return k == p or (pattern[k-2] == '?' and dp(i, k+2))

        if text[i] == pattern[k] or pattern[k] == '.':
            return dp(i+1, k+1)
        elif pattern[k] == '?':
            return dp(i, k+1) or dp(i, k+2)
        elif pattern[k] == '*':
            stay = text[i] == pattern[k+1] and dp(i+1, k) 
            skip = dp(i, k+2)
            return stay or skip
        else:
            return False
    
    return dp(0, 0)

# test case 1
text = "doooooooog"
pattern = "d*og"
print(f"match: {match(text, pattern)}")

# test case 2
text = "dg"
pattern = "d*og"
print(f"match: {match(text, pattern)}")

