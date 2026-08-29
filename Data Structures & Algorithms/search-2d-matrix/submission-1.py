class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        # binary Search for row 
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        # check if got such row
        # finish above loop but cannot find row that contain the target
        if top > bot:
            return False

        # binary search for target in that row
        L, R = 0, len(matrix[0]) - 1
        while L <= R:
            m = (L + R) // 2
            if target > matrix[row][m]:
                L = m + 1
            elif target < matrix[row][m]:
                R = m - 1
            else:
                return True
        return False
