class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        k = 0
        i, j = 0, 0
        m1 = m2 = 0
        while k <= total // 2:
            m1 = m2
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    m2 = nums1[i]
                    i += 1
                else:
                    m2 = nums2[j]
                    j += 1
            elif i < m:
                m2 = nums1[i]
                i += 1
            elif j < n:
                m2 = nums2[j]
                j += 1
            k += 1
        
        return m2 if total & 1 else (m1 + m2) / 2