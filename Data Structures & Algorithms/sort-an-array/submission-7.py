class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # iterative
        n = len(nums)
        chunk_size = 1
        while chunk_size < n:
            for i in range(0, n, chunk_size * 2):
                p1 = nums[i : i+chunk_size]
                p2 = nums[i+chunk_size: i+chunk_size * 2]
                nums[i:i+chunk_size * 2] = self.merge(p1, p2)
            chunk_size *= 2
        return nums
    
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
        # extend remaining
        tmp.extend(p1[i:])
        tmp.extend(p2[j:])
        return tmp