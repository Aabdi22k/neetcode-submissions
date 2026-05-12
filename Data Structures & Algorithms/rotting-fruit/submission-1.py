class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q, fresh = deque(), 0

        def determine(r, c):
            nonlocal fresh
            if r<0 or c<0 or r>=R or c>=C or grid[r][c] != 1 : return
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
                    
        
        t = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                determine(r+1, c)
                determine(r-1, c)
                determine(r, c+1)
                determine(r, c-1)
            t += 1

        return t if fresh ==0 else -1
