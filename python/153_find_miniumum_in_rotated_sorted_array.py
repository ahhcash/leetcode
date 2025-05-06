class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[-1]:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return nums[res]