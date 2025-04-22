class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        freq = defaultdict(int)
        for i, c in enumerate(s):
            freq[c] += 1
        heap = []
        for k, v in freq.items():
            heappush(heap, (-v, k))
        while heap:
            if res and heap[0][1] == res[-1]:
                return ""
            
            f1, c1 = heappop(heap)
            res += c1
            f1 += 1
            if heap:
                f2, c2 = heappop(heap)
                res += c2
                f2 += 1
                if not f2 >= 0:
                    heappush(heap, (f2, c2))
            
            if not f1 >= 0:
                heappush(heap, (f1, c1))

        return res