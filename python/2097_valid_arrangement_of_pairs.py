class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        outdeg = Counter()
        #every node will have an outdeg of 1 and indeg of 1 *except* the starting node
        # we need to determine that one node that has a NET outdeg of 1
        for start, end in pairs:
            outdeg[start] += 1
            outdeg[end] -= 1
            graph[start].append(end)
        
        q = deque()
        # recursive hierholzer's algorithm
        def dfs(node):
            while graph[node]:
                next = graph[node].pop()
                dfs(next)
            q.appendleft(node)
        
        # iterative hierholzer's algorithm
        def idfs(node):
            st = [node]
            while st:
                node = st[-1]
                if not graph[node]:
                    q.appendleft(node)
                    st.pop()
                else:
                    next = graph[node].pop()
                    st.append(next)
            
        start = pairs[0][0]
        for n, d in outdeg.items():
            if d == 1:
                start = n
                break
        idfs(start)

        ans = []
        n = len(q)
        for i in range(n-1):
            ans.append([q[i], q[i+1]])
        return ans