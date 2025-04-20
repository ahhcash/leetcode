class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_ctr = Counter(t)
        reqd = len(t_ctr)
        n = len(s)
        l = 0
        inf = 10**5 + 1
        minl = inf
        mins = 0
        w_ctr = Counter()
        formed = 0
        for r in range(n):
            w_ctr[s[r]] += 1

            if t_ctr[s[r]] > 0 and t_ctr[s[r]] == w_ctr[s[r]]:
                formed += 1
            
            while l <= r and formed == reqd:
                if r - l + 1 < minl:
                    minl = r - l + 1
                    mins = l
                
                w_ctr[s[l]] -= 1
                if t_ctr[s[l]] > 0 and w_ctr[s[l]] < t_ctr[s[l]]:
                    formed -= 1
                l += 1
        
        return "" if inf == minl else s[mins:mins+minl]