class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        half = len(nums) // 2
        p1 = self.sortArray(nums[:half])
        p2 = self.sortArray(nums[half:])
        return self.merge(p1,p2)
    
    def merge(self, p1, p2):
        i = 0
        j = 0
        tmp = []
        while i < len(p1) and j < len(p2):
            if p1[i] < p2[j]:
                tmp.append(p1[i])
                i += 1
            else:
                tmp.append(p2[j])
                j += 1
        # add remaining      
        tmp.extend(p1[i:])
        tmp.extend(p2[j:])
        return tmp