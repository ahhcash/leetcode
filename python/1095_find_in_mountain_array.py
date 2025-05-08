# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def bsearch(l, r, rev=False):
            res = -1
            while l <= r:
                m = (l + r) // 2
                val = mountainArr.get(m)
                if not rev:
                    if val == target:
                        return m
                    elif val < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if val == target:
                        return m
                    elif val < target:
                        r = m - 1
                    else:
                        l = m + 1
            return -1
        n = mountainArr.length()
        l = 0
        r = n - 1
        pivot = -1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            nextval = mountainArr.get(m+1)
            if val < nextval:
                pivot = m
                l = m + 1
            else:
                r = m - 1
        left = bsearch(0, pivot)
        right = bsearch(pivot + 1, n - 1, True)

        return right if left == -1 else left