class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = -float('inf')
        n = len(intervals)
        heap = []
        for i in range(n):
            s, e = intervals[i]
            while heap and s >= heap[0][0]:
                heappop(heap)
            
            if not heap or s < heap[0][0]:
                heappush(heap, (e, s))
            
            res = max(res, len(heap))
        
        return res