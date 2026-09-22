class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # ===== PACIFIC QUEUE ====== #
        pacific_queue = collections.deque([])
        visited_pacific_queue = set() # -> contains all the cells that water can reach pacific ocean

        # push 1st row to pacific_queue
        for c in range(COLS):
            pacific_queue.append((0,c)) # append coords
            visited_pacific_queue.add((0,c))
        # push 1st col to pacific_queue
        for r in range(ROWS):
            pacific_queue.append((r,0)) # append coords
            visited_pacific_queue.add((r,0))
        
        # ===== ATLANTIC QUEUE ====== #
        atlantic_queue = collections.deque([])
        visited_atlantic_queue = set()

        # push last row to atlantic_queue
        for c in range(COLS):
            atlantic_queue.append((ROWS-1,c))
            visited_atlantic_queue.add((ROWS-1,c))
        # push last col to pacific_queue
        for r in range(ROWS):
            atlantic_queue.append((r,COLS-1))
            visited_atlantic_queue.add((r,COLS-1))

        # ===== BFS FOR PACIFIC QUEUE ====== #
        while pacific_queue:
            level_size = len(pacific_queue)
            for _ in range(level_size):
                r,c = pacific_queue.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                        if (nr,nc) not in visited_pacific_queue:
                            pacific_queue.append((nr,nc))
                            visited_pacific_queue.add((nr,nc))
        
        # ===== BFS FOR ATLANTIC QUEUE ====== #
        while atlantic_queue:
            level_size = len(atlantic_queue)
            for _ in range(level_size):
                r,c = atlantic_queue.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                        if (nr,nc) not in visited_atlantic_queue:
                            atlantic_queue.append((nr,nc))
                            visited_atlantic_queue.add((nr,nc))
        
        # get common nums in visited_pacific_queue and visited_atlantic_queue
        res = []
        for (r,c) in visited_pacific_queue:
            if (r,c) in visited_atlantic_queue:
                res.append((r,c))
        
        return res
                
 



        

