class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapp = defaultdict(list)
        for word in strs:
            unqiue_key = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                unqiue_key[idx] += 1
            mapp[tuple(unqiue_key)].append(word)
        return list(mapp.values())
