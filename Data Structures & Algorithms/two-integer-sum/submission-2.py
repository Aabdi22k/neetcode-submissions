class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        
        for i, v in enumerate(nums):
            val = target - v
            if val in vals and vals[val] != i:
                return [vals[val], i]
            vals[v] = i