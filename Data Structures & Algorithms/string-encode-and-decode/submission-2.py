class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # soln: <len><delimiter><string>
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res 

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res 