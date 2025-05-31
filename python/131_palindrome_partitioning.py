class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def pal(ss):
            return ss == ss[::-1]
        
        n = len(s)
        def dfs(i, sub):
            if i == n:
                res.append(sub.copy())
                return
            
            for l in range(i+1, n+1):
                if pal(s[i:l]):
                    sub.append(s[i:l])
                    dfs(l, sub)
                    sub.pop()
        dfs(0, [])
        return res

