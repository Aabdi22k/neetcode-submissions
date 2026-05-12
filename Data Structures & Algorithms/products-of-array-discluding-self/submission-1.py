class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pf = 1
        for i in range(len(nums)):
            res[i] *= pf
            pf *= nums[i]
       
        sf = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= sf
            sf *= nums[i]

        return res