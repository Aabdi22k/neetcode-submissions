class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxh = 0
        stack = []

        for i,h in enumerate(heights):
            ind = i
            while stack and stack[-1][0] > h:
                sheight,sind = stack.pop()
                a = sheight * (i - sind)
                maxh = max(a,maxh)
                ind = sind
            stack.append((h,ind))

        print(stack)

        for h,i in stack:
            maxh = max(maxh, h * (len(heights) - i))
        
        return maxh