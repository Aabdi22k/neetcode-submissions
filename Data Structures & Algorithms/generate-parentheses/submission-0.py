class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openc, closedc):
            if openc == closedc == n:
                res.append(''.join(stack))
                
            if openc < n:
                stack.append('(')
                backtrack(openc + 1, closedc)
                stack.pop()
            
            if openc > closedc:
                stack.append(')')
                backtrack(openc, closedc + 1)
                stack.pop()

        backtrack(0,0)
        return res