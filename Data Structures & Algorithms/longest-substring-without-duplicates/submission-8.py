class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        seen = {}
        for r,ch in enumerate(s):
            if ch in seen:
                l = max(l, seen[ch] + 1)
            seen[ch] = r
            ans = max(ans, r - l + 1)
            print(seen, l, ans)

        return ans