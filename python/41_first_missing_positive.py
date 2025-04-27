class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        
        for i in range(n):
            ideal_index = abs(nums[i]) - 1
            if ideal_index < n and nums[ideal_index] > 0:
                nums[ideal_index] = -nums[ideal_index] # remove from contention
        
        for i in range(n):
            if nums[i] > 0:
                # nobody has marked the ith index to be negative so the value i which would be present in the ideal array [1...n] is the answer (technically i+1 because we want the integer itself and i is the index)
                return i + 1
        
        return n+1