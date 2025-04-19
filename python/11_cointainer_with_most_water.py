class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        ans = 0
        while l <= r:
            if height[l] < height[r]:
                area = height[l] * (r-l)
                l += 1
            else:
                area = height[r] * (r-l)
                r -= 1
            ans = max(ans, area)
        return ans