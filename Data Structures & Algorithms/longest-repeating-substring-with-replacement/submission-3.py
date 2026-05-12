class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l,mf,longest = 0,0,0

        for r, ch in enumerate(s):
            count[ch] += 1 
            mf = max(mf, count[ch])

            while (r - l + 1) - mf > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest