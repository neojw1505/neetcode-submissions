class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        first_row_originally_have_zero = False
        first_col_originally_have_zero = False

        for c in range(COLS):
            if matrix[0][c] == 0:
                first_row_originally_have_zero = True
                break
        
        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_originally_have_zero = True
                break

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if first_row_originally_have_zero:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if first_col_originally_have_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
        

        