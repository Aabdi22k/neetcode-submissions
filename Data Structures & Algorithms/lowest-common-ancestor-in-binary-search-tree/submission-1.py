# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smaller = p if p.val <= q.val else q
        larger = q if smaller == p else p

        if root.val < smaller.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > larger.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
