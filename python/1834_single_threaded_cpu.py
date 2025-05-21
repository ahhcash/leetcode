class Solution:
    def getOrder(self, tasks: List[List[int]]) ->  List[int]:
        tasks = sorted((eq, pt, i) for i, (eq, pt) in enumerate(tasks))
        t = 0
        n = len(tasks)
        res = []
        heap = []
        i = 0
        while i < n:
            eq, pt, _ = tasks[i]
            if not heap and t < eq:
                t = eq
            
            while i < n and tasks[i][0] <= t:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            npt, idx = heappop(heap)
            t += npt
            res.append(idx)
        
        while heap:
            _, idx = heappop(heap)
            res.append(idx)
        
        return res