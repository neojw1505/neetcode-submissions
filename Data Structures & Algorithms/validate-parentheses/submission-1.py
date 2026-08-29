class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }
        for ch in s:
            # append open brackets
            if ch not in mapping.keys():
                stack.append(ch)
            # closing brackets
            else:
                # stack not empty
                if stack:
                    # check top of stack is correct bracket
                    if stack[-1] != mapping[ch]:
                        return False
                    stack.pop() # just pop from stack, cause it's correct
                else:
                    return False
        # need check if stack is empty because
        # if string contains all open brackets, the stack will not be closed
        if len(stack) == 0:
            return True
        return False # not valid stack as not closed properly