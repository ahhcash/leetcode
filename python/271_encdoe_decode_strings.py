class Codec:
    SPECIAL: str = "#"
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            l = len(s)
            res += (str(l) + Codec.SPECIAL + s)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            si = s.find(Codec.SPECIAL, i)
            l = int(s[i:si])
            res.append(s[si+1:si+1+l])
            i = si+1+l
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))