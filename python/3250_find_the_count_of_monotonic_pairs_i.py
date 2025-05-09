class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        @lru_cache(maxsize=None)
        def dp(i, lo, hi):
            if i == n:
                return 1
            ans = 0
            for k in range(lo, nums[i]+1):
                a = k
                b = nums[i] - k
                if a < 0 or b < 0:
                    continue
                print(f"a: {a}\tb: {b}")
                if lo <= a and b <= hi:
                    ans = (ans+dp(i+1, a, b)) % mod
            
            return ans
        
        return dp(0, 0, 50)
