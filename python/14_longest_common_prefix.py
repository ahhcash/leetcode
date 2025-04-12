class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        i = 0
        n = len(strs)
        sl = float('inf')
        for i in range(n):
            if len(strs[i]) < sl:
                sl = len(strs[i])
        first = 0
        for i in range(n):
            if not len(strs[i]) == 0:
                first = i
                break
        def sameatindex(idx):
            f = strs[first][idx]
            for i in range(1, n):
                if strs[i][idx] != strs[i-1][idx]:
                    return False
            return True
        
        i = first
        res = ""
        while i < sl and sameatindex(i):
            res += strs[first][i]
            i += 1

        return res
