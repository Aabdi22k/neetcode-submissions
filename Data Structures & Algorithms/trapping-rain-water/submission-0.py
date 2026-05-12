class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, total = 0, len(height) - 1, 0
        lm, rm = height[l], height[r]

        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                total += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                total += rm - height[r]
        return total