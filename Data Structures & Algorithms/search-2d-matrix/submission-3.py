class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat it like a flatten sorted 1D array
        l = 0 
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l+r) // 2
            ROW = m // len(matrix[0])
            COL = m % len(matrix[0])
            if matrix[ROW][COL] == target:
                return True
            elif matrix[ROW][COL] > target:
                r = m - 1
            else:
                l = m + 1
        return False

        