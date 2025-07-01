class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r, common = 0, 10 ** 10, lcm(divisor1, divisor2)

        ans = -1
        while l <= r:
            m = (l+r) // 2
            d1 = m - m//divisor1 >= uniqueCnt1 # largest value for divisor1 with uniqueCnt1 elements
            d2 = m - m//divisor2 >= uniqueCnt2
            c = m - m//common >= (uniqueCnt1 + uniqueCnt2)

            if d1 and d2 and c:
                # try smaller
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans
