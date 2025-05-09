class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        maxr = [0] * n
        maxr[n-1] = n-1
        for i in range(n-2, -1, -1):
            if nums[i] > nums[maxr[i+1]]:
                maxr[i] = i
            else:
                maxr[i] = maxr[i+1]
        for i in range(n):
            if nums[i] < nums[maxr[i]]:
                nums[maxr[i]], nums[i] = nums[i], nums[maxr[i]]
                return int("".join(nums))
        
        return num