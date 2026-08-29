class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # idx, temp

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                res[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            stack.append((idx, temp))
        return res 
        