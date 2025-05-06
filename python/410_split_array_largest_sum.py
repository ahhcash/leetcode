class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splittableIntoK(maxsum):
            c = 1
            curr = 0
            for i, v in enumerate(nums):
                if c > k:
                    return False
                if curr + v <= maxsum:
                    curr += v
                else:
                    c += 1
                    curr = v
            return c <= k
        
        l, r = max(nums), sum(nums)
        res = l
        while l <= r:
            m = (l + r) // 2
            if splittableIntoK(m):
                res = m
                r = m - 1
            else:
                l = m + 1
            
        return res