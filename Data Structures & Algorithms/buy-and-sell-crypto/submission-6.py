class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)
        for i in range(1,len(prices)):
            profits[i] += max(0,(prices[i] - min(prices[:i])))
            print(profits)

        return max(profits)
        