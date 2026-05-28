class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for v in nums:
            if v - 1 not in nums:
                length = 1
                while (v + length) in nums:
                    length += 1
                res = max(res, length)
                
        return res