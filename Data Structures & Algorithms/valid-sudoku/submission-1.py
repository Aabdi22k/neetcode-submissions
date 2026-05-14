class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i,_ in enumerate(board):
            for j, v in enumerate(board[i]):
                if v == '.': continue

                if v in rows[i] or v in cols[j] or v in boxes[(i // 3, j // 3)]:
                    return False

                rows[i].add(v)
                cols[j].add(v)
                boxes[(i//3,j//3)].add(v)

        return True

        