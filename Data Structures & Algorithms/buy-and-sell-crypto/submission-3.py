class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(1,len(prices)):
            profits.append(prices[i] - min(prices[:i]))
            print(profits)

        if profits and max(profits) >= 0:
            return max(profits)
        else:
            return 0