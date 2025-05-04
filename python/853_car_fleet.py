class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])

        def meetBeforeTarget(p1, p2, v1, v2):
            finalpos = p1 + v1 * ((p2 - p1)/(v1-v2))
            return finalpos <= target
        
        n = len(position)
        st = []
        for i in range(n):
            while st and st[-1][1] > cars[i][1] and meetBeforeTarget(st[-1][0], cars[i][0], st[-1][1], cars[i][1]):
                st.pop()
            st.append(cars[i])
        
        return len(st)
