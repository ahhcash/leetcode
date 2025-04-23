class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i, v in enumerate(nums):
            if len(heap) < k:
                heappush(heap, v)
            else:
                heappushpop(heap, v)
            
        return heap[0]