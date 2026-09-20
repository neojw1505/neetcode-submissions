class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set() # global 
        def dfs(r,c,i):
            # base case
            if i == len(word): # found all words
                return True
            if 0 > r or r >= ROWS or 0 > c or c >= COLS: # Out-of-bound
                return False
            if word[i] != board[r][c]: # not same char
                return False
            if (r,c) in seen: # see coords before
                return False
          
            # multiple choices
            # - 4 directions -> loop 
            seen.add((r, c))  # add 

            choices = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for new_r, new_c in choices:
                if dfs(new_r,new_c,i+1): # recurse 
                    return True
            
            seen.remove((r, c)) # undo 
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False