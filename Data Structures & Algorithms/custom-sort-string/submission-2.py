class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_map = collections.Counter(s)
        res = []
        for ch in order: # O(n) n = length of order
            if ch in count_map:
                res.append(ch * count_map[ch])
                del count_map[ch]
        # append remaining values
        for k,v in count_map.items():
            res.append(k * v)
        return ''.join(res)
    # T:O(n * k), S:O(n + k)
