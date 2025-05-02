class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * (n+1)
        for i in range(n):
            res[i+1] = res[i] * nums[i]
        r = 1
        for i in range(n-1, -1, -1):
            res[i+1] = res[i]*r
            r *= nums[i]
         
        return res[1:]