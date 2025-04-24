import static java.lang.Math.max;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (null == nums || nums.length == 0) {
            return 0;
        }

        Set<Integer> seen = new HashSet<>();
        for (int v: nums) {
            seen.add(v);
        }
        int ans = 0;
        for (int num: seen) {
            if (!seen.contains(num - 1)) {
                // start of a sequence
                int v = num, c = 1;
                while (seen.contains(v+c)) {
                    c++;
                }
                ans = max(ans, c);
            }
        }
        return ans;
    }
}