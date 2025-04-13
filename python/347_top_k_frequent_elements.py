class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, v in freq.items():
            heappush(heap, (-v, key))
        res = []
        while k > 0:
            if not heap:
                break
            res.append(heappop(heap)[1])
            k -= 1

        return res