class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        maxLength = 0
        freq = defaultdict(int)
        while r < len(s):
            while freq[s[r]] > 0:
                freq[s[l]] -= 1
                l += 1
            freq[s[r]] += 1
            length = r - l + 1
            maxLength = max(length, maxLength)
            r += 1

        return maxLength