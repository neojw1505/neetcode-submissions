class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # BFS standard algo
        if not grid:
            return 0

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        length = 0
        queue = collections.deque([(0,0)])
        visited = {(0,0)}


        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft() # pop from queue

                # success
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                # append all 4 directions neighbours
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0: # in-bound
                        if (nr, nc) not in visited:
                            queue.append((nr,nc))
                            visited.add((nr,nc))
            length += 1

        return length
