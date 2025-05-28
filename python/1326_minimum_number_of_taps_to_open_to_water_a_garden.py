class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [0] * (n + 1)
        for i, v in enumerate(ranges):
            l, r = max(0, i - v), min(n, i + v)
            # print(f"for range {i}, l = {l}, r = {r}")
            # if the same index is overalpped, take the maximum possible value we can get for this index
            intervals[l] = max(intervals[l], r)
        curr = next = 0
        ans = 0
        for i in range(n+1):
            # if we ever cross the maximum possible reach in our garden
            if i > next:
                return -1
            
            if i > curr:
                ans += 1
                curr = next
            # if the reach of the current index is greater than the max reach of the current one, keep the same thing because we want to minimise the taps
            next = max(next, intervals[i])
        return ans