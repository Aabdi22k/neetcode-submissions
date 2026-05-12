class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l,r = l + 1, r - 1
            return True

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur[:])
                return
            
            for j in range(i, len(s)):
                if isPal(i, j):
                    cur.append(s[i:j+1])
                    backtrack(j+1, cur)
                    cur.pop()
        backtrack(0, [])
        return res