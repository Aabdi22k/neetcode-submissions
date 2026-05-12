class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        def makeRotten(r,c):
            nonlocal fresh
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] != 1): return
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))

        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                makeRotten(r+1, c)
                makeRotten(r-1, c)
                makeRotten(r, c+1)
                makeRotten(r, c-1)
            minutes += 1
        
        return minutes if fresh==0 else -1
        


        