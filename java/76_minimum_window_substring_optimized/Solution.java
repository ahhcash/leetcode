class Solution {
    private static Integer INFINITY = 100001;
    private Map<Character, Integer> t_ctr = new HashMap<>();

    public String minWindow(String s, String t) {
        int l = 0, n = s.length(), required = 0, formed = 0, mins = 0;
        int minl = Solution.INFINITY;
        for (char c: t.toCharArray()) {
            int val = this.t_ctr.getOrDefault(c, 0);
            if (val == 0) {
                required++;
            }
            this.t_ctr.put(c, val + 1);
        }
        Map<Character, Integer> w_ctr = new HashMap<>();
        for (int r = 0; r < n; ++r) {
            w_ctr.put(s.charAt(r), w_ctr.getOrDefault(s.charAt(r), 0) + 1);

            if (this.t_ctr.containsKey(s.charAt(r)) && w_ctr.get(s.charAt(r)).equals(this.t_ctr.get(s.charAt(r)))) {
                formed++;
            }

            while (l <= r && formed == required) {
                if (r - l + 1 < minl) {
                    minl = r - l + 1;
                    mins = l;
                }

                w_ctr.put(s.charAt(l), w_ctr.getOrDefault(s.charAt(l), 0) - 1);

                if (t_ctr.containsKey(s.charAt(l)) && w_ctr.get(s.charAt(l)).intValue() < t_ctr.get(s.charAt(l)).intValue()) {
                    formed--;
                }

                l++;
            }
        }

        return minl == INFINITY ? "" : s.substring(mins, mins+minl);
    }
}