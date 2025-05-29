class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)

        l, r = 0, n - 1

        def repeats(ll):
            seen = set()
            for i in range(n-ll+1):
                sub = s[i:i+ll]

                if sub in seen:
                    return True
                seen.add(sub)

            return False
        
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if repeats(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans