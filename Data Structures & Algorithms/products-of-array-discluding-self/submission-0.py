class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for n in nums]

        s = 1
        for i,n in enumerate(nums):
            res[i] = s
            s *= n
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        
        return res