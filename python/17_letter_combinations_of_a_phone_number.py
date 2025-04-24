class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lettermap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9":  "wxyz"
        }
        n = len(digits)
        res = []
        def dfs(i, curr):
            nonlocal res
            if i == n:
                if curr:
                    res.append(curr)
                return
            for j in lettermap[digits[i]]:
                dfs(i+1, curr+j)
        
        dfs(0, "")
        return res