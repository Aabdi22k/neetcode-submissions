# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = self.dfs(root, defaultdict(list), 0)
        if d: return list(d.values())
        return []
    
    def dfs(self, root, levels, level):
        if not root: return
        levels[level].append(root.val)

        self.dfs(root.left, levels, level + 1)
        self.dfs(root.right, levels, level + 1)

        return levels

