"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        def dfs(node):
            if node in d: return d[node]
            
            d[node] = Node(node.val)

            for neighbor in node.neighbors:
                d[node].neighbors.append(dfs(neighbor))
            return d[node]
        
        return dfs(node) if node else None