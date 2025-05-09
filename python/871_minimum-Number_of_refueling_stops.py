class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        # stations.sort(key = lambda x:x[0])

        heap = []
        i = 0
        # technically startFuel * miles/liter = 1 in this case
        reach = startFuel
        prev = 0
        s = 0
        while reach < target:
            while i < n and stations[i][0] <= reach: # pass by every station on the way
                heappush(heap, -stations[i][1])
                i += 1
            
            if not heap:
                # couldn't pass by any station
                return -1
            
            best = -heappop(heap)
            reach += best
            s += 1
        
        return s

           
