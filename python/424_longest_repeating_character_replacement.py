class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uc = defaultdict(int)
        l = 0
        n = len(s)
        maxf = 0
        ans = 0
        for r in range(n):
            uc[s[r]] += 1
            maxf = max(maxf, uc[s[r]])
            # window length (r - l + 1) - frequency of most frequent element is the optimal amount of charatcers we can replace.
            # if this value exceeds k, shrink the window.
            while (r - l + 1) - maxf > k:
                uc[s[l]] -= 1
                if 0 >= uc[s[l]]:
                    del uc[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans