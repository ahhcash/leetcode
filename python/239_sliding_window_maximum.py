class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        prevmax = prevpos = None
        n = len(nums)
        res = []
        l = 0
        q = deque()
        for r in range(n):
            if q and q[0] <= r - k:
                q.popleft()
            
            # i suck unfortunately

            #pop from the back to maintain a monotonically decreasing queue
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            
            q.append(r)

            if r >= k - 1:
                res.append(nums[q[0]])
            

        return res