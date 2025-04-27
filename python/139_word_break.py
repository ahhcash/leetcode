class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)

        # dp = [False] * (n+1)
        # dp[n] = True
        # for i in range(n-1, -1, -1):
        #     for word in wordDict:
        #         if i + len(word) <= n and s[i:i+len(word)] == word and dp[i+len(word)]:
        #             dp[i] = True
        #             break
        # return dp[0]
        res = []
        @lru_cache(maxsize=None)
        def dp(i, curr):
            if i == n:
                return curr in wordDict or curr == ""
            
            curr += s[i]
            if dp(i+1, curr):
                return True
            elif curr in wordDict: #break it up and try the the rest
                return dp(i+1, "")
            
            return False
        ans =  dp(0, "")
        return ans