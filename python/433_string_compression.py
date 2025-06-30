class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars: return 0
        if len(chars) == 1: return 1

        k = i = 0
        n = len(chars)
        while i < n:
            curr = chars[i]
            c = 0
            while i < n and chars[i] == curr:
                c += 1
                i += 1
            chars[k] = curr
            k += 1
            if c > 1:
                for d in str(c):
                    chars[k] = d
                    k += 1
        return k
            


