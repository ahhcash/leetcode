class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        @lru_cache(maxsize=None)
        def dp(i, r):
            if i >= r:
                return 0
            
            take = nums[i] + dp(i+2, r)
            skip = dp(i+1, r)

            return max(take, skip)
        
        return max(dp(0, n-1), dp(1, n))