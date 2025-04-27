class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def oppositedir(a, b, idxa, idxb):
            return (a < 0 and b > 0 and idxa > idxb)
        st = []
        for i, ast in enumerate(asteroids):
            st.append((i, ast))
            while len(st) >= 2 and oppositedir(st[-1][1], st[-2][1], st[-1][0], st[-2][0]):
                i1, top1 = st.pop()
                i2, top2 = st.pop()
                if abs(top1) > abs(top2):
                    st.append((i1, top1))
                elif abs(top1) < abs(top2):
                    st.append((i2, top2))

        return [v for _, v in st]