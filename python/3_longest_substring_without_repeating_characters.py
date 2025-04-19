class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            seen[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans