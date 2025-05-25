class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n+1)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        
        curr = 0
        for d, v in zip(diff, nums):
            curr += d
            if curr < v:
                return False
        
        return True