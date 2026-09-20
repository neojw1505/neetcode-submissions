class Solution:
    # T: O(n)
    # S: O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        self.quickSelect(nums, 0, len(nums)-1, target)
        return nums[len(nums) - k]
    
    def quickSelect(self, nums, left, right, target):
        # base case
        if left >= right:
            return
        # define pivot
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # swap pivot to new separation point
        nums[right], nums[i] = nums[i], nums[right]

        if i == target: # kth largest
            return
        elif i > target:
            self.quickSelect(nums, left, i-1, target) # search left, throw right pile
        else:
            self.quickSelect(nums, i+1, right, target) # search right, throw left pile
        