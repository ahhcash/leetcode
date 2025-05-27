class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            mins.append(h * 60 + m)
        
        total = 24*60
        mins.sort()
        ans = total - mins[-1] + mins[0]
        for i in range(1, len(mins)):
            ans = min(ans, mins[i] - mins[i-1])
        return ans