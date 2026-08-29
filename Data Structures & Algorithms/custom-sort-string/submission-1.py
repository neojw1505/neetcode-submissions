class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_map = collections.Counter(s)
        res = []
        for ch in order: # O(n) n = length of order
            if ch in count_map:
                repeat_times = count_map[ch]
                for _ in range(repeat_times): # O(k) k = times to repeat
                    res.append(ch)
                del count_map[ch]
        # append remaining values
        for k,v in count_map.items():
            for _ in range(v):
                res.append(k)
        return ''.join(res)
    # T:O(n * k), S:O(n + k)
