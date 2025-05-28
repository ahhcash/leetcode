class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev = None
        for i in range(len(intervals)):
            if not prev:
                prev = intervals[i]
            else:
                ps, pe = prev
                s, e = intervals[i]
                if s < pe:
                    return False
                prev = intervals[i]
        
        return True