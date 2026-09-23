class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #  STEP 1: TRANSPOSE THE GRID
        ROWS,COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(r+1, COLS):
                matrix[r][c],matrix[c][r] = matrix[c][r], matrix[r][c]

        # STEP 2: FLIP THE COLUMNS HORIZONTALLY
        for r in range(ROWS):
            matrix[r].reverse()
        
