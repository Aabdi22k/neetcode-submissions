class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n: return False

        graph = {i: [] for i in range(n)}
        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        visited = set()
        
        def dfs(v, p):
            if v in visited: return False

            visited.add(v)
            for e in graph[v]:
                if e == p: continue
                if not dfs(e, v): return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n 


