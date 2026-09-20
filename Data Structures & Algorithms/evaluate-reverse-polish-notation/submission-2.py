class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+*/-": # is a num
                stack.append(ch)
            elif ch == "+":
                # pop the 2 operands
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(int(first) + int(second))))
            elif ch == "*":
                # pop the 2 operands
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(first) * int(second)))
            elif ch == "/":
                # pop the 2 operands
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(first) / int(second)))
            elif ch == "-":
                # pop the 2 operands
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(first) - int(second)))
        return int(stack[-1])
