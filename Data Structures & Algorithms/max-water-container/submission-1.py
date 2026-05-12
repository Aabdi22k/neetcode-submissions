class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l,r = 0, len(heights) -1
        while l < r:
            a,b = heights[l], heights[r]
            water = (r - l) * min(a, b)
            maxWater = max(water, maxWater)

            if a < b:
                l += 1
            else:
                r -= 1
        
        return maxWater
        