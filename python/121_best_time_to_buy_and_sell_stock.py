class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        curr = 0
        for i in range(n):
            if prices[i] < prices[curr]:
                curr = i
            else:
                profit = prices[i] - prices[curr]
                ans = max(ans, profit)
        return ans