class Solution:
    def isValid(self, s: str) -> bool:
        d= {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in d.values():
                stack.append(ch)
            else:
                if stack and stack[-1] == d[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
        return not stack