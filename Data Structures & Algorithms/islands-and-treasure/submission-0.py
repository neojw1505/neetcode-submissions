class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source bfs from each treasure
        # the current level is the value to replace the non -1 cells

        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque([])
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1:
                        if (nr,nc) not in visited:
                            grid[nr][nc] = grid[r][c] + 1
                            queue.append((nr,nc))
                            visited.add((nr,nc))
            


