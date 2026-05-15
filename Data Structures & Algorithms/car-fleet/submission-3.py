class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ps = list(zip(position, speed))

        ps.sort(reverse = True)

        for p, s in ps:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        

        return len(stack)