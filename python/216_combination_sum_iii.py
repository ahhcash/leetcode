class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i for i in range(1, 10)]
        res = []
        sub = []
        def dfs(i, curr):
            if i >= n:
                return
            if len(sub) == k:
                if curr == n:
                    res.append(sub.copy())
                return
            
            for j in range(i, len(arr)):
                sub.append(arr[j])

                dfs(j+1, curr + arr[j])

                sub.pop()

            return res
        dfs(0, 0)

        return res