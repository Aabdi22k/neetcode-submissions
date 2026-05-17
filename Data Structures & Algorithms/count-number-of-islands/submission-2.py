class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == "0"): return 

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands