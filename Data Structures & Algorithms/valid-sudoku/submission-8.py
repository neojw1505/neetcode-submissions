class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # validate rows
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                cell = board[r][c]
                if cell not in seen and cell != ".":
                    seen.add(cell)
                elif cell in seen:
                    return False
        # validate cols
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                cell = board[r][c]
                if cell not in seen and cell != ".":
                    seen.add(cell)
                elif cell in seen:
                    return False
        # validate 3x3
        boundaries = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for dr,dc in boundaries:
            seen = set()
            for r in range(dr, dr+3):
                for c in range(dc, dc+3):
                    cell = board[r][c]
                    if cell not in seen and cell != ".":
                        seen.add(cell)
                    elif cell in seen:
                        return False

        return True