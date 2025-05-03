class Solution:
    def simplifyPath(self, path: str) -> str:
        path = filter(lambda v: not v == "", path.split("/"))

        st = []
        for v in path:
            if v == ".":
                continue
            elif v == "..":
                if st:    
                    st.pop()
            else:
                st.append(v)
        
        return "/" + "/".join(st)