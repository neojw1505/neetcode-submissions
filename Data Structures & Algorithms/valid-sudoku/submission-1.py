class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # check rows 
        for r in range(ROWS):
            seen = set() # new set to keep track of nums in a row
            for c in range(COLS):
                if board[r][c] == ".": continue
                if board[r][c] not in seen:
                    seen.add(board[r][c])
                else:
                    return False

        # check cols
        for c in range(COLS):
            seen = set() # new set to keep track of nums in a col
            for r in range(ROWS):
                if board[r][c] == ".": continue
                if board[r][c] not in seen:
                    seen.add(board[r][c])
                else:
                    return False

        # check 3x3 
        coords = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]
        
        for dr,dc in coords:
            seen = set() # new set to keep track of nums in a 3x3
            for r in range(dr, dr + 3):
                for c in range(dc, dc + 3):
                    if board[r][c] == ".": continue
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False
        
        return True
