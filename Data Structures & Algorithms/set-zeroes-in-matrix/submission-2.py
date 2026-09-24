class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row_that_have_zero = set()
        col_that_have_zero = set()

        ROWS, COLS = len(matrix), len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_that_have_zero.add(r)
                    col_that_have_zero.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in row_that_have_zero or c in col_that_have_zero:
                    matrix[r][c] = 0
        