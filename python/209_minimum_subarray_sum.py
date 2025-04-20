class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        inf = 10**5 + 1
        ans = inf
        tc = 0
        for r in range(n):
            tc += nums[r]

            while tc >= target:
                ans = min(ans, r - l + 1)
                tc -= nums[l]
                l += 1
        return ans if not ans == inf else 0