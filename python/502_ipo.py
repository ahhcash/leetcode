class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        heap = []
        projects = sorted(zip(capital, profits), key=lambda x: (x[0], -x[1]))
        i = 0
        while k:
            while i < n and w >= projects[i][0]:
                heappush(heap, -projects[i][1])
                i += 1
            
            # print(f" heap: {heap}")
            if not heap:
                break
            w += -heappop(heap)
            k -= 1
        
        return w