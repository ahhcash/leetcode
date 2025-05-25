class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        n = len(trips)
        curr = 0
        prev = None
        # print(trips)
        heap = []
        for i in range(n):
            # print(f"heap: {heap}")
            num, fro, to = trips[i]
            # print(f"at {num}, {fro}, {to}")
            while heap and heap[0][0] <= fro:
                # print(f"{heap[0][0]} disembarked")
                curr -= heappop(heap)[2]
                # print(f"{curr} left")
            
            curr += num
            # print(f"{curr} entered total")
            if curr > capacity:
                return False
            heappush(heap, (to, fro, num))            

        return True