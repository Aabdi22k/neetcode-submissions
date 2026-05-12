class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minp = math.inf
        for i,p in enumerate(prices):
            minp = min(minp, p)
            profit = max(profit, (p - minp))
            

        return profit
        