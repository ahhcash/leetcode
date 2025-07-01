class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        n = len(prices)
        ans = 0
        for i in range(1, n):
            if prices[i] > buy:
                ans += (-buy + prices[i])
            buy = prices[i]
        return ans