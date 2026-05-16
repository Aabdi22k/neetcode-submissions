class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxY, maxX = len(board), len(board[0])

        def backtrack(x, y, i):
            if i == len(word): return True
            if (x < 0 or y < 0 or x >= maxX or y >= maxY or board[y][x] != word[i] or board[y][x] == '#'): return False
            
            board[y][x] = '#'  # Setting Char to Seen

            res = (backtrack(x+1, y, i + 1) or 
                backtrack(x-1, y, i + 1) or 
                backtrack(x, y+1, i + 1) or 
                backtrack(x, y-1, i + 1))

            board[y][x] = word[i]

            return res

        for y in range(maxY):
            for x in range(maxX):
                if backtrack(x,y,0): return True
        return False