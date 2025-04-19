class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(ss, l, r):
            return ss[l:r+1] == ss[l:r+1][::-1]
        
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l] == s[r]:
                return palindrome(s, l+1, r) or palindrome(s, l, r-1)
            l += 1
            r -= 1
        return True
