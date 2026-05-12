class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s2) < len(s1):
        #     return False
        s1f = Counter(s1)
        freq = defaultdict(int)
        l = 0
        for r, ch in enumerate(s2):
            freq[ch] += 1
            if (r-l+1) == len(s1):
                if freq == s1f:
                    return True
                else:
                    freq[s2[l]] -= 1
                    if freq[s2[l]] <= 0:
                        del freq[s2[l]]
                    l += 1
            print(freq,s1f)
        return False
            
                