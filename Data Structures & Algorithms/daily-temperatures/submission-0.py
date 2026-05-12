class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        maxtemp = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stemp, sind = stack.pop()
                res[sind] = i - sind
            stack.append((temp,i))
        return res            

