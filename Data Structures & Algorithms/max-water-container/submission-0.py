class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        l = 0 
        r = len(heights) - 1
        while l < r:
            a,b = heights[l], heights[r]
            vol = max(vol,min(a,b) * (r - l))
            if a < b:
                l += 1
            else:
                r -= 1
        return vol
            