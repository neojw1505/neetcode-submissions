class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for word in strs:
            encoded_strs.append(str(len(word)) + "#" + word)
        return ''.join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_word = int(s[i:j])
            word = s[j+1:j+1+len_word]
            res.append(word)
            i = j+1+len_word
        return res

        
