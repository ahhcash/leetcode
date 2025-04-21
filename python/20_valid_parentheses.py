class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        opentype = {"(", "{", "["}
        for c in s:
            if c in opentype:
                st.append(c)
            else:
                matched = st \
                and ((c == ")" and st[-1] == "(") \
                or (c == "}" and st[-1] == "{") \
                or (c == "]" and st[-1] == "["))
                if matched:
                    st.pop()
                else:
                    return False
        return len(st) == 0