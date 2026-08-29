class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        # put open brackets in stack, 
        # if meet corresponding close bracket pop from stack
        for c in s:
            # found open bracket
            if c in bracketsMap.values():
                stack.append(c)
            # found close bracket
            else:
                # check if anything in stack to pop
                # check current char (close bracket)
                # matches top of stack (open bracket)
                if len(stack) == 0 or stack[-1] != bracketsMap[c]:
                    return False
                # close bracket matches open brackets
                stack.pop()
        
        if len(stack) == 0:
            return True
        return False
                
