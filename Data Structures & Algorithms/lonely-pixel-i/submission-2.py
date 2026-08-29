class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS = len(picture)
        COLS = len(picture[0])

        row_count = [0] * ROWS
        col_count = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == "B":
                    row_count[r] += 1
                    col_count[c] += 1
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == "B" and row_count[r] == 1 and col_count[c] == 1: 
                    res += 1
        return res