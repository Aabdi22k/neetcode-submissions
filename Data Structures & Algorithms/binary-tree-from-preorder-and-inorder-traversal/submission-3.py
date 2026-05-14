# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxs = {v:i for i,v in enumerate(inorder)}

        self.pidx = 0

        def dfs(l, r):
            if l > r: return None
            val = preorder[self.pidx]
            root = TreeNode(val)
            self.pidx += 1
            mid = idxs[val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(preorder) - 1)