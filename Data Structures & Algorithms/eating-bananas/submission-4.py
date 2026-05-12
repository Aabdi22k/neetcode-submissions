class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            m = (l + r) // 2 # SPEED OR K
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/m)
            if hrs <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        