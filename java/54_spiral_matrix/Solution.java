class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int sr = 0, er = m-1, sc = 0, ec = n-1;
        List<Integer> res = new ArrayList<>();
        int total = m * n, c = 0;
        int i;
        while (c < total) {
            for (i = sc; i <= ec; ++i) {
                if (c >= total) {
                    break;
                }
                res.add(matrix[sr][i]);
                c++;
            }
            sr++;
            for (i = sr; i <= er; ++i) {
                if (c >= total) {
                    break;
                }
                res.add(matrix[i][ec]);
                c++;
            }
            ec--;
            for (i = ec; i >= sc; --i) {
                if (c >= total) {
                    break;
                }
                res.add(matrix[er][i]);
                c++;
            }
            er--;
            for (i = er; i >= sr; --i) {
                if (c >= total) {
                    break;
                }
                res.add(matrix[i][sc]);
                c++;
            }
            sc++;
        }

        return res;
    }
}