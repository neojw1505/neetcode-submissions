class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = collections.deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append([r,c])
        time = 0
        while rotten and fresh > 0:
            rotten_size = len(rotten)
            time += 1
            for _ in range(rotten_size):
                r,c = rotten.popleft()
                for dr,dc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        rotten.append([dr,dc])
                        fresh -= 1
                        if fresh == 0:
                            return time
        if fresh == 0:
            return time
        return -1
                        
