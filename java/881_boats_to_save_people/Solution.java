class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int n = people.length;
        int c = 0, l = 0, r = n - 1;
        int ans = 0;
        Arrays.sort(people);
        while (l < r) {
            if (people[l] + people[r] <= limit) {
                l++;
                r--;
                c += 2;
            } else {
                r--;
                c++;
            }
            ans++;
        }

        return ans + (c < n ? 1 : 0);
    }
}