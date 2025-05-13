class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        ans = 0
        lefts = [-1] * n
        rights = [n] * n
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if st:
                lefts[i] = st[-1]
            st.append(i)
        
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if st:
                rights[i] = st[-1]

            st.append(i)
        for i in range(n):
            width = rights[i] - lefts[i] - 1
            area = heights[i] * width
            ans = max(ans, area)

        return ans