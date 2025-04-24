class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int l = 0, r = n - 1;
        int pivot = 0;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] < nums[0]) {
                pivot = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        int left = Arrays.binarySearch(nums, 0, pivot, target);
        int right = Arrays.binarySearch(nums, pivot, n, target);

        if (left >= 0) {
            return left;
        }

        if (right >= 0) {
            return right;
        }

        return -1;
    }
}