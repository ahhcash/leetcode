class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        i = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            # find the closest peak from the detected valley
            while i < n - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            ans += peak - valley
        return ans