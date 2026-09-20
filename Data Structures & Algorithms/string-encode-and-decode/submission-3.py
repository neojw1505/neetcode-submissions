class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += len(s) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while j != "#":
                j += 1
            length = s[i:j]
            word = s[j+1: j+1+length]
            res.append(word)
            i = j + 1 + length
        return res