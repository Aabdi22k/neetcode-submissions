class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        mins = r
        while l <= r:
            m = (l + r ) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / m)
            if hrs <= h:
                mins = m
                r = m - 1
            else:
                l = m + 1
        return mins
