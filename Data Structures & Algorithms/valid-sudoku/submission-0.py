class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[i][j]
                if item not in seen:
                    if item in "0123456789":
                        seen.add(item)
                else:
                    return False
        # check each col
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[j][i]
                if item not in seen:
                    if item in "0123456789":
                        seen.add(item)
                else:
                    return False
        # check each 3x3 blocks
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6),
        ]

        for start in starts:
            x,y = start
            seen = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    item = board[i][j]
                    if item not in seen: 
                        if item in "0123456789":
                            seen.add(item)
                    else:
                        return False
        
        return True