class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        freq = [0] * 26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        # def printfreq(f):
        #     for i, v in enumerate(f):
        #         print(f"{chr(i+ord('a'))}: {v}", end=" ")
        #     print()

        while t:
            # print("befiore: ")
            # printfreq(freq)
            nxt = [0] * 26
            for c in range(26):
                if freq[c]:
                    # print(f"transforiming: {chr(c+ord('a'))} into the next {nums[c]} chars")
                    for i in range(nums[c]):
                        ni = (c+1+i) % 26
                        nxt[ni] += freq[c]
            
            # print("after: ")
            # printfreq(nxt)
            freq = nxt
            t -= 1
        return (sum(freq) % mod)

