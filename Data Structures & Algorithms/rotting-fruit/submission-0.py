class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0,0
        ROWS, COLS = len(grid), len(grid[0])
        # 1. count fresh oranges and add rotten to a queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        # 2. multi bfs, rot adjacent orange, reduce fresh, increase time
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        while q and fresh > 0:
            # need this loop to simulate 1 unit of time
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions: 
                    nr = r + dr
                    nc = c + dc
                    # if inbound and fresh
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # rot it
                        q.append((nr,nc)) # add new rotten orange to queue
                        fresh -= 1 # reduce fresh orange
            time += 1 # increase time
        return time if fresh == 0 else -1 