class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {"+", "-", "*", "/"}
        for val in tokens:
            # print(st)
            if val in operators:
                op1 = st.pop()
                op2 = st.pop()

                if val == "+":
                    st.append(op1 + op2)
                elif val == "-":
                    st.append(op2 - op1)
                elif val == "*":
                    st.append(op1 * op2)
                else:
                    st.append(int(op2 / op1))
            else:
                st.append(int(val))
        # print(st)
        return st[0]