# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        res = self.dfs(root, 0, res)
        return list(res.values()) if res else []


    def dfs(self, root, level, arr):
        if not root: return
        arr[level].append(root.val)
        self.dfs(root.left, level + 1, arr)
        self.dfs(root.right, level + 1, arr)

        return arr