class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch != '.':
                    if ch in rows[i] or ch in cols[j] or ch in boxes[(i//3, j//3)]:
                        return False
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[i//3, j//3].add(ch)
        return True
        
