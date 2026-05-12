class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) -1

        while l < r:
            a,b = s[l], s[r]

            while not a.isalnum() and l < r:
                l += 1
                a = s[l]
            
            while not b.isalnum() and r > l:
                r -= 1
                b = s[r]
            

            if a != b:
                return False
            
            l += 1
            r -= 1
        
        return True