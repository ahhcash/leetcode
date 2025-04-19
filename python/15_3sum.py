class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue # keep moving until we find the first pair of distinct consecutive values
            l, r = i + 1, n - 1
            # same as two sum II input array is sorted
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # make l point to the next element in sorted order
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # make r point to the previous element in sorted prder
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    
                    # now l points to the last occurrence of it's initial value (at the beginning of the loop)
                    # and r points to the first occurrence of its initial value
                    # move them right and left
                    l += 1
                    r -= 1

        return res