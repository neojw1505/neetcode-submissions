class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        items_path = path.split('/')

        for item in items_path:
            if item == "..":
                if stack:
                    stack.pop()
            elif item == "." or item == "":
                continue
            else:
                stack.append(item)
        return "/" + "/".join(stack)