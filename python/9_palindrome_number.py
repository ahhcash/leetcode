class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res = 0
        t = x
        while x:
            x, rem = divmod(x, 10)
            res = res * 10 + rem
        return res == t