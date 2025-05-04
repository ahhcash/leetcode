class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def decode(ss):
            nonlocal i
            res = ""
            while i < len(ss) and not ss[i] == "]":
                if not ss[i].isdigit():
                    res += ss[i]
                    i += 1
                else:
                    num = ""
                    while i < len(ss) and ss[i].isdigit():
                        num += ss[i]
                        i += 1
                    print(num)
                    # skip open bracket
                    i += 1
                    inner = decode(ss)

                    # skip close bracket
                    i += 1

                    res += (int(num) * inner)
            return res
        return decode(s)