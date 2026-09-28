class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # 1. Setup: Initialize the nxn grid with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Keep your exact exclusive boundaries using 'n'
        ROWS, COLS = n, n
        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

        UP_WALL = 0
        DOWN_WALL = ROWS
        LEFT_WALL = -1
        RIGHT_WALL = COLS
        
        DIRECTION = RIGHT
        i, j = 0, 0
        num = 1 # Running sum/counter

        # 2. Main loop condition: track cells filled
        while num <= n * n:
            if DIRECTION == RIGHT:
                while j < RIGHT_WALL:
                    matrix[i][j] = num  # 3. Write instead of read
                    num += 1
                    j += 1
                RIGHT_WALL -= 1
                j -= 1
                i += 1
                DIRECTION = DOWN
                
            elif DIRECTION == DOWN:
                while i < DOWN_WALL:
                    matrix[i][j] = num  # 3. Write instead of read
                    num += 1
                    i += 1
                DOWN_WALL -= 1 
                i -= 1
                j -= 1
                DIRECTION = LEFT
                
            elif DIRECTION == LEFT:
                while j > LEFT_WALL:
                    matrix[i][j] = num  # 3. Write instead of read
                    num += 1
                    j -= 1
                LEFT_WALL += 1
                j += 1
                i -= 1
                DIRECTION = UP
                
            elif DIRECTION == UP:
                while i > UP_WALL:
                    matrix[i][j] = num  # 3. Write instead of read
                    num += 1
                    i -= 1
                UP_WALL += 1
                i += 1
                j += 1
                DIRECTION = RIGHT           
                
        return matrix
