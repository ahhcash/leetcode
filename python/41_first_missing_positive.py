class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # filter elements
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            # nums[i] will exist in an ideal array of size n with range [1...n]. so we just mark the index as negative, iff not marked already
            idx = abs(nums[i]) - 1
            if idx < n and nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        # finally, just check for any integers not makred. 1 + that integer is the answer
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # if everything is negative, n + 1 is the answer
        return n+1