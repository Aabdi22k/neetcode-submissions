class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l, r = 0, 0
        maxLength = 0
        mf = 0 
        while r < len(s):
            freq[s[r]] += 1
            mf = max(mf, freq[s[r]])
            while r - l + 1 - mf > k:
                freq[s[l]] -= 1
                l += 1
                hfl = s[r] if freq[s[r]] > freq[s[l]] else s[l]

            maxLength = max(r - l + 1, maxLength)
            r += 1
        
        return maxLength

