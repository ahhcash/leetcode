class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        mx = max(nums)
        w = ans = 0
        for r in range(n):
            if nums[r] == mx:
                w += 1

            while l < n and w >= k:
                if nums[l] == mx:
                    w -= 1
                l += 1
            ans += l
        return ans
