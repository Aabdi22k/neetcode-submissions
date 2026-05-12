# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxv):
            if not node:
                return 0
            if node.val >= maxv:
                res = 1
            else:
                res = 0
            
            maxv = max(maxv, node.val)
            res += dfs(node.left, maxv)
            res += dfs(node.right, maxv)
            return res

        return dfs(root, root.val)
        