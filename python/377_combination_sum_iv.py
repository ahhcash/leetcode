class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(remaining):
            if remaining == 0:
                return 1
            
            ans = 0
            for v in nums:
                if remaining - v >= 0:
                    ans += dp(remaining - v)
            
            return ans
        
        return dp(target)