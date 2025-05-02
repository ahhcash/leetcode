class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        n = len(nums)
        ll, r = -1, n-1
        for i in range(n):
            if nums[i] == target:
                ll = i
                break
        
        l = ll
        last = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                last = m
                l = m + 1
            else:
                r = m - 1
        
        return [ll, last]