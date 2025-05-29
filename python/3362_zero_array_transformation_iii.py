class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(queries)
        queries.sort()
        heap = []
        diff = [0] * (len(nums)+1)
        ops = 0
        q = 0
        for i, v in enumerate(nums):
            ops += diff[i]
            while q <len(queries) and queries[q][0] == i:
                heappush(heap, -queries[q][1])
                q += 1
            
            while ops < v and heap and -heap[0] >= i:
                ops += 1
                diff[-heappop(heap) + 1] -= 1
            if ops < v: return -1
        return len(heap)

        
        

