class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newpositions = {}
        n = len(nums)
        for i, v in enumerate(nums):
            newpositions[(i, v)] = (i + k) % n
        nums2 = nums.copy()

        for i in range(n):
            p = newpositions[(i, nums2[i])]
            nums[p] = nums2[i]