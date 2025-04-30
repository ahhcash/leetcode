class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        n = len(candidates)
        def dfs(i, curr):
            if i == n or curr > target:
                return
            if curr == target:
                res.append(sub.copy())
                return
            sub.append(candidates[i])
            dfs(i, curr + candidates[i])

            sub.pop()
            dfs(i+1, curr) 
        
        dfs(0, 0)

        return res