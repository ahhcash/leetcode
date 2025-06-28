class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0
        
        l, r = 0, 0
        s = 0
        ans = 0
        while r < n:
            if r >= k:
                if s / k >= threshold:
                    ans += 1
                s -= arr[l]
                l += 1
            s += arr[r]
            r += 1
        return ans + int(s/k >= threshold)