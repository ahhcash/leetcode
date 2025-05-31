class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        f = Counter(nums)
        n = len(nums)
        res = []
        sub = []
        def dfs():
            if len(sub) == n:
                res.append(sub.copy())
                return
            
            for v in f:
                if f[v]:
                    sub.append(v)
                    f[v] -= 1

                    dfs()

                    f[v] += 1
                    sub.pop()
        
        dfs()
        return list(res)