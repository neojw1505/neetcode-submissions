class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = list(s)

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:   
                    res[i] = ""
                else:
                    stack.pop()
        
        while stack:
            res[stack.pop()] = ""
        
        return ''.join(res)

        # Time: O(n) 
        # Space: O(n)