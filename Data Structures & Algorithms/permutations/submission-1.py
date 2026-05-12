class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(cur, nums, pick):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    cur.append(nums[i])
                    backtrack(cur, nums, pick)
                    cur.pop()
                    pick[i] = False
        backtrack([], nums, [False] * len(nums))
        return res