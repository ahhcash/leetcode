class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if 1 == k:
            return 1
        heap = []
        heappush(heap, -1)
        heappush(heap, -n)
        for i in range(2, isqrt(n)+1):
            if n % i == 0:
                heappush(heap, -i)

                if len(heap) > k:
                    heappop(heap)
                
                # if not a perfect square, we add i and n // i
                if not i * i == n:
                    if len(heap) < k or n // i < -heap[0]:
                        # replace the kth largest with the current one n // i
                        heappush(heap, -n // i)

                        if len(heap) > k:
                            heappop(heap)
        
        return -1 if not len(heap) == k else -heap[0]