class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        def dfs(s):
            i = 0
            res = ""
            while i < len(s):
                if not s[i] == "%":
                    res += s[i]
                    i += 1
                else:
                    # check if the key that follows the first % has nested format specifiers
                    if "%" in graph[s[i+1]]:
                        graph[s[i+1]] = dfs(graph[s[i+1]])
                    res += graph[s[i+1]]
                    i += 3
            return res
        
        graph = defaultdict(str)
        for k, s in replacements:
            graph[k] = s
        
        return dfs(text)