class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = []
        for i in range(n):
            pos_speed.append([position[i], speed[i]])
        
        stack = []
        for cur_pos, cur_speed in sorted(pos_speed)[::-1]:
            time_to_target = (target - cur_pos) / cur_speed
            stack.append(time_to_target)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            