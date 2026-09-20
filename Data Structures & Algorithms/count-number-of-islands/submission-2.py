class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            # base case
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                grid[r][c] = 0 # mark as visited
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
                    
        return count 
                
        
        
