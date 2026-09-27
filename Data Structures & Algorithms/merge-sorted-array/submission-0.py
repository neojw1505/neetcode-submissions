class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #  nums1 = [10,20,10,20,20,40], nums2 = [1,2]
        #                       ^   ^            ^
        
        n1 = m-1
        n2 = n-1
        tail = m+n-1

        while n1 >= 0 and n2 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[tail] = nums1[n1]
                tail -= 1
                n1 -= 1
            else:
                nums1[tail] = nums2[n2]
                tail -= 1
                n2 -= 1
        
        while n2 >= 0:
            nums1[tail] = nums2[n2]
            tail -= 1
            n2 -= 1
        

            
            

