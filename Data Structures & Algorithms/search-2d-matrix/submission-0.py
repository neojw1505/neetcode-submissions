class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # every row just binary search to find target

        # Loop each row
        for row in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            # bsearch
            while l <= r:
                m = (l+r) // 2

                if matrix[row][m] == target:
                    return True
                
                elif matrix[row][m] > target:
                    r = m - 1
                
                else:
                    l = m + 1
        
        return False