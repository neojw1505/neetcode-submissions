class Solution:
    def decodeString(self, s: str) -> str:
        # T: O(n), S:O(m) m = length of decoded string
        # "2[a3[b]]c"
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                curr = ""
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                curr = curr * int(num)
                stack.append(curr)
        return ''.join(stack)


                