class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        heapify(rooms)

        use = [0] * n
        meetings.sort(key=lambda x: x[0])

        heap = []
        for i in range(len(meetings)):
            s, e = meetings[i]
            duration = e - s

            while heap and s >= heap[0][0]:
                _, r = heappop(heap)
                heappush(rooms, r)
            
            if rooms:
                r = heappop(rooms)
                heappush(heap, (e, r))
                use[r] += 1
            else:
                earliest, r = heappop(heap)
                e = earliest + duration
                heappush(heap, (e, r))
                use[r] += 1
        
        return use.index(max(use))
            
