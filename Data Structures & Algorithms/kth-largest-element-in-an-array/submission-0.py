class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSelect(nums, 0, len(nums)-1, k)
        return nums[len(nums)-k]
    
    def quickSelect(self, nums, left, right, k):
        if left >= right:
            return
        
        pivot = nums[right]
        i = 0
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # swap pivot to new separation point
        nums[right], nums[i] = nums[i], nums[right]

        if i == len(nums) - k: # kth largest
            return
        elif i > len(nums) - k:
            self.quickSelect(nums, left, i-1, k) # search left, throw right pile
        else:
            self.quickSelect(nums, i+1, right, k) # search right, throw left pile
        