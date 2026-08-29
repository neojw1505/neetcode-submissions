class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        pointers = [0] * m

        while True:
            # get max_val from the current num in each row
            max_val = mat[0][pointers[0]]
            for i in range(m):
                if mat[i][pointers[i]] > max_val:
                    max_val = mat[i][pointers[i]]
                
            # move up ptrs less than max_val
            for i in range(m):
                while pointers[i] < n and mat[i][pointers[i]] < max_val:
                    pointers[i] += 1
                if pointers[i] == n:
                    return -1

            # check if all nums equals
            all_equal = True
            for i in range(m): 
                if mat[i][pointers[i]] != max_val:
                    all_equal = False
                    break
            
            if all_equal:
                return max_val
