class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # setup 
        ROWS, COLS = len(matrix), len(matrix[0])
        FIRST_ROW, FIRST_COL = False, False

        # check FIRST_ROW contains zero
        FIRST_ROW = 0 in matrix[0]
        # check FIRST_COL contains zero
        FIRST_COL = any(matrix[row][0]==0 for row in range(ROWS))

        # mark indicators for sub-matrix (less first row first col)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # set first item in that row to 0            
                    matrix[r][0] = 0 # set first item in that col to 0                   

        # indicators are ready, loop the sub-matrix to fill in zeroes
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # check first item in row or col = 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # finish sub-matrix, fill in FIRST_ROW, FIRST_COL
        if FIRST_ROW:
            matrix[0] = [0] * COLS
        if FIRST_COL:
            for r in range(ROWS):
                matrix[r][0] = 0