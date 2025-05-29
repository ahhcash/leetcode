class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        sub = []
        def dfs(i):
            res.append(sub.copy())
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]: continue
                sub.append(nums[j])
                dfs(j+1)
                sub.pop()
        dfs(0)
        return res