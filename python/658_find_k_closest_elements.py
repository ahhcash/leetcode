class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bsearch(arr, key, smaller=True):
            res = -1
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if smaller:
                    if arr[m] <= key:
                        res = m
                        l = m+1
                    else:
                        r = m-1
                else:
                    if arr[m] >= key:
                        res = m
                        r = m-1
                    else:
                        l = m+1
            return res
        n = len(arr)
        # find either the smallest element <= x (s1) or the smallest element >= x (s2)
        # choose the starting value (s) to be the one that's closer to x
        s1 = bsearch(arr, x)
        s2 = bsearch(arr, x, False)
        s = s1 if abs(x - arr[s1]) <= abs(arr[s2] - x) else s2
        res = [arr[s]]

        # two pointers to the left and right of s
        l, r = s-1, s+1

        # since we've already added arr[s] to the result, subtract by 1
        k -= 1

        # iterate to find the remainig k elments
        while k > 0:
            if 0 <= l < r < n:
                # if l and r are within the limits of 0 and n, get the left distance (ld) and the right distance (rd)
                # choose the smaller of the two, perfer the left distance if both are equal since the left index is always smaller (look at the second rule for distance)
                ld = abs(x - arr[l])
                rd = abs(arr[r] - x)
                if ld <= rd:
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l < 0 and r < n:
                # if the left elements are exhausted and we still have some elements to add, use the right elements
                res.append(arr[r])
                r += 1
            elif l >= 0 and r >= n:
                # if the right side elements are exhausted and we still have some elements to add (k > 0), use the left side elements
                res.append(arr[l])
                l -= 1
            k -= 1
        
        # sort the result (for whatever reason lmao)
        res.sort()
        return res