class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            d[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in d and d[diff] != i:
                return[i, d[diff]]
