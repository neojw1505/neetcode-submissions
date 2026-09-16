class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # check rows
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                cell = board[r][c]
                if cell in seen:
                    return False
                elif cell != ".":
                    seen.add(cell)
        # check cols
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                cell = board[r][c]
                if cell in seen:
                    return False
                elif cell != ".":
                    seen.add(cell)
                    
        # check 3x3
        boundaries = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for i in range(len(boundaries)):
            dr = boundaries[i][0]
            dc = boundaries[i][1]
            seen = set()
            for r in range(dr, dr + 3):
                for c in range(dc, dc + 3):
                    cell = board[r][c]
                    if cell in seen:
                        return False
                    elif cell != ".":
                        seen.add(cell)

        return True