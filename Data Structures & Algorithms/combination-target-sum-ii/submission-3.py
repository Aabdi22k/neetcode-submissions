class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or len(curr) == len(nums): return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: continue

                curr.append(nums[i])
                dfs(i + 1, curr, total + nums[i])
                curr.pop()
        dfs(0, [], 0)
        return res