class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0] * (n+2)

        for i in range(n-1, -1, -1):
            take = nums[i] + dp[i+2]
            skip = dp[i+1]

            dp[i] = max(take, skip)
        
        return dp[0]

        # @lru_cache(maxsize=None)
        # def dp(i):
        #     if i >= n:
        #         return 0
            
        #     take = nums[i] + dp(i+2)
        #     skip = dp(i+1)

        #     return max(take, skip)
        