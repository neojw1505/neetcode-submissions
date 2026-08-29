class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def backtrack(open_cnt, close_cnt):
            if len(path) == n * 2:
                res.append(''.join(path))
                return
            
            if open_cnt < n:
                path.append('(')
                backtrack(open_cnt + 1, close_cnt)
                path.pop()
            
            if open_cnt > close_cnt:
                path.append(')')
                backtrack(open_cnt, close_cnt+1)
                path.pop()
        backtrack(0,0)
        return res