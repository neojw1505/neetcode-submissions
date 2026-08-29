class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # setup ROWS, COLS
        ROWS, COLS = len(matrix), len(matrix[0])

        # create new matrix
        output = [[0] * ROWS for _ in range(COLS)]

        # fill in the matrix with right numbers
        for r in range(ROWS):
            for c in range(COLS):
                output[c][r] = matrix[r][c] # just swap 
        
        return output