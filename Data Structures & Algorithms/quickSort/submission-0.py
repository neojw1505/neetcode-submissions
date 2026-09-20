# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    


    def quickSortHelper(self, pairs, left, right):
        if left >= right: 
            return 
        pivot = pairs[right]
        i = left 
        for j in range(left, right):
            if pairs[j].key < pivot.key:
                # swap 
                pairs[j], pairs[i] = pairs[i], pairs[j]
                i += 1 # move pointer forward
        
        # swap pivot (pairs[right]) with i, because i is the correct separation point
        pairs[i], pairs[right] = pairs[right], pairs[i]
        # slicing
        self.quickSortHelper(pairs, left, i-1) # left pile
        self.quickSortHelper(pairs, i+1, right) # right pile