class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()
        n = len(candidates)
        def dfs(i, curr):
            if curr == target:
                res.append(sub.copy())
                return
            elif i == n or curr > target:
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                sub.append(candidates[j])
                dfs(j+1, curr +candidates[j])
                sub.pop()
                # loop handles the skip branch of the tree
        
        dfs(0, 0)

        return res