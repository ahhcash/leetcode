class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = ['u'] * numCourses
        graph = defaultdict(list)

        for p, c in prerequisites:
            graph[p].append(c)
        
        res = []
        def dfs(i):
            nonlocal res
            if vis[i] == 'e':
                return False
            
            if vis[i] == 'c':
                return True
            vis[i] = 'e'
            for n in graph[i]:
                if not dfs(n):
                    return False
            
            vis[i] = 'c'
            res.append(i)
            return True
        
        for c in range(numCourses):
            if vis[c] == 'u':
                if not dfs(c):
                    return []
        return res