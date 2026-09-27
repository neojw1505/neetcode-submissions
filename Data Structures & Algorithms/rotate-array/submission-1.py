class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def swap(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # expected: [5,6,7,8 | 1,2,3,4]
        swap(0, n-1) # [8,7,6,5,| 4,3,2,1] 
        swap(0, k-1) # [5,6,7,8,| 4,3,2,1] 
        swap(k, n-1) # [5,6,7,8,| 1,2,3,4] 
        """
        3 reverse trick
        - reverse entire array 
        - reverse first k elements
        - reverse from k+1 elements
        """
