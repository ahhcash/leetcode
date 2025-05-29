class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        ans = 0
        f = 0
        o = 0
        for r in range(n):
            if nums[r] == 1:
                o += 1
            else:
                f += 1
            
            while l <= r and f > k:
                if nums[l] == 0: 
                    f -= 1
                else:
                    o -= 1
                l += 1
            
            ans = max(ans, o+f)
        
        return ans