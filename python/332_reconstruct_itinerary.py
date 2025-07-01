class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        outdeg = Counter()
        for fro, to in tickets:
            outdeg[fro] += 1
            graph[fro].append(to)
        
        for v in graph:
            graph[v].sort(reverse=True)
        
        ans = deque()
        def dfs(node):
            while outdeg[node]:
                outdeg[node] -= 1
                next = graph[node][outdeg[node]]
                dfs(next)
            ans.appendleft(node)
        dfs("JFK")
        return list(ans)