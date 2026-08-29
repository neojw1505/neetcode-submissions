class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if (r,c) in visit:
                continue
            
            visit.add((r,c))

            if r == ROWS - 1 and c == COLS - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if neiR < 0 or neiC < 0 or neiR == ROWS or neiC == COLS or grid[neiR][neiC] in visit:
                    continue
                if (neiR, neiC) not in visit:
                    heapq.heappush(minHeap, (max(grid[neiR][neiC], t), neiR, neiC))
            
            