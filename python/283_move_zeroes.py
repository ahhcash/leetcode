class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        for i in range(n):
            if not nums[i] == 0:
                nums[l] = nums[i]
                l += 1
        
        for i in range(l, n):
            nums[i] = 0