class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if not self.maxheap or num < -self.maxheap[0]:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)
        
        self.count += 1

        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        if self.count & 1:
            return -self.maxheap[0]
        return (self.minheap[0] - self.maxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()