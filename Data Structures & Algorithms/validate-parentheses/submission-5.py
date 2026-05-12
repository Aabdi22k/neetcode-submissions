class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for ch in s:
            if stack and ch in pairs:
                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
        return len(stack) == 0
