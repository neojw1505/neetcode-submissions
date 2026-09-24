class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        UP,DOWN,LEFT,RIGHT = 0,1,2,3

        UP_WALL = 0
        DOWN_WALL = ROWS
        LEFT_WALL = -1
        RIGHT_WALL = COLS
        
        res = []
        DIRECTION = RIGHT
        
        i,j = 0,0

        while len(res) < ROWS * COLS:
            if DIRECTION == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                RIGHT_WALL -= 1
                j -= 1
                i += 1
                DIRECTION = DOWN
            if DIRECTION == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                DOWN_WALL -= 1 
                i -= 1
                j -= 1
                DIRECTION = LEFT
            if DIRECTION == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                LEFT_WALL += 1
                j += 1
                i -= 1
                DIRECTION = UP
            if DIRECTION == UP:
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                UP_WALL += 1
                i += 1
                j += 1
                DIRECTION = RIGHT           
        return res