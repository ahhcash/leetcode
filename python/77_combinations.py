class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        sub = []
        def dfs(i):
            if i == n:
                if len(sub) == k:
                    res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i+1)

            sub.pop()
            dfs(i+1)
        dfs(0)
        return res