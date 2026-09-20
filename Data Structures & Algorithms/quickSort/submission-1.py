# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # trigger quick sort in place
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], left:int, right:int):
        # base case: point same element or cross over 
        if left >= right:
            return
        # define pivot at last element
        pivot = pairs[right]
        i = left
        # iterate each ele in partition[left:right]
        for j in range(left, right):
            # check the j element smaller than pivot
            if pairs[j].key < pivot.key:
                # if yes, swap the i and j element
                pairs[i], pairs[j] = pairs[j], pairs[i]
                # after swapping must increment i forward
                i += 1
        # i is now the correct pivot point, swap current pivot with new pivot
        pairs[i], pairs[right] = pairs[right], pairs[i]
        # use new pivot to recursively call left and right pile
        self.quickSortHelper(pairs, left, i-1) # current left up to just before pivot 
        self.quickSortHelper(pairs, i+1, right) # one after pivot up to right wall
        
