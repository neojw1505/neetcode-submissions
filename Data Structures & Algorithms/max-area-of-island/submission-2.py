class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        def dfs(r,c): # every dfs returns the island area
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 0 # mark visited

                top = dfs(r+1,c)
                down = dfs(r-1,c)
                right = dfs(r,c+1)
                left = dfs(r,c-1)
            else:
                return 0
            
            return 1 + top + down + right + left
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   max_area = max(max_area, dfs(r,c)) 
        return max_area