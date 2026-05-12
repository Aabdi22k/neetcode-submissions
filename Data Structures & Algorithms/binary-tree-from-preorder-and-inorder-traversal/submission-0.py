# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = 0

        idx_in = {val: i for i, val in enumerate(inorder)}
        h = {val: idx_in[val] for val in preorder}

        def build(lo, hi):
            nonlocal p
            if lo > hi:
                return None

            nodev = preorder[p]; p += 1
            m = h[nodev]
            node = TreeNode(nodev)
            node.left = build(lo, m - 1)
            node.right = build(m + 1, hi)
            return node

        return build(0, len(preorder) - 1)