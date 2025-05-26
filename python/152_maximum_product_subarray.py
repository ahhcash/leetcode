class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        res = max(nums)
        curmax = curmin = 1
        for i, v in enumerate(nums):
            t = curmax
            curmax = max(curmax * v, curmin * v, v)
            curmin = min(t * v, curmin * v, v)

            res = max(res, curmax)
        
        return res
