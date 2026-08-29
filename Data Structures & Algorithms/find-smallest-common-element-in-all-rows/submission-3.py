class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        pointers = [0] * m
        max_val = mat[0][0]
        while True:
            # step 1: find max_val in current pointers
            for i in range(1, m):
                max_val = max(max_val, mat[i][pointers[i]])
            
            # step 2: update pointers less than max_val
            for i in range(m):
                while mat[i][pointers[i]] < max_val:
                    pointers[i] += 1
                if pointers[i] == n: # exhausted that row
                    return -1
            
            # step 3: check if pointer are all equal
            all_equal = True
            for i in range(m):
                if mat[i][pointers[i]] != max_val:
                    all_equal = False
                    break

            if all_equal:
                return max_val