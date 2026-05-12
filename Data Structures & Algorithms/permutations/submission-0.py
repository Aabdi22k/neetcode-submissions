class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, nums, pick):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(curr, nums, pick)
                    curr.pop()
                    pick[i] = False
        dfs([], nums, [False] * len(nums))

        return res