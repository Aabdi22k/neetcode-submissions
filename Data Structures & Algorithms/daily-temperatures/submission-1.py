class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Stores a tuple (Temp, day)
        res = defaultdict(int)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, day = stack.pop()
                res[day] = i - day
            res[i] = 0
            stack.append(tuple([temp, i]))
            
        
        return list(res.values())