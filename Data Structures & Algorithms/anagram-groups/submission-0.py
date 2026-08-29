class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            if tuple(key) in d:
                d[tuple(key)].append(s)
            else:
                d[tuple(key)] = [s]
        
        return d.values()