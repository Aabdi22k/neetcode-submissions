# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minv, maxv = -1001, 1001


        def dfs(root, minv, maxv):
            if not root: return True
            if not minv < root.val < maxv: return False

            return dfs(root.left, minv, root.val) and dfs(root.right, root.val, maxv)

        return dfs(root, minv, maxv)
