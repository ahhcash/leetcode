class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 10**5
        ans = -inf
        curr = -inf
        for i, v in enumerate(nums):
            curr = max(curr + v, v)
            ans = max(ans, curr)
        
        return ans