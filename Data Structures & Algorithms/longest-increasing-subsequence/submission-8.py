class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: # no numbers -> LIS = 0
            return 0 
        board = []
        for x in nums:
            left, right = 0, len(board) # not len(board)-1 because the ans can be an index out of the board
            while left < right:
                mid = (left + right) // 2
                if board[mid] >= x: # find first num bigger than x, potential slot to replace with x
                    right = mid
                else:
                    left = mid + 1 # value too small, look right
            idx = left
            if idx == len(board): # APPEND
                board.append(x)
            else:
                board[left] = x # REPLACE 
            return len(board)
    
    # T:O(nlogn) S:O(k)


