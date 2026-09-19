class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # for each rows, do a binary search
        for row in range(ROWS):
            # binary search
            l = 0
            r = COLS - 1
            while l <= r:
                m = (l+r)//2
                if matrix[row][m] == target:
                    return True
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return False

