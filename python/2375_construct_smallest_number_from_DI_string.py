class Solution:
    def smallestNumber(self, pattern: str) -> str:
        st = []
        n = len(pattern)
        ans = ""
        for i in range(n+1):
            st.append(i+1)
            # print(st)
            if i == n or pattern[i] == 'I':
                # if i == n:
                #     # print(f"i is {n}, popping stack: {st}")
                # else:
                #     # print(f"pattern[i] is I, popping stack: {st}")
                while st:
                    ans += str(st.pop())
        return ans