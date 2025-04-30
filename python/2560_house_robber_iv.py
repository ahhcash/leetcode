class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def robcount(mid):
            i = 0
            res = 0
            while i < n:
                if nums[i] <= mid:
                    res += 1
                    i += 2
                else:
                    i += 1
            return res
        
        l = min(nums)
        r = max(nums)
        res = -1
        while l <= r:
            m = (l + r) // 2
            v = robcount(m)
            if v >= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res