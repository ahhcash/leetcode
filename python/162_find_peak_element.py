class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2

            if m+1 >= n or (m-1 >= 0 and nums[m-1] < nums[m] > nums[m+1]):
                return m
            elif nums[m-1] > nums[m+1]:
                r = m -1
            else:
                l = m+1

        return l