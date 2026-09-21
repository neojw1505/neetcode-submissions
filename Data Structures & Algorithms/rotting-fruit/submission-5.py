class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque([])
        visited = set()
        fresh_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # fresh
                    fresh_oranges += 1
                if grid[r][c] == 2: # rotten fruit
                    queue.append((r,c))
                    visited.add((r,c))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        if (nr, nc) not in visited:
                            fresh_oranges -= 1
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                            visited.add((nr,nc))
            
            if queue:
                minutes += 1

        return minutes if fresh_oranges == 0 else -1
