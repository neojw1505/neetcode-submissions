class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        self.count = 0
        visited = set()
        def dfs(r,c):
            # base case 
            if r == ROWS-1 and c == COLS-1: # end
                self.count += 1
                return
            if 0 > r or r >= ROWS or 0 > c or c >= COLS: # oob
                return
            if grid[r][c] == 1: # rock
                return
            if (r,c) in visited: # seen 
                return
            
            # choices 
            visited.add((r,c)) # add 
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            visited.remove((r,c)) # pop
        
        if grid[0][0] == 0:
            dfs(0,0) 

        return self.count