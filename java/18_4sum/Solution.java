class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            for (int j = i + 1; j < n; ++j) {
                if (j > i + 1 && nums[j] == nums[j-1]) {
                    continue;
                }
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long val = (long)nums[i] + nums[j] + nums[l] + nums[r];
                    if (val > target) {
                        r -= 1;
                    } else if (val < target) {
                        l += 1;
                    } else {
                        res.add(Arrays.asList(nums[i], nums[j], nums[l], nums[r]));
                        
                        while (l < r && nums[l] == nums[l+1]) {
                            l++;
                        }

                        while (r > l && nums[r] == nums[r-1]) {
                            r--;
                        }

                        l++;
                        r--;
                    }
                }
            }
        }
        return res;
    }
}