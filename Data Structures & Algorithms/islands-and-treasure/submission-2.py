class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])

        def dfs(r, c, d):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == -1 or grid[r][c] == 0 or grid[r][c] <= d: return
            
            grid[r][c] = d
            dfs(r+1, c, d+1)
            dfs(r-1, c, d+1)
            dfs(r, c+1, d+1)
            dfs(r, c-1, d+1)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    dfs(r+1, c, 1)
                    dfs(r-1, c, 1)
                    dfs(r, c+1, 1)
                    dfs(r, c-1, 1)
