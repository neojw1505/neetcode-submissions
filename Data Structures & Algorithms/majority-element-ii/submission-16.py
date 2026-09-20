class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0
    
        for i, num in enumerate(nums):
            if candidate1 is None:
                candidate1 = num
                count1 += 1 
                continue
            if candidate2 is None and num != candidate1:
                candidate2 = num
                count2 += 1
                continue
            
            if num == candidate1:
                count1 += 1
                continue
            if num == candidate2:
                count2 += 1
                continue
            # if see a third number
            count1 -= 1
            count2 -= 1
            if count1 == 0: 
                candidate1 = num # replaced with the number that kicked it out
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
        
        res = []
        n = len(nums)

        actual1 = 0
        actual2 = 0

        for num in nums:
            if num == candidate1:
                actual1 += 1
            if num == candidate2:
                actual2 += 1

        if candidate1 is not None and actual1 > n//3:
            res.append(candidate1)
        if candidate2 is not None and actual2 > n//3:
            res.append(candidate2)
        return res