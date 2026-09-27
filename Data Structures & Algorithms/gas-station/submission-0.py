class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        n = len(gas)
        station = 0
        tank = 0
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0: # failure point
                tank = 0
                station = i + 1
        return station 
