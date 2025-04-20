class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1ctr = Counter(s1)
        n = len(s2)
        m = len(s1)
        l = 0
        s2ctr = Counter()
        for r in range(n):
            s2ctr[s2[r]] += 1
            if r - l + 1 > m:
                s2ctr[s2[l]] -= 1
                if 0 >= s2ctr[s2[l]]:
                    del s2ctr[s2[l]]
                l += 1
            
            if s1ctr == s2ctr:
                return True
    
        return False