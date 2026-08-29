class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Index-Based Merge Sort uses less memory but more complex
        def merge(arr, l, m, r):
            Left, Right = arr[l:m+1], arr[m+1:r+1] 
            # 3 ptrs i -> left half, j -> right half, k -> arr
            i,j,k = 0,0,l
            while i < len(Left) and j < len(Right):
                if Left[i] < Right[j]:
                    arr[k] = Left[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = Right[j]
                    j += 1
                    k += 1
            # check leftover Left
            while i < len(Left):
                arr[k] = Left[i]
                i += 1
                k += 1
            # check leftover Right
            while j < len(Right):
                arr[k] = Right[j]
                j += 1
                k += 1
            return arr
        # merge sort
        def mergeSort(arr, l, r):
            # base case
            if l == r:
                return arr
            # recursive case:
            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr,l,m,r)
            return arr
        return mergeSort(nums,0,len(nums)-1)
        