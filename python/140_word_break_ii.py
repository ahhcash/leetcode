class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        @lru_cache(maxsize=None)
        def dp(i):
            if i == n:
                return [""]
            sub = []
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    remaining = dp(j)
                    curr = s[i:j]
                    for w in remaining:
                        if w:
                            sub.append(curr + " " + w)
                        else:
                            sub.append(curr)
            return sub
        return dp(0)
