class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 1 if nums[0] == nums[1] else 0

        even = Counter()
        odd = Counter()
        for i, v in enumerate(nums):
            if i % 2 == 0:
                even[v] += 1
            else:
                odd[v] += 1

        eheap = []
        oheap = []
        for k, v in even.items():
            heappush(eheap, (-v, k))
        for k, v in odd.items():
            heappush(oheap, (-v, k))
        
        e1v, e1k = 0, -1
        e2v, e2k = 0, -2
        if eheap:
            e1v, e1k = heappop(eheap)
            e1v, e1k = -e1v, e1k
        if eheap:
            e2v, e2k = heappop(eheap)
            e2v, e2k = -e2v, e2k
        
        o1v, o1k = 0, -1
        o2v, o2k = 0, -2
        if oheap:
            o1v, o1k = heappop(oheap)
            o1v, o1k = -o1v, o1k
        if oheap:
            o2v, o2k = heappop(oheap)
            o2v, o2k = -o2v, o2k

        # remember, i am KEEPING e1 + o1v here, so the ones im choang is just len(nums) - (e1v + o1v)
        if not e1k == o1k:
            return n - (e1v + o1v)
        else:
            return n - max(e1v + o2v, e2v + o1v)