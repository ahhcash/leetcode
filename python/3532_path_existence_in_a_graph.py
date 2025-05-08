class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        parent = 0
        prev = 0
        for i in range(n):
            if abs(nums[i] - prev) > maxDiff:
                parent += 1
            prev = nums[i]
            nums[i] = parent
        return [nums[u] == nums[v] for u,v in queries]
        