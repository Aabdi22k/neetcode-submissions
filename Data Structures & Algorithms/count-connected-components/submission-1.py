class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0
        graph = {i: [] for i in range(n)}
        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        visited = set()

        def dfs(v):
            for e in graph[v]:
                if not e in visited:
                    visited.add(e)
                    dfs(e)
            
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                cc += 1
        
        return cc
        