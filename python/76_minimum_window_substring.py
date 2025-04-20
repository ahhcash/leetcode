class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_ctr = Counter(t)
        n = len(s)
        l = 0
        minl = float('inf')
        res = ""
        w_ctr = Counter()

        def contains(window):
            for k, v in t_ctr.items():
                if window[k] < v:
                    return False
            return True

        for r in range(n):
            w_ctr[s[r]] += 1
            while contains(w_ctr):
                if (r - l + 1) < minl:
                    minl = r- l + 1
                    res = s[l:r+1]
                w_ctr[s[l]] -= 1
                l += 1
        
        return res