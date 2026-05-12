class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)
        for i in range(1,len(prices)):
            profits[i] += (prices[i] - min(prices[:i]))
            print(profits)
            
        m = max(profits)
        if m >= 0:
            return m
        else:
            return 0