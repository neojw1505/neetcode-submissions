class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(open_count, close_count):
            # base case
            if len(path) == n * 2:
                res.append("".join(path[:]))
                return
            # choices rules:
            #  - 2 choices -> no loop template
            #  - limited to n open and n close brackets 
            #  - open bracket can use on 1 condition
            #    1. open brackets less than n -> open_count < n
            #  - close bracket can use on 2 conditions:
            #    1. close brackets less than n -> close_count < n 
            #    2. when more open brackets than close brackets -> open_count > close_count

            # choice 1: pick (
            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count)
                path.pop()

            # choice 2: pick )
            if close_count < n and open_count > close_count:
                path.append(")")
                dfs(open_count, close_count+1)
                path.pop()

        dfs(0,0)
        return res