class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search soln T:O(nlogn) S:O(1)
        # step1 sub arr
        sub = []
        # step 2 loop 
        for num in nums:
            # step 3 binary search
            l,r = 0,len(sub)-1
            while l <= r:
                m = (l+r)//2
                if sub[m] < num:
                    l = m + 1
                else:
                    r = m - 1
            
            # step 4 check left pointer
            if l == len(sub): # append to sub
                sub.append(num)
            else: # replace 
                sub[l] = num
        return len(sub)