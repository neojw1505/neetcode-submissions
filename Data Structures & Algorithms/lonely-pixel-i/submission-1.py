class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # Lonely Pixel 2 Solution

        ROWS, COLS = len(picture), len(picture[0])
        row_map = collections.Counter()
        col_count = [0] * COLS
        # count row occurence in matrix
        for row in picture:
            row_map[tuple(row)] += 1
            for j, val in enumerate(row):
                if val == "B":
                    col_count[j] += 1
        res = 0
        for row in picture:
            for j,val in enumerate(row):
                if val == "B" and row_map[tuple(row)] == col_count[j]:
                    res += 1
        return res

