class Solution {
    private static Long INFINITY = 100001l;
    private Map<Character, Integer> t_ctr = new HashMap<>();

    private boolean contains(Map<Character, Integer> window) {
        return !this.t_ctr.entrySet().stream().anyMatch(e -> window.getOrDefault(e.getKey(), 0) < e.getValue());
    }

    public String minWindow(String s, String t) {
        int l = 0, n = s.length();
        long minl = Solution.INFINITY;
        String res = "";
        for (int i = 0; i < t.length(); ++i) {
            char c = t.charAt(i);
            this.t_ctr.put(c, this.t_ctr.getOrDefault(c, 0) + 1);
        }
        Map<Character, Integer> w_ctr = new HashMap<>();
        for (int r = 0; r < n; ++r) {
            w_ctr.put(s.charAt(r), w_ctr.getOrDefault(s.charAt(r), 0) + 1);
            while (this.contains(w_ctr)) {
                if (r - l + 1 < minl) {
                    minl = r - l + 1;
                    res = s.substring(l, r+1);
                }
                w_ctr.put(s.charAt(l), w_ctr.getOrDefault(s.charAt(l), 0) - 1);
                l++;
            }
        }

        return res;
    }
}