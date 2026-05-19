class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res, resLen = [-1, -1], float('inf')
        freq, tfreq = defaultdict(int), Counter(t)
        have, need = 0, len(tfreq)

        for r in range(len(s)):
            freq[s[r]] += 1
            
            if s[r] in tfreq and freq[s[r]] == tfreq[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                freq[s[l]] -= 1

                if s[l] in tfreq and freq[s[l]] < tfreq[s[l]] :
                    have -= 1

                l += 1

                

        l, r = res
        return s[l: r + 1]


        

