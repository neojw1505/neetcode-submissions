class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if 0 > r or r >= ROWS or 0 > c or c >= COLS or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            top = dfs(r+1,c)
            btm = dfs(r-1,c)
            right = dfs(r,c+1)
            left = dfs(r,c-1)
            return top + btm + left + right 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)
         

