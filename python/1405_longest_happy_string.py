class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ctr = {
            'a': a,
            'b': b,
            'c': c
        }

        heap = [(-v, k) for k, v in ctr.items() if v > 0]
        heapify(heap)
        res = []
        while heap:
            f, c = heappop(heap)
            f = -f
            if len(res) >= 2 and res[-1] == c and res[-2] == c:
                if not heap:
                    break
                ff, cc = heappop(heap)
                ff = -ff
                res.append(cc)
                ff -= 1
                if ff > 0:
                    heappush(heap, (-ff, cc))
                
                heappush(heap, (-f, c))
            else:
                f -= 1
                res.append(c)
                if f > 0:
                    heappush(heap, (-f, c))
        return "".join(res)