class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        res = 0
        for op in operations:
            if op == "C":
                res -= st[-1]
                st.pop()
            elif op == "D":
                res += 2*st[-1]
                st.append(2*st[-1])
            elif op == "+":
                res += (st[-1] + st[-2])
                st.append(st[-1] + st[-2])
            else:
                res += int(op)
                st.append(int(op))

        return res