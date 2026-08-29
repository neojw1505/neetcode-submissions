class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROWS,COLS = len(board), len(board[0])

        def dfs(r,c,i):
            # found a path
            if i == len(word):
                return True
            # found the char
            if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in path and board[r][c] == word[i]:
                path.add((r,c))
                res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
                path.remove((r,c))
                return res 
            # did not find the char
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False