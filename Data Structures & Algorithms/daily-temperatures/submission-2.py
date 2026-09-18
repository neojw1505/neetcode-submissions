class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res

# stack = [0,]
# res = [1]








