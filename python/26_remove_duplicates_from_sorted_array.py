class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq = [0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            unq.append(i)
        
        for i, v in enumerate(unq):
            nums[i] = nums[v]

        return len(unq)