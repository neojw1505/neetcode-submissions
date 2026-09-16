# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        l1 = self.mergeSort(pairs[:m])
        l2 = self.mergeSort(pairs[m:])
        return self.merge(l1,l2)
    
    def merge(self, l1, l2):
        out = []
        i = 0 
        j = 0
        while i < len(l1) and j < len(l2):
            k1 = l1[i].key
            k2 = l2[j].key
            if k1 <=k2:
                out.append(l1[i])
                i += 1
            else:
                out.append(l2[j])
                j += 1
        while i < len(l1):
            out.append(l1[i])
            i += 1
        while j < len(l2):
            out.append(l2[j])
            j += 1
        return out
