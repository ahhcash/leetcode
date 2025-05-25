class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i+1)

            sub.pop()
            dfs(i+1)
        dfs(0)

        return res