class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = collections.defaultdict(list)
        for word in strs:
            unique_key = [0] * 26
            for ch in word:
                idx = ord(ch) - ord('a')
                unique_key[idx] += 1
            mapp[tuple(unique_key)].append(word)
        return list(mapp.values())

