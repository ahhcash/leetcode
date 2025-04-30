class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        i = 0
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            heappush(heap, diff)
            if len(heap) > ladders: # we can;t cover the route with just ladders
                smallestdiff = heappop(heap)
                # can we cover smallest diff with bricks
                if bricks >= smallestdiff:
                    bricks -= smallestdiff
                else:
                    # we can;t cover the route via ladders OR bricks. quit and return i
                    return i
        return n-1