class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        _, kk = divmod(k, n)

        def reverse(arr, l, r):
        # works in place
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        reverse(nums, 0, n-1)
        reverse(nums, 0, kk-1)
        reverse(nums, kk, n-1)