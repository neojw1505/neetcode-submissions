class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for s in strs:
            len_str = len(s)
            encoded_strs.append(str(len_str)+"#"+s)
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_word = int(s[i:j])
            word = s[j+1:j+len_word+1]
            res.append(word)
            i = j + len_word + 1 # jump to next word
        return res