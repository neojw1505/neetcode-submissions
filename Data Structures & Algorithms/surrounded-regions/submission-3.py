class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()

        # 1. change all O at edges to S, add to queue
        queue = collections.deque([])
        # 1st row
        for c in range(COLS):
            queue.append((0,c))
            board[0][c] = "S"
            visited.add((r,c))
        # last row
        for c in range(COLS):
            queue.append((ROWS-1,c))
            board[r][c] = "S"
            visited.add((ROWS-1,c))
        # 1st col
        for r in range(ROWS):
            queue.append((r,0))
            board[r][c] = "S"
            visited.add((r,0))
        # last col
        for r in range(ROWS):
            queue.append((r,COLS-1))
            board[r][c] = "S"
            visited.add((r,COLS-1))
        
        # 2. mutli-source bfs, mark S 
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                        if (nr,nc) not in visited:
                            board[nr][nc] = "S"
                            queue.append((nr,nc))
                            visited.add((r,c))
        
        # 3. check remaining O, mark as X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 4. check remaining S, mark as O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "S":
                    board[r][c] = "O"

