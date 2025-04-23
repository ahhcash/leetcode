class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        n = len(strs)
        min_len = min(len(s) for s in strs)

        idx = 0
        while idx < min_len:
            # define a reference charatcer
            ref_char = strs[0][idx]
            for j in range(1, n):
                if not strs[j][idx] == ref_char:
                    return strs[0][:idx]
            idx += 1
        
        return strs[0][:min_len]
