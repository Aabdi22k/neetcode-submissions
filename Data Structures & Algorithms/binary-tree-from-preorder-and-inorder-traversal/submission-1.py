# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.p = 0

        ind = {val: i for i, val in enumerate(inorder)}

        def dfs(lo, hi):
            if lo > hi:
                return None

            nodev = preorder[self.p] 
            self.p += 1
            node = TreeNode(nodev)
            m = ind[nodev]
            node.left = dfs(lo, m - 1)
            node.right = dfs(m + 1, hi)
            return node

        return dfs(0, len(inorder) - 1)