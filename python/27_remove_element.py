class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        c = 0
        while l < r:
            while r > l and nums[r] == val:
                r -= 1
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        
        for i in range(n):
            if not nums[i] == val:
                c += 1
        return c