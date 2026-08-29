class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != '1':
                return
            
            grid[r][c] = 0

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
        