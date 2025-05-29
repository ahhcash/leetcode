class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26
        mod = 10 ** 9 + 7
        res = 0
        for c in s:
            freq[ord(c)-ord('a')] += 1
        while t:
            # print(f"freq: {freq}")
            nxt = [0] * 26
            nxt[0] = freq[-1]
            nxt[1] = (freq[0] + freq[-1]) % mod
            for c in range(2, 26):
                nxt[c] = freq[c-1]
            freq = nxt
            t -= 1
        res = sum(freq) % mod
        return res
